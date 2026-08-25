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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X72MIAJJ%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T102039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIFIVk1b3%2FZpUj%2BDb%2BbbvWOzjKWTbTgY1KBZwE5ywcfPRAiAIgjsDyRa2XGhTChNUALl4%2BKCwFA%2FMYOVz3DmdspuDhyr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMYSYxTmwerjmhPa98KtwDCHwC%2BuvIyO%2BJeDpu424DHEXieftSZRlECV5JDaRRkCY6%2FVdyBnQoWsG07E7W1zXjo22Q2V6a0L05sbMGFLgCee1Fv5Z9dzJFyWuuKsrXtFV16uCpy7vV7CQsKIMcWLvM8%2BaT1LP%2FLegFSsATD64hIr7%2FiPlSDJN1JWePNYThiCzmmQfp0WOdAiKHDWaAXXRWzsU41ZFOCSZ40hIm%2Fqha6OQg5ug5dkrumM3h3frC3fqlFDtzC8ZVjAnT8YcIi9at7riTYIG3AAPK5Do3T6EITnv0Ulmqd6cedvuqwnLs%2FHKeaRqizFiDwXFAkHe89TsXdToqPVzTTa2Z0xN2vx9ctRQQsssboOGghYbw8BW0ytGTsXduG5RZtHm12DkgYSHt%2FZJU8QYGe2t9yLpm3lNZ9Sz1KRRqCKk5rFLan7A7BTLCHcmYupboTs0Zt2ZJdvTIOgN4FFFsuhVaEEj6L477SAwF%2Bt1F2ZQS%2FzVmB0lT82ah8EBSbueprdX6mznl%2FLmayPi2E6oqcQPloV%2BkbXafyHTi0AmbbyFLP2FdAvZJF87IEzwb2MiYHp076nypXFByDlW5FE7t1y%2BnR3NKEl5CVlkkS%2BupW%2FJQ%2BIpAdias0k5MhZT6qDFS0%2BuINkQwp9O11AY6pgG%2BZVRWMzHMQq%2FmbzP9o%2FIz1xpS5GfHd3HvPJQXjEeyHIr241Nq83ZoWD57X%2FQcWB7eE1xgH5Lnx%2FUsimUtWrMqPFo8E90ozf9UxpDhOyhLNDuHOB8PjKqg53rEq%2Fw0ha0KbcdSi6zU%2Bs2fjrXNlMpPvWYb7gjux5SfiYQTG4CSkJUxkvEOKJA0aXXk%2BQeB%2B2wQtRHwQVxQUER%2FJkvSzYEYj%2FqwDmFm&X-Amz-Signature=3eeacea0d4df2b21c2bd7b7beaf79cd484e2ebab1866d4ab5d2c05b781052be2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X72MIAJJ%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T102039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIFIVk1b3%2FZpUj%2BDb%2BbbvWOzjKWTbTgY1KBZwE5ywcfPRAiAIgjsDyRa2XGhTChNUALl4%2BKCwFA%2FMYOVz3DmdspuDhyr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMYSYxTmwerjmhPa98KtwDCHwC%2BuvIyO%2BJeDpu424DHEXieftSZRlECV5JDaRRkCY6%2FVdyBnQoWsG07E7W1zXjo22Q2V6a0L05sbMGFLgCee1Fv5Z9dzJFyWuuKsrXtFV16uCpy7vV7CQsKIMcWLvM8%2BaT1LP%2FLegFSsATD64hIr7%2FiPlSDJN1JWePNYThiCzmmQfp0WOdAiKHDWaAXXRWzsU41ZFOCSZ40hIm%2Fqha6OQg5ug5dkrumM3h3frC3fqlFDtzC8ZVjAnT8YcIi9at7riTYIG3AAPK5Do3T6EITnv0Ulmqd6cedvuqwnLs%2FHKeaRqizFiDwXFAkHe89TsXdToqPVzTTa2Z0xN2vx9ctRQQsssboOGghYbw8BW0ytGTsXduG5RZtHm12DkgYSHt%2FZJU8QYGe2t9yLpm3lNZ9Sz1KRRqCKk5rFLan7A7BTLCHcmYupboTs0Zt2ZJdvTIOgN4FFFsuhVaEEj6L477SAwF%2Bt1F2ZQS%2FzVmB0lT82ah8EBSbueprdX6mznl%2FLmayPi2E6oqcQPloV%2BkbXafyHTi0AmbbyFLP2FdAvZJF87IEzwb2MiYHp076nypXFByDlW5FE7t1y%2BnR3NKEl5CVlkkS%2BupW%2FJQ%2BIpAdias0k5MhZT6qDFS0%2BuINkQwp9O11AY6pgG%2BZVRWMzHMQq%2FmbzP9o%2FIz1xpS5GfHd3HvPJQXjEeyHIr241Nq83ZoWD57X%2FQcWB7eE1xgH5Lnx%2FUsimUtWrMqPFo8E90ozf9UxpDhOyhLNDuHOB8PjKqg53rEq%2Fw0ha0KbcdSi6zU%2Bs2fjrXNlMpPvWYb7gjux5SfiYQTG4CSkJUxkvEOKJA0aXXk%2BQeB%2B2wQtRHwQVxQUER%2FJkvSzYEYj%2FqwDmFm&X-Amz-Signature=de17cffdf6a9061c76b907aad0a86d703d422073b6be4b19e9dfd21f8c2d32e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
