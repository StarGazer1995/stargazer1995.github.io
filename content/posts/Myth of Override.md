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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WFGCSHC%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T220256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYJUhut0uGQ4yF%2Fc3iCfrhKtIwJ%2FJpyrKYRulWvC5g%2BAIgV1nUzPTzhYFh2CvvytlngpqiN0SrX5n8B4B9INw6A8IqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCZQZ86jReTOwOyyircA8q0C60E8yDFm1Ij3AskFPWBvbJGwUmUgfga5YqBZdNB3HGMggcA%2FhYwP9OXTzmYO8cA%2FBekPIogAz7Gx2mZmsTEGkgbhLC6D4plv0bXr9X5F09CbuH28k%2FwwbCHad9DUq4fKK%2FZcrmuF8KEH9DWvgJOq0NBXQI6k%2BlmCnfbjohUrjhiSKou7hdTX9T0QpY%2BcpCqDznAMC1KYXQgkE%2Bgg5XZxV41xCOIja4kel%2B7dpVShBAX6FexmlpkU8P%2FTkSL5WcYVNeMqSAGUKL5pBFjFdG4JYpfMNm3CRTGyM1bsrtkXE31OmBsFYjiwN4sNnnqfJepPM6lPPku%2FTVSr2aTNd5iuodBgZxEx96X86RVgq6E5w2FUCR4dahmMUmm%2FxbBn%2FTQHihdEWsWg3Y0wJ9n8MB837X%2B54txX9253EMByTHnr0bY%2Fxw8YMc560wsWdtrkSVywxxK%2Fibk5RgqlCbIoBC2qFdMeT3x0EMUigQESkhm%2FR9rVC8x8Q4Ra8%2FIgs%2F%2F%2BraX6M6k1Lonvq4GadrQXKaVgn6VL%2FXdWirMh2WcyhoDsKQ7aTfAEXwGu84ZUfhyleZ5jAROCd2j%2BMPtIC%2FVqqyvIYwm3RxQdlrUgHYn8hLSU6WBkXQnGwBMAZq2MMGXutYGOqUBZMzb%2FL3tHfqEZrpSl%2F1o56%2FXZCCrpaGnisuLaZWfsTlkTDjN4lSPHSZBMLOt6z%2Ft77RCxxflxrNgsfGm4ZuzMNFKhuwE3q%2BCUJkEkWIWSrXNmMZAtcdWYsH5aheJU3%2FJjBZDSfwa5tNcjGepJCoh17Oa1%2FN9LfqtIkguxS0sJHv8N0qEggqHudY83p9ybB6dXml2kjB3MzTau5SNkoC43k3gOrKS&X-Amz-Signature=b2578ea97305ae2645ee70d7c3f9a58d03e248d23856566b6605c2621565f973&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WFGCSHC%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T220256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYJUhut0uGQ4yF%2Fc3iCfrhKtIwJ%2FJpyrKYRulWvC5g%2BAIgV1nUzPTzhYFh2CvvytlngpqiN0SrX5n8B4B9INw6A8IqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCZQZ86jReTOwOyyircA8q0C60E8yDFm1Ij3AskFPWBvbJGwUmUgfga5YqBZdNB3HGMggcA%2FhYwP9OXTzmYO8cA%2FBekPIogAz7Gx2mZmsTEGkgbhLC6D4plv0bXr9X5F09CbuH28k%2FwwbCHad9DUq4fKK%2FZcrmuF8KEH9DWvgJOq0NBXQI6k%2BlmCnfbjohUrjhiSKou7hdTX9T0QpY%2BcpCqDznAMC1KYXQgkE%2Bgg5XZxV41xCOIja4kel%2B7dpVShBAX6FexmlpkU8P%2FTkSL5WcYVNeMqSAGUKL5pBFjFdG4JYpfMNm3CRTGyM1bsrtkXE31OmBsFYjiwN4sNnnqfJepPM6lPPku%2FTVSr2aTNd5iuodBgZxEx96X86RVgq6E5w2FUCR4dahmMUmm%2FxbBn%2FTQHihdEWsWg3Y0wJ9n8MB837X%2B54txX9253EMByTHnr0bY%2Fxw8YMc560wsWdtrkSVywxxK%2Fibk5RgqlCbIoBC2qFdMeT3x0EMUigQESkhm%2FR9rVC8x8Q4Ra8%2FIgs%2F%2F%2BraX6M6k1Lonvq4GadrQXKaVgn6VL%2FXdWirMh2WcyhoDsKQ7aTfAEXwGu84ZUfhyleZ5jAROCd2j%2BMPtIC%2FVqqyvIYwm3RxQdlrUgHYn8hLSU6WBkXQnGwBMAZq2MMGXutYGOqUBZMzb%2FL3tHfqEZrpSl%2F1o56%2FXZCCrpaGnisuLaZWfsTlkTDjN4lSPHSZBMLOt6z%2Ft77RCxxflxrNgsfGm4ZuzMNFKhuwE3q%2BCUJkEkWIWSrXNmMZAtcdWYsH5aheJU3%2FJjBZDSfwa5tNcjGepJCoh17Oa1%2FN9LfqtIkguxS0sJHv8N0qEggqHudY83p9ybB6dXml2kjB3MzTau5SNkoC43k3gOrKS&X-Amz-Signature=c46c9c5b14808462ff0587e6be39015787c833f03be90b95868800237930299c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
