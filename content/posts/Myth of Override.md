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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STLJXWBX%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T015147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCXh9ESb3598ESZWVG%2BsCK%2Bol3diOXKTQ5fomJ7HsV4MAIhAKfmKqGu9ybyLJ8lrBpXEvP6u1BBG9%2Fba2bQXS0qm6HEKv8DCD8QABoMNjM3NDIzMTgzODA1IgxMRplcewi44weceRIq3AMPc5mx5TyI85DySAqkeswqlzDzoOYLy6k1piDd8nXuJlpFnTPtvWSFv9L7VITwel9epBWl6cOUjqHiF2QoSQq1FG%2FsGYgI6sggd7E0gJSQodLLNZd0s7FzPpDT%2FW5uV2NpsfyMZb3VSsDll1XjqdpFD%2B6tMqJFGLNNCnOvlCZ3i33HqSrscUTvFHQLjSpTjx%2FZ8XchhCzP6pdrDqNpZSzOeFy9j4m9AkBn%2Fzaq%2BVMC6Otxv8YTKBmMqao8I1M68KFYimNTm3XJSOzKldTnUGWCeVgrnPG4A3OgYoZoho3HukpeZkSEmnmkEAln5OulYDt%2BMEhIK%2BJLi0VVZHIFaHZ6MGZOUcVj8zk0Hs97dTtGZ9hSfQDL9t1tOzfof18JepzXNQfFkPyr8lx2km4cXTv9fTTkrOcz3E4WB7b3a%2Bpd8eD5yXd0%2BTP34c9XuYDV2BFKtY0rsQZRdQ97IaDSyAG9wAId5U1XoX2Yz%2F%2FwJhEHDVD3lAMDUJkgMGv%2FhrAUIvLkN6wp%2F5%2FfP3oZwu9z%2FP1Fgk%2B%2FGAbAzDPRPKluxOnQCsxvJOcgtl1wa3gOI0brcLZ0kbQyGd8kKTBvazov15lqWcGE8DSHF8H04Ch2zACJQ%2B6WWyRa3zXc371qwDDC2MLUBjqkAWNoxHYVLix5edsOxRC1sTvXoHpgnHWRwC0lnFCE2n%2FCoK3Jxs92%2Fej%2Fjc1NSQNJLparnyDWk2zhctcxXw7tkoq%2Fnjg7Ngm2xjVVO87rUQkbo1v3YwCCRXdC4unRAMEHfXVC4oolQZy%2BkeVaIO9I%2BOAOxZ30hqKokJIr6eJZkM5l%2BOdFirkLRxcshOAGpio4%2B71uLtNeGrR4H7dDJoDvQUDVQfqd&X-Amz-Signature=14010579eae2ca97b6956d4be6add3378c09aab5cbeb2c0f4cc2eabd87ac6a00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STLJXWBX%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T015147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCXh9ESb3598ESZWVG%2BsCK%2Bol3diOXKTQ5fomJ7HsV4MAIhAKfmKqGu9ybyLJ8lrBpXEvP6u1BBG9%2Fba2bQXS0qm6HEKv8DCD8QABoMNjM3NDIzMTgzODA1IgxMRplcewi44weceRIq3AMPc5mx5TyI85DySAqkeswqlzDzoOYLy6k1piDd8nXuJlpFnTPtvWSFv9L7VITwel9epBWl6cOUjqHiF2QoSQq1FG%2FsGYgI6sggd7E0gJSQodLLNZd0s7FzPpDT%2FW5uV2NpsfyMZb3VSsDll1XjqdpFD%2B6tMqJFGLNNCnOvlCZ3i33HqSrscUTvFHQLjSpTjx%2FZ8XchhCzP6pdrDqNpZSzOeFy9j4m9AkBn%2Fzaq%2BVMC6Otxv8YTKBmMqao8I1M68KFYimNTm3XJSOzKldTnUGWCeVgrnPG4A3OgYoZoho3HukpeZkSEmnmkEAln5OulYDt%2BMEhIK%2BJLi0VVZHIFaHZ6MGZOUcVj8zk0Hs97dTtGZ9hSfQDL9t1tOzfof18JepzXNQfFkPyr8lx2km4cXTv9fTTkrOcz3E4WB7b3a%2Bpd8eD5yXd0%2BTP34c9XuYDV2BFKtY0rsQZRdQ97IaDSyAG9wAId5U1XoX2Yz%2F%2FwJhEHDVD3lAMDUJkgMGv%2FhrAUIvLkN6wp%2F5%2FfP3oZwu9z%2FP1Fgk%2B%2FGAbAzDPRPKluxOnQCsxvJOcgtl1wa3gOI0brcLZ0kbQyGd8kKTBvazov15lqWcGE8DSHF8H04Ch2zACJQ%2B6WWyRa3zXc371qwDDC2MLUBjqkAWNoxHYVLix5edsOxRC1sTvXoHpgnHWRwC0lnFCE2n%2FCoK3Jxs92%2Fej%2Fjc1NSQNJLparnyDWk2zhctcxXw7tkoq%2Fnjg7Ngm2xjVVO87rUQkbo1v3YwCCRXdC4unRAMEHfXVC4oolQZy%2BkeVaIO9I%2BOAOxZ30hqKokJIr6eJZkM5l%2BOdFirkLRxcshOAGpio4%2B71uLtNeGrR4H7dDJoDvQUDVQfqd&X-Amz-Signature=32e08007f8670b84ee7b3030a94bee2f891bf5a987fd7c64027aa6b3b49e0a95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
