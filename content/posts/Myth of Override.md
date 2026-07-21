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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MIFGELR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T205746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZQOYnLahx0aLx1V3tDuGIP%2FdvQcBMACgdaklzpBaPeAiEAzqRqS%2F0DOSQJlwPVVs%2Ft9WuprvoATuTpVQf%2Fc%2FJIZP0qiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCFVeynP9wHbqOKEkircAytonWxkhWU72vC8B32NNCvzj%2B%2BbDfdoC9THDiuC1uCSUULJPzTS8BRZllJsUB9%2BU9PPjzEqZE81hdbKnuQgFfac4TPYVF9bteWS8uVhIXAM92TU4i9tvZO0LOti2MXbO9KBdtb1lfeY%2FshCsl7rcxXj%2BlhDnROZ%2FN492j%2F3iIzECn3e1vR2dO8CZNshRtAzoATpCgE2TVIkDh3IxG0bqJ6mkx4iaIEjmX7b4%2BQRA8XN14n4UU2HOl1ZYjRBBnIExWkkyH4%2BnIcwklSuDpSyHJM%2F7U4eFzC8T4MndsLnBfrZCR1B38n2aC4S2RoCV7tzBmwz50Dy1qRsBPT4ZWSIXV9XCSmIOfsuZm%2F7%2B0ngEA2izfOiF04BEuVCaapjTegnJ3UWGXz2QN0f1H3IbqIUh1QC70lbKs%2B1h%2FJqxgERoUuZTckbP0m6dQ8f6RoMiOfaoJ114dqfave8aWx41cT5MDMRWai3I7jVClLqyAZzWwnnzK7knUtJnHP%2Bmf9bkG5opsyfOX6hwrZnL%2BqxCjDg5Br8hA2nnpFT77NTXkS5DxmfTW326a%2FfVlDXJpDmI%2BF4FIC%2B4mEjB25h%2B4rKtP2WXYQ6wo%2B%2BKfWXyEhbCDYOvw69oUaRR4odN%2F9CxJscMN6q%2FtIGOqUBF5bgzRidHeP7PSTkzpH9pP67ag5YvD95Lm09Z2v%2FBIa2ECBx%2F3rVvMK9vWj3yVRB7m9%2Fgd2MrxQ2tCbLssaVxNQ6fG9PjBCxuDQCetiL5NfWvxW%2BWOsSAV0%2BpLh7jP7l9Gr0nvioEQsUq7z9lvUKfRzC%2Bw%2FCM2Dbuzz00Bma40FJubRJZYqDXlwVmN4M8%2Fq%2F4T%2BSjGQ84VvXye0IwTeT3MB1OrZ%2B&X-Amz-Signature=54feb7353436b807818878c075ef3eb22ff166efd57f7cf0c37ca6fa32d996a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MIFGELR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T205746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZQOYnLahx0aLx1V3tDuGIP%2FdvQcBMACgdaklzpBaPeAiEAzqRqS%2F0DOSQJlwPVVs%2Ft9WuprvoATuTpVQf%2Fc%2FJIZP0qiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCFVeynP9wHbqOKEkircAytonWxkhWU72vC8B32NNCvzj%2B%2BbDfdoC9THDiuC1uCSUULJPzTS8BRZllJsUB9%2BU9PPjzEqZE81hdbKnuQgFfac4TPYVF9bteWS8uVhIXAM92TU4i9tvZO0LOti2MXbO9KBdtb1lfeY%2FshCsl7rcxXj%2BlhDnROZ%2FN492j%2F3iIzECn3e1vR2dO8CZNshRtAzoATpCgE2TVIkDh3IxG0bqJ6mkx4iaIEjmX7b4%2BQRA8XN14n4UU2HOl1ZYjRBBnIExWkkyH4%2BnIcwklSuDpSyHJM%2F7U4eFzC8T4MndsLnBfrZCR1B38n2aC4S2RoCV7tzBmwz50Dy1qRsBPT4ZWSIXV9XCSmIOfsuZm%2F7%2B0ngEA2izfOiF04BEuVCaapjTegnJ3UWGXz2QN0f1H3IbqIUh1QC70lbKs%2B1h%2FJqxgERoUuZTckbP0m6dQ8f6RoMiOfaoJ114dqfave8aWx41cT5MDMRWai3I7jVClLqyAZzWwnnzK7knUtJnHP%2Bmf9bkG5opsyfOX6hwrZnL%2BqxCjDg5Br8hA2nnpFT77NTXkS5DxmfTW326a%2FfVlDXJpDmI%2BF4FIC%2B4mEjB25h%2B4rKtP2WXYQ6wo%2B%2BKfWXyEhbCDYOvw69oUaRR4odN%2F9CxJscMN6q%2FtIGOqUBF5bgzRidHeP7PSTkzpH9pP67ag5YvD95Lm09Z2v%2FBIa2ECBx%2F3rVvMK9vWj3yVRB7m9%2Fgd2MrxQ2tCbLssaVxNQ6fG9PjBCxuDQCetiL5NfWvxW%2BWOsSAV0%2BpLh7jP7l9Gr0nvioEQsUq7z9lvUKfRzC%2Bw%2FCM2Dbuzz00Bma40FJubRJZYqDXlwVmN4M8%2Fq%2F4T%2BSjGQ84VvXye0IwTeT3MB1OrZ%2B&X-Amz-Signature=379940ee3442b8f3987b47204a8b792c4340366e597515eb345236771b1b2466&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
