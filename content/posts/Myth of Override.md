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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QL4MNTHI%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T043348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGulymQqeiEcXSysm9S6UpOvHRUm5u7itDD8F4fBMeP%2FAiBv1i3tFGonhe5lTjMf1ZXRHbb6WD%2F8vIFd5Yt7kJFpYSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM%2FOqjssPR45YgTMGfKtwD9hqND7FhYe0r1MrecCFsuYPMcDIx7W3m3tB67PDI5H%2BNJFappR2TbG0IxzojwCaTfQ1a7yUnEv7oqjdWkdtny1bO1Y%2B99gyXXby0%2B9abk5VahZiXD3n5xhO8hFRWdzJwTvkBaIz0HbnTf7RbhkmsTMP9BK3Yuvt4rnPxD1lCzrMAm%2FiL17qO%2BOj2f9Axn%2FFN9rmYujdoVFIuN7pZ49dcIUc1cupSv8SFkX%2BiNhv%2FwR4KkQHIIIkHCkOmXSL7OpIJsV%2FepBD29nb%2BMiI2M66Lt7FPjv8wKNxuJL5beWtOTXfs8%2By1ZL9%2FuMgvYkXcziPEidxWMgkFJtT29wgtd%2FFxwS72fXjnAzdg8Z3zwdi3x7uR0UO80GXDc3rQW8vcLbwBLfiiMehvpeSJdoVG97gQ40EkQQoQmffAz0VEGxZ8aThzZuBmA1m0I2WXUaBHMLCIcGKGNZT1%2FKiif%2FKod1SQMiVv%2FZw9Q8mwQh20oZIdCemblbNLhjmbQKGC5mb1cDl5iib5cg5CoEPovThKBVAANrom8cBIccQS3ZueZlr%2Fegqm5t7bJDhE8BtVQ1Pi32SB5agqFcuAIiMqBPpSUpbU0%2F9j%2F4irBQhpJIU0WzLAhIiYbcQyuo1Sbq%2FQrcMwmZLJ1AY6pgED%2FvIuvm%2FwqFkfr7wbBR8j3e4fB0qhjXd8sO%2F%2ByBxc0vVsRDpLtc0XOVstKde3FNBqUVUtO8jkAnuJCO%2BfGZWnpV7Ol4vUmj7DD8oBhwsnBaPjzK0Tyk35ZsLbqfwzZt5koxVgx1skZTYNBU1MOYg980rWHAAnfZWdnYGwbkM4QrQ4k%2B4vG1XpyYyz4Fe9LptpYsfdxz7%2FDm91TN7Sa2I%2BN7PM5Ta%2B&X-Amz-Signature=86a92b8196e07daa1ababc23b060862202f33ed33407c8e825b4bf78803fa3da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QL4MNTHI%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T043348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGulymQqeiEcXSysm9S6UpOvHRUm5u7itDD8F4fBMeP%2FAiBv1i3tFGonhe5lTjMf1ZXRHbb6WD%2F8vIFd5Yt7kJFpYSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM%2FOqjssPR45YgTMGfKtwD9hqND7FhYe0r1MrecCFsuYPMcDIx7W3m3tB67PDI5H%2BNJFappR2TbG0IxzojwCaTfQ1a7yUnEv7oqjdWkdtny1bO1Y%2B99gyXXby0%2B9abk5VahZiXD3n5xhO8hFRWdzJwTvkBaIz0HbnTf7RbhkmsTMP9BK3Yuvt4rnPxD1lCzrMAm%2FiL17qO%2BOj2f9Axn%2FFN9rmYujdoVFIuN7pZ49dcIUc1cupSv8SFkX%2BiNhv%2FwR4KkQHIIIkHCkOmXSL7OpIJsV%2FepBD29nb%2BMiI2M66Lt7FPjv8wKNxuJL5beWtOTXfs8%2By1ZL9%2FuMgvYkXcziPEidxWMgkFJtT29wgtd%2FFxwS72fXjnAzdg8Z3zwdi3x7uR0UO80GXDc3rQW8vcLbwBLfiiMehvpeSJdoVG97gQ40EkQQoQmffAz0VEGxZ8aThzZuBmA1m0I2WXUaBHMLCIcGKGNZT1%2FKiif%2FKod1SQMiVv%2FZw9Q8mwQh20oZIdCemblbNLhjmbQKGC5mb1cDl5iib5cg5CoEPovThKBVAANrom8cBIccQS3ZueZlr%2Fegqm5t7bJDhE8BtVQ1Pi32SB5agqFcuAIiMqBPpSUpbU0%2F9j%2F4irBQhpJIU0WzLAhIiYbcQyuo1Sbq%2FQrcMwmZLJ1AY6pgED%2FvIuvm%2FwqFkfr7wbBR8j3e4fB0qhjXd8sO%2F%2ByBxc0vVsRDpLtc0XOVstKde3FNBqUVUtO8jkAnuJCO%2BfGZWnpV7Ol4vUmj7DD8oBhwsnBaPjzK0Tyk35ZsLbqfwzZt5koxVgx1skZTYNBU1MOYg980rWHAAnfZWdnYGwbkM4QrQ4k%2B4vG1XpyYyz4Fe9LptpYsfdxz7%2FDm91TN7Sa2I%2BN7PM5Ta%2B&X-Amz-Signature=611c362f21e89f46205e03a1190813f6dbfe2878e355467001a693722d8f6f12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
