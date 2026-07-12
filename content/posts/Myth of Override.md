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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2W6Z3EV%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T223738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAUUVuOZ352GvWvxASNe9UaaaUjpTlUobvmrGGU4%2FAW3AiA0VR29gW0BZQkc5a9lFJd4y%2FCwlBGfD2ZyuQV5Qf2uciqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqvvabfG6IusXJOXvKtwD0niAJfEqoF6xzUvNt3rIn%2FCqhMeOo0v%2FLg9thoo4YHCaOZgOMXT%2FDhNU5qocc5AS6R%2FXhSlMWJIkev0huhoKghWSijQFlvWCya%2FtYNFsPzRukMD9JJLgPnW9KEtfDaghYxV%2FSkeegYMEuhuC4w%2Bunv9Ng6UkemuB5IW7QuOrXiaGmm0eye8Y%2FoXVqVAiCYmEhy0ntxG56cn4BN%2B2lsh6z5JLaobha0b9cIkeGAlxS2zPal%2FgQzdKkd1mJgu%2BYug9ATwzfhDybEL2obl9XK1sRhbwnGePcWwQVCAq4cL5CsNVO%2Bu%2F2QTuJqI9ai41Q8JP9kWOXbtwFe6SVPFy61TaOI8SwH8G1hBC%2ByM6XqtTM4Fb%2Fgqlt0x5zMAZ1bdP9dB86xtvDOJV1%2BfUoNV8mRtcfDhDocVnaY6HSpZrdi4H5fVgFbC4Vu%2BrW%2BHhsPKIItmBl%2FteJ7PFxQvKuUxlLdVOqr4Yi%2Bk7AUrWjTeW1IHRBoCxYj5Y50w8wiXzjcqdE8aaP%2F36tGORa86HZoW9%2Bdq%2B9a%2BlLni8F0h%2Fq%2BRi3lDb6O0n2Y1wfV%2FEO%2BoPF8BUIxe0mZ8L1sbkViDsgzaod%2F8MTITqGkNCuL3MJwDWDk6AkUfsotCTFWSe1yJt%2BC4wn%2FXP0gY6pgGoWNZxTdmmbf1embMMcaIp6Pt38uxj8hRnE2z6IfzKyn90upVIBNE4AYXgKvY9o6NNvuxHnZg9i5uh5rZ1oIHVFIV%2Fmd8cvY4CIU6KEzy7eVx8gTZkE8Km1nPvJgDpodjLsW1b56WZ1NONvAQlZrvMwCcEUGHdSRq4EPwPzHc7J6Hcj%2B%2FuVtF6StXsgxPgIWgGfhFNk65lXaDWRRFYHMN7cdao%2FEZ6&X-Amz-Signature=08d044e68da105480dc4aae65df306795c62f3824f957cbe4cf60f105a4eedc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2W6Z3EV%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T223738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAUUVuOZ352GvWvxASNe9UaaaUjpTlUobvmrGGU4%2FAW3AiA0VR29gW0BZQkc5a9lFJd4y%2FCwlBGfD2ZyuQV5Qf2uciqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqvvabfG6IusXJOXvKtwD0niAJfEqoF6xzUvNt3rIn%2FCqhMeOo0v%2FLg9thoo4YHCaOZgOMXT%2FDhNU5qocc5AS6R%2FXhSlMWJIkev0huhoKghWSijQFlvWCya%2FtYNFsPzRukMD9JJLgPnW9KEtfDaghYxV%2FSkeegYMEuhuC4w%2Bunv9Ng6UkemuB5IW7QuOrXiaGmm0eye8Y%2FoXVqVAiCYmEhy0ntxG56cn4BN%2B2lsh6z5JLaobha0b9cIkeGAlxS2zPal%2FgQzdKkd1mJgu%2BYug9ATwzfhDybEL2obl9XK1sRhbwnGePcWwQVCAq4cL5CsNVO%2Bu%2F2QTuJqI9ai41Q8JP9kWOXbtwFe6SVPFy61TaOI8SwH8G1hBC%2ByM6XqtTM4Fb%2Fgqlt0x5zMAZ1bdP9dB86xtvDOJV1%2BfUoNV8mRtcfDhDocVnaY6HSpZrdi4H5fVgFbC4Vu%2BrW%2BHhsPKIItmBl%2FteJ7PFxQvKuUxlLdVOqr4Yi%2Bk7AUrWjTeW1IHRBoCxYj5Y50w8wiXzjcqdE8aaP%2F36tGORa86HZoW9%2Bdq%2B9a%2BlLni8F0h%2Fq%2BRi3lDb6O0n2Y1wfV%2FEO%2BoPF8BUIxe0mZ8L1sbkViDsgzaod%2F8MTITqGkNCuL3MJwDWDk6AkUfsotCTFWSe1yJt%2BC4wn%2FXP0gY6pgGoWNZxTdmmbf1embMMcaIp6Pt38uxj8hRnE2z6IfzKyn90upVIBNE4AYXgKvY9o6NNvuxHnZg9i5uh5rZ1oIHVFIV%2Fmd8cvY4CIU6KEzy7eVx8gTZkE8Km1nPvJgDpodjLsW1b56WZ1NONvAQlZrvMwCcEUGHdSRq4EPwPzHc7J6Hcj%2B%2FuVtF6StXsgxPgIWgGfhFNk65lXaDWRRFYHMN7cdao%2FEZ6&X-Amz-Signature=848e1bd899740b56c350fa19816f58f1bf298d959f2f267fbff660bf4ebcadfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
