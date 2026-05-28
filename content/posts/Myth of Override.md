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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCYSRNMS%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T100154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEClPPS5RqV%2BpR3ttOSvM1CWA2l79ejzdJ%2FJoDo9GqUgIhAO1ddVReuxTITSFJtsnpW4zC6QAJ%2F%2FKagDdR0GnsBqUDKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaupTN7TPKcuKg99cq3AMV2Iiv3HWkOMon2RZlmaxhwtSA11XlOnRD8ERY8X6WVudWUet%2F%2BXXJQWdSxC6%2FUocIZe4VFHE%2BXArAknr5qBIRwAcEFcYdT%2F0PD7WpffLHx8vXq4m4xrgK%2FPmH%2FSfDNMpocC5DP97KQfA9CAJoF2kKN7xlryYPWX7DDQT1c0YPliGSBQ2ERi1y19TQNAYjErYona96oDqlwLrSdXnE9XnololEMN7N326OoOSxl3kVSskyMvvIu7xRLWBuTS%2FxwdUEtEcZ%2FhiWWXF9Zm%2BShg23nQOUAZH6SIfn9t0m20pmAqRT31hifXPkxECOvDrSyhc2qdG1UUFL0TCb78quomgXLgo9viCe%2BheEHzak92yi8XhIqg3KFRwmXw5J8v4kXhGC5n7AqBWbcYlm3d%2BUD0Bem18T%2BG%2BYIfTFZ%2F1FNS3NbhVRgtnRx1K21MLYOLen2XtdBIiu0OKxK6sZB25UbvyZl4%2FM72eawFiCURU3ShcWRuCTCG6QwAbADVgqOngg9llJz%2Bu10ZWPh3B%2B3xAg%2Bd%2BVOjzyE4gwpqewIu60dSnZ01u1se8lQWlVR7o78QHVTZDD6IfXWO5JqSRFI6ek%2BMr8RDC8ciCN2uJv9ujX6%2Be3DWqwq2p4G2EQ8CDNOzCpkODQBjqkAd%2F1r6LzWWoeiFVkyCuxaXE23rAl0NA10S15dOPT2CsqXjK%2F3Ew2GV74MQ3%2BgrcL%2FV48Sf2prEsq3NdRcdl3xgaMvLE%2BFMhRgQ8dHQeC9h2vBNf31mlL7BV16ty5r6TSyjb4WxCNJOjnnNpG242bmJglbXRVV6LPgazuyHkyQ58nLJAJpjdTdKk921c8FEK9VKnBx7ZptNFQncOPeZOQD8EYRfVp&X-Amz-Signature=cf7849c093484d4a777375071a370c6532672e0f4767b4a7e8b2304c986090f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCYSRNMS%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T100154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEClPPS5RqV%2BpR3ttOSvM1CWA2l79ejzdJ%2FJoDo9GqUgIhAO1ddVReuxTITSFJtsnpW4zC6QAJ%2F%2FKagDdR0GnsBqUDKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaupTN7TPKcuKg99cq3AMV2Iiv3HWkOMon2RZlmaxhwtSA11XlOnRD8ERY8X6WVudWUet%2F%2BXXJQWdSxC6%2FUocIZe4VFHE%2BXArAknr5qBIRwAcEFcYdT%2F0PD7WpffLHx8vXq4m4xrgK%2FPmH%2FSfDNMpocC5DP97KQfA9CAJoF2kKN7xlryYPWX7DDQT1c0YPliGSBQ2ERi1y19TQNAYjErYona96oDqlwLrSdXnE9XnololEMN7N326OoOSxl3kVSskyMvvIu7xRLWBuTS%2FxwdUEtEcZ%2FhiWWXF9Zm%2BShg23nQOUAZH6SIfn9t0m20pmAqRT31hifXPkxECOvDrSyhc2qdG1UUFL0TCb78quomgXLgo9viCe%2BheEHzak92yi8XhIqg3KFRwmXw5J8v4kXhGC5n7AqBWbcYlm3d%2BUD0Bem18T%2BG%2BYIfTFZ%2F1FNS3NbhVRgtnRx1K21MLYOLen2XtdBIiu0OKxK6sZB25UbvyZl4%2FM72eawFiCURU3ShcWRuCTCG6QwAbADVgqOngg9llJz%2Bu10ZWPh3B%2B3xAg%2Bd%2BVOjzyE4gwpqewIu60dSnZ01u1se8lQWlVR7o78QHVTZDD6IfXWO5JqSRFI6ek%2BMr8RDC8ciCN2uJv9ujX6%2Be3DWqwq2p4G2EQ8CDNOzCpkODQBjqkAd%2F1r6LzWWoeiFVkyCuxaXE23rAl0NA10S15dOPT2CsqXjK%2F3Ew2GV74MQ3%2BgrcL%2FV48Sf2prEsq3NdRcdl3xgaMvLE%2BFMhRgQ8dHQeC9h2vBNf31mlL7BV16ty5r6TSyjb4WxCNJOjnnNpG242bmJglbXRVV6LPgazuyHkyQ58nLJAJpjdTdKk921c8FEK9VKnBx7ZptNFQncOPeZOQD8EYRfVp&X-Amz-Signature=3a5d875729ae464f6325195b3153aaadb756cb7f622293d4e988702bed8c1a1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
