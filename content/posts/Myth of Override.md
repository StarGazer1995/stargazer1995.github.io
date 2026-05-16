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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TA7PV3Z%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T144737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2Fv4yzlNv5%2FHV92eML%2B%2FmgGmbp0euCwgyng5z%2F8aKRhAiEAnhqQtUcEP3YQi2djObcjOd2RqyYS5x1zcgjIykS36TgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhmU%2BOiIN5gKz76sircAxjKAuJuE%2BxoZ0X%2B1FJbPWazxSm5M7szmPadaBcRn54YXWkg4ubg0KIhxyEz0%2F0yU6GqzMcXbd7Er%2FtLFcyMVOLC6FapLLNGL2BXap7orvE0wr0%2FIjOS1swNfcXlTPgzqE19hRP%2Fa3pSIisfrhZlzjpD2bXC42LzTkCWSmhsauVagdhlY7mcebfXrnegu2DZHDuUiSwuF7TyY8ZUJpTz31fJrFZxdk8GHmAO4sfWssoVkv%2BfNqffRUnO%2FaioFE%2F1%2FOTZH3vVFpzboahyEKuJjcCU3occqqitVNx1tu93ujpqC2EVGWDQm6fRRYuDFpu2wP9x4Tdv2UzT5OHsJzpEEV87aFpY%2BfDhI92Z%2F7J%2BoZJVZI83x%2FzVd1MMl95Tjl8FBDzcFcHeOOWK7L94KAw%2B96NwtDuYPjkJ3LZD9gtqJF0jH1qEwI1rZ7rH%2B5tn%2FdgEFh5qR5paAG7SLrVkPM%2Bt0vreIE7n%2FY%2BQ0zmpFyL%2FVhdUtnflFf%2F9snkwt2OhjKgJh5NxbsIkzsIG2GW0r7PdP79iVdYrqglxp%2FmaRuNArPuB1bHDEcBLQmeRnyAIFWvGBROwEceO3fn1hPO6pqXJ5HuUTn27nmNCpGWmJikbRXjCTjSO1UtkUpJcPSJJMISdodAGOqUBhqZby0PxnEBH40pZnkMDGKUB%2FHbrrQjSYf8ccfw9PIQacTe41JxYOJVPB9%2B%2FGpkRwbvbn84sqwWX9iNyx3wAVgiBPccwAL%2BgKq%2FXgPLp%2FjyPIbSAeMghJRnh4WOW29bGhAJBL0CutUIZlE0%2BGCmJzoJtYZvkcI0irs1%2FOnvPSDf6Hy1ZyRXg8Dcfcq30Bd9jeJl8nEo99dhCwnklLuLOJZaBkKOy&X-Amz-Signature=3df028acd9421ed33155970b95fa7eeeaed662476e0e3d302a0a40a69dba8baf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TA7PV3Z%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T144737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2Fv4yzlNv5%2FHV92eML%2B%2FmgGmbp0euCwgyng5z%2F8aKRhAiEAnhqQtUcEP3YQi2djObcjOd2RqyYS5x1zcgjIykS36TgqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhmU%2BOiIN5gKz76sircAxjKAuJuE%2BxoZ0X%2B1FJbPWazxSm5M7szmPadaBcRn54YXWkg4ubg0KIhxyEz0%2F0yU6GqzMcXbd7Er%2FtLFcyMVOLC6FapLLNGL2BXap7orvE0wr0%2FIjOS1swNfcXlTPgzqE19hRP%2Fa3pSIisfrhZlzjpD2bXC42LzTkCWSmhsauVagdhlY7mcebfXrnegu2DZHDuUiSwuF7TyY8ZUJpTz31fJrFZxdk8GHmAO4sfWssoVkv%2BfNqffRUnO%2FaioFE%2F1%2FOTZH3vVFpzboahyEKuJjcCU3occqqitVNx1tu93ujpqC2EVGWDQm6fRRYuDFpu2wP9x4Tdv2UzT5OHsJzpEEV87aFpY%2BfDhI92Z%2F7J%2BoZJVZI83x%2FzVd1MMl95Tjl8FBDzcFcHeOOWK7L94KAw%2B96NwtDuYPjkJ3LZD9gtqJF0jH1qEwI1rZ7rH%2B5tn%2FdgEFh5qR5paAG7SLrVkPM%2Bt0vreIE7n%2FY%2BQ0zmpFyL%2FVhdUtnflFf%2F9snkwt2OhjKgJh5NxbsIkzsIG2GW0r7PdP79iVdYrqglxp%2FmaRuNArPuB1bHDEcBLQmeRnyAIFWvGBROwEceO3fn1hPO6pqXJ5HuUTn27nmNCpGWmJikbRXjCTjSO1UtkUpJcPSJJMISdodAGOqUBhqZby0PxnEBH40pZnkMDGKUB%2FHbrrQjSYf8ccfw9PIQacTe41JxYOJVPB9%2B%2FGpkRwbvbn84sqwWX9iNyx3wAVgiBPccwAL%2BgKq%2FXgPLp%2FjyPIbSAeMghJRnh4WOW29bGhAJBL0CutUIZlE0%2BGCmJzoJtYZvkcI0irs1%2FOnvPSDf6Hy1ZyRXg8Dcfcq30Bd9jeJl8nEo99dhCwnklLuLOJZaBkKOy&X-Amz-Signature=8c81a2b5190df7ab5fbc77c6debff8f67c9c23aab785bc5b55f920701f555ba6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
