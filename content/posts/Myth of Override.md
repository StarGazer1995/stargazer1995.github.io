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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2DJTYHQ%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T124906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDRMGU%2BxOq5%2BAKlGJyUSKLMkklZZXPzBGvx%2Ft90jLiPAiBjHi4sjoF%2F%2BqGncu9G1%2FHTuSqg5OoHw2a1nEzR1x3d1Cr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM0Mmg1Ljmg%2FR%2BUvcaKtwDJAgJgrOKuk4XU%2FJ4%2BIGK71RzrbJogHHTxaBLQODAJYNQufqaunaHFFN4QJwTveXXR8ez0v4SrBKFSwmyno7JKJ4BqXnzfZVr8OQq0QFn2GNT64wL4C9Nlcw5qCnLr0MEgsd3s5p%2BFcJKMy3g0RBvxQUbogrF5QOQXA1tWoPmtbTK00xYyiHooDy9%2BH4CH32eGBX2ib56ZYoIuiIDd8iaDzmFFcjm5wxBWB6dK5O0KX5m6LfotBw5%2B16xSZOw2l%2BQD%2FrALQOh4HFQ3LSHrx6YY%2FYti3XVGZrjLjj9KV3W0Bn%2BWzr2hBdcF1aS%2BQBGy4FIfPaBL81BtxYVPCLLWkkFxGK21r1g3DhO3hU%2FbcVUMYh69uDL45Bm3sNnd6EvZe7BYUXithHkZy1g%2BbyOuw5JsQ8IH3q4YShB%2BDBfAUrsdxvZp2FXWUx3y1QuIZ%2BuIgfW5eltgDmJHzvbp4wiKMdq0jmfkL2AaAP%2BwCefRtdSbYpV7sxD3xY%2BTzZB2RSyvfdmsgcSEk21dTm5sEshnrMp24M5StxD7lm5iuzTPNdo9Qv69EaKGMwPQ77RlRnt6BKnGxA9z7893EYTU6J2JPfnhwQCIuPoesJH3CkbrJg1ZIKtQdBiqJu8Iisf76gwrJed0wY6pgH2KpDglSQrD4j0THKUs4wGXuLAQAyrgS4XRs16lGlIr3se6zayW95lBfRaGU7PBCIFr5mn8sVzgucr6y8%2FWIyckDOZrvIQ%2BPnreNZ2wOBlqClm0XeBE7687WdhtWYR%2FeSHnPafjIMUNdblNWl%2FU7h9oH7bE%2F9aDqmIsUx51Fpr7FZRYxr6S6atQLY%2F%2BfgMlIV5l2h%2BAXBUjRhh6tPekH%2BWVRojhuM%2B&X-Amz-Signature=bd2e0dd9e044003d8f6c12a780d0debf60089ee94f31b0e326b01bd0eeb1c012&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2DJTYHQ%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T124906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDRMGU%2BxOq5%2BAKlGJyUSKLMkklZZXPzBGvx%2Ft90jLiPAiBjHi4sjoF%2F%2BqGncu9G1%2FHTuSqg5OoHw2a1nEzR1x3d1Cr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM0Mmg1Ljmg%2FR%2BUvcaKtwDJAgJgrOKuk4XU%2FJ4%2BIGK71RzrbJogHHTxaBLQODAJYNQufqaunaHFFN4QJwTveXXR8ez0v4SrBKFSwmyno7JKJ4BqXnzfZVr8OQq0QFn2GNT64wL4C9Nlcw5qCnLr0MEgsd3s5p%2BFcJKMy3g0RBvxQUbogrF5QOQXA1tWoPmtbTK00xYyiHooDy9%2BH4CH32eGBX2ib56ZYoIuiIDd8iaDzmFFcjm5wxBWB6dK5O0KX5m6LfotBw5%2B16xSZOw2l%2BQD%2FrALQOh4HFQ3LSHrx6YY%2FYti3XVGZrjLjj9KV3W0Bn%2BWzr2hBdcF1aS%2BQBGy4FIfPaBL81BtxYVPCLLWkkFxGK21r1g3DhO3hU%2FbcVUMYh69uDL45Bm3sNnd6EvZe7BYUXithHkZy1g%2BbyOuw5JsQ8IH3q4YShB%2BDBfAUrsdxvZp2FXWUx3y1QuIZ%2BuIgfW5eltgDmJHzvbp4wiKMdq0jmfkL2AaAP%2BwCefRtdSbYpV7sxD3xY%2BTzZB2RSyvfdmsgcSEk21dTm5sEshnrMp24M5StxD7lm5iuzTPNdo9Qv69EaKGMwPQ77RlRnt6BKnGxA9z7893EYTU6J2JPfnhwQCIuPoesJH3CkbrJg1ZIKtQdBiqJu8Iisf76gwrJed0wY6pgH2KpDglSQrD4j0THKUs4wGXuLAQAyrgS4XRs16lGlIr3se6zayW95lBfRaGU7PBCIFr5mn8sVzgucr6y8%2FWIyckDOZrvIQ%2BPnreNZ2wOBlqClm0XeBE7687WdhtWYR%2FeSHnPafjIMUNdblNWl%2FU7h9oH7bE%2F9aDqmIsUx51Fpr7FZRYxr6S6atQLY%2F%2BfgMlIV5l2h%2BAXBUjRhh6tPekH%2BWVRojhuM%2B&X-Amz-Signature=f98732b1b5e0edcd23a3c354589c8f035658fc0d4fc7e1f68a4c83791a351523&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
