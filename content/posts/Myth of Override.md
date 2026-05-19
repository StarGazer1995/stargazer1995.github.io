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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VHVL3KC%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T143157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQC7EM%2BtSeBpuD%2FYOHHdG4vs4pYQn7tm8%2FQ4J9GxaWkDaAIgBs1JOeY2qaW0Kngz5b2xU8Ke48ofXj%2Bf%2FADAIDOpkcEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nz0Ie2XvnTBBrZyrcA6rbYxGhFd0bswrR2gJNf4VbZBWA3CGJJoaQC%2B4rnHAunTcS1T%2BXMUKEHpbLJJvwLxZR9%2Fi9wXXWR%2FCInK%2BUy%2B7dagdazU23Yj5llPhCYB9gDc8D0S2h64wBdswOu77Rk4eg6uXwgoZFU4nqFLtUn8JrzIq%2BqNR%2FSbeIkLbXwxn5PG7LYuvLIw8knn299%2F%2FOyk9G5bBijkT182QRdNwzBTIpZGqT98zvJYnvLduap90C%2FI36mRxgkIrWj4BwjzPAVu1tbSl%2BQffxV6DeJ5813nQabGxNINRwj0%2Bt8iIxjDhCv%2FmsM%2FbwXODXf8kitK6t7Xy71qjcG8skduWXrIGlinbmsWMmXp8c3gJ0bc618h3nHxdBz93agzWLLNbZ0%2F7Es9O6Atnwm0p0Yup4GL%2F8%2FBu0HuDj0OmM05HFmVmr%2Frbdfu%2B1YL1wNXV22DwY35Ih%2FvT%2BbZyIwx3QtQV%2FIG%2FxerPRqZWom5YpefWOa8509qa1PbhRv4g6UYLwfMWIHP3jPsnHI%2Bi%2Fgdq8Gk8X98%2F4kICIMLDdnmcOVdbqYSnGe32dy5Hqcg5%2Fbwrdv3hSuRAS%2FcFVC6hdAxnb0xoaCPukUFEaykVJuODDnfkNYVXIGZA%2Bd3GV%2Bw0d78I1R2vJMMTKsdAGOqUBSpvTvu6e72xqYlkV6nNvI4XtyAEmyh73qEW9aMIF01BETWicF0QhCHj15asgmGXXmwyf%2FDQ7xa%2FKZ29ftApghqLNzmAvEwnq3rf4meeRRtMrz2pbBAh3aupITgmVUqsWxFIODcRTua4zyAFpc%2FIYdrr0cVG5JbHruRy2HvJzTuQDzPTDO5W0vmaykTjVAZiSwctW%2F25nkb3KZuRHbpfxOiIyMGju&X-Amz-Signature=2ed01fd11af36781b2d8b6fef62b285391fcb3686844925a16655a405c437489&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VHVL3KC%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T143157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQC7EM%2BtSeBpuD%2FYOHHdG4vs4pYQn7tm8%2FQ4J9GxaWkDaAIgBs1JOeY2qaW0Kngz5b2xU8Ke48ofXj%2Bf%2FADAIDOpkcEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO5nz0Ie2XvnTBBrZyrcA6rbYxGhFd0bswrR2gJNf4VbZBWA3CGJJoaQC%2B4rnHAunTcS1T%2BXMUKEHpbLJJvwLxZR9%2Fi9wXXWR%2FCInK%2BUy%2B7dagdazU23Yj5llPhCYB9gDc8D0S2h64wBdswOu77Rk4eg6uXwgoZFU4nqFLtUn8JrzIq%2BqNR%2FSbeIkLbXwxn5PG7LYuvLIw8knn299%2F%2FOyk9G5bBijkT182QRdNwzBTIpZGqT98zvJYnvLduap90C%2FI36mRxgkIrWj4BwjzPAVu1tbSl%2BQffxV6DeJ5813nQabGxNINRwj0%2Bt8iIxjDhCv%2FmsM%2FbwXODXf8kitK6t7Xy71qjcG8skduWXrIGlinbmsWMmXp8c3gJ0bc618h3nHxdBz93agzWLLNbZ0%2F7Es9O6Atnwm0p0Yup4GL%2F8%2FBu0HuDj0OmM05HFmVmr%2Frbdfu%2B1YL1wNXV22DwY35Ih%2FvT%2BbZyIwx3QtQV%2FIG%2FxerPRqZWom5YpefWOa8509qa1PbhRv4g6UYLwfMWIHP3jPsnHI%2Bi%2Fgdq8Gk8X98%2F4kICIMLDdnmcOVdbqYSnGe32dy5Hqcg5%2Fbwrdv3hSuRAS%2FcFVC6hdAxnb0xoaCPukUFEaykVJuODDnfkNYVXIGZA%2Bd3GV%2Bw0d78I1R2vJMMTKsdAGOqUBSpvTvu6e72xqYlkV6nNvI4XtyAEmyh73qEW9aMIF01BETWicF0QhCHj15asgmGXXmwyf%2FDQ7xa%2FKZ29ftApghqLNzmAvEwnq3rf4meeRRtMrz2pbBAh3aupITgmVUqsWxFIODcRTua4zyAFpc%2FIYdrr0cVG5JbHruRy2HvJzTuQDzPTDO5W0vmaykTjVAZiSwctW%2F25nkb3KZuRHbpfxOiIyMGju&X-Amz-Signature=939e757642affaec551d251da964463c5e3f6f9fb0d3d10cc6a489803208fba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
