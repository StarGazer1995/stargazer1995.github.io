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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6FYVURJ%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T105315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDOlOmO85agyq8pKnE276fVHEWMLMlssqminNU3%2BzaMNgIhAK6Bcm6roj9Rla1yE28zis3QuryFmF%2BAbH8Cvvv8nArtKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwH7UzI%2BhokpwgrEK0q3AMO7KcMO2nraAnsaAighrBDG7HRLdDsI6QgUgGCx0%2BfVlnqJwmz8K%2B2XhGR3JSRxcyYo3Ls%2Bp%2BYpG1t2klHu0VDMr%2B5Yw1nWL%2F0%2BzTzk%2B1bRk%2Bhq0XlGUZHyqTSFu1PWT7nzM21LHoHVDnb8tcI%2F9GeOvN2sbpSbidYh1%2Fgo68bTMrYbsSQbE1AJndswH0B0VZWnuX6OMegJ7C9yxCvVNVkLAiuNq5DkP1ndPM948mMqtNpgIRuEWLQLbXR8XL6UtYVLZOHrVaYeIKIoqiNsSIXhB%2FXri%2BMI2W8PByGHr5FzvM1raMhYiRFn62hHl1NdW4bx21gFylzRmfvs3ybkDiJ16Ap%2Bk01NwCnuNzQUyh92bmJImL5BHOTcN5rZiAtCaJtpTCHg9PAmTRQXD5R0sD0kdNPDQjy4XZL%2B0SZxW%2Bg8tHd01oP0%2Fnln7fBvSmJsdBRojxwAbNYEB4MW8brfV8Rs8H3qP83uRKV0RS1fRpmv0d8LiCAg%2BL7dSftIUP8tw2V1AABiCwGg%2BO0fLHK6SUX%2BH1kytbJujkoPHb%2BE0H48PNQDAZGYdzm%2FVB00alcfp3BXCP0U4ooBjiaRQOsvg%2Bd5pEjwJIvvwNgbcxRP8HDoAIK5QqfnlNlYWmCeDDRmJPWBjqkATP8VAEv9DaW0ZxJR1nqSPm4dGMK%2FCF82VdTK9HUBawjG%2BaXI%2BwjJghwmwG%2BUEwuiF1qulEtvrfa9Dik7aeeyUjPHxlRJLzl5LLGQwWLqUMWpVeU%2FD8HwIris5AqmP%2BW8EorwTMiUtpHwKHipEXOB%2BWFBQ28ZenDkSENLNQw1ddg6KAIYlOiHkU8PXSJEa1CZt1PYkRt5YSniBBw0ImSgqGRwRfz&X-Amz-Signature=2d91179eef6e2d0816f97679cbfe76205d505d1036a8a10e871c7617f2533be3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6FYVURJ%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T105315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDOlOmO85agyq8pKnE276fVHEWMLMlssqminNU3%2BzaMNgIhAK6Bcm6roj9Rla1yE28zis3QuryFmF%2BAbH8Cvvv8nArtKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwH7UzI%2BhokpwgrEK0q3AMO7KcMO2nraAnsaAighrBDG7HRLdDsI6QgUgGCx0%2BfVlnqJwmz8K%2B2XhGR3JSRxcyYo3Ls%2Bp%2BYpG1t2klHu0VDMr%2B5Yw1nWL%2F0%2BzTzk%2B1bRk%2Bhq0XlGUZHyqTSFu1PWT7nzM21LHoHVDnb8tcI%2F9GeOvN2sbpSbidYh1%2Fgo68bTMrYbsSQbE1AJndswH0B0VZWnuX6OMegJ7C9yxCvVNVkLAiuNq5DkP1ndPM948mMqtNpgIRuEWLQLbXR8XL6UtYVLZOHrVaYeIKIoqiNsSIXhB%2FXri%2BMI2W8PByGHr5FzvM1raMhYiRFn62hHl1NdW4bx21gFylzRmfvs3ybkDiJ16Ap%2Bk01NwCnuNzQUyh92bmJImL5BHOTcN5rZiAtCaJtpTCHg9PAmTRQXD5R0sD0kdNPDQjy4XZL%2B0SZxW%2Bg8tHd01oP0%2Fnln7fBvSmJsdBRojxwAbNYEB4MW8brfV8Rs8H3qP83uRKV0RS1fRpmv0d8LiCAg%2BL7dSftIUP8tw2V1AABiCwGg%2BO0fLHK6SUX%2BH1kytbJujkoPHb%2BE0H48PNQDAZGYdzm%2FVB00alcfp3BXCP0U4ooBjiaRQOsvg%2Bd5pEjwJIvvwNgbcxRP8HDoAIK5QqfnlNlYWmCeDDRmJPWBjqkATP8VAEv9DaW0ZxJR1nqSPm4dGMK%2FCF82VdTK9HUBawjG%2BaXI%2BwjJghwmwG%2BUEwuiF1qulEtvrfa9Dik7aeeyUjPHxlRJLzl5LLGQwWLqUMWpVeU%2FD8HwIris5AqmP%2BW8EorwTMiUtpHwKHipEXOB%2BWFBQ28ZenDkSENLNQw1ddg6KAIYlOiHkU8PXSJEa1CZt1PYkRt5YSniBBw0ImSgqGRwRfz&X-Amz-Signature=6f25d85d77079519e9721ca24db8b655ba94cff73d97c03c6119f9047f8b836c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
