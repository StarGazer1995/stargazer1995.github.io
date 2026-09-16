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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ7XVN4Y%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T191051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIHHF%2FK3bs%2FoTZH4LXg8ttIMiVSkoi1QKZ9SPoIZyXPrxAiAoA9NU2DeCeio8NBhTDT134zeUrVzu1%2Fbp0zB2%2FKBnRir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMyKJAteI9zrzvLmqSKtwDIaT2mk28YXvdS9FPgQk9OxL1rinJo%2FNLu4T%2FI2xwksodG6F0tOiNcne5a6Q212FRS4hhOKswNeg7D2N6p%2FUegKtJowvzYw4FJy6fQ5pC5iuwg8vqVktik4Cdjc%2Bfx2Tic9wYJBEePbsOQazcS9%2BJebb%2B3rnEt1LiqiLUW2T7AT4ajSXy8r256DPCiTdjbHRL%2BgAaasI8BISiorEMWJhdjrI5%2BP8iClrwQ0XXi0x4bGKrqAY5PM2OtYAl64DbAmhfF9JU0n6F%2F2pniI6B3FeXQEg9KhOtzluSaIU1TdT1b%2Fk7kVEt2kLf5BiTDTeK5WRJbFYb7k55E4UXGN6OhsegzuglFAc1v7ZOXZIc480A2O%2BrkCi8BTUXmS0%2BP1IuWMYelWDmZPTIOrGd7w8RdCpNGcTdKT7ldvCtH997XMjv1WampSgJ27WYoIAaeefxQCDbsRo%2FTFMiAn94AuQoC8Yxvif31I%2Bx%2FBCVJmyY8a%2F%2FX6tZOnewHW8cwoZHhzKUIovm0WijHb8z%2FMVK%2BZtZpbYUS93RYK3f4K%2FUUNhDya6Vbm3jusn%2F923TjZNO%2F9lIJY9XuoroTye98pqgypYB%2FnApuMeeI1om5DWTFHOj0TUrKOK39MTpqENTfVJyW98w6J6r1QY6pgG9NpuLqPH6cYj5XsxErvntLzTZ62K2TNc%2BZuMJ750wy8gDCMPO%2B40KY7UjkA06R8vLwX3O50beFz0VDgN%2Fy7QrCwlnxkOE%2FtT5Q4%2BuTWFkHqaK0XtWxCmJxeOUS8DTsjYoQTkUcPq83rvv94qK3ArtRnjQFpph%2F1%2FJqOJnAcY7qiZ9lZLKGAgE2%2BPfBlxCn7%2BBzPkJjFpP%2BQhFoYsRQff2dcpaHLrk&X-Amz-Signature=9105fae1cc4744bdd435f877580c2c1c9a5a968647a8519e98ff4f0a6d58e1e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ7XVN4Y%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T191051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIHHF%2FK3bs%2FoTZH4LXg8ttIMiVSkoi1QKZ9SPoIZyXPrxAiAoA9NU2DeCeio8NBhTDT134zeUrVzu1%2Fbp0zB2%2FKBnRir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMyKJAteI9zrzvLmqSKtwDIaT2mk28YXvdS9FPgQk9OxL1rinJo%2FNLu4T%2FI2xwksodG6F0tOiNcne5a6Q212FRS4hhOKswNeg7D2N6p%2FUegKtJowvzYw4FJy6fQ5pC5iuwg8vqVktik4Cdjc%2Bfx2Tic9wYJBEePbsOQazcS9%2BJebb%2B3rnEt1LiqiLUW2T7AT4ajSXy8r256DPCiTdjbHRL%2BgAaasI8BISiorEMWJhdjrI5%2BP8iClrwQ0XXi0x4bGKrqAY5PM2OtYAl64DbAmhfF9JU0n6F%2F2pniI6B3FeXQEg9KhOtzluSaIU1TdT1b%2Fk7kVEt2kLf5BiTDTeK5WRJbFYb7k55E4UXGN6OhsegzuglFAc1v7ZOXZIc480A2O%2BrkCi8BTUXmS0%2BP1IuWMYelWDmZPTIOrGd7w8RdCpNGcTdKT7ldvCtH997XMjv1WampSgJ27WYoIAaeefxQCDbsRo%2FTFMiAn94AuQoC8Yxvif31I%2Bx%2FBCVJmyY8a%2F%2FX6tZOnewHW8cwoZHhzKUIovm0WijHb8z%2FMVK%2BZtZpbYUS93RYK3f4K%2FUUNhDya6Vbm3jusn%2F923TjZNO%2F9lIJY9XuoroTye98pqgypYB%2FnApuMeeI1om5DWTFHOj0TUrKOK39MTpqENTfVJyW98w6J6r1QY6pgG9NpuLqPH6cYj5XsxErvntLzTZ62K2TNc%2BZuMJ750wy8gDCMPO%2B40KY7UjkA06R8vLwX3O50beFz0VDgN%2Fy7QrCwlnxkOE%2FtT5Q4%2BuTWFkHqaK0XtWxCmJxeOUS8DTsjYoQTkUcPq83rvv94qK3ArtRnjQFpph%2F1%2FJqOJnAcY7qiZ9lZLKGAgE2%2BPfBlxCn7%2BBzPkJjFpP%2BQhFoYsRQff2dcpaHLrk&X-Amz-Signature=b28ef39ec546e15e33517296eb181b860952c2399676a2b8b820bd7ec4dd8723&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
