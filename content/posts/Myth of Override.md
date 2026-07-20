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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPEYSIJG%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID6973CcfkEZZPr2mGwYsc5lDnSZo0u0VomvHcsi1PVtAiBQ2Q6NsaLqyH%2FF9sH8z0%2F7t5v5GiHzKY8BQKqmsasq%2BiqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9aXRJ9vn%2FxW4HwbCKtwDPIHUpFzaw4B8GrUX%2FZi%2BCRruDyXvSo6mLwDb1N56%2Bzz%2Be7jdEJqeoaxq6C5sAGEJR3Vy8%2Bo4LJEZg%2FU8VpvBU%2FYZfmwkX3IyILXYR23ralonT%2F5bGJyExZgfNfNq0VooD8wkQ50XJkouSV6MiR7BKm28GQ2Ml2Lba%2FrvP0mehU4cUXpygP9AJTpzlDR03PygpbI2rA5JBI889O8QSRKDNEUI45YFu5B8OoAPVYY84eLi06g%2BGfnwJMrJbNj8OeCoD1k%2F6UA5duZQbyfkPNMCI6GSYDzG%2BgrykZZB0SxbkEMLrxcDQ9y014ibfHT9yGb47qqa5iqiaiOJAi9T9rgJZ2diw2ZkywJ4SOPmU%2BVnZ5a9yulOLMCkL05uie9%2FMW8b0xx%2B5JnJzpj%2F3JQp1nHD4%2FudvHVuY3SaSZFX82e9%2BjJUQVwPC8VP%2Fo6RNZYjqb4L%2F8x1Y3IEhOFSLhcqJGUK68O78SbBCHcROj2Ln2MZyiJpHOGL%2FeHRDdx9qtwVGSzkfwYpgz%2Bm2pqYfiWQsLd%2BcUnRy4FeUzp2m54tGFRtnuolSk2DIaXhPNYCZiXGfqBGq9JTSM0VOW%2FQJRABzM4VUfDCKbX36o%2BKu4UTvEoMcSGNRw%2FNrluZUoxFsLQwzOP40gY6pgHFJbscf0tVMsAKmHJp0RKxJkiSUsQx%2Btuv5xiS%2BBl%2BMq94Zn%2FjhFPlSoNUYcR%2Fg3686a0JwAygEKn2dXYfqE%2FVTacU2Xt0jmMOIvHcoaroEPszk512YYA9F3X0c5GHgjqWnz2A2Ou6rcCdFaWd4s28wBzLR6yhmAUdENEHNAw7fwIQsZgy%2F6u4thXZHxZmVYC5a7AyEaoCXyD6R63R6w9to0iOu2DS&X-Amz-Signature=d175bc952902532392b6006a32f053e95778105ae8b4527bd6f4a36422769192&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPEYSIJG%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T154427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID6973CcfkEZZPr2mGwYsc5lDnSZo0u0VomvHcsi1PVtAiBQ2Q6NsaLqyH%2FF9sH8z0%2F7t5v5GiHzKY8BQKqmsasq%2BiqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9aXRJ9vn%2FxW4HwbCKtwDPIHUpFzaw4B8GrUX%2FZi%2BCRruDyXvSo6mLwDb1N56%2Bzz%2Be7jdEJqeoaxq6C5sAGEJR3Vy8%2Bo4LJEZg%2FU8VpvBU%2FYZfmwkX3IyILXYR23ralonT%2F5bGJyExZgfNfNq0VooD8wkQ50XJkouSV6MiR7BKm28GQ2Ml2Lba%2FrvP0mehU4cUXpygP9AJTpzlDR03PygpbI2rA5JBI889O8QSRKDNEUI45YFu5B8OoAPVYY84eLi06g%2BGfnwJMrJbNj8OeCoD1k%2F6UA5duZQbyfkPNMCI6GSYDzG%2BgrykZZB0SxbkEMLrxcDQ9y014ibfHT9yGb47qqa5iqiaiOJAi9T9rgJZ2diw2ZkywJ4SOPmU%2BVnZ5a9yulOLMCkL05uie9%2FMW8b0xx%2B5JnJzpj%2F3JQp1nHD4%2FudvHVuY3SaSZFX82e9%2BjJUQVwPC8VP%2Fo6RNZYjqb4L%2F8x1Y3IEhOFSLhcqJGUK68O78SbBCHcROj2Ln2MZyiJpHOGL%2FeHRDdx9qtwVGSzkfwYpgz%2Bm2pqYfiWQsLd%2BcUnRy4FeUzp2m54tGFRtnuolSk2DIaXhPNYCZiXGfqBGq9JTSM0VOW%2FQJRABzM4VUfDCKbX36o%2BKu4UTvEoMcSGNRw%2FNrluZUoxFsLQwzOP40gY6pgHFJbscf0tVMsAKmHJp0RKxJkiSUsQx%2Btuv5xiS%2BBl%2BMq94Zn%2FjhFPlSoNUYcR%2Fg3686a0JwAygEKn2dXYfqE%2FVTacU2Xt0jmMOIvHcoaroEPszk512YYA9F3X0c5GHgjqWnz2A2Ou6rcCdFaWd4s28wBzLR6yhmAUdENEHNAw7fwIQsZgy%2F6u4thXZHxZmVYC5a7AyEaoCXyD6R63R6w9to0iOu2DS&X-Amz-Signature=2aa4f6bb3617ffba31ee1de6e9aa578627670732ec612540c36c467c1956e1e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
