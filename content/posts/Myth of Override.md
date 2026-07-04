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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OURMKIV%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T185331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFG%2BT2aLO5lqLVZrypVg%2FEQFnx7eAMHgfUpzEEFaSHHeAiEApodzUaSqyr8jQT7bcJiK8v97V0AZAarCxHcaEAV%2FEG4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDN45OZRzkHC1JSk%2FhSrcA1wueaEGoa8vgc3Yyn9YGwc1PBxLPd6X5Zb%2B5%2FEW3AsdXA7KjzyelMfApy7XCvfCleFbkfGC87USlPMNrmqoinmqpc%2B%2BKLuGtqyXMmWyLvOJmAefDlcb4Kh0pWl5OynUHi30O8jMMWs8kYI4adfqDh7VKe050UtaW8i2IGc5qxFooM7jI9FV6EuJQuSXbRvM%2B23sZqaz4gCszcKCwbNMYQSWkpL%2FW3%2Bf4BrUZAQfUqPSbfR4N2IOiDOpnO64ap6gAPhHE%2FQ4NmgeuLhUL45A66DIkk2eNjuUwUlm75aalLdVHJKX%2BiT22bHABC2f5ha2Ue1CS2zMB%2FMTaeyz6lFgGyI0pEN9TOBFpggbQuGOvPOMu554bfwLrSFwbnNBzR9evXmwwUwqUM%2BDjQ%2Fi0Su92almlBWkZZ2vcVO59Xdic%2Fm3nQtjJfym6xzE%2BDfCS00b3bNu%2FcbPmgD%2FQL8EeUgYSoBVeqnT7KAdn1EpWXgsYhns5WM3EG6V9JMnJ%2FvL0SyyE9J7B7pF4ftpmw78sdUwtiQRSk%2BZ1MeP82GHN5wG%2BGCnc28b4yM4Cgf8Hbfq8WUvW5kOV1c1kgr1elAQur9tIOdm4rQojhJcc9cZgiyCGNdv5%2F%2BAbCMFtJDsJTh4MIj9pNIGOqUBaIorpVypPJXkTIl%2FYpExk%2BwVGiXEmtgwHH82s%2B9iVl3rrOYwVfgwITVXjY4ljC9AHcmGoFpxJM2nIg0K6TaVi9hl40uxxvk6uM3sd%2Bt%2FshQhCZlHZ3dzpWPh3ZJptcj6sUaRVUTl7qE810iDqyzd0MrV0grDeyHYldJZo0HpGD%2B%2FqHgyx%2B27NL8N0FEZVcVhoXyA5alk9TbXYh9eqp3tsBrBrKvM&X-Amz-Signature=9e3aa7f42212eae3b06789c0cd16eee67cd421198d8bb4442fee5faa25854f5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OURMKIV%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T185331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFG%2BT2aLO5lqLVZrypVg%2FEQFnx7eAMHgfUpzEEFaSHHeAiEApodzUaSqyr8jQT7bcJiK8v97V0AZAarCxHcaEAV%2FEG4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDN45OZRzkHC1JSk%2FhSrcA1wueaEGoa8vgc3Yyn9YGwc1PBxLPd6X5Zb%2B5%2FEW3AsdXA7KjzyelMfApy7XCvfCleFbkfGC87USlPMNrmqoinmqpc%2B%2BKLuGtqyXMmWyLvOJmAefDlcb4Kh0pWl5OynUHi30O8jMMWs8kYI4adfqDh7VKe050UtaW8i2IGc5qxFooM7jI9FV6EuJQuSXbRvM%2B23sZqaz4gCszcKCwbNMYQSWkpL%2FW3%2Bf4BrUZAQfUqPSbfR4N2IOiDOpnO64ap6gAPhHE%2FQ4NmgeuLhUL45A66DIkk2eNjuUwUlm75aalLdVHJKX%2BiT22bHABC2f5ha2Ue1CS2zMB%2FMTaeyz6lFgGyI0pEN9TOBFpggbQuGOvPOMu554bfwLrSFwbnNBzR9evXmwwUwqUM%2BDjQ%2Fi0Su92almlBWkZZ2vcVO59Xdic%2Fm3nQtjJfym6xzE%2BDfCS00b3bNu%2FcbPmgD%2FQL8EeUgYSoBVeqnT7KAdn1EpWXgsYhns5WM3EG6V9JMnJ%2FvL0SyyE9J7B7pF4ftpmw78sdUwtiQRSk%2BZ1MeP82GHN5wG%2BGCnc28b4yM4Cgf8Hbfq8WUvW5kOV1c1kgr1elAQur9tIOdm4rQojhJcc9cZgiyCGNdv5%2F%2BAbCMFtJDsJTh4MIj9pNIGOqUBaIorpVypPJXkTIl%2FYpExk%2BwVGiXEmtgwHH82s%2B9iVl3rrOYwVfgwITVXjY4ljC9AHcmGoFpxJM2nIg0K6TaVi9hl40uxxvk6uM3sd%2Bt%2FshQhCZlHZ3dzpWPh3ZJptcj6sUaRVUTl7qE810iDqyzd0MrV0grDeyHYldJZo0HpGD%2B%2FqHgyx%2B27NL8N0FEZVcVhoXyA5alk9TbXYh9eqp3tsBrBrKvM&X-Amz-Signature=26660523d9374d6bbd08bfb43a123cdde0eac4d5f4c455700301fbb6588e1861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
