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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7GTNUWZ%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T020102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCZN1YqyhEFd2f6b%2B40rrcFdzNhxJALuVuyAVzQAeaF0AIhANEG51sRmbHLPTDSg2OHKI0XgWrtzZA9FlrQfSvxkv8FKv8DCCsQABoMNjM3NDIzMTgzODA1IgzZS%2FKHO6zRLUwOPPYq3AOlurH4XrTm%2ByQzMXPD58gKgUOEt69tO0LFk73KahN0iHdPnlV6DqZChi%2FKRJkRqKDhwQwB7RO75eU3sfGbTLSf78Iq1QzhjV1Ahq1GO2%2FKNnJJpr2jZpeE9l%2BpcNpA1tmkBMUWVS2TQSVFAeK1ER4zOjCwurLZFN8%2FfyWzL3Sxy7pWbzeD%2BNQd2WTn5JUgnUZOZYyMHC0jHgPe3PpJSSnXkExtL38hVoAp633PGyEUzBjbRVihNqYAX%2FjfrmDrC3pZwyNSsxbEQtZkEN9DUCYIicuUU661wNdhzzEXIlMX31dKtMv8fm6h10lwhkQyAD2W0s0UI5AjAs4s0xtDTi2NfcVBqXYGVKZ6%2BSwHPNQU9%2BnPlwBE9ZrBb4MUDD0sH0IASx%2Bh0apt3QvpE7lAEIut0U%2BDHTafRu%2FMeWqlDSwssLr8Bi9VIG2qhgLBWGpYoLWJ56F5jp71oAjjF0HtBmoZ3%2FY8CRfvfHM%2BZ7nek3yGzMe2qfBvugR6j7XgPdA6gwyi8s4WLmYgdDBk%2B%2BFTxvWw162bkqKUJGNxRZbLUuTgjKSEX6SDgp6Ih%2BhFlsKGNRfJ84tdJ7WICGZ7W0GKRu0lxIXlKfX8kp25Gesbm9SeeFyAA2xNcYumaFM7TjDi7uzRBjqkAV61Tj3%2ByfXyxvNpAGKpqEUq8hbY71wA0ib5R57U7uzM2VQ223jMPD8K695qwPux0TYcGUDhzeZ1x%2FEsTXUThkl5qVs8rprEvMlrxvfnKxDE98IefSPphMgyj9dob%2BJ8sEpACsYU24JU7fshH41FjGBFRjQXzJsRGRTlgmmxoVcbXBQPkNUCdqa7iU8tlpaYMJMF89SjKesG8FsZjYlcDFazbCFn&X-Amz-Signature=97dd97c7b54239fdbb3ccf00eefb7dabb942b4642fd4984ca3bebdad65c769e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7GTNUWZ%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T020102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCZN1YqyhEFd2f6b%2B40rrcFdzNhxJALuVuyAVzQAeaF0AIhANEG51sRmbHLPTDSg2OHKI0XgWrtzZA9FlrQfSvxkv8FKv8DCCsQABoMNjM3NDIzMTgzODA1IgzZS%2FKHO6zRLUwOPPYq3AOlurH4XrTm%2ByQzMXPD58gKgUOEt69tO0LFk73KahN0iHdPnlV6DqZChi%2FKRJkRqKDhwQwB7RO75eU3sfGbTLSf78Iq1QzhjV1Ahq1GO2%2FKNnJJpr2jZpeE9l%2BpcNpA1tmkBMUWVS2TQSVFAeK1ER4zOjCwurLZFN8%2FfyWzL3Sxy7pWbzeD%2BNQd2WTn5JUgnUZOZYyMHC0jHgPe3PpJSSnXkExtL38hVoAp633PGyEUzBjbRVihNqYAX%2FjfrmDrC3pZwyNSsxbEQtZkEN9DUCYIicuUU661wNdhzzEXIlMX31dKtMv8fm6h10lwhkQyAD2W0s0UI5AjAs4s0xtDTi2NfcVBqXYGVKZ6%2BSwHPNQU9%2BnPlwBE9ZrBb4MUDD0sH0IASx%2Bh0apt3QvpE7lAEIut0U%2BDHTafRu%2FMeWqlDSwssLr8Bi9VIG2qhgLBWGpYoLWJ56F5jp71oAjjF0HtBmoZ3%2FY8CRfvfHM%2BZ7nek3yGzMe2qfBvugR6j7XgPdA6gwyi8s4WLmYgdDBk%2B%2BFTxvWw162bkqKUJGNxRZbLUuTgjKSEX6SDgp6Ih%2BhFlsKGNRfJ84tdJ7WICGZ7W0GKRu0lxIXlKfX8kp25Gesbm9SeeFyAA2xNcYumaFM7TjDi7uzRBjqkAV61Tj3%2ByfXyxvNpAGKpqEUq8hbY71wA0ib5R57U7uzM2VQ223jMPD8K695qwPux0TYcGUDhzeZ1x%2FEsTXUThkl5qVs8rprEvMlrxvfnKxDE98IefSPphMgyj9dob%2BJ8sEpACsYU24JU7fshH41FjGBFRjQXzJsRGRTlgmmxoVcbXBQPkNUCdqa7iU8tlpaYMJMF89SjKesG8FsZjYlcDFazbCFn&X-Amz-Signature=04fcc303710e59ff9ecae344a093b2d16fe4f96e8d5b1547bc134a32790b8b3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
