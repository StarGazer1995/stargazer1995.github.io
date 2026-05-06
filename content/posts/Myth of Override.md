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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5G5WNXT%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T051929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOkd3K0BqVy0fNbBW3FnNOdkrpJIFStIEgM1TepFNEUgIgPd6hCzsJc6zoqzcqSMhVNw60ZDjzNA5%2FW9SmNzOUp3MqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTNuzAQg2P%2BddgRPircA47W%2F4%2Bwm%2F2rT5%2FtxhThd08IdVoR%2Ffc7LKGdGgUWQwR54%2FCVcMbT1SRZAoshdVUbhTkOeJLdn2pRt7L7PJX2W6zufsuJQCHP%2BXwM00wiZ06cXI0%2FYfqxudfGcovZuNfDlgjLC47lpc1fgP9Ol32TYHlB4QwMM1jR8M5cG3I7PWvEzjsQ6z2KStgixpOtkd%2FY845BpxnU4ZddQ48Qzu1ZCtDabHi11dzqoVzSauLoD2HzLYcjnlHX0DdQjyYfY3EX9LpjUAkjcxg5I0HRT1Hn%2FYO9nMqfxI%2BDNC%2Fifk%2F8%2F5XvTh%2FzLXR0VV6LuteDeYpv2tJ%2BV08mADk8U7NprIYx8uhtnXCp97x%2Fe5BlU0BzZC%2BHVGMNxNtaDa8zXyKlkTlMev%2Bzm8Kj%2Bq2wZmH7nmc5qUZi0la2WJ%2FsWBrJcODvUycCbzJ6FGIjxdGlftAbJ7f%2Frv82H2syad1WmH7scv4GkH3ZS2bZFYYba2K0txI%2BkkVpyjxlSKiLqzqm1ExRonoq3W58ARhi2RuZyl4OVOvL%2BiYz9RvN4fhJzbTyp26fqFROMIgyuFQ6NG1QVR8SkfS4fLdS0jjrwFyhV4ll18g5r2E03FRxQv0XN2KuVkUIaRX%2BIP1HUUVbT4k2NHhuMN2a688GOqUBoJN2RAdtrm8Qh%2FVvwOqS72QHcQH2HX03UcBZBe9fc81mAfRFHy%2FXk%2BR0cWhX6laYpOPzCr5dfi%2FfNGDD04FWQ2saLD1ZSKlfRtv8pZdiu3hMANW0O14VcrXBsNxjIGBdFoT%2F%2FPJGdIkNBdqkLa4b79nn1fPCKSasgfuW%2FGKK15zQJ9n9lteBtjc4SIBBh%2BIWDPABx3%2BB6Z7Ao76CgjBE%2FYlfQ%2Bjr&X-Amz-Signature=e579a97d864fd44274e072ac2fe401a77f26d290b2ada809d71eb8db4e1a6892&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5G5WNXT%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T051929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOkd3K0BqVy0fNbBW3FnNOdkrpJIFStIEgM1TepFNEUgIgPd6hCzsJc6zoqzcqSMhVNw60ZDjzNA5%2FW9SmNzOUp3MqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTNuzAQg2P%2BddgRPircA47W%2F4%2Bwm%2F2rT5%2FtxhThd08IdVoR%2Ffc7LKGdGgUWQwR54%2FCVcMbT1SRZAoshdVUbhTkOeJLdn2pRt7L7PJX2W6zufsuJQCHP%2BXwM00wiZ06cXI0%2FYfqxudfGcovZuNfDlgjLC47lpc1fgP9Ol32TYHlB4QwMM1jR8M5cG3I7PWvEzjsQ6z2KStgixpOtkd%2FY845BpxnU4ZddQ48Qzu1ZCtDabHi11dzqoVzSauLoD2HzLYcjnlHX0DdQjyYfY3EX9LpjUAkjcxg5I0HRT1Hn%2FYO9nMqfxI%2BDNC%2Fifk%2F8%2F5XvTh%2FzLXR0VV6LuteDeYpv2tJ%2BV08mADk8U7NprIYx8uhtnXCp97x%2Fe5BlU0BzZC%2BHVGMNxNtaDa8zXyKlkTlMev%2Bzm8Kj%2Bq2wZmH7nmc5qUZi0la2WJ%2FsWBrJcODvUycCbzJ6FGIjxdGlftAbJ7f%2Frv82H2syad1WmH7scv4GkH3ZS2bZFYYba2K0txI%2BkkVpyjxlSKiLqzqm1ExRonoq3W58ARhi2RuZyl4OVOvL%2BiYz9RvN4fhJzbTyp26fqFROMIgyuFQ6NG1QVR8SkfS4fLdS0jjrwFyhV4ll18g5r2E03FRxQv0XN2KuVkUIaRX%2BIP1HUUVbT4k2NHhuMN2a688GOqUBoJN2RAdtrm8Qh%2FVvwOqS72QHcQH2HX03UcBZBe9fc81mAfRFHy%2FXk%2BR0cWhX6laYpOPzCr5dfi%2FfNGDD04FWQ2saLD1ZSKlfRtv8pZdiu3hMANW0O14VcrXBsNxjIGBdFoT%2F%2FPJGdIkNBdqkLa4b79nn1fPCKSasgfuW%2FGKK15zQJ9n9lteBtjc4SIBBh%2BIWDPABx3%2BB6Z7Ao76CgjBE%2FYlfQ%2Bjr&X-Amz-Signature=bec26d7ef01acec53c7bf716dabe434409c932cf6eb272b68d84b79260425c31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
