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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBJ6Q25E%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T145510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIH1NAhwZYX654Xi53K2qbN01C51SK%2FpXPZthyNQxMqzpAiAzegPaWJ8EXKun8hQVxpvlC2xQ64DSbMQJAG75zEO6YSr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMi7wIR7VpRtQ%2FEML%2BKtwD6zJQP%2BCCabzcXEbLC2fxXGTdu8uc2ZgW2E%2FAeZkkxAhVtP8iXThUXIEr0J7d4oIc%2FNcWdqh8M7ZAGhj8RYe%2FGZRz7ugYHSk%2FSoIJ%2FiQNje1bYwsLEuxsswK5InWbNJy1mYLqQeiU%2B85%2F4vvNb91xJK9Q6f5TKyBnebiM8smuEIYWh6VsBHuNX1KHKEqjxh9zqmAdYWq46sPW2ng%2F1yT3eT1W2jA%2Fabtr2Cx7r5N1T%2Bgq9g1lI53ytGGMkCFwXTWpPkWz26v7p6Y4jsn3TUKbvTVvbajvnXvreEUSGJNqINTt2ePZKMJGlMbF1E7pM4oQcsrFb6vrrvlNOPLPdcSMfgEP2H%2FhWnVVC03ITcLno59sR5QMlb5dnCyQziSpSF5cmoVJMLhQLlJE0ro1Ak5Inn9rA2Mw%2BPO%2F6kWUfLh6gKPrtx9WiPOjIWCb3VKT%2Fc3lBnH2D3rFMaXv60Unvnqw1W%2BxF%2BDFnriwurCZ6XXRtvXmXbROzjE%2B78iI1FYmlH1mIV1fihWoQETN4nDnH1L5K4lvJnM4wtbvrdM321Wtoo%2F9V%2BxpsOf5taLl%2Fvnxl%2Fq3JtupxZ5v%2FgsZ4E21FRMIGJ96SVjpyKVp4Hh5tr3osntq0%2BiKfiN5Xj%2BB4QIwv4ST0wY6pgEucyOyXt7Uw5Z97B63mxHcNv5kmFutGXD%2FjGQhxy6fieSCc6LD86efaGcwxYg94PIcJBWYTB4dRZnG8lLbTz%2FG8yPfprfxggLPtDnhFvdjJmGaqq2Jz%2BaJCAnZrsXRWpB%2Bfl5E1t1VS1hIKbuhMUTA8opurZxB1HQDVF9X2KM0fuh3sCmCvW50xe7pcCAH6Q17zkSuJnXR6pQXhOf%2FNYV0nFvBF2Za&X-Amz-Signature=ad071055df49547b757fc3096a2b7d3f22e7f13f8dbbe9c8a7e58a6a0299869a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBJ6Q25E%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T145510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIH1NAhwZYX654Xi53K2qbN01C51SK%2FpXPZthyNQxMqzpAiAzegPaWJ8EXKun8hQVxpvlC2xQ64DSbMQJAG75zEO6YSr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMi7wIR7VpRtQ%2FEML%2BKtwD6zJQP%2BCCabzcXEbLC2fxXGTdu8uc2ZgW2E%2FAeZkkxAhVtP8iXThUXIEr0J7d4oIc%2FNcWdqh8M7ZAGhj8RYe%2FGZRz7ugYHSk%2FSoIJ%2FiQNje1bYwsLEuxsswK5InWbNJy1mYLqQeiU%2B85%2F4vvNb91xJK9Q6f5TKyBnebiM8smuEIYWh6VsBHuNX1KHKEqjxh9zqmAdYWq46sPW2ng%2F1yT3eT1W2jA%2Fabtr2Cx7r5N1T%2Bgq9g1lI53ytGGMkCFwXTWpPkWz26v7p6Y4jsn3TUKbvTVvbajvnXvreEUSGJNqINTt2ePZKMJGlMbF1E7pM4oQcsrFb6vrrvlNOPLPdcSMfgEP2H%2FhWnVVC03ITcLno59sR5QMlb5dnCyQziSpSF5cmoVJMLhQLlJE0ro1Ak5Inn9rA2Mw%2BPO%2F6kWUfLh6gKPrtx9WiPOjIWCb3VKT%2Fc3lBnH2D3rFMaXv60Unvnqw1W%2BxF%2BDFnriwurCZ6XXRtvXmXbROzjE%2B78iI1FYmlH1mIV1fihWoQETN4nDnH1L5K4lvJnM4wtbvrdM321Wtoo%2F9V%2BxpsOf5taLl%2Fvnxl%2Fq3JtupxZ5v%2FgsZ4E21FRMIGJ96SVjpyKVp4Hh5tr3osntq0%2BiKfiN5Xj%2BB4QIwv4ST0wY6pgEucyOyXt7Uw5Z97B63mxHcNv5kmFutGXD%2FjGQhxy6fieSCc6LD86efaGcwxYg94PIcJBWYTB4dRZnG8lLbTz%2FG8yPfprfxggLPtDnhFvdjJmGaqq2Jz%2BaJCAnZrsXRWpB%2Bfl5E1t1VS1hIKbuhMUTA8opurZxB1HQDVF9X2KM0fuh3sCmCvW50xe7pcCAH6Q17zkSuJnXR6pQXhOf%2FNYV0nFvBF2Za&X-Amz-Signature=4df764d6bf292512e8c73f1025425795952dbf5f022f768877ee9ee3aefd45be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
