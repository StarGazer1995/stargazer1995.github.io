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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBCQYKJ4%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T034304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs3JK4ABzL1%2FTUBSGbBoYfdYUBvPYkHnl0OM%2FY71FMUgIgVx466KxliobeZ8uNTgfJ5pip5lawygJOeC7jDhXAZMEqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrMGnBUABA89DYk7yrcAyn19uszvsu3muSrp7uz5AfrLIKeOv2E0KW%2BV3xK%2FP3%2FvZPTI%2BUGavtRquDYZbbkpWQACsXM8Xf2Hh3%2FB5bQ8vvMGuqkJvBPj2mcLkJ1JgwgyZ1aS6Tvn%2Fw%2FLc7fAoJfZgh3smvwm0accmL%2FuqS%2Bnhr9KTk22wdJyJ8aYVheH8y9gXWzXcDrreWjTd5BRbu0%2FZo1IwBGihmkJQPmfqg6bPno4PQ9mJemsCP7J%2Fk4cyLzIDYgjebzGfP7URbo370GbE%2FITumgM9Zo4JssxBg0103mYA8OYPqv%2BrSLMalkcC0axHBjA%2BXLcob5gd%2BY5Ax6vs7wNfFJZRxMiDVvHsW1ho8wVyf6AkNiztZZhwHXb3XyakEo%2BWeFUOidK%2BP095QCwBhZPx8cecb5gJrGhHzFzlV6u3xLWUDWnRzTYxAaJ55WgkSaYghXWttndnHKVrWpOjEm3bHxnkZlEiPnJicOPyqH6NCCl%2B9V%2Bzg1mmKUbbele%2FFEOW9e8%2BnQff5k5MMjGxKEuDInOvB262KVaC9kPqJKEfGxjZq6KFs3SrYlz2%2B%2FjhE5iYPR3xNQJJRKQ4BNZW4o0XupEwfb%2FgaAFxKLvEd%2Fx79xk7GtnAs9x5F1Rxouax3fYBvwMpvrDxRqMMPj5NMGOqUBPTp5sbUe1QqpN5EpOSTACcHyj5N0Dfl7nJ13jb%2FTSQ7fxiwl93TYDCE4gUUxVLAGuUd%2FyswnhZWazrk2YcYrQjs1PBQnWyN6DxrOiOcZBrp4pROWoxhcegMUg6KIOW25iu66nEU8vwQT7BDvgl%2Bbv2Fvz%2BhbdIUvM8WHsOawhaLUHQAh%2BvJRWsHz86cYdQfcn20wMXS2jlTIfX%2F1R7LKLXdkRS3V&X-Amz-Signature=81d34097c32e07046bc489b787fc7bce09c3c81a1cb266a70e29bcba6093d975&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBCQYKJ4%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T034304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs3JK4ABzL1%2FTUBSGbBoYfdYUBvPYkHnl0OM%2FY71FMUgIgVx466KxliobeZ8uNTgfJ5pip5lawygJOeC7jDhXAZMEqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrMGnBUABA89DYk7yrcAyn19uszvsu3muSrp7uz5AfrLIKeOv2E0KW%2BV3xK%2FP3%2FvZPTI%2BUGavtRquDYZbbkpWQACsXM8Xf2Hh3%2FB5bQ8vvMGuqkJvBPj2mcLkJ1JgwgyZ1aS6Tvn%2Fw%2FLc7fAoJfZgh3smvwm0accmL%2FuqS%2Bnhr9KTk22wdJyJ8aYVheH8y9gXWzXcDrreWjTd5BRbu0%2FZo1IwBGihmkJQPmfqg6bPno4PQ9mJemsCP7J%2Fk4cyLzIDYgjebzGfP7URbo370GbE%2FITumgM9Zo4JssxBg0103mYA8OYPqv%2BrSLMalkcC0axHBjA%2BXLcob5gd%2BY5Ax6vs7wNfFJZRxMiDVvHsW1ho8wVyf6AkNiztZZhwHXb3XyakEo%2BWeFUOidK%2BP095QCwBhZPx8cecb5gJrGhHzFzlV6u3xLWUDWnRzTYxAaJ55WgkSaYghXWttndnHKVrWpOjEm3bHxnkZlEiPnJicOPyqH6NCCl%2B9V%2Bzg1mmKUbbele%2FFEOW9e8%2BnQff5k5MMjGxKEuDInOvB262KVaC9kPqJKEfGxjZq6KFs3SrYlz2%2B%2FjhE5iYPR3xNQJJRKQ4BNZW4o0XupEwfb%2FgaAFxKLvEd%2Fx79xk7GtnAs9x5F1Rxouax3fYBvwMpvrDxRqMMPj5NMGOqUBPTp5sbUe1QqpN5EpOSTACcHyj5N0Dfl7nJ13jb%2FTSQ7fxiwl93TYDCE4gUUxVLAGuUd%2FyswnhZWazrk2YcYrQjs1PBQnWyN6DxrOiOcZBrp4pROWoxhcegMUg6KIOW25iu66nEU8vwQT7BDvgl%2Bbv2Fvz%2BhbdIUvM8WHsOawhaLUHQAh%2BvJRWsHz86cYdQfcn20wMXS2jlTIfX%2F1R7LKLXdkRS3V&X-Amz-Signature=65381665898c09916c947a1e913b954022a413065f9b5094997f0e74b66f8cbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
