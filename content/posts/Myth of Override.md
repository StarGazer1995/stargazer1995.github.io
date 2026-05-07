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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466533YMHL7%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T192426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXyEBP%2Bhq0nxZSSvMSMqTBNHHmaFTo3RcSSCwUuWnB4gIgeL%2Bty1aMHqGZjyfumhF3vb2cBg8TrTbdo96hxs4n1s4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOL%2BObTVe6cgVHiiFCrcAy3aUasSXFb%2B%2BBb%2FzuoQHTKEIs2h5d%2F4obGeu%2FBC3Oyas0VE4gCkty6WT%2Bjrw7%2B9wK9rpX2g%2Bj2Jw2pRLtCYLkr5ld9TRt1OQd0DQK2%2BD85SE1ggU2V8QqVGoHv%2BQb4dTIsZH0nPdMX1eHOJhqctTW9QgZFpymQ%2FjMdGAn20Q0sjjqwwy%2Bqv%2BcFVSU0PCsuFb5SgxDK8M09FxKHin%2FeDCLnEBfl2JLF3PRlGI52P%2FG%2FadbnCu7KEap6ujQgK%2B3Cyqd99V57Ldb9N2GAT6V07A%2BHRE6azRU9GaorC8sunCoFp3oleP5Qciq1qcO8sTykKxr19uYIuP5i7zD6ozDY1Zy1doE7zxl7j6shlCrQgwzqjc71DHPRdG0%2FYnCZHpJK5ZBG4YJ38ygzzogDruxf8CSAjtsXX6mWCu5DWDvq9pzvOPyDppKTLSPnAL5rZiAHzcki9%2FIwx5MHqYdPwgub%2FRtZS3m47fIidjHPrup%2BbP6OU9QtEYCCEhiqXyYNx6uKb1KKgU5CsSpad8%2FDPnZnOVVyq0nHon084rR0IYXIdFTkrE%2FmyYQrNu2sOqabXDJ1HNfQB1m%2FWCWfVsZ%2FH93%2FatkmXK%2FBHhDmrhL2xMvKVuNWETjLjq1X1QGqorNxQMOGs888GOqUBMDpTAhNfcqPcknLgHUhBCatfbii80Ir0XsgA407LO7F6G%2F2UMAaFpemnD2w7e90LNCFy%2FfUu2%2FsoaUhR2lDmmVtcRryvuWoLzgZFTIgEMVzc050ShOb7FSsdvzcLpl2jFWxiONRY67wdwYSMh03ikyc5gSUgVrEKab4t%2BHy3YXGK4rJ8LtSdzNZJsGnK9AXVL6ehXBpx3B68ix78xvxrTry3MERp&X-Amz-Signature=5d38af8ad48f9079ccea6bbd3f312c9694e1a7612c64177f3bd35e249b3c69b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466533YMHL7%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T192426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXyEBP%2Bhq0nxZSSvMSMqTBNHHmaFTo3RcSSCwUuWnB4gIgeL%2Bty1aMHqGZjyfumhF3vb2cBg8TrTbdo96hxs4n1s4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOL%2BObTVe6cgVHiiFCrcAy3aUasSXFb%2B%2BBb%2FzuoQHTKEIs2h5d%2F4obGeu%2FBC3Oyas0VE4gCkty6WT%2Bjrw7%2B9wK9rpX2g%2Bj2Jw2pRLtCYLkr5ld9TRt1OQd0DQK2%2BD85SE1ggU2V8QqVGoHv%2BQb4dTIsZH0nPdMX1eHOJhqctTW9QgZFpymQ%2FjMdGAn20Q0sjjqwwy%2Bqv%2BcFVSU0PCsuFb5SgxDK8M09FxKHin%2FeDCLnEBfl2JLF3PRlGI52P%2FG%2FadbnCu7KEap6ujQgK%2B3Cyqd99V57Ldb9N2GAT6V07A%2BHRE6azRU9GaorC8sunCoFp3oleP5Qciq1qcO8sTykKxr19uYIuP5i7zD6ozDY1Zy1doE7zxl7j6shlCrQgwzqjc71DHPRdG0%2FYnCZHpJK5ZBG4YJ38ygzzogDruxf8CSAjtsXX6mWCu5DWDvq9pzvOPyDppKTLSPnAL5rZiAHzcki9%2FIwx5MHqYdPwgub%2FRtZS3m47fIidjHPrup%2BbP6OU9QtEYCCEhiqXyYNx6uKb1KKgU5CsSpad8%2FDPnZnOVVyq0nHon084rR0IYXIdFTkrE%2FmyYQrNu2sOqabXDJ1HNfQB1m%2FWCWfVsZ%2FH93%2FatkmXK%2FBHhDmrhL2xMvKVuNWETjLjq1X1QGqorNxQMOGs888GOqUBMDpTAhNfcqPcknLgHUhBCatfbii80Ir0XsgA407LO7F6G%2F2UMAaFpemnD2w7e90LNCFy%2FfUu2%2FsoaUhR2lDmmVtcRryvuWoLzgZFTIgEMVzc050ShOb7FSsdvzcLpl2jFWxiONRY67wdwYSMh03ikyc5gSUgVrEKab4t%2BHy3YXGK4rJ8LtSdzNZJsGnK9AXVL6ehXBpx3B68ix78xvxrTry3MERp&X-Amz-Signature=77ec92379634a0be7aa6f09f2a304eb093380b9cfb4e21f06b0ddbe276d348c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
