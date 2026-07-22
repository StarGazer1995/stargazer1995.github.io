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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5DFSZIG%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T131758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDr3TWUmsGv1giTV2rMtfrSjLLVybLqNUNUuEvYHfA0rwIhANBloXXyNrM8ilKmVd%2BQTMDA%2FYM%2FXUJPTk3qwvcfF4l9KogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOU4Kyjq4y%2BhI01nYq3AMghRVvu5EpLO3yehUfIF%2BTWKvVafoz%2FtRTu%2FeVSaXxLvVfUV%2FM%2FcKadNEcVFsxm%2BxM6YxUlZe9HrsiWa94XgHqutsZhqhZWfU8%2Fg2z3QJBsLdsXccNeUfTuSR68Ttb7%2FcJ%2BXsowkp7oH4U0mKnMXy9gtZyli3SIe%2F2OT9R0IKaqIN89S1oka%2Fr%2B142TICfShv%2Fbk7YUd5lBeerccKgF%2BIi4zeo2OL7onXfJqolGvCulTR7K%2BACkn821ss9dAVuegBZOCbnhl4sWqHcCgPxFk7UWFBivHsqrKMz%2Ft1feGG1P6gxMY5z7R5Y5U6CT75bECAxUiuYL22C5syjTzdReJK%2BnnJ1Eu12JWS9AufGGpEoDyduCrypwcLPlDhgdz3YvE00W3IB3brWwk0RM7X%2FFq8jtsC8eYXoDUQnTkwCAZs%2BvNSgB4wS0Rs2RfjWKEpicxdhUaiqEEpXF%2FyQ5bmYOhRLI8r943iQ5w7a6BF8Nfo%2BNxXyiBOJE8TbSG9JT5IQxMG8Kx8tn4%2BGl9BTdHAYYiX8%2FoLh11KLWEbtPFPurad3fMxW5PmwXo4X%2F%2BxPuaR3%2FaPvEduMtpjzqjFgzm1QgIyy9WYaxfP7E7MC1QPLwbSKSXs7AKZkYr%2F9bIIRnzCh5oLTBjqkAe%2FElrD5knxKhgZiPOUvMXKYEuZrf3rpSQja9gaLPd7o%2FenVPz%2BvodoI4ehrn9nR1d%2BhD56sgNWywLk9TFGkoa%2F1Uzeqzoki9yTcQlNz7BDvVbqxMJJGZHLdzwTtk9Nal%2BMX4xRlqQKIjG0xhrbJMPzVrgznn6LS8%2FKHlGAoRorn%2FkP5WHRyqUBSu%2BhYhStrXGqhxROa4%2Flg9tNJnW7zdPkBWihc&X-Amz-Signature=87c5250574399bb6c18b02bba458f47d9c94618eb483f4511431336709ba9a1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5DFSZIG%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T131758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDr3TWUmsGv1giTV2rMtfrSjLLVybLqNUNUuEvYHfA0rwIhANBloXXyNrM8ilKmVd%2BQTMDA%2FYM%2FXUJPTk3qwvcfF4l9KogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOU4Kyjq4y%2BhI01nYq3AMghRVvu5EpLO3yehUfIF%2BTWKvVafoz%2FtRTu%2FeVSaXxLvVfUV%2FM%2FcKadNEcVFsxm%2BxM6YxUlZe9HrsiWa94XgHqutsZhqhZWfU8%2Fg2z3QJBsLdsXccNeUfTuSR68Ttb7%2FcJ%2BXsowkp7oH4U0mKnMXy9gtZyli3SIe%2F2OT9R0IKaqIN89S1oka%2Fr%2B142TICfShv%2Fbk7YUd5lBeerccKgF%2BIi4zeo2OL7onXfJqolGvCulTR7K%2BACkn821ss9dAVuegBZOCbnhl4sWqHcCgPxFk7UWFBivHsqrKMz%2Ft1feGG1P6gxMY5z7R5Y5U6CT75bECAxUiuYL22C5syjTzdReJK%2BnnJ1Eu12JWS9AufGGpEoDyduCrypwcLPlDhgdz3YvE00W3IB3brWwk0RM7X%2FFq8jtsC8eYXoDUQnTkwCAZs%2BvNSgB4wS0Rs2RfjWKEpicxdhUaiqEEpXF%2FyQ5bmYOhRLI8r943iQ5w7a6BF8Nfo%2BNxXyiBOJE8TbSG9JT5IQxMG8Kx8tn4%2BGl9BTdHAYYiX8%2FoLh11KLWEbtPFPurad3fMxW5PmwXo4X%2F%2BxPuaR3%2FaPvEduMtpjzqjFgzm1QgIyy9WYaxfP7E7MC1QPLwbSKSXs7AKZkYr%2F9bIIRnzCh5oLTBjqkAe%2FElrD5knxKhgZiPOUvMXKYEuZrf3rpSQja9gaLPd7o%2FenVPz%2BvodoI4ehrn9nR1d%2BhD56sgNWywLk9TFGkoa%2F1Uzeqzoki9yTcQlNz7BDvVbqxMJJGZHLdzwTtk9Nal%2BMX4xRlqQKIjG0xhrbJMPzVrgznn6LS8%2FKHlGAoRorn%2FkP5WHRyqUBSu%2BhYhStrXGqhxROa4%2Flg9tNJnW7zdPkBWihc&X-Amz-Signature=a2c246e88589398ead25a766918560e78640758f3c2fb1bdaade62e9b1802c08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
