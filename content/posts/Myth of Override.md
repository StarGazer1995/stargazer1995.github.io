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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2GJNZ74%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T210947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCOc%2FqSz7%2FguEpgfxBkxkQP4ck12aKQMwQJYmnI7tpooQIhAPbI3nnLOdnVO82WYYUflXK7AmiwYQrcQM5NSrQ6ixLcKv8DCB4QABoMNjM3NDIzMTgzODA1Igz0pIZcuVEFQMwsuWoq3AMvuokeXe4XG8O3f4uEXwphePOph%2FUA2PwDWiYjnurLnqN6bk7J6kOEpt94YZm7xTMaCAhAxnc08PJ24KdLuYjz2G6PO00WsxO%2B%2FXH7GPyF1mLmCuoJQWO8ODtBqf2RgqXhvHGXySVr4i2jQK0CvzSZSL0pFTejo7Ssm2SNVGmnFdGWS7EaCbFPCj9yw1IBTHt8fXt8j7WC6gDbZ9HfM%2FG6GQ5wIo0XO8MIcDtyA2F5m89VDte%2BT2WHW2qv2%2B%2BDq0WoOxB0YnWVkZxcVS%2FTfowhp83VzhART4d66Yi%2FfbRhjMiTNNg%2FS8i71wTxprucDCl%2BZs6raT825aak%2FS%2BV%2BFE04WlIP3h4O%2FRjqsx2PTRUOfrabZtwq794V7PCfsP1Gl0tEERGYV6SNBzyl3e8IgixkFrDt3bsJPmk39OzLOyowlr92HyY9bIqT5wUo30JlIK3pqUC2UgeE4ZUufKsj4OVsW69fIruIE2xzGEbAA8DLENPiNvl265i1qbbK2XgJ1BlRTop1DzyNLiHy%2BJThPebMw9mSBzoA%2FFXslxdtflX6f3r%2BtJdXA1hVOm7xQZ0xrnYYl7OTqpOlvZissA1Tiw51SsOaV00oGlykFD7SBjZE01AzAZCC8dWdMlByDCvionQBjqkAVb4JY0wjv3KaKdljJlLygExlA4Ujr%2FvZ%2FyI4bUdkIyqcW%2FNLM836NHQQX7p4EIDxImP24hSjsWdIEQ10ECS%2FE3oE3g%2Bsh4036bsMiDMkVHhV2h0qp4Im5cDLXBRHag9vY6su6SB%2BTR73bB8nXHdZAbFyDGfWdYSmx4KDlVJrU1aytuTxQ8cmySV3VVlGhwPVGreR6I8qPBxhPG4NjmF5VeTKXq%2F&X-Amz-Signature=b01f321db801392f9f338ae3a8a9fa80cc661b3327cd81a7ed3eca52c4055c11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2GJNZ74%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T210947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCOc%2FqSz7%2FguEpgfxBkxkQP4ck12aKQMwQJYmnI7tpooQIhAPbI3nnLOdnVO82WYYUflXK7AmiwYQrcQM5NSrQ6ixLcKv8DCB4QABoMNjM3NDIzMTgzODA1Igz0pIZcuVEFQMwsuWoq3AMvuokeXe4XG8O3f4uEXwphePOph%2FUA2PwDWiYjnurLnqN6bk7J6kOEpt94YZm7xTMaCAhAxnc08PJ24KdLuYjz2G6PO00WsxO%2B%2FXH7GPyF1mLmCuoJQWO8ODtBqf2RgqXhvHGXySVr4i2jQK0CvzSZSL0pFTejo7Ssm2SNVGmnFdGWS7EaCbFPCj9yw1IBTHt8fXt8j7WC6gDbZ9HfM%2FG6GQ5wIo0XO8MIcDtyA2F5m89VDte%2BT2WHW2qv2%2B%2BDq0WoOxB0YnWVkZxcVS%2FTfowhp83VzhART4d66Yi%2FfbRhjMiTNNg%2FS8i71wTxprucDCl%2BZs6raT825aak%2FS%2BV%2BFE04WlIP3h4O%2FRjqsx2PTRUOfrabZtwq794V7PCfsP1Gl0tEERGYV6SNBzyl3e8IgixkFrDt3bsJPmk39OzLOyowlr92HyY9bIqT5wUo30JlIK3pqUC2UgeE4ZUufKsj4OVsW69fIruIE2xzGEbAA8DLENPiNvl265i1qbbK2XgJ1BlRTop1DzyNLiHy%2BJThPebMw9mSBzoA%2FFXslxdtflX6f3r%2BtJdXA1hVOm7xQZ0xrnYYl7OTqpOlvZissA1Tiw51SsOaV00oGlykFD7SBjZE01AzAZCC8dWdMlByDCvionQBjqkAVb4JY0wjv3KaKdljJlLygExlA4Ujr%2FvZ%2FyI4bUdkIyqcW%2FNLM836NHQQX7p4EIDxImP24hSjsWdIEQ10ECS%2FE3oE3g%2Bsh4036bsMiDMkVHhV2h0qp4Im5cDLXBRHag9vY6su6SB%2BTR73bB8nXHdZAbFyDGfWdYSmx4KDlVJrU1aytuTxQ8cmySV3VVlGhwPVGreR6I8qPBxhPG4NjmF5VeTKXq%2F&X-Amz-Signature=d90c25c10c8ad7f53bf11618fac6bf9d416b21e784f47d21da9ae9a20dc895c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
