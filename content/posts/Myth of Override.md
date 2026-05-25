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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJY7OMIG%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T125637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV4IqtPtMU%2F9iG3PlTv4UUnM34ozGe0jCz6ECPErL9ZAIgDgirpS9mTkWqyOagk6qNEhQe5I50EWJjgGf5IVXsSBsq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDF6NvydQh%2Bm4a%2BCFGSrcA2AtNyPTTAvJz%2F1IXC2Hkzi90GMuXu%2BzcN5WW6dLMamv2YSPPpy8P79Gg0%2Bp4MQ5Q3KG3jsbbhwNHW0%2FDr%2FQnrBIoKAala3lKopU1NcaQk9LOFb0V4b4mpYJMi7G6zKZWIF3SFZIznZQnV2oWYS9nLrS7XjqiX1B27YiJ4VCVDO%2F%2B2h4BM02%2F0voR2t5DTvBM4QXetA7r%2BEALdOoj26ZBpF73tyZukp8nr60DRSDPBi8dnBavXx3zjSSPD7v%2Fet7%2FwRFjuwjT83qyqb1Wp7Pch43He%2BHG4qbrcOZ5qFq1ZhNHd9qz8EkUqWr9eRfn0TPIY2nhTo%2F3d%2BBv7dr20hnw3ch1q45KWOb6xsVv0HzV7i3x74%2BpL5MHgFI1oynW1HmSsm50bizOoDpjjhxQ5%2Fv24M2M%2BydyjZhtpZGzxp63fKSc7WzSLEGfeMbQnW79g%2BxUEU4iBMOTiGJB5x9rhrzKPMAZJ8jStYGjm6r%2FaWWB0hkTCo5e0SgLklQk8xdpm0Ma7iR%2Bq2tsa8yiy2SMU2iw95w8yTii9du9ibXGdNeOcEheblQjdNyK6C2VhcwoCiGR9ybJXdDFcjYUBsaNqgniZHVloOBR797LErmh0u5QSk%2FZy%2BGoJyESwPPQbAnMMWN0NAGOqUBFwIng7s%2FBFd9uHSHC3%2BU9MP0wb%2BkVRFTpUhxaRm1s%2FZD6kZgVzCA%2BO2TwghFcLlUrE8zHKbQB1yx5YR3t%2B3%2BpLIxd3%2B%2BqL1TC0P0ZTY8Q1JSqoHx8mdVNH6xpwtBqjrMFmLlejVh%2Bt4ALBYBDWSPr%2BcRpo4HxXs0s%2FNAIVzzqoctVB%2Bz3F1Pv4eicMpi2Dz8vMcbtfxci8eLoVTt8mdGK3r%2Bi8Lv&X-Amz-Signature=ee146cdbcf2ee1d8df86e9d3adb45f5f389238f082b392fd07aedc2678bb7c8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJY7OMIG%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T125637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV4IqtPtMU%2F9iG3PlTv4UUnM34ozGe0jCz6ECPErL9ZAIgDgirpS9mTkWqyOagk6qNEhQe5I50EWJjgGf5IVXsSBsq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDF6NvydQh%2Bm4a%2BCFGSrcA2AtNyPTTAvJz%2F1IXC2Hkzi90GMuXu%2BzcN5WW6dLMamv2YSPPpy8P79Gg0%2Bp4MQ5Q3KG3jsbbhwNHW0%2FDr%2FQnrBIoKAala3lKopU1NcaQk9LOFb0V4b4mpYJMi7G6zKZWIF3SFZIznZQnV2oWYS9nLrS7XjqiX1B27YiJ4VCVDO%2F%2B2h4BM02%2F0voR2t5DTvBM4QXetA7r%2BEALdOoj26ZBpF73tyZukp8nr60DRSDPBi8dnBavXx3zjSSPD7v%2Fet7%2FwRFjuwjT83qyqb1Wp7Pch43He%2BHG4qbrcOZ5qFq1ZhNHd9qz8EkUqWr9eRfn0TPIY2nhTo%2F3d%2BBv7dr20hnw3ch1q45KWOb6xsVv0HzV7i3x74%2BpL5MHgFI1oynW1HmSsm50bizOoDpjjhxQ5%2Fv24M2M%2BydyjZhtpZGzxp63fKSc7WzSLEGfeMbQnW79g%2BxUEU4iBMOTiGJB5x9rhrzKPMAZJ8jStYGjm6r%2FaWWB0hkTCo5e0SgLklQk8xdpm0Ma7iR%2Bq2tsa8yiy2SMU2iw95w8yTii9du9ibXGdNeOcEheblQjdNyK6C2VhcwoCiGR9ybJXdDFcjYUBsaNqgniZHVloOBR797LErmh0u5QSk%2FZy%2BGoJyESwPPQbAnMMWN0NAGOqUBFwIng7s%2FBFd9uHSHC3%2BU9MP0wb%2BkVRFTpUhxaRm1s%2FZD6kZgVzCA%2BO2TwghFcLlUrE8zHKbQB1yx5YR3t%2B3%2BpLIxd3%2B%2BqL1TC0P0ZTY8Q1JSqoHx8mdVNH6xpwtBqjrMFmLlejVh%2Bt4ALBYBDWSPr%2BcRpo4HxXs0s%2FNAIVzzqoctVB%2Bz3F1Pv4eicMpi2Dz8vMcbtfxci8eLoVTt8mdGK3r%2Bi8Lv&X-Amz-Signature=6e0d0352403032d333c808bee36768bcad74b353a1b3606731b92b71070c6a18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
