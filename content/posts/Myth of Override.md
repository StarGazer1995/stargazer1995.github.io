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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNWPX7RX%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T124038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtZ8%2FLO1kJ1wJMmYAfNVUN3V22l4TNpMeF5ndxiAB0%2BgIgXeQHo2DRXms0%2BLAaCfyzbKeJudxr7L1Ns8sPZd8DZF4qiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKl6tKcz%2FT%2Fm06yNCrcA6vt2lGemnLz7lTSKO7ffBAOl69ImIRutQTf4GFaKCSOhXJpXH5IYnB5cICZ2MMF9xNyVtFcsOp5tSEhZtrmall7KxykmLUqHNDYJKgKEPy7QOZ6XkxKkHGBEIHWr3QI15Bq44V8ZcQXRGxUd1tcOTDyajyblgyQMG9Vv3ZCPvFUDKsq0oNkHlL4VVi05oGr2A0fHAttTFUvvK%2FU59IUIyj04Feda%2BKUmoH9mtp8cp2DLlOa%2BrkXxk51mrMifGB4KYcdc0JIb%2Fo%2FDyixAYWxHMQPmOGpj%2FS0IT9xHxJqeX%2FVqlRLIaaqd4YMKmfe2y0jfVPX4%2B3bcWAB1iZKPdfJa6rSs%2FePL5Sapm0AesrBODDRcWSjdTuGSKh3dK98877k0SUQP2Bf9x6i0bAKhJWwhG17u6x5vmnoeYp66d7tbVNI47xDhglKZ%2BEu3hplGoupXu0fvI6Pf3D7xRkYLbfaPTrcc5475uPqDH8%2FjLSxyzqLvL1%2BSB0XOEb8RE68bJGw1MqO7d2TOMnl%2FwClIRlGiLeTISVmHmpjU8k%2BpRqkTnUw0Gj7UDNZzGZ3lFQRjmmKUwM4guf5Jw6e61YiDPQgyUfB4woC%2Fg3VpACQxEWObPb5bFXozX8g1A3yKDBPMNjs5tMGOqUBmI%2FKnSd5FIBOCugxYhPAaeCqHkTgbQOzZFG%2F8m5qqxLpMryc0EdX%2B9smfhLo8ytgSX5FPeKK8h5%2FdbxypZHAOPhqwScmwnqEO2O9c7sMruv0SM1UM4x4Pfv7D8E0fxh6zoDUreUVhvcN8fVLcmxlHwS8a97hgbEOpM1BN85UIdRQ2fDsGh80QAWVz%2FUyzGeDG47qNc1ed78kV04sekxhwwKEKSD4&X-Amz-Signature=e27308dea59327a87be7a53e3757a8f8036994e562feb026f32c2cf73303e75c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNWPX7RX%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T124038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtZ8%2FLO1kJ1wJMmYAfNVUN3V22l4TNpMeF5ndxiAB0%2BgIgXeQHo2DRXms0%2BLAaCfyzbKeJudxr7L1Ns8sPZd8DZF4qiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKl6tKcz%2FT%2Fm06yNCrcA6vt2lGemnLz7lTSKO7ffBAOl69ImIRutQTf4GFaKCSOhXJpXH5IYnB5cICZ2MMF9xNyVtFcsOp5tSEhZtrmall7KxykmLUqHNDYJKgKEPy7QOZ6XkxKkHGBEIHWr3QI15Bq44V8ZcQXRGxUd1tcOTDyajyblgyQMG9Vv3ZCPvFUDKsq0oNkHlL4VVi05oGr2A0fHAttTFUvvK%2FU59IUIyj04Feda%2BKUmoH9mtp8cp2DLlOa%2BrkXxk51mrMifGB4KYcdc0JIb%2Fo%2FDyixAYWxHMQPmOGpj%2FS0IT9xHxJqeX%2FVqlRLIaaqd4YMKmfe2y0jfVPX4%2B3bcWAB1iZKPdfJa6rSs%2FePL5Sapm0AesrBODDRcWSjdTuGSKh3dK98877k0SUQP2Bf9x6i0bAKhJWwhG17u6x5vmnoeYp66d7tbVNI47xDhglKZ%2BEu3hplGoupXu0fvI6Pf3D7xRkYLbfaPTrcc5475uPqDH8%2FjLSxyzqLvL1%2BSB0XOEb8RE68bJGw1MqO7d2TOMnl%2FwClIRlGiLeTISVmHmpjU8k%2BpRqkTnUw0Gj7UDNZzGZ3lFQRjmmKUwM4guf5Jw6e61YiDPQgyUfB4woC%2Fg3VpACQxEWObPb5bFXozX8g1A3yKDBPMNjs5tMGOqUBmI%2FKnSd5FIBOCugxYhPAaeCqHkTgbQOzZFG%2F8m5qqxLpMryc0EdX%2B9smfhLo8ytgSX5FPeKK8h5%2FdbxypZHAOPhqwScmwnqEO2O9c7sMruv0SM1UM4x4Pfv7D8E0fxh6zoDUreUVhvcN8fVLcmxlHwS8a97hgbEOpM1BN85UIdRQ2fDsGh80QAWVz%2FUyzGeDG47qNc1ed78kV04sekxhwwKEKSD4&X-Amz-Signature=f69ac4d209373f89d1910a2a74ecdfbfb318288a29374452aec113c09e0a7cad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
