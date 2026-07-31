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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ORPHZ52%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T115213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEME9QwBDONFlOEI5URmzMIaw4r3Bj7KOJq4PpZssK6PAiEAzSQq%2F0%2FVDnq6j8lald2%2BedYDEMPaQyKG7PWAbUUoYAgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpDgiQLhIz2zYaBEyrcAyhrlNkIYKegfMo73GWLGgjMxmkfR9hV%2FwRtgKVPYYthE3zjLwdJJG4mJorWDTTmO05bkh7FWUPyDI1zi3qhJI%2B5O7CyNM4W2pyo1cE8F1CQ%2FmAPg%2FXFU5obGRTGarZ27LqVr2HHPl2iKTg0mY%2FX4gP4Z%2FmoTu%2FIuUr238GNwTDaQ%2F7WPdKncEELrZPGNU6Tatyawf9DDPzWIniPFy9E%2BkS2zDrjtLQpTZXtZK8tPFsLlQxNHfWdIaeOjev4jFoot8Z0RL818mTelKNf6TuLXiia7M7zu6uR2uuX%2Fnw6v%2BWCJiivjrfbL5LK2gyE1x1Pd7fs0qrklvbC9JGn0o%2B47iQQ60de0vpqg1CPq%2FsL6nNhfdXWxo%2F%2BbNHoS1U1RVl4ziZ9hb8DlxFoxEpzvjy89NGqvXHYR7S1TX0KMoEO9TCJfU0crkcK87Tgf%2F0PsHqY2dt2Wos3MmhCf7EYINOp%2B66v1FKLHQbz1FboUk7w8ksPK9%2FkTuh3ampG0L2wzcNZ4YW%2BhwfqSBCXlybAF863f6Hp43%2FSF%2FxkttIrD7wQS8Eq5Eb9CQNOs9GxFyty6OhN4hoRl0cs6zINKFAqlfn1VeBVEoALcTS1Cfz9rRSgG5NlncH5j7hamxlvIQ8WMMGFstMGOqUBMkE6CPt1WdzP2ZiTArZt2cLAhYpbYsAhhhNYsjRXvq255jHdImiATiMK8pHk8ig7t5L3v4AIkL6o8TJ9PgK8TnlIgNiNY%2FFsgBqKEe%2F4HeXbse8%2BwY17c4kan4Ea%2Fm2Hci6TzSDlR0IULE0tmlJ15hcXoF%2BwmpxO5%2BGsOtFy4j0tht5fGIcp6YzBd3cR2oDlBmmBHLVMbFTzKTSoq8U1V6ooKnIe&X-Amz-Signature=11fc8b35adf7e81a225f129cfa2b3c5a98d5a39462ed8ad375e6a10c1448d4a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ORPHZ52%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T115213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEME9QwBDONFlOEI5URmzMIaw4r3Bj7KOJq4PpZssK6PAiEAzSQq%2F0%2FVDnq6j8lald2%2BedYDEMPaQyKG7PWAbUUoYAgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpDgiQLhIz2zYaBEyrcAyhrlNkIYKegfMo73GWLGgjMxmkfR9hV%2FwRtgKVPYYthE3zjLwdJJG4mJorWDTTmO05bkh7FWUPyDI1zi3qhJI%2B5O7CyNM4W2pyo1cE8F1CQ%2FmAPg%2FXFU5obGRTGarZ27LqVr2HHPl2iKTg0mY%2FX4gP4Z%2FmoTu%2FIuUr238GNwTDaQ%2F7WPdKncEELrZPGNU6Tatyawf9DDPzWIniPFy9E%2BkS2zDrjtLQpTZXtZK8tPFsLlQxNHfWdIaeOjev4jFoot8Z0RL818mTelKNf6TuLXiia7M7zu6uR2uuX%2Fnw6v%2BWCJiivjrfbL5LK2gyE1x1Pd7fs0qrklvbC9JGn0o%2B47iQQ60de0vpqg1CPq%2FsL6nNhfdXWxo%2F%2BbNHoS1U1RVl4ziZ9hb8DlxFoxEpzvjy89NGqvXHYR7S1TX0KMoEO9TCJfU0crkcK87Tgf%2F0PsHqY2dt2Wos3MmhCf7EYINOp%2B66v1FKLHQbz1FboUk7w8ksPK9%2FkTuh3ampG0L2wzcNZ4YW%2BhwfqSBCXlybAF863f6Hp43%2FSF%2FxkttIrD7wQS8Eq5Eb9CQNOs9GxFyty6OhN4hoRl0cs6zINKFAqlfn1VeBVEoALcTS1Cfz9rRSgG5NlncH5j7hamxlvIQ8WMMGFstMGOqUBMkE6CPt1WdzP2ZiTArZt2cLAhYpbYsAhhhNYsjRXvq255jHdImiATiMK8pHk8ig7t5L3v4AIkL6o8TJ9PgK8TnlIgNiNY%2FFsgBqKEe%2F4HeXbse8%2BwY17c4kan4Ea%2Fm2Hci6TzSDlR0IULE0tmlJ15hcXoF%2BwmpxO5%2BGsOtFy4j0tht5fGIcp6YzBd3cR2oDlBmmBHLVMbFTzKTSoq8U1V6ooKnIe&X-Amz-Signature=9e5150e0c86f32b77cf1746ccb598a3a7d4cbe36758db76a3bb3a153e99be021&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
