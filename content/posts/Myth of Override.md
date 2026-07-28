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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSLAGRJS%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T045240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGPLdu6Lk41OzICjvCXm1QRK%2F5rir3sPq7tP%2B8EQFOKfAiEA0KSxZMJpCwFMtpfItek62s1z3dGfizAUL5bbGbpThdUq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDDqUjovYxOzVdAHmBCrcAy4mZ9bxbsbfVdNdyljpSO2iMxSmJmC9QYuAfrMlJNZG17lM8I1a0UYwT5EztkaPnYeLc%2FRya%2F8kwAdb37JA65gL9I5wodoUUdDqEwSRukgZoK1f3%2FrARPvNZnr5FVvJFM49b7hZTMhMwVP6amMo5uoDZU59Ma0q4yo%2FVYe89VAN60EPZbLJRqliynl0I7iHH8rnAlmfOW6LEuLPR3vgxfGbL61Ipvfzf4YC3apXEnO4Y4lkZspidodq%2F03P3NZqgCgY%2FO5HwP5LlRiKLPnWcz%2Bp6EBkJ98x5aQDahH4pfGslvDOhIBh2%2FOhBfIPU0u4HQ9tXokGcWgWigeUdr%2F%2FvrBvYG2tzblGR9BiyL3G1kow4FUay0LXA7Ip8cffgv2J1D%2FMKmWkz%2B5KtwTB7KRpL5Gkd0i0QKdtGDgaqOPOA51RJDc4hPLCB4gFqpGu8tYL7YQV1L299ByEx96MmEzRAdcIB1WYV%2F%2FwXsbURtIN6gLCVW79JvDuJns81BB4hwFhcXPoK9hLJ9ZjjHjp6tsGgfRKp6NrR0if%2FzchD%2F7WtRQTDoE%2Ftm47RX2bLpIuaT0y0w9eixWLELzH%2BtltrtZgg7n67PpsIyOsOFWJ%2BNgEwBWuzN1uT3wBDEjWD4%2F2MNbZoNMGOqUBJai4zlnYjiKPyNUGQRnrfP79kjqWeKpnxNU7rLLJheNl9lO8Ed%2BevfXRnEy2mEo0%2BtoY7a9kmja0rrOprTbUhIhKR%2BtxKtuKeA8yLDNu%2BmDjvjfJDtsqHBcCw%2Bj1EfLKX%2BP7zHJsgkrYDUJ%2BNehiE02PxJUzlef5DNcDoYD%2Fh1n3zFXUFLgel%2FYQUo4IrynZBtXv92wjcHvk3%2Bg%2BYPjwrmTjymn0&X-Amz-Signature=7e7e96421759198fb159c5c65de5e4671589dadc97196bf9af99d58fb3abf5bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSLAGRJS%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T045240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGPLdu6Lk41OzICjvCXm1QRK%2F5rir3sPq7tP%2B8EQFOKfAiEA0KSxZMJpCwFMtpfItek62s1z3dGfizAUL5bbGbpThdUq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDDqUjovYxOzVdAHmBCrcAy4mZ9bxbsbfVdNdyljpSO2iMxSmJmC9QYuAfrMlJNZG17lM8I1a0UYwT5EztkaPnYeLc%2FRya%2F8kwAdb37JA65gL9I5wodoUUdDqEwSRukgZoK1f3%2FrARPvNZnr5FVvJFM49b7hZTMhMwVP6amMo5uoDZU59Ma0q4yo%2FVYe89VAN60EPZbLJRqliynl0I7iHH8rnAlmfOW6LEuLPR3vgxfGbL61Ipvfzf4YC3apXEnO4Y4lkZspidodq%2F03P3NZqgCgY%2FO5HwP5LlRiKLPnWcz%2Bp6EBkJ98x5aQDahH4pfGslvDOhIBh2%2FOhBfIPU0u4HQ9tXokGcWgWigeUdr%2F%2FvrBvYG2tzblGR9BiyL3G1kow4FUay0LXA7Ip8cffgv2J1D%2FMKmWkz%2B5KtwTB7KRpL5Gkd0i0QKdtGDgaqOPOA51RJDc4hPLCB4gFqpGu8tYL7YQV1L299ByEx96MmEzRAdcIB1WYV%2F%2FwXsbURtIN6gLCVW79JvDuJns81BB4hwFhcXPoK9hLJ9ZjjHjp6tsGgfRKp6NrR0if%2FzchD%2F7WtRQTDoE%2Ftm47RX2bLpIuaT0y0w9eixWLELzH%2BtltrtZgg7n67PpsIyOsOFWJ%2BNgEwBWuzN1uT3wBDEjWD4%2F2MNbZoNMGOqUBJai4zlnYjiKPyNUGQRnrfP79kjqWeKpnxNU7rLLJheNl9lO8Ed%2BevfXRnEy2mEo0%2BtoY7a9kmja0rrOprTbUhIhKR%2BtxKtuKeA8yLDNu%2BmDjvjfJDtsqHBcCw%2Bj1EfLKX%2BP7zHJsgkrYDUJ%2BNehiE02PxJUzlef5DNcDoYD%2Fh1n3zFXUFLgel%2FYQUo4IrynZBtXv92wjcHvk3%2Bg%2BYPjwrmTjymn0&X-Amz-Signature=03350762f03733928a20486f1f968bf3d216a24eae3cf7c3bfdcb8db559e8450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
