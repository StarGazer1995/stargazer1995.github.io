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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FPRKKWU%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T094509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpch6Qsai%2FoWnlNdKJYHqeTCnXbcz4A%2FYZCxgX3FfUhAiEA9jrA%2Bf3HTbo%2Fo2PyLKWeiAonz0%2B6VfZGmngdWVwoeycq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHPJQsVATQwWy0qGrCrcA1Gk5Dtgr1C6YN3ZiYFJKn4zKmPH36w0%2BwNF%2BtOxZyLdpUhFKigjW5m%2FyqHwPCJF6oDNBARIID7M8N6DVONAW9XTKXILt%2Bq0LzNrx0yWrwn6m%2BsgTf8kcBPv5Lojs%2FfOfrWIRru2bcGaXhLmy5BxU7HTfyxes4LuRzddss7LnOJW3fxFCyrit%2F4lctCn0gADKswfxNa0HjrZ%2F6u%2F3M5sx4XyXruociB5L%2FJL5jKii%2FN4huCXflGHBhgHcd4BUHkbqDyi%2F7V8GTdM272mU%2Bu10h2pPptvM8KiggVDO4SUWvC1WWDQKsZ586%2FPp85mxDvNLvZtC3VLWN4gn%2B8ZGqjpCrGutkuYPYX9oAiOwaq5KF6xqXn5EyE%2FsnwpQgrzBYoewsLZYPT7p%2FoxRA4VLa6rE1lm%2FU4j8LHbpIkh9bq7GDDEVJ36geDkZu2xAxse%2BvZF%2Fk%2FeHwpsugkHii2VDlaIkhSrzPhUvVB%2F6lAjuDmLohLcClJo%2B%2F8TWWynMypSbkUj8BdvcxwD3%2BF4MJSzEklEKOh9XKpcOYrzgx3gu0m6tl0ZJ7eyt2jaz1dE3HwKUy1hsMRFAkDgHJIeDJvtoRYHMGqYArxa4%2Fkm5LQNIZ%2BUwJeqw5hXJYuzkJWwmtn1MMPf59IGOqUBavwcyHpBEPtT6PeaU0CHKIVhCK4KpF0izThQXCbkqH2KthuIgwXoUkJzEe2CWDhCObQyvsyOvJM3xAUNKv7zTUO4dKEn9IUlVnWIHP0zk8h2VkzCDbasl0tiRQ5m%2B2YTgPIGrhI%2FPrhxcs3C%2Fu4bb%2FJgvnS3%2BnxRnzgMN5stjU1RDAqBHqsKzqUKPH6E5BAXwXBG%2BeylzPqc5YcXRNUNGI5NESU2&X-Amz-Signature=4a7cb5f6a4cca5e410ed1762e917240d02dff39ce2d5bae6662aa0e726087651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FPRKKWU%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T094509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBpch6Qsai%2FoWnlNdKJYHqeTCnXbcz4A%2FYZCxgX3FfUhAiEA9jrA%2Bf3HTbo%2Fo2PyLKWeiAonz0%2B6VfZGmngdWVwoeycq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHPJQsVATQwWy0qGrCrcA1Gk5Dtgr1C6YN3ZiYFJKn4zKmPH36w0%2BwNF%2BtOxZyLdpUhFKigjW5m%2FyqHwPCJF6oDNBARIID7M8N6DVONAW9XTKXILt%2Bq0LzNrx0yWrwn6m%2BsgTf8kcBPv5Lojs%2FfOfrWIRru2bcGaXhLmy5BxU7HTfyxes4LuRzddss7LnOJW3fxFCyrit%2F4lctCn0gADKswfxNa0HjrZ%2F6u%2F3M5sx4XyXruociB5L%2FJL5jKii%2FN4huCXflGHBhgHcd4BUHkbqDyi%2F7V8GTdM272mU%2Bu10h2pPptvM8KiggVDO4SUWvC1WWDQKsZ586%2FPp85mxDvNLvZtC3VLWN4gn%2B8ZGqjpCrGutkuYPYX9oAiOwaq5KF6xqXn5EyE%2FsnwpQgrzBYoewsLZYPT7p%2FoxRA4VLa6rE1lm%2FU4j8LHbpIkh9bq7GDDEVJ36geDkZu2xAxse%2BvZF%2Fk%2FeHwpsugkHii2VDlaIkhSrzPhUvVB%2F6lAjuDmLohLcClJo%2B%2F8TWWynMypSbkUj8BdvcxwD3%2BF4MJSzEklEKOh9XKpcOYrzgx3gu0m6tl0ZJ7eyt2jaz1dE3HwKUy1hsMRFAkDgHJIeDJvtoRYHMGqYArxa4%2Fkm5LQNIZ%2BUwJeqw5hXJYuzkJWwmtn1MMPf59IGOqUBavwcyHpBEPtT6PeaU0CHKIVhCK4KpF0izThQXCbkqH2KthuIgwXoUkJzEe2CWDhCObQyvsyOvJM3xAUNKv7zTUO4dKEn9IUlVnWIHP0zk8h2VkzCDbasl0tiRQ5m%2B2YTgPIGrhI%2FPrhxcs3C%2Fu4bb%2FJgvnS3%2BnxRnzgMN5stjU1RDAqBHqsKzqUKPH6E5BAXwXBG%2BeylzPqc5YcXRNUNGI5NESU2&X-Amz-Signature=38b54833f20678830662631c37d99b33e086e6c948b0a7c4efd82f9588f70d6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
