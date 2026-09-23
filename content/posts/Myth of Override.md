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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBUQPA4W%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T191831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3O9%2BC8msD363zEs0qwxW%2B0HD0llcGanqx1lJnzfWyJgIgFUVci2mwnwODUAwK9WQDDtP%2B%2Bz1aCnsEvqgvls8E6cgqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsnNMoGq9wFzgvASrcA2PYrO3sZJp7HIfFs6HdaaevNXmi%2F2ufI%2FclHFds2UyNldHrcUCGL5uz3CtYMDg5Qx6t6NJjBsoAg0eyIzRV0q9xuSr2d9iXjd2YeSZWY1Y3Dtjd27h9b1y7BG7Z9x%2FiNUp9jRsVZcmM6LCsx6CYtDupDshW5aTG5J6EUR%2Fy8g5dv8%2FmaB1xv5p%2Fw21ennZJ%2FgLG8NyL0Mh%2FPnxyl7C3wBOQfNv6iY2%2FvqaaDIYbZw9WOKZ0UAtuO6dNG6dCaLkcFKNQvodE0tE44re1kH4s5J9zudnR9Nrl44qOHkRhkZID%2FhP5X4lN6%2FoDAMeYI5j%2BPhBcr7DyhTLPrIRJC8BekTycC4Bxy5AUbUnTSbdCWXuvyGA0eU4wwb6cP79%2FCXNRzzJZXwcY1WlAasJ3jOQ2MpX4TwY3ahzdpmVbHk9PzMxhzI8QyQM9%2BtbvZICLJoJ5Y6Mzsg3qZf8eHbl4pIrrjOVVVp2V63S0mABuZ%2F%2BQa4TqZdBMo84dg5DCDsOvy40mMwMzHVXToJW1%2BRE30FSQyHRn5IlyniXzsrSbUxZ90yB7ceTZucaMjqF0%2F8kmYb%2BpQz7Jc3w4%2FPiev0xsADYjpZk1dof0Z92i61Prr1TcbeHfQeL5Xc%2FBOxyJX6uEMJix0NUGOqUB9pM45XKz0AOEYt9HsQdOWD33xA1SW8IycYRCLSlXZgYAgXhdlwUI45a0JrSNxYJmEMGx374qmPWwbtKkTeyBdcLkkUAzApH3YJG0poFj%2FcIncStjcLXmF%2Bk%2FYzJu8XuVn%2FP2%2BcEItOrKSAOa5ZtHLQ1g4VOAA2iGIi1sAPwo9yBFAf7l3tFudZ0R4euE3C7u5bIZ%2F28g5Z39mDAW4v%2FOCsvn9y5T&X-Amz-Signature=789373e8bfa61335cfc28e131d544b27fb7cfdf0e934e9a5ba28356c8f05cd2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBUQPA4W%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T191831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3O9%2BC8msD363zEs0qwxW%2B0HD0llcGanqx1lJnzfWyJgIgFUVci2mwnwODUAwK9WQDDtP%2B%2Bz1aCnsEvqgvls8E6cgqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrsnNMoGq9wFzgvASrcA2PYrO3sZJp7HIfFs6HdaaevNXmi%2F2ufI%2FclHFds2UyNldHrcUCGL5uz3CtYMDg5Qx6t6NJjBsoAg0eyIzRV0q9xuSr2d9iXjd2YeSZWY1Y3Dtjd27h9b1y7BG7Z9x%2FiNUp9jRsVZcmM6LCsx6CYtDupDshW5aTG5J6EUR%2Fy8g5dv8%2FmaB1xv5p%2Fw21ennZJ%2FgLG8NyL0Mh%2FPnxyl7C3wBOQfNv6iY2%2FvqaaDIYbZw9WOKZ0UAtuO6dNG6dCaLkcFKNQvodE0tE44re1kH4s5J9zudnR9Nrl44qOHkRhkZID%2FhP5X4lN6%2FoDAMeYI5j%2BPhBcr7DyhTLPrIRJC8BekTycC4Bxy5AUbUnTSbdCWXuvyGA0eU4wwb6cP79%2FCXNRzzJZXwcY1WlAasJ3jOQ2MpX4TwY3ahzdpmVbHk9PzMxhzI8QyQM9%2BtbvZICLJoJ5Y6Mzsg3qZf8eHbl4pIrrjOVVVp2V63S0mABuZ%2F%2BQa4TqZdBMo84dg5DCDsOvy40mMwMzHVXToJW1%2BRE30FSQyHRn5IlyniXzsrSbUxZ90yB7ceTZucaMjqF0%2F8kmYb%2BpQz7Jc3w4%2FPiev0xsADYjpZk1dof0Z92i61Prr1TcbeHfQeL5Xc%2FBOxyJX6uEMJix0NUGOqUB9pM45XKz0AOEYt9HsQdOWD33xA1SW8IycYRCLSlXZgYAgXhdlwUI45a0JrSNxYJmEMGx374qmPWwbtKkTeyBdcLkkUAzApH3YJG0poFj%2FcIncStjcLXmF%2Bk%2FYzJu8XuVn%2FP2%2BcEItOrKSAOa5ZtHLQ1g4VOAA2iGIi1sAPwo9yBFAf7l3tFudZ0R4euE3C7u5bIZ%2F28g5Z39mDAW4v%2FOCsvn9y5T&X-Amz-Signature=571500be0dd5b8fa1be67b1680cf3a3966c0d21f3627d99c0134d1024d386042&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
