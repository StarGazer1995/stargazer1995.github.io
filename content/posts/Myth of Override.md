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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZ4EFLLY%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDj%2FMLYfr4JjcVFN8TZFyQVMn31S6534BKW%2BMSp1Z6AuAiAoB8FvLjD%2BqPwcUMzpwfPPqKJXKx5b7d%2B5hve%2FpIsriSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMcY5FYDwby%2BDE7HSyKtwDc1WRxE984qJBtIq9l%2BQ0mnMVFhtq%2Be%2Fu0sqRp%2FV3aY8cyhj9%2FWb1Jc6Hm9jzF0Kub6LbiMeXEkAHCxIC2DA1e9QqUkn5T2AmTRm6ZVsKQSYIVRki%2BraNme9OWwo6bBdeAns4doZo74YNHWNsDN%2FrAyA7ZXLdJNXZ4e2E166lUNtz01MIt7xI6IS4t0TvRoBa1Sk5Eh3wAdv%2F23E%2BtslRXD2McDzgLvcJTXwSalGmsP4NsBe1vWTefWuwQxo%2BtB8KCFUPxvj9bcAPX5urWpK3lbz6pweUd7C3bwDISyj0gC16Suc5UPwMShJY%2BYxpR45N8ABQvAOWsxMLrNWJA0fvWRGjpCfE8Kl7eJKj%2BT3o%2BGT9lSLbFo7sW5HP8c%2F8O1GH7VbKr7dxm6K274h19%2BI0d00zOzZC0Mkk3b1PhjSL0LEE83Cz9cl6eV1tZbDVChhkaSSXTabJSPmVdklbxYQYeYYQQw%2F%2FP1aQ4avnPUeYWMT%2Fu0Alwm2dhBNFXHkhScuyTCfIm9VMTbnDvNXnL2q4MoGiq2%2BLwB5TJVEoMvjuIrdVL4pM%2BKMZsTonlIQLBTqrGUqq9UlzKiu%2Bssy3FHsw0SElj1wfzuu30EIGR0oRHMxw8J0c9XEzGaiznFIwgvbj0QY6pgF2GyRlBiQTKNJT1NFNOPb7PiodAqEvcOrL2QyDYw%2FxnHcSR%2BO52Tm%2F%2FUcI0vakRtCKb59HJ0M1%2BQxTbwtEaKkCUjQ1kS%2Fi60h9isIXQAfYfZ27iQ3l9PH2MbMpqXiJuB3SQ%2FLr%2BNOn6nfGBJpPBRrTJoEgjQcQeRLlr00sukHOVVkO7s2wBmQLXHugUYP%2FlBT5VaWOJVBrtXRIZPvZb7fu8cDUG47o&X-Amz-Signature=65a719a8f8439862d9dae01d74ceb805a82f647eab3f8a588656d17ec85aba5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZ4EFLLY%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T093755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIDj%2FMLYfr4JjcVFN8TZFyQVMn31S6534BKW%2BMSp1Z6AuAiAoB8FvLjD%2BqPwcUMzpwfPPqKJXKx5b7d%2B5hve%2FpIsriSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMcY5FYDwby%2BDE7HSyKtwDc1WRxE984qJBtIq9l%2BQ0mnMVFhtq%2Be%2Fu0sqRp%2FV3aY8cyhj9%2FWb1Jc6Hm9jzF0Kub6LbiMeXEkAHCxIC2DA1e9QqUkn5T2AmTRm6ZVsKQSYIVRki%2BraNme9OWwo6bBdeAns4doZo74YNHWNsDN%2FrAyA7ZXLdJNXZ4e2E166lUNtz01MIt7xI6IS4t0TvRoBa1Sk5Eh3wAdv%2F23E%2BtslRXD2McDzgLvcJTXwSalGmsP4NsBe1vWTefWuwQxo%2BtB8KCFUPxvj9bcAPX5urWpK3lbz6pweUd7C3bwDISyj0gC16Suc5UPwMShJY%2BYxpR45N8ABQvAOWsxMLrNWJA0fvWRGjpCfE8Kl7eJKj%2BT3o%2BGT9lSLbFo7sW5HP8c%2F8O1GH7VbKr7dxm6K274h19%2BI0d00zOzZC0Mkk3b1PhjSL0LEE83Cz9cl6eV1tZbDVChhkaSSXTabJSPmVdklbxYQYeYYQQw%2F%2FP1aQ4avnPUeYWMT%2Fu0Alwm2dhBNFXHkhScuyTCfIm9VMTbnDvNXnL2q4MoGiq2%2BLwB5TJVEoMvjuIrdVL4pM%2BKMZsTonlIQLBTqrGUqq9UlzKiu%2Bssy3FHsw0SElj1wfzuu30EIGR0oRHMxw8J0c9XEzGaiznFIwgvbj0QY6pgF2GyRlBiQTKNJT1NFNOPb7PiodAqEvcOrL2QyDYw%2FxnHcSR%2BO52Tm%2F%2FUcI0vakRtCKb59HJ0M1%2BQxTbwtEaKkCUjQ1kS%2Fi60h9isIXQAfYfZ27iQ3l9PH2MbMpqXiJuB3SQ%2FLr%2BNOn6nfGBJpPBRrTJoEgjQcQeRLlr00sukHOVVkO7s2wBmQLXHugUYP%2FlBT5VaWOJVBrtXRIZPvZb7fu8cDUG47o&X-Amz-Signature=6a86b854cfb848d0d9bd51ab087eea9cf8a679ae26e4c144ddf171f8225eba68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
