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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y4L6HW7%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T190837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPQAz3MplqVm4oHCynqtQO69%2F0Ixuce3Ym553kcrgzhgIgAeWpV9zw5qTp6crKF4dzJko%2FzKKCtO0eCtB%2BE7uNWPQq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDLMFy0lML6CO9wyaFyrcA3WosoXNx7kFYo2o7bFof18MgqIZJuhgNcqXc5hp2%2BqDuiWVKXF8IcbI4SjlfTtiXqPrB6YtqaBw6uVvOoTAYPy5QUGCQx817R5Sf81qsKXDetPDufbSN65DH6u%2FwZuUgxT%2FS1NtHHU6%2FnpMYJ%2BOeeZc28vRkg4BR%2FT4lNgdkM%2FDnckdtnuCILu%2F8E4MPWmNdcIcwbEf%2FzakwpPnjedh3DleqWd9Y6Pc%2BKZFvyCb3usUDRX4aCrldYkVW1RADHxMf1rszwF48TDJOEaQ7ey1qQfLHmW2d0Sb%2BSGukjvipA4y04DfYG7m%2Fiyk7%2FkZDO%2BUO420r77JmR6iAMtiV4iuKrZeb0ZEUgXsa1uE2%2FmnjAVG39V9aFPlBGmZSJDDv%2BdvoQKedQTzOcxoP1uZIw4Zb0Pt0jNHdbiKO0Xq%2Fn%2F5Es%2FRgh5wf%2FmPFd2gFxJqN6pu2EQzi9q4DeG6cu3pTkUWxvHNyeAOVI84BBKkQqENRSuM219Y19KBpbJyFgUlPWxpNnAgYUKSE4S8pouYzTcwcM3BLOyHwh9nfwjs0hb3EceairgIYppOsq818wmA4xQfssCm9i5fJQh6inc%2Bcg9PJTI3OV7Q%2FUaSHMUlCA4%2BaKW7SL%2FQdSswDSMFgxcsMO7FntMGOqUBOLhnGBUHD%2BEjbpekvETS0MVyGeJgSJk3Q5TikBO2WBpaPRSkBK%2FaaydpzXpcU3k0sC4zmuZwP0XsFWaWIOZHvvl7O8J84DAxn1WdVVKj0M1r8BHh3P7yTMvc2BNdgQ0r2Lm%2FkP9j0512VwrBmLnmM8nImMShPTpi6fVdvnCnDGNWZ%2B22%2FgoM0uIQY%2BSXSKd6UTPTlLO%2FFVY7NWWHJ1wIl%2FcDWonI&X-Amz-Signature=de0be1456af618b4c6712db7b250f8b3ea19085988664775e836015c1377aedc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y4L6HW7%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T190837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPQAz3MplqVm4oHCynqtQO69%2F0Ixuce3Ym553kcrgzhgIgAeWpV9zw5qTp6crKF4dzJko%2FzKKCtO0eCtB%2BE7uNWPQq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDLMFy0lML6CO9wyaFyrcA3WosoXNx7kFYo2o7bFof18MgqIZJuhgNcqXc5hp2%2BqDuiWVKXF8IcbI4SjlfTtiXqPrB6YtqaBw6uVvOoTAYPy5QUGCQx817R5Sf81qsKXDetPDufbSN65DH6u%2FwZuUgxT%2FS1NtHHU6%2FnpMYJ%2BOeeZc28vRkg4BR%2FT4lNgdkM%2FDnckdtnuCILu%2F8E4MPWmNdcIcwbEf%2FzakwpPnjedh3DleqWd9Y6Pc%2BKZFvyCb3usUDRX4aCrldYkVW1RADHxMf1rszwF48TDJOEaQ7ey1qQfLHmW2d0Sb%2BSGukjvipA4y04DfYG7m%2Fiyk7%2FkZDO%2BUO420r77JmR6iAMtiV4iuKrZeb0ZEUgXsa1uE2%2FmnjAVG39V9aFPlBGmZSJDDv%2BdvoQKedQTzOcxoP1uZIw4Zb0Pt0jNHdbiKO0Xq%2Fn%2F5Es%2FRgh5wf%2FmPFd2gFxJqN6pu2EQzi9q4DeG6cu3pTkUWxvHNyeAOVI84BBKkQqENRSuM219Y19KBpbJyFgUlPWxpNnAgYUKSE4S8pouYzTcwcM3BLOyHwh9nfwjs0hb3EceairgIYppOsq818wmA4xQfssCm9i5fJQh6inc%2Bcg9PJTI3OV7Q%2FUaSHMUlCA4%2BaKW7SL%2FQdSswDSMFgxcsMO7FntMGOqUBOLhnGBUHD%2BEjbpekvETS0MVyGeJgSJk3Q5TikBO2WBpaPRSkBK%2FaaydpzXpcU3k0sC4zmuZwP0XsFWaWIOZHvvl7O8J84DAxn1WdVVKj0M1r8BHh3P7yTMvc2BNdgQ0r2Lm%2FkP9j0512VwrBmLnmM8nImMShPTpi6fVdvnCnDGNWZ%2B22%2FgoM0uIQY%2BSXSKd6UTPTlLO%2FFVY7NWWHJ1wIl%2FcDWonI&X-Amz-Signature=c251d5ed936b1490ac9fbb2bea89d744e96d759e6c669770e8d693cfc9f0404b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
