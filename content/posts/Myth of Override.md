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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663URWR43E%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T170904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDsz6eF7KZ0B8gpjvk%2BgNEVYX5mmEP4AQEvKcjqF%2B%2BiNAIhAPw1NZ%2FCPheVW9JFbbY19KhJAu%2B2Ab%2BDis43dGiEdYjrKv8DCCkQABoMNjM3NDIzMTgzODA1Igy60qTU%2Bv5PfYoFJiAq3APJLImWv8KPXAJv8tpteWDuib0XnXdmPPgplxGnF4wikj7yV52MXdpKTfDnf6gwU7TrJZHZjljOo%2BQa0v3S2VfceeG426YMWbbk4w0nii1GyizvDlVkfDMbM7CNumHRMG%2BtbsvZucaIvQpoEfJWnIkxzw1bzSqMDWYie4ujVCx3ceu2OZsDkcvKpHh7ZBDE5pQCCuez%2FMN7H0LLJPuz41zuoD%2FLdN0srrBV1wL9g5r980ktBeYAVqYRRaOXUYnMVqOykkPWeegytT%2B%2F27jpqPfRlzSj%2FSjHrjkp42qT8azLUTD1ThHKLAqXcPhUk75m%2BTaFg8eAiamLmxxhRCqJk5juRs9%2FqrQiDKF8OeUNNpd%2FjQv7L2et3VxeHZEP%2FQlJ2HBK1on6lIHjcoAIaB4SH1zVFks2H%2Fh0Ti1Ivmc2Oe6BGP6vXFK3kYaNIPGpVLwFtKLuZ9m2HoIX%2FV2IvacXZ4b%2BoevYdBksnMtHUhUuHvhXe7%2BjZ3bWs6M%2FtguNJ7rThYTsWQ2jM2HCA%2Bid%2FmbfCEKXCo4Fn8v99%2B1PcR4eCuxW0K75IRs9bqo3zvoon1DBUO63UcT7wGXWToM%2Foi%2B%2FDaYeThdAYwiL3Ty0YPxcLUKLJMvc3hRF0rETOcHEvzDi8Z7WBjqkAexns9%2F6GjXUJIJq1vIYAph7JmYGTG27arMIdCBwqNVxTtld3gh12WqPbE4IcESv798ZwcbGTHO%2FDmnfKAaWvZ8vtM35olDyl4xQDIaUIg9FU8ycoKLurVg%2FVvFCEwvWThBtJTXSDjZak8xBW5nR%2B9phKUYqPwSXS98U5n%2BoKJoLcqKmze2gXdyiuzZzDp2MXFuFU2A4BRmwsPXHyEL%2BMYJ8TrDQ&X-Amz-Signature=ab6eaa3ca22b7b499f4cbafc662cbd528e8e2b2ca3ced9aad8c8a7a1a66372ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663URWR43E%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T170904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDsz6eF7KZ0B8gpjvk%2BgNEVYX5mmEP4AQEvKcjqF%2B%2BiNAIhAPw1NZ%2FCPheVW9JFbbY19KhJAu%2B2Ab%2BDis43dGiEdYjrKv8DCCkQABoMNjM3NDIzMTgzODA1Igy60qTU%2Bv5PfYoFJiAq3APJLImWv8KPXAJv8tpteWDuib0XnXdmPPgplxGnF4wikj7yV52MXdpKTfDnf6gwU7TrJZHZjljOo%2BQa0v3S2VfceeG426YMWbbk4w0nii1GyizvDlVkfDMbM7CNumHRMG%2BtbsvZucaIvQpoEfJWnIkxzw1bzSqMDWYie4ujVCx3ceu2OZsDkcvKpHh7ZBDE5pQCCuez%2FMN7H0LLJPuz41zuoD%2FLdN0srrBV1wL9g5r980ktBeYAVqYRRaOXUYnMVqOykkPWeegytT%2B%2F27jpqPfRlzSj%2FSjHrjkp42qT8azLUTD1ThHKLAqXcPhUk75m%2BTaFg8eAiamLmxxhRCqJk5juRs9%2FqrQiDKF8OeUNNpd%2FjQv7L2et3VxeHZEP%2FQlJ2HBK1on6lIHjcoAIaB4SH1zVFks2H%2Fh0Ti1Ivmc2Oe6BGP6vXFK3kYaNIPGpVLwFtKLuZ9m2HoIX%2FV2IvacXZ4b%2BoevYdBksnMtHUhUuHvhXe7%2BjZ3bWs6M%2FtguNJ7rThYTsWQ2jM2HCA%2Bid%2FmbfCEKXCo4Fn8v99%2B1PcR4eCuxW0K75IRs9bqo3zvoon1DBUO63UcT7wGXWToM%2Foi%2B%2FDaYeThdAYwiL3Ty0YPxcLUKLJMvc3hRF0rETOcHEvzDi8Z7WBjqkAexns9%2F6GjXUJIJq1vIYAph7JmYGTG27arMIdCBwqNVxTtld3gh12WqPbE4IcESv798ZwcbGTHO%2FDmnfKAaWvZ8vtM35olDyl4xQDIaUIg9FU8ycoKLurVg%2FVvFCEwvWThBtJTXSDjZak8xBW5nR%2B9phKUYqPwSXS98U5n%2BoKJoLcqKmze2gXdyiuzZzDp2MXFuFU2A4BRmwsPXHyEL%2BMYJ8TrDQ&X-Amz-Signature=003bc8d23c88aad355218af18d9ca0879378d98e2fc1bb7e2ae281050cbb462d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
