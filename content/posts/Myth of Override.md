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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624L2I54Q%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T161807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5h1vK5cg8H9l2bEVO64CXw2x3lqwUT5cdmmrvjTJRPAiBVt2CpLCzwgDH9cn7XG4H4WRqY%2B3XcVcfR1QuHaMz1myr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMqgNMWZ6KN8swXe2aKtwDs%2BR4cJD96CCwBh7%2B7tK78dHNTl%2BemffvTDfZ5aGPbf8TvNljFGfkp2Q6FUZ4PBRTlZHRNyqQj7U8uHYVlXOdOBcfoHPLEwhXhcvZ8SXD3%2F6PudRRi2vsQKh14oYB1oRMdE0HkJuf66XHZYDaYYH%2BIif42J1QdoIdkqByCVYxNUb2KKt8wkFZPEIfibcIVJPV5k40PV8iSRRUEVRqf3w%2FihtBKtaansuSYw9jHHwmOw0ZqLHGpGL1P5izWDPxv7TTEoLW8ytJjQQWMJgMqt1wSQjQ1cDPhFjCEFNe2uEqvp7f50x7f6KrGawJJGCw61rCMa4%2B17AyWV1jah%2BFI7KPnUxse2HfVBJ114iLgNnCq47Df7OnrJv1eNinpw9qqJhnhfSayFL8n1U3iwOgUBsHpqi6hYt2Qb80qEam3OMM5taFolYhMRYP7f86HXYxETKH5wrzn1J0QLfxhzkVfs1dCXuJH4Hqua%2FjHSEZqsMhQNxd6%2FVR2owt7jHBi9VQU4ehWQ4DWXT7eNoftXTRNELkPppRvW7lo%2BrB5yue%2BENA%2BaHibt2LJNn4u%2FgO38r88pqmc3iP8ME0gJaB3r%2BkhxiMRtMC3MP66WlU%2Bw4UY%2BL%2FUzSdf3kB6CrimLffEdEwsv2R1AY6pgF%2BDq2CTJJhYh43D1ezldvSdm6mTf%2F04Impc83qXzQVrwOEHpJdpLe0K4%2Bx5dlC2fIhz198FTnQo95O8A%2BI%2FIadklK7S62Snpl7LWuHpFaWU1taMBshFHsGgX%2FDFGxWn9lTfCa2wLiHWDXLj0t9OzP%2B1zhhmNFEOMoi37UL1o%2FeS92moe5k7lrRZQaFeMtDkLN2uTZrSGs3KjmiLxzbUpOJuAiSGfEP&X-Amz-Signature=5610fc5885d3d4ffff00dacbbb40deadbf6a26a288634d71f10748f8bbaa3c04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624L2I54Q%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T161807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5h1vK5cg8H9l2bEVO64CXw2x3lqwUT5cdmmrvjTJRPAiBVt2CpLCzwgDH9cn7XG4H4WRqY%2B3XcVcfR1QuHaMz1myr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMqgNMWZ6KN8swXe2aKtwDs%2BR4cJD96CCwBh7%2B7tK78dHNTl%2BemffvTDfZ5aGPbf8TvNljFGfkp2Q6FUZ4PBRTlZHRNyqQj7U8uHYVlXOdOBcfoHPLEwhXhcvZ8SXD3%2F6PudRRi2vsQKh14oYB1oRMdE0HkJuf66XHZYDaYYH%2BIif42J1QdoIdkqByCVYxNUb2KKt8wkFZPEIfibcIVJPV5k40PV8iSRRUEVRqf3w%2FihtBKtaansuSYw9jHHwmOw0ZqLHGpGL1P5izWDPxv7TTEoLW8ytJjQQWMJgMqt1wSQjQ1cDPhFjCEFNe2uEqvp7f50x7f6KrGawJJGCw61rCMa4%2B17AyWV1jah%2BFI7KPnUxse2HfVBJ114iLgNnCq47Df7OnrJv1eNinpw9qqJhnhfSayFL8n1U3iwOgUBsHpqi6hYt2Qb80qEam3OMM5taFolYhMRYP7f86HXYxETKH5wrzn1J0QLfxhzkVfs1dCXuJH4Hqua%2FjHSEZqsMhQNxd6%2FVR2owt7jHBi9VQU4ehWQ4DWXT7eNoftXTRNELkPppRvW7lo%2BrB5yue%2BENA%2BaHibt2LJNn4u%2FgO38r88pqmc3iP8ME0gJaB3r%2BkhxiMRtMC3MP66WlU%2Bw4UY%2BL%2FUzSdf3kB6CrimLffEdEwsv2R1AY6pgF%2BDq2CTJJhYh43D1ezldvSdm6mTf%2F04Impc83qXzQVrwOEHpJdpLe0K4%2Bx5dlC2fIhz198FTnQo95O8A%2BI%2FIadklK7S62Snpl7LWuHpFaWU1taMBshFHsGgX%2FDFGxWn9lTfCa2wLiHWDXLj0t9OzP%2B1zhhmNFEOMoi37UL1o%2FeS92moe5k7lrRZQaFeMtDkLN2uTZrSGs3KjmiLxzbUpOJuAiSGfEP&X-Amz-Signature=ea07b00ee5b2f5dacb40bde5f20662ee1d1168a514bb1ab70c2afed8bacc6b31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
