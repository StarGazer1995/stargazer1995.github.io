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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRHCAO4Y%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T224442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCICHxdECu0bdKu33YA72crrIospb7TBf9kA1MSHssULErAiAFm%2B9337TxJAYpLZCUHG%2BLeQ1MFIYr1qaI1bkgxwedZiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoOlaogQsdHLsdcyEKtwDVba2l%2Fk1uCCRyvJxoOSeO%2Fqaa0l%2B4rpaVc3%2FjFiDVhJQP76hu9b4MX9DKMuCCdkz1U72lDgdi%2FV%2F6erogR0wZ%2FwfrDfb89LP0Fb%2BwUgLzGx7W1goZz5FKmgnhaE9NWL7KbYGXZ3%2BpDmwFHSVBG5o8JXc7CVspqjW61I0TCN1a6yDdcpjVegMEJp217nUR8GYTM8vug6JKvvHsF1rQ3%2FXdmglxn44uad%2B1AtTSh9hXp30mtWzz24ZiPkBy627VaUxEfd0dsi%2BkhnRMRMvbxP%2FXOQxVHFuBwg%2FFUSrnOuepuXzMAM2irR%2Fbs5Jr6kDodWyNVLAha%2BAfPJxfwbkkYlnX99R2sIAInPHqynunF5ujtfIPIXayrq9wBy1JFqiajdo%2Bha6uNdQoirvuVgQInU71A%2ByZJte5BJ0wSZx1cNf8a0B88nxp4da7n%2FF0lN908QZrTCA4Lp8y4r44mo7pGzJXXUvIHmDls5D3aMelKvkY7pCUniGVkEKG0H4FQkM8YWJiXFmAd5WGmDTR9tJqK6OO5arwFI4kt4M2ea72g6UxY5Zqml5MEjAgg5%2Ftl73eLCeCL2Kklr1ydjPRY%2F1%2FTYHazWEaZ2yoNHEHTFFgmjHGTUj5B0H5mjGTQDoq9Qw7sH5zwY6pgGo8ShcybMR1atzYdT76uQ6E7oMyK8GwLWaz2TV%2FzizI21McClCNkcVXbHIDp1NHFQiEoOuAvbJPu95z3auesU257PNaQrEeO87W9PDiEsikd5UX2UY%2F0eqlmLQ%2BRPJz7RU%2BE%2FP5OAGYAGvvcd9VXCldj2xzio5HeHpwtFYykGJ7MPZUwY4lX2uTPubQQ%2FHS%2F9bRI3Q3iZgSR1qJD9uYJRgkNWQvHLQ&X-Amz-Signature=999d275c3c506cd4478ed6b17a828c578571ec4d3b4c3d40fffd0b037d241f00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRHCAO4Y%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T224442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCICHxdECu0bdKu33YA72crrIospb7TBf9kA1MSHssULErAiAFm%2B9337TxJAYpLZCUHG%2BLeQ1MFIYr1qaI1bkgxwedZiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoOlaogQsdHLsdcyEKtwDVba2l%2Fk1uCCRyvJxoOSeO%2Fqaa0l%2B4rpaVc3%2FjFiDVhJQP76hu9b4MX9DKMuCCdkz1U72lDgdi%2FV%2F6erogR0wZ%2FwfrDfb89LP0Fb%2BwUgLzGx7W1goZz5FKmgnhaE9NWL7KbYGXZ3%2BpDmwFHSVBG5o8JXc7CVspqjW61I0TCN1a6yDdcpjVegMEJp217nUR8GYTM8vug6JKvvHsF1rQ3%2FXdmglxn44uad%2B1AtTSh9hXp30mtWzz24ZiPkBy627VaUxEfd0dsi%2BkhnRMRMvbxP%2FXOQxVHFuBwg%2FFUSrnOuepuXzMAM2irR%2Fbs5Jr6kDodWyNVLAha%2BAfPJxfwbkkYlnX99R2sIAInPHqynunF5ujtfIPIXayrq9wBy1JFqiajdo%2Bha6uNdQoirvuVgQInU71A%2ByZJte5BJ0wSZx1cNf8a0B88nxp4da7n%2FF0lN908QZrTCA4Lp8y4r44mo7pGzJXXUvIHmDls5D3aMelKvkY7pCUniGVkEKG0H4FQkM8YWJiXFmAd5WGmDTR9tJqK6OO5arwFI4kt4M2ea72g6UxY5Zqml5MEjAgg5%2Ftl73eLCeCL2Kklr1ydjPRY%2F1%2FTYHazWEaZ2yoNHEHTFFgmjHGTUj5B0H5mjGTQDoq9Qw7sH5zwY6pgGo8ShcybMR1atzYdT76uQ6E7oMyK8GwLWaz2TV%2FzizI21McClCNkcVXbHIDp1NHFQiEoOuAvbJPu95z3auesU257PNaQrEeO87W9PDiEsikd5UX2UY%2F0eqlmLQ%2BRPJz7RU%2BE%2FP5OAGYAGvvcd9VXCldj2xzio5HeHpwtFYykGJ7MPZUwY4lX2uTPubQQ%2FHS%2F9bRI3Q3iZgSR1qJD9uYJRgkNWQvHLQ&X-Amz-Signature=19cc7304beae5a06685daaf18d0b297ad9d48cff579560590ef868d780dbe0db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
