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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTA3CQA%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T190931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIQCtPDe2Tv21bG9RN3v55sOJdDXMDs5n8cKLRLyjiBbzsAIfHBdAIB%2BnOjzhpOvEvqeLHpWoeeoIPKp7pwuLRUQp1Cr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIM%2Bez7NSK92%2FQ6iqyOKtwDhxKAcrYX5pzwCnjaXMzhSU7e9zyEzaueUm%2B47WZKLJ59dJG9RaYZJG3ePJ6kzjSeJ05GaUr7%2Bolzs6OwuhdBK1puUlUbTOo%2FIvRWtENGPARX5V2lnh4q17N5IIuWMwHrSr0wf2ABGmrA3PKpGsYhwHps4LBePArSiKe22MXz5gJn61vN0Z%2BgmdH%2BErQLTf9%2F9L3R%2Bslm7dqt0ZhOSWrk0H6dzqPTgn%2BUMLruVjZhpj0SZkedIuSYBsTGT7EREJQd5qSoAEoOyMVkjgFn8IBybOda7zbMwq0MB8ldxaoJliSJ7aQRtKphO86bNJnEZwt3i7LYZcMcy48Z27Ly40CCEwDBvPPaoItgM5c2FKFxx%2By0f0Pd4T3AOMEdI%2F92qzg9IbrG8qRJ0yAIRg3WzGthha%2FMVx8XjJQvGxU6tLSzRBsGW2SsBa36V%2FiYzBCkBXXdU5FY%2F3SeE1zFlE3N5F0ZYST25Qxbnresqx09n775ABKUABNksaPPIJO09FkY%2FYWHctHccF5X2wZGvGlN5YoNkCA7zSCQovfM1OSkb4ET0oSmVObhVAVBb2yDfzTA9kQscix%2BWCX42ha7n728%2FzVvoUWYYyVmll%2Ben9CISFs8VqLTdKMxcNaBqRqOF3Ewo9HU0gY6pgH1ZnZROdVllt436zXep0YYv0xHTwVwncCk0PdTvxbYNQljrXJ9VJo5cSnsl1OmoACBVJaovpmK%2Fly42UGZJ5qSPA%2BDSSg7keXyO7t3UtSXALIylenkFd8TJR83FLsMTk1XAjdblKOGAl5OUY1CKhHZ3TM2enAhdaSgE68O159ciItCtQb009fFnVJcpM0m3bpFQH1eIiw6ppjw4t%2BeIixO%2FEVlwzR%2B&X-Amz-Signature=05a698c8b8e5e874905154ce0e6640327ea062895dc5c80d6d84bb4b5266fc29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QTA3CQA%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T190931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIQCtPDe2Tv21bG9RN3v55sOJdDXMDs5n8cKLRLyjiBbzsAIfHBdAIB%2BnOjzhpOvEvqeLHpWoeeoIPKp7pwuLRUQp1Cr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIM%2Bez7NSK92%2FQ6iqyOKtwDhxKAcrYX5pzwCnjaXMzhSU7e9zyEzaueUm%2B47WZKLJ59dJG9RaYZJG3ePJ6kzjSeJ05GaUr7%2Bolzs6OwuhdBK1puUlUbTOo%2FIvRWtENGPARX5V2lnh4q17N5IIuWMwHrSr0wf2ABGmrA3PKpGsYhwHps4LBePArSiKe22MXz5gJn61vN0Z%2BgmdH%2BErQLTf9%2F9L3R%2Bslm7dqt0ZhOSWrk0H6dzqPTgn%2BUMLruVjZhpj0SZkedIuSYBsTGT7EREJQd5qSoAEoOyMVkjgFn8IBybOda7zbMwq0MB8ldxaoJliSJ7aQRtKphO86bNJnEZwt3i7LYZcMcy48Z27Ly40CCEwDBvPPaoItgM5c2FKFxx%2By0f0Pd4T3AOMEdI%2F92qzg9IbrG8qRJ0yAIRg3WzGthha%2FMVx8XjJQvGxU6tLSzRBsGW2SsBa36V%2FiYzBCkBXXdU5FY%2F3SeE1zFlE3N5F0ZYST25Qxbnresqx09n775ABKUABNksaPPIJO09FkY%2FYWHctHccF5X2wZGvGlN5YoNkCA7zSCQovfM1OSkb4ET0oSmVObhVAVBb2yDfzTA9kQscix%2BWCX42ha7n728%2FzVvoUWYYyVmll%2Ben9CISFs8VqLTdKMxcNaBqRqOF3Ewo9HU0gY6pgH1ZnZROdVllt436zXep0YYv0xHTwVwncCk0PdTvxbYNQljrXJ9VJo5cSnsl1OmoACBVJaovpmK%2Fly42UGZJ5qSPA%2BDSSg7keXyO7t3UtSXALIylenkFd8TJR83FLsMTk1XAjdblKOGAl5OUY1CKhHZ3TM2enAhdaSgE68O159ciItCtQb009fFnVJcpM0m3bpFQH1eIiw6ppjw4t%2BeIixO%2FEVlwzR%2B&X-Amz-Signature=338dfaf63b6b9b3d4bfa1a6fbb2b993081d3512b87bcfb3ed5737f9cb8d41cab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
