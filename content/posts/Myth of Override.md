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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QICCPIS%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T074147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNLYnltAmN6MCqWl6OgCgaDTKfA9Er0u%2FW316xACKWzAiEAtEHzk1LJ%2BghH0%2FWyPvfRiKfFSJpWwu6nIGfDmAp0GnAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJpwbB5Nu2ZmKMPjFCrcAwroFOzHmYVVMcCsHN4hfbQn7K3kuPeoHmtHdt5Z4ODwp%2Fnaj%2BhrS%2ByFnR3O%2Bm6GyuJvwUw%2FzTWn2wm%2F4VnPGpsw8n01VTNDFNNsIvKFQGVeYX%2Fxh%2BWqXk1IUeYIyDbD9fhZnpLANxKmq9pgDp79hrf7S74CEXU7N4b4gXjHt1TPYf%2Fzw%2B7mx83lYG86JgF%2BJ4oG3D2%2B7R%2B9q1C7%2BZ2qid5JKerBuPeKQFOm%2Fq4Kz5bZgzUGnNGURA7moRZUOoaWSfD1D%2BOVctGNZA%2FnRFSYNOzzNdOL50bngA72ytRT4%2FwXlo1j1dg%2B2tYrDH%2BK%2F0tRLCGtHv9jl%2Bxq81O1WqzSSA2YQYvjo0p%2Bvf%2BymvVDs86A4FlIXXYE9T%2BFR1QK%2F3qBGaGbdTvV2RYBNgy1f6kmXBcDoOF4zAU71ZcCQ7rbTG3tDgJ5z97liyka7Igguivt1RMIvam%2BJ%2BHxWgaY42b8xh7T2DliAwG56LKEsk4yooaAaHkY%2BT6TzXIWlVNqp1F7xaJlLUcIRURjwFFPN9tQ7eQkhFIvO9ezbulmiPqbTgb7F5P1Z5LWMwzeWVI6cBz8XPi4w0XojLh2m169pZSPPBlgKRstiSAIhw4GPf8zriSh8iU0fwUFXTYROozcMP%2FI%2BNEGOqUBCxCWgV3YlccabCkeoWx08kyTTxCuYoOvEc2UQWm3Ha%2F8I3h6amDgbvOea2s4cVF%2B97Uw%2FbFThlFUD%2BxWuoWhhfjFq2mEAsWBGFihJbHd8e40BbPbMsKPT%2Fg3EC%2BPbz%2Fma%2FIKlTTbQcCOCz0gP2DZecKkwjlbT%2FAu9DQ2Ievrqea5QrrmN0s5CVR5jabMhujYdktTFqPE4om%2B40hbgdAMnrqak5oo&X-Amz-Signature=e53ceecd04a783a583e55974ccb878a8f576ab3cea83877aaa431a9ad88be1ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QICCPIS%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T074147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNLYnltAmN6MCqWl6OgCgaDTKfA9Er0u%2FW316xACKWzAiEAtEHzk1LJ%2BghH0%2FWyPvfRiKfFSJpWwu6nIGfDmAp0GnAq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJpwbB5Nu2ZmKMPjFCrcAwroFOzHmYVVMcCsHN4hfbQn7K3kuPeoHmtHdt5Z4ODwp%2Fnaj%2BhrS%2ByFnR3O%2Bm6GyuJvwUw%2FzTWn2wm%2F4VnPGpsw8n01VTNDFNNsIvKFQGVeYX%2Fxh%2BWqXk1IUeYIyDbD9fhZnpLANxKmq9pgDp79hrf7S74CEXU7N4b4gXjHt1TPYf%2Fzw%2B7mx83lYG86JgF%2BJ4oG3D2%2B7R%2B9q1C7%2BZ2qid5JKerBuPeKQFOm%2Fq4Kz5bZgzUGnNGURA7moRZUOoaWSfD1D%2BOVctGNZA%2FnRFSYNOzzNdOL50bngA72ytRT4%2FwXlo1j1dg%2B2tYrDH%2BK%2F0tRLCGtHv9jl%2Bxq81O1WqzSSA2YQYvjo0p%2Bvf%2BymvVDs86A4FlIXXYE9T%2BFR1QK%2F3qBGaGbdTvV2RYBNgy1f6kmXBcDoOF4zAU71ZcCQ7rbTG3tDgJ5z97liyka7Igguivt1RMIvam%2BJ%2BHxWgaY42b8xh7T2DliAwG56LKEsk4yooaAaHkY%2BT6TzXIWlVNqp1F7xaJlLUcIRURjwFFPN9tQ7eQkhFIvO9ezbulmiPqbTgb7F5P1Z5LWMwzeWVI6cBz8XPi4w0XojLh2m169pZSPPBlgKRstiSAIhw4GPf8zriSh8iU0fwUFXTYROozcMP%2FI%2BNEGOqUBCxCWgV3YlccabCkeoWx08kyTTxCuYoOvEc2UQWm3Ha%2F8I3h6amDgbvOea2s4cVF%2B97Uw%2FbFThlFUD%2BxWuoWhhfjFq2mEAsWBGFihJbHd8e40BbPbMsKPT%2Fg3EC%2BPbz%2Fma%2FIKlTTbQcCOCz0gP2DZecKkwjlbT%2FAu9DQ2Ievrqea5QrrmN0s5CVR5jabMhujYdktTFqPE4om%2B40hbgdAMnrqak5oo&X-Amz-Signature=940f76553f1669dcf972ac1a6e12dfee0780a0dc8e6e226c1a5462cb0d32fd97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
