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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZASCP4N7%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T065957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFKCdNdrkhJWqWamnG%2BE1XMymiTlpNse9r4IImHJga43AiEAiAZcIWXWuqr7P9I29kw02Kt991koM9aPG%2FG7yLd1u6YqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyQe5sDPrhU4q03tSrcAxwrPoUp9snpRMsuoGxWjpxWJeRxsPaS52DpcAPLfRGtgHkaED8O2qSuQdz2apYVJb6%2BjDhiPeJC9nHxXCFy6lO3Mqs10NshFqDfET60b6CCGW2auDCrn4A2sW8LBhsO5VOx3z6usmUbfy8pLbAkUEthur6F7Od2Qjq9MzL1qyaLDf0asBApdjjepU1JH65pgHCasz%2FU6GAZKdCkd4yaD6ekdGhW%2Fy3pA0%2FnA10yWvE0OCckJUypX1O4TsYtSjOGE0euWisMWjw%2Fe1Fxy2WyW3V2DLC%2BnaS5py8i3nvUZF5g12qCedymRoDmbMcUen7cKZ0%2BgirkfI3BAXzx2Lx6CXtiSQOvr9z1H7l%2BLRhX8727uifyQWKpOgynRFPU6fSifK%2BGe9JoszReHuNf81XhEHIAjoyWTuZ1YGEUGJi174DbCdscrSOy1WZZADrSHx6FEhOQfh0I%2FoBkazFeu4rixXYcKkt3oKIcp9qe1vmcn9nK0za7DJDL0tawiaXirzZ1vCcZfOuEumR7qqQipuXHIROift9KRvtQgLwTvvT6IZAmxOAF57eSpH4RxMAMG4q5Yutsbntt5rsAKBKwS%2FN2PraJiLdlBsAOFXYEu3bwwGyqna9qKXWW1iSpTG%2BjMN33l9IGOqUBL4FG0nNuw3lz4R5g8%2Bg4q3I5sXxoJc%2FI05iVoHG3%2FuWkjM8sC5tVNixNXq4VvUcf7Wi1zOSt97nUUbgHRwj523OZCuapKw%2FMmdAlNMqlI4vlkM3iX%2F2tISAxZm7RvmR1b0ospCSXFr3rFBf%2BFOg8Ik42xujviwwPCSx2Up0C0p78HrdNiR97pc2TgNysRIkqmwZxjCY3MBsBEGWBG8YQLvNhsC7J&X-Amz-Signature=bba389e278cd7ea3d12f90d2ccadbda6cb4cbcf558579a1dd8e5bce807c657a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZASCP4N7%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T065957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFKCdNdrkhJWqWamnG%2BE1XMymiTlpNse9r4IImHJga43AiEAiAZcIWXWuqr7P9I29kw02Kt991koM9aPG%2FG7yLd1u6YqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyQe5sDPrhU4q03tSrcAxwrPoUp9snpRMsuoGxWjpxWJeRxsPaS52DpcAPLfRGtgHkaED8O2qSuQdz2apYVJb6%2BjDhiPeJC9nHxXCFy6lO3Mqs10NshFqDfET60b6CCGW2auDCrn4A2sW8LBhsO5VOx3z6usmUbfy8pLbAkUEthur6F7Od2Qjq9MzL1qyaLDf0asBApdjjepU1JH65pgHCasz%2FU6GAZKdCkd4yaD6ekdGhW%2Fy3pA0%2FnA10yWvE0OCckJUypX1O4TsYtSjOGE0euWisMWjw%2Fe1Fxy2WyW3V2DLC%2BnaS5py8i3nvUZF5g12qCedymRoDmbMcUen7cKZ0%2BgirkfI3BAXzx2Lx6CXtiSQOvr9z1H7l%2BLRhX8727uifyQWKpOgynRFPU6fSifK%2BGe9JoszReHuNf81XhEHIAjoyWTuZ1YGEUGJi174DbCdscrSOy1WZZADrSHx6FEhOQfh0I%2FoBkazFeu4rixXYcKkt3oKIcp9qe1vmcn9nK0za7DJDL0tawiaXirzZ1vCcZfOuEumR7qqQipuXHIROift9KRvtQgLwTvvT6IZAmxOAF57eSpH4RxMAMG4q5Yutsbntt5rsAKBKwS%2FN2PraJiLdlBsAOFXYEu3bwwGyqna9qKXWW1iSpTG%2BjMN33l9IGOqUBL4FG0nNuw3lz4R5g8%2Bg4q3I5sXxoJc%2FI05iVoHG3%2FuWkjM8sC5tVNixNXq4VvUcf7Wi1zOSt97nUUbgHRwj523OZCuapKw%2FMmdAlNMqlI4vlkM3iX%2F2tISAxZm7RvmR1b0ospCSXFr3rFBf%2BFOg8Ik42xujviwwPCSx2Up0C0p78HrdNiR97pc2TgNysRIkqmwZxjCY3MBsBEGWBG8YQLvNhsC7J&X-Amz-Signature=2c2ae2ebab97ee06058d00b02a446be15662785f50f08f9b0ee1e0080e2726d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
