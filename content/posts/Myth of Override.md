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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I53TGYT%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T012455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQCxX81P9Juh8HoMwKkTE22nJRtS9eNvipUFbXEEITKX0wIgaMU4GC7BNv%2B4DdObKWDdYxm14gVMhrxUrNaEH3yacrMq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM%2Bqy1eLkGSEOXkKRSrcA3XDhv2eo3HvXZsEXZJ876ygYQS6%2Bg8Vab0TlRtt1XUMamuigFXcoZqr8PKaclMVKGOvR%2F03oWSZM9QNETI7GmhvOHBXL4TCmc3t8GaUklPky6Rqy9WVRZh9MoXLy3O2PQinWXj8XFsP0XvYa45MTdd70bvtY%2BfSroXqX9Ws6yrx2AxRe28jo3J0JINJ%2B1byc4KIektA5MYivisn3ulRA7qdreVNC7UQzsnirdHs%2FFLWPlEzxdjsfOt2JzlVmuG0orBlXvHo47xn77456X4h7iFFoDODv%2BeUYoa%2Fu8DMjN8jCdedW%2Bc9%2FpTGbwccKbXkSLjt7HcQX3tSB1qvcmVu1r6HmWc%2F6cr6uNLYZv9Oda%2FWTozo3POxjNkroR%2BUg1cckymN7Ah4PYSMxY6fqHvj650VtwiF0cps%2BlGBlNmWX%2FuLUC%2Fx2TOgE7B9Ub8a%2BOdbbHCPN5fK6Pc0%2FPuXYR4RGTJtXelvi2W593g5c2FL9TUnYA1Q9ocH1War4pXaSCmZaua9wZTjaIiELf5xQdL%2F%2BLyP4amz8kWVcyWWrpju7yfIg7ikNp%2Bqwz%2F1oLlowCVbLIOQPmAOMZpMGVmDR6HJ1wDarx%2FguouHtQq7cMUG7h6d3VG8KMac%2FvGbcoTnMKLDm9YGOqUBy5qCopkt32brMTGmjPGigd4513YHIriggeU5aaENT9VwFgNQwb8zIpzzLc0fh4IgwRthmdsi%2Ffe0DzfcBe0uZlVvaBOB825eL8c0dxPmBnzaRqJsDLkeTntO3%2FBvA7ikQ9zkYiBESWKgGTq8nwcbwBxaUy7T3FxTxnPfvMMIS%2FxqaThLRwIfsEwCj5WowmE301KR4GCuj8YIJcGW%2BYE7QVeTsnSS&X-Amz-Signature=fa185ea91ada19eacf5c7d7a7e9f35d4ac4f0837b25773a327fc26000febec8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666I53TGYT%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T012455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQCxX81P9Juh8HoMwKkTE22nJRtS9eNvipUFbXEEITKX0wIgaMU4GC7BNv%2B4DdObKWDdYxm14gVMhrxUrNaEH3yacrMq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDM%2Bqy1eLkGSEOXkKRSrcA3XDhv2eo3HvXZsEXZJ876ygYQS6%2Bg8Vab0TlRtt1XUMamuigFXcoZqr8PKaclMVKGOvR%2F03oWSZM9QNETI7GmhvOHBXL4TCmc3t8GaUklPky6Rqy9WVRZh9MoXLy3O2PQinWXj8XFsP0XvYa45MTdd70bvtY%2BfSroXqX9Ws6yrx2AxRe28jo3J0JINJ%2B1byc4KIektA5MYivisn3ulRA7qdreVNC7UQzsnirdHs%2FFLWPlEzxdjsfOt2JzlVmuG0orBlXvHo47xn77456X4h7iFFoDODv%2BeUYoa%2Fu8DMjN8jCdedW%2Bc9%2FpTGbwccKbXkSLjt7HcQX3tSB1qvcmVu1r6HmWc%2F6cr6uNLYZv9Oda%2FWTozo3POxjNkroR%2BUg1cckymN7Ah4PYSMxY6fqHvj650VtwiF0cps%2BlGBlNmWX%2FuLUC%2Fx2TOgE7B9Ub8a%2BOdbbHCPN5fK6Pc0%2FPuXYR4RGTJtXelvi2W593g5c2FL9TUnYA1Q9ocH1War4pXaSCmZaua9wZTjaIiELf5xQdL%2F%2BLyP4amz8kWVcyWWrpju7yfIg7ikNp%2Bqwz%2F1oLlowCVbLIOQPmAOMZpMGVmDR6HJ1wDarx%2FguouHtQq7cMUG7h6d3VG8KMac%2FvGbcoTnMKLDm9YGOqUBy5qCopkt32brMTGmjPGigd4513YHIriggeU5aaENT9VwFgNQwb8zIpzzLc0fh4IgwRthmdsi%2Ffe0DzfcBe0uZlVvaBOB825eL8c0dxPmBnzaRqJsDLkeTntO3%2FBvA7ikQ9zkYiBESWKgGTq8nwcbwBxaUy7T3FxTxnPfvMMIS%2FxqaThLRwIfsEwCj5WowmE301KR4GCuj8YIJcGW%2BYE7QVeTsnSS&X-Amz-Signature=3a5d9e2ddf4c28c8dcbd019aa33cde5b06d4ae116a5fcbe85281afff874e6564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
