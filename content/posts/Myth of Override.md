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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3PLNIHI%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T114417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6q1e1Ib3ZZWtVSvuN5aEu9DO%2BQhAMpOCB6FZnNtO5NAiEAkVvk%2FWf4hEgveJSIyvd%2BPGXgdcsJyKxoE8lBaAyX9%2BkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3yUToamlzLDT7yDircAzAXF8THgCnDT47CpWWbSx1xZCl5eD5PaDI8zZ0U9JH59%2Bp3nPFjsqywUVybfLbQumg0%2FvU0%2BX1Sbuwq34R7SJk9mI9kUQfULQuC2vcdjiO%2FfmRd1bV7c3I0FWlDvCD8nSogOJMEHzk88pPld3%2B%2B%2BGZDt%2F3YvU7%2F4FBXFQrvJi%2BBDlrjwEKtrI7vOtNYTQAcYbhjEbChGUiuDpcx%2BVxOV%2Fa5FucrPf8%2BzcuA95MJ0ck6QBt%2BT0f30uGurBIc8ZVmxw%2BG2whIhQjOqWknBkkraHfm3C0JCtvMcPURN7WeBaCXY3W%2BgkzGz6jfkHUoUeE6wVGocmHrCizjorBVGG2mh2XDGj%2BQfFyM%2BNzJlmBbi8Pe9rVAHb2Jv71bMY%2BPLg3fb6Q2Qb4kI3YH2lRfD8EDe%2F%2B5wze0T7RxXblvc5e%2BWJ0ASjHHUqY273mAtdODgNvi6tbDgcJhReXKD1d280RVgtEysEP1kiWTQEI6vJZ1ECsM%2BGJFW9mHj1O31Gk54zuSwB6fKadk3Ay%2BmAlFv7MdHmbYc0gmUGDcfB0COA1F6L0l1sFMXnYkVu5rQv%2FAijZeD%2Bbh803OfgwDkuMgQzvSqO9rTdGXzSHrqUBa70aM1M7aSRwDICu%2BWkPLPGvCMLLG7M8GOqUBE3XJM9AH%2FBw7gyQ6qsN292mGmyL%2Fbb4C7Ukst8IG%2BopmVsY37hN9je0evhCgdFXOgnSN7TvL1d1E5SPRxY%2FeJu2dcGpvmh30jticCj79YuoRPFRyhIm1Pgz2pyGpra%2FPR9VRsABfNmru6lzxdcg1FNHWPmn9c5lX4WNLYhkEz0t3wkIXXQ4AAk5pKwUSl4cJU6S%2FlZLSmCVcCxjo4TBByiIDPdhK&X-Amz-Signature=9f4848700943f63297502bcbab08d009e18a4745618714ae53fb93ab3d7a916a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3PLNIHI%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T114417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6q1e1Ib3ZZWtVSvuN5aEu9DO%2BQhAMpOCB6FZnNtO5NAiEAkVvk%2FWf4hEgveJSIyvd%2BPGXgdcsJyKxoE8lBaAyX9%2BkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI3yUToamlzLDT7yDircAzAXF8THgCnDT47CpWWbSx1xZCl5eD5PaDI8zZ0U9JH59%2Bp3nPFjsqywUVybfLbQumg0%2FvU0%2BX1Sbuwq34R7SJk9mI9kUQfULQuC2vcdjiO%2FfmRd1bV7c3I0FWlDvCD8nSogOJMEHzk88pPld3%2B%2B%2BGZDt%2F3YvU7%2F4FBXFQrvJi%2BBDlrjwEKtrI7vOtNYTQAcYbhjEbChGUiuDpcx%2BVxOV%2Fa5FucrPf8%2BzcuA95MJ0ck6QBt%2BT0f30uGurBIc8ZVmxw%2BG2whIhQjOqWknBkkraHfm3C0JCtvMcPURN7WeBaCXY3W%2BgkzGz6jfkHUoUeE6wVGocmHrCizjorBVGG2mh2XDGj%2BQfFyM%2BNzJlmBbi8Pe9rVAHb2Jv71bMY%2BPLg3fb6Q2Qb4kI3YH2lRfD8EDe%2F%2B5wze0T7RxXblvc5e%2BWJ0ASjHHUqY273mAtdODgNvi6tbDgcJhReXKD1d280RVgtEysEP1kiWTQEI6vJZ1ECsM%2BGJFW9mHj1O31Gk54zuSwB6fKadk3Ay%2BmAlFv7MdHmbYc0gmUGDcfB0COA1F6L0l1sFMXnYkVu5rQv%2FAijZeD%2Bbh803OfgwDkuMgQzvSqO9rTdGXzSHrqUBa70aM1M7aSRwDICu%2BWkPLPGvCMLLG7M8GOqUBE3XJM9AH%2FBw7gyQ6qsN292mGmyL%2Fbb4C7Ukst8IG%2BopmVsY37hN9je0evhCgdFXOgnSN7TvL1d1E5SPRxY%2FeJu2dcGpvmh30jticCj79YuoRPFRyhIm1Pgz2pyGpra%2FPR9VRsABfNmru6lzxdcg1FNHWPmn9c5lX4WNLYhkEz0t3wkIXXQ4AAk5pKwUSl4cJU6S%2FlZLSmCVcCxjo4TBByiIDPdhK&X-Amz-Signature=56176f17c88ce5dabfa15c812c843965174bbef069b50ce49fe746555ce7f277&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
