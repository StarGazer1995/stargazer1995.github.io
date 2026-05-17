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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4CJJ4CN%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T125224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBlInOzTFtVWcvFz%2BXBtYuwfKO4xCMCK7JVBy5%2FbusdvAiEAp7oTHbs98H44oHq85jPOep33d7xb1ECXoEvkswM123cqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRMj8BZdse%2Bry77nircA9MoEgjm%2BXkxtDiRFxYQ4%2Fn1Ud8yjwVgiZNqPD8zTVHI3fPwJgiAEVzAlz4w7P24G4wmZQzAT2zxlOovO6aq%2F9MvyC10EdtuizbFLfdiaxZMk6mGGDnt%2B94aduRugClWBk2NEUwqH8h9f65DV58%2B%2FHOUPm6I%2FuD8TV%2BAuCncmA6Jt5SCZqMZYHas4AU1vXu39QVUhM4LoEacntQYKn5xVsXAwrXqWSH774yRvitCMN58JnzZYFHogmt%2FwX3OoRo37L7iBOvwPCol9p99pJvPYEryNfwSI%2FI32%2FXVs%2BxlgTHjtTXXR92kxUAUIgctijl8TX%2FwVCjk9xdk8yxYjN93W%2Bx%2BXVrd3V6W1phENh1Z%2FDMJpR0ELo%2F39jcb%2Fy%2BG2cG1UDqDWYrgTXxtox7o1YnC1byNe98Zro3mAusYvhv9oXeH3pxF6sXjSqWgHYsjyI6ABUsQH4pOUThCemkas%2BOYrtPOnN2zYKF5%2B3gEBpkieaaAKZQrIH%2BkdUPgVMFTLYqPWhL79UnwBVROUkq7b6XOOjyoHXRM0Yydvah%2FQk3PU9iTx4i1sJ3U7%2FNYPq%2BIh%2Fd4paD372dJBdVyX09kUk6fsPxYmE4XTn8%2BBpsm8GgOnxmDz7CA%2F%2Br3AJ4lnW57MNLepdAGOqUBsaoLbt4%2BfXQLqG%2Bk9UD1Evo8XyQaVj%2FZ2jqGkdbKc4AkbANOhIC45bW2rFsTYFRSJazK0HeI9jeMj8Yzq8%2F2aYUuBu6wn6vijGIEQo6tXSOJ28%2Fa%2FCF52j6O6VSOcuSFfMKjGPVk40RzSWwJD%2Fvgb4sFYR%2ButyPi4ahde4zY%2BHLcqN7eWHWhLIsY5U2rxa7%2F76TNN8efDHf%2Battynvc8rcuLPcQD&X-Amz-Signature=19706efcd5f88567c749ff4ee9ca3081580a53180701be042bd35465cee5183d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4CJJ4CN%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T125224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBlInOzTFtVWcvFz%2BXBtYuwfKO4xCMCK7JVBy5%2FbusdvAiEAp7oTHbs98H44oHq85jPOep33d7xb1ECXoEvkswM123cqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRMj8BZdse%2Bry77nircA9MoEgjm%2BXkxtDiRFxYQ4%2Fn1Ud8yjwVgiZNqPD8zTVHI3fPwJgiAEVzAlz4w7P24G4wmZQzAT2zxlOovO6aq%2F9MvyC10EdtuizbFLfdiaxZMk6mGGDnt%2B94aduRugClWBk2NEUwqH8h9f65DV58%2B%2FHOUPm6I%2FuD8TV%2BAuCncmA6Jt5SCZqMZYHas4AU1vXu39QVUhM4LoEacntQYKn5xVsXAwrXqWSH774yRvitCMN58JnzZYFHogmt%2FwX3OoRo37L7iBOvwPCol9p99pJvPYEryNfwSI%2FI32%2FXVs%2BxlgTHjtTXXR92kxUAUIgctijl8TX%2FwVCjk9xdk8yxYjN93W%2Bx%2BXVrd3V6W1phENh1Z%2FDMJpR0ELo%2F39jcb%2Fy%2BG2cG1UDqDWYrgTXxtox7o1YnC1byNe98Zro3mAusYvhv9oXeH3pxF6sXjSqWgHYsjyI6ABUsQH4pOUThCemkas%2BOYrtPOnN2zYKF5%2B3gEBpkieaaAKZQrIH%2BkdUPgVMFTLYqPWhL79UnwBVROUkq7b6XOOjyoHXRM0Yydvah%2FQk3PU9iTx4i1sJ3U7%2FNYPq%2BIh%2Fd4paD372dJBdVyX09kUk6fsPxYmE4XTn8%2BBpsm8GgOnxmDz7CA%2F%2Br3AJ4lnW57MNLepdAGOqUBsaoLbt4%2BfXQLqG%2Bk9UD1Evo8XyQaVj%2FZ2jqGkdbKc4AkbANOhIC45bW2rFsTYFRSJazK0HeI9jeMj8Yzq8%2F2aYUuBu6wn6vijGIEQo6tXSOJ28%2Fa%2FCF52j6O6VSOcuSFfMKjGPVk40RzSWwJD%2Fvgb4sFYR%2ButyPi4ahde4zY%2BHLcqN7eWHWhLIsY5U2rxa7%2F76TNN8efDHf%2Battynvc8rcuLPcQD&X-Amz-Signature=4717e5fe97be54765a8cc8a862c420af15732482f7f239a772197d69f7c0f6ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
