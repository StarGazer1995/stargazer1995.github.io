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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVHV2K7J%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T080421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIDGbnPzfoMvEJ9tR9%2BPemYLC7tz0gDrwl3yWoz10OWWDAiEAgfogaXzFjAOaR2S2TImTXUOY1ip5TRDvRZ4%2FCXkg1Roq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDFAcXGVOBhFRCxMrNyrcA50ycCDs%2FgrNfjCACZnlTRlWqznffliVBfZPVYJKbVYtxqFlSviqBMvH3011TR1K%2BpyabNvR8D80U2ipLtcZYOz5AuXXIIOOYt65qOtUBZJyHhtQKqhWQuu1wsyAEiYvWCKMlYLKSEbh%2F6xXMKQkefKEie30GMRr6DBqaaBN5ACaD1ayvMPx1ERmQjyP4m2JViz0WCClndLphOEqmrRmpTHnUemyID3BM3P5kf%2BObz9n1uQ66DyMFfC07wFf3fnHLrnRvBKHKvSXRggOxf8ahBhTfpA8PFb3L9FjOI7iIuslU7wkjuo2HS3SVL00l8ltWCNElpbA0wk69wuocQpRKrW4zp35m%2BNadGbcPc64DdQxzkdWeIdGUAZMU0VWv2nkYUwIa%2FAggJt4PlcefqadoF6sCQZA%2Bz9gyEcYVNB%2B3G2BDOZR7nWEJjKf6yXm%2FgWYU1ViR3OY10kS8i%2FJCgJjGg9EkATT3y%2B5yRN6p0KDmKzYfMzjUzmByPrFIZEDgtTNDcY5LTH%2B9SXpTN7p%2FQohqfDjuNfYvbmA6PCvMTQceslYknQI609j7fWNzk3r2x%2FEHZvv4WTYZAsrvOMKDtSPHabDLtfR0PflcONGUA%2FE6%2F6nZYfPJlWcG%2F5toJxIMJ%2F5ltMGOqUBWQCmRv7XH94lr%2BlxmFTT%2B74g8NIZjp1nIG0wwQzNqccyTImCeI7z2YtpeXM5LjwR3p4AEvlBEz9Kx%2FlOjchEhDwLZimY9tCUqhIj7uIDt8BzDJuw3%2BtT8%2Bv2V3q5pn9j3ukIrE5panm1r6H4%2FA%2FuVyK1Ff6g%2FaE0Z34Yau7KU5YWMVpIhFPQT6zmMOX76bJhlpCiORTo0waEapy%2BKYVMHiwQINyk&X-Amz-Signature=a07438fada8881f6cd613a5a5411d77f8412b69539214d8dc48d03c917164607&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVHV2K7J%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T080421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIDGbnPzfoMvEJ9tR9%2BPemYLC7tz0gDrwl3yWoz10OWWDAiEAgfogaXzFjAOaR2S2TImTXUOY1ip5TRDvRZ4%2FCXkg1Roq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDFAcXGVOBhFRCxMrNyrcA50ycCDs%2FgrNfjCACZnlTRlWqznffliVBfZPVYJKbVYtxqFlSviqBMvH3011TR1K%2BpyabNvR8D80U2ipLtcZYOz5AuXXIIOOYt65qOtUBZJyHhtQKqhWQuu1wsyAEiYvWCKMlYLKSEbh%2F6xXMKQkefKEie30GMRr6DBqaaBN5ACaD1ayvMPx1ERmQjyP4m2JViz0WCClndLphOEqmrRmpTHnUemyID3BM3P5kf%2BObz9n1uQ66DyMFfC07wFf3fnHLrnRvBKHKvSXRggOxf8ahBhTfpA8PFb3L9FjOI7iIuslU7wkjuo2HS3SVL00l8ltWCNElpbA0wk69wuocQpRKrW4zp35m%2BNadGbcPc64DdQxzkdWeIdGUAZMU0VWv2nkYUwIa%2FAggJt4PlcefqadoF6sCQZA%2Bz9gyEcYVNB%2B3G2BDOZR7nWEJjKf6yXm%2FgWYU1ViR3OY10kS8i%2FJCgJjGg9EkATT3y%2B5yRN6p0KDmKzYfMzjUzmByPrFIZEDgtTNDcY5LTH%2B9SXpTN7p%2FQohqfDjuNfYvbmA6PCvMTQceslYknQI609j7fWNzk3r2x%2FEHZvv4WTYZAsrvOMKDtSPHabDLtfR0PflcONGUA%2FE6%2F6nZYfPJlWcG%2F5toJxIMJ%2F5ltMGOqUBWQCmRv7XH94lr%2BlxmFTT%2B74g8NIZjp1nIG0wwQzNqccyTImCeI7z2YtpeXM5LjwR3p4AEvlBEz9Kx%2FlOjchEhDwLZimY9tCUqhIj7uIDt8BzDJuw3%2BtT8%2Bv2V3q5pn9j3ukIrE5panm1r6H4%2FA%2FuVyK1Ff6g%2FaE0Z34Yau7KU5YWMVpIhFPQT6zmMOX76bJhlpCiORTo0waEapy%2BKYVMHiwQINyk&X-Amz-Signature=1c7618a54e161dabee0fc1500f011fc7ab9668e3c8a50475240d6de590a10930&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
