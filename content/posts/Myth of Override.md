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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SBKOMEO%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T093956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCp4SsliHHJZQWXuMZoP4GF8lGBzxD3xc7qxaBmOMTKEQIgDGTD6VC6eYGMXHF9OwZ%2FA2LpOTvNJek%2FQJ65p9ryOFsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM2wLpQ5eiws6EfzsCrcAyAfWTxwkxY8pUfZBUsku9%2BgXbSekujUCcRQEtdz6yIRrSjaxY69ra9Zu994AiIjPLGlgcS4WxGLD%2F0TmRGatX74RBVSiQsguRw9nNpKXy%2FWrx%2BCqh5bcwl9yquep9U4ZN%2BARzj7HS0L%2F6NuBA6jb6O2RpUQrxAndGQ5nTHUUH8Khd%2BvRyClNsCxKQbdJ%2F7P9P6dap7PVB%2BRmF%2Fy%2FcdV33wYTWxHLzKbHI6ZwpDd%2BorDuXNS1vhnHFbP%2FhTt7qeAZRzflKyC6fO9J5NScbqS7KVukmhJxEhAvYsS2XOcHBuEqZyPG5otoL2D5Gyra%2FpeZ6AHExYjHpTetcY2MHG3gUYKkhVncl8jpXduccr36RX9%2F5%2Brt7yIEDA9Qz17Mewwh085ZFZZUWwHiAUccECENI7wBmRpK7LSJQmFo1dn6R8OtCbyeSowrDZq7l2C7%2FCxqBnyqPr2UjS%2F4sLZC32%2FLnjhau56FAiZCyHjqR7a%2Fc%2FcG2ww%2BMSo7hysqjR%2FMEiU3eSG86E7G1q0QLsji2URMKrGZCpe7WW5M%2FkZBOCwTCSYegZZ1xr1Z9h9PAGYExbsHr3QnJdVwwwFPK%2FsNbr9jgiUMTo1pzhQVHeXPu92j7JC7rAxHoSbbq5lwVjuML%2B5n9EGOqUBlSDiTqYC%2BibTvsdSa%2BB4IB3cXS2Am9Ycdt4VsjNyPxZnoOr%2B0ix3qJzKBJtVbU655z%2FT7SLMaYxU6T8Cyh%2FkXvmg0cjwUkdogznwT4B18SuVENVo8MphVNA3PSg2Vs23rVyMFD%2Fvj9n6ShKZ6qJFqUC6yR5ohywvdhMTJTjBKMIY5N7v1OlBcISbHUyfGZgOUCEKXSPJ2Dv1TC9i1cxcSRfd%2FEAo&X-Amz-Signature=cf33cfd9666a7316d1383ec54eafe85acf958e7d3cf606f9ad142331dafb189e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SBKOMEO%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T093956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCp4SsliHHJZQWXuMZoP4GF8lGBzxD3xc7qxaBmOMTKEQIgDGTD6VC6eYGMXHF9OwZ%2FA2LpOTvNJek%2FQJ65p9ryOFsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM2wLpQ5eiws6EfzsCrcAyAfWTxwkxY8pUfZBUsku9%2BgXbSekujUCcRQEtdz6yIRrSjaxY69ra9Zu994AiIjPLGlgcS4WxGLD%2F0TmRGatX74RBVSiQsguRw9nNpKXy%2FWrx%2BCqh5bcwl9yquep9U4ZN%2BARzj7HS0L%2F6NuBA6jb6O2RpUQrxAndGQ5nTHUUH8Khd%2BvRyClNsCxKQbdJ%2F7P9P6dap7PVB%2BRmF%2Fy%2FcdV33wYTWxHLzKbHI6ZwpDd%2BorDuXNS1vhnHFbP%2FhTt7qeAZRzflKyC6fO9J5NScbqS7KVukmhJxEhAvYsS2XOcHBuEqZyPG5otoL2D5Gyra%2FpeZ6AHExYjHpTetcY2MHG3gUYKkhVncl8jpXduccr36RX9%2F5%2Brt7yIEDA9Qz17Mewwh085ZFZZUWwHiAUccECENI7wBmRpK7LSJQmFo1dn6R8OtCbyeSowrDZq7l2C7%2FCxqBnyqPr2UjS%2F4sLZC32%2FLnjhau56FAiZCyHjqR7a%2Fc%2FcG2ww%2BMSo7hysqjR%2FMEiU3eSG86E7G1q0QLsji2URMKrGZCpe7WW5M%2FkZBOCwTCSYegZZ1xr1Z9h9PAGYExbsHr3QnJdVwwwFPK%2FsNbr9jgiUMTo1pzhQVHeXPu92j7JC7rAxHoSbbq5lwVjuML%2B5n9EGOqUBlSDiTqYC%2BibTvsdSa%2BB4IB3cXS2Am9Ycdt4VsjNyPxZnoOr%2B0ix3qJzKBJtVbU655z%2FT7SLMaYxU6T8Cyh%2FkXvmg0cjwUkdogznwT4B18SuVENVo8MphVNA3PSg2Vs23rVyMFD%2Fvj9n6ShKZ6qJFqUC6yR5ohywvdhMTJTjBKMIY5N7v1OlBcISbHUyfGZgOUCEKXSPJ2Dv1TC9i1cxcSRfd%2FEAo&X-Amz-Signature=4587c8e830f54458c0c16e016553195d518585474ca653419598ec24192bb3fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
