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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOPHWS6S%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T211921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTXxY5ruQ5HQ66DJue3iDvUC9Fap5A07UlGamCVwm1HAIgceGBqfuxtuIlO7mz%2BaZJIhheaw6k8v%2FzX%2Bq1%2BI3UjW8qiAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwoJ%2Fabzw90csRMWircA18FZaguxpuoCo4oE6PDyWmabKalh2RGAbIw47l%2BkY2FltI2c9meHu%2FQluU4ylkPOFOIKst2ep%2FrmRW5TIM20N2CGJ9Lbp%2Fa9wFM7L6fIcB0Kz%2FJ1Sb24Fe2jNBFh5CeXutSa8FZi7I5IVLLNDLxBzqC9vWGOl5BZ%2FXpUZKButzT49U7l8FIFZvLGvSdFrNWRWa%2FFab1MX2%2FC%2F%2FftFCLFrTwxctWsa0%2FYNNk%2FsA4LiJ1Y1fHkXAeLkYDtbKqcovlomwrJu0cfzdICKuY%2BXS9%2ByuRRfX1blrjFuMGYd0DUz65%2FLAvMJAfVb03POgork1Ru2q3FRzYSRbYpdiM0lkJASmQx1LUo5mWuCdi8ZdPTL1rGdwK%2BKSEHt3qjpmQSOPJo11tFQORFxzdBKwy5PdfnlTqSBd7%2BVLWIpEucNqip%2FkkZo6teyDGK8Qu6DamMhWzUzwBHbnQcTKKew3a9szzdVPM6myYxCWPNRQzEiHYE%2BzQa1pr1A3M%2Bne7IbZglQQv6NzuaxJwa15dv00JxvqXPdO1%2FFDdRlrIDOSvsYsU%2F8mLoQhMtNi7Fld1chjv70Uh2oaidocxTpYFkNIWWpfB6qa0%2BTnt0a%2BW4V0E9ipZRc3LuxsBR2%2Fx%2FZjuNZ3zMOKYxdUGOqUB%2B24oX7EjIzh76VttSTTgTkQTWX%2FiJJK0kRAkmgSflc0EGx9sUoPIGM1lZbaxXMch5ylGRTD661I69fCpBizW5Rip1xm9sW0r%2BHLTOoJBDy96b%2BzKg8fjhvrh4My9W3gYrj7KFu3ogeApuj4QiMZmOJ4TwMIS3tCwuAHc7C5x5WlINiLHuwAN%2FcToiu6HSh1hOFTxwNkzduFVew9V6PNHIUIqjcO7&X-Amz-Signature=2548a5be406c2fbc7a75812efd00bc1073e8de236a1b994e392947e66fe0e183&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOPHWS6S%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T211921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTXxY5ruQ5HQ66DJue3iDvUC9Fap5A07UlGamCVwm1HAIgceGBqfuxtuIlO7mz%2BaZJIhheaw6k8v%2FzX%2Bq1%2BI3UjW8qiAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwoJ%2Fabzw90csRMWircA18FZaguxpuoCo4oE6PDyWmabKalh2RGAbIw47l%2BkY2FltI2c9meHu%2FQluU4ylkPOFOIKst2ep%2FrmRW5TIM20N2CGJ9Lbp%2Fa9wFM7L6fIcB0Kz%2FJ1Sb24Fe2jNBFh5CeXutSa8FZi7I5IVLLNDLxBzqC9vWGOl5BZ%2FXpUZKButzT49U7l8FIFZvLGvSdFrNWRWa%2FFab1MX2%2FC%2F%2FftFCLFrTwxctWsa0%2FYNNk%2FsA4LiJ1Y1fHkXAeLkYDtbKqcovlomwrJu0cfzdICKuY%2BXS9%2ByuRRfX1blrjFuMGYd0DUz65%2FLAvMJAfVb03POgork1Ru2q3FRzYSRbYpdiM0lkJASmQx1LUo5mWuCdi8ZdPTL1rGdwK%2BKSEHt3qjpmQSOPJo11tFQORFxzdBKwy5PdfnlTqSBd7%2BVLWIpEucNqip%2FkkZo6teyDGK8Qu6DamMhWzUzwBHbnQcTKKew3a9szzdVPM6myYxCWPNRQzEiHYE%2BzQa1pr1A3M%2Bne7IbZglQQv6NzuaxJwa15dv00JxvqXPdO1%2FFDdRlrIDOSvsYsU%2F8mLoQhMtNi7Fld1chjv70Uh2oaidocxTpYFkNIWWpfB6qa0%2BTnt0a%2BW4V0E9ipZRc3LuxsBR2%2Fx%2FZjuNZ3zMOKYxdUGOqUB%2B24oX7EjIzh76VttSTTgTkQTWX%2FiJJK0kRAkmgSflc0EGx9sUoPIGM1lZbaxXMch5ylGRTD661I69fCpBizW5Rip1xm9sW0r%2BHLTOoJBDy96b%2BzKg8fjhvrh4My9W3gYrj7KFu3ogeApuj4QiMZmOJ4TwMIS3tCwuAHc7C5x5WlINiLHuwAN%2FcToiu6HSh1hOFTxwNkzduFVew9V6PNHIUIqjcO7&X-Amz-Signature=1b262b19c73795e074d7e2f0dd18d222d1331d8e0e768f3098284f02595b99ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
