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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLGAFAWT%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T062336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBs8SrsbeFb%2BXhtAgdfkDfTk3GQPicM9TWQAZx0lf1QZAiEA2yQApvPM4vJjC9JxboBoREQL90b%2B9Qo219AsFQmkbcoqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCfA6Fk%2FMuwY4sfSryrcA%2FKFsPHvEbJLqzUvRF1UI5QKyeOBP9cpcfWgUzXECGvVUQnyCh4MWAaQ%2FS8XhxEHo0l6BfxXswS53Q3LWBNzKoochD97cJpVLbwLcDqEa%2Fs8itlAPE3Nf0ngGTIK3R1j1Vb7HRQtmfJp7%2BdWS7d66EsJkPfFRHfvUU%2Fah4lBJHeiR0b4WPNHDI1ggmIqee0A2hFP5bf3SijOjyqc0n1e1ixyo3FY1eRQLAnR1yIb1UmqjlRn686FmbUyu9gMj6Ua4s32pBZwi0nahs8r5yWme%2FVYFi6ev8eQVtwJfQUmzsiyPX2EXbLnAoj%2BqFCdTnPWaC8BEt%2FHcm28xGHV4rZlvUGZAWYVZiCnFkrWfSpB2Y8xSfaT%2F891uRtUaqgVZpQiJoZKyEqPsjOu8mPcw1OIF7kubCOQCnR7M1pYpQovlKtS7UT2SWUGAfAXmS4YXLJznaIcftEy9dOIJxG4KA0TYiUhEY1rGUbKxgkn6T8HK9iRgwaeBq55YAgXamEcK%2Bc%2BONQi80HUOOK%2FANV9f1ddHJx8GwM7Gi6IK7dIluO9NG6tqFw5SlmTBZ0UIfpZpx%2F71BdPipt%2FEGs13R9hidkJZ%2BMQn%2FeAyBg%2F81hdOvjOmJnIBv2d6RViTyUARnGnMIytmtQGOqUBNBPpJG32c4KwBAgnVOyZOWwMf2vZcQiOE8zqpLO4AZqxThzn0kXsTda25K2YY8dAklC3wp0AXYVxCdQJREiAKpOAFWgxHkTcJ3lQFxJwGOS8TttXF1%2B0Az0DQ2Enn8IMF8OJEmXkqvqphyUY0IUZK%2BJVbu3liT7Mxd2k3cQnOAblnELlieRuv6JUfXoPfWkVItpZT7RFWbcJJSTRHXtWhwJOm81A&X-Amz-Signature=b164dc8beb0a7e38a3d8f06fc8d4c1cf900c33134a21dd93163fa9f34a57a5ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLGAFAWT%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T062336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBs8SrsbeFb%2BXhtAgdfkDfTk3GQPicM9TWQAZx0lf1QZAiEA2yQApvPM4vJjC9JxboBoREQL90b%2B9Qo219AsFQmkbcoqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCfA6Fk%2FMuwY4sfSryrcA%2FKFsPHvEbJLqzUvRF1UI5QKyeOBP9cpcfWgUzXECGvVUQnyCh4MWAaQ%2FS8XhxEHo0l6BfxXswS53Q3LWBNzKoochD97cJpVLbwLcDqEa%2Fs8itlAPE3Nf0ngGTIK3R1j1Vb7HRQtmfJp7%2BdWS7d66EsJkPfFRHfvUU%2Fah4lBJHeiR0b4WPNHDI1ggmIqee0A2hFP5bf3SijOjyqc0n1e1ixyo3FY1eRQLAnR1yIb1UmqjlRn686FmbUyu9gMj6Ua4s32pBZwi0nahs8r5yWme%2FVYFi6ev8eQVtwJfQUmzsiyPX2EXbLnAoj%2BqFCdTnPWaC8BEt%2FHcm28xGHV4rZlvUGZAWYVZiCnFkrWfSpB2Y8xSfaT%2F891uRtUaqgVZpQiJoZKyEqPsjOu8mPcw1OIF7kubCOQCnR7M1pYpQovlKtS7UT2SWUGAfAXmS4YXLJznaIcftEy9dOIJxG4KA0TYiUhEY1rGUbKxgkn6T8HK9iRgwaeBq55YAgXamEcK%2Bc%2BONQi80HUOOK%2FANV9f1ddHJx8GwM7Gi6IK7dIluO9NG6tqFw5SlmTBZ0UIfpZpx%2F71BdPipt%2FEGs13R9hidkJZ%2BMQn%2FeAyBg%2F81hdOvjOmJnIBv2d6RViTyUARnGnMIytmtQGOqUBNBPpJG32c4KwBAgnVOyZOWwMf2vZcQiOE8zqpLO4AZqxThzn0kXsTda25K2YY8dAklC3wp0AXYVxCdQJREiAKpOAFWgxHkTcJ3lQFxJwGOS8TttXF1%2B0Az0DQ2Enn8IMF8OJEmXkqvqphyUY0IUZK%2BJVbu3liT7Mxd2k3cQnOAblnELlieRuv6JUfXoPfWkVItpZT7RFWbcJJSTRHXtWhwJOm81A&X-Amz-Signature=6aa9703c812e3aa7c21a564d6a2145061da90d5156e61a8f4279cc45374ad53a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
