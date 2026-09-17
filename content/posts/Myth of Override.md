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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD552TCE%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T223134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIDpROxXeMLNmGlkKtTTQbRWeNzcSsRbPsvKv%2BoQs6SD7AiAIPzOCLnlFFXXF0vhkH8d%2Bl1kGrV9Zx8Eo0tghwOJmtir%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMsJWnD3MisYjY75RZKtwDLscQASBXLF9Ma0rrdRcDDWRFUZJSGW39NxcLOLbEdwgCZD9jh8ecypG8J5oG5hf%2Fk44PJgQwuahUDZVfKl4pmAkmsetgxK2vliOxY81ILtBF%2B8mciVbJ%2Bku%2FliQluSsPs0NWzbZfj5ya2B4ihEns5VqC%2FsKnXy648OK2gggYM%2B%2FajQYlEFMurARw3riwq%2BVChctz%2Fl6iI%2BADYre8J%2BBQrro75OmzeRt%2BIE%2FADjik20sebSbI2KalC%2Fm1bz8MY5iY6cDo6Bp%2FB6UbyEgRVDQ4mGk3ZnTWVARqwSdzdzTk%2FWr2Udl%2BjGJh7%2FRJ1Y3f8NI2xwIngaQ1NvXhU2jttR1wzBBj%2FtX0PTm1VyC6MzMWVEtYbHWStJkR7R6nrbtUjMFvcsn4W2g4k1G0WBoIsYb5Gm1D9w%2F1qtcg20oHDk8obLRg7857yTa3WHJYG2c1L3juy6tSTo6D94wySCylGyfS6iJHueRPsA%2BuMn7n5K1B5G0ONLl9NW3S0I5VNXH%2FVPIiThZUrrpvcGCXqH2uskVxNvMsQRJU9gatsV9x0tXdsaJpC6NzIzHNrHVmdlxnm2clrcgQDdham0nY7yZCzPeQscFUplLfwLC7Mxxm1p3ckFmPBHCF1CQ6hsPJOj0wwa%2Bx1QY6pgEaFwPdDnZfltsqmjrsQbJNfFUdViRxYCZkLJ93GhtozS1DVeSKXwbS9rGAd8LgTowicvDgtGrOcD0rQ4FkGV%2FXHqvWA6QQsiWINHJrgOZf9AfZQ79XiDWvmIY6uP2VQoj2ZrzwMPhDT%2Fq85ejMZiKjNYvlFFFaV%2Fdxa0hoURYlv3AEqDNnm3Ug%2FPIupiNuwmyB%2F5AG6QFyKwtolVjacttY6HeEJfxj&X-Amz-Signature=122fc720c30cdecedfd6016a936ecf6f250c55d778e2f77d620f1d301e2c473b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD552TCE%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T223134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIDpROxXeMLNmGlkKtTTQbRWeNzcSsRbPsvKv%2BoQs6SD7AiAIPzOCLnlFFXXF0vhkH8d%2Bl1kGrV9Zx8Eo0tghwOJmtir%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMsJWnD3MisYjY75RZKtwDLscQASBXLF9Ma0rrdRcDDWRFUZJSGW39NxcLOLbEdwgCZD9jh8ecypG8J5oG5hf%2Fk44PJgQwuahUDZVfKl4pmAkmsetgxK2vliOxY81ILtBF%2B8mciVbJ%2Bku%2FliQluSsPs0NWzbZfj5ya2B4ihEns5VqC%2FsKnXy648OK2gggYM%2B%2FajQYlEFMurARw3riwq%2BVChctz%2Fl6iI%2BADYre8J%2BBQrro75OmzeRt%2BIE%2FADjik20sebSbI2KalC%2Fm1bz8MY5iY6cDo6Bp%2FB6UbyEgRVDQ4mGk3ZnTWVARqwSdzdzTk%2FWr2Udl%2BjGJh7%2FRJ1Y3f8NI2xwIngaQ1NvXhU2jttR1wzBBj%2FtX0PTm1VyC6MzMWVEtYbHWStJkR7R6nrbtUjMFvcsn4W2g4k1G0WBoIsYb5Gm1D9w%2F1qtcg20oHDk8obLRg7857yTa3WHJYG2c1L3juy6tSTo6D94wySCylGyfS6iJHueRPsA%2BuMn7n5K1B5G0ONLl9NW3S0I5VNXH%2FVPIiThZUrrpvcGCXqH2uskVxNvMsQRJU9gatsV9x0tXdsaJpC6NzIzHNrHVmdlxnm2clrcgQDdham0nY7yZCzPeQscFUplLfwLC7Mxxm1p3ckFmPBHCF1CQ6hsPJOj0wwa%2Bx1QY6pgEaFwPdDnZfltsqmjrsQbJNfFUdViRxYCZkLJ93GhtozS1DVeSKXwbS9rGAd8LgTowicvDgtGrOcD0rQ4FkGV%2FXHqvWA6QQsiWINHJrgOZf9AfZQ79XiDWvmIY6uP2VQoj2ZrzwMPhDT%2Fq85ejMZiKjNYvlFFFaV%2Fdxa0hoURYlv3AEqDNnm3Ug%2FPIupiNuwmyB%2F5AG6QFyKwtolVjacttY6HeEJfxj&X-Amz-Signature=e2f9fae3ce3bff6b709f9c13f19a07e5a1901214d2a158498d61f02c802e9afd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
