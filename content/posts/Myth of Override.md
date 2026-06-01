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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5D6HJOY%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T021706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIETDVtZvJEEZ698xI%2FiS25ce7MlbQnoSq2vpTJWClSROAiBHzVuj9GESrwfMh36HVj4VdXQhZpmY6d0uiBrMq8l8iir%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIM9sJJPBhD7qX5opCxKtwD%2BQE0U%2BXdFwEaM8DYhWjIFq8Ct3Db7d1ahEA5HAEDY7Y4wXzfMW%2FrbqGWJtqdTddd1POmXhwsdYLNiIYmaKZ2407t4QV89mI6yabX13wSu1sumb3QRumcbvscuaZ4gmG%2BTu%2B%2BXZUWfgAP4FwLH6JjZh%2FA1QCpmLuZOZdzaimyfV08VOgw9lY0b%2FYnVhudtn92PWAhnjyiuz6bpZUiRhsZ9Ob0RJNuRdypK7IHSDzSddqe5SFMXzfsBac0JIHXM1Rw0P9%2BK0lw91DzpyMxyrl8ZMVEYcWY4YYQJbmRWR9g1aGx7DE2aFlfpA0aIXaO8ylbsOGKWYhR0rGj3hzJzdmeC9ncT0Si2MkbiOZXgXgS9HbUA4fDkr2Ick7lNLh4ZqZ6vi3Jnbaz7Q3FMOfxi6fFXp7w3AiA%2FffZ2msXIn%2BqUcoK7z8kCLWM%2FrASjPr4xbbrMV15vWpHtiuoMZFODLbJ02UJ1SoLb5eIzapCYw41ZZazogFJCWBjA%2Fi7I6fKnZLwx2qLqxqaCFTJjQj4%2Bg0ul1otMM%2B848XzKHtc6VI5E7oCPuMM%2F%2BVfEL5mvvsHu0x5aY7JqB365PsKXGJBTnRLwDprlFSeEtz5EBmeTCYx8GEy6P8dusW8s2pWR3ww4qXz0AY6pgG661KH%2B6lFTqWmdZINwJNbY2Mn%2FPl%2BGv8X5ANBqYq4SOhiWFgoZ7JEtlKjkMvd%2F9kfq3%2Fag%2FsTZj8AyK9qGiubNF8%2BtzSPkgWrcAbohoq0FQuRSIy54eZIjPxgeIonErY7eDqydd1Zrl3dmeJQKbKvC2TPU7ZmJ%2B4zryRQxjccSjiei5pxcnUS2VqqgPAu2yaeoYrMR0Dk7%2FTTMAowDUB9bx4XTH5K&X-Amz-Signature=543c42f93c065a99faee4c6c74e9a17ba39a9c64e73dbdc2c887d79c9922c523&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5D6HJOY%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T021706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIETDVtZvJEEZ698xI%2FiS25ce7MlbQnoSq2vpTJWClSROAiBHzVuj9GESrwfMh36HVj4VdXQhZpmY6d0uiBrMq8l8iir%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIM9sJJPBhD7qX5opCxKtwD%2BQE0U%2BXdFwEaM8DYhWjIFq8Ct3Db7d1ahEA5HAEDY7Y4wXzfMW%2FrbqGWJtqdTddd1POmXhwsdYLNiIYmaKZ2407t4QV89mI6yabX13wSu1sumb3QRumcbvscuaZ4gmG%2BTu%2B%2BXZUWfgAP4FwLH6JjZh%2FA1QCpmLuZOZdzaimyfV08VOgw9lY0b%2FYnVhudtn92PWAhnjyiuz6bpZUiRhsZ9Ob0RJNuRdypK7IHSDzSddqe5SFMXzfsBac0JIHXM1Rw0P9%2BK0lw91DzpyMxyrl8ZMVEYcWY4YYQJbmRWR9g1aGx7DE2aFlfpA0aIXaO8ylbsOGKWYhR0rGj3hzJzdmeC9ncT0Si2MkbiOZXgXgS9HbUA4fDkr2Ick7lNLh4ZqZ6vi3Jnbaz7Q3FMOfxi6fFXp7w3AiA%2FffZ2msXIn%2BqUcoK7z8kCLWM%2FrASjPr4xbbrMV15vWpHtiuoMZFODLbJ02UJ1SoLb5eIzapCYw41ZZazogFJCWBjA%2Fi7I6fKnZLwx2qLqxqaCFTJjQj4%2Bg0ul1otMM%2B848XzKHtc6VI5E7oCPuMM%2F%2BVfEL5mvvsHu0x5aY7JqB365PsKXGJBTnRLwDprlFSeEtz5EBmeTCYx8GEy6P8dusW8s2pWR3ww4qXz0AY6pgG661KH%2B6lFTqWmdZINwJNbY2Mn%2FPl%2BGv8X5ANBqYq4SOhiWFgoZ7JEtlKjkMvd%2F9kfq3%2Fag%2FsTZj8AyK9qGiubNF8%2BtzSPkgWrcAbohoq0FQuRSIy54eZIjPxgeIonErY7eDqydd1Zrl3dmeJQKbKvC2TPU7ZmJ%2B4zryRQxjccSjiei5pxcnUS2VqqgPAu2yaeoYrMR0Dk7%2FTTMAowDUB9bx4XTH5K&X-Amz-Signature=df2288b464a208041e5903074e5f148c2fec2729dbb564e241a30efbd6aeca9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
