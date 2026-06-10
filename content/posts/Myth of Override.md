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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNPHG4BL%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T182410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHV5QuEylRwqH55EvBZ3rJgGcBlvYtJ1yy2Rat4WVHhUAiAB4m5hiCHlca7EdVJyW%2BBfRFcaFIVsK9SPnI2q6XuIoiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb%2FOpTRbiBPe2GJgmKtwD7tBtvVdiX1mloxiGgrbDucqEzc4tp%2BWjEjSxGyXybJP4ttSslQxMXX4zPZXZQlHYmBZcBnf4cjwUjdTOJkhWogaub0KwfJOopDcgLP2d47PDufyg0XVGkAsfPIsGGwhfzh5%2BeZJsf%2F%2FIaX2xXdcMzIOsAm2aTsjAH91fmFq8pk5kvUE0Rj977qhsMf3Tl18KUGsC0QuEi%2FZsqBAdYs7%2FEuvPRnfbHTWvEoP9Jia74xCaIMhL060lsz%2Bf1bXUa%2FC%2F95OvaFNSdcZhS6UWibg6aA7UDIYNwxaQEeBZbb4z%2BEbB1KE6Yr34vHiZMo38USMbClYHhYu%2BmDu2CtBphit5oqwUaHJbS7L6%2BR6O8N6vNkUOM8fq1lifaLCqHAqcSn9sAg7oNXA8091beACGcdQ%2FKPppMzlvrIB9U%2BALWzV0QECUvCeXRqwFdpYlYpJ0XbYGTQuQidnZuKQP5eoxd3N4mmH5SzXrhS%2Be%2FUKfXOsfF503yTvUz8ZlFVlScNd%2FIj06NMnZKE%2FkxlV970NUUuoyXtcRG4ZCPewETm%2FV1GVejGDNd1JXqJ9AABcGA8%2BkDC2yEv%2FBBteVZ44hJDDUq9noCU4styLGBUezqqyK%2B4%2FrbQ4J8R9pmr%2BsQlqItGkwvr%2Bm0QY6pgFt3X3chHtO8IyqqIzzjOfX7YmiaNmlsK%2FIWoYV6hKoDbqakdQ%2FYeqX0LD%2BtRnhTJm9CmvGvJo%2FlGQi6uJsh2F%2BYlNzlmAXq2V6gwZY7BtDPbi0KTwk%2FJbuLB6UG%2F1y33btUVhsmjyhGUVAQaCXp8A5%2B5UDLXLIW9wy9AJJhTQqr1izcDhrRbJjsbJU1IJwbZqSarZMnMM%2F2KlyvQXCXfq9%2FG2jUKy2&X-Amz-Signature=078ca4a4d4d3d7617335a7330d9d4ad3e980509f601dce051e8d016b654cd4d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNPHG4BL%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T182410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHV5QuEylRwqH55EvBZ3rJgGcBlvYtJ1yy2Rat4WVHhUAiAB4m5hiCHlca7EdVJyW%2BBfRFcaFIVsK9SPnI2q6XuIoiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb%2FOpTRbiBPe2GJgmKtwD7tBtvVdiX1mloxiGgrbDucqEzc4tp%2BWjEjSxGyXybJP4ttSslQxMXX4zPZXZQlHYmBZcBnf4cjwUjdTOJkhWogaub0KwfJOopDcgLP2d47PDufyg0XVGkAsfPIsGGwhfzh5%2BeZJsf%2F%2FIaX2xXdcMzIOsAm2aTsjAH91fmFq8pk5kvUE0Rj977qhsMf3Tl18KUGsC0QuEi%2FZsqBAdYs7%2FEuvPRnfbHTWvEoP9Jia74xCaIMhL060lsz%2Bf1bXUa%2FC%2F95OvaFNSdcZhS6UWibg6aA7UDIYNwxaQEeBZbb4z%2BEbB1KE6Yr34vHiZMo38USMbClYHhYu%2BmDu2CtBphit5oqwUaHJbS7L6%2BR6O8N6vNkUOM8fq1lifaLCqHAqcSn9sAg7oNXA8091beACGcdQ%2FKPppMzlvrIB9U%2BALWzV0QECUvCeXRqwFdpYlYpJ0XbYGTQuQidnZuKQP5eoxd3N4mmH5SzXrhS%2Be%2FUKfXOsfF503yTvUz8ZlFVlScNd%2FIj06NMnZKE%2FkxlV970NUUuoyXtcRG4ZCPewETm%2FV1GVejGDNd1JXqJ9AABcGA8%2BkDC2yEv%2FBBteVZ44hJDDUq9noCU4styLGBUezqqyK%2B4%2FrbQ4J8R9pmr%2BsQlqItGkwvr%2Bm0QY6pgFt3X3chHtO8IyqqIzzjOfX7YmiaNmlsK%2FIWoYV6hKoDbqakdQ%2FYeqX0LD%2BtRnhTJm9CmvGvJo%2FlGQi6uJsh2F%2BYlNzlmAXq2V6gwZY7BtDPbi0KTwk%2FJbuLB6UG%2F1y33btUVhsmjyhGUVAQaCXp8A5%2B5UDLXLIW9wy9AJJhTQqr1izcDhrRbJjsbJU1IJwbZqSarZMnMM%2F2KlyvQXCXfq9%2FG2jUKy2&X-Amz-Signature=341332461ba70124d513aaf257375c85ead2be48d02a95eb2c34ff2af190e968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
