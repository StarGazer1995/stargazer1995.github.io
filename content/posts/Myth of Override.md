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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN7Z5HLY%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T014954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCYrWCLacTpUY%2F8vYocCo19aLqP1qfZEF3sfDL9yWCCcwIgFMJ6EVW6fvY4%2FHFf1LAyL96XUySsv30DPQOQFYt9%2BzQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDNhVZX1RPM9DPPdwPyrcAzSEz0Zla%2FjZoICQ7B021Hm8JbZodyJDJQnCmALh64J564cPXdM8sP0Co7ztlNcsrPa4HzSgNwXbFdbjoSGX1UPVMW8%2FEnZvBIB6Qy5YjnSnDZLSz7yYbWDCqnZSr1ePXd21C4dBuKWpkvbfiSOAUF03lIjx9ZwkuYyMTEazoZOkAuMa6uiCwkLlmK5SjXuBtf1HJTsGqO3uvcGq7%2FNo32JeMsj%2Bb0TYcvfqslOsBLK8iWzI3Jy45Xl6drDNr2UoDP2c83gXhtrGtyyD74EWBzOWVxAKIdWHqkxRbvDPuTujms%2FHBPfS9MFMmE9yL8vTTpa0ojjQr2jIuGbMqozB91lyV1gP8Ks16qCssXxW3aTp2zgI25VC%2FZvL%2FUElz1GOxDvSVS%2BwCtsMhDxR0oVnP2WU73ZFtVS0pciq0xxJnfCgmfyJWAfdZjPmLNKA6GcE5BBOZghBmXH7dbjSU%2B7RmMfZ8BR8kCOd%2BOJ%2FGocvwTG7rz%2Bxp77RE4SguiEiKuBsG8xlMbZuAU9rG6rUikx3vHsX1cxlowzrn%2BzlC3tx4YzFaEPWRgC06b68dzLMQM9793uZOFl9n3%2Bpwh%2BSM0TqX5O%2F1kU3AlofB2TGZEwPRyGVtRAKEOPWoaQ3KrDVMMHZptIGOqUB44QFYPT%2FiyPHLnW4mT2ZaoMOVA3QRjTlgPP%2BX4DsjUQ0o6rdt31RkC9t9ObRYYrLdWtlC%2B%2B4PkNTZ45yWFS97DozdaKWRV6EhKuNmQ1YePuRgmWBAbsNDsGpqaKl6p%2ByWiXYKl5zM5jUBIr%2B32Tgm7r7ql%2FQ734U9Xah%2FcagxDQzmIUQbahGFbhQRTKTM0JBV%2FPOZhjUh2zlqWy4Sy4Owr4m26%2Bv&X-Amz-Signature=f43f5f155e3038afa51dbedd46a1bcb7eed8a4f72f7c8b36acbc9dd3840d6a15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN7Z5HLY%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T014954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCYrWCLacTpUY%2F8vYocCo19aLqP1qfZEF3sfDL9yWCCcwIgFMJ6EVW6fvY4%2FHFf1LAyL96XUySsv30DPQOQFYt9%2BzQq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDNhVZX1RPM9DPPdwPyrcAzSEz0Zla%2FjZoICQ7B021Hm8JbZodyJDJQnCmALh64J564cPXdM8sP0Co7ztlNcsrPa4HzSgNwXbFdbjoSGX1UPVMW8%2FEnZvBIB6Qy5YjnSnDZLSz7yYbWDCqnZSr1ePXd21C4dBuKWpkvbfiSOAUF03lIjx9ZwkuYyMTEazoZOkAuMa6uiCwkLlmK5SjXuBtf1HJTsGqO3uvcGq7%2FNo32JeMsj%2Bb0TYcvfqslOsBLK8iWzI3Jy45Xl6drDNr2UoDP2c83gXhtrGtyyD74EWBzOWVxAKIdWHqkxRbvDPuTujms%2FHBPfS9MFMmE9yL8vTTpa0ojjQr2jIuGbMqozB91lyV1gP8Ks16qCssXxW3aTp2zgI25VC%2FZvL%2FUElz1GOxDvSVS%2BwCtsMhDxR0oVnP2WU73ZFtVS0pciq0xxJnfCgmfyJWAfdZjPmLNKA6GcE5BBOZghBmXH7dbjSU%2B7RmMfZ8BR8kCOd%2BOJ%2FGocvwTG7rz%2Bxp77RE4SguiEiKuBsG8xlMbZuAU9rG6rUikx3vHsX1cxlowzrn%2BzlC3tx4YzFaEPWRgC06b68dzLMQM9793uZOFl9n3%2Bpwh%2BSM0TqX5O%2F1kU3AlofB2TGZEwPRyGVtRAKEOPWoaQ3KrDVMMHZptIGOqUB44QFYPT%2FiyPHLnW4mT2ZaoMOVA3QRjTlgPP%2BX4DsjUQ0o6rdt31RkC9t9ObRYYrLdWtlC%2B%2B4PkNTZ45yWFS97DozdaKWRV6EhKuNmQ1YePuRgmWBAbsNDsGpqaKl6p%2ByWiXYKl5zM5jUBIr%2B32Tgm7r7ql%2FQ734U9Xah%2FcagxDQzmIUQbahGFbhQRTKTM0JBV%2FPOZhjUh2zlqWy4Sy4Owr4m26%2Bv&X-Amz-Signature=bb364499e38ef0487955a64679b0bc82dc7f4b1f3aaddfeeac7d020923e2d9e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
