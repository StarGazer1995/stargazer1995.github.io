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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R37YJH42%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T200801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwsODWtxgszfXRjHrk2lQpr1B56ZFvuidqPCQKEh%2BVpwIgB%2FF8ccuCAicUPqm7sHWC3gLiLRRCzAWa1xX3Szsdd1UqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0dG0P82XqX9bWkdCrcA1jqcyn5aCotWrvW7Hg2%2B%2BB92cfarAan%2BxuLctKQak%2FmC2KqAQ9D7x7LyAICafZu%2Fpro5C1Txb4UHkrGnmxtVGx%2BN%2FMFW3l67Mp1TioFtOkMZsO9A2kk9Wlw59wRUJhpYS3jkBMGmJjmquguig33TM7cmLZ45vMHSVcnzFSE38xNbhwadjqucIyN5CCQcPRginptM8CpVDkMt8BrVSxRH2aS8vEZqg6zg1X6FKWl8%2Bex6uVk8SIDIW6OcY59GZwRF5jL2p23cR3vOfU85%2FlwjVbA61VhR3TuP3oDH4suJS8yAQug40qn3H%2F6oSF5g1%2F5z%2B%2FNEmbBC%2F%2Fim4RfZcPt9sTv7ebIF1rhl%2BEgjgVNIWvH2oGkH28P08Fe8cJo833fBjMvleJgvCYxbikoABx34ohksoh6RFMzpk9EaOtZez6xfWYSbPSI6nyAsEL8jUtF1gaDSysfetR59Nl5MRnoe6C6KbluubPkCV%2BS0SR4UYSzjNh07lxOSM5xTLDLM0pKEs8V6p6rysJNjE8FdIoX0Vc%2Bn3%2BhcuUkpvzdeJLvSafeJerO20aU%2FXWiNGCOYssNKW2TI%2FuY7IV2e%2F1rq23XRRmaMrlEfZuLqr0VZHJQENPNg9NAYTXRtwfSWGHVMOGD0dEGOqUBOUBmz1sZWo5T4qK5BRy3LziMUTHcBjLUNcVw2p7%2B1XZ9db9v5t8FYX6zEoyz0ljyWpp1rClavoTBGZkDTL%2B3uQEmgV0yQWp4XbgV2kyBpFeUUBVud9jRErfZaPxbloagtfeATwAgnxR%2FyjiKGgtI3wF5zjy%2FzUNyQKREcO5ojcOmbDsE9Igj%2FYIplDywX%2BkXbjUOU30Gwr%2FOz1pIJcDzgnKf28C7&X-Amz-Signature=91dd4a89b6704e52265d582e6412bbc9c7f28d35469928a41236b40d96f6270b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R37YJH42%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T200801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwsODWtxgszfXRjHrk2lQpr1B56ZFvuidqPCQKEh%2BVpwIgB%2FF8ccuCAicUPqm7sHWC3gLiLRRCzAWa1xX3Szsdd1UqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0dG0P82XqX9bWkdCrcA1jqcyn5aCotWrvW7Hg2%2B%2BB92cfarAan%2BxuLctKQak%2FmC2KqAQ9D7x7LyAICafZu%2Fpro5C1Txb4UHkrGnmxtVGx%2BN%2FMFW3l67Mp1TioFtOkMZsO9A2kk9Wlw59wRUJhpYS3jkBMGmJjmquguig33TM7cmLZ45vMHSVcnzFSE38xNbhwadjqucIyN5CCQcPRginptM8CpVDkMt8BrVSxRH2aS8vEZqg6zg1X6FKWl8%2Bex6uVk8SIDIW6OcY59GZwRF5jL2p23cR3vOfU85%2FlwjVbA61VhR3TuP3oDH4suJS8yAQug40qn3H%2F6oSF5g1%2F5z%2B%2FNEmbBC%2F%2Fim4RfZcPt9sTv7ebIF1rhl%2BEgjgVNIWvH2oGkH28P08Fe8cJo833fBjMvleJgvCYxbikoABx34ohksoh6RFMzpk9EaOtZez6xfWYSbPSI6nyAsEL8jUtF1gaDSysfetR59Nl5MRnoe6C6KbluubPkCV%2BS0SR4UYSzjNh07lxOSM5xTLDLM0pKEs8V6p6rysJNjE8FdIoX0Vc%2Bn3%2BhcuUkpvzdeJLvSafeJerO20aU%2FXWiNGCOYssNKW2TI%2FuY7IV2e%2F1rq23XRRmaMrlEfZuLqr0VZHJQENPNg9NAYTXRtwfSWGHVMOGD0dEGOqUBOUBmz1sZWo5T4qK5BRy3LziMUTHcBjLUNcVw2p7%2B1XZ9db9v5t8FYX6zEoyz0ljyWpp1rClavoTBGZkDTL%2B3uQEmgV0yQWp4XbgV2kyBpFeUUBVud9jRErfZaPxbloagtfeATwAgnxR%2FyjiKGgtI3wF5zjy%2FzUNyQKREcO5ojcOmbDsE9Igj%2FYIplDywX%2BkXbjUOU30Gwr%2FOz1pIJcDzgnKf28C7&X-Amz-Signature=dc6df3a75d5506c1037e6ee1b18cce8a33d50e065d35cede8c7c9abfd3b5f97b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
