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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIWDTZ4%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T005042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAmcLVrykbjxks3ib0jryZTGr0QOSrUT4h59moUsOfjAIhAMXQN4z%2F%2B51IPUh%2Bzxpf%2BJM2tzLPcI1XBymCYMZnkbNfKv8DCFkQABoMNjM3NDIzMTgzODA1IgxZGE0rXVq3k1rXF9wq3AP7YLTHIze9jKixCpeYkOBDgCUdKlcvWNAu0V7%2Bc0n%2B93VVA7jL5AO7dDrOv4oaZOvACHD1tBJHOG8XQj82rrq1KehC%2F%2Ft%2Fn7seu2rVwaa1CikBj085YWU1Q8vGg5fPQ%2BgVZW8hFKm%2BlqCJl2p0zpMHXv8NukndRmxf4J9aF610xDv4whu0URMsByC3gGTc%2F%2FzLKRPpebcKoWQRMKkA%2Bj%2BCaBuxzNdD1HuOo9bq8R%2Bynf%2FzySICvj0LkKjUb2CQZMzzo3gE%2Bc7xkmweEzE%2BWKY2FjkWgx553wVMU9Ga0r92nR%2B0nEc77cOF2rx2AR3CXpfo54NdCEgE%2FWEBcriyR3FYXFa%2FUdmALAudtgVqpHTtki04NaxpK8%2BBFkKz0glJIkAjaNRKY4sujdmzvoETsUPlPf8JibMCrh9mswvaMwOzTJTDgioJA3EZld4uBGMklrGhbjAhE%2Bpz1TDESSIvYQVEPq2TcR1WuFjBLq7m5UskYQh3LGdja9IZmLjwK%2FgJJrpC%2FAIJ64jwM1qqd6JbLiEsnCloJlWPbT%2BlEzNenMOeESCJuKHeJu0yfOrytpLeMRh5FObfNnGoCx%2BPgkocKZG%2FwLHhvNLsfG7HQN07ly7L7%2Buk4npAHRWzL7vLizDeq%2FHVBjqkARhbJnarl5c3uJBY6xXrVgMU9pWbJxJmna%2Fv4gO8WM%2FN4T3sIdSoxb3ovcTh%2B4qWa9LIR0MKp%2F2ZhWgI1JV3acONDpIdbpVFAwwbWO5XOqOSwSkp%2BxhMJBWYZSYV6MvKHr3VweO8Q8UseoGmK%2BY3UUmg2S5mlcoQ3jwapO7kaaN0HgP63FqVQEyVyX%2FfJHHRDMNJaiXHysqJ4x4IL%2FopPCWJDFnD&X-Amz-Signature=2fa1336b3b59dd41eff3af4a0772e6e20d982d0979b78a08213d4b247112a8f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIWDTZ4%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T005042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAmcLVrykbjxks3ib0jryZTGr0QOSrUT4h59moUsOfjAIhAMXQN4z%2F%2B51IPUh%2Bzxpf%2BJM2tzLPcI1XBymCYMZnkbNfKv8DCFkQABoMNjM3NDIzMTgzODA1IgxZGE0rXVq3k1rXF9wq3AP7YLTHIze9jKixCpeYkOBDgCUdKlcvWNAu0V7%2Bc0n%2B93VVA7jL5AO7dDrOv4oaZOvACHD1tBJHOG8XQj82rrq1KehC%2F%2Ft%2Fn7seu2rVwaa1CikBj085YWU1Q8vGg5fPQ%2BgVZW8hFKm%2BlqCJl2p0zpMHXv8NukndRmxf4J9aF610xDv4whu0URMsByC3gGTc%2F%2FzLKRPpebcKoWQRMKkA%2Bj%2BCaBuxzNdD1HuOo9bq8R%2Bynf%2FzySICvj0LkKjUb2CQZMzzo3gE%2Bc7xkmweEzE%2BWKY2FjkWgx553wVMU9Ga0r92nR%2B0nEc77cOF2rx2AR3CXpfo54NdCEgE%2FWEBcriyR3FYXFa%2FUdmALAudtgVqpHTtki04NaxpK8%2BBFkKz0glJIkAjaNRKY4sujdmzvoETsUPlPf8JibMCrh9mswvaMwOzTJTDgioJA3EZld4uBGMklrGhbjAhE%2Bpz1TDESSIvYQVEPq2TcR1WuFjBLq7m5UskYQh3LGdja9IZmLjwK%2FgJJrpC%2FAIJ64jwM1qqd6JbLiEsnCloJlWPbT%2BlEzNenMOeESCJuKHeJu0yfOrytpLeMRh5FObfNnGoCx%2BPgkocKZG%2FwLHhvNLsfG7HQN07ly7L7%2Buk4npAHRWzL7vLizDeq%2FHVBjqkARhbJnarl5c3uJBY6xXrVgMU9pWbJxJmna%2Fv4gO8WM%2FN4T3sIdSoxb3ovcTh%2B4qWa9LIR0MKp%2F2ZhWgI1JV3acONDpIdbpVFAwwbWO5XOqOSwSkp%2BxhMJBWYZSYV6MvKHr3VweO8Q8UseoGmK%2BY3UUmg2S5mlcoQ3jwapO7kaaN0HgP63FqVQEyVyX%2FfJHHRDMNJaiXHysqJ4x4IL%2FopPCWJDFnD&X-Amz-Signature=d680d04ff9aee9edd970273be1f3aef60d1dcc8b159ac32bd1fa6f7e900e102b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
