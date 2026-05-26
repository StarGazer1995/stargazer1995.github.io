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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFT4IJC%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T015819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBOVL3ocWITcFDuB48NDVKmHsOBQUZDzTLaRn73UrZqAiBw%2Fxr6fhWfEKOLhDxwtcp%2BMC1M%2BrkzDv3modnlA%2FFMCSr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMP1hEJZgtxDSc08ZbKtwDctHAfBT2yjkThDqFqb4BBwfJMnS9YezcUH21gjZ%2BIBsuou5ztK9W6TfrZn0zkakWmE1SBPV7WR9yrxeD%2BoJLqqWQ2vYP%2F%2BjLmmIr5zQ9ADOyubF%2B5%2BwcF1R3BNtPVMMdtEbN1x6ElKIL%2FId%2FjxFtVjR37bgazAV3KRjV286%2B0aAtGHeIp06orvUirK8vE%2FkkrVnePj%2FubEUk9fXveqjhcz8FU7MTAS%2BIhzhoUCpspGB5CzsPGbvdAqgn5BgZk%2B5tZQbC6K57RLzY0o9QZGl37rqelyLaJW8iL4SEZo0Ivpf47qf%2Fj%2Fb0wYqA6xS0xqyjj6TYGJ9TZRDeUpIhqNmhAmONKQx%2BGCTBH5M4WoFVurYUtottIOm1%2FLCLxZOod5gqy990eqYXrnEUq6AZJmZdgKG3l7cSXP5eDNeMBi9JD8h88WcMa7SN8MJ5rXkoXAQX4Q6bHCCRlaRnD2QHoQW%2FM249OLReTiDoFTE34wb9IXiJbhfAXclDF7bkM88E6tax9cd8xiZL1Skmfw8JnuqHyvdmq0jwLYoP38sL768teeWe7Lgb3P70OpCxZ1cRRDTVpmE1aNVqWRq9tydNwbKniqJXm3m3ITszZpAGIIW%2FgDOCsGjtUNteo%2FSYMbswu%2FjT0AY6pgF7KR7KsVBkJLhzgWtZzhAMdTYsKAv8M3%2BRa8jzGPVVYP8xAHbXRUa7JLphDbU2pT%2BZhH8l%2Bp5vVPSIj8xjsQ1WmjXl4srWIvWBYVPJxW6dcGWC59ZZpXrH%2Fc%2BygiFxfLRZyxYrjJ4K0Ix8WALs0dbRO9Pk3mi7any9rSV8sFbCtgrXTbbvxD%2B2E9RZScpNOaC6FimANiB5xBr9qWhhjxABodgwkV5M&X-Amz-Signature=1856d4542c560ef99773856e8e1aea345f802d46124378a08ae416965db3ccf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFT4IJC%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T015819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBOVL3ocWITcFDuB48NDVKmHsOBQUZDzTLaRn73UrZqAiBw%2Fxr6fhWfEKOLhDxwtcp%2BMC1M%2BrkzDv3modnlA%2FFMCSr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMP1hEJZgtxDSc08ZbKtwDctHAfBT2yjkThDqFqb4BBwfJMnS9YezcUH21gjZ%2BIBsuou5ztK9W6TfrZn0zkakWmE1SBPV7WR9yrxeD%2BoJLqqWQ2vYP%2F%2BjLmmIr5zQ9ADOyubF%2B5%2BwcF1R3BNtPVMMdtEbN1x6ElKIL%2FId%2FjxFtVjR37bgazAV3KRjV286%2B0aAtGHeIp06orvUirK8vE%2FkkrVnePj%2FubEUk9fXveqjhcz8FU7MTAS%2BIhzhoUCpspGB5CzsPGbvdAqgn5BgZk%2B5tZQbC6K57RLzY0o9QZGl37rqelyLaJW8iL4SEZo0Ivpf47qf%2Fj%2Fb0wYqA6xS0xqyjj6TYGJ9TZRDeUpIhqNmhAmONKQx%2BGCTBH5M4WoFVurYUtottIOm1%2FLCLxZOod5gqy990eqYXrnEUq6AZJmZdgKG3l7cSXP5eDNeMBi9JD8h88WcMa7SN8MJ5rXkoXAQX4Q6bHCCRlaRnD2QHoQW%2FM249OLReTiDoFTE34wb9IXiJbhfAXclDF7bkM88E6tax9cd8xiZL1Skmfw8JnuqHyvdmq0jwLYoP38sL768teeWe7Lgb3P70OpCxZ1cRRDTVpmE1aNVqWRq9tydNwbKniqJXm3m3ITszZpAGIIW%2FgDOCsGjtUNteo%2FSYMbswu%2FjT0AY6pgF7KR7KsVBkJLhzgWtZzhAMdTYsKAv8M3%2BRa8jzGPVVYP8xAHbXRUa7JLphDbU2pT%2BZhH8l%2Bp5vVPSIj8xjsQ1WmjXl4srWIvWBYVPJxW6dcGWC59ZZpXrH%2Fc%2BygiFxfLRZyxYrjJ4K0Ix8WALs0dbRO9Pk3mi7any9rSV8sFbCtgrXTbbvxD%2B2E9RZScpNOaC6FimANiB5xBr9qWhhjxABodgwkV5M&X-Amz-Signature=ed52ee274217f16db5accde9a9a1740a3a94408643eb5be7817d8f339ceeb7a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
