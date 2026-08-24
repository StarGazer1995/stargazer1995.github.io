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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4ZYXPF7%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T122751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIFXDFuPQxAgxexLiBKw5k2Es8H7fxXIOhUaBKheByRTTAiEAjnWY6GyX1h339ZNX4ffCQEDDTdwTKCvfuZFQBblb%2B6EqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt8ftB6wRkOgXl11CrcAy6knIG8jkJzfnnbCS%2Fo6l2so%2Fz1UY3aBJxm0nQkjHlFv7g6Bh0jBZ4slQrfxaAwR0vS5zM3lE3pNMD5Ha8yTrGP18ICjFKZBk%2FqOw%2BzWdFUZEVX53akFLnJsIBrSqGxyCVfIFmz0hTqVEtTidgjXc9%2F7LCRFBBZ3aoLpbW6VyrjaSm0XEIsT2ZGEWXAuPmITg4F4LBB2bHUVRl96KrMfaKNjO9hhV%2BG%2FMHut7C1fTf3pBBUu%2BkM28%2BFtmHKKYv2wfgxvd%2FmY6nctHNWOsQ4F6S66s4xYWoApDNvDmFOHyw9O%2B0DoJL7YZmqeoBTcG%2FEz3CA6lCEjNDKLAeOoV2nKlayx64JOwMvjt2zl2ABDJP%2FiZT88%2BrDZJTXJ9pRBw0a7d5tmyNugEingqw5%2B9X6Mm5f6e9dsi%2BFAU9NOQeEZoIFr5HozaHsxsLs82ryVZWWkrNsH75GmO6zxI3VBu32uELN5uoDlEjbaXScsFex4y3FFMktMnY9kdOnFqx%2BW6LAJ4R%2F8OF90FuaUsjoPH1ngGk8Ojjx4SNRABNJHzquTiL9kIFrv2XYqOxrNSjnaB85pJ8tBXPasRP2VDofV93kJLd%2FXRz0hHLjD3g8k%2B66omPkCXMCTHPbigVtIwV6MPTssNQGOqUB28rikXAVCRXFb%2F8Kgr2RVt0942afqUcn0XgNuMdrbxdwBN66H0vzy7GjdWyOYYIWCUQJXi8Uv57P7jVOlU33KUkfdUp2rRoQt9ecIDGYXUl5afh19vWSQ0od4H%2Bd%2FE%2Bo8eGRbqE7OFizf4BCF6B8p6xR65%2FAWAkdw9Y9oRc31IR874YOaNsqx9tUboVV3QhL%2BJM1u%2FIkyUfSpLHGhIai3Fd%2BIF%2Fv&X-Amz-Signature=9ab7d999c5d0d592cc9ae5fb2109fe29fef06dd2cc5bb05b09366b747eb9379c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4ZYXPF7%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T122751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIFXDFuPQxAgxexLiBKw5k2Es8H7fxXIOhUaBKheByRTTAiEAjnWY6GyX1h339ZNX4ffCQEDDTdwTKCvfuZFQBblb%2B6EqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHt8ftB6wRkOgXl11CrcAy6knIG8jkJzfnnbCS%2Fo6l2so%2Fz1UY3aBJxm0nQkjHlFv7g6Bh0jBZ4slQrfxaAwR0vS5zM3lE3pNMD5Ha8yTrGP18ICjFKZBk%2FqOw%2BzWdFUZEVX53akFLnJsIBrSqGxyCVfIFmz0hTqVEtTidgjXc9%2F7LCRFBBZ3aoLpbW6VyrjaSm0XEIsT2ZGEWXAuPmITg4F4LBB2bHUVRl96KrMfaKNjO9hhV%2BG%2FMHut7C1fTf3pBBUu%2BkM28%2BFtmHKKYv2wfgxvd%2FmY6nctHNWOsQ4F6S66s4xYWoApDNvDmFOHyw9O%2B0DoJL7YZmqeoBTcG%2FEz3CA6lCEjNDKLAeOoV2nKlayx64JOwMvjt2zl2ABDJP%2FiZT88%2BrDZJTXJ9pRBw0a7d5tmyNugEingqw5%2B9X6Mm5f6e9dsi%2BFAU9NOQeEZoIFr5HozaHsxsLs82ryVZWWkrNsH75GmO6zxI3VBu32uELN5uoDlEjbaXScsFex4y3FFMktMnY9kdOnFqx%2BW6LAJ4R%2F8OF90FuaUsjoPH1ngGk8Ojjx4SNRABNJHzquTiL9kIFrv2XYqOxrNSjnaB85pJ8tBXPasRP2VDofV93kJLd%2FXRz0hHLjD3g8k%2B66omPkCXMCTHPbigVtIwV6MPTssNQGOqUB28rikXAVCRXFb%2F8Kgr2RVt0942afqUcn0XgNuMdrbxdwBN66H0vzy7GjdWyOYYIWCUQJXi8Uv57P7jVOlU33KUkfdUp2rRoQt9ecIDGYXUl5afh19vWSQ0od4H%2Bd%2FE%2Bo8eGRbqE7OFizf4BCF6B8p6xR65%2FAWAkdw9Y9oRc31IR874YOaNsqx9tUboVV3QhL%2BJM1u%2FIkyUfSpLHGhIai3Fd%2BIF%2Fv&X-Amz-Signature=4e33165d77abe2caf9794a79b6fa69ac62a5118e1ce899b22d397759df5d025c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
