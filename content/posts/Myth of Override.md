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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3QROGDC%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T234457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEakUNkoL3bcE1LDYFsc1Xf8fReGQFus7ZsIhBBMrX42AiAkvmz820Xu7YvYzdInS7sNT2KmEfuDXpn4xOsOa1%2Bbxyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMuU3%2BtbJVVlM5%2FwSxKtwD8EUZIGOZf1hV0%2B1i0x2qeQzz6mWMUhFe5XnyvmlIk3xQIZMNQdNP0P%2FajHiBjdlz5UZsi3XSKDvgo5pq7R42%2FlXKu%2BF1YLX3ebrM2NPHIYE9nVVn3Sa7iahIv%2FhYFtOHfpy%2F1kme4v%2F9CiygvwWEz5%2BUVau3et0nKFL6KqHro3Lc%2BXcdVRQmZOPPusfg0URplsHkVHUoaE3utD3qyeUStYlOMIjMFZH3Vi8F3pZZ%2BZ%2BM4ZvkF4S%2FXQzRIQOdKFqUFKXPSBlzzT9uoxT3erGY%2FDOxmNZI8OKTB0n4FlrOwQUW6pdt%2BAq2YfrKfZwuQ6PizjOD12wD0bGGM0FYoNQr%2Bmwbjwaz7bfOywj%2Bbg4qbQF7rsS0bYtWDSjA68pTJW19PoYgRtXbEpkpj%2B8nnm7sg8Ht%2FnqnSUWrJLH6QksYkAbrFH2FIc5TZuKLOVpGpw7BSreTv%2BpalKfP665g2F7w7GzVGgW9yZmQ%2Fv7h1afIrr%2Flp5BetHZ6xeBZKhJGQcpIQAhISS8wnWODio2F3cjMh36Kfhkj4gLMZdIxph0kyKQZDBJLNpwMV5QQaq6vAJEP3Uh9xa8JTFOnT2RIYbFi1NVgkGvhAXCFYKDSVH7lhwmad3ilgaJJAVktovAwhqeC1QY6pgHRec%2BMiCh422d3scoJzRLV3sR%2FyCMVlyTBamCzhPS84ZwmzHQ%2F%2FpLYa%2F38TMA1guDYA3y91KISNBueiMtC%2BFTf3qa5SbNBrMcwEHXTl1LvkdmEFatXSyck64nO%2BEDPz1A1fYHEUDPeXDCzyFFAQqwBRmkIdHu0JNpQJ%2FDES71QjLxlXygi8kmnhLxq3j1ZoxbPoqhKy%2FrNrNPUzBcfSiNL303I85uF&X-Amz-Signature=3ac174e24c4e37c91123720f026fc3c0b56fb621a5ae38c125ee8f7d534c2895&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3QROGDC%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T234457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEakUNkoL3bcE1LDYFsc1Xf8fReGQFus7ZsIhBBMrX42AiAkvmz820Xu7YvYzdInS7sNT2KmEfuDXpn4xOsOa1%2Bbxyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMuU3%2BtbJVVlM5%2FwSxKtwD8EUZIGOZf1hV0%2B1i0x2qeQzz6mWMUhFe5XnyvmlIk3xQIZMNQdNP0P%2FajHiBjdlz5UZsi3XSKDvgo5pq7R42%2FlXKu%2BF1YLX3ebrM2NPHIYE9nVVn3Sa7iahIv%2FhYFtOHfpy%2F1kme4v%2F9CiygvwWEz5%2BUVau3et0nKFL6KqHro3Lc%2BXcdVRQmZOPPusfg0URplsHkVHUoaE3utD3qyeUStYlOMIjMFZH3Vi8F3pZZ%2BZ%2BM4ZvkF4S%2FXQzRIQOdKFqUFKXPSBlzzT9uoxT3erGY%2FDOxmNZI8OKTB0n4FlrOwQUW6pdt%2BAq2YfrKfZwuQ6PizjOD12wD0bGGM0FYoNQr%2Bmwbjwaz7bfOywj%2Bbg4qbQF7rsS0bYtWDSjA68pTJW19PoYgRtXbEpkpj%2B8nnm7sg8Ht%2FnqnSUWrJLH6QksYkAbrFH2FIc5TZuKLOVpGpw7BSreTv%2BpalKfP665g2F7w7GzVGgW9yZmQ%2Fv7h1afIrr%2Flp5BetHZ6xeBZKhJGQcpIQAhISS8wnWODio2F3cjMh36Kfhkj4gLMZdIxph0kyKQZDBJLNpwMV5QQaq6vAJEP3Uh9xa8JTFOnT2RIYbFi1NVgkGvhAXCFYKDSVH7lhwmad3ilgaJJAVktovAwhqeC1QY6pgHRec%2BMiCh422d3scoJzRLV3sR%2FyCMVlyTBamCzhPS84ZwmzHQ%2F%2FpLYa%2F38TMA1guDYA3y91KISNBueiMtC%2BFTf3qa5SbNBrMcwEHXTl1LvkdmEFatXSyck64nO%2BEDPz1A1fYHEUDPeXDCzyFFAQqwBRmkIdHu0JNpQJ%2FDES71QjLxlXygi8kmnhLxq3j1ZoxbPoqhKy%2FrNrNPUzBcfSiNL303I85uF&X-Amz-Signature=894eabec5672f46abaec60eb35905239030514e4f172e824f9708a3b47ec9979&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
