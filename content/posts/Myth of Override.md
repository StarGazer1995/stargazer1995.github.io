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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FIAJCDW%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T011042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCICASjBKb0YX34EeXQhX4g5X%2FFA1EJcJFpHr0m7c%2BkQS4AiAPX71z3L%2Fv%2BFdUvwlhvD7s8cLdneYZHBHq8phQXIqbtyr%2FAwgBEAAaDDYzNzQyMzE4MzgwNSIMmAfEk%2FBDAq7ApiiGKtwDO4aXQUilfXLKEKm7uzkWJGU5zxBZ1VyOjIsjMoFjSuXau5DZfCEgLSI%2BvumXKxX%2FbLakD8HZMx%2FhCTgImWXz6XUdFTwO0xm%2FWRtQCd9vCyHsD1eL5Qp%2BQkakY2Iwua1chctTMech8Et%2FfFYh%2Fih3nfBezFPpHWi95c6Q%2BnkHJk3vkntPoWMWuxs%2FgJfChYpQelAJjKH88i0zahIu%2F%2BY3mA5ug5UrrEZ%2F%2FSqdPxTUFxh5mtjhg8zaldXroaXzao4GTK7R5XR0dbd9cUwu%2BY2VXte5Rm5HMpmMw2J%2BHZWH0O51UomVQo%2BN2uSe28hBHqi8QudcDJ04VLFVNtwPHKArUACRgwCZHSG%2F%2BO5tROJde7pYGXN60fh3KdqgBBf9LJisqD0JCxu%2BGiGljlHy52BPHFnhl7uKWFtFzj5O1OaO9Aql3bq4Np9mmHhTKOxlFI2dt1dM79QMj9QyKU3icCQ165KofAScXlvDHsNuDWijIz4KPl3%2B5n4Wv3Z8eljdTrbttZpf2kL%2BrFkv36CG2vYgkSF3F98zzT7UfXINiH7mLwR6bDXl1tcIGy0ToQlVMRmI%2FWRuFAu7xo6L0E8LcCZYivRR9WbbBWhO%2B5%2FMPforJ82H%2FrmA8bgGb03j26gwjq6W1gY6pgGv3b8fVeqpvXqDU7YaixmlYN1ljlG0DBwIzlPTmjQuaoh6eRma%2B5anYEMXdZRzyz6tBQzgtZPu8kFqyNfYoe7bjf1jDfC6kNl%2F%2B8r0ByhVdA6gwbpaPbSENdE66exgMzn6iRq%2F0BdFiJr%2BXA4%2BE8FK1aEfIavmCLlLDaovkjmAjC42dVYMDt6mLeCJxL20RPYAWKVgSuF612pwH9ND3aKB32oVpvoF&X-Amz-Signature=591aea0f97bc86615255ec0d685837de2f18e1c9b23fade05deb62c9baa2aa73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FIAJCDW%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T011042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCICASjBKb0YX34EeXQhX4g5X%2FFA1EJcJFpHr0m7c%2BkQS4AiAPX71z3L%2Fv%2BFdUvwlhvD7s8cLdneYZHBHq8phQXIqbtyr%2FAwgBEAAaDDYzNzQyMzE4MzgwNSIMmAfEk%2FBDAq7ApiiGKtwDO4aXQUilfXLKEKm7uzkWJGU5zxBZ1VyOjIsjMoFjSuXau5DZfCEgLSI%2BvumXKxX%2FbLakD8HZMx%2FhCTgImWXz6XUdFTwO0xm%2FWRtQCd9vCyHsD1eL5Qp%2BQkakY2Iwua1chctTMech8Et%2FfFYh%2Fih3nfBezFPpHWi95c6Q%2BnkHJk3vkntPoWMWuxs%2FgJfChYpQelAJjKH88i0zahIu%2F%2BY3mA5ug5UrrEZ%2F%2FSqdPxTUFxh5mtjhg8zaldXroaXzao4GTK7R5XR0dbd9cUwu%2BY2VXte5Rm5HMpmMw2J%2BHZWH0O51UomVQo%2BN2uSe28hBHqi8QudcDJ04VLFVNtwPHKArUACRgwCZHSG%2F%2BO5tROJde7pYGXN60fh3KdqgBBf9LJisqD0JCxu%2BGiGljlHy52BPHFnhl7uKWFtFzj5O1OaO9Aql3bq4Np9mmHhTKOxlFI2dt1dM79QMj9QyKU3icCQ165KofAScXlvDHsNuDWijIz4KPl3%2B5n4Wv3Z8eljdTrbttZpf2kL%2BrFkv36CG2vYgkSF3F98zzT7UfXINiH7mLwR6bDXl1tcIGy0ToQlVMRmI%2FWRuFAu7xo6L0E8LcCZYivRR9WbbBWhO%2B5%2FMPforJ82H%2FrmA8bgGb03j26gwjq6W1gY6pgGv3b8fVeqpvXqDU7YaixmlYN1ljlG0DBwIzlPTmjQuaoh6eRma%2B5anYEMXdZRzyz6tBQzgtZPu8kFqyNfYoe7bjf1jDfC6kNl%2F%2B8r0ByhVdA6gwbpaPbSENdE66exgMzn6iRq%2F0BdFiJr%2BXA4%2BE8FK1aEfIavmCLlLDaovkjmAjC42dVYMDt6mLeCJxL20RPYAWKVgSuF612pwH9ND3aKB32oVpvoF&X-Amz-Signature=ffb369dee4455a7b86dcae929e9ed8b124a97b23b687a630352ba8627ed95bbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
