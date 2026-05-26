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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWK7HSGM%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T143526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHP5nkb47iJGRfycCOzsHcbwXOr2rAHu9tPvBgpzZUbWAiADNFcWT5%2Ff%2BgV%2BzPEQ9Q8druVXoC5LW6mr%2Bk1gdKOobCr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEA86ewZ9xd9sNPgnKtwDUrcsmEn8jw%2B9r%2For2yj6zITpNLNuF1lj4vrzHJzEASU08wt1M6etWs9inG3dg7WJFDp9NKBZ1L0Md7DBGrBMTIfD4vdO9OPiW1t57h%2BKW6k4%2B7v5lFH5Hq1S3VHeLrcpheUeR9SOW7WuISMpk%2BK8%2BnsIDTtq0ZOG%2Fomk95of494XWuhtIh2uRzAVLZVNWud2BbEIzovn0e5m9Sj1cx22Sbj8sNbD%2BvBDxfU80pPfTug0ldeEJNC01ICQOCKkFT7k0CUcsNv2wgoaCy4OsTJqmJFn13iH00RlwLHxFncIiBWUhxLdcyo1FD6lmGn1o8loZFUMtVyyqyC6Gya2J%2B3GHf3TplKzhCiva%2BISTpRDPB%2B%2BOzz1S3SvNw%2FBmXLZ97JhRy%2B03yEic0oralYzV6gAyJIpqqcStCHDCm0SvGo%2BtpjlwLyCyji%2Bh1klVSZ8KcVPbUV4l6nR%2B4YE3XKTpKAHCOf1SRShxZPJAsgDgs56E%2FwNwboOA3MezFFfNtGU2LZ%2F%2FPWVJSq6SrdsAVMDCVPMacLZaqVeVAiDlX8EGhZAxr9lPDpq8LDVsoIPWJ5gwdJRpehAR%2BTDgbfgo9QvcxwO4W0YWcdML%2BDzoYmzjK50SV7yp4bXL6mPwa%2FPKQ0w49fV0AY6pgELjKF1ea3Tck9dsMmIjwDwnex3XbKzNvspiTfZqEYWws2KGW%2BYn7%2FBoYZA3FeswoPCvoKb%2BlpBAjMnIqc6wh2BG7oPuaM8maSYZQvnh0F%2FCjwHBVYaAhCrkU4tkahPldT4ckPn9xThQTHIKgDA8bTKQ0VOMYqnBd%2F4Poyxu0Cs03HwD44f2wEWjpwgU1QtX3Mrkz9QtGpMWS3ONOe6Ma2wimngvcTt&X-Amz-Signature=893fbb0cd446c9f1c59cf870d5935543f5411163a03a617ebc239a521c7bdf0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWK7HSGM%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T143526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHP5nkb47iJGRfycCOzsHcbwXOr2rAHu9tPvBgpzZUbWAiADNFcWT5%2Ff%2BgV%2BzPEQ9Q8druVXoC5LW6mr%2Bk1gdKOobCr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMEA86ewZ9xd9sNPgnKtwDUrcsmEn8jw%2B9r%2For2yj6zITpNLNuF1lj4vrzHJzEASU08wt1M6etWs9inG3dg7WJFDp9NKBZ1L0Md7DBGrBMTIfD4vdO9OPiW1t57h%2BKW6k4%2B7v5lFH5Hq1S3VHeLrcpheUeR9SOW7WuISMpk%2BK8%2BnsIDTtq0ZOG%2Fomk95of494XWuhtIh2uRzAVLZVNWud2BbEIzovn0e5m9Sj1cx22Sbj8sNbD%2BvBDxfU80pPfTug0ldeEJNC01ICQOCKkFT7k0CUcsNv2wgoaCy4OsTJqmJFn13iH00RlwLHxFncIiBWUhxLdcyo1FD6lmGn1o8loZFUMtVyyqyC6Gya2J%2B3GHf3TplKzhCiva%2BISTpRDPB%2B%2BOzz1S3SvNw%2FBmXLZ97JhRy%2B03yEic0oralYzV6gAyJIpqqcStCHDCm0SvGo%2BtpjlwLyCyji%2Bh1klVSZ8KcVPbUV4l6nR%2B4YE3XKTpKAHCOf1SRShxZPJAsgDgs56E%2FwNwboOA3MezFFfNtGU2LZ%2F%2FPWVJSq6SrdsAVMDCVPMacLZaqVeVAiDlX8EGhZAxr9lPDpq8LDVsoIPWJ5gwdJRpehAR%2BTDgbfgo9QvcxwO4W0YWcdML%2BDzoYmzjK50SV7yp4bXL6mPwa%2FPKQ0w49fV0AY6pgELjKF1ea3Tck9dsMmIjwDwnex3XbKzNvspiTfZqEYWws2KGW%2BYn7%2FBoYZA3FeswoPCvoKb%2BlpBAjMnIqc6wh2BG7oPuaM8maSYZQvnh0F%2FCjwHBVYaAhCrkU4tkahPldT4ckPn9xThQTHIKgDA8bTKQ0VOMYqnBd%2F4Poyxu0Cs03HwD44f2wEWjpwgU1QtX3Mrkz9QtGpMWS3ONOe6Ma2wimngvcTt&X-Amz-Signature=f94f8ce453b9678535b5e7638c9b0a61fed3b7a5512f481158744e8a6bbd5165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
