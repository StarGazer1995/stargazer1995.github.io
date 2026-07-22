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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQCZNM2N%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T225158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCbvStofHycOr8WLADVWoN8Yp3rpzLOndKsYf4F1RFFrgIgZm8AXhAbYk2tfqpYHsVNZ8UYUi9A8YCSsglCoifH5D8qiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJK4QVHMEwT%2F5xRlLCrcAxDHyvIpEzRisaxTNYe0gCROxShHwkauzY%2B6JuA8JryRgf5mz%2FdOLOPBFYWy%2BWWjSquYeUkLO4mDhfM8PViV%2F0%2F7HcaYrBgmVFOm8ugAfv%2Bz6ryzOCPzJWTlRCrXMuJpdvxa3S%2FEiOc0B3Z140CvDs7JHgibFjr72I0bTIv53VYaTLjMhVgupp%2BoHRRyom%2Bxt7zwcjIRRBU9OZphPbwg2P46i9NkV1w9qHkYqircXKc4k15nwOrHHjKqvU%2BphiMS1Cj%2Bugwi6J7IrhHCtnwoVC%2Fan6frMVab53wNdXc0wcGh0EawnAC2HQJjiTg0rYoyWi8VZN%2BHJ0CqMaokThj9bVJ3usreZFujdYKkojjgcuz6aJh%2BDHbkta7oTh6K28WrVE5LceFMpAfEGQ8yBtisuQpnv%2BC68OqHKfeh%2BIb5lHABR%2FS7RZMAFJswhYfD9vUwarepuRq7giVCqVMvIrpi2e%2BcDVSR%2BzPKG%2F%2FWRUJHN4ePjJLjuAptCBjakTTLX%2FYtHJbgPxt31pBw%2BXKdSRtcDAvbfmTaLnVZvc2DldwfriYhFdVr8o8fZb3jgF10yJj%2BVU1fczlBxDWAf%2BaTqbCsVdUTG3twORE18gF5GZGhcVlFV5ONM0YZtejh7gcSMIO%2FhNMGOqUBEbW21mQ%2FgrzKVj2bXkLKN%2B8mx6flB2FXu5QHF9uzw2JpOmF8NKIbGoNInprH9Ubt6rf26IELRP9TVowtNjZa8bBmEPIq0ebNV4yYySOuhA3YcHkA773MXLSpqfWShtZzXxyuyYS%2FCBrcml5GK8rcVTU8BlTE%2BvQ1dwjxlHscLZUo0zodCY86a%2BPMKk9i1B6bikENHd2Dk07j8OhTFEiZY4j1J6uy&X-Amz-Signature=ce948a7ec5919ce121f9a437188153ba20d4605f063b1c248577f29a244a0bc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQCZNM2N%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T225158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCbvStofHycOr8WLADVWoN8Yp3rpzLOndKsYf4F1RFFrgIgZm8AXhAbYk2tfqpYHsVNZ8UYUi9A8YCSsglCoifH5D8qiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJK4QVHMEwT%2F5xRlLCrcAxDHyvIpEzRisaxTNYe0gCROxShHwkauzY%2B6JuA8JryRgf5mz%2FdOLOPBFYWy%2BWWjSquYeUkLO4mDhfM8PViV%2F0%2F7HcaYrBgmVFOm8ugAfv%2Bz6ryzOCPzJWTlRCrXMuJpdvxa3S%2FEiOc0B3Z140CvDs7JHgibFjr72I0bTIv53VYaTLjMhVgupp%2BoHRRyom%2Bxt7zwcjIRRBU9OZphPbwg2P46i9NkV1w9qHkYqircXKc4k15nwOrHHjKqvU%2BphiMS1Cj%2Bugwi6J7IrhHCtnwoVC%2Fan6frMVab53wNdXc0wcGh0EawnAC2HQJjiTg0rYoyWi8VZN%2BHJ0CqMaokThj9bVJ3usreZFujdYKkojjgcuz6aJh%2BDHbkta7oTh6K28WrVE5LceFMpAfEGQ8yBtisuQpnv%2BC68OqHKfeh%2BIb5lHABR%2FS7RZMAFJswhYfD9vUwarepuRq7giVCqVMvIrpi2e%2BcDVSR%2BzPKG%2F%2FWRUJHN4ePjJLjuAptCBjakTTLX%2FYtHJbgPxt31pBw%2BXKdSRtcDAvbfmTaLnVZvc2DldwfriYhFdVr8o8fZb3jgF10yJj%2BVU1fczlBxDWAf%2BaTqbCsVdUTG3twORE18gF5GZGhcVlFV5ONM0YZtejh7gcSMIO%2FhNMGOqUBEbW21mQ%2FgrzKVj2bXkLKN%2B8mx6flB2FXu5QHF9uzw2JpOmF8NKIbGoNInprH9Ubt6rf26IELRP9TVowtNjZa8bBmEPIq0ebNV4yYySOuhA3YcHkA773MXLSpqfWShtZzXxyuyYS%2FCBrcml5GK8rcVTU8BlTE%2BvQ1dwjxlHscLZUo0zodCY86a%2BPMKk9i1B6bikENHd2Dk07j8OhTFEiZY4j1J6uy&X-Amz-Signature=d656f9ba10c97e9b8997da05e83fcfceddff5dfd33788454fd1f3c92c8f41319&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
