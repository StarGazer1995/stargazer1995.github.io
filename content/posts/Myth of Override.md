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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL4J34IP%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T140716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDttxlKjPaatT6W8InR3CemwhAohyFvPFveGw5VPLnVGAIgAP3Jc%2BztIqq6n62qeUuHqPttYvf5mje4XMHfG%2B0T7Soq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDAUrhob7DMlGrjT7tCrcA7SSh6xob%2F%2B6HFhEIb2iQJHkTnj1MeyMqibGsRdmCaHF%2BwEJ6Rcciq2vrPoeevwTO9WTfHzO%2BcBbOtb8vJosFQWLpcLlTSkA5R40qKFI7Ce%2BKbD9WrY2FjjEEume4JgbH2RC9WJWsZHc03QwZAcoshQlNSu0jm%2FCSyxeYpwwwKbcqXtxpFhMe15c5S9yfLm0ItHgkYVGTNavdUWiBGsMF%2Bh7MrrXL6x9mCQQfwKtwHg8bqwrXvU2sdzM8Joqtf%2FLhaEJmiK1hp2wUMTKCAVzbQqDHPyjdaQNz7ZOdNTCGLCwZ%2F9ZEwiKHmIkAc9t37bzxRYZA1kHVK4%2BgV70RZH4%2FOqUTJ7u6aKf0fGqmuvg7iIJZJn9PjxBCYpamLXxfri%2FXHUJWADbhyXyicFjudKAk9tKu82JG0VDvCcKoEsMmpyuKxTVKWEZLW0%2B2pbPhRway2nl9y%2BW5TqJkEuUF18VKgbk7IBRlG%2Fv%2Bo%2BrxCOp3r4N33gaFa2ysbhIuwLgdQP9GqVZiLN7kpjJmblj4qE1Jd0V3SB2LKRQQ00o7i%2FqYc1X%2BkovDqUzYuSmykMAc%2BNOh6qT4h29a%2FUIjHldmIZL9eNGj66WZx86CgONxc5PA5ObkCW%2Bwnm6KzQwbi4IMN2v8NQGOqUBGI255t5%2BDjqizpJr0Xl9Scq8l%2BLDTOmUqCEfNd6kbHnJmbJ5UMBCNO8pFuhoz1%2BXq9PWqlZaTPlRdFXhsqjf9w3rXqeyyU5Xwzjz%2FlDeSfdEl4OH0AJqPna%2BaxxINSAeYYqHamab%2Fbp5104kq%2FH8bTzxykkhCmxg7PFYKJWpuFnIwIL75Xinl5sBgMjXNucmbUC6SeLYKbt7RbDtmCKsgkO8uH95&X-Amz-Signature=8490db3f39b56124777dcbd2606f4ededd606a9110c5447e8a8cb651dd14f450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL4J34IP%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T140716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDttxlKjPaatT6W8InR3CemwhAohyFvPFveGw5VPLnVGAIgAP3Jc%2BztIqq6n62qeUuHqPttYvf5mje4XMHfG%2B0T7Soq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDAUrhob7DMlGrjT7tCrcA7SSh6xob%2F%2B6HFhEIb2iQJHkTnj1MeyMqibGsRdmCaHF%2BwEJ6Rcciq2vrPoeevwTO9WTfHzO%2BcBbOtb8vJosFQWLpcLlTSkA5R40qKFI7Ce%2BKbD9WrY2FjjEEume4JgbH2RC9WJWsZHc03QwZAcoshQlNSu0jm%2FCSyxeYpwwwKbcqXtxpFhMe15c5S9yfLm0ItHgkYVGTNavdUWiBGsMF%2Bh7MrrXL6x9mCQQfwKtwHg8bqwrXvU2sdzM8Joqtf%2FLhaEJmiK1hp2wUMTKCAVzbQqDHPyjdaQNz7ZOdNTCGLCwZ%2F9ZEwiKHmIkAc9t37bzxRYZA1kHVK4%2BgV70RZH4%2FOqUTJ7u6aKf0fGqmuvg7iIJZJn9PjxBCYpamLXxfri%2FXHUJWADbhyXyicFjudKAk9tKu82JG0VDvCcKoEsMmpyuKxTVKWEZLW0%2B2pbPhRway2nl9y%2BW5TqJkEuUF18VKgbk7IBRlG%2Fv%2Bo%2BrxCOp3r4N33gaFa2ysbhIuwLgdQP9GqVZiLN7kpjJmblj4qE1Jd0V3SB2LKRQQ00o7i%2FqYc1X%2BkovDqUzYuSmykMAc%2BNOh6qT4h29a%2FUIjHldmIZL9eNGj66WZx86CgONxc5PA5ObkCW%2Bwnm6KzQwbi4IMN2v8NQGOqUBGI255t5%2BDjqizpJr0Xl9Scq8l%2BLDTOmUqCEfNd6kbHnJmbJ5UMBCNO8pFuhoz1%2BXq9PWqlZaTPlRdFXhsqjf9w3rXqeyyU5Xwzjz%2FlDeSfdEl4OH0AJqPna%2BaxxINSAeYYqHamab%2Fbp5104kq%2FH8bTzxykkhCmxg7PFYKJWpuFnIwIL75Xinl5sBgMjXNucmbUC6SeLYKbt7RbDtmCKsgkO8uH95&X-Amz-Signature=8a6cb847ebc3da4d0f274fc73341e4d77144db61e686dc9feafaf34794eb0cfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
