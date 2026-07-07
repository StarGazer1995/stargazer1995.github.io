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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663N7RLDES%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T161634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExfb%2Fqn2Yk09d4cdkdV%2FSj%2FAFcTFcEFsqFG3fJ4l0UGAiA1lIyOXlcsps91%2BIAkcl9inhvhmmk7b99NqEQh3ihogir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMjYdycUeauXe0eZ5FKtwDW0FV9k%2FyjQbtvvSVc4fhoJPRyi7d2lkQoh4hLisw%2BMlSl8Che5RQ2Joe8z3NNqXw3zz3gBtHjpEqsuvOQvLx31Bhwg2gRVeFiZNSYTcJDMblnpHJNgZZQRgAS5LSawDwnVPQ7wAuPkh2IIRXmnQqVAiE6uaf8uMdLpgp9UEp%2BHrEyhcrSP0%2FJAqI%2FFVv2fHKNBnC5Ppcv5zy%2BkPkpbnYoi0fA3OApcbth%2FwtPVOY2KtwVJyTg%2BhwF0VPdJovIivwpDntWu73e7q1DBRhhoGHJgt9xIxypX%2FWmyDnMto0pMutqqR1BArOKCTn7tZsPtAB5LisOOm%2Bt6K3%2F6UAmkVyjMDvCU3jhc%2Fvst8aqhkUbjjAC2NjqmMM%2BN3h3Znc1b3C0C06g9vpTnXV8UrfMZqyWB8xkpsnrKqr%2BHW7L3%2FIw0h9WbmT7lF2g6zM7Gn5JlZ6gSJemh2IRKzm%2BgHeqsE%2FNEAKBHAHupo46ZHrtSWEG3j0Uh8trrzdOC4KtzVN9SLHHEiouQu9GeXaH1%2BExzSImo%2FvpK9FBSRTojM10a1GBd4abP3ZtZzy21WQjw1U2VEXiv%2FjMyVY1uytBLn4yoyKf%2F45gc9%2FOFM%2FK1nIzmgFLRKymEKRogN3vhqAa6Iw%2BbO00gY6pgEtWRGYFOmJtMs%2FvvCbiIhbgfbzQk%2ByKCXI9g3yYR77dIKS0tdRTaupQMpn2P%2BFYibLwCMdSar2FUMfHH6rLf71pGdpMxDlAE2aSlIzsRIzBpMw2HLB8gLIPNST3kR%2FW9ee2hDUQCUY%2B4D%2FZ33KDNHiSEaeuV3r0jhtFZ5GDgVRNV047iJfs1Yb7KDCJx1MheJEXI2NeVicdWx7uMHs1f95%2Ft%2Fxvtqx&X-Amz-Signature=6ad810cbec38f57af53b3c7c2b6094e7d41c55bd84d82bb3af403fed05731a52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663N7RLDES%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T161634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExfb%2Fqn2Yk09d4cdkdV%2FSj%2FAFcTFcEFsqFG3fJ4l0UGAiA1lIyOXlcsps91%2BIAkcl9inhvhmmk7b99NqEQh3ihogir%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMjYdycUeauXe0eZ5FKtwDW0FV9k%2FyjQbtvvSVc4fhoJPRyi7d2lkQoh4hLisw%2BMlSl8Che5RQ2Joe8z3NNqXw3zz3gBtHjpEqsuvOQvLx31Bhwg2gRVeFiZNSYTcJDMblnpHJNgZZQRgAS5LSawDwnVPQ7wAuPkh2IIRXmnQqVAiE6uaf8uMdLpgp9UEp%2BHrEyhcrSP0%2FJAqI%2FFVv2fHKNBnC5Ppcv5zy%2BkPkpbnYoi0fA3OApcbth%2FwtPVOY2KtwVJyTg%2BhwF0VPdJovIivwpDntWu73e7q1DBRhhoGHJgt9xIxypX%2FWmyDnMto0pMutqqR1BArOKCTn7tZsPtAB5LisOOm%2Bt6K3%2F6UAmkVyjMDvCU3jhc%2Fvst8aqhkUbjjAC2NjqmMM%2BN3h3Znc1b3C0C06g9vpTnXV8UrfMZqyWB8xkpsnrKqr%2BHW7L3%2FIw0h9WbmT7lF2g6zM7Gn5JlZ6gSJemh2IRKzm%2BgHeqsE%2FNEAKBHAHupo46ZHrtSWEG3j0Uh8trrzdOC4KtzVN9SLHHEiouQu9GeXaH1%2BExzSImo%2FvpK9FBSRTojM10a1GBd4abP3ZtZzy21WQjw1U2VEXiv%2FjMyVY1uytBLn4yoyKf%2F45gc9%2FOFM%2FK1nIzmgFLRKymEKRogN3vhqAa6Iw%2BbO00gY6pgEtWRGYFOmJtMs%2FvvCbiIhbgfbzQk%2ByKCXI9g3yYR77dIKS0tdRTaupQMpn2P%2BFYibLwCMdSar2FUMfHH6rLf71pGdpMxDlAE2aSlIzsRIzBpMw2HLB8gLIPNST3kR%2FW9ee2hDUQCUY%2B4D%2FZ33KDNHiSEaeuV3r0jhtFZ5GDgVRNV047iJfs1Yb7KDCJx1MheJEXI2NeVicdWx7uMHs1f95%2Ft%2Fxvtqx&X-Amz-Signature=6e11a255e02628798f495a3e20c393e44a8561eaa49537a07ec5d702662b3019&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
