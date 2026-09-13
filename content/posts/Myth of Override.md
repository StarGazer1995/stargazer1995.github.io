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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3VBGLID%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T065437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBivZj4LmzAU0gef7pMUrk6yB9ZXdgtVBKxvkWxEM9oFAiAlOFtJo75XyMCSwtc8DnWLbH2SYygxMYiZ7iZYRU1HLyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR75aFygWwmPOjFCIKtwDw7khuvzaO2Ev%2BafJq7N3pe8uyYmLl9WE%2FfKIuv%2FwkBttJSVJFx6TW%2FSGka8yjBWRwo%2F8%2BUfCEmHuowSYB3qpgPRDEs4%2B1dK7dRHQBusEMXxxvSC8nYi3ZuotoT536nALJiZln%2B%2Boo5id%2B4YQLHqCKadJ%2FaNWT7%2BNz2Skto1OYG%2F1xu0hPg%2BOLr4kU5owMLEHX8grjRlk4jfOR2%2FtHujxQyCp2hGi57JhHE2t1DwsbVGWe8XL9vAGXfPpxaMpk2W0WJ8xZlfX3p1qNkl7pSw7mrVR4GXFLtpPVzAeJEuDk2wbX2ET45rq7%2BRxWDMxDCJ%2FI62BMuRxrXtbyE31ikT%2F%2BUw83soc6Ho3EUxmX6fGW1qK79LOEJrOroEwb5qZxfB2cHiGtLKYGfsclO1RpjKazH3nOYvzYmt0o45hZyY1K2WM6OkbPLsP7%2FIvxRYc1lWKrusAR1uaBesCZjcvPREotp1IUD7VDofo7SnscMF%2FwxPhqo35G%2FJvqR%2F4x%2BYFjoaYvbYVLFuwZoYdbPBfIUxNES%2F1xu3Vn7DxQ%2F%2FJvllUFk8EjP41XUgW5ucbuulytRszA9HPNgjtBEqbPqxeRc0Jl2dK4mIJcMGOd%2BtFyseWUUY72LRyQ6ni%2FQsWQ6Mw786Y1QY6pgGJzpGqLnDJSL6JuQauqcTmNtTYTjv3XX8c5VYn%2BBOsbRrXrMZtec3M6ddFJJ2%2FEFfN8flyoo%2FuUFi9E21hK1dKqgdptl5NRhdJU3sg6BwkEysjdDnNRauMfVnV4vX9z1FWiqq6rKIiuH98Jxci1Ns85M3hPoS33Ui%2BR9tBrEZCeKTJ9Eg%2FMwEHYl5pBvsoAQVvuGeQbrXaycr%2FgtnvIIlRVBkg4rzt&X-Amz-Signature=f69eec45c57302d8acdfc9c1b6da946e96b174dcc7b01a5f9706c05f38d62607&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3VBGLID%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T065437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBivZj4LmzAU0gef7pMUrk6yB9ZXdgtVBKxvkWxEM9oFAiAlOFtJo75XyMCSwtc8DnWLbH2SYygxMYiZ7iZYRU1HLyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR75aFygWwmPOjFCIKtwDw7khuvzaO2Ev%2BafJq7N3pe8uyYmLl9WE%2FfKIuv%2FwkBttJSVJFx6TW%2FSGka8yjBWRwo%2F8%2BUfCEmHuowSYB3qpgPRDEs4%2B1dK7dRHQBusEMXxxvSC8nYi3ZuotoT536nALJiZln%2B%2Boo5id%2B4YQLHqCKadJ%2FaNWT7%2BNz2Skto1OYG%2F1xu0hPg%2BOLr4kU5owMLEHX8grjRlk4jfOR2%2FtHujxQyCp2hGi57JhHE2t1DwsbVGWe8XL9vAGXfPpxaMpk2W0WJ8xZlfX3p1qNkl7pSw7mrVR4GXFLtpPVzAeJEuDk2wbX2ET45rq7%2BRxWDMxDCJ%2FI62BMuRxrXtbyE31ikT%2F%2BUw83soc6Ho3EUxmX6fGW1qK79LOEJrOroEwb5qZxfB2cHiGtLKYGfsclO1RpjKazH3nOYvzYmt0o45hZyY1K2WM6OkbPLsP7%2FIvxRYc1lWKrusAR1uaBesCZjcvPREotp1IUD7VDofo7SnscMF%2FwxPhqo35G%2FJvqR%2F4x%2BYFjoaYvbYVLFuwZoYdbPBfIUxNES%2F1xu3Vn7DxQ%2F%2FJvllUFk8EjP41XUgW5ucbuulytRszA9HPNgjtBEqbPqxeRc0Jl2dK4mIJcMGOd%2BtFyseWUUY72LRyQ6ni%2FQsWQ6Mw786Y1QY6pgGJzpGqLnDJSL6JuQauqcTmNtTYTjv3XX8c5VYn%2BBOsbRrXrMZtec3M6ddFJJ2%2FEFfN8flyoo%2FuUFi9E21hK1dKqgdptl5NRhdJU3sg6BwkEysjdDnNRauMfVnV4vX9z1FWiqq6rKIiuH98Jxci1Ns85M3hPoS33Ui%2BR9tBrEZCeKTJ9Eg%2FMwEHYl5pBvsoAQVvuGeQbrXaycr%2FgtnvIIlRVBkg4rzt&X-Amz-Signature=e741d24f3cbdcf3803d1d0664ecde536f820171e5fe9fa100d0e1a490d74a9c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
