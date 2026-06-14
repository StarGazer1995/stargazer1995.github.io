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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBBK7GXV%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T225911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDUqqBbwCntoP5k0%2Fx%2BB8nPeYK5W6c9Vz3nEjwmPs93AIgZ%2BnZec%2Be9rZWvUOFhc6oxPLkkeofp1B2H0WTq09gcgwq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDKYqi9FRYwhWWZSzCSrcAwMRsOn1GIiCjmUffPuwRZOhETSNH8unRu5Jdra4Z8YqSK9Co8rd1uGTYpwvo3hvVIosLWuHnkVxqjBgKuB0sklqEtm%2Bg2TIHMbOTlTjeb0XLrFDro4AB%2BTC%2BLmFJ5SW6B9BP00z3f7f2OmtnxUwYaep8pvh7qUa8ROrExV%2B7VsP4XcHIPWI22EJ513WysZJF8iO55fWh%2FuNdvkr7KZ0bNxZs7bJCsp4autyefY7us3MpkcvQ%2B%2B6P%2FWm0PM4un7FenLeoG4hWoArUl6gq70wlRKxK1wo3eW6qXwIUMJ4vcFm57sioeBGRG0A8MyGiuBCLAu43V5xiYVF95XGNZDjZfjNHxFdhYxKwyYPAfGg1%2BRBTGuAJq4ka1Hln1N8gIdCPZ53ZpTrm4tZLLKXakn661dtH2L6FU9O7mYP5uNO%2BnLl7Fr1IvdYdZeE%2FnXLncmm83oN5Y76D%2BzxfKtsdTwVCss5kbsJ35xEtLmXVRZwWbNzP6iL27TFZz7bSAs9l1rdE0u0wXvQVgdkWsdBnxF4gNgquiDEUW3Z1TSR1Gsx9p%2F9DIrrz%2B1mpQ7mYp%2FkFdxGonoMPSrzhf3MclPJ8bMTNA8o%2BmrFR3lZc39RIZmW7f5iPYYFk1Vf7eJL8IkAMMKVvNEGOqUB1tkFhAbNAlBghM0DcXuT%2BGrXrNvo7YwQ3sWMJWUxnuNoS6rh5Cr9oHnJOYGmXWWcfSEINzQ5p0EUFltXQmDRkbQNXpfwu%2FbclAvLMvnHeYVI8T6%2BjBp0cCDoBnDSqdl1KpEMen8FiELXKU2a%2Fm6krOIDOIvf%2FkEi7fE9Hd3N2f6JMQ5yQfCfM5Lf%2FfDumJR9H%2FtxONi%2Bfv0TEPaN3DVCDZEiMKSP&X-Amz-Signature=48b5d8432e43b9e76477f20338d500bd14996ead88ce7f590698648d49c7b865&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBBK7GXV%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T225911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDUqqBbwCntoP5k0%2Fx%2BB8nPeYK5W6c9Vz3nEjwmPs93AIgZ%2BnZec%2Be9rZWvUOFhc6oxPLkkeofp1B2H0WTq09gcgwq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDKYqi9FRYwhWWZSzCSrcAwMRsOn1GIiCjmUffPuwRZOhETSNH8unRu5Jdra4Z8YqSK9Co8rd1uGTYpwvo3hvVIosLWuHnkVxqjBgKuB0sklqEtm%2Bg2TIHMbOTlTjeb0XLrFDro4AB%2BTC%2BLmFJ5SW6B9BP00z3f7f2OmtnxUwYaep8pvh7qUa8ROrExV%2B7VsP4XcHIPWI22EJ513WysZJF8iO55fWh%2FuNdvkr7KZ0bNxZs7bJCsp4autyefY7us3MpkcvQ%2B%2B6P%2FWm0PM4un7FenLeoG4hWoArUl6gq70wlRKxK1wo3eW6qXwIUMJ4vcFm57sioeBGRG0A8MyGiuBCLAu43V5xiYVF95XGNZDjZfjNHxFdhYxKwyYPAfGg1%2BRBTGuAJq4ka1Hln1N8gIdCPZ53ZpTrm4tZLLKXakn661dtH2L6FU9O7mYP5uNO%2BnLl7Fr1IvdYdZeE%2FnXLncmm83oN5Y76D%2BzxfKtsdTwVCss5kbsJ35xEtLmXVRZwWbNzP6iL27TFZz7bSAs9l1rdE0u0wXvQVgdkWsdBnxF4gNgquiDEUW3Z1TSR1Gsx9p%2F9DIrrz%2B1mpQ7mYp%2FkFdxGonoMPSrzhf3MclPJ8bMTNA8o%2BmrFR3lZc39RIZmW7f5iPYYFk1Vf7eJL8IkAMMKVvNEGOqUB1tkFhAbNAlBghM0DcXuT%2BGrXrNvo7YwQ3sWMJWUxnuNoS6rh5Cr9oHnJOYGmXWWcfSEINzQ5p0EUFltXQmDRkbQNXpfwu%2FbclAvLMvnHeYVI8T6%2BjBp0cCDoBnDSqdl1KpEMen8FiELXKU2a%2Fm6krOIDOIvf%2FkEi7fE9Hd3N2f6JMQ5yQfCfM5Lf%2FfDumJR9H%2FtxONi%2Bfv0TEPaN3DVCDZEiMKSP&X-Amz-Signature=404e9d0d9ed09006c75ee387f673a5ad33e2f678813aa5dac8ab6adb019d467d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
