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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NLSB3KQ%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T111035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcPQihqzGH%2BJgMdAMkLEZgycmvdMgEwzvDemyWZSN6zgIgBo3RJ3JHR9m6lmUs3EsFPNEUa2DHChbCHPcnr3U38JIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAECaneKNke2eN4uoircA3XQ%2FxMYldjAfSPCgFvicRkmgZqoK%2FYoOMiRC8cw73t9zAlXPOfOJjzIJ%2Bn3ivuRgvUrCsj%2FIQfor6sQH5iX6YdLaKbWT%2BKL2hpKHPEv47D8bzrnSws65cSEt5NE65oiLjR1hvK679lK0xgQzAbi%2FYocDbk1XXTaX%2B%2BQGLs3ZPRNGP0plYt8qnGo%2F9s4uYvI%2Bx%2BgY5Y32MEU139YCdwX3b%2FffwFqYrIkQzc3soAB%2B6OxV%2BfOnL%2BN2TiiP2kXvU5mWcvZh5VUdaCzw3y5aicbQTYefq7vfjIUaw84PWk7tQeY5dLxSFr%2BM29webe%2BVJZiOcqIiMd9R5XRX5imQ3O1dxiIWKtyzd1DlOm3%2F%2Fu%2FyHi078VfOUrvghj%2FPISraLn2TMUi35PqYKCMevrKqlVsnMdcI4SK9%2BmDuoGzmcVrCbIU5DNBhafuFHl0sF96DMMtrTK%2FO1cw%2FJKyBcm0Q3HOvAyZGUCuCaJSZp05ZXmTasbUCxpj3zEyYkS%2F9p%2FfxJT6IPD1yiKRDlE%2BWF%2BFzsU%2BX6f38xG7nxXtayRYxE9x%2F5WvTrK8%2FjvqS7dMtDkSMsrWCs%2FbjS3ATWEl5UugaNSweSfS8PgqJDzlmP6mnnLcixLCM1ECFN5dH%2BOanuvPMML3ttMGOqUB47QPFoYOyLmVuQelreiIbtaHb11D5%2FwH9VUA4zliiaZnoDT25VhQvtAgI5KrzUcRvdutFcbL100Do1TwTGCy40TPwnqsdOmASAa51d6KZ%2FP6X92BHlEtytBwVqv00G4jjOyhPYuHOmmMNs2wwB4IlBtmm%2BJFUz7v1Ym7NTjJrMmViIfQYeruoIAP6i%2FfrHXRYojxbvwGo2Cywb5Z96vOQJMnNxbk&X-Amz-Signature=d37a4b7ecfd014efedf0a37464ec14973120a570b92acbbd968b2e3b2ef9fc36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NLSB3KQ%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T111035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcPQihqzGH%2BJgMdAMkLEZgycmvdMgEwzvDemyWZSN6zgIgBo3RJ3JHR9m6lmUs3EsFPNEUa2DHChbCHPcnr3U38JIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAECaneKNke2eN4uoircA3XQ%2FxMYldjAfSPCgFvicRkmgZqoK%2FYoOMiRC8cw73t9zAlXPOfOJjzIJ%2Bn3ivuRgvUrCsj%2FIQfor6sQH5iX6YdLaKbWT%2BKL2hpKHPEv47D8bzrnSws65cSEt5NE65oiLjR1hvK679lK0xgQzAbi%2FYocDbk1XXTaX%2B%2BQGLs3ZPRNGP0plYt8qnGo%2F9s4uYvI%2Bx%2BgY5Y32MEU139YCdwX3b%2FffwFqYrIkQzc3soAB%2B6OxV%2BfOnL%2BN2TiiP2kXvU5mWcvZh5VUdaCzw3y5aicbQTYefq7vfjIUaw84PWk7tQeY5dLxSFr%2BM29webe%2BVJZiOcqIiMd9R5XRX5imQ3O1dxiIWKtyzd1DlOm3%2F%2Fu%2FyHi078VfOUrvghj%2FPISraLn2TMUi35PqYKCMevrKqlVsnMdcI4SK9%2BmDuoGzmcVrCbIU5DNBhafuFHl0sF96DMMtrTK%2FO1cw%2FJKyBcm0Q3HOvAyZGUCuCaJSZp05ZXmTasbUCxpj3zEyYkS%2F9p%2FfxJT6IPD1yiKRDlE%2BWF%2BFzsU%2BX6f38xG7nxXtayRYxE9x%2F5WvTrK8%2FjvqS7dMtDkSMsrWCs%2FbjS3ATWEl5UugaNSweSfS8PgqJDzlmP6mnnLcixLCM1ECFN5dH%2BOanuvPMML3ttMGOqUB47QPFoYOyLmVuQelreiIbtaHb11D5%2FwH9VUA4zliiaZnoDT25VhQvtAgI5KrzUcRvdutFcbL100Do1TwTGCy40TPwnqsdOmASAa51d6KZ%2FP6X92BHlEtytBwVqv00G4jjOyhPYuHOmmMNs2wwB4IlBtmm%2BJFUz7v1Ym7NTjJrMmViIfQYeruoIAP6i%2FfrHXRYojxbvwGo2Cywb5Z96vOQJMnNxbk&X-Amz-Signature=5d3df0b7b2346145e336f2effa78fd53ee392bb2544d601ab52c1e002a5f9a95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
