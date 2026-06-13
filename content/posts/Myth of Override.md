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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPIYQHB%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T152526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIFL14VVSQd19glkHYS9SOGChF3W32bEhoIFV7XgI80seAiAbKyNxLKMClTQmmXpo8wQfwwQdTqiq6ZLHmVMIN9c7ZCr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMsd5X26u66ckGjY9UKtwDRBBgKrDQqKy4pBgHSMFyF5UZp3z0WpF%2BdYAXiPwBOqfiu9XjKfejhStC7xz8WTRtebgUEcyi7BYGTHV3d%2B4KoarU3jUQbbWCFIGRbKU86lKRbTegc35J3xjctua3FTVMNE7kRKUnaTxtjaRgjt7LP4TUSHW0gudZXNnMHr90%2BM08a2c1W3ZW8I%2BwYvqL2lsMeHmovE%2BA%2BOHPjTJxyv2Rf7zciDTWQPEY%2Beah3nXalOq50tvW8%2FKi%2FXHTf99NXQsZTCqVWDNPjjzLiaUewEDu2WxTZ04k8YgAqzxEWEBTAm9doO1EjGfC%2FEoP7ajKPThJT2EwYs1nSXCjCXYzMQy2feeGoBPm%2BmK52ApmxjaNrCQXPCpqGMD2zgPJTyESnUu4xO5paPG9A13co32WrA3SenLbZdLmGmvr8mI7SBq3jov%2BSzv2aC9ah0IWUYk63G%2FPEDHZBlMMNIhc0ulwol5qtj1CLPH8XYY0sM2djrAhKDgdoWjhkgixaZ2VAXt08mopYvBkx1QWFI3WsKsbnUP%2BC0sTXKMRzPDmxJ07YlIqhtwG6nkF2CAmoYXK4EDMFFu1VQgf7%2BASWS4doA0smnqh%2Fz5v5deHu5S96pjPBC%2FNviPCZ0NmV1wW%2BfLW3IAw9um10QY6pgFdGAOVnpzYKXyTAE5ME9H8JmzsfzcObI5omgyUx%2Fs19QxroD4ymlQGyCp8JGv7UYUmQ%2F56PcnIM4%2FK85aguTgLUryQgTFwLOBBIbxj6D6S%2BUZ3iySXw3fHYntG5B6OIFdI%2FY%2FehWSMUD1A1jYAL3Pi6w2Xkq0HjMHMwezEiyBqjmIOoYvY2TrJU%2BHtchrB7rEE4Zb%2F%2F28czoryfRAGyFOEr6Emq%2Fm9&X-Amz-Signature=42131e1607545c9f850d7cef00af320470649ba9fb4b225085016ea5c20fe338&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVPIYQHB%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T152526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIFL14VVSQd19glkHYS9SOGChF3W32bEhoIFV7XgI80seAiAbKyNxLKMClTQmmXpo8wQfwwQdTqiq6ZLHmVMIN9c7ZCr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMsd5X26u66ckGjY9UKtwDRBBgKrDQqKy4pBgHSMFyF5UZp3z0WpF%2BdYAXiPwBOqfiu9XjKfejhStC7xz8WTRtebgUEcyi7BYGTHV3d%2B4KoarU3jUQbbWCFIGRbKU86lKRbTegc35J3xjctua3FTVMNE7kRKUnaTxtjaRgjt7LP4TUSHW0gudZXNnMHr90%2BM08a2c1W3ZW8I%2BwYvqL2lsMeHmovE%2BA%2BOHPjTJxyv2Rf7zciDTWQPEY%2Beah3nXalOq50tvW8%2FKi%2FXHTf99NXQsZTCqVWDNPjjzLiaUewEDu2WxTZ04k8YgAqzxEWEBTAm9doO1EjGfC%2FEoP7ajKPThJT2EwYs1nSXCjCXYzMQy2feeGoBPm%2BmK52ApmxjaNrCQXPCpqGMD2zgPJTyESnUu4xO5paPG9A13co32WrA3SenLbZdLmGmvr8mI7SBq3jov%2BSzv2aC9ah0IWUYk63G%2FPEDHZBlMMNIhc0ulwol5qtj1CLPH8XYY0sM2djrAhKDgdoWjhkgixaZ2VAXt08mopYvBkx1QWFI3WsKsbnUP%2BC0sTXKMRzPDmxJ07YlIqhtwG6nkF2CAmoYXK4EDMFFu1VQgf7%2BASWS4doA0smnqh%2Fz5v5deHu5S96pjPBC%2FNviPCZ0NmV1wW%2BfLW3IAw9um10QY6pgFdGAOVnpzYKXyTAE5ME9H8JmzsfzcObI5omgyUx%2Fs19QxroD4ymlQGyCp8JGv7UYUmQ%2F56PcnIM4%2FK85aguTgLUryQgTFwLOBBIbxj6D6S%2BUZ3iySXw3fHYntG5B6OIFdI%2FY%2FehWSMUD1A1jYAL3Pi6w2Xkq0HjMHMwezEiyBqjmIOoYvY2TrJU%2BHtchrB7rEE4Zb%2F%2F28czoryfRAGyFOEr6Emq%2Fm9&X-Amz-Signature=4c743544963e8f83865259ae45a278458842314d0d45479f40faadb2aaf2de2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
