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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6VLSGEK%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T215314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDNjHEmPf4YH%2B2mQjfMO%2FUV0hk7qGUIR2r3kvrqtQ61WAiB34lGY7yCgEF8YWMcBlu9e9elqCp%2BKBiHfD0Pr7eD5bCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMwltRIxnq0CNfx2%2BdKtwDyANzJ9HLBB%2Bq7SPn6T6RTO61wz40iO0UNT86vEkpUeUlVJB6d1X9w2%2FCWCs8GTEUgd0nhp3BHXR6de7GctgjSI3ZNmD3kMpS%2BOz1fKfw%2FkbYsBp45UUM2ChG1AIWX6uxNJytW%2FLbQ6xowGkj2TGVOkV7Rm2bAAgd9NUa2tTQkmw9dopFleGE1iHvFfG0pxVY%2BCZIIE7YkHQvNn8JOUrDDNGZiRf%2F3ieAN2ZGX5s6jeHqEdaYDa%2BYQ6hPhDKj2mFe%2FuCiBR%2FMKSrPcZPJ2bmwHEpW9TzDX2YRPyjz5ZY9tg2bIJv42ULg1sXfFmVBVEMkqR7mBh7xtCgX%2BDI7w7nxkyElxBaGQf2NWzvfKq80WvCfBJru9izqBhz3dF0dyhwZgxx2K%2FKc8wVLwXVQwRipY2WNnYrVYStgWAxxpK6U%2BaS4SyMiGn6FxR5K6ryIQm4m2lWSuEQkZx6ycWillI82sjQWHK1YAQ5w47VWie%2F5hq%2FDLnRcDROp9rNCWXsQbg3kQeeT64DX7yDFzu6DPgZoELXCV9wb3PkeFRfApFzcnATiyUE2kb4ZVdpeaenyY%2B5Cq922oL2lZiCuqgs9XOQODcxe%2Fzu4xpPLgMr6tUslKcOIBt%2F2sbOShmE6VaYwzLC71QY6pgHWD4bN24T%2BpYRcH0ZGSshiZVx2%2BcVFMQ9e0LXV7cA%2Bxp42MzEx%2B2AkGOYhus9SrG%2BmyeaFrZiJfutzrUCrorqDiZiBC7b883Z12lnVHrWIOD00cRtpSbOqFjVd4kbOJ0NHyUEafP3aHq1RfApYMouhlKeKKKuvtpyaKgWl7DmWIwsLd92dNDa5WmISSIhDsPnRINF9XxBTCDiJhQPYkjyEt9y6nbiY&X-Amz-Signature=6dee1b812638e377ffe3c688d07050acb5d2da854ba002ff75813ab51a8ec530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6VLSGEK%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T215314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDNjHEmPf4YH%2B2mQjfMO%2FUV0hk7qGUIR2r3kvrqtQ61WAiB34lGY7yCgEF8YWMcBlu9e9elqCp%2BKBiHfD0Pr7eD5bCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMwltRIxnq0CNfx2%2BdKtwDyANzJ9HLBB%2Bq7SPn6T6RTO61wz40iO0UNT86vEkpUeUlVJB6d1X9w2%2FCWCs8GTEUgd0nhp3BHXR6de7GctgjSI3ZNmD3kMpS%2BOz1fKfw%2FkbYsBp45UUM2ChG1AIWX6uxNJytW%2FLbQ6xowGkj2TGVOkV7Rm2bAAgd9NUa2tTQkmw9dopFleGE1iHvFfG0pxVY%2BCZIIE7YkHQvNn8JOUrDDNGZiRf%2F3ieAN2ZGX5s6jeHqEdaYDa%2BYQ6hPhDKj2mFe%2FuCiBR%2FMKSrPcZPJ2bmwHEpW9TzDX2YRPyjz5ZY9tg2bIJv42ULg1sXfFmVBVEMkqR7mBh7xtCgX%2BDI7w7nxkyElxBaGQf2NWzvfKq80WvCfBJru9izqBhz3dF0dyhwZgxx2K%2FKc8wVLwXVQwRipY2WNnYrVYStgWAxxpK6U%2BaS4SyMiGn6FxR5K6ryIQm4m2lWSuEQkZx6ycWillI82sjQWHK1YAQ5w47VWie%2F5hq%2FDLnRcDROp9rNCWXsQbg3kQeeT64DX7yDFzu6DPgZoELXCV9wb3PkeFRfApFzcnATiyUE2kb4ZVdpeaenyY%2B5Cq922oL2lZiCuqgs9XOQODcxe%2Fzu4xpPLgMr6tUslKcOIBt%2F2sbOShmE6VaYwzLC71QY6pgHWD4bN24T%2BpYRcH0ZGSshiZVx2%2BcVFMQ9e0LXV7cA%2Bxp42MzEx%2B2AkGOYhus9SrG%2BmyeaFrZiJfutzrUCrorqDiZiBC7b883Z12lnVHrWIOD00cRtpSbOqFjVd4kbOJ0NHyUEafP3aHq1RfApYMouhlKeKKKuvtpyaKgWl7DmWIwsLd92dNDa5WmISSIhDsPnRINF9XxBTCDiJhQPYkjyEt9y6nbiY&X-Amz-Signature=0f4f0be31de474fc478beda8a408d2c8811c1d829a0e63e0b8e7d13328f53140&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
