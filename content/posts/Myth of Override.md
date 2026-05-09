---
created: 2024-07-04T01:57:00+00:00
categories:
  - Blog
tags:
  - Problems
  - Blog
updated: 2024-07-04T02:13:00+00:00
date: 2024-07-04T01:57:00+00:00
title: Myth of Override
cover: https://www.notion.so/images/page-cover/webb1.jpg
id: 6e79f44c-5df9-46d3-bbec-45dc2f724d70
---

# Introduction:

Recently, while acquainting myself with the new company, I encountered a piece of unusual code.

It seems quite straightforward. We start by declaring a base class with a private virtual function, which is then called by a public member function. Next, we derive a class from the base class and override the virtual function. This pattern is known as the Template Pattern. It defines the skeleton of an algorithm but allows subclasses to override specific steps without altering its structure. The code appears sound until we scrutinize the derived class.

```c++
#include<iostream>
#include<memory>

class base {
public:
    base() = default;
    void callPrivateFunction(){
        privateFunction();
    }
private:
    virtual void privateFunction(){
        std::cout<<"The call comes from a private function"<<std::endl;
    }
};

class derived : public base {
public:
    void privateFunction() override {
        std::cout<<"The cal comes from the overrided function"<<std::endl;
    }
};

int main(){
    base *ptr = new derived();
    ptr->callPrivateFunction();

    derived *ptr_derived = new derived();
    ptr_derived->privateFunction();
    return 0;
}
```

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">github.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBZYZD4%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T184258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDijSNU8Df%2B3OxbD81DP5Zctf2Cc3v3DBPdsBc8aPVhtgIgXQkypCBEvD7YwQ0q%2B8CtbqKdiPrw87pxgQ2r3BkAIQUqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB1K99AEuZmbVfHTtCrcA0JlB9CNVeA%2Fk%2BaSPKiSHznrkf98UNE0ODTy1l4oUFY5bFw47l1vdqaodEnKeQEe1bYwBuRDNNditSvPPHwY6qhg2s%2B0E8sk3oHY3U%2Ba%2F0%2BzPRemtZCbgo5zllcODNMihUkH%2FqCSArwcN7fYOkpGn1mkQM3NQV1iyutvN1Bkw9ugVVr31JkoacQW3hmpsb1Rg9bp6yXQlKFKzSDYYt3GcA4C6gLcK%2Bra5JSNlsolrqAFqTJduKf35drMaW0aBdLGU8UuqBuaImeLxC2zeKTZa6qhgRSxpv6au%2FOMLaEajMzwy6HGkNlRHVwWrxfw9plADqQ7aTcnJl5vxfDcgG4GrA1WErI6HPj1XDmwV5SfFeCH5tEduSNXNvMQXDQ7K7CcUEEVVQNFEvGslIBn33lyZOTIhZNaqOTzW822639IAAUYQnnkz4KNl9vPJ%2BZ2O%2BtDwFPKqJrboTUXS%2BM5k5vDpZ%2FZEE8Hj0whFmGqHmQ5j%2FrSOnpqqT7YpdGWBLJ3zBObtmLoplZm5vGii9YVSohnh80vyoC7Qkj6HkTPYDEie%2FYTDlu%2BM6Uv7vKYlY%2BXshFWs0OJSs%2BO0A2C2h%2FT3%2FN%2BhLgjIkmfiUcUInqoiNe0jLEoeEzFEtfvV4GlUC9jMK%2Fa%2Fc8GOqUBDBgOKOnYVClG%2BzCEnCRccJLyNRskUNmYQvV3rLmLEFtRaF60y8iJTnMlv7%2Fx%2FD2pj%2B22LS9idnFF5Cwq8XiGb0buvsHUnJaTjaKVLZZYgR8vR8P4irQFKXsObtpGNy8WAquKHe32ZM1fZSA6W%2BrGJg5HNHHNr8G8YZXn%2BjDyqVuQCvJABQZUBE3pOQkBU%2FpzgEFur2Vyspgr22rF01A2RtDQMt3E&X-Amz-Signature=3140cf60fed8557c3027f0a9571957264e7f9f8f40be6ec1408e5b6f6fc9c3d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBZYZD4%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T184258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDijSNU8Df%2B3OxbD81DP5Zctf2Cc3v3DBPdsBc8aPVhtgIgXQkypCBEvD7YwQ0q%2B8CtbqKdiPrw87pxgQ2r3BkAIQUqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB1K99AEuZmbVfHTtCrcA0JlB9CNVeA%2Fk%2BaSPKiSHznrkf98UNE0ODTy1l4oUFY5bFw47l1vdqaodEnKeQEe1bYwBuRDNNditSvPPHwY6qhg2s%2B0E8sk3oHY3U%2Ba%2F0%2BzPRemtZCbgo5zllcODNMihUkH%2FqCSArwcN7fYOkpGn1mkQM3NQV1iyutvN1Bkw9ugVVr31JkoacQW3hmpsb1Rg9bp6yXQlKFKzSDYYt3GcA4C6gLcK%2Bra5JSNlsolrqAFqTJduKf35drMaW0aBdLGU8UuqBuaImeLxC2zeKTZa6qhgRSxpv6au%2FOMLaEajMzwy6HGkNlRHVwWrxfw9plADqQ7aTcnJl5vxfDcgG4GrA1WErI6HPj1XDmwV5SfFeCH5tEduSNXNvMQXDQ7K7CcUEEVVQNFEvGslIBn33lyZOTIhZNaqOTzW822639IAAUYQnnkz4KNl9vPJ%2BZ2O%2BtDwFPKqJrboTUXS%2BM5k5vDpZ%2FZEE8Hj0whFmGqHmQ5j%2FrSOnpqqT7YpdGWBLJ3zBObtmLoplZm5vGii9YVSohnh80vyoC7Qkj6HkTPYDEie%2FYTDlu%2BM6Uv7vKYlY%2BXshFWs0OJSs%2BO0A2C2h%2FT3%2FN%2BhLgjIkmfiUcUInqoiNe0jLEoeEzFEtfvV4GlUC9jMK%2Fa%2Fc8GOqUBDBgOKOnYVClG%2BzCEnCRccJLyNRskUNmYQvV3rLmLEFtRaF60y8iJTnMlv7%2Fx%2FD2pj%2B22LS9idnFF5Cwq8XiGb0buvsHUnJaTjaKVLZZYgR8vR8P4irQFKXsObtpGNy8WAquKHe32ZM1fZSA6W%2BrGJg5HNHHNr8G8YZXn%2BjDyqVuQCvJABQZUBE3pOQkBU%2FpzgEFur2Vyspgr22rF01A2RtDQMt3E&X-Amz-Signature=00a0fa367a338490e2cef3a664d4ebe9d15de29b83e32e63fee5b11c98cf08ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
