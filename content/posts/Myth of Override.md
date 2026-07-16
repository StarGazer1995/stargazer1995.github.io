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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSDIWYXB%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T112559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIEI20yPf89jm%2F0mYuwTxWzIJhQPYgLuT8CUqvGp4kSUwAiEA9mWLH%2FwQ3vI1zhfXDFhh%2BAgaAthfbOoClYZ6GWAjMqMq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDCaP1Xr2etCCKUqoaCrcA6KdwBovQXSe68SMBa6q0OJ8T4a4p%2BOgvvQoXUJ3TiDBJU0D%2BHXf48DFfaIzjgkRioK75WZqSjnaj4zHdxAp%2BqqafkWn3FUYEbwIAeEyGMh2fwafr%2F03DjLmibZ2y%2BmL3VBJS1%2BUJMWPhhg2IRlS9kgvlEO4%2FlDE0RG3ndAPJ63acDfeT5jsu6fiUSaXvyMEWCZiXC5DN%2B7%2BFZz3cImp18TEFTTgnUtKTb6ApnH0UrEAJ1gwCZMOQm5cEcukCfnqWYYl3%2FviUnAcWkVc3e%2BlBPaYnM39%2BhJna%2FAXEuErC2%2Bu9HHb%2FrKT5vrHpyY4jZZJtDi1akQYzdA4W7%2B8vSGajmUt3RysewfzIi9DAafiLOajlNXMPSzYO6lY5AzUDSy396PwTp1GPWsAL8JPejt0Iq%2BiQww2FbUICsyFfYBkF6RpAqMOu%2FKlQwOLDigZrRj4IesSaIUwrgRnt%2ByWVDIzvVSxf54zthi48%2Fddvn75NYKXNEvnrYguT8Kif9%2FNJzuR1gld9Z3MFk9MlX9E3MjGaEQ4EePCNKUWPpHxbE6%2F7e1jIPCtpj%2Bki5pYTOoWrIzdd62NYMJ2c5OspiTfzAx74gohKCa49ASDL33gsqsRCyIUdYqg2%2BK4K31hvEB%2FMLjd4tIGOqUBEhNxnkK5M0OBWbv1NfEnzvEZyq8Oij%2F5uD7Xr0g%2Bol0ws%2FCiKhpVjIJZcztQR62OU8zbldMWxU%2FJIxoMMDk4EjHeYGBfaufnMY2QoEDHCesn5K4c4TDe8gnbDOVL3fWLerXQ0R%2B4wMNWwo88ns9etTvV%2B226N4uVMPz0AyEJZKYfB%2BEIeT1tRlVWTLIu8z41YCvI8xS4Dd9tlZW9aJzZB6Oe1XOf&X-Amz-Signature=f43bf7b0e0f08b558f9218b50eabf7b3cb6528a005d540bc030fd0659703800a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSDIWYXB%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T112559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIEI20yPf89jm%2F0mYuwTxWzIJhQPYgLuT8CUqvGp4kSUwAiEA9mWLH%2FwQ3vI1zhfXDFhh%2BAgaAthfbOoClYZ6GWAjMqMq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDCaP1Xr2etCCKUqoaCrcA6KdwBovQXSe68SMBa6q0OJ8T4a4p%2BOgvvQoXUJ3TiDBJU0D%2BHXf48DFfaIzjgkRioK75WZqSjnaj4zHdxAp%2BqqafkWn3FUYEbwIAeEyGMh2fwafr%2F03DjLmibZ2y%2BmL3VBJS1%2BUJMWPhhg2IRlS9kgvlEO4%2FlDE0RG3ndAPJ63acDfeT5jsu6fiUSaXvyMEWCZiXC5DN%2B7%2BFZz3cImp18TEFTTgnUtKTb6ApnH0UrEAJ1gwCZMOQm5cEcukCfnqWYYl3%2FviUnAcWkVc3e%2BlBPaYnM39%2BhJna%2FAXEuErC2%2Bu9HHb%2FrKT5vrHpyY4jZZJtDi1akQYzdA4W7%2B8vSGajmUt3RysewfzIi9DAafiLOajlNXMPSzYO6lY5AzUDSy396PwTp1GPWsAL8JPejt0Iq%2BiQww2FbUICsyFfYBkF6RpAqMOu%2FKlQwOLDigZrRj4IesSaIUwrgRnt%2ByWVDIzvVSxf54zthi48%2Fddvn75NYKXNEvnrYguT8Kif9%2FNJzuR1gld9Z3MFk9MlX9E3MjGaEQ4EePCNKUWPpHxbE6%2F7e1jIPCtpj%2Bki5pYTOoWrIzdd62NYMJ2c5OspiTfzAx74gohKCa49ASDL33gsqsRCyIUdYqg2%2BK4K31hvEB%2FMLjd4tIGOqUBEhNxnkK5M0OBWbv1NfEnzvEZyq8Oij%2F5uD7Xr0g%2Bol0ws%2FCiKhpVjIJZcztQR62OU8zbldMWxU%2FJIxoMMDk4EjHeYGBfaufnMY2QoEDHCesn5K4c4TDe8gnbDOVL3fWLerXQ0R%2B4wMNWwo88ns9etTvV%2B226N4uVMPz0AyEJZKYfB%2BEIeT1tRlVWTLIu8z41YCvI8xS4Dd9tlZW9aJzZB6Oe1XOf&X-Amz-Signature=d574813e137a8b958580c5c50e6758209305de0f22c5e08ffeac318f25c6c8a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
