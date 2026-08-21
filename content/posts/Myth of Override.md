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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDOAPX4S%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T101857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDmYFvCvm4JJ8fwYbsfWLdziDlOQmwVm0566AvkuJ3agIhAM6%2BYTM5Sg4Xhb%2F%2FiJNaB%2F8c9A%2FBUXwcRD0Ms%2B3W%2FfhZKogECKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0TyBGZcUbUN4p%2Fegq3APBovFs%2Fhp2lQDgT%2FkB%2BTNDfBebcpe9kOMfLHI2YlMuVGPAeD%2BpEUzhpTD9WsbtgoUpDpOfZjUllseh%2FniiK9BtKajUi0YwKMNrdshZh5H7NaYoeAxPUIwQ94dS8tH0HKqhSnOi4Pj%2FawB7XSSTzfwaylE1%2Fg1LzJRlFzji44mDU%2FpQNT%2B0Yh3C0gGbjZoMCr5F%2FDjsN4WgPR1eLVk8pfLI7zlG%2BfuXZ1AE7AiTuadT3T0aaxFwPYh8LLb9Quvvh8t2WSbfz%2BS5p5rnHdvyzzcOZYIJQhv0QXFI2ojsrdHStcj7ckHOvzipNKPiD4%2Fx9QZUNkTMgrbEQ7jE1Qwl5PkwzYppapDCfjQ%2FoX81ZVLSRs4erqj9rFyl2oQMtJHrrR17f5ub6n%2FWvLcQSSoP8ucwKE1F0PBgUsPgp9yBuSxG6crOpBCIGid5WOJes6%2BaSA8ceL%2BujIL3r1YXnt004LKkN52CxkpWklWQ3fhWyBfobPoKxLJY2IZm0b9xt8mH%2BVb0BteG3y2H95oR9pX%2FInGqGQCC76qWUcn0dPIhZXqYERkIQdEJBAb%2FNCHsLCM86vWWCiYuyYqzxrkO4UY1iu3fC7jF9r%2BN8SbwdPUeBvU0WHdQC730TdfZLiMjrTDKoaDUBjqkAWsJd0nBjV%2FAvBpBCim%2By2%2FfALickgtLVNrt7%2FQSHqGDcaeR8YLpQWgaYY5CouSJxLZ5XU9OVd%2F56SSA%2BMjONkb%2BoYRXbeDjQBmJq2A6SvZtaSm5foq9jaU%2Bc8cAhp59ZATaCl4ZBMHNl7cdFIZdQvSXCZEHVVXug%2BEqxdVC%2FdWej%2B9C8xOLBtiOT08LviaFEyvWn1hQxaEhR67HyrBLAhLd8Bd5&X-Amz-Signature=d31b97a4b4a60fa03cf9464c2fcda282f326feff748fd02886571af2cc4820dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDOAPX4S%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T101857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCDmYFvCvm4JJ8fwYbsfWLdziDlOQmwVm0566AvkuJ3agIhAM6%2BYTM5Sg4Xhb%2F%2FiJNaB%2F8c9A%2FBUXwcRD0Ms%2B3W%2FfhZKogECKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0TyBGZcUbUN4p%2Fegq3APBovFs%2Fhp2lQDgT%2FkB%2BTNDfBebcpe9kOMfLHI2YlMuVGPAeD%2BpEUzhpTD9WsbtgoUpDpOfZjUllseh%2FniiK9BtKajUi0YwKMNrdshZh5H7NaYoeAxPUIwQ94dS8tH0HKqhSnOi4Pj%2FawB7XSSTzfwaylE1%2Fg1LzJRlFzji44mDU%2FpQNT%2B0Yh3C0gGbjZoMCr5F%2FDjsN4WgPR1eLVk8pfLI7zlG%2BfuXZ1AE7AiTuadT3T0aaxFwPYh8LLb9Quvvh8t2WSbfz%2BS5p5rnHdvyzzcOZYIJQhv0QXFI2ojsrdHStcj7ckHOvzipNKPiD4%2Fx9QZUNkTMgrbEQ7jE1Qwl5PkwzYppapDCfjQ%2FoX81ZVLSRs4erqj9rFyl2oQMtJHrrR17f5ub6n%2FWvLcQSSoP8ucwKE1F0PBgUsPgp9yBuSxG6crOpBCIGid5WOJes6%2BaSA8ceL%2BujIL3r1YXnt004LKkN52CxkpWklWQ3fhWyBfobPoKxLJY2IZm0b9xt8mH%2BVb0BteG3y2H95oR9pX%2FInGqGQCC76qWUcn0dPIhZXqYERkIQdEJBAb%2FNCHsLCM86vWWCiYuyYqzxrkO4UY1iu3fC7jF9r%2BN8SbwdPUeBvU0WHdQC730TdfZLiMjrTDKoaDUBjqkAWsJd0nBjV%2FAvBpBCim%2By2%2FfALickgtLVNrt7%2FQSHqGDcaeR8YLpQWgaYY5CouSJxLZ5XU9OVd%2F56SSA%2BMjONkb%2BoYRXbeDjQBmJq2A6SvZtaSm5foq9jaU%2Bc8cAhp59ZATaCl4ZBMHNl7cdFIZdQvSXCZEHVVXug%2BEqxdVC%2FdWej%2B9C8xOLBtiOT08LviaFEyvWn1hQxaEhR67HyrBLAhLd8Bd5&X-Amz-Signature=888a07dfea6e52f08f6a9f6c491e7de4b0ffbb7484dbf58055217916ffaf516d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
