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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D7CDONF%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T224637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDh7H7%2BS3S4kyuk4%2BreDQLX6CKoF66%2Fb8FR8xsbl%2BRxBAiEA%2BlHXnFyIbUHDYwvMqosv56s5rmMTwDuk%2BFGB0RwC1sYq%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDKN6zqBs1xTx9j%2FqxSrcA8AgooaTXPdVo%2BVU4PiOoIWpssWi%2BP7NuXXXaeEcTlEl86IVOu%2B7Qx0WKuGez3tq4Xw3wsqH0boUROA8snu7L1NHC6dA8HF92iPP3vdlWiyEDwQUm4fiGcEdSkrbKjoroED7tJzHQk%2FxLszcBULxGl%2FMTdCCpwD6WmdYo9qKOJVDFL60xPDDKbLi5ho0raIB%2BF4r5b8gq2Oi79PXGLtYYNfyjmLUNB9KC%2FmlCMyIKXuIIJTvdHJXlcpw6xD62CHPf%2BDiesh2vzunF0Yc%2FUI2UvAh8Ni0%2BDWNE74IOuEY7h39nAU3JKNlMZ0F4vGSdLpFpxS5jDZiWGFiLRncjs3VJxhMvCFrNZZSsEaVP5F%2B1TQfSVmdvgQ%2B4xXBjOmPmY%2FvcDCidU1k9LvGWV4dd%2Futr2LMy2LgaOgwKrtDWAzfz7BnAyqSbwn%2BF9bP1qds7OO7WCBKHSggwbESyAmRcGlw3WT5TbpVE9YraiZMIKR2yD%2BjoUBOa0IkodoMopPW%2BYKTUu%2Fqmc%2FH9%2F7%2Base%2BnDc78evXTZoXJR3%2BT5eKwFdO0fL2Df4lVouRhq%2Bz4rtJNKCY7JEX2IxgAeJ53KrHObtY3g9CXhUfRUXM7W2PEUpPUzJGredCTWK%2BnQEv8OfKMO6J5dIGOqUBqnArpYy%2FsugghL0SVN4MGQ%2BqtIWaYs%2B66AZqOupC6R86QXquYgZBp%2F5TCFrxc1o76LMMY%2BC02DX8XokMc8yird0FIu4h0aiNSpQ41ZR244igq5O5wGC3l%2FbZag8rGc7KAZ8gy4F5zff4OiNg4AQC2a9ITNBW9iVUhnEc651%2FQr3ADBOftcksRSzYFjnUJcbHc5uueD71YHE%2BcygRpvMXiyPnnHys&X-Amz-Signature=b1c0442dbb5ab390184aee720fe2a23723b7714866009a65ec5cdf6123164190&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D7CDONF%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T224637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDh7H7%2BS3S4kyuk4%2BreDQLX6CKoF66%2Fb8FR8xsbl%2BRxBAiEA%2BlHXnFyIbUHDYwvMqosv56s5rmMTwDuk%2BFGB0RwC1sYq%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDKN6zqBs1xTx9j%2FqxSrcA8AgooaTXPdVo%2BVU4PiOoIWpssWi%2BP7NuXXXaeEcTlEl86IVOu%2B7Qx0WKuGez3tq4Xw3wsqH0boUROA8snu7L1NHC6dA8HF92iPP3vdlWiyEDwQUm4fiGcEdSkrbKjoroED7tJzHQk%2FxLszcBULxGl%2FMTdCCpwD6WmdYo9qKOJVDFL60xPDDKbLi5ho0raIB%2BF4r5b8gq2Oi79PXGLtYYNfyjmLUNB9KC%2FmlCMyIKXuIIJTvdHJXlcpw6xD62CHPf%2BDiesh2vzunF0Yc%2FUI2UvAh8Ni0%2BDWNE74IOuEY7h39nAU3JKNlMZ0F4vGSdLpFpxS5jDZiWGFiLRncjs3VJxhMvCFrNZZSsEaVP5F%2B1TQfSVmdvgQ%2B4xXBjOmPmY%2FvcDCidU1k9LvGWV4dd%2Futr2LMy2LgaOgwKrtDWAzfz7BnAyqSbwn%2BF9bP1qds7OO7WCBKHSggwbESyAmRcGlw3WT5TbpVE9YraiZMIKR2yD%2BjoUBOa0IkodoMopPW%2BYKTUu%2Fqmc%2FH9%2F7%2Base%2BnDc78evXTZoXJR3%2BT5eKwFdO0fL2Df4lVouRhq%2Bz4rtJNKCY7JEX2IxgAeJ53KrHObtY3g9CXhUfRUXM7W2PEUpPUzJGredCTWK%2BnQEv8OfKMO6J5dIGOqUBqnArpYy%2FsugghL0SVN4MGQ%2BqtIWaYs%2B66AZqOupC6R86QXquYgZBp%2F5TCFrxc1o76LMMY%2BC02DX8XokMc8yird0FIu4h0aiNSpQ41ZR244igq5O5wGC3l%2FbZag8rGc7KAZ8gy4F5zff4OiNg4AQC2a9ITNBW9iVUhnEc651%2FQr3ADBOftcksRSzYFjnUJcbHc5uueD71YHE%2BcygRpvMXiyPnnHys&X-Amz-Signature=5910a5e1c4307f5ce8efa5e165b5fecc4bd1402bbfe33cec5268c9237d51b7da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
