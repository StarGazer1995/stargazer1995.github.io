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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKE37IN5%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T102030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH08DJl77Qe8E%2FPC7sygnUQodCk%2B92A3XjPZKU%2F3G2%2BAAiAvg4lyd2gdRpSYTTXf1vZDjE0RTYdT9z9G213xt7Jchyr%2FAwhqEAAaDDYzNzQyMzE4MzgwNSIM6%2BGO7thhhnzxTtWzKtwDPCr957NWyFAQgAKi4pvdcnrnTzHzyh9UjTVK8foOOIPQ6ZiZEVb%2BJG1btHavAUhrwr997673GDR3oodfZxzsRBhNmgHTW%2BM%2BVXqAz06r1DpKy057DEesB2h2dYfxw62GuvUzH%2BACwLlpVZeJK0RJQx7C0E3%2BZriKSfWCeW2jIznofQpa84sYSIi98gx9ayjkfJr1b1FfMCeeGlB%2BOzIQs7NXFahhASyCGfXLyqm1X9d5DYUOQGjeOcGlnwdTGv%2FKv%2BbxLeFcp4z2BsYeoIcNatg6eaOx2uOdIoH12z2g3Ym1TJtgfpx0NdTGpIbE6jzllJ%2FJsEjBvVA7yCaS9Q6mH7aqNnibByGcL%2BLIxkelOqxTgRkf9Gyt7Lse7fkPlNh06NeLYu7X2d0m4GhFp%2BM%2FQ7x9JMiVqNO6Ddc8s7jp0T32ZNRhpedjkUTxMmUqYoWMQJXEh4iSKxbVSrN5DTEuFDxbG%2BjAjH1CC9oKwc%2B9W9siLjYFyWqQybXwGjUrvcShr%2Fl6O%2BCUE4B1EWDGp8QpjbH3Yafubjklt7BNNZBtiHBONjAW9txOGjYw5Co9NeXFvYWmt59jI7ctAimFTzhPmlToH8pN4E%2Fsx0gXoFy%2BjM7WmHehwiOHyf3m6d0wstTb0wY6pgEnioTPDf4cDhudTVx7YRWKE17h0%2F0NwiEOz1bUWIANCQH40RkAb2c%2BDJkKDy3GinNCziskJvNAxmO05y06b6C3%2FOz4N5k7E1oFjG8Ss%2Fi31cW9KqJINYoKRgrHwe3h3Yy%2BXikj%2FFsxV1fh1mKKuxVoKGadcz4q%2FS8hdRGQk7Rb8h7I42fBYP0r8wSoo7WYfERV4uY1HOaRLW62UZe50BDym6%2FjmUge&X-Amz-Signature=e40dbec6e32aa9a22c4b243dfdb62f9fd8f6d72b28cb8b15c1be6e9972b85ee1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKE37IN5%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T102030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH08DJl77Qe8E%2FPC7sygnUQodCk%2B92A3XjPZKU%2F3G2%2BAAiAvg4lyd2gdRpSYTTXf1vZDjE0RTYdT9z9G213xt7Jchyr%2FAwhqEAAaDDYzNzQyMzE4MzgwNSIM6%2BGO7thhhnzxTtWzKtwDPCr957NWyFAQgAKi4pvdcnrnTzHzyh9UjTVK8foOOIPQ6ZiZEVb%2BJG1btHavAUhrwr997673GDR3oodfZxzsRBhNmgHTW%2BM%2BVXqAz06r1DpKy057DEesB2h2dYfxw62GuvUzH%2BACwLlpVZeJK0RJQx7C0E3%2BZriKSfWCeW2jIznofQpa84sYSIi98gx9ayjkfJr1b1FfMCeeGlB%2BOzIQs7NXFahhASyCGfXLyqm1X9d5DYUOQGjeOcGlnwdTGv%2FKv%2BbxLeFcp4z2BsYeoIcNatg6eaOx2uOdIoH12z2g3Ym1TJtgfpx0NdTGpIbE6jzllJ%2FJsEjBvVA7yCaS9Q6mH7aqNnibByGcL%2BLIxkelOqxTgRkf9Gyt7Lse7fkPlNh06NeLYu7X2d0m4GhFp%2BM%2FQ7x9JMiVqNO6Ddc8s7jp0T32ZNRhpedjkUTxMmUqYoWMQJXEh4iSKxbVSrN5DTEuFDxbG%2BjAjH1CC9oKwc%2B9W9siLjYFyWqQybXwGjUrvcShr%2Fl6O%2BCUE4B1EWDGp8QpjbH3Yafubjklt7BNNZBtiHBONjAW9txOGjYw5Co9NeXFvYWmt59jI7ctAimFTzhPmlToH8pN4E%2Fsx0gXoFy%2BjM7WmHehwiOHyf3m6d0wstTb0wY6pgEnioTPDf4cDhudTVx7YRWKE17h0%2F0NwiEOz1bUWIANCQH40RkAb2c%2BDJkKDy3GinNCziskJvNAxmO05y06b6C3%2FOz4N5k7E1oFjG8Ss%2Fi31cW9KqJINYoKRgrHwe3h3Yy%2BXikj%2FFsxV1fh1mKKuxVoKGadcz4q%2FS8hdRGQk7Rb8h7I42fBYP0r8wSoo7WYfERV4uY1HOaRLW62UZe50BDym6%2FjmUge&X-Amz-Signature=4eb76d2b64ae7ccf18eef13de41536a7224efbb9d689db7a24d22ee965117f37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
