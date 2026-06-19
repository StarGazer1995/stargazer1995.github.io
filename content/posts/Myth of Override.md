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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRSD5ZPQ%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T132714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyNGAKp3UBBec5dpRlryATuFR9BUDPfoy1iUkxcqqJggIhAKtqUU%2FLL%2Bl50LrV7auWUnWLhYSiv74lpf4c9hkGWwjVKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyyLbl3QfFYmFq38N8q3APh2fTzhtgGmlR%2BcHkWbZBrd2c1TBhtUXwXGr27rjqHhuNZboKk3XrFRQzH3H%2FuyekMDzl3RFjdY%2FgKkAD1Hba%2F1%2FX5RKWNl8lCzA3SoQZ5%2FgtAWTYcMaJVAyffmjW92T5TFIL8FG9YL7w%2B1eETKnoeS4dYPIrXirS%2FPF9CqgAvq1wl0PNzJIzEyAOBmaz29Lb9TzXyr5vqD6lmO3fzfqCGFrC%2BeNE0dvypdpGhltdpW6ZClGdO%2BGpkCfY4QCs8iJpoA1ReOXALLVjd01gOpzJ9Bj9EQ8YTArG9hYJDRbI47SW7kbCsTuB%2FEPnsIKQqTkKY%2BGEKWqP13c7BbOIWV2nKCetKMRnGFtNtxswoitMsJFO%2BS7cc%2BjZCTk%2FCKLp42CWY%2FWJeaKURK43vJprH8g2JvjAho9xmhSn%2FEs9o1GywU1wZriUb%2FbWTG%2BzXoCiyfV4Ft1YAAlhU3uJIfKc28OcTMYZ6sIBoD0pE95va8kx7oN9%2BITowH74LPNqB3h6SW8nMjd66LI3bOe5gRM5N4AZ%2F14vIhj7sJ26wLn591IhO6wYQ%2FAvOWF1N3AgQY20lxAkxHNVMAEsnappeG%2BXsLglCFM53l237oRnOurK63C2MSkuSdNEe3danfjDyCzCq6dTRBjqkAbjzZqzJaRrNxQNFW0lH8ewukpaB86X77dpBjXRfTmIc9IHyLKrsZMeZ17iPep7cewiuKpwrHX%2Ffz%2FM11OZL7Wt7B2c5wT2c0yUG6ZMWXGbyppEeEA9XhlT%2BVq2hBIdN2Cjnn8O4FK0O6yt8oKBjxlITblvZfb%2Fe6mdj5NCAuJHUFLWlooSPqYc%2F4Oznz1YrU1UWnwLeSPLvIdbJV64HRwY3ki%2Bg&X-Amz-Signature=fa3a0d96c2f845c0c9c863ab33809238101a2bf59e4567dd63d65510715b83b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRSD5ZPQ%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T132714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyNGAKp3UBBec5dpRlryATuFR9BUDPfoy1iUkxcqqJggIhAKtqUU%2FLL%2Bl50LrV7auWUnWLhYSiv74lpf4c9hkGWwjVKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyyLbl3QfFYmFq38N8q3APh2fTzhtgGmlR%2BcHkWbZBrd2c1TBhtUXwXGr27rjqHhuNZboKk3XrFRQzH3H%2FuyekMDzl3RFjdY%2FgKkAD1Hba%2F1%2FX5RKWNl8lCzA3SoQZ5%2FgtAWTYcMaJVAyffmjW92T5TFIL8FG9YL7w%2B1eETKnoeS4dYPIrXirS%2FPF9CqgAvq1wl0PNzJIzEyAOBmaz29Lb9TzXyr5vqD6lmO3fzfqCGFrC%2BeNE0dvypdpGhltdpW6ZClGdO%2BGpkCfY4QCs8iJpoA1ReOXALLVjd01gOpzJ9Bj9EQ8YTArG9hYJDRbI47SW7kbCsTuB%2FEPnsIKQqTkKY%2BGEKWqP13c7BbOIWV2nKCetKMRnGFtNtxswoitMsJFO%2BS7cc%2BjZCTk%2FCKLp42CWY%2FWJeaKURK43vJprH8g2JvjAho9xmhSn%2FEs9o1GywU1wZriUb%2FbWTG%2BzXoCiyfV4Ft1YAAlhU3uJIfKc28OcTMYZ6sIBoD0pE95va8kx7oN9%2BITowH74LPNqB3h6SW8nMjd66LI3bOe5gRM5N4AZ%2F14vIhj7sJ26wLn591IhO6wYQ%2FAvOWF1N3AgQY20lxAkxHNVMAEsnappeG%2BXsLglCFM53l237oRnOurK63C2MSkuSdNEe3danfjDyCzCq6dTRBjqkAbjzZqzJaRrNxQNFW0lH8ewukpaB86X77dpBjXRfTmIc9IHyLKrsZMeZ17iPep7cewiuKpwrHX%2Ffz%2FM11OZL7Wt7B2c5wT2c0yUG6ZMWXGbyppEeEA9XhlT%2BVq2hBIdN2Cjnn8O4FK0O6yt8oKBjxlITblvZfb%2Fe6mdj5NCAuJHUFLWlooSPqYc%2F4Oznz1YrU1UWnwLeSPLvIdbJV64HRwY3ki%2Bg&X-Amz-Signature=eb86eb6ec84ed5e8ee2c80089c23592a8d98cdaea1358d1d15db782ea2d68c39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
