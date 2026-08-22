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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBCQCQSF%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T141041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCysXq486Mx3BFwsMqiDLLaCgbJ7oPxH%2FA1b6C7h8rIRwIhAMnkHQ77Lk%2F2m8p7TukFaVYwLc9KgQH6igi%2BAykbldwiKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWYESmVZgJTXp5YvMq3AMv6J%2FcWdSJEbzdD9TNATn510URGFePEf33J6iPcBCfsatTGapXflVQOXfDeTntPBgv2qd0G52r5cpR%2BHUXVNA3fkficZm4fdQnFDnJD6mCCoky78k0yY%2FEIMZ4S8mRPxjClN2cd8XSZTwlVRYWdKi2bZElVG3gAgT%2BlTtIjGGTxK7Y0t0bA8E4wNtiSo7oe59SdkqVPgW2zf46E3yrSFK5Yft%2FcDlEDDqhDKmK6TcCmVmnap7sc6K2JuZgabJujAvN6tVPDP4ru3ehMlf8lyBTiE8QpEv%2BIY8Z%2BJSezK8oGIx8vlHSf%2B2V10eSPb5eqDH8lUYW1UZ%2FLUOe3p8Ga1QfSCkFic%2FUeaNgRKV81M0S2yElnj%2FuQHM6naX4JuVUOJynkk9btNpEcElWjikp2fESdFociwqFEKUaSCgP7d3MQV5ovZP2rHV91ncx4UqyEaZnyF7rAqU6VM6tGxq%2FjMhmfxFBrLofk7RWwJnhP1UqdWz1ZYWiAggZ%2FYo56d2yB%2F%2F3tetW92mRVyGBL8uZu1KFIXHZ37SYVqw29smZJFbyqGpOIC9Nwd%2F1IIoif%2Fw0ECCo%2F525%2F4Hwd5xnLzYM8nFEdVeZXoiiyEWtq9LXMZqYosNCwFEIHJgGaXdmLjDkw6bUBjqkAdVy8ZSOBjLzLoOL8v2C%2BSq3W55QzvXJCUscGUM7T3iauVpVXCgQlqzzZfHnGeFuXMq4fZSM8Y7AUmLdtRzXPZxeejGDCyz98GJwKneajTtRlP1Yv9PGudPLqKVVPqTOV2B3ijvW3JvamZ4KIq1yK%2BZJVIK3ZCNoWClxJxgGWyS1HSKMNCf1M511FpzA8SDexhMkApsv3%2Fg0Yjeb3NSA4eHr%2B4T2&X-Amz-Signature=512dc2abdb1bc82ea46315f53f47d6cba2131afc9cfe07180e91be10740c0b5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBCQCQSF%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T141041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCysXq486Mx3BFwsMqiDLLaCgbJ7oPxH%2FA1b6C7h8rIRwIhAMnkHQ77Lk%2F2m8p7TukFaVYwLc9KgQH6igi%2BAykbldwiKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWYESmVZgJTXp5YvMq3AMv6J%2FcWdSJEbzdD9TNATn510URGFePEf33J6iPcBCfsatTGapXflVQOXfDeTntPBgv2qd0G52r5cpR%2BHUXVNA3fkficZm4fdQnFDnJD6mCCoky78k0yY%2FEIMZ4S8mRPxjClN2cd8XSZTwlVRYWdKi2bZElVG3gAgT%2BlTtIjGGTxK7Y0t0bA8E4wNtiSo7oe59SdkqVPgW2zf46E3yrSFK5Yft%2FcDlEDDqhDKmK6TcCmVmnap7sc6K2JuZgabJujAvN6tVPDP4ru3ehMlf8lyBTiE8QpEv%2BIY8Z%2BJSezK8oGIx8vlHSf%2B2V10eSPb5eqDH8lUYW1UZ%2FLUOe3p8Ga1QfSCkFic%2FUeaNgRKV81M0S2yElnj%2FuQHM6naX4JuVUOJynkk9btNpEcElWjikp2fESdFociwqFEKUaSCgP7d3MQV5ovZP2rHV91ncx4UqyEaZnyF7rAqU6VM6tGxq%2FjMhmfxFBrLofk7RWwJnhP1UqdWz1ZYWiAggZ%2FYo56d2yB%2F%2F3tetW92mRVyGBL8uZu1KFIXHZ37SYVqw29smZJFbyqGpOIC9Nwd%2F1IIoif%2Fw0ECCo%2F525%2F4Hwd5xnLzYM8nFEdVeZXoiiyEWtq9LXMZqYosNCwFEIHJgGaXdmLjDkw6bUBjqkAdVy8ZSOBjLzLoOL8v2C%2BSq3W55QzvXJCUscGUM7T3iauVpVXCgQlqzzZfHnGeFuXMq4fZSM8Y7AUmLdtRzXPZxeejGDCyz98GJwKneajTtRlP1Yv9PGudPLqKVVPqTOV2B3ijvW3JvamZ4KIq1yK%2BZJVIK3ZCNoWClxJxgGWyS1HSKMNCf1M511FpzA8SDexhMkApsv3%2Fg0Yjeb3NSA4eHr%2B4T2&X-Amz-Signature=669648d9fd8c4cda9079d403127e88a526a800aae407dac033d357ab4e0cb81b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
