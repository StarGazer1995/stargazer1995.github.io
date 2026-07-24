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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUDU2MO%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T012457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD0Ob%2Fzm8LmMbyiwgHVNa%2BD5oiLW7JKiL2vjXgLOOlmXAIgInkE0%2BQ7UTTKfPuF46t9Hxr9WbRo0s9DxLQIbDugK8MqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXeCyBa1J8%2BASf6eSrcA2InYnEX2jUK%2B9UirGMixSnNPAw%2FT3qn9KTEsWjrhMlzWsEMJG0L8l2%2FVywkAbah02BlBhdHdZoNOb3L4IJsFs8OKbU4gN0S%2BFouunRbQJO374RbO7P%2BS2YjFWMX0DBnwN%2FwTct%2FzDzlqdx%2FbQji7%2BGGAFAbpkgbkJYSnOpEv8qK3fold6gl7zQmicF%2FiQSgU9uPXaHKahmU3fRmppvkhq2KvBQIZhLT021hDTfM1k5OnpSdSz0lEmSI2W1lfwuJgZD2MjDIRJWifo%2FbW1a%2FQBr1ZBONtzYxwE6famaNuaDhZJy59ZJh%2Fl82gfLEBAx7PllPvCPl4PiRW4rmaX0dZUvJXIPZEHnAbX%2FYpFi6UuZeH9QynzA7EpwBu9janioIYDsg3csCoMX1r%2BgdVCBqmTmd9bdIT9IGo5l9jSkuTdv6uN1aCy7cKLPRzSPhcDT8lqdRRmov%2BeLHVw%2F%2FXLCHifzxNeOG4VQUyY5Cz1FWxXjB3XLvwwxOc5W%2BY615PuJJ4S%2F9guVkq6jowktAkdSC4eOR8RSAgPV16wmBzy%2B2h7090KXfb6StzZqcF01a7EdvsOtdKyHrhUjFeMrcnICGZay1ionP5dLB6POrni8AsT7b1a03a9Ag%2B5uoGtT%2BMOruitMGOqUBa%2FkuG3u74wwOZhEtqpy7kVlISg04N%2B8HpKqrUe32JfwCTxMAfOZsQcg4QWeZzUorwVOgMwQX5HJ0mKdoLq9HjtNGdh7MZ3hgNzWV7Ax3m%2Bhk09Bju1oLxJe%2B6QimvhjPhMKzdhsnuOUVYAruKyoHeSOCztS%2FXZnej%2FuF0l%2FErOSA%2BSp2kZdR3BaIB%2BEs%2Bf6%2BO843y3kJbkkP6FXZJDGN50joF042&X-Amz-Signature=516ecfd940fae68fadb3f5afae1544705a4cf8bc19d077759dcbd576e9ab3cb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUDU2MO%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T012457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD0Ob%2Fzm8LmMbyiwgHVNa%2BD5oiLW7JKiL2vjXgLOOlmXAIgInkE0%2BQ7UTTKfPuF46t9Hxr9WbRo0s9DxLQIbDugK8MqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXeCyBa1J8%2BASf6eSrcA2InYnEX2jUK%2B9UirGMixSnNPAw%2FT3qn9KTEsWjrhMlzWsEMJG0L8l2%2FVywkAbah02BlBhdHdZoNOb3L4IJsFs8OKbU4gN0S%2BFouunRbQJO374RbO7P%2BS2YjFWMX0DBnwN%2FwTct%2FzDzlqdx%2FbQji7%2BGGAFAbpkgbkJYSnOpEv8qK3fold6gl7zQmicF%2FiQSgU9uPXaHKahmU3fRmppvkhq2KvBQIZhLT021hDTfM1k5OnpSdSz0lEmSI2W1lfwuJgZD2MjDIRJWifo%2FbW1a%2FQBr1ZBONtzYxwE6famaNuaDhZJy59ZJh%2Fl82gfLEBAx7PllPvCPl4PiRW4rmaX0dZUvJXIPZEHnAbX%2FYpFi6UuZeH9QynzA7EpwBu9janioIYDsg3csCoMX1r%2BgdVCBqmTmd9bdIT9IGo5l9jSkuTdv6uN1aCy7cKLPRzSPhcDT8lqdRRmov%2BeLHVw%2F%2FXLCHifzxNeOG4VQUyY5Cz1FWxXjB3XLvwwxOc5W%2BY615PuJJ4S%2F9guVkq6jowktAkdSC4eOR8RSAgPV16wmBzy%2B2h7090KXfb6StzZqcF01a7EdvsOtdKyHrhUjFeMrcnICGZay1ionP5dLB6POrni8AsT7b1a03a9Ag%2B5uoGtT%2BMOruitMGOqUBa%2FkuG3u74wwOZhEtqpy7kVlISg04N%2B8HpKqrUe32JfwCTxMAfOZsQcg4QWeZzUorwVOgMwQX5HJ0mKdoLq9HjtNGdh7MZ3hgNzWV7Ax3m%2Bhk09Bju1oLxJe%2B6QimvhjPhMKzdhsnuOUVYAruKyoHeSOCztS%2FXZnej%2FuF0l%2FErOSA%2BSp2kZdR3BaIB%2BEs%2Bf6%2BO843y3kJbkkP6FXZJDGN50joF042&X-Amz-Signature=31f0a9c5f3a42c12f0753ad28e0f5959d762db53714726a176dc4c463ca6ddd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
