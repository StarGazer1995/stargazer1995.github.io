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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQVSU54R%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T220958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwiY8cn1iZ%2FnSaL9%2FL3jOuMsttOiGvlH74%2Fv3qffEhjAiEAghqTeQBU%2FcxsJaQ9wF7Ly%2BrLzg9X%2BKidzTrqMzg0SJAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDNiiHUo7Xd1xSFlx%2FCrcA%2FXhigz8QtKvlK%2FJzgyjY8PKaMLeAmXVm0Sn9%2BO4Cnf%2BSuvHZVv%2FIE4NL63Ivp8YVUNy5I63W5uOfW3cXDuNHc0tY1kfBDP0m0hdu4gibhm8wGqdD4wHkSUAqm6Rk2H7wzgj2crkTuMuO3MjDehhvyoXmEiBPp9S4PZp%2BAh6K7vzVHIAwI6xesa%2FDUtwmgq%2B4FaVi1rIWE%2FMTsbqyxDhqTepaD22SHhKE3ZpV6GkDu8XyTWM2TkcBYDC4PKdiaWck6pr296LcOTvQDYrudOJUhDjNAU8f2mx3xKQjAoxeJuFe4OMNzspvR6VHhPF8V3HqxdMRUr2d7bxQX%2F601%2BKDkuiFM4H4T4NqXNJAyv2CRbEffKrNlAk6KsPL9yH1JTBihvoGIXiUjfYgFoIot1AA4jLHDRkStuAJY0qZDZvGdfcTZs1WwP9Ah%2F6BRvUg5vZrYpun%2B5nBfqTsrEDZqFpH12XqXxJZZdErgrRTa9Lh0fFdOodG6nOfsIOWoFWAJy72d%2BsGQ4vr19KQLKzXD4tmUWDOboLyZsVK5we438JQKTWkOce62zxqsOSB8HS9%2Fd9hosB5wVE0xudex%2BhIpQw5kM9ini%2BraVz%2Fa2WnBHuIqTXbKKfa2DI%2BesvjkS%2BMJm7g9QGOqUBIuPNwHOlxTnC4wEWhOm74%2BXSNDnCrnZ%2BjXHISI5soaeQ29ufGXBfK1HXHPyKBG8Gn8l7Dzn4Z4Li%2B2ZcjX8ZYQP%2F45bkVN8TxNON%2B5slScQj5CYQet3m3DoaW7gMHwP27wrgylIS9dH3%2B5Gwdj4ygv0Jfx64V66TcY%2BQiDctn0MxVM1bq%2BPBZPdNh7y6AFD56k1hmJePrno02%2FGV1IiE2zuzCkrt&X-Amz-Signature=575643136bebc73d4e45bb08798759e81296fa01420fd433f20610fe06d13c2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQVSU54R%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T220958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwiY8cn1iZ%2FnSaL9%2FL3jOuMsttOiGvlH74%2Fv3qffEhjAiEAghqTeQBU%2FcxsJaQ9wF7Ly%2BrLzg9X%2BKidzTrqMzg0SJAq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDNiiHUo7Xd1xSFlx%2FCrcA%2FXhigz8QtKvlK%2FJzgyjY8PKaMLeAmXVm0Sn9%2BO4Cnf%2BSuvHZVv%2FIE4NL63Ivp8YVUNy5I63W5uOfW3cXDuNHc0tY1kfBDP0m0hdu4gibhm8wGqdD4wHkSUAqm6Rk2H7wzgj2crkTuMuO3MjDehhvyoXmEiBPp9S4PZp%2BAh6K7vzVHIAwI6xesa%2FDUtwmgq%2B4FaVi1rIWE%2FMTsbqyxDhqTepaD22SHhKE3ZpV6GkDu8XyTWM2TkcBYDC4PKdiaWck6pr296LcOTvQDYrudOJUhDjNAU8f2mx3xKQjAoxeJuFe4OMNzspvR6VHhPF8V3HqxdMRUr2d7bxQX%2F601%2BKDkuiFM4H4T4NqXNJAyv2CRbEffKrNlAk6KsPL9yH1JTBihvoGIXiUjfYgFoIot1AA4jLHDRkStuAJY0qZDZvGdfcTZs1WwP9Ah%2F6BRvUg5vZrYpun%2B5nBfqTsrEDZqFpH12XqXxJZZdErgrRTa9Lh0fFdOodG6nOfsIOWoFWAJy72d%2BsGQ4vr19KQLKzXD4tmUWDOboLyZsVK5we438JQKTWkOce62zxqsOSB8HS9%2Fd9hosB5wVE0xudex%2BhIpQw5kM9ini%2BraVz%2Fa2WnBHuIqTXbKKfa2DI%2BesvjkS%2BMJm7g9QGOqUBIuPNwHOlxTnC4wEWhOm74%2BXSNDnCrnZ%2BjXHISI5soaeQ29ufGXBfK1HXHPyKBG8Gn8l7Dzn4Z4Li%2B2ZcjX8ZYQP%2F45bkVN8TxNON%2B5slScQj5CYQet3m3DoaW7gMHwP27wrgylIS9dH3%2B5Gwdj4ygv0Jfx64V66TcY%2BQiDctn0MxVM1bq%2BPBZPdNh7y6AFD56k1hmJePrno02%2FGV1IiE2zuzCkrt&X-Amz-Signature=513f42d57a4af2854143e9be09cba7135c5349e5a1d861adc9d1ec4b0c090aa7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
