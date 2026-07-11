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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q23DW3G7%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T073048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3MEiyB4qOiW4qFKtZQt8QjVRwjmDndRg9EYTOYq9b8gIhAN5TYO9L9TVzc9ucGGxEsFeZb7cNvqyZYPVOfDHMwf%2B4KogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdNptrnDEqZChC9Swq3AObhzldeI4xrxCr62Q2algOlN6ueDP7wQs4a5fuLx91O1aV%2FIWN6ei%2FWd3wOFZexN38Fmj8lKffcKVweZf4n92uIte7CARPTmBfG4mn3TuxH3F49IoPy5zgegW7BTF7eKD58rVQO%2F4NwWVKEMGozqj1u%2FI9907w9gvJS2DPrQXJVE879GLsAr4%2FXwFN7LffAS1f2xUNpjGGa1abdbmESFS%2FQ5ez%2Fd%2FgJaHEaMSIFVj%2BScskHs5nKLyQ9NzaMC%2F1b2hG%2F6v9XxxwVVkwni5zJk1PPL8TInh7EVaU%2FICk4VyRw2N6BWVsHgc0MByg0mObwckBINnjUZGdFI92Lgb4%2BeG18SgXflU26GpmPCqwN%2F%2FH%2BBUk11kBm%2F20R%2BWCswUG3yL%2B1hdP7f5zmv%2B%2BQa0urCsHxGj6d4%2FSUjZ5dRIT3lCrMIv17viE3mIAl6AZMBUZOT29%2FJmiUHb7U0zou553GPErAiHKATJtNatwyjCB9OIkQ4Ee1hcVoOCkeIJzzceJVR6josZuLeKbhv4Tj4N%2FgZNcNJ19au3cvZqI6JGMVR1rRpkaHA30HU0Bc2qnl%2FyvZEZAAUU1rNr1kfv%2BHInijq5rmr406Beo3FjtBVZw1sYjKw4BBGpr2bQwkOhPdzDWwsfSBjqkAVD3pcvJ%2FQxDE2FC%2BsSxSA5IL8uvqFHfoOoPl63Wt%2BrGOyfIBADNgAOag3ULZziV2ZXJB5znkM1s0%2F5p6YeRWtSz%2F3osfniZQfq36MScEE1woDuAbXxvKtGY2%2FYguy%2BF67SMJhPOd9EWGUqwpSfJGLPGIqkHXWzj3CbDJNAzc8aF0XPWVZpDKoZvuDfFhe3igFXO5%2FG5NzV850t8Q9%2BaoYlNLa72&X-Amz-Signature=044248ca0f965c78efeee8e3810a9203932476c5f7a418e8d5bfe0c1b9b70399&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q23DW3G7%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T073048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3MEiyB4qOiW4qFKtZQt8QjVRwjmDndRg9EYTOYq9b8gIhAN5TYO9L9TVzc9ucGGxEsFeZb7cNvqyZYPVOfDHMwf%2B4KogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdNptrnDEqZChC9Swq3AObhzldeI4xrxCr62Q2algOlN6ueDP7wQs4a5fuLx91O1aV%2FIWN6ei%2FWd3wOFZexN38Fmj8lKffcKVweZf4n92uIte7CARPTmBfG4mn3TuxH3F49IoPy5zgegW7BTF7eKD58rVQO%2F4NwWVKEMGozqj1u%2FI9907w9gvJS2DPrQXJVE879GLsAr4%2FXwFN7LffAS1f2xUNpjGGa1abdbmESFS%2FQ5ez%2Fd%2FgJaHEaMSIFVj%2BScskHs5nKLyQ9NzaMC%2F1b2hG%2F6v9XxxwVVkwni5zJk1PPL8TInh7EVaU%2FICk4VyRw2N6BWVsHgc0MByg0mObwckBINnjUZGdFI92Lgb4%2BeG18SgXflU26GpmPCqwN%2F%2FH%2BBUk11kBm%2F20R%2BWCswUG3yL%2B1hdP7f5zmv%2B%2BQa0urCsHxGj6d4%2FSUjZ5dRIT3lCrMIv17viE3mIAl6AZMBUZOT29%2FJmiUHb7U0zou553GPErAiHKATJtNatwyjCB9OIkQ4Ee1hcVoOCkeIJzzceJVR6josZuLeKbhv4Tj4N%2FgZNcNJ19au3cvZqI6JGMVR1rRpkaHA30HU0Bc2qnl%2FyvZEZAAUU1rNr1kfv%2BHInijq5rmr406Beo3FjtBVZw1sYjKw4BBGpr2bQwkOhPdzDWwsfSBjqkAVD3pcvJ%2FQxDE2FC%2BsSxSA5IL8uvqFHfoOoPl63Wt%2BrGOyfIBADNgAOag3ULZziV2ZXJB5znkM1s0%2F5p6YeRWtSz%2F3osfniZQfq36MScEE1woDuAbXxvKtGY2%2FYguy%2BF67SMJhPOd9EWGUqwpSfJGLPGIqkHXWzj3CbDJNAzc8aF0XPWVZpDKoZvuDfFhe3igFXO5%2FG5NzV850t8Q9%2BaoYlNLa72&X-Amz-Signature=18eca559f5064cbafaaa6d22c482bb28c64fe81256adf1e1fd22c102640847c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
