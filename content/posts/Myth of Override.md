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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRYTJTQY%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T081628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC0N9%2FS6YuEBrC4g%2Bk2LZ2ZImP6QexlpU7KPqHVFKlf5AiBw1lHQiKwaEU4xzbBTP9Bf68RecMqkVrYpxyNkYscpjSqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb6JF1HJ8hDQyaLphKtwDRDm%2FI27pt9yID%2FfyODrwkTxX30Laf77j3TpfDeAG%2FIgjLs1P0LQs3P%2BsSNpD1O1rYh5J%2Fxz53U%2BDOVPrNUlz2%2F4MQ%2Bp%2BflV2P1x2Z%2BGkbP0bFJ0GJrDlhco9l84Ai1cwVAUo9GCLyydItshZxGOygZML6t%2FMTu6V36AnHLkPu%2FPLxDSOYHN0%2BsiAhjS%2BT68IA4pNhIO%2BKA9iHA%2FTAwK6cpBB4omTRuB7X8ydMgeKw0gOKMrOfysAnTqe7uWYBGoUc7B66%2FTuWTO7WcROU04SHDWcnF5tUHGMFnXZcs2SZpOUf64jWwCYEnXTThKxk9iuMsAUe6%2BkgyCCPlm%2FXGhNX1taQldi68hRdWWREa751EaoEA%2BXmwgC4YEXY3z3iICMrHeFOqtrLu%2BNhP6AX2Tr8SNCEQvRn0sjPLqAMNiIeDWFd4xAf7SdkhE8K%2FTAU8DMVfqLIdYvpmH1yMAMR%2FroOdGEKkcr6dh0iYVKaxdKb%2Bun8ammpykN9k2YGq7FPbzPuNSXARrbbRoC7bhbHZNgRf3pVxX8uluVg%2Fwtk4MZVNLD1BkD81GNIqilbrf4IXXiBs8kXxbB1Fs5vjWXgQz5GUsYx%2BNeG2yrEJQFY8EGBaPIoBWCT5%2Fmj3vRrZkwhK2l1AY6pgGy0B8VWeFVsUxSyHej5hW3IXEjsftLyGHoOsg%2FMGEnm9EKyM%2B7K8dKG%2ByKVMPf87O1uAOK6svzM%2F2UxwVc0ojeBZ%2FJ%2FKfGC48zbed623uj7F4uHJw1KhJFtwSGZo%2FRZT3oGMEN5mBW9NljezZO2FqxLVrgP2lkPY8Q0DYFJUefJauaEubDQuKS18X%2BBNEcyo8SBQCTptDQV8OTITug%2BgRUFkX2h0N1&X-Amz-Signature=19fec5af4620e9be99e6a22b3bab53d077503c6d2131cf254ed28d9205124dad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRYTJTQY%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T081628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC0N9%2FS6YuEBrC4g%2Bk2LZ2ZImP6QexlpU7KPqHVFKlf5AiBw1lHQiKwaEU4xzbBTP9Bf68RecMqkVrYpxyNkYscpjSqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb6JF1HJ8hDQyaLphKtwDRDm%2FI27pt9yID%2FfyODrwkTxX30Laf77j3TpfDeAG%2FIgjLs1P0LQs3P%2BsSNpD1O1rYh5J%2Fxz53U%2BDOVPrNUlz2%2F4MQ%2Bp%2BflV2P1x2Z%2BGkbP0bFJ0GJrDlhco9l84Ai1cwVAUo9GCLyydItshZxGOygZML6t%2FMTu6V36AnHLkPu%2FPLxDSOYHN0%2BsiAhjS%2BT68IA4pNhIO%2BKA9iHA%2FTAwK6cpBB4omTRuB7X8ydMgeKw0gOKMrOfysAnTqe7uWYBGoUc7B66%2FTuWTO7WcROU04SHDWcnF5tUHGMFnXZcs2SZpOUf64jWwCYEnXTThKxk9iuMsAUe6%2BkgyCCPlm%2FXGhNX1taQldi68hRdWWREa751EaoEA%2BXmwgC4YEXY3z3iICMrHeFOqtrLu%2BNhP6AX2Tr8SNCEQvRn0sjPLqAMNiIeDWFd4xAf7SdkhE8K%2FTAU8DMVfqLIdYvpmH1yMAMR%2FroOdGEKkcr6dh0iYVKaxdKb%2Bun8ammpykN9k2YGq7FPbzPuNSXARrbbRoC7bhbHZNgRf3pVxX8uluVg%2Fwtk4MZVNLD1BkD81GNIqilbrf4IXXiBs8kXxbB1Fs5vjWXgQz5GUsYx%2BNeG2yrEJQFY8EGBaPIoBWCT5%2Fmj3vRrZkwhK2l1AY6pgGy0B8VWeFVsUxSyHej5hW3IXEjsftLyGHoOsg%2FMGEnm9EKyM%2B7K8dKG%2ByKVMPf87O1uAOK6svzM%2F2UxwVc0ojeBZ%2FJ%2FKfGC48zbed623uj7F4uHJw1KhJFtwSGZo%2FRZT3oGMEN5mBW9NljezZO2FqxLVrgP2lkPY8Q0DYFJUefJauaEubDQuKS18X%2BBNEcyo8SBQCTptDQV8OTITug%2BgRUFkX2h0N1&X-Amz-Signature=09ea4371bde8acf5e0b08ad32384e68844bdaa2050ed3d4fb4d021bb5db240d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
