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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7A3I44%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T122631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIG0CQHz%2B7KaTvQuSlyEkp%2FYl0jUMxs%2B9octxJSl89AHkAiEA3nrtFKXQb1kkkCJbqPr%2BzjRkNkRs9HndNN4FivyNThMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDE07IlGJo7mvkd2coircA%2FPs9oCE2gTO7D60TDOpjmYJXDeSCoujORUtKJHPLhcKnyuBuewFK8IkhpJCBrNMPa8d6%2FkbjQlkIQJPYpU%2BnGyd6AtyFzeMK5UdASxThViRhI%2FkJCAsH3ciEgMJzvxuXUArXYfr7wCov1BPlm6TobpWHDgp3rLj0GljI2tFxBAhfs7BHL2%2FaMVCXnsilZDCEJjFn3kHiouAQqjt6WEmPpFowPW5jhApKZkbjUSF4bhU9CkzaaQyXl4ct3Hrb%2FdvOvRsGsat%2FnhhLb7tJb2vB8qQkAi1enaON6psZGiU%2FX82OAAKkFKcqoVLsh72axvs%2F9FlGb5uEGllRhiAsuIyLEYYDg8Uy5pWkXxdpHoW1Z8sOz6YJyKHlm412xAgCgRzcC53KiY0Cj8zoxdp4pjJX5uBM2QVsFOinc39LIOKln9357LVGb88MubM013mXNzxiZNvOnxGgnO5qrsGt9QuDogEy1G99vgke07pC%2F%2B%2BtRrYOCzM5lBYLM2eZDviMlaEtOs3JvTvhVQoCgs98vrGwCUap%2BW8Xp4wRwZrCn5D%2BstWtoyTHQ8vVw6e2rZPv4cuIT5lVv5mASbGhjdIVW9LWqRMcT3H0KDJODkivQ3%2BdsE59nGf7WnRGyDy%2B271MOi%2Bs9UGOqUB%2FrwM7NF7jl4Wfy91GqKqJ340xaD5FZQr%2FWUMVbz%2BA%2Fq9xUelCo04aHxWuCnF%2Be4FCzgb2XT1uCVOUqg5SB8gycg7MYJpT3D4CZrUuEjaJtPbjVxa9Atqdf9m2v%2BOklxWWxfr7ypiNOa98ZKJN2U1jEyMXEsQyLlIaq%2FByRwY0SodOHZa5XX%2BSXvRL20qTu%2BqwNBT3kSrQ%2B0OTNIGVWsX%2By33Qm%2F3&X-Amz-Signature=16fa128b54376d36a9f0602cdfbca1b8b4f409a777ad06f66fe8a0493d3bad5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7A3I44%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T122631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIG0CQHz%2B7KaTvQuSlyEkp%2FYl0jUMxs%2B9octxJSl89AHkAiEA3nrtFKXQb1kkkCJbqPr%2BzjRkNkRs9HndNN4FivyNThMq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDE07IlGJo7mvkd2coircA%2FPs9oCE2gTO7D60TDOpjmYJXDeSCoujORUtKJHPLhcKnyuBuewFK8IkhpJCBrNMPa8d6%2FkbjQlkIQJPYpU%2BnGyd6AtyFzeMK5UdASxThViRhI%2FkJCAsH3ciEgMJzvxuXUArXYfr7wCov1BPlm6TobpWHDgp3rLj0GljI2tFxBAhfs7BHL2%2FaMVCXnsilZDCEJjFn3kHiouAQqjt6WEmPpFowPW5jhApKZkbjUSF4bhU9CkzaaQyXl4ct3Hrb%2FdvOvRsGsat%2FnhhLb7tJb2vB8qQkAi1enaON6psZGiU%2FX82OAAKkFKcqoVLsh72axvs%2F9FlGb5uEGllRhiAsuIyLEYYDg8Uy5pWkXxdpHoW1Z8sOz6YJyKHlm412xAgCgRzcC53KiY0Cj8zoxdp4pjJX5uBM2QVsFOinc39LIOKln9357LVGb88MubM013mXNzxiZNvOnxGgnO5qrsGt9QuDogEy1G99vgke07pC%2F%2B%2BtRrYOCzM5lBYLM2eZDviMlaEtOs3JvTvhVQoCgs98vrGwCUap%2BW8Xp4wRwZrCn5D%2BstWtoyTHQ8vVw6e2rZPv4cuIT5lVv5mASbGhjdIVW9LWqRMcT3H0KDJODkivQ3%2BdsE59nGf7WnRGyDy%2B271MOi%2Bs9UGOqUB%2FrwM7NF7jl4Wfy91GqKqJ340xaD5FZQr%2FWUMVbz%2BA%2Fq9xUelCo04aHxWuCnF%2Be4FCzgb2XT1uCVOUqg5SB8gycg7MYJpT3D4CZrUuEjaJtPbjVxa9Atqdf9m2v%2BOklxWWxfr7ypiNOa98ZKJN2U1jEyMXEsQyLlIaq%2FByRwY0SodOHZa5XX%2BSXvRL20qTu%2BqwNBT3kSrQ%2B0OTNIGVWsX%2By33Qm%2F3&X-Amz-Signature=ffbbf4ada17afd7c9f7d4a7f43670894b94b165651c7502521e96acdb2f94549&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
