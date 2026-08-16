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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM527STL%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T220940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIF013eC1586NFRfEbDzprXTWRCiRhJ5yS4X61ehXCYCvAiEArWg1QrReQ8wipnZ1DASAPC17KSK2FNBNCQgLUiVPHqIq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDEyPHBCwSW4w2SjsjircA7cQbIzWx4WSZHIpkUswd7JKzU0%2FoK9b%2F%2FCN56OWbL1lUiP9LdAXgIeKjFAIYGtbqeCngCWqyIQ66K3c5JWdA%2BFzLuDW9jTi71MSlF%2FJNz7rjLc7gkpwtBe54A%2FQLcFYQ50Of9eYQDSQC7gvNXA4npDj%2BTkFkttY2DFpsIS75GSDFwF5CJkQGQDA8kMSyT6i1EdcwBaX16VIGbAkJ5AJ6J2edMUd0YDJVbzltYofvqZcbH%2BHwfZsvAIQ6uBrJEJmYRDfJCBMLxASQQflXzg1DZnyMD9NjXZnHAyw8zgi0T33TW%2FpqPgttxO0MiGG0%2BdKBzs9hBYHyEQWagdjgQtiqS0VK3urAaSvEYcxgfB4Y6jdCtFyRdBQaJxr06aDSgIbif4IU5NOjc2CMWdIZvCFY%2FnWzDpdCiHk8pENCo87wFIZ%2FI7cmx4%2FfdcMmJdrQ7jzD%2BiZ%2FX8oLa8%2FIe9zWHt23C1KquRB%2BzJ7PMCrCRA2cZsUHHRXcKgUdNODxGDknkfEySCeuoKdo1ruxxvV1uN3tW8b5JjL8J4Yh6Kr5a74%2Ffo0L9ay6lQ4%2FvLcCSniafVw00reUlHAFpZn4ARJRCMyaMwEF0jrHGfO%2F3A%2FOwahIZJkrce%2BWtjXLqyzkiBuMKe4iNQGOqUBKMU7vAzPUz3T%2FxUehGlr7EAQVbgZSpTR17MeX09Mpl5E2hyIzeXaLY87rmfk6ehY5sW%2F%2Bty2cBQArBQHlt3Gy28TjQ54DQgNRUUbp8sxHrHTkRuH0mCW9aWfIG9LmOiCXB4AFJu61IMuqwL4hZbORx%2BXNqMWdQG1RcZPcLG6jNoUGXfGMgmL%2B2BtbzteeKRmJkqP7lbfNLxIV9g0FXwGLG62akXn&X-Amz-Signature=7665ee8c2b4f748d2a758be731d2302b90bbcd8c3e0ffdcb01a33eba83cf1299&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM527STL%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T220940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIF013eC1586NFRfEbDzprXTWRCiRhJ5yS4X61ehXCYCvAiEArWg1QrReQ8wipnZ1DASAPC17KSK2FNBNCQgLUiVPHqIq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDEyPHBCwSW4w2SjsjircA7cQbIzWx4WSZHIpkUswd7JKzU0%2FoK9b%2F%2FCN56OWbL1lUiP9LdAXgIeKjFAIYGtbqeCngCWqyIQ66K3c5JWdA%2BFzLuDW9jTi71MSlF%2FJNz7rjLc7gkpwtBe54A%2FQLcFYQ50Of9eYQDSQC7gvNXA4npDj%2BTkFkttY2DFpsIS75GSDFwF5CJkQGQDA8kMSyT6i1EdcwBaX16VIGbAkJ5AJ6J2edMUd0YDJVbzltYofvqZcbH%2BHwfZsvAIQ6uBrJEJmYRDfJCBMLxASQQflXzg1DZnyMD9NjXZnHAyw8zgi0T33TW%2FpqPgttxO0MiGG0%2BdKBzs9hBYHyEQWagdjgQtiqS0VK3urAaSvEYcxgfB4Y6jdCtFyRdBQaJxr06aDSgIbif4IU5NOjc2CMWdIZvCFY%2FnWzDpdCiHk8pENCo87wFIZ%2FI7cmx4%2FfdcMmJdrQ7jzD%2BiZ%2FX8oLa8%2FIe9zWHt23C1KquRB%2BzJ7PMCrCRA2cZsUHHRXcKgUdNODxGDknkfEySCeuoKdo1ruxxvV1uN3tW8b5JjL8J4Yh6Kr5a74%2Ffo0L9ay6lQ4%2FvLcCSniafVw00reUlHAFpZn4ARJRCMyaMwEF0jrHGfO%2F3A%2FOwahIZJkrce%2BWtjXLqyzkiBuMKe4iNQGOqUBKMU7vAzPUz3T%2FxUehGlr7EAQVbgZSpTR17MeX09Mpl5E2hyIzeXaLY87rmfk6ehY5sW%2F%2Bty2cBQArBQHlt3Gy28TjQ54DQgNRUUbp8sxHrHTkRuH0mCW9aWfIG9LmOiCXB4AFJu61IMuqwL4hZbORx%2BXNqMWdQG1RcZPcLG6jNoUGXfGMgmL%2B2BtbzteeKRmJkqP7lbfNLxIV9g0FXwGLG62akXn&X-Amz-Signature=7c2a421c9f2ca0eee75bddbed6c1706a12d14443e9b21ef59592368e24244b59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
