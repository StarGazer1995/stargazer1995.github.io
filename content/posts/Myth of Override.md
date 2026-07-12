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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4S6BSAA%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T125058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDuUbNkXr7Sd9A%2FRXsJkXnYWSZnyD2pgL2wuixVEQ1BgwIhAOi0cQ4OZdfCj80shVpwAT28kjLUdceZaUYQ2tTcLD%2B7KogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2SHzk7d5FCj9FZdQq3APt%2BgIOiCBuf7I0acCCbKagy%2Flb7kF2Q0kwhMoHSok6QWF8%2ByTzfdoMoyXJ7ggNylLGIHGw4K4hnOCuSDOvsP5IaJ%2B7r0kD7YlKKumYsuwnw4It6R097HR%2FbXHku5b7mQHhwcdhBY4znD1NXKDLGGJL3iBSlGlHQkbEPIia7hllYpnmtywcxmxaC2aifIFqd5PKE5pWCb66UFodlvRsBjS9TaYgLkK%2Bm2IkpOjukzC3VXxIPXvtO8hQ5l4iX4yZnLlKn4fmM8SjYY5OemuCOm92x80YLC90OXOIcoxiUddJXgIh8fU6Sn5tEMlDf42Sy0LXGPyJukZk%2FffJ0wU9G4pFQSAg7utlk3LvdKu35uSoT9ljozVFkGmVftZWzgt79GBcTC9qEjhYaKXcFmIvP9Nfv2KxEozNLqxW5eBTp%2BPkG700dmNcLzMgsMF5SgSw5P47pI1yk9ik%2FHTbEEzOWI%2BY8zQkw%2Fn9dUIJpz2ODTUhSCdrRuYK4DQ%2FMwpe4grCClUBiVLGUm973Eewk5D2idZZLn178F9dY7T1tWXvGnT68A9vBSb9wdp8L7R6F%2BWzCQDkkpcbVpRLt%2BJWdDt39jUiHKH1L%2BVUXuBi7fnbamJXT3HQIf39f6PL38CS8TDZ%2F83SBjqkAZiDxM8utiwoKTaUVCPvp57ZgrgoNrmdv3fhrAdFwceCXrxjVlVcYwX%2BSqx%2FaQ%2BF5T%2F%2FxPZScB87hvOzBVHBlOn23X8CK1V%2Bro%2F5eGZTwP7Xc4pmP8FDidIg8gv5qH6lCrE0Rxu5BvjOYUdgJThdb9pUpmOG6%2Fo5CzLw2vnOM3D7tloiqEEn4x1KWc%2B7FeBvZ489dka1RYWn4LtMchays5dcatcQ&X-Amz-Signature=3105d787ff0cebec09c79e4e182c86b9e99c569519d8a9dacbbeb65c512e7876&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4S6BSAA%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T125058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDuUbNkXr7Sd9A%2FRXsJkXnYWSZnyD2pgL2wuixVEQ1BgwIhAOi0cQ4OZdfCj80shVpwAT28kjLUdceZaUYQ2tTcLD%2B7KogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2SHzk7d5FCj9FZdQq3APt%2BgIOiCBuf7I0acCCbKagy%2Flb7kF2Q0kwhMoHSok6QWF8%2ByTzfdoMoyXJ7ggNylLGIHGw4K4hnOCuSDOvsP5IaJ%2B7r0kD7YlKKumYsuwnw4It6R097HR%2FbXHku5b7mQHhwcdhBY4znD1NXKDLGGJL3iBSlGlHQkbEPIia7hllYpnmtywcxmxaC2aifIFqd5PKE5pWCb66UFodlvRsBjS9TaYgLkK%2Bm2IkpOjukzC3VXxIPXvtO8hQ5l4iX4yZnLlKn4fmM8SjYY5OemuCOm92x80YLC90OXOIcoxiUddJXgIh8fU6Sn5tEMlDf42Sy0LXGPyJukZk%2FffJ0wU9G4pFQSAg7utlk3LvdKu35uSoT9ljozVFkGmVftZWzgt79GBcTC9qEjhYaKXcFmIvP9Nfv2KxEozNLqxW5eBTp%2BPkG700dmNcLzMgsMF5SgSw5P47pI1yk9ik%2FHTbEEzOWI%2BY8zQkw%2Fn9dUIJpz2ODTUhSCdrRuYK4DQ%2FMwpe4grCClUBiVLGUm973Eewk5D2idZZLn178F9dY7T1tWXvGnT68A9vBSb9wdp8L7R6F%2BWzCQDkkpcbVpRLt%2BJWdDt39jUiHKH1L%2BVUXuBi7fnbamJXT3HQIf39f6PL38CS8TDZ%2F83SBjqkAZiDxM8utiwoKTaUVCPvp57ZgrgoNrmdv3fhrAdFwceCXrxjVlVcYwX%2BSqx%2FaQ%2BF5T%2F%2FxPZScB87hvOzBVHBlOn23X8CK1V%2Bro%2F5eGZTwP7Xc4pmP8FDidIg8gv5qH6lCrE0Rxu5BvjOYUdgJThdb9pUpmOG6%2Fo5CzLw2vnOM3D7tloiqEEn4x1KWc%2B7FeBvZ489dka1RYWn4LtMchays5dcatcQ&X-Amz-Signature=cfe60aec07beff9c5d917cc865a15fd20d8c0b6afbac32819c6ae10875a69613&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
