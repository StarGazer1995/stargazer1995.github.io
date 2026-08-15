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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4C7VFL%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T061906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIDWjKv6XvR4WGKO95ekbBKgHWvjbiEJ1dedA320g9%2B21AiB41Ee9LCcCL8sOw2isbBqiM851N3nIOaOhgc5QydWD1ir%2FAwgPEAAaDDYzNzQyMzE4MzgwNSIMRs25ldyWey6Im3Y2KtwDYUjbyWjybOGrdEXhsa5boR%2Fw2%2Bc9k5jPorU5cRbLdgECA%2B%2Foet5LB2%2BmW%2BHvUecquYcIoX1b5nW28vmoKWtqWjN7Xa5nYaeBO%2FnOCfXvk1n%2FZg5J0E7CmlQeo26fkchmGSa6Yg6yYTQA2OjVjmU49dsNWhauazSlGoGD2P9G9QzkgI71s36XoHyNBzImRCGmKouHqht8JsNQnbnavgnSuAxBIeO8CeACr5j4BNiQOh8TA%2B4u0BWsDSP5E5J0MBPfvAS2dZs%2BkpJ%2B9mgREpWc19MqLpibKZwLqN614gNBzUQABOATtxlnsP4sjRppeWMs0dhStKUZQSQBco10SlywdwzyOr8AXgxzMnP3e3ZOnJYZtxNmczRENDK6tw%2BIOagoFPgux%2FFrR2r%2BOmw9bv%2BhxSHi6bPNL66RkjPAQjTQQMhNvLmYBT7fYZR2ZMWkUNtH4kc9txh6J%2BSOdziyg406%2FV1L4qJWvb4D8KDZMO0QoXKC9L0B9RErqXE9GkcfsH8evtnstmBqmvlVj3PLR0WNP3EAZUQvOa%2Bp%2F8LppP36CygiY2td06W8wKaVhY1rgiomKKz0MnWwVnckySHYfK%2FNr0XSMmnJ2V1R0F1cwehzR%2BSjQwxhwQiLhAdJqrgw9IGA1AY6pgGJITlE74b2dD%2BHO4dJXdg0Gu%2FVgPYStAlZR53fS99usswe9V8ODvNu1moJ1wvmGRoJJ%2FA%2BDR8fDqidvybIhi2vG91NY6se9oX1zBpQpo%2BVbFeLUtXwZwHbzkaUbWNn4DzMmwfX8qIGUiJBndblH6ZLD2cypPTXvkVVgqQPtyWHreR6RMC29cjx1AvEGZSIdF5EIvyEgLfqB6RcomRozeglc9Nve%2Bv%2B&X-Amz-Signature=0a7491eb3b57ee3793c21fc6ac6012be64b03a00fb5a5a677cd381a6a2cad724&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4C7VFL%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T061906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIDWjKv6XvR4WGKO95ekbBKgHWvjbiEJ1dedA320g9%2B21AiB41Ee9LCcCL8sOw2isbBqiM851N3nIOaOhgc5QydWD1ir%2FAwgPEAAaDDYzNzQyMzE4MzgwNSIMRs25ldyWey6Im3Y2KtwDYUjbyWjybOGrdEXhsa5boR%2Fw2%2Bc9k5jPorU5cRbLdgECA%2B%2Foet5LB2%2BmW%2BHvUecquYcIoX1b5nW28vmoKWtqWjN7Xa5nYaeBO%2FnOCfXvk1n%2FZg5J0E7CmlQeo26fkchmGSa6Yg6yYTQA2OjVjmU49dsNWhauazSlGoGD2P9G9QzkgI71s36XoHyNBzImRCGmKouHqht8JsNQnbnavgnSuAxBIeO8CeACr5j4BNiQOh8TA%2B4u0BWsDSP5E5J0MBPfvAS2dZs%2BkpJ%2B9mgREpWc19MqLpibKZwLqN614gNBzUQABOATtxlnsP4sjRppeWMs0dhStKUZQSQBco10SlywdwzyOr8AXgxzMnP3e3ZOnJYZtxNmczRENDK6tw%2BIOagoFPgux%2FFrR2r%2BOmw9bv%2BhxSHi6bPNL66RkjPAQjTQQMhNvLmYBT7fYZR2ZMWkUNtH4kc9txh6J%2BSOdziyg406%2FV1L4qJWvb4D8KDZMO0QoXKC9L0B9RErqXE9GkcfsH8evtnstmBqmvlVj3PLR0WNP3EAZUQvOa%2Bp%2F8LppP36CygiY2td06W8wKaVhY1rgiomKKz0MnWwVnckySHYfK%2FNr0XSMmnJ2V1R0F1cwehzR%2BSjQwxhwQiLhAdJqrgw9IGA1AY6pgGJITlE74b2dD%2BHO4dJXdg0Gu%2FVgPYStAlZR53fS99usswe9V8ODvNu1moJ1wvmGRoJJ%2FA%2BDR8fDqidvybIhi2vG91NY6se9oX1zBpQpo%2BVbFeLUtXwZwHbzkaUbWNn4DzMmwfX8qIGUiJBndblH6ZLD2cypPTXvkVVgqQPtyWHreR6RMC29cjx1AvEGZSIdF5EIvyEgLfqB6RcomRozeglc9Nve%2Bv%2B&X-Amz-Signature=c6f9f998591693f3ed1e424410138ffae5705c19597664f9b16b10c170b2bf9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
