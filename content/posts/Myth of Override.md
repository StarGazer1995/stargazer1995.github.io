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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5HMGT4I%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T102316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDJ5iPaWpnJsaNJyEFveWMOYwLSUV%2BT8DWS9aE2ucFUQQIgTAJ9H1Wtm%2F1Y8r7yqcbS7fs4V%2Fr2IzozYh221D3vecoq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLGrKeRy9qMqgSHnYCrcAyBkJqaeFpdHi%2BccEtnBxxgPx1XJSnYG1x831KLHy1h6YxD0%2FDGlzydULZCPt7wMnanXJcLFroOyVeeqzY1%2B%2FBiAxOhKLadCRAPCMbXluBP1YOP1zC4OzQRr5ET%2BenkCQ89z1JImsQmhjTxX3Ynij0RYlf8AR%2B6aJWBeE1ujyAQCuyEX6tQqD%2B%2FXksZIHuMGUZOnzETX3T9gBaOd08HD9QkZ08aEhtUKOJYHjncN6xHGpnBp2Cb7MoX0QhVAvTc7P5CNz7PE28mPW%2FeuwTUxuQm%2Bw0lquR7DfuxhxgV3Js1u9AC3hgZKGK8siHIuUcSUFlRuwtIcGYEwZCSC7BkxGyhhrjs1gRkMzecX1H0ljrCUlpKfkvd7wc5SrzRDeppTyHEzmtLI%2FhUdyLXDc8s77gjdTeRqkOgKYcEnVuKb%2FaKEx6j7gA4zYKymaF1Qe065jkTIfMsNax553eI9ViR3k1sMYBtB259%2FHElegumpGw0mrGj7igHwbPdRKus9NmSH0zYObLuZc0a%2BiLjP2Hp8yrU5BkXxX0p8oxrDZEObxWvDnEiwp7i3Frw8wL%2FLXiQkkcH95rYnSNSD%2BaVpSWCdZwQ4S9w3bDsnfFTxO3s2d97Z%2B8sIPTYOit72sdgPMKa5utQGOqUBVtYWLWIyzpqXRSHB4wdMwpBrTKNZtSFE3%2F6cQh3ADgO5kXt%2FtWTIXNROok6GNDPsOIlTFnIvNXlAs1UxqpbQKje5NGUgwR5OtMq5%2Bm%2BitA8L5ONOqtsjz9mqtGTCr%2BxUUFo3c0sbyfWYXx8joXnxthdg2VRE0P6cZZA4Xsai4G5rcVQF8ZSC23EbrhtQoCIkxG9jb95avuBiz5NUcYxhn2CIRsyW&X-Amz-Signature=6b9a2e7002f959c64ad0468a6bc05b3010738b64e8229f75c910915cf9aa1b0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5HMGT4I%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T102316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDJ5iPaWpnJsaNJyEFveWMOYwLSUV%2BT8DWS9aE2ucFUQQIgTAJ9H1Wtm%2F1Y8r7yqcbS7fs4V%2Fr2IzozYh221D3vecoq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLGrKeRy9qMqgSHnYCrcAyBkJqaeFpdHi%2BccEtnBxxgPx1XJSnYG1x831KLHy1h6YxD0%2FDGlzydULZCPt7wMnanXJcLFroOyVeeqzY1%2B%2FBiAxOhKLadCRAPCMbXluBP1YOP1zC4OzQRr5ET%2BenkCQ89z1JImsQmhjTxX3Ynij0RYlf8AR%2B6aJWBeE1ujyAQCuyEX6tQqD%2B%2FXksZIHuMGUZOnzETX3T9gBaOd08HD9QkZ08aEhtUKOJYHjncN6xHGpnBp2Cb7MoX0QhVAvTc7P5CNz7PE28mPW%2FeuwTUxuQm%2Bw0lquR7DfuxhxgV3Js1u9AC3hgZKGK8siHIuUcSUFlRuwtIcGYEwZCSC7BkxGyhhrjs1gRkMzecX1H0ljrCUlpKfkvd7wc5SrzRDeppTyHEzmtLI%2FhUdyLXDc8s77gjdTeRqkOgKYcEnVuKb%2FaKEx6j7gA4zYKymaF1Qe065jkTIfMsNax553eI9ViR3k1sMYBtB259%2FHElegumpGw0mrGj7igHwbPdRKus9NmSH0zYObLuZc0a%2BiLjP2Hp8yrU5BkXxX0p8oxrDZEObxWvDnEiwp7i3Frw8wL%2FLXiQkkcH95rYnSNSD%2BaVpSWCdZwQ4S9w3bDsnfFTxO3s2d97Z%2B8sIPTYOit72sdgPMKa5utQGOqUBVtYWLWIyzpqXRSHB4wdMwpBrTKNZtSFE3%2F6cQh3ADgO5kXt%2FtWTIXNROok6GNDPsOIlTFnIvNXlAs1UxqpbQKje5NGUgwR5OtMq5%2Bm%2BitA8L5ONOqtsjz9mqtGTCr%2BxUUFo3c0sbyfWYXx8joXnxthdg2VRE0P6cZZA4Xsai4G5rcVQF8ZSC23EbrhtQoCIkxG9jb95avuBiz5NUcYxhn2CIRsyW&X-Amz-Signature=84dcd8617225868d198391ece972f19b44eca8baf35ea35bc88da0fba86d720a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
