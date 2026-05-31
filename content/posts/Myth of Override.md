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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XL46KN3%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T190102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCkSqssShVuI9HxndmHo%2B74i11CnhMKYqIZPNYZ%2Fwwf8QIhAKxcAM2fjPXeeUzBoGHMVg%2BazHm4GCh1tJae8%2B8rbROyKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxn8blgeaG7LtxVHkAq3APAQ3BG0YNPDKW4anxiSWFaeob%2BuEelcBw%2F1GLrYoh5u9jbu9xDL3w%2B9YRFWRp%2BVKpEc2bScoAl20mPscfjBwZxvYiZB6uEYSnBJVhTFr4ZsO2Ahkbk%2FlGWElWJz%2F0Pjaia%2FYLDlhKePc2w9QC6qHgGaMsgQ7TdcwEaIJlLX4EdCOkvOg8HcMhj6fa8a6JWtvk3jwRmHkkgaGer1tIN9pWR6L85KJYDAsx%2Bi5ddsFNsvZVOxkIyhaHJR6UqOdYaU%2FkubZtgqewG5o7dbsn6Id788iFaH8X8Wz1xIzcqDoiFYfGf%2B1G7m6jht6kji3E0xKQRdL9bqwpvlbhE1TrBW7dXUL7A2I91X8HUivkRm%2FZRiBUMCX0Yo5d2Smx6a79g8vdNcjCQ264hPw1DOq4Tmt3KgCxnnbXmU%2FWwIm8RDL8tpaM2iZvu1gy%2BKpQ3YH%2FlATcyoyZ%2Bpo4xYHYnaKJhP5P616%2FoOG4XSYVPK2pkUrXzzh0JEAOOCnpYI3Qkb6P773GCRGygTsvqFVGBnB3t9B93bN%2FOP4Qtj28pRGDeNVUHNBuT%2BsHWa7CgjfGL%2B5%2BkuQYmRpzS7CmwaTV8UY1vXOfhh1kiFzytYYEZx0DatE7iR3W%2BY%2BgZTGXy%2BOaMiTCJ0fHQBjqkAdi3R86A%2B3y7gGp4aF38VV17Puo6Ljems8dBZAh%2FNQiMdNJ25WtYyB2dRnZfbYp3ZuekTZTAy1qd5TH6msVnvCWe9PUuASnq2tjynakqsYkcNKd%2BVQsfpFPQSUctVPaNjOwNjrDT9f%2B%2FOSPY%2BedEDd%2F8gY0e45KWnLJ9yz9lJKr5otbEdmALTO2iYSrAn%2FwvIE84GhiTXitUpPyhj9gh94JZXvBn&X-Amz-Signature=6fc281dd7f7e73eb2b553cf4f376095200f0285c4d69f40383f6f8e9f44bf35d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XL46KN3%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T190102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCkSqssShVuI9HxndmHo%2B74i11CnhMKYqIZPNYZ%2Fwwf8QIhAKxcAM2fjPXeeUzBoGHMVg%2BazHm4GCh1tJae8%2B8rbROyKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxn8blgeaG7LtxVHkAq3APAQ3BG0YNPDKW4anxiSWFaeob%2BuEelcBw%2F1GLrYoh5u9jbu9xDL3w%2B9YRFWRp%2BVKpEc2bScoAl20mPscfjBwZxvYiZB6uEYSnBJVhTFr4ZsO2Ahkbk%2FlGWElWJz%2F0Pjaia%2FYLDlhKePc2w9QC6qHgGaMsgQ7TdcwEaIJlLX4EdCOkvOg8HcMhj6fa8a6JWtvk3jwRmHkkgaGer1tIN9pWR6L85KJYDAsx%2Bi5ddsFNsvZVOxkIyhaHJR6UqOdYaU%2FkubZtgqewG5o7dbsn6Id788iFaH8X8Wz1xIzcqDoiFYfGf%2B1G7m6jht6kji3E0xKQRdL9bqwpvlbhE1TrBW7dXUL7A2I91X8HUivkRm%2FZRiBUMCX0Yo5d2Smx6a79g8vdNcjCQ264hPw1DOq4Tmt3KgCxnnbXmU%2FWwIm8RDL8tpaM2iZvu1gy%2BKpQ3YH%2FlATcyoyZ%2Bpo4xYHYnaKJhP5P616%2FoOG4XSYVPK2pkUrXzzh0JEAOOCnpYI3Qkb6P773GCRGygTsvqFVGBnB3t9B93bN%2FOP4Qtj28pRGDeNVUHNBuT%2BsHWa7CgjfGL%2B5%2BkuQYmRpzS7CmwaTV8UY1vXOfhh1kiFzytYYEZx0DatE7iR3W%2BY%2BgZTGXy%2BOaMiTCJ0fHQBjqkAdi3R86A%2B3y7gGp4aF38VV17Puo6Ljems8dBZAh%2FNQiMdNJ25WtYyB2dRnZfbYp3ZuekTZTAy1qd5TH6msVnvCWe9PUuASnq2tjynakqsYkcNKd%2BVQsfpFPQSUctVPaNjOwNjrDT9f%2B%2FOSPY%2BedEDd%2F8gY0e45KWnLJ9yz9lJKr5otbEdmALTO2iYSrAn%2FwvIE84GhiTXitUpPyhj9gh94JZXvBn&X-Amz-Signature=e0975047e551d5e3bc795cd75f2d48c92c009500629d403b4c04a239ff63482f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
