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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666K7INYEL%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T073625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQClxq4wDHywElOebMtI2QKNOBAX4aoHf8zYO6E6TLX8xwIgKKbwX20jOwDQlt7kGrMaFlATT2XHqg9S2X4M0pbuqioqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2FTARpd4OpQ9aHuzCrcAzHg%2BNkdieeLZ6L8H2c%2B151RhxmZxc7DhZ517G675GfsFC%2Bbu2VJue2oiauMTh66nZj3T2HHuxfftOXOX8RvPVzpQjmhrCGZQXiKI%2BmJegodrF9jF34kQnUDeZI2eh0YRk6J5t6MceuezLCqxwQveagut9qW7m84FeUKU30khjyiLcnWmIiTo%2BqS4fLp206u9%2F2vLCltzS5t5h1P%2BluPixNwU7nYQ1o%2FRfucJ2wRlTDd5JgF7dagLWbeeyEZjVLVTxO1FO9ZeIIUrQZmsBfRdyEh7UjZmV3%2BkhBT9WbITfM5hhuz%2Bly%2BAyQcoXb6ECfvkQetBcqpQjTobUpFykQ%2BvYP%2B0qA3NYw9FH4GP3dfzJ1vw1WGhnaFQSyLYYgCj4cRYmeQAT9oOL0AXwNRjflGcRZOjWr0ikHAan9JIymW45ySfZIvMuKidRohNWlw%2BunSTULD0XxkRKtTCUxPVdbIE7KI9HjJwsMytBenojgx%2FnGiiQrqpXbL3JKrvZki7Rbb5ZTp9RODbO4NLXgZw1VaLgMCjnwGmx9mvehOKARtvUej%2FmsIFi9daWBr9KPaf59%2BMCwbfdLDgkJbs6WbOqTVWvAIaZKse3ez9X%2BKKGWZTRImYTTooiZhrz%2BpGpEcMN2fsNAGOqUBWNGkFNDZFcZ1pxg7dm6UktYRprbJo87y8avP6t83yzTM8KulDW2RqocPcZhFgbnjHN00j3%2FEIPWcDEri5rFSeVOBqZlJbZ85mC9nYKU%2BPd%2FKIxaiiklq98Tq%2BDHrz7M35qraHlVIjUuKoD1Dxfo%2FfyrwS4WE0iEFAUdzrQ3ImNrkjjHmEA9ufU4MOZK7fs%2F1FA%2F5t9TM%2F%2F5ZQiWppzWJ%2BptkuOYd&X-Amz-Signature=057bf417380cb403249faf1b015b56da41e447920250925d2417daf672355ae4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666K7INYEL%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T073625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQClxq4wDHywElOebMtI2QKNOBAX4aoHf8zYO6E6TLX8xwIgKKbwX20jOwDQlt7kGrMaFlATT2XHqg9S2X4M0pbuqioqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2FTARpd4OpQ9aHuzCrcAzHg%2BNkdieeLZ6L8H2c%2B151RhxmZxc7DhZ517G675GfsFC%2Bbu2VJue2oiauMTh66nZj3T2HHuxfftOXOX8RvPVzpQjmhrCGZQXiKI%2BmJegodrF9jF34kQnUDeZI2eh0YRk6J5t6MceuezLCqxwQveagut9qW7m84FeUKU30khjyiLcnWmIiTo%2BqS4fLp206u9%2F2vLCltzS5t5h1P%2BluPixNwU7nYQ1o%2FRfucJ2wRlTDd5JgF7dagLWbeeyEZjVLVTxO1FO9ZeIIUrQZmsBfRdyEh7UjZmV3%2BkhBT9WbITfM5hhuz%2Bly%2BAyQcoXb6ECfvkQetBcqpQjTobUpFykQ%2BvYP%2B0qA3NYw9FH4GP3dfzJ1vw1WGhnaFQSyLYYgCj4cRYmeQAT9oOL0AXwNRjflGcRZOjWr0ikHAan9JIymW45ySfZIvMuKidRohNWlw%2BunSTULD0XxkRKtTCUxPVdbIE7KI9HjJwsMytBenojgx%2FnGiiQrqpXbL3JKrvZki7Rbb5ZTp9RODbO4NLXgZw1VaLgMCjnwGmx9mvehOKARtvUej%2FmsIFi9daWBr9KPaf59%2BMCwbfdLDgkJbs6WbOqTVWvAIaZKse3ez9X%2BKKGWZTRImYTTooiZhrz%2BpGpEcMN2fsNAGOqUBWNGkFNDZFcZ1pxg7dm6UktYRprbJo87y8avP6t83yzTM8KulDW2RqocPcZhFgbnjHN00j3%2FEIPWcDEri5rFSeVOBqZlJbZ85mC9nYKU%2BPd%2FKIxaiiklq98Tq%2BDHrz7M35qraHlVIjUuKoD1Dxfo%2FfyrwS4WE0iEFAUdzrQ3ImNrkjjHmEA9ufU4MOZK7fs%2F1FA%2F5t9TM%2F%2F5ZQiWppzWJ%2BptkuOYd&X-Amz-Signature=4893fed548d36ca3ab6547d4b0b362b38d621556db597fb9f3f5c4182656269c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
