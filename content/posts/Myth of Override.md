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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCX5UUUL%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T195801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCqrBxJVF2Ds8xtDFQZNGsiQ%2BylX5iYgKR4mU%2Fq0vxa%2FAIgBb9CgRcpokiGX7ghmSI9TGjBK2qtDHVcMcjIZL8tj3UqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPHEf1IZsdyPvkR2yircA7tQ1OODqZFHdV8ElwFE22Bq%2BdWjze%2FNYcMRpZrNt3OnFf3ziQWvC1qEIXGmpT9PM8k6PONqL5o668KxeVPdtCycrYndC8W65oRyMm8WoeQdEMgYJbTpIwUcZSPtQ7MnZUGDI6ezywJAGZ%2BB5Hut4ZOq8JkjezrnzFa6%2Fdey22%2F8w%2FXbDaSwMFrg106JWZ%2FkPZW0wDFdDW%2FD2GqY7WA3f%2BrAU0iahp3QGRwwA%2BQON3ndLFtitopJtRHyC%2F3vAXuGBHKPkLrn4j6LqomvecaWVQGy%2FpfQys6m9%2FXOR9XKmu9gZt9oIMndmr5cbGdOxYfj1ewo%2FXl%2FTD5E5uaXogHhbMfiz9BuEbtIbbUT7WBrI2RCeTzPAZd6RKZd%2F3JcjxtlB%2BNkkyZM7Tx71r%2Beuy%2BncB%2BykUTT1lHOAOUzyPTVaosK%2FGqfSzaMjma%2F53gA9m32V2HvDcnPVfsth468OfdbBZaDWA%2FIFzi8SImLzgo0kJYdgh8u2kQDoUNr8CUUmKQjlc8UGw9yXdzWSh0vNn1MlRyeIfTyCff3EcsjsMPqLI7NFYio22kfqQQQpcCYsJxK9qj%2FS%2FU4sPtTbbW2I3U5pTVmDSRx%2ByYykdX7tfpYstIkhJm%2BrkZfL4DCB3jYMI7Pm9UGOqUBbWjKlXNypCSLMNjQPhcUMAa1gjbK%2BoVmBO%2Fr0z5TTbahhL%2FCGrTAr%2BEjjX8sT33EON2si4VVJ%2FzDzzPuOB4i5Ae%2BWZ2xS9IJkcK%2BYDfxhR7IDwJiWmAcR3t7kEjDGco5H7x1%2Bsy9rOu5nEZOdpQx48Mnw9lxkkU%2BG6tJUcw%2BjNS0CuSsxKCDG2ShpqrqNYG%2Fjh1RbHXFH2kwyB4fdX1cSeke1ss1&X-Amz-Signature=f7fb574afd24372bfcd67a49059130fe8ecba1e2a349bf18148f6e4cd2c17ea3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCX5UUUL%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T195802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQCqrBxJVF2Ds8xtDFQZNGsiQ%2BylX5iYgKR4mU%2Fq0vxa%2FAIgBb9CgRcpokiGX7ghmSI9TGjBK2qtDHVcMcjIZL8tj3UqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPHEf1IZsdyPvkR2yircA7tQ1OODqZFHdV8ElwFE22Bq%2BdWjze%2FNYcMRpZrNt3OnFf3ziQWvC1qEIXGmpT9PM8k6PONqL5o668KxeVPdtCycrYndC8W65oRyMm8WoeQdEMgYJbTpIwUcZSPtQ7MnZUGDI6ezywJAGZ%2BB5Hut4ZOq8JkjezrnzFa6%2Fdey22%2F8w%2FXbDaSwMFrg106JWZ%2FkPZW0wDFdDW%2FD2GqY7WA3f%2BrAU0iahp3QGRwwA%2BQON3ndLFtitopJtRHyC%2F3vAXuGBHKPkLrn4j6LqomvecaWVQGy%2FpfQys6m9%2FXOR9XKmu9gZt9oIMndmr5cbGdOxYfj1ewo%2FXl%2FTD5E5uaXogHhbMfiz9BuEbtIbbUT7WBrI2RCeTzPAZd6RKZd%2F3JcjxtlB%2BNkkyZM7Tx71r%2Beuy%2BncB%2BykUTT1lHOAOUzyPTVaosK%2FGqfSzaMjma%2F53gA9m32V2HvDcnPVfsth468OfdbBZaDWA%2FIFzi8SImLzgo0kJYdgh8u2kQDoUNr8CUUmKQjlc8UGw9yXdzWSh0vNn1MlRyeIfTyCff3EcsjsMPqLI7NFYio22kfqQQQpcCYsJxK9qj%2FS%2FU4sPtTbbW2I3U5pTVmDSRx%2ByYykdX7tfpYstIkhJm%2BrkZfL4DCB3jYMI7Pm9UGOqUBbWjKlXNypCSLMNjQPhcUMAa1gjbK%2BoVmBO%2Fr0z5TTbahhL%2FCGrTAr%2BEjjX8sT33EON2si4VVJ%2FzDzzPuOB4i5Ae%2BWZ2xS9IJkcK%2BYDfxhR7IDwJiWmAcR3t7kEjDGco5H7x1%2Bsy9rOu5nEZOdpQx48Mnw9lxkkU%2BG6tJUcw%2BjNS0CuSsxKCDG2ShpqrqNYG%2Fjh1RbHXFH2kwyB4fdX1cSeke1ss1&X-Amz-Signature=34b7803e1f816abde89ac9d60c2da63c499d1370802efee5a02d8bc2bf0e12b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
