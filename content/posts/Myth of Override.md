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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJN7GDRU%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T081217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEi0fHByIv2UFAnL1ysxjxskb8OHoKpKjaJEOrJdyfkqAiAn6dwXmJOPWvi7DRZZ8Am04%2Flq9iWypfkly%2FZLtRhvFCqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIZOQaAFQj7dauxalKtwDREr2SvAgKqdA%2FshNLid%2B8Yyzc8TYWQixK0g70xlh6%2BI5fo7MkU7kYK5TMpRmPbyXx6Qx4cTA1LkE%2BJ6LL1MKICTI2gKJavhzEmjf%2Br0LRNdWGzxqW2S6snCEV0D5869QlfvmdBt58p3sb6GCDZInbuN2SgJO13AflflNLkrk1tGmDVcsVy2y5CALnki0iTgFZaeHtJtmmyygO9aCYUwBZ85Mr5FavpSAFZFntNbteH9HLwqa0M63KmnoRaElE36yXMmTtAvTLGUtOHKjeb1zXUfJTR95eO%2BF60ygfOux1ZOeskFfAF5RLp3g03mNOptd6bK50huQtYHVYmIPexdz8OXz2aTmOzEY%2FYuKbiWEBYGNfHBmUUEkBzaWuY9zNuvGeeqiiTspw0NYe1g6gNjhidt%2B2vlMouUJTf%2Fg6HCkDOlGe7vbupkE%2B%2FyV3rNEkH9qaTkm9o2iP7k2p0%2BbwYmbn5Mcy5ZrURWQ0dutvslJQQn2PTjRfyyMzgFnqp9SihEHaZCfuFk0QXa5ZcbZmYSfR3zxHuYxS%2FnLxjhqlQhysFvlp9L5Gtp0NTYR8O40ZfqTECP9gzyazlynUWynVVzqWCKAStYEBS0ffAgDUI28NRB1XZYbdvF3M7hYsc8wotvwzwY6pgGmVUyNNQh8NyRrI%2FeL2E0EtQ2VKyXppuAJis325wYl9TEgfdzGaFEB1HgnkArDToLOAfspe6Qh8iZJL8nBEbd%2BPr%2F8OC0jO6ZHllWoRbLd74tMrpRaevbk2EEnqUO1oXhILhxxn%2BdN4SguQxBoMCB7jqUO9f467jPR8SQ9f5TFplvQWig9E%2Fx8eqNYQz2wLf%2FNfDaRHv%2FPIN3Kd9GpX0oa5oz8I8U%2F&X-Amz-Signature=64c9e8689937228b16fd2a62dcb9d450d1628bd8f714a482c70f29e255cdc337&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJN7GDRU%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T081217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEi0fHByIv2UFAnL1ysxjxskb8OHoKpKjaJEOrJdyfkqAiAn6dwXmJOPWvi7DRZZ8Am04%2Flq9iWypfkly%2FZLtRhvFCqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIZOQaAFQj7dauxalKtwDREr2SvAgKqdA%2FshNLid%2B8Yyzc8TYWQixK0g70xlh6%2BI5fo7MkU7kYK5TMpRmPbyXx6Qx4cTA1LkE%2BJ6LL1MKICTI2gKJavhzEmjf%2Br0LRNdWGzxqW2S6snCEV0D5869QlfvmdBt58p3sb6GCDZInbuN2SgJO13AflflNLkrk1tGmDVcsVy2y5CALnki0iTgFZaeHtJtmmyygO9aCYUwBZ85Mr5FavpSAFZFntNbteH9HLwqa0M63KmnoRaElE36yXMmTtAvTLGUtOHKjeb1zXUfJTR95eO%2BF60ygfOux1ZOeskFfAF5RLp3g03mNOptd6bK50huQtYHVYmIPexdz8OXz2aTmOzEY%2FYuKbiWEBYGNfHBmUUEkBzaWuY9zNuvGeeqiiTspw0NYe1g6gNjhidt%2B2vlMouUJTf%2Fg6HCkDOlGe7vbupkE%2B%2FyV3rNEkH9qaTkm9o2iP7k2p0%2BbwYmbn5Mcy5ZrURWQ0dutvslJQQn2PTjRfyyMzgFnqp9SihEHaZCfuFk0QXa5ZcbZmYSfR3zxHuYxS%2FnLxjhqlQhysFvlp9L5Gtp0NTYR8O40ZfqTECP9gzyazlynUWynVVzqWCKAStYEBS0ffAgDUI28NRB1XZYbdvF3M7hYsc8wotvwzwY6pgGmVUyNNQh8NyRrI%2FeL2E0EtQ2VKyXppuAJis325wYl9TEgfdzGaFEB1HgnkArDToLOAfspe6Qh8iZJL8nBEbd%2BPr%2F8OC0jO6ZHllWoRbLd74tMrpRaevbk2EEnqUO1oXhILhxxn%2BdN4SguQxBoMCB7jqUO9f467jPR8SQ9f5TFplvQWig9E%2Fx8eqNYQz2wLf%2FNfDaRHv%2FPIN3Kd9GpX0oa5oz8I8U%2F&X-Amz-Signature=e4c1da2728ac7fef09cda20184a86fbfa88272568dc62069a2849de539f56d03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
