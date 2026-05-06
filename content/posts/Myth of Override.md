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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDVCDTSO%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T080455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC43aawHPsHbNIrmRq2vN2him3dQik%2F2AejEp%2F4ofKADAIgOH835SflewaTYJo%2B1TrVdf818H6Ukb3ZQxd%2Fd0K7NwMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMSoaYxGxfGoD%2FsTircA9ujPOVgfk3Naat1CrR264DiWMBLIYFNPyl5Wr7IpQwm5G%2FZpaCp3V7ArLtM%2Buf3Hco4ZZD1gUnML90g3Tx2PAwAo%2Fcfe2rQz4bTD2XoAeZ%2BFBIrGy%2Bp0wwueObO17S6x5LQMMe7LWMkTbpQc7gOw%2FSAHB61UgMjOwtHcooM77zsFeWrgwvarLNuDTPD9BsMLplE0auwZ%2FDE90gs%2Bx00bsINcxjWcz8vvUeOHGlf%2B9HR4FNl7HZCeG9GyFvazChDveyjUdcyeU%2FszlvdVWXZy7b0Z%2FcWzVQ9IOLf3%2BwYEhJSBjw7AkbwwInN2AxbGfQRZuAMtCEsbWFbjz93r6%2FG3JlU%2FBMhWtLUvzbiVNjacZdb0Fjs%2BXpPyx8RRGiYbIU%2BqQx%2FDHiYTocmZkUV89zV8jPiXs9uclZlpGh1yJnYTJVFNl%2BRC%2BL5NRDPhwtEZJh71vSn6ijHM2gAnYCfCL1oWMWRVqQxpW9o36UpDVJy0GzCkrg9jN7SCxA%2Fsu9DKAqdBUbH0buTdrmhQ5OFQo8lUDhUgUjolC7LXwn5Zvx2pMaV9pYaG1ipTtbBDx8Ki7tlEReQArc2tEfa0aX3M9qNy8zDWz%2FJWfeky%2Fx4tsPHFeueBiz10ZUzKRXwb6FCMPrd688GOqUBfKpunWBw3kdT8kWDhZ7mPz9ck0TbAyRuvQkSFi4YbRbNEZFNjWlGpPRpyK%2Ba%2FGwZvCsK2x0QTaz%2B6Z2B3lV2GPQlThtBUQ%2BslHGxcV05lhfkAwy%2FhzQBzTEuCWGp%2B%2BRav2SYLLjDoW%2FPLbJSsI0ue%2BoIUkoG4eUeoe3YGsqvI%2BwbBSqveNKJ7064eHSeKGYpqfjnrDuX%2Fymn6%2BIC3UmzAIztLFhS&X-Amz-Signature=4ee2bca599f094c59618a87749b6c44185570bd3386d28c04f5a2995ef8e07bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDVCDTSO%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T080455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC43aawHPsHbNIrmRq2vN2him3dQik%2F2AejEp%2F4ofKADAIgOH835SflewaTYJo%2B1TrVdf818H6Ukb3ZQxd%2Fd0K7NwMqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOMSoaYxGxfGoD%2FsTircA9ujPOVgfk3Naat1CrR264DiWMBLIYFNPyl5Wr7IpQwm5G%2FZpaCp3V7ArLtM%2Buf3Hco4ZZD1gUnML90g3Tx2PAwAo%2Fcfe2rQz4bTD2XoAeZ%2BFBIrGy%2Bp0wwueObO17S6x5LQMMe7LWMkTbpQc7gOw%2FSAHB61UgMjOwtHcooM77zsFeWrgwvarLNuDTPD9BsMLplE0auwZ%2FDE90gs%2Bx00bsINcxjWcz8vvUeOHGlf%2B9HR4FNl7HZCeG9GyFvazChDveyjUdcyeU%2FszlvdVWXZy7b0Z%2FcWzVQ9IOLf3%2BwYEhJSBjw7AkbwwInN2AxbGfQRZuAMtCEsbWFbjz93r6%2FG3JlU%2FBMhWtLUvzbiVNjacZdb0Fjs%2BXpPyx8RRGiYbIU%2BqQx%2FDHiYTocmZkUV89zV8jPiXs9uclZlpGh1yJnYTJVFNl%2BRC%2BL5NRDPhwtEZJh71vSn6ijHM2gAnYCfCL1oWMWRVqQxpW9o36UpDVJy0GzCkrg9jN7SCxA%2Fsu9DKAqdBUbH0buTdrmhQ5OFQo8lUDhUgUjolC7LXwn5Zvx2pMaV9pYaG1ipTtbBDx8Ki7tlEReQArc2tEfa0aX3M9qNy8zDWz%2FJWfeky%2Fx4tsPHFeueBiz10ZUzKRXwb6FCMPrd688GOqUBfKpunWBw3kdT8kWDhZ7mPz9ck0TbAyRuvQkSFi4YbRbNEZFNjWlGpPRpyK%2Ba%2FGwZvCsK2x0QTaz%2B6Z2B3lV2GPQlThtBUQ%2BslHGxcV05lhfkAwy%2FhzQBzTEuCWGp%2B%2BRav2SYLLjDoW%2FPLbJSsI0ue%2BoIUkoG4eUeoe3YGsqvI%2BwbBSqveNKJ7064eHSeKGYpqfjnrDuX%2Fymn6%2BIC3UmzAIztLFhS&X-Amz-Signature=4bf55d337db61f56fe95b4ef307214232b1010d751d869653b8a011aa2d4626b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
