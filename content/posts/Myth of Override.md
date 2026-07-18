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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQLN5DR6%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T072458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAb4udKHBo%2F8HIiru4SAub1%2BcwwwNjHkaBTc6yBSRqv%2FAiEA6bBAgEBcYtc6T1ngOmbXk%2Fvx3UixxqacY4ogunhB6eAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDOZ8wsH5AoSM4UHvFyrcA9nhcjoSMWQYINOtznHfeAD1xgG%2BfOIt3p6odEwkmHlZ7a8Q%2FGWOhsImm17nKgHIUD1%2Fh7uIo7HYUm%2B5A2teUrCioPoi5AguKdhU6KRfzKtO6HTxsI29I8%2FavzJDUXCWXxzoOLNTy9UcF2cl%2Fgl%2BjT3p1rdrNKIEeMsv8wQPcdlm1z8qWquopK3IjJRyBEu%2FyJNykceMSBSjfg9x%2B9Oo2iQNvHJ5Y8vqRHtY%2FTfKrLhKvlShfpjYhPHTXzez6Etn7iwHlctzMK%2FsQWpKyYJFNhVENo7qQM%2Biehv4vQH8F6dWnYs7VSRS6jYXQHsWcTuQPA54vFF3RyAf8RV9R17SR1IP0oAaCWZsdowEFOcaAQ1%2BBkbTlpV7gB7utCeqQJ2%2Bb8c98C42Znm0yyBYOZ6vfOV57Q1lLW3d18FI15f1SXW5z5aER454EwcYW6g1QLRs%2BtIYGN%2BpFeYZHEwMGzCAH3RQfuIRXyUHUxzoIcqrtzXAPCLee%2FucTTiTNikY8pZCVS7GzGsDk7dW3%2Bwr1ssFI%2BFmbx1q05VJFWWiIzApQ6cJlErl4jPa%2F9EX1OTbAYp8JksLRl3CaePh7b5NrY9grTcl1oDwykFOP2jnRLPvf1M9LriA%2FQvHHlmJ166bMIbC7NIGOqUBY5iBIwfVufW0Eb%2BmwHUKEi%2FCTsxT3iuNWGsIOBDocxtv68%2FEbslT%2FYHBf6ueSZEre%2BjZcDUqTlgqcTnyWEDwCzUpF5B4VKjXiCCaPQc5yNM5C2IK5UVwLLaw7rzYRI4gXuCHELcHkgT%2BA59rHG8SsIU3K3QgstPG%2Br1wpCaTgjXv2C8JknM2s6aUveNHeWh2ikQWmTgSKSSfT2u3i%2Fk0InUaEkQN&X-Amz-Signature=8807949058d702b05623a636cf58a6d8873085488ef39abb69d2b193ecd7fd93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQLN5DR6%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T072458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAb4udKHBo%2F8HIiru4SAub1%2BcwwwNjHkaBTc6yBSRqv%2FAiEA6bBAgEBcYtc6T1ngOmbXk%2Fvx3UixxqacY4ogunhB6eAq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDOZ8wsH5AoSM4UHvFyrcA9nhcjoSMWQYINOtznHfeAD1xgG%2BfOIt3p6odEwkmHlZ7a8Q%2FGWOhsImm17nKgHIUD1%2Fh7uIo7HYUm%2B5A2teUrCioPoi5AguKdhU6KRfzKtO6HTxsI29I8%2FavzJDUXCWXxzoOLNTy9UcF2cl%2Fgl%2BjT3p1rdrNKIEeMsv8wQPcdlm1z8qWquopK3IjJRyBEu%2FyJNykceMSBSjfg9x%2B9Oo2iQNvHJ5Y8vqRHtY%2FTfKrLhKvlShfpjYhPHTXzez6Etn7iwHlctzMK%2FsQWpKyYJFNhVENo7qQM%2Biehv4vQH8F6dWnYs7VSRS6jYXQHsWcTuQPA54vFF3RyAf8RV9R17SR1IP0oAaCWZsdowEFOcaAQ1%2BBkbTlpV7gB7utCeqQJ2%2Bb8c98C42Znm0yyBYOZ6vfOV57Q1lLW3d18FI15f1SXW5z5aER454EwcYW6g1QLRs%2BtIYGN%2BpFeYZHEwMGzCAH3RQfuIRXyUHUxzoIcqrtzXAPCLee%2FucTTiTNikY8pZCVS7GzGsDk7dW3%2Bwr1ssFI%2BFmbx1q05VJFWWiIzApQ6cJlErl4jPa%2F9EX1OTbAYp8JksLRl3CaePh7b5NrY9grTcl1oDwykFOP2jnRLPvf1M9LriA%2FQvHHlmJ166bMIbC7NIGOqUBY5iBIwfVufW0Eb%2BmwHUKEi%2FCTsxT3iuNWGsIOBDocxtv68%2FEbslT%2FYHBf6ueSZEre%2BjZcDUqTlgqcTnyWEDwCzUpF5B4VKjXiCCaPQc5yNM5C2IK5UVwLLaw7rzYRI4gXuCHELcHkgT%2BA59rHG8SsIU3K3QgstPG%2Br1wpCaTgjXv2C8JknM2s6aUveNHeWh2ikQWmTgSKSSfT2u3i%2Fk0InUaEkQN&X-Amz-Signature=7c1ea0f1e447c729e700d19c41a07f684899267174824b2f3e6998b8409aabb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
