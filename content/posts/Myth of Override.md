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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7BVKGIT%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T171104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDRglfGLiSqBBucSJKWcvo36895J4Qr3iRIh%2BqmN7I6PAIgWT7bIl3rJJRviK%2BX5V3CTcvTJEpbtOhwPU%2F67Ai1ASIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDA4%2BmZc6GcSrpZJWwircA21B2R8rGLwcNKn4VsJmlEbpaSK435wBLrnghl1A80KPu9KvARUrJsGp9cJultJlbspBejiDyr5Ildpk2WNAX862jiCjl6r%2BkzncUvDuKV00l9PcPSI%2FhalIfkViVX6tZV0uYe07uq6HwAPx5tXatEoPn4bZB5%2BOtfI5OZPNSvPPHZ7HqfEOEup%2FyaOUZfKyTmidJfqODpUFxIBLR0%2FKStJjWNy%2FkA%2BO%2FMcC87F9biPhECqXQUZ%2BzNoSqRYv4HvjZhufHYOnvSzcxHa1qIm7ak3hldJHvpn0twyMf%2B4Znt8WYS0fmYksWLJgB2vyVeejh50wOAVYELqbnnQcywMPd2zTwugu%2FPhlJGr8dpozNw6WjEMN7yeKTritCME2iLvXIbqxqlRZ%2BJ6DUcds0CsG3VQNJuMaQaL4gDJSWKr6GrXH0JVZ%2Fe0zJ7bui6BIMKclEEG8GyWt0CQ4XXtx0ps%2F1wIw7XmtuJnAzFeUq5AeeCrxtdvbwWLA40kD8cxL2Zkw0toffGauazpe1j0BOX2XcuY0hDJGkThRrqroc%2FETnYLi2n%2B%2BMl%2FSA4Jkdgje2tdtoyx95YCNeK%2BKy7qP%2FBIajELo6EjeMN%2FXGnI3xdVpIWMVZOuRTlJ4XFSz2JZ8MN%2Bun9IGOqUBu479WQEU3ey6sFLvyjJDRX%2BUfKYqaEZpEy7BY%2F5TJXDbcplvrVg8qYwjVlYCBEjnAvi%2FNjWKGtMo8Ssa7GEhQTaXmPiW8GB4QlId9i0I5movpWlvgsZ3NtwNEgKy0GdY%2Bl5gZf%2FOyRho0udVpm%2BNcrCqm7z5tlcRl8xZlSm0gVzdSlfeBgYQZ0%2BR7KJU3lwgn%2F%2Fh3FivLaLQYE6HAjNOjdSV9PjM&X-Amz-Signature=84d7145b2e71b96b882b1738f491e767a9d7781b61131bc3a91c6d8adbba0eef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7BVKGIT%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T171104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDRglfGLiSqBBucSJKWcvo36895J4Qr3iRIh%2BqmN7I6PAIgWT7bIl3rJJRviK%2BX5V3CTcvTJEpbtOhwPU%2F67Ai1ASIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDA4%2BmZc6GcSrpZJWwircA21B2R8rGLwcNKn4VsJmlEbpaSK435wBLrnghl1A80KPu9KvARUrJsGp9cJultJlbspBejiDyr5Ildpk2WNAX862jiCjl6r%2BkzncUvDuKV00l9PcPSI%2FhalIfkViVX6tZV0uYe07uq6HwAPx5tXatEoPn4bZB5%2BOtfI5OZPNSvPPHZ7HqfEOEup%2FyaOUZfKyTmidJfqODpUFxIBLR0%2FKStJjWNy%2FkA%2BO%2FMcC87F9biPhECqXQUZ%2BzNoSqRYv4HvjZhufHYOnvSzcxHa1qIm7ak3hldJHvpn0twyMf%2B4Znt8WYS0fmYksWLJgB2vyVeejh50wOAVYELqbnnQcywMPd2zTwugu%2FPhlJGr8dpozNw6WjEMN7yeKTritCME2iLvXIbqxqlRZ%2BJ6DUcds0CsG3VQNJuMaQaL4gDJSWKr6GrXH0JVZ%2Fe0zJ7bui6BIMKclEEG8GyWt0CQ4XXtx0ps%2F1wIw7XmtuJnAzFeUq5AeeCrxtdvbwWLA40kD8cxL2Zkw0toffGauazpe1j0BOX2XcuY0hDJGkThRrqroc%2FETnYLi2n%2B%2BMl%2FSA4Jkdgje2tdtoyx95YCNeK%2BKy7qP%2FBIajELo6EjeMN%2FXGnI3xdVpIWMVZOuRTlJ4XFSz2JZ8MN%2Bun9IGOqUBu479WQEU3ey6sFLvyjJDRX%2BUfKYqaEZpEy7BY%2F5TJXDbcplvrVg8qYwjVlYCBEjnAvi%2FNjWKGtMo8Ssa7GEhQTaXmPiW8GB4QlId9i0I5movpWlvgsZ3NtwNEgKy0GdY%2Bl5gZf%2FOyRho0udVpm%2BNcrCqm7z5tlcRl8xZlSm0gVzdSlfeBgYQZ0%2BR7KJU3lwgn%2F%2Fh3FivLaLQYE6HAjNOjdSV9PjM&X-Amz-Signature=1cd045fdd518ea90c8b2c1e6f8a2b4f926b47ee5d40bed7b955ed3fd2315f2d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
