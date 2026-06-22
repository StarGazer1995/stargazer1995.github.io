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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP36FM5Z%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T231146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIDxACl%2B0tRGiZ2zq1sZ4eB2QjMLXjLtUhfhGfcq%2FVMQiAiEAr9IOjRS65V7LzX%2FRjo7AncS7tQMb8F9p7RrKj3XS64Aq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDBrDJrB8h%2BX86ANpxCrcA1NhHdFsJfGcRaRSRg2z9YpSTn%2BkGBdKs0qlcAfDsfMCRpjadrn0K0AYw2K545O1uouxfPRUUR5BvBFM9VcQ5ZiGiKjl2F%2FyK%2FjJbiIAnG%2BQfWDWJML9z%2FW3780vPGWzUZtOhRvZ%2B3pS8QBRPlIpIVNQBBKNulcw8OTqG9RKAKMgO0h8l8x4k6%2BD4jxNpuosScxmjdBKbBNTh2brYWmcOQ6mBenKK%2FKHB1K0wuNvcnYTLGffpZr22pRO8v0kbXA68JrzJ31o%2FzkjlA04376McjOqwiGIrr3ppfxM1%2FadpC7tn84S83TTm62zYf7cWwYvHIjKxqiulloBDgT2yIO4aVcQrEg9O7b5BJIlv6%2BQPVS5DHe3O7Z0PV%2FFifZlhX1vR%2FVLl2RI6KD%2FUkAcrTyazpt1YsMHAjR3u95C7YSkl%2B7EsWIBKzojeaN0EaywTzZ%2FvRxGH4cJOx%2Bbf3mBdIROm3eKVfguwy3ya0hDH6iVikZqjkVtXUkeYmVxBLESpRg%2FGt4qY0kJOE5ZIKUttXzR17mLNh1ZKoguqFOy9ck%2BYCuVVbu6KQKvjc7oJrt0rSkZxnnD6qw8L2BFRKbnuD2N%2BD1%2FWqfNN5Jn15bCFDrW00A9ytcRdKyMljip%2FzkrMPuO5tEGOqUBBBisQz1Uiz21k8S%2FpDb5O1zm%2BH0cx%2F4CJ98l4YUBpDdrsGMFMIcbhiTsZc%2FZjozeHKXUnQBHAofjduNoJ9mhEuLK%2F0%2FpZyh70c6BrY9rsNjwqim3gBVK3pyUfjP2d3JB1Ssga4mZt9pDVfMP8Q%2Fi0KsrXWR4S1KvnEa6bIG7rkFamAM%2Fnqozxuy91n32ueCfOrxn9gPVrEsNQzmRvHKws5rZW49W&X-Amz-Signature=9d34c6a9a89165705790fe9da4df832079c63b7aac59aa6feebd92c95abd5fad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP36FM5Z%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T231146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIDxACl%2B0tRGiZ2zq1sZ4eB2QjMLXjLtUhfhGfcq%2FVMQiAiEAr9IOjRS65V7LzX%2FRjo7AncS7tQMb8F9p7RrKj3XS64Aq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDBrDJrB8h%2BX86ANpxCrcA1NhHdFsJfGcRaRSRg2z9YpSTn%2BkGBdKs0qlcAfDsfMCRpjadrn0K0AYw2K545O1uouxfPRUUR5BvBFM9VcQ5ZiGiKjl2F%2FyK%2FjJbiIAnG%2BQfWDWJML9z%2FW3780vPGWzUZtOhRvZ%2B3pS8QBRPlIpIVNQBBKNulcw8OTqG9RKAKMgO0h8l8x4k6%2BD4jxNpuosScxmjdBKbBNTh2brYWmcOQ6mBenKK%2FKHB1K0wuNvcnYTLGffpZr22pRO8v0kbXA68JrzJ31o%2FzkjlA04376McjOqwiGIrr3ppfxM1%2FadpC7tn84S83TTm62zYf7cWwYvHIjKxqiulloBDgT2yIO4aVcQrEg9O7b5BJIlv6%2BQPVS5DHe3O7Z0PV%2FFifZlhX1vR%2FVLl2RI6KD%2FUkAcrTyazpt1YsMHAjR3u95C7YSkl%2B7EsWIBKzojeaN0EaywTzZ%2FvRxGH4cJOx%2Bbf3mBdIROm3eKVfguwy3ya0hDH6iVikZqjkVtXUkeYmVxBLESpRg%2FGt4qY0kJOE5ZIKUttXzR17mLNh1ZKoguqFOy9ck%2BYCuVVbu6KQKvjc7oJrt0rSkZxnnD6qw8L2BFRKbnuD2N%2BD1%2FWqfNN5Jn15bCFDrW00A9ytcRdKyMljip%2FzkrMPuO5tEGOqUBBBisQz1Uiz21k8S%2FpDb5O1zm%2BH0cx%2F4CJ98l4YUBpDdrsGMFMIcbhiTsZc%2FZjozeHKXUnQBHAofjduNoJ9mhEuLK%2F0%2FpZyh70c6BrY9rsNjwqim3gBVK3pyUfjP2d3JB1Ssga4mZt9pDVfMP8Q%2Fi0KsrXWR4S1KvnEa6bIG7rkFamAM%2Fnqozxuy91n32ueCfOrxn9gPVrEsNQzmRvHKws5rZW49W&X-Amz-Signature=bebd09b25867ae3f17b078f1799c48de29c71a699f6fbd4ee6780f04eeafce34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
