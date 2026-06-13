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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6SEUQ4Z%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIAQBLuKhL%2BKptyOLxNGFjNKkaG0GazKkxlflToVSmcg7AiAkXtYorDDDqp%2BmE5reGUTzNt9Hhw%2FQj1V1ePKCvB2rPSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMqYzucS6MoGBG97GRKtwDWQvdBC2MwDLoP1gibfs35QtKPfUErd%2BYLE9l4pZ3vUqPxpAXiQ77pYpzRFEVEfHwIH%2Fs2vVfkSPC4F2xJOyb1tXz8TRKUI03imN5qjh0turI5yLdJKfUhsuwQdKph%2FgfG0KjdUoi3gjMLXNv6IXRH%2FwB%2BKViDjkU61gSPoyqVTTCWQd7l0nyBdiHOTp%2Bf1QEf3kCrCL6EUFFpyFhCqn5UsYJsefvw7oW8%2FPjyaDF6PeW%2F8mm53MyiCF6XJWaCBLv3WVT604IiB9y13o6nfIWrLuTGtyW94z1viCM0xpjGF%2FiT2kBNw00AJQzgLAcYt%2BOQ%2BcII1ghbFCTROsWkagd7a%2FfHVjqft8IquaGjsi8kdWE5uEF2as5ldzY2dRulZUnwYNXr6A2HrcinKlyGlQv0kDF0xj6VlfUMwhDG%2BmR4%2F49HIbNBSuPJ%2BsRZqsYm1Ly2oCTL6%2FsdJqVyFFHz1cqlyVHv3UK5QJJPhRiPgQU1YW2YFYoxkXW9wpvIl%2BeKiT8QuriBe1KPjrhnrJMrz3vWmr9KwkND7l%2Bi4e2%2BvmxSBaybjeVTDcVP4ZXYsAiG9rNwKhgr8%2Bc7j2GcIwsUxOXXRhXoBbenAGLKmAYA4EfJw0miMJRAW8axg74gE0ws6a30QY6pgGQwlrD%2Bwzi9CsnTCtvG0OJ%2Fz4Q53lNW6wQoefBZgjsvKfHC9Gm%2FFSj7PhXEA%2F3808jHDthdm54UQVP7KuM4QDrueAxUw7tarWcS%2BkNS0PPoNMpiEl%2BnkR9FrmdGVSNHJeeWeXybfYr4fDMDh%2FgfE19yj3OsOTMZWSVJNrKb2Fg7RXNy474Q6enYXnFf2qLGR8xa5LfE8IcxNGuGcg2KFDyLrFhOuuL&X-Amz-Signature=8522bb7d13635c5b8c2232d013230626cc4b85f0a4578026f8061e317f8ea188&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6SEUQ4Z%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIAQBLuKhL%2BKptyOLxNGFjNKkaG0GazKkxlflToVSmcg7AiAkXtYorDDDqp%2BmE5reGUTzNt9Hhw%2FQj1V1ePKCvB2rPSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMqYzucS6MoGBG97GRKtwDWQvdBC2MwDLoP1gibfs35QtKPfUErd%2BYLE9l4pZ3vUqPxpAXiQ77pYpzRFEVEfHwIH%2Fs2vVfkSPC4F2xJOyb1tXz8TRKUI03imN5qjh0turI5yLdJKfUhsuwQdKph%2FgfG0KjdUoi3gjMLXNv6IXRH%2FwB%2BKViDjkU61gSPoyqVTTCWQd7l0nyBdiHOTp%2Bf1QEf3kCrCL6EUFFpyFhCqn5UsYJsefvw7oW8%2FPjyaDF6PeW%2F8mm53MyiCF6XJWaCBLv3WVT604IiB9y13o6nfIWrLuTGtyW94z1viCM0xpjGF%2FiT2kBNw00AJQzgLAcYt%2BOQ%2BcII1ghbFCTROsWkagd7a%2FfHVjqft8IquaGjsi8kdWE5uEF2as5ldzY2dRulZUnwYNXr6A2HrcinKlyGlQv0kDF0xj6VlfUMwhDG%2BmR4%2F49HIbNBSuPJ%2BsRZqsYm1Ly2oCTL6%2FsdJqVyFFHz1cqlyVHv3UK5QJJPhRiPgQU1YW2YFYoxkXW9wpvIl%2BeKiT8QuriBe1KPjrhnrJMrz3vWmr9KwkND7l%2Bi4e2%2BvmxSBaybjeVTDcVP4ZXYsAiG9rNwKhgr8%2Bc7j2GcIwsUxOXXRhXoBbenAGLKmAYA4EfJw0miMJRAW8axg74gE0ws6a30QY6pgGQwlrD%2Bwzi9CsnTCtvG0OJ%2Fz4Q53lNW6wQoefBZgjsvKfHC9Gm%2FFSj7PhXEA%2F3808jHDthdm54UQVP7KuM4QDrueAxUw7tarWcS%2BkNS0PPoNMpiEl%2BnkR9FrmdGVSNHJeeWeXybfYr4fDMDh%2FgfE19yj3OsOTMZWSVJNrKb2Fg7RXNy474Q6enYXnFf2qLGR8xa5LfE8IcxNGuGcg2KFDyLrFhOuuL&X-Amz-Signature=9c435440cda023d55f1fddd4db797146597fb99cb57a8b4b203786966bd509df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
