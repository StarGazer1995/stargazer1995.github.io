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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645HVXV36%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T142319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHcPWRJYFGu51qiWC67XaCCAIKD70a4jNozHM0qzu7L3AiEAiQG52bksXia7Uaj3MLNSM06EIaNy5gT0ZQLD3HE8EfwqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKQ0m3oxPYjLCGqSsircA46jmB4wOaxzE8Mt9SqaKtdGr4lOnIp2UfaXFLG4%2BZyO8LPLEPc90VOT6oSUWpn1l%2F42FE0OkE0TARZ5F6S3YVW5dJLSztPAc7RvOFyY1sJD2%2BKeLiCtf4uBQhtEjbzTKHLxqCtICcJ4yRh1aTaZPQY7wJNYalhA7uWB3gMRR2ob88OkigBxpv5KSTdX9JFCQATkbbzWSsH6qXNt4BoC%2FkRtwkIpcD%2B5D%2FJtBMyPzYhCJzI1yIKLV6td5S9ezwTkj1ij0zRjJeO2knjW3IVR74uaKa9XTEbxkFfyJm1IXuGvXRfn0hLWCf1yIo3jWDBpQWwoimv0Ecc1I4eCqHGnOe6sEdd3IQfx6CmO3EhqyPF6uaP8J5TIRjkLI6qOmChQraFt18KQxBwid74XWEW9kxB0LKX3yu8yF6i7ONwEX4nhKGS%2FpNj8eoucwtttEM0AT5Ncby7MqQ9OzZV5dtzpwc3osLcBOI4kLWP0wCyP%2FBsuUNodSg5LT%2FApYbVKBIju%2FbFSDCJvsKT03q0mt8ehYOmQ5QgvILFRVZDA5tT9cOxdWtvk1Q2Yug%2Bl8rACku0rlXng1kiT8zakuGLR0GXGeOC4kUJC8FcUjdXxvWFuaa8%2FIgvF7UmEYNTnvQrMMM%2BOodQGOqUBjEDEp1Q0mohraWpv0UubGJp7Sw2qcDxELjpnLjEqvCGOdJ0yCJUjwZI%2FkGub1RFN26BlyIDpr95slUfzycV1GpVe0Q9HRBetCVgi29LaZL%2BJsXQaxgI8gDHsrYJrMgOxB2IaFlK5jdZdSZXWpWun8B7z6G4afp%2Fxs7Kve6aWWGpEK9lunwT594QKjryh%2BSkkxx1t%2Bh0J1IGlwMShMhdZFijAuJY%2B&X-Amz-Signature=4f753b833ce3f18c99aa03edb3ad573b2f2eadc63f95c4df6a7adee3453da878&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645HVXV36%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T142319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHcPWRJYFGu51qiWC67XaCCAIKD70a4jNozHM0qzu7L3AiEAiQG52bksXia7Uaj3MLNSM06EIaNy5gT0ZQLD3HE8EfwqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKQ0m3oxPYjLCGqSsircA46jmB4wOaxzE8Mt9SqaKtdGr4lOnIp2UfaXFLG4%2BZyO8LPLEPc90VOT6oSUWpn1l%2F42FE0OkE0TARZ5F6S3YVW5dJLSztPAc7RvOFyY1sJD2%2BKeLiCtf4uBQhtEjbzTKHLxqCtICcJ4yRh1aTaZPQY7wJNYalhA7uWB3gMRR2ob88OkigBxpv5KSTdX9JFCQATkbbzWSsH6qXNt4BoC%2FkRtwkIpcD%2B5D%2FJtBMyPzYhCJzI1yIKLV6td5S9ezwTkj1ij0zRjJeO2knjW3IVR74uaKa9XTEbxkFfyJm1IXuGvXRfn0hLWCf1yIo3jWDBpQWwoimv0Ecc1I4eCqHGnOe6sEdd3IQfx6CmO3EhqyPF6uaP8J5TIRjkLI6qOmChQraFt18KQxBwid74XWEW9kxB0LKX3yu8yF6i7ONwEX4nhKGS%2FpNj8eoucwtttEM0AT5Ncby7MqQ9OzZV5dtzpwc3osLcBOI4kLWP0wCyP%2FBsuUNodSg5LT%2FApYbVKBIju%2FbFSDCJvsKT03q0mt8ehYOmQ5QgvILFRVZDA5tT9cOxdWtvk1Q2Yug%2Bl8rACku0rlXng1kiT8zakuGLR0GXGeOC4kUJC8FcUjdXxvWFuaa8%2FIgvF7UmEYNTnvQrMMM%2BOodQGOqUBjEDEp1Q0mohraWpv0UubGJp7Sw2qcDxELjpnLjEqvCGOdJ0yCJUjwZI%2FkGub1RFN26BlyIDpr95slUfzycV1GpVe0Q9HRBetCVgi29LaZL%2BJsXQaxgI8gDHsrYJrMgOxB2IaFlK5jdZdSZXWpWun8B7z6G4afp%2Fxs7Kve6aWWGpEK9lunwT594QKjryh%2BSkkxx1t%2Bh0J1IGlwMShMhdZFijAuJY%2B&X-Amz-Signature=1860863c2985a57ff7dabddf17d871219ed0f344b881c245a6fd317e745b24fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
