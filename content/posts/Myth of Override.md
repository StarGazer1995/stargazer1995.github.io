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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRP37XPO%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T213013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQDMov9c%2FqXYerAFPySwJt9jPd%2B5hVkBQUIeFRnBwzx9QAIhAJtGbVMLMXacThMPstcDf%2BjXPes%2FE51J%2Fr6Nq4Gq14PHKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyjbTjfo2%2B5drqicBgq3AO3jUWiaiwabBC6V3zhLcch%2BLlrcFD2q5H0trY5otyM9dzEm7n68azWeRd%2B1kLj3ZWQUcxF5vHFAuI%2BNOB6l4e8vvzIiZBwNx4FknBZVaA%2Bk9qOeC7dUmiKpeKyixLw%2FvcZlQsBR73%2Fms9qLXy7z%2FH8bxngGLJnrg%2F5CxS1jdE3habJxTUYpmoim4UFOBq0cKrW0DnV8csa5SF7f7xzflF%2FiKfssVmLEqyxLaI5KliDoEZs1RL90i8t8pUP9mqtX%2FAFILuVhHmXhoZ85dV%2BTt%2BJ0tQcKOIJxyIJIBWd36ha6jM1dGZoukaa1Mp541W1tXg20YbEojv76nHR5%2Fw55gtVcjDG4CTIGxm37SWsE1L4kZFOR4W%2B4GaJ%2BePD4Ok0ekvVclbh3ovLdlBkyhDq%2Fd8MgHlUerWwsOaLoYYIl8v2PKLCBGQk3mj4RjzHgopknFea1R%2BP7LXwsXd1OwnOa6c1D6bc%2F3LNdQYzTOx5Ux9pWsTBKErkNaQzn7PoI8Kg6SavdUSNr88qOQ2FFLA4tx9sJg5Ya9eZzIiH60II47tJTPK3mRtiRHAkl0zBpvdtmi7PNtvXI%2BItcXiVHnU6usf3YdM4Fln3mg13mNoU8NSnWgq5LvskKCF4nIOPQTCJv7jQBjqkAY7H24xfUETQHkEVKxOvUuhxW3LWG6P9Qwz3wh58sw8fkrzUbggp61K5aYDIKpxK3EdhaHVQGPwPmwnnWTKz1xormGa1ErQOnLfLQzDQDKDEWfUzYu2dHcxaBYEo35nNmTEAb9XfMKqYEB9V8ViApdPXmUAkbdwKhJeGduZj8eHSChAaTHeYzUFN%2BK8PCerw3f1AC%2FcMqFUYrM%2BWITJfG%2Br4j7T0&X-Amz-Signature=3493af2d614956e80a2b1338732a16ea555af9665a0b690e0f1744db4e5246ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRP37XPO%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T213013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQDMov9c%2FqXYerAFPySwJt9jPd%2B5hVkBQUIeFRnBwzx9QAIhAJtGbVMLMXacThMPstcDf%2BjXPes%2FE51J%2Fr6Nq4Gq14PHKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyjbTjfo2%2B5drqicBgq3AO3jUWiaiwabBC6V3zhLcch%2BLlrcFD2q5H0trY5otyM9dzEm7n68azWeRd%2B1kLj3ZWQUcxF5vHFAuI%2BNOB6l4e8vvzIiZBwNx4FknBZVaA%2Bk9qOeC7dUmiKpeKyixLw%2FvcZlQsBR73%2Fms9qLXy7z%2FH8bxngGLJnrg%2F5CxS1jdE3habJxTUYpmoim4UFOBq0cKrW0DnV8csa5SF7f7xzflF%2FiKfssVmLEqyxLaI5KliDoEZs1RL90i8t8pUP9mqtX%2FAFILuVhHmXhoZ85dV%2BTt%2BJ0tQcKOIJxyIJIBWd36ha6jM1dGZoukaa1Mp541W1tXg20YbEojv76nHR5%2Fw55gtVcjDG4CTIGxm37SWsE1L4kZFOR4W%2B4GaJ%2BePD4Ok0ekvVclbh3ovLdlBkyhDq%2Fd8MgHlUerWwsOaLoYYIl8v2PKLCBGQk3mj4RjzHgopknFea1R%2BP7LXwsXd1OwnOa6c1D6bc%2F3LNdQYzTOx5Ux9pWsTBKErkNaQzn7PoI8Kg6SavdUSNr88qOQ2FFLA4tx9sJg5Ya9eZzIiH60II47tJTPK3mRtiRHAkl0zBpvdtmi7PNtvXI%2BItcXiVHnU6usf3YdM4Fln3mg13mNoU8NSnWgq5LvskKCF4nIOPQTCJv7jQBjqkAY7H24xfUETQHkEVKxOvUuhxW3LWG6P9Qwz3wh58sw8fkrzUbggp61K5aYDIKpxK3EdhaHVQGPwPmwnnWTKz1xormGa1ErQOnLfLQzDQDKDEWfUzYu2dHcxaBYEo35nNmTEAb9XfMKqYEB9V8ViApdPXmUAkbdwKhJeGduZj8eHSChAaTHeYzUFN%2BK8PCerw3f1AC%2FcMqFUYrM%2BWITJfG%2Br4j7T0&X-Amz-Signature=504998b887588335f535c739eb2856e39b0c39765771c8aa8c7d26d9b32c6302&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
