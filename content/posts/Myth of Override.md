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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIF4OUU6%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T132518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbL%2B%2Fhyf707uZNW6s%2Bp%2Bj6dBekP3vNaIXSNj%2BeSH4zJAIhALfpV913r5OLkcvCVHh6smoebIRHHV7NaGrhW%2BrNxBB4Kv8DCHYQABoMNjM3NDIzMTgzODA1IgzbQfzGKHvhV%2Frj3IQq3AOLnpVCsSZB738axsR9lQ4ryyoeg7DXCuU6HJklE3DRFEwcwPUV7bX1sbJhU6%2FQ4nIcgE3i97dt3kSnsswG5wOeSJRI%2BCcluRyxhKhcUQCzjoaOC8G5VxlQ%2F%2FDfWbPXdKN4yecVsZvX%2BYVU9AbTcIlL7gk9TyEvX%2FfsA2ZvoG7UzvEwwTAUP9gaN%2B00JwODifNZwCA0fKzWFIIWFu4rDhq%2BqOo5oo9SP2gQEOPcSXVh8tIEKOlfizS4JGgiGd6Og1jU3oO0FyAAnnaCILv79FIthVXHUfE%2Boz0U3XQN64vfmndIc1B%2FRCgzf0X5PfGjBpLdDPR%2BqG7cVhjnq2RC9AU3Jonrg8nPzgX5eJpShColkCU4vqVZHTJ6bCaT5%2BLyDdoJdKOmtdPCGlRZ5kdqALn0fPKNWK1tFnPlPzo1CANqn4TA3jnAlzOW7%2B7AuqnIeEVx2bgSyVAwR9dDP%2B887xZ1FYwKVXzQrZHNzVlW%2BxO5XNQGFlFSkk4TBm3PPfGc9r%2FADBVxGh1gJRU5ceTcPnAc70z2rC8DCSdX7A8IzRaCkotVgAIJLPdEGx1A6HAkOIe64ZGLQL4GiMzgSuXV4Oy%2FMesPsZPydmTIUyQHlNsFKMDlaV1iwKv8392%2BHzDFqpzQBjqkAbT%2B22JW0HLAQQ824smmvS8w2Vzatkc4gnJ24Tb8Qi%2FrqDRFTonhcayEZl%2FN5IQbdG6DMO9ClUtiBvdM3MQPOukbpy3u7HVIRqLJ4b%2Be5dbJaCM16muebKhlJExE1AuH7gSQCWg8ZiSx59%2B9kE4wHlF4SF8rSGXYes8DgSCN%2BDuwP3w%2FCz3UHCco3z7%2Fe4QMNjklxbuo2%2B%2FxLKhvMPeMUBgFCGg5&X-Amz-Signature=43b109824428de049905c8c92646b6d7d2d4fa8c96c79a62c2857ef5246c1970&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIF4OUU6%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T132518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbL%2B%2Fhyf707uZNW6s%2Bp%2Bj6dBekP3vNaIXSNj%2BeSH4zJAIhALfpV913r5OLkcvCVHh6smoebIRHHV7NaGrhW%2BrNxBB4Kv8DCHYQABoMNjM3NDIzMTgzODA1IgzbQfzGKHvhV%2Frj3IQq3AOLnpVCsSZB738axsR9lQ4ryyoeg7DXCuU6HJklE3DRFEwcwPUV7bX1sbJhU6%2FQ4nIcgE3i97dt3kSnsswG5wOeSJRI%2BCcluRyxhKhcUQCzjoaOC8G5VxlQ%2F%2FDfWbPXdKN4yecVsZvX%2BYVU9AbTcIlL7gk9TyEvX%2FfsA2ZvoG7UzvEwwTAUP9gaN%2B00JwODifNZwCA0fKzWFIIWFu4rDhq%2BqOo5oo9SP2gQEOPcSXVh8tIEKOlfizS4JGgiGd6Og1jU3oO0FyAAnnaCILv79FIthVXHUfE%2Boz0U3XQN64vfmndIc1B%2FRCgzf0X5PfGjBpLdDPR%2BqG7cVhjnq2RC9AU3Jonrg8nPzgX5eJpShColkCU4vqVZHTJ6bCaT5%2BLyDdoJdKOmtdPCGlRZ5kdqALn0fPKNWK1tFnPlPzo1CANqn4TA3jnAlzOW7%2B7AuqnIeEVx2bgSyVAwR9dDP%2B887xZ1FYwKVXzQrZHNzVlW%2BxO5XNQGFlFSkk4TBm3PPfGc9r%2FADBVxGh1gJRU5ceTcPnAc70z2rC8DCSdX7A8IzRaCkotVgAIJLPdEGx1A6HAkOIe64ZGLQL4GiMzgSuXV4Oy%2FMesPsZPydmTIUyQHlNsFKMDlaV1iwKv8392%2BHzDFqpzQBjqkAbT%2B22JW0HLAQQ824smmvS8w2Vzatkc4gnJ24Tb8Qi%2FrqDRFTonhcayEZl%2FN5IQbdG6DMO9ClUtiBvdM3MQPOukbpy3u7HVIRqLJ4b%2Be5dbJaCM16muebKhlJExE1AuH7gSQCWg8ZiSx59%2B9kE4wHlF4SF8rSGXYes8DgSCN%2BDuwP3w%2FCz3UHCco3z7%2Fe4QMNjklxbuo2%2B%2FxLKhvMPeMUBgFCGg5&X-Amz-Signature=e2108bcbca7a54ae1fff9caab8952084624bb8fa60dc86559799252f07a381d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
