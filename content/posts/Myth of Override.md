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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIUIRXDB%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T014954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPnrejVM78aC8epwrzeMa%2BGoBFqsp5MAijZGTvVaImZgIgLo1NtMLt2t9nF3bmVyz1E8J109Fyin0YwEdL%2F%2BxM1soqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPsiREx24vr8uO4U2ircA4JNYKTslr7FFXCUYashG8s8PXiks9lV3Y5fUXv7%2BZjhOexp7X7LAwRUWsnzTVWK1lHYUptF1u3HUcddTJ4x2bRWogEeIhBdwHuAE21OMiU2vmZnSHmI86u0gjZMd7mQxPKBQkP9zaN2VwEyhVfrTB1WnJdkwTYTAi%2B7MEpM%2B9WdEgsbfa%2FQ7D8GLaZo6OCcxcdI00ReNv%2FpIJC6mqAKoEyVBKR5YjdC90gXq5BmD6MpRid67AiB4p5iGw9u7uS5%2FR7NXmtz2Gg%2Bht2SRkMIDwtcZKguKssUwADQfPUiNJ6ETjAZopgw4BmvMtF1nOkK%2Bep58KH0%2FTAO%2BmHuVZxUjVs%2BDhD0JGVVmwXekfBs7OY%2BGGy%2BPlMEfsC7Idy0xL9E0oqaAmujoF7QVs176IZt1Wer0HiKtp6We4U5Xa%2FJMgk3%2BayS17ISXg76dKBb4qBeVlW71v7yWU%2BL9up798ji7qj8iYqP2ETwL6roSLGuUNwitAE9T9f3YIqIT9FBsaCQ%2FhPk27YKqxt5cUa2urfgtUpXAr%2FH2spmhHn%2FX8m2FWFkAtRJHLXU1Ah%2B1pCAPN6Wbr0jNyHlYjGODbyhTOk1L1FByo3%2B8IMIZPtxGYvBw4060nNlUU8nb79FT7TiMICVn9AGOqUB%2Fdk855rItkd2rbKUOI1K02w1HhQURj4kEn99I6G4LiIo5HHCbxFDHi1%2FluMaxKcS8pdD2UTKsi6YpGdgmHgYZpWTgokQeGccL%2BlNGvaLR9wRPSSvJFrTaHOWgCbAoNc6FRBBi4YTsAuaR5ZugPEqMArXoZpipY77PGo1CiqoXu%2F03fohEoGLN9n5utmq53Uji20PKGcSUE4YHDXO7CVUKrOU3g54&X-Amz-Signature=6bd4502dcc38ea263d83b839d27f009f4c19691e2ff92d6448cc42d51c64e44d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIUIRXDB%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T014954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPnrejVM78aC8epwrzeMa%2BGoBFqsp5MAijZGTvVaImZgIgLo1NtMLt2t9nF3bmVyz1E8J109Fyin0YwEdL%2F%2BxM1soqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPsiREx24vr8uO4U2ircA4JNYKTslr7FFXCUYashG8s8PXiks9lV3Y5fUXv7%2BZjhOexp7X7LAwRUWsnzTVWK1lHYUptF1u3HUcddTJ4x2bRWogEeIhBdwHuAE21OMiU2vmZnSHmI86u0gjZMd7mQxPKBQkP9zaN2VwEyhVfrTB1WnJdkwTYTAi%2B7MEpM%2B9WdEgsbfa%2FQ7D8GLaZo6OCcxcdI00ReNv%2FpIJC6mqAKoEyVBKR5YjdC90gXq5BmD6MpRid67AiB4p5iGw9u7uS5%2FR7NXmtz2Gg%2Bht2SRkMIDwtcZKguKssUwADQfPUiNJ6ETjAZopgw4BmvMtF1nOkK%2Bep58KH0%2FTAO%2BmHuVZxUjVs%2BDhD0JGVVmwXekfBs7OY%2BGGy%2BPlMEfsC7Idy0xL9E0oqaAmujoF7QVs176IZt1Wer0HiKtp6We4U5Xa%2FJMgk3%2BayS17ISXg76dKBb4qBeVlW71v7yWU%2BL9up798ji7qj8iYqP2ETwL6roSLGuUNwitAE9T9f3YIqIT9FBsaCQ%2FhPk27YKqxt5cUa2urfgtUpXAr%2FH2spmhHn%2FX8m2FWFkAtRJHLXU1Ah%2B1pCAPN6Wbr0jNyHlYjGODbyhTOk1L1FByo3%2B8IMIZPtxGYvBw4060nNlUU8nb79FT7TiMICVn9AGOqUB%2Fdk855rItkd2rbKUOI1K02w1HhQURj4kEn99I6G4LiIo5HHCbxFDHi1%2FluMaxKcS8pdD2UTKsi6YpGdgmHgYZpWTgokQeGccL%2BlNGvaLR9wRPSSvJFrTaHOWgCbAoNc6FRBBi4YTsAuaR5ZugPEqMArXoZpipY77PGo1CiqoXu%2F03fohEoGLN9n5utmq53Uji20PKGcSUE4YHDXO7CVUKrOU3g54&X-Amz-Signature=5738b0d71e70898ea078d8f1901ead0e4ac6ef442027531b846efbc94bc67235&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
