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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJR2LFAN%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T042504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIALLgY%2F1htyfJkqXo4cck6MDvwfWu3%2BUk4WEqoI4Gj3nAiAzVeBVJPvSzmSLgkQ7%2FM%2B6M9IRcXguiK2KN%2BqiZtpFMyr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMycMFkFv35zLQhUoVKtwDM%2BrHMvwW%2BPVDTPs%2F6pXYBbkJvWb5OegT72pBHQ3GfW6eFEdkxpN4KltjdZszVmIbwZ9f8rJnmvZ4ftEnh4SvRGaWPMn8cesP%2FPYbNNVqWmvcoA220ULS2BZaw5bEw%2BnCPuHTqQA9thre7rj2%2Bwjo4r3LCKtp9LzzpRCqyw1hKW22Zb0NH75YqFZMcyEHmRElw1TtJSA2m%2BD2jcVmw9dgpbIYMlDZzZmh4QCrladJ11jDscPdhjVQp7%2F3AbAz%2B174y5%2FR8XzWFNEQKcCC7ZMaTxpgLYoZx6ATJWS71W%2FQEJsjAuTvOEqadFkNTN2SYvMx4n7sII%2FO2ZhXDyXZ%2BvuBiN8Z98gGnd%2Fh8ZQFa9SWzMlWs1ByV9CxsW%2BsEE4jNwb5oaavFJZxYMBX4BWd5jIvMkGcBiM7uE1M2XHYNoxDy4ERjy0WlaBlO9ARhq46DxvEA4525rmT1ApLWXdRB%2FX5ERLTSWgWigW12dr1gu0uq1ejpY2ahUXQBfXiKW2ZpM87otkqwCMihuQ4dk85gGtVvKDKAFr1GWefmqWqq6mvEswrWjB9FTKbBwsIFlGlCdaD6fuWUdbwAjTP9%2BJMli17tHirG%2Ff6sk971HgTv9Pk8tMeNli2Q1ZRxJTte5Ywje2D1AY6pgHQ9IMm11oLR4LVav1eNJEM6Zp4I50WDcSrFxuWg8TSGK11rW9uW6GNTBU09DuF2NIuJSTyT8DOEMXHFqtwzOVclgacbwGtWQN%2Ft0DoccDqW5sxmCW3iAileJbIhQzfsjQFZ0selvTisiK%2Bmxjx5PqYq5c1Jr%2B6V1MnR4nEoFGLuI7aqQtDQG0JFl0Q1eXbI%2F3WD2Llj4vwnrsZafXba8q0UeO%2FhHyL&X-Amz-Signature=c3a7b497c4b5fb8dbe87d10aac5ab2b6aab66e556a18aa842bc360b36ace2870&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJR2LFAN%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T042504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIALLgY%2F1htyfJkqXo4cck6MDvwfWu3%2BUk4WEqoI4Gj3nAiAzVeBVJPvSzmSLgkQ7%2FM%2B6M9IRcXguiK2KN%2BqiZtpFMyr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMycMFkFv35zLQhUoVKtwDM%2BrHMvwW%2BPVDTPs%2F6pXYBbkJvWb5OegT72pBHQ3GfW6eFEdkxpN4KltjdZszVmIbwZ9f8rJnmvZ4ftEnh4SvRGaWPMn8cesP%2FPYbNNVqWmvcoA220ULS2BZaw5bEw%2BnCPuHTqQA9thre7rj2%2Bwjo4r3LCKtp9LzzpRCqyw1hKW22Zb0NH75YqFZMcyEHmRElw1TtJSA2m%2BD2jcVmw9dgpbIYMlDZzZmh4QCrladJ11jDscPdhjVQp7%2F3AbAz%2B174y5%2FR8XzWFNEQKcCC7ZMaTxpgLYoZx6ATJWS71W%2FQEJsjAuTvOEqadFkNTN2SYvMx4n7sII%2FO2ZhXDyXZ%2BvuBiN8Z98gGnd%2Fh8ZQFa9SWzMlWs1ByV9CxsW%2BsEE4jNwb5oaavFJZxYMBX4BWd5jIvMkGcBiM7uE1M2XHYNoxDy4ERjy0WlaBlO9ARhq46DxvEA4525rmT1ApLWXdRB%2FX5ERLTSWgWigW12dr1gu0uq1ejpY2ahUXQBfXiKW2ZpM87otkqwCMihuQ4dk85gGtVvKDKAFr1GWefmqWqq6mvEswrWjB9FTKbBwsIFlGlCdaD6fuWUdbwAjTP9%2BJMli17tHirG%2Ff6sk971HgTv9Pk8tMeNli2Q1ZRxJTte5Ywje2D1AY6pgHQ9IMm11oLR4LVav1eNJEM6Zp4I50WDcSrFxuWg8TSGK11rW9uW6GNTBU09DuF2NIuJSTyT8DOEMXHFqtwzOVclgacbwGtWQN%2Ft0DoccDqW5sxmCW3iAileJbIhQzfsjQFZ0selvTisiK%2Bmxjx5PqYq5c1Jr%2B6V1MnR4nEoFGLuI7aqQtDQG0JFl0Q1eXbI%2F3WD2Llj4vwnrsZafXba8q0UeO%2FhHyL&X-Amz-Signature=d25109f33e047e619e136762c52305feff3199715ca895a385bac09fc071fd94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
