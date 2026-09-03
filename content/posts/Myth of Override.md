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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HLKWQXH%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T014808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD1t9VFLHbcbfmvXGHrNEuAgE1su1Q7RTxlrdpWPElIFAIgNaQDh9F4H1mRZwWbKhQZrCq4CtZMZQi0UPy1XFhUBnEqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbS6HzwHHuo%2FXj6tyrcA%2BGU%2BAVO5NEXR8vW1fO3lgfiJKwlsjZZPqIV8mQjKGP7pHOExj7p8LUN1mXeNqYLXHrBBK7xMQU96jgomVe9a6vfqA05qnyG7D2pOWQFvL5Bx%2B%2FR0qysiystQb%2FnVB0nmwAyvwxR2twEdwdoKFJOvLrY%2BW%2FQ7%2BTw3EZCSvW%2BvKHpqHK5fQ9oRpQjr8hoFS%2F6sjhRMCddYoX%2BpN8QrajJBv8vMXSQrj8X%2F6t7esc%2FVquqEWnv1uNp0oUD7nP3AzlAl9FdA33qiwffr3GmabYkFk0wOl8d%2BIQ6xS6Fqob7mfmcKBoZoa0Wjn5VvLrRZCYpX775SlE4NHKUy50QPodK1FngldxSJfCWc4gDmQ2vF1fEyMC1yXf%2BH6rooaOBLvaKxNLtYpNIDXazl4vllRWARo6L0Leo9T4OhSu5rI8UvCDXkBRHXqnVx9XAU%2F68S6PTM1zYo6lVbQCjSyplO892et%2BQiT3BSpBeCohoxH89dL%2B%2BnsCFCM4E%2BK%2BArKfAzuccALNEMqpMAtvA2%2F%2BkbI0mKSRESNQDPsjxpRZfjXRjWYdiZBL8jFdUyaz8I3YPS45DGY9FFR2dsgGNlQiiN2fChd6yjBocm%2FhrfTCa4axMvIlsWruflIE%2F78tFjwnRMNbI4tQGOqUBymZGnim0hlxekQI1%2BPIuS9JC%2Ffu6GcjSAKsSE%2BfH2txSAW4jeaAFaT0SsQv6UyKVP4v6MhbuEQGvMVP%2BMH8IZ62dBwZAl1F0OswDORY75msuLFqeC36z0SNpa8cvBXL5S8RuW6tsAmqjUT67iJFKfb%2BRjAX5%2FfggVx6ptnBE9%2BwKECQQv4DQ28%2Fn6TNwlTQiyw8auGLdp47mPPO14zbKhkb3TM%2Bt&X-Amz-Signature=3bc5e9c3bc4e96f227d1ab10390c28023173eb990bca8b47151043c70f8f4339&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HLKWQXH%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T014808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQD1t9VFLHbcbfmvXGHrNEuAgE1su1Q7RTxlrdpWPElIFAIgNaQDh9F4H1mRZwWbKhQZrCq4CtZMZQi0UPy1XFhUBnEqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbS6HzwHHuo%2FXj6tyrcA%2BGU%2BAVO5NEXR8vW1fO3lgfiJKwlsjZZPqIV8mQjKGP7pHOExj7p8LUN1mXeNqYLXHrBBK7xMQU96jgomVe9a6vfqA05qnyG7D2pOWQFvL5Bx%2B%2FR0qysiystQb%2FnVB0nmwAyvwxR2twEdwdoKFJOvLrY%2BW%2FQ7%2BTw3EZCSvW%2BvKHpqHK5fQ9oRpQjr8hoFS%2F6sjhRMCddYoX%2BpN8QrajJBv8vMXSQrj8X%2F6t7esc%2FVquqEWnv1uNp0oUD7nP3AzlAl9FdA33qiwffr3GmabYkFk0wOl8d%2BIQ6xS6Fqob7mfmcKBoZoa0Wjn5VvLrRZCYpX775SlE4NHKUy50QPodK1FngldxSJfCWc4gDmQ2vF1fEyMC1yXf%2BH6rooaOBLvaKxNLtYpNIDXazl4vllRWARo6L0Leo9T4OhSu5rI8UvCDXkBRHXqnVx9XAU%2F68S6PTM1zYo6lVbQCjSyplO892et%2BQiT3BSpBeCohoxH89dL%2B%2BnsCFCM4E%2BK%2BArKfAzuccALNEMqpMAtvA2%2F%2BkbI0mKSRESNQDPsjxpRZfjXRjWYdiZBL8jFdUyaz8I3YPS45DGY9FFR2dsgGNlQiiN2fChd6yjBocm%2FhrfTCa4axMvIlsWruflIE%2F78tFjwnRMNbI4tQGOqUBymZGnim0hlxekQI1%2BPIuS9JC%2Ffu6GcjSAKsSE%2BfH2txSAW4jeaAFaT0SsQv6UyKVP4v6MhbuEQGvMVP%2BMH8IZ62dBwZAl1F0OswDORY75msuLFqeC36z0SNpa8cvBXL5S8RuW6tsAmqjUT67iJFKfb%2BRjAX5%2FfggVx6ptnBE9%2BwKECQQv4DQ28%2Fn6TNwlTQiyw8auGLdp47mPPO14zbKhkb3TM%2Bt&X-Amz-Signature=0a0699b3b91a335527292e7777bfd0625a9fd671619515978d76beb191fa4212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
