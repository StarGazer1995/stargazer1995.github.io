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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO4K3GUH%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T043732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHm65JINviGg3eJIc8pGNiKNu8o6HO50jCrN%2FXLd5FeuAiEA0D1akKRsx40By7BnuRWYd8Oq8NkPcgmSrsT75EHbC24q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDPVurD3kQizqzRj35CrcA8R%2BG9bJ99mXkPNkBPkBAApP%2BIU1WoVbpXFiz1Pv1%2FCso5qw3BGFIteDBNPYJ%2F59v%2BOyUkmcihFgu5tvGoIv7Fw4BwZ1jdS0kVvjdI9JSAY5gqNp63aYQgVgU%2BN1swkxQafOGC0yDADX%2FutBmRhzgSQ1V2FBrPB%2BcpTwkAiH5%2FB1nhTyFEW126Q8FHoRC9RhCxuCoc5lAKd4gcRkJDN76F1INA2ZIVlYxKwrDnfkwQdsSgiRbd2qRIeagrD2%2BzOU95mUg1%2FigrpDhd6eS%2FZQ5xrDmGmROleLiCIm7eqrZsBCPRiAxGmog25TmRdxMWMsCkPRe9SrTL45ef0c25nN6accr5OiS2BDi9OCoy71Y9DUb6IPHk%2BsufYeWsQYQ1%2BMf63WL3u0PZDuv0g2j9Q2w1owLZct0Zjvhfk8%2FRZ4lMe3rZXKNhWUF35z7T2T9Jo4L57Bd00xKmD%2Fz5qFwnkjyEn%2BRINFn2mbVGqFhYoXl9jEOjA%2FhM657ZeIht3KNZtW4srgkkY5OWlU4HrxuTkZa9rmJoiTSl1i94%2BoS4acCnQUCvzFB2kuU5pHKGVo9DxwvR8EQsc2FaqVBlu1PMYApB50HPIQgCJ8m4THogVrplFALUNhkSaQ4LuVMOD2MJ3h69IGOqUBRX%2F0RCo9713CbGPqZwExAy1hGbUfpE1d629Xd9CvlElly9a3HPmWOj2sJBJFIxdNp1Ci00SCVs8y38lmfW%2FX7wywUWNjhe4ug%2BEPs7vnxx%2B02uc28YlPSimva6g%2BDwWm7Bt1PK%2Fuzi7uXqfwIefeq%2FB52mCrUzahCm4mtGMn9RZmokyYlLqg%2FvJLl6g8dnZlrZ5lxV6hxfMe0xUm7NV%2B1PbsWH43&X-Amz-Signature=7f62d8a1f6b675e094a6d9a73d71bb9648928555f51c3662d71b11e137b3bd3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO4K3GUH%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T043732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHm65JINviGg3eJIc8pGNiKNu8o6HO50jCrN%2FXLd5FeuAiEA0D1akKRsx40By7BnuRWYd8Oq8NkPcgmSrsT75EHbC24q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDPVurD3kQizqzRj35CrcA8R%2BG9bJ99mXkPNkBPkBAApP%2BIU1WoVbpXFiz1Pv1%2FCso5qw3BGFIteDBNPYJ%2F59v%2BOyUkmcihFgu5tvGoIv7Fw4BwZ1jdS0kVvjdI9JSAY5gqNp63aYQgVgU%2BN1swkxQafOGC0yDADX%2FutBmRhzgSQ1V2FBrPB%2BcpTwkAiH5%2FB1nhTyFEW126Q8FHoRC9RhCxuCoc5lAKd4gcRkJDN76F1INA2ZIVlYxKwrDnfkwQdsSgiRbd2qRIeagrD2%2BzOU95mUg1%2FigrpDhd6eS%2FZQ5xrDmGmROleLiCIm7eqrZsBCPRiAxGmog25TmRdxMWMsCkPRe9SrTL45ef0c25nN6accr5OiS2BDi9OCoy71Y9DUb6IPHk%2BsufYeWsQYQ1%2BMf63WL3u0PZDuv0g2j9Q2w1owLZct0Zjvhfk8%2FRZ4lMe3rZXKNhWUF35z7T2T9Jo4L57Bd00xKmD%2Fz5qFwnkjyEn%2BRINFn2mbVGqFhYoXl9jEOjA%2FhM657ZeIht3KNZtW4srgkkY5OWlU4HrxuTkZa9rmJoiTSl1i94%2BoS4acCnQUCvzFB2kuU5pHKGVo9DxwvR8EQsc2FaqVBlu1PMYApB50HPIQgCJ8m4THogVrplFALUNhkSaQ4LuVMOD2MJ3h69IGOqUBRX%2F0RCo9713CbGPqZwExAy1hGbUfpE1d629Xd9CvlElly9a3HPmWOj2sJBJFIxdNp1Ci00SCVs8y38lmfW%2FX7wywUWNjhe4ug%2BEPs7vnxx%2B02uc28YlPSimva6g%2BDwWm7Bt1PK%2Fuzi7uXqfwIefeq%2FB52mCrUzahCm4mtGMn9RZmokyYlLqg%2FvJLl6g8dnZlrZ5lxV6hxfMe0xUm7NV%2B1PbsWH43&X-Amz-Signature=1b7c6795f062b60419af42b0b772cbcbac463a14b65fb876bc1c9590b3404c49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
