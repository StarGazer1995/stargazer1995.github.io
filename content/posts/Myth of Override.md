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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZP5GA4F%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T164139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLFI82ehCq0ghXSVGcM7EDBFZw7GDgM3T1%2BHzAHAYfwIgSgRHhFHSlW%2FTtlraapsb54kp7giPackA9bAfLDk3HjoqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDANr96onQDT%2BS0teRSrcA%2FlkGTo5ggR%2BM%2BvxmOeRQmr%2BWKHxdec4k%2BYduXjX%2Bt11nJkVdOvjw8cak2NxM4PYDU%2BDnS7ulthuJFM%2FbUfMFpN7lTa9doZoLO5kLienfxX7AIFiBqRBAIbUgXNNElzB9JItq6nClbWbqGRVMDN5pYmBH7Q%2F4WoW%2BSMfdD7pcwLAzzWlKIUt%2FUjZ86PcoJXcVdvGfUiZMe2bqXPmmnctI0xmbx1YIeYlyIS%2BTu1F57Q42at2ifdskXUxULxi3PdzUeDd5V6Z23aI5PF4P7u39RfS47fPwuEX3FNqfXKOTPZ4%2FAJeAuafws2rsMIBKXzsyRCt7AnigNDE7cNwTXcfI7YnfiY7hVxgL0tX1mSh0p7I%2FF%2BQhXEq9DRUrZsqQZJiRvhtO2hVHSNkMbDqq6rHvQvljqfxyMt3d5%2FAURUqzAi2xhvHv%2BI9GZ9aTWNgQXDhhAnXwCPOKsPkeVxJ5GxoouaRB3GW9FT4A1ulxO8a%2BSiIPDAvRpA3nx2JesY9aoxb58inpVIt%2FbUMpN1qoWV3WiOLq0vzvpmVwYiHc3trOantR72WmdoSi%2B7XzcVmO0RFlf3NA4kR5bDIelUfsIidrTpcrLYVgbvkzc0pjhClDYKqyqJsS9%2F7%2BDK8kkkhMOr059MGOqUBF2oGuxMevvDmrqYzgowC86L17xwl2grTt7fJOtHn%2Byjbou%2BZqROt3SpD10LzhZgpIPKVocT7MBat2eK3eJELNxy9hl4bYvx%2BuGWPrFzfnkP3vkSsbegU5N%2Bxz%2BWZMWIS2D6H6OQc5U%2BRyxo6lOTB1KzOZg2F1xzXRly3OLVGtUMU4bIPc0HUASJ%2FaE%2FPtupmHS3l1nRuSZJP6D6oc4jMeFt%2Fz4TE&X-Amz-Signature=93c31507c7be192efc83c1e28d9292683956235d2b0319f6d4194b37859012f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZP5GA4F%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T164139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvLFI82ehCq0ghXSVGcM7EDBFZw7GDgM3T1%2BHzAHAYfwIgSgRHhFHSlW%2FTtlraapsb54kp7giPackA9bAfLDk3HjoqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDANr96onQDT%2BS0teRSrcA%2FlkGTo5ggR%2BM%2BvxmOeRQmr%2BWKHxdec4k%2BYduXjX%2Bt11nJkVdOvjw8cak2NxM4PYDU%2BDnS7ulthuJFM%2FbUfMFpN7lTa9doZoLO5kLienfxX7AIFiBqRBAIbUgXNNElzB9JItq6nClbWbqGRVMDN5pYmBH7Q%2F4WoW%2BSMfdD7pcwLAzzWlKIUt%2FUjZ86PcoJXcVdvGfUiZMe2bqXPmmnctI0xmbx1YIeYlyIS%2BTu1F57Q42at2ifdskXUxULxi3PdzUeDd5V6Z23aI5PF4P7u39RfS47fPwuEX3FNqfXKOTPZ4%2FAJeAuafws2rsMIBKXzsyRCt7AnigNDE7cNwTXcfI7YnfiY7hVxgL0tX1mSh0p7I%2FF%2BQhXEq9DRUrZsqQZJiRvhtO2hVHSNkMbDqq6rHvQvljqfxyMt3d5%2FAURUqzAi2xhvHv%2BI9GZ9aTWNgQXDhhAnXwCPOKsPkeVxJ5GxoouaRB3GW9FT4A1ulxO8a%2BSiIPDAvRpA3nx2JesY9aoxb58inpVIt%2FbUMpN1qoWV3WiOLq0vzvpmVwYiHc3trOantR72WmdoSi%2B7XzcVmO0RFlf3NA4kR5bDIelUfsIidrTpcrLYVgbvkzc0pjhClDYKqyqJsS9%2F7%2BDK8kkkhMOr059MGOqUBF2oGuxMevvDmrqYzgowC86L17xwl2grTt7fJOtHn%2Byjbou%2BZqROt3SpD10LzhZgpIPKVocT7MBat2eK3eJELNxy9hl4bYvx%2BuGWPrFzfnkP3vkSsbegU5N%2Bxz%2BWZMWIS2D6H6OQc5U%2BRyxo6lOTB1KzOZg2F1xzXRly3OLVGtUMU4bIPc0HUASJ%2FaE%2FPtupmHS3l1nRuSZJP6D6oc4jMeFt%2Fz4TE&X-Amz-Signature=4098d51b2dc150c9eb253f37cdd80b1c0facc520f97d64ae12ff51599cf0cc82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
