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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CW377K5%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T192734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFJOB%2B7twRaHSBC7kuETa3kifLh39Pxktjig2081dz3RAiAM%2BS6IUonfZzTHrSdGZ50BiGR6F%2F%2F00I0c6IYB18%2BAVyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMu0ooFwJnApxipO4SKtwDcfinyOb%2Fz47KflDHu8qMJ313FA%2B6CweaCZZ3LMoVzNBMNF%2Ff%2BLqmvakQq0%2FoCJGDfEzQ7pOyL0lrRhLZEfEHGwVWp3vM7bgEDA4VDc8OxDfpuQnR6XlfCfgcdVG4zvIftttVS4%2F50sIbjNq9FDCQnzhID7J0ucfJwd4aWGoow8LQ2PS%2BwN08siovMFwU6iedg%2B0fbPaN4Uyg%2BhxmpwmAzFt4nYeFwKiw5C8tOw7E6MAF1AI1rJyunNejkqxjftXajP%2Bqv2I3szZIMMVQ2h0up9BunjbiQqPvYZ%2BxFve7Dk5Vr7130jJ0H%2FjXL8rRl%2Fzh9HCUemklxE1ZjC%2BEIYTwt2TK9NPNn%2Bf6YWdZxWy1oXG3zFaAB25xTziwMv98pTDmiGqVoHwSn5lnt6kWcsminKsJ7vcnoNDAJ6FvjdnzdVgsRjyfrreFjWtWs%2BI7lVrz1aLHbeeJYkJTdPcIq0w7zZ7wH3N5dJ%2B8AoWfuTFWdjWcof61ItfG235WXkRBtddeUtYDEcjDVhAXYlXvJpms%2BYtEmAhZiXRlOMQFsHuGb%2B0qrXXo2D8BpwpfysPFnvfXmFIucXn7PL8HT1L1gdvyV7xSL2wJw4PfIVzO5CRN0mslwrQ8R7HP3TJj728wl%2FCN0AY6pgFjjvIwXDZdEB6Rmge9cGcEItWqIrXBy55S%2F0Du0D7djuYgvmaHKF4dBCCxb%2B6pTE8WADhepUrPHwAMEwlAa19Cy8demMeCCAJGyeNnB%2BzU4nTDOb8zQME26vtx6EjJcROGs7%2FaTypVs2eko9WqwSUl2WgSt0FxktUk4qOtU01s8fXlqVJmgvV5GX5EzjFuEpwSbdWfO0j7OYapfjVMBd02rBMOSavo&X-Amz-Signature=dd51f90e7cc4c8f95e6caf28c977293f31a8fce7defaedf93145514b222e9f6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CW377K5%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T192734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFJOB%2B7twRaHSBC7kuETa3kifLh39Pxktjig2081dz3RAiAM%2BS6IUonfZzTHrSdGZ50BiGR6F%2F%2F00I0c6IYB18%2BAVyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMu0ooFwJnApxipO4SKtwDcfinyOb%2Fz47KflDHu8qMJ313FA%2B6CweaCZZ3LMoVzNBMNF%2Ff%2BLqmvakQq0%2FoCJGDfEzQ7pOyL0lrRhLZEfEHGwVWp3vM7bgEDA4VDc8OxDfpuQnR6XlfCfgcdVG4zvIftttVS4%2F50sIbjNq9FDCQnzhID7J0ucfJwd4aWGoow8LQ2PS%2BwN08siovMFwU6iedg%2B0fbPaN4Uyg%2BhxmpwmAzFt4nYeFwKiw5C8tOw7E6MAF1AI1rJyunNejkqxjftXajP%2Bqv2I3szZIMMVQ2h0up9BunjbiQqPvYZ%2BxFve7Dk5Vr7130jJ0H%2FjXL8rRl%2Fzh9HCUemklxE1ZjC%2BEIYTwt2TK9NPNn%2Bf6YWdZxWy1oXG3zFaAB25xTziwMv98pTDmiGqVoHwSn5lnt6kWcsminKsJ7vcnoNDAJ6FvjdnzdVgsRjyfrreFjWtWs%2BI7lVrz1aLHbeeJYkJTdPcIq0w7zZ7wH3N5dJ%2B8AoWfuTFWdjWcof61ItfG235WXkRBtddeUtYDEcjDVhAXYlXvJpms%2BYtEmAhZiXRlOMQFsHuGb%2B0qrXXo2D8BpwpfysPFnvfXmFIucXn7PL8HT1L1gdvyV7xSL2wJw4PfIVzO5CRN0mslwrQ8R7HP3TJj728wl%2FCN0AY6pgFjjvIwXDZdEB6Rmge9cGcEItWqIrXBy55S%2F0Du0D7djuYgvmaHKF4dBCCxb%2B6pTE8WADhepUrPHwAMEwlAa19Cy8demMeCCAJGyeNnB%2BzU4nTDOb8zQME26vtx6EjJcROGs7%2FaTypVs2eko9WqwSUl2WgSt0FxktUk4qOtU01s8fXlqVJmgvV5GX5EzjFuEpwSbdWfO0j7OYapfjVMBd02rBMOSavo&X-Amz-Signature=598f750b4bcd09eda647cc09aae2e1c514109a56a65d7f5923ed9b4df0ed0251&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
