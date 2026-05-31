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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625G5TGFG%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T073815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQCfV7RMZagb3DWgP2C5t2R7kFNUBY%2B7DmY88XWT3A0UagIgPNgMs%2BccEC6R%2BV0DNxSBA60xhXlyTn35WZLJkWgdT4cqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbEHKg%2B572PEK1K2CrcA4ZqStdlMUKpdyL5rUlbwitv5c%2Biy2F4TbpFWSRLBmiHe8vbkKSIMKvQhyWZta%2B3EO6UYqBgIAYq%2BHBH28skPZ%2FpdH%2Fu72rNSUUMFVqvggHZgIOd7UeLLGA2wnM7%2FYo6ZVlRceIAQqSYWclzRLxfsA3MPByQ0BAQ1IatEqD02l7sx3z2kuBZYGsbsHcgRdP3puBnKLg5YOXimncDj4W0HVgBkjl%2BzLxnumAnamTklbiPTQf77Ln2yGo9ZAqpPdD8QRwEEeu4KH8I%2Bcyg2KH2z0WNjLUvfBE%2FwJk9LCy88qIEqZgE12wKGdI2DXRYIxHpWTM1Wv5uiHhHkruxPWFZZuyxSQcYehHwUea9LnUQNhgp14Rvx5HGtz%2FuabCMOVxovDeISVw7tBTH48frNjvZefSLEt%2FpdO69AIRgvVRCa3xI9cKcwM88q%2F0MOT6cYjR6HnA7PniAyPWUTIkyaI%2B2P8sdnPVX3UzICRcvo1JmOLRJiS%2BWLIUMYxYwORT5LLmLP4fp3mrMDaF%2F%2BCfVqLwONu9BGedI2O8L3MDhOuyLk7RFFCgDBVGHHg9SJTASO9wFHorRQ1DGmfiFcOXOamvV8ZjR63vFwrq0LYcwquuF654tZU22stJv9IRpEN5tMPSq79AGOqUBrgXZZg6p8myvfpbL08PQ0krsFqjQ0ZMoKrd3oNxceU8ngQOI5VyvL6jKeIkpc3bWO9unfVnxUs4ctJf%2FC5bChdgFcBkhbwp7APY3ZnqvBsbaEoSbOl5l2EXv%2B6xXP%2BwHk1AVV9gIMlNGY79kKkd2E4%2BP5qHV5jZGBVKHXRPo7wybUP3ddqZOgtyHWox2VRc6brgLZeNks%2FjNQcjQVc6wIk2TyYhd&X-Amz-Signature=bb8b2bf9c4f1e5036ded6ff87de520c2ca1db451f0ff8ccbfd7824408921479f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625G5TGFG%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T073815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQCfV7RMZagb3DWgP2C5t2R7kFNUBY%2B7DmY88XWT3A0UagIgPNgMs%2BccEC6R%2BV0DNxSBA60xhXlyTn35WZLJkWgdT4cqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbEHKg%2B572PEK1K2CrcA4ZqStdlMUKpdyL5rUlbwitv5c%2Biy2F4TbpFWSRLBmiHe8vbkKSIMKvQhyWZta%2B3EO6UYqBgIAYq%2BHBH28skPZ%2FpdH%2Fu72rNSUUMFVqvggHZgIOd7UeLLGA2wnM7%2FYo6ZVlRceIAQqSYWclzRLxfsA3MPByQ0BAQ1IatEqD02l7sx3z2kuBZYGsbsHcgRdP3puBnKLg5YOXimncDj4W0HVgBkjl%2BzLxnumAnamTklbiPTQf77Ln2yGo9ZAqpPdD8QRwEEeu4KH8I%2Bcyg2KH2z0WNjLUvfBE%2FwJk9LCy88qIEqZgE12wKGdI2DXRYIxHpWTM1Wv5uiHhHkruxPWFZZuyxSQcYehHwUea9LnUQNhgp14Rvx5HGtz%2FuabCMOVxovDeISVw7tBTH48frNjvZefSLEt%2FpdO69AIRgvVRCa3xI9cKcwM88q%2F0MOT6cYjR6HnA7PniAyPWUTIkyaI%2B2P8sdnPVX3UzICRcvo1JmOLRJiS%2BWLIUMYxYwORT5LLmLP4fp3mrMDaF%2F%2BCfVqLwONu9BGedI2O8L3MDhOuyLk7RFFCgDBVGHHg9SJTASO9wFHorRQ1DGmfiFcOXOamvV8ZjR63vFwrq0LYcwquuF654tZU22stJv9IRpEN5tMPSq79AGOqUBrgXZZg6p8myvfpbL08PQ0krsFqjQ0ZMoKrd3oNxceU8ngQOI5VyvL6jKeIkpc3bWO9unfVnxUs4ctJf%2FC5bChdgFcBkhbwp7APY3ZnqvBsbaEoSbOl5l2EXv%2B6xXP%2BwHk1AVV9gIMlNGY79kKkd2E4%2BP5qHV5jZGBVKHXRPo7wybUP3ddqZOgtyHWox2VRc6brgLZeNks%2FjNQcjQVc6wIk2TyYhd&X-Amz-Signature=671093bd455cb1814fb76c58eb49d3af05b73cc67697296c92b51fae3e3e5544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
