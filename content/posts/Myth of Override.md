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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOIMZO4R%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T003354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEvuuDNrqkyLaN37Rz%2BOpqakLUNtP3gjTqSfb%2FM4uSauAiEAszM1TqdOlGPdjwlmK%2BEqBSHccoKF3LGoCpk57sCophcq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDDBxJfTJU4ugzgBeSyrcAz6npg%2FRGUBAWQ0Zwb9jf7b0HykmZ4znpfSB3hv8ElHtzg2Q1SVvUnpQxkaeRQOJD%2BycP7fCjlrdfuy%2BcmgOkiPZwuEMw3vx1nx1IGFs4bzh7Ct7zjwRI2s4nLc1UlY4FAsdWOrYAQpZf5%2Bp%2FDo54uJjGYLI5XBWTHtzGFTdsn75gkRtDX1MepWtfm9TshCPQshzpH%2F%2BDBYnRlscvH7EHgVl6ZaZZqH9flfPzs3OmUJCxo4iJDAi6r%2BvaFLpUPugIzGyLfKHvQOzy%2Bsu5douhZbBtviS%2BZcy65jBIlOMGh1qz3vaAgQivo6psw1ZtkBWJOimAElfxevwL672cTZOqUuMRmt%2B1dg2HJb2IqxjzLddpSXAk9mZQBm4cvuu%2F9HH%2BoUojlcECkupogQBfY4rX%2BQ6x3nnLGaYxj%2FD2hLCf%2BGvsh2Fxk79xrsBQwztL%2B9wyj83IMmbMhJi3p921fl9r7JMfbjktJGOMKL41i%2Fy8x1hfDABUhb2DdANskKJcWcZ1gU5XIzMRPkIchPFEhq%2B9Upr37NceFgrL3awFBEJKD11t%2F0XV%2F2UnGvh6UL5g56kGYbjDqvi6ecSSOSiokvnysR3t56CUXY4dpt7eKGWLggFOr85NNlRHSkkjtihMJntg9QGOqUBw8653fCmCUEFzqJvfYDR1iaZ7OvIHwT5p0HhacAOE%2FgREe2CQJigSkicgcY6CZzxbPBxnBLI%2FL8pV8Tv1xo%2Fn4nYnk53mfDvqVZwm5%2BRMJ1xPp8Ya9VaNFGRLXp1M39EHXWWgYYUt6F4gRVfQdeP7hyW1XAeHI4MTQTxx4HQEaA%2F1mDD%2Fv7pCLjaDbgtZbJj1%2BPH4S4qC3lUXSGgNlsr72vg%2Bp4w&X-Amz-Signature=c3079a7da5385bd241786da8173520209428c6b6d31c848b363273dcc28d7609&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOIMZO4R%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T003354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEvuuDNrqkyLaN37Rz%2BOpqakLUNtP3gjTqSfb%2FM4uSauAiEAszM1TqdOlGPdjwlmK%2BEqBSHccoKF3LGoCpk57sCophcq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDDBxJfTJU4ugzgBeSyrcAz6npg%2FRGUBAWQ0Zwb9jf7b0HykmZ4znpfSB3hv8ElHtzg2Q1SVvUnpQxkaeRQOJD%2BycP7fCjlrdfuy%2BcmgOkiPZwuEMw3vx1nx1IGFs4bzh7Ct7zjwRI2s4nLc1UlY4FAsdWOrYAQpZf5%2Bp%2FDo54uJjGYLI5XBWTHtzGFTdsn75gkRtDX1MepWtfm9TshCPQshzpH%2F%2BDBYnRlscvH7EHgVl6ZaZZqH9flfPzs3OmUJCxo4iJDAi6r%2BvaFLpUPugIzGyLfKHvQOzy%2Bsu5douhZbBtviS%2BZcy65jBIlOMGh1qz3vaAgQivo6psw1ZtkBWJOimAElfxevwL672cTZOqUuMRmt%2B1dg2HJb2IqxjzLddpSXAk9mZQBm4cvuu%2F9HH%2BoUojlcECkupogQBfY4rX%2BQ6x3nnLGaYxj%2FD2hLCf%2BGvsh2Fxk79xrsBQwztL%2B9wyj83IMmbMhJi3p921fl9r7JMfbjktJGOMKL41i%2Fy8x1hfDABUhb2DdANskKJcWcZ1gU5XIzMRPkIchPFEhq%2B9Upr37NceFgrL3awFBEJKD11t%2F0XV%2F2UnGvh6UL5g56kGYbjDqvi6ecSSOSiokvnysR3t56CUXY4dpt7eKGWLggFOr85NNlRHSkkjtihMJntg9QGOqUBw8653fCmCUEFzqJvfYDR1iaZ7OvIHwT5p0HhacAOE%2FgREe2CQJigSkicgcY6CZzxbPBxnBLI%2FL8pV8Tv1xo%2Fn4nYnk53mfDvqVZwm5%2BRMJ1xPp8Ya9VaNFGRLXp1M39EHXWWgYYUt6F4gRVfQdeP7hyW1XAeHI4MTQTxx4HQEaA%2F1mDD%2Fv7pCLjaDbgtZbJj1%2BPH4S4qC3lUXSGgNlsr72vg%2Bp4w&X-Amz-Signature=9c739c78db58f6ae0dd85b13c989d1eac12f5f596f6d9a70ecbe5d7f2c86b644&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
