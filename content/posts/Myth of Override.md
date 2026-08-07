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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4I74ECK%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T202749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsdzv7LCKhp8jg42v5DJf%2FJDn4sxq0cygKpgQuOZEDfgIgYtSDclJiv%2BMati5Vh1MD3lbFM165fuzsYkvY8RKwgiMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDPrgbxcIIFFJqZkB9yrcA%2Fq0xfn7d3JHEivEJK3RIEAkvEyqLG%2BCNRaG3rfvAa7OcsrgW4OqXgVYwgLG5WPg8pn2W6zQ%2Bvpv0D%2Fcr8lsM0vWFE733fj6aDUKkk02DmyOPwdfLvyAg9TgUrvwQ7qRQVtayjFh7Qds7Ae%2Brd8FsgfYrUUdGDP5VlsHCJpM%2FpiOJ9vLzB8a18qg2O3zt3bLSrr4RhTCBdTKlgUUb9msv3rqb1IzXTKx8W8iqTWHDPfMn5OmBxKEtIr1QFbYTVIfNYAfwBnS0eTsqlfGIY4i5CoWDERcdfk86mBRAp0ZsFHk0zAguBP9WCfLN4d%2BQ6OXW6%2FzeQkjUzfem2mt5eX8f%2BCQdiePM%2FDKSLqn9axZl3aOo2H4yZNVkCLnFVAsIRXw4d6OejmaNY3Ur29vOOGEAFhLGTiXtR5z0GXJhjw3UbIUsdM8exECUAS0ZYQse22bZgmpQi150G4x9zYjgLtgbA9dXzoxf20g0hI4BNuEYvAnTAwxZ0RP752l%2BhstJrmT9PBLgZZa%2F945yqRAwI3XRrY1BowaBFfyoxFJ6AW4dkKfmzoK4reUmnz4fh6xFr73Abv4pjpcJohRp%2FY7s%2BQnPKT5y8k%2Fd4wvuasaCK1PFLRR2qUiCMsAQTrRE4zGMNv82NMGOqUBiTeBaIyJLHLbRTN20LtS18JhE08PDXcRRXDVtKKneDz6OUklzWo4lPhhOIikFUhAavPQRN%2B6kPR%2F4P1W%2F2F3nWORIxe%2BfvmpYOjJEpHB4HnZvEM%2F2g0UUtl2y5QxqYMg%2FFYMNY38P4JlRADAm%2Bqx4rcOf3k58J7irBTM%2Fp%2FNVE1KZc522AgU71wpOIuoYLGetkZssShRwpC%2BcyqB3%2FUL7j3v5u41&X-Amz-Signature=553f82aeeef63808e9f81f79fc00856c034fae49173a897f1fb5d1834f3bac97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4I74ECK%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T202749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsdzv7LCKhp8jg42v5DJf%2FJDn4sxq0cygKpgQuOZEDfgIgYtSDclJiv%2BMati5Vh1MD3lbFM165fuzsYkvY8RKwgiMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDPrgbxcIIFFJqZkB9yrcA%2Fq0xfn7d3JHEivEJK3RIEAkvEyqLG%2BCNRaG3rfvAa7OcsrgW4OqXgVYwgLG5WPg8pn2W6zQ%2Bvpv0D%2Fcr8lsM0vWFE733fj6aDUKkk02DmyOPwdfLvyAg9TgUrvwQ7qRQVtayjFh7Qds7Ae%2Brd8FsgfYrUUdGDP5VlsHCJpM%2FpiOJ9vLzB8a18qg2O3zt3bLSrr4RhTCBdTKlgUUb9msv3rqb1IzXTKx8W8iqTWHDPfMn5OmBxKEtIr1QFbYTVIfNYAfwBnS0eTsqlfGIY4i5CoWDERcdfk86mBRAp0ZsFHk0zAguBP9WCfLN4d%2BQ6OXW6%2FzeQkjUzfem2mt5eX8f%2BCQdiePM%2FDKSLqn9axZl3aOo2H4yZNVkCLnFVAsIRXw4d6OejmaNY3Ur29vOOGEAFhLGTiXtR5z0GXJhjw3UbIUsdM8exECUAS0ZYQse22bZgmpQi150G4x9zYjgLtgbA9dXzoxf20g0hI4BNuEYvAnTAwxZ0RP752l%2BhstJrmT9PBLgZZa%2F945yqRAwI3XRrY1BowaBFfyoxFJ6AW4dkKfmzoK4reUmnz4fh6xFr73Abv4pjpcJohRp%2FY7s%2BQnPKT5y8k%2Fd4wvuasaCK1PFLRR2qUiCMsAQTrRE4zGMNv82NMGOqUBiTeBaIyJLHLbRTN20LtS18JhE08PDXcRRXDVtKKneDz6OUklzWo4lPhhOIikFUhAavPQRN%2B6kPR%2F4P1W%2F2F3nWORIxe%2BfvmpYOjJEpHB4HnZvEM%2F2g0UUtl2y5QxqYMg%2FFYMNY38P4JlRADAm%2Bqx4rcOf3k58J7irBTM%2Fp%2FNVE1KZc522AgU71wpOIuoYLGetkZssShRwpC%2BcyqB3%2FUL7j3v5u41&X-Amz-Signature=eccec15914f48ecbe1024f8adb1d573b0e17ea12e049ece21d41f36d474f1a9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
