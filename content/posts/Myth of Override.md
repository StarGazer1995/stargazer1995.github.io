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
cover: https://app.notion.com/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJHEBVM%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T075121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEQ7sxW66A3OaAEbCd27dPR17VcCONxEMbd4TY2NcjcTAiAaM3BbirV%2Ff%2FWkY4BebJ2w9QY0FXDMpDM70786OAgW9yr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIM6n2Zbe4NmblWUy3EKtwDHWxa5AcUvQnGb8bUDAWIAyl%2FuQOlKqmsP0gCQKdPPqjsFfaRb0Kr6kpkHDKTiSKxybgaecNdUbX5n6L7a1Qa62FdGCyHeXfklH4R5DQhjT2%2Bsox0zWdNglkebk7IX9HBEPVde7x6dw%2BqqEPdd0OEgG1YZRiOlbyjM8qNDIlRRvaVKYU9igiZFARyyD51013uWvV2hCBPpMAnocLARM2ao72RNFFv8qEUG31yXhudoGpNXIC7sGlQA%2FjV%2BEKEhEJEpT%2FzA9%2FbecCiNIvnYV1VeMxrXNST7cHeKYfUUZ%2FI4OzDA9Bn6DIllvcaJoW7RV%2BBJJ%2Bjodq31NjTvUqWyJ3s2PzUiJ0wn7LYU7YaT1hzKZa63Qft%2F6%2BOaJVINMOh6sPiPOz4bR9lNNUrLZorWHvkEzy6uI1A8i4K1PwGIY6E14NL3jEoDvbXfBe6VZea2IdzZUQS5KsJjhXG%2B51HwTl8cwveR8iXm99eYmVu2wh3rytp9arppzvRH2XEjM6n0JJ1j6dl%2BVX6bVk%2BJ0WqoWPMoF3cMYF0ipG3YirZC8N3v5JIYR7S74%2Fg62MKnII3TrpbCZ5ojC8b8toz3FMe0SiufnIcT8Pbo0GL0WgfM4%2B7y2R%2BHLhLjh8cUWwpyREwtran1gY6pgFI7oKbce3ZINoN%2Fg10mWWyRXTy8IOz80e0lc2%2FmK1QsvEKd%2Bmab%2BlB9tGL5RpKO9PbobZQO%2FPYt5DBOD%2FxT9wACaYCjJkE5ifLA5EbLkHXb1RgyyDLlvYzFNwp0S7%2FosuvuH78AWAU0EUseaMb0%2B6%2FP2pf7yuVcVf%2F%2BJ11oiuIxwAhQPqmciMW5Hp1ReblHV%2BBqmnHiOEjvcvDM4hXNHlQf65DE8vG&X-Amz-Signature=fea595d2300f92c4f72f8ce82e72879be62502d824be3f62bd264cf7e503c5cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUJHEBVM%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T075121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEQ7sxW66A3OaAEbCd27dPR17VcCONxEMbd4TY2NcjcTAiAaM3BbirV%2Ff%2FWkY4BebJ2w9QY0FXDMpDM70786OAgW9yr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIM6n2Zbe4NmblWUy3EKtwDHWxa5AcUvQnGb8bUDAWIAyl%2FuQOlKqmsP0gCQKdPPqjsFfaRb0Kr6kpkHDKTiSKxybgaecNdUbX5n6L7a1Qa62FdGCyHeXfklH4R5DQhjT2%2Bsox0zWdNglkebk7IX9HBEPVde7x6dw%2BqqEPdd0OEgG1YZRiOlbyjM8qNDIlRRvaVKYU9igiZFARyyD51013uWvV2hCBPpMAnocLARM2ao72RNFFv8qEUG31yXhudoGpNXIC7sGlQA%2FjV%2BEKEhEJEpT%2FzA9%2FbecCiNIvnYV1VeMxrXNST7cHeKYfUUZ%2FI4OzDA9Bn6DIllvcaJoW7RV%2BBJJ%2Bjodq31NjTvUqWyJ3s2PzUiJ0wn7LYU7YaT1hzKZa63Qft%2F6%2BOaJVINMOh6sPiPOz4bR9lNNUrLZorWHvkEzy6uI1A8i4K1PwGIY6E14NL3jEoDvbXfBe6VZea2IdzZUQS5KsJjhXG%2B51HwTl8cwveR8iXm99eYmVu2wh3rytp9arppzvRH2XEjM6n0JJ1j6dl%2BVX6bVk%2BJ0WqoWPMoF3cMYF0ipG3YirZC8N3v5JIYR7S74%2Fg62MKnII3TrpbCZ5ojC8b8toz3FMe0SiufnIcT8Pbo0GL0WgfM4%2B7y2R%2BHLhLjh8cUWwpyREwtran1gY6pgFI7oKbce3ZINoN%2Fg10mWWyRXTy8IOz80e0lc2%2FmK1QsvEKd%2Bmab%2BlB9tGL5RpKO9PbobZQO%2FPYt5DBOD%2FxT9wACaYCjJkE5ifLA5EbLkHXb1RgyyDLlvYzFNwp0S7%2FosuvuH78AWAU0EUseaMb0%2B6%2FP2pf7yuVcVf%2F%2BJ11oiuIxwAhQPqmciMW5Hp1ReblHV%2BBqmnHiOEjvcvDM4hXNHlQf65DE8vG&X-Amz-Signature=1cdbbfa5f315e67c5b3b0b1f4e9c6c378f2447dc08ace5e8e6e3a4045a054917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
