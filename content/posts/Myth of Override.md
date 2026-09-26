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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWDPWZF7%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T021738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIC2KtgVLPRz0qhPsDoWQVPm8L%2BBWfRjJYpqfzPSDKtwDAiEAjLlaC2gEH70Vg3JF7YWzG2TCcBovY5EKJo39HLuFhrYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEPt9BgsfYjXQjnkvCrcA4lbV2KaGLfOZpJnil26oDqIH4z2l7YJsVMXtCaD7%2FUY2ifZhAtUIt0FQjr5i1d5UghQ%2BY9QUUBBXXU7BAt0Qcs0DVlUEuKteuEXyX%2BCR0Hd1yJ9%2BedG1Es7O5oZWaqbRUPos1i5ox2U%2FEEmMgoYJrDyLsp75CUigakCyp7nm%2FBoBlixGWPiC7pDty1%2Bds9sm5WPLUyAvVnDfYpI6Ajrlsxb5GpmP6PFZ9NpOfr8yb3X14JZ8MoNoOlTBgdqKBkbG0DfkW8r%2BowT%2F4kTtzUgHeupaRlCE5jiQdpFnsrBW9F1XGtkliz3gNCtCTE3noB16XbeUPNFlNOLaVRAw44ve2t3AjriOJkhQm2GWwbX5CReLbeIJvgpjd2m6p01Sd7KLQTrjfQRvkgX4SwQQlelWVI%2FEww7hHCP2l6tZvG5tjiEQF2cio1YZpysD7OzhhqtP3xAi574HFdxR4hS8e8m7PPsZY5k%2FUD1LwJa4v4ibM28yfKUiQ1n4eGay8odWRohl6hrIZ3WMOPbTvrvJVb2YtEvfLOK%2Bt5y3Oo9IKWk6FRTYk4Hzq4GMa1dowsky%2Fh2Dhz0mJ18qdGk7VZCsNljf5S8al53kNPAnLG2Rzm%2Fj1XPZ%2FZ4eQiS%2FEd97YqRMKfJ3NUGOqUBriLCClNh%2FF7TNpj6knJMwzGmbF5bsuLowVUNyBzNOYRip7pXCdos0GVuKLgfT%2FVeq4DSgossYHMHnYLt%2F9sgfP8fYvUvFe3YY8Jq15X%2FZs%2Fweu687GzbI4U3Arr3hq1UQ49JtBGMVVobA4EoFv0mHoqBH8ofpBg0KX%2Bpd0MJe09N%2BmPF2CJzxdqWPWwyv8RA0D1W3pBl59CpP0s5a7Oc%2Bm8vZq%2Fy&X-Amz-Signature=56188303898a9591580fa239a58c8fa89e05b685055bc4117a4007e0b5433264&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWDPWZF7%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T021738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIC2KtgVLPRz0qhPsDoWQVPm8L%2BBWfRjJYpqfzPSDKtwDAiEAjLlaC2gEH70Vg3JF7YWzG2TCcBovY5EKJo39HLuFhrYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEPt9BgsfYjXQjnkvCrcA4lbV2KaGLfOZpJnil26oDqIH4z2l7YJsVMXtCaD7%2FUY2ifZhAtUIt0FQjr5i1d5UghQ%2BY9QUUBBXXU7BAt0Qcs0DVlUEuKteuEXyX%2BCR0Hd1yJ9%2BedG1Es7O5oZWaqbRUPos1i5ox2U%2FEEmMgoYJrDyLsp75CUigakCyp7nm%2FBoBlixGWPiC7pDty1%2Bds9sm5WPLUyAvVnDfYpI6Ajrlsxb5GpmP6PFZ9NpOfr8yb3X14JZ8MoNoOlTBgdqKBkbG0DfkW8r%2BowT%2F4kTtzUgHeupaRlCE5jiQdpFnsrBW9F1XGtkliz3gNCtCTE3noB16XbeUPNFlNOLaVRAw44ve2t3AjriOJkhQm2GWwbX5CReLbeIJvgpjd2m6p01Sd7KLQTrjfQRvkgX4SwQQlelWVI%2FEww7hHCP2l6tZvG5tjiEQF2cio1YZpysD7OzhhqtP3xAi574HFdxR4hS8e8m7PPsZY5k%2FUD1LwJa4v4ibM28yfKUiQ1n4eGay8odWRohl6hrIZ3WMOPbTvrvJVb2YtEvfLOK%2Bt5y3Oo9IKWk6FRTYk4Hzq4GMa1dowsky%2Fh2Dhz0mJ18qdGk7VZCsNljf5S8al53kNPAnLG2Rzm%2Fj1XPZ%2FZ4eQiS%2FEd97YqRMKfJ3NUGOqUBriLCClNh%2FF7TNpj6knJMwzGmbF5bsuLowVUNyBzNOYRip7pXCdos0GVuKLgfT%2FVeq4DSgossYHMHnYLt%2F9sgfP8fYvUvFe3YY8Jq15X%2FZs%2Fweu687GzbI4U3Arr3hq1UQ49JtBGMVVobA4EoFv0mHoqBH8ofpBg0KX%2Bpd0MJe09N%2BmPF2CJzxdqWPWwyv8RA0D1W3pBl59CpP0s5a7Oc%2Bm8vZq%2Fy&X-Amz-Signature=08f003f1a63180460e95c258a8d161eaf80e6c1874b63642d0bed633ceceb4c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
