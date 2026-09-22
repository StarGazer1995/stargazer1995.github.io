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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUC22LW2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T203559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc9DRWy3KFN78Do0wvAdOwV71s7Y6St0W5YacAc6i0%2BwIgcYtqFEQKEbr1n6BKjisIXnnVneHFe2Sfn5DkCYET4bEqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMl862UOyVtrtasdkSrcA07n54UIjqG%2BNV86yheC18bxWwSkvTCGGb0ldvzQhiAz5oOncDZ1wSp2MwObQ%2Fi40l6F1bVy0wRXfLvFraMOf8yPSCRmZaauP3FPCA0GqhIhuon1xnUAeyF6twIPn77dZ8GzhKuVyNEEuUVnaQj72rSBVS504tm4WQEDtkfU2pU8%2FG00rpaNspATA0clgSJITunEJn3lkx45q81hFMWQd%2BXRlbTNaOG%2Fws4m1Y0W907x5f4o0SSeQ0PmmHwyXYCE87TH1skFRbiLl9nFNnq2F80lEbsL7Jst4MB5ln463K4BplD%2BhlaMU3AT5T9iAp5qCFmILCYShKHFVAISFOau0Qm8D1DNFReoysc5GsHkpMxRk%2BIQH7RLQipCtgjPKbNPSnvE6W%2FaJ4y7Hch%2FDy%2F1jqbiPrFaoqzTKKz8a6QvKQfbwxGsEoQoGwTXsjY5sEqCbJZ2EmtgZo9jRPqMzcIVOyhDZS03xNB7CJiiG4kX8n2TW4hYgVbj%2B8RwTAUaPqxGL%2FvJLxQwiAsSGJj%2FXsiazB4a%2FyUqwC%2BTE6y18qyfkbMpCe8zzL3dFNLEmx24oi3LvZZiLqVPGguKFkLXh0Kw9XFcJ5j4M%2Bq%2FRm2XkmHlZoe2kIzkSMWqxTgMdTo7MK3LytUGOqUBoaRSLBmAzLyrk4vn95lbqN9BINee8TZ8E89LSKomxXXIsNkgl3n9YxeRCvOMN8JlBm%2FXugOsDUcG43BWKH4s6ZIwi2KkvMYXHIM6RSHIiMx9J%2FpFoI36e7R%2Bn4LdhWi1CF%2FP6WBgrvtit%2FDiaYr7kTNCv77bg2zul7QaWyMzMwjYFlTrjbA8LyrQRwZ4xGtFyh84S%2Fi1eVD9ZUwKeCB08alqJeO%2F&X-Amz-Signature=1ef4f0173f2749ea458f46257c725c227c0aceda142b5f534c2fe7a7ca20cd9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUC22LW2%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T203559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc9DRWy3KFN78Do0wvAdOwV71s7Y6St0W5YacAc6i0%2BwIgcYtqFEQKEbr1n6BKjisIXnnVneHFe2Sfn5DkCYET4bEqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMl862UOyVtrtasdkSrcA07n54UIjqG%2BNV86yheC18bxWwSkvTCGGb0ldvzQhiAz5oOncDZ1wSp2MwObQ%2Fi40l6F1bVy0wRXfLvFraMOf8yPSCRmZaauP3FPCA0GqhIhuon1xnUAeyF6twIPn77dZ8GzhKuVyNEEuUVnaQj72rSBVS504tm4WQEDtkfU2pU8%2FG00rpaNspATA0clgSJITunEJn3lkx45q81hFMWQd%2BXRlbTNaOG%2Fws4m1Y0W907x5f4o0SSeQ0PmmHwyXYCE87TH1skFRbiLl9nFNnq2F80lEbsL7Jst4MB5ln463K4BplD%2BhlaMU3AT5T9iAp5qCFmILCYShKHFVAISFOau0Qm8D1DNFReoysc5GsHkpMxRk%2BIQH7RLQipCtgjPKbNPSnvE6W%2FaJ4y7Hch%2FDy%2F1jqbiPrFaoqzTKKz8a6QvKQfbwxGsEoQoGwTXsjY5sEqCbJZ2EmtgZo9jRPqMzcIVOyhDZS03xNB7CJiiG4kX8n2TW4hYgVbj%2B8RwTAUaPqxGL%2FvJLxQwiAsSGJj%2FXsiazB4a%2FyUqwC%2BTE6y18qyfkbMpCe8zzL3dFNLEmx24oi3LvZZiLqVPGguKFkLXh0Kw9XFcJ5j4M%2Bq%2FRm2XkmHlZoe2kIzkSMWqxTgMdTo7MK3LytUGOqUBoaRSLBmAzLyrk4vn95lbqN9BINee8TZ8E89LSKomxXXIsNkgl3n9YxeRCvOMN8JlBm%2FXugOsDUcG43BWKH4s6ZIwi2KkvMYXHIM6RSHIiMx9J%2FpFoI36e7R%2Bn4LdhWi1CF%2FP6WBgrvtit%2FDiaYr7kTNCv77bg2zul7QaWyMzMwjYFlTrjbA8LyrQRwZ4xGtFyh84S%2Fi1eVD9ZUwKeCB08alqJeO%2F&X-Amz-Signature=a4b04af98733ba39a5026f79e572619ee5d3865297484322d2f60df9a349bffe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
