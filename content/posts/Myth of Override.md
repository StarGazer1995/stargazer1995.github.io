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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGKDDJLF%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T212355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQCiwPKFdQ5V2YEImKUtazfs5nr9DWBSTLxgId7qu8QNSQIhAKGXV8EZNig%2Bl09jJELPbiXSN1pIzwoSvvsHd%2BuauSeMKv8DCB0QABoMNjM3NDIzMTgzODA1IgyaGlNENvo1gRKLCs0q3APo%2BQJg4EGOB6oMhQ%2FeyCu2uqMPJL5ZAM69JpN9z9X4aqqXZqHfWkoxmkRVhJQnc1p0%2Fn5tP6KdrPX8cfBMUUKhPvcVXPlA5mMyBcVxK7UC7Y5c2s6tYw359kn%2FlW3zFDs5%2BR82ps4c%2Bs0B%2FsrjYmM1aUtpDkuQ0rFItM5FpYEGsH3ViJoy56MIB24gGAR9zXQKk2pJp5GL9sVjZw3nlHZVw5KFhDNSJczXuXGoZJvkultPY3PwzzcW0iJCu8onUIfI%2BGu3We8Wyuqp6lSKKuv1Zd2yj0dO0qwK1MeSX4%2FTjdyneLy2DkQCi3U%2Fz0pJaZjmKi90rhr4%2BCgHtKxAaxPXVnGfLRTwO7M8qQo998fx%2FyaFiSbuuwONo2dHbhiHnKrUBH7ez98kgf7tA42Be8zt9Qd1IXHvMfNqEdl1E%2BZEdtYtUhBmlpt1A0Kp24quxL5wXFp1OYrSILkZtObVq2zWoKM%2BtkrFyqJp4Kiyn94MlBU9PHMwdHocC9ksYKo95L0%2BDSqNYdiIDWyGFHy6JTpH2dHQc7TeY1v1kAkTK9RQ9dYBIKnLUeCYUhMHu9cuP9FRce5UJUHEvMFTopeYAVgVkQpwuwJxqcne1BbyCaFTt94TcVqncVg0owC46jDny7HRBjqkAZibIsf7tRv97F7dOsgejcXYFLN04n6kXYQ%2FkJS5jtN7n3HyF1IKRpCabwCOXm6jExz%2BMH%2FmydWlcITH66%2FzHBeLA076s7DhZ5f2PD0jtmZDg5Mf2Xoz%2B0Uge%2BKg7yeE7XJljISUmi%2FNLItFhEmQfuOb4UeLMpCY9dAr07d%2BEL3eBgQyWt1hQ3%2BgZT1ZWMkbdBq1GQo09ist76FRb6%2FMGoUz%2F%2BAL&X-Amz-Signature=07c55d19c0b95af31cad16b99e82fa0dc85465d5a6d7135f73c5f78c7e5a4933&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGKDDJLF%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T212355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQCiwPKFdQ5V2YEImKUtazfs5nr9DWBSTLxgId7qu8QNSQIhAKGXV8EZNig%2Bl09jJELPbiXSN1pIzwoSvvsHd%2BuauSeMKv8DCB0QABoMNjM3NDIzMTgzODA1IgyaGlNENvo1gRKLCs0q3APo%2BQJg4EGOB6oMhQ%2FeyCu2uqMPJL5ZAM69JpN9z9X4aqqXZqHfWkoxmkRVhJQnc1p0%2Fn5tP6KdrPX8cfBMUUKhPvcVXPlA5mMyBcVxK7UC7Y5c2s6tYw359kn%2FlW3zFDs5%2BR82ps4c%2Bs0B%2FsrjYmM1aUtpDkuQ0rFItM5FpYEGsH3ViJoy56MIB24gGAR9zXQKk2pJp5GL9sVjZw3nlHZVw5KFhDNSJczXuXGoZJvkultPY3PwzzcW0iJCu8onUIfI%2BGu3We8Wyuqp6lSKKuv1Zd2yj0dO0qwK1MeSX4%2FTjdyneLy2DkQCi3U%2Fz0pJaZjmKi90rhr4%2BCgHtKxAaxPXVnGfLRTwO7M8qQo998fx%2FyaFiSbuuwONo2dHbhiHnKrUBH7ez98kgf7tA42Be8zt9Qd1IXHvMfNqEdl1E%2BZEdtYtUhBmlpt1A0Kp24quxL5wXFp1OYrSILkZtObVq2zWoKM%2BtkrFyqJp4Kiyn94MlBU9PHMwdHocC9ksYKo95L0%2BDSqNYdiIDWyGFHy6JTpH2dHQc7TeY1v1kAkTK9RQ9dYBIKnLUeCYUhMHu9cuP9FRce5UJUHEvMFTopeYAVgVkQpwuwJxqcne1BbyCaFTt94TcVqncVg0owC46jDny7HRBjqkAZibIsf7tRv97F7dOsgejcXYFLN04n6kXYQ%2FkJS5jtN7n3HyF1IKRpCabwCOXm6jExz%2BMH%2FmydWlcITH66%2FzHBeLA076s7DhZ5f2PD0jtmZDg5Mf2Xoz%2B0Uge%2BKg7yeE7XJljISUmi%2FNLItFhEmQfuOb4UeLMpCY9dAr07d%2BEL3eBgQyWt1hQ3%2BgZT1ZWMkbdBq1GQo09ist76FRb6%2FMGoUz%2F%2BAL&X-Amz-Signature=3c55d4dd7e77715051f6e08daed76b0ca37cc339746f8e7f6bc731c69b9237c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
