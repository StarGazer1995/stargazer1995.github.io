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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHU4WX4R%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T105336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQCI3tJit1IjTNALzxz4R8GFrHrgcTvUXFB3H9Jr9gVuZgIgd%2B6U3QCpYq6I5OUNwSt6fIjH23IguOAKHxUX8T99D7Aq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDLdXZD%2FXZ8pJcyRIFyrcA4CnxLxfcoG0SAxztBZF5O2nOLSsXxosFqVIQdBd3SxlvYVXM9BRcWwBxYcK37z6jmLeeyj1t164yJ1Qk1K6dcxW9pfT8sH5oIA7IEds2tUVSvU%2FUL6807skzNDCC0kCQUQ%2FPd0Egfgodnby0woSrMElywJFMthmcG%2FZWGxc5KSftlSgcW8O7PAWJ7asFpAkptI0H%2Fa0pCDrayiQ0borPHxkp6E6IP3V5DT8bJnJnhEFo8zUQgSfX6SjEq91SgdYFFJ0x64aB06hurxBjFNACUYy5qZlXNhuGugs2MPZBBTf6CSdt7zoTsBDKdwePVihIHSjH1rWPMibA1LPYT0RgT%2FFio0eyKHzNRVYShyrqXOeD1cvf2uvfy2VgftIT0UOfCKPHzzvEFfa18dwZ5QXnN8i6a4n4Iwqnb3mz0vtAAK8ww1Vr5ekjLUrL%2FcfUgp2XIJgQSIqepvPkmBR8pcftLHfCCbB8AeIL7saY3qIOmbvRRThJ%2Bj8bvXDp1z5cq7Vkn8ikmKf3nYL4E0DCe%2BelANCg%2BAfVD9jnHxp%2BUk8rbHpLFI4Yd43NHUZI0RzN8MR7X8887kVI1kYX5t%2Fyj3N%2BtBFRn%2FCf8ej0inmDPGVQATt4IxSes5GRe6MjcvYMKyc6dEGOqUB0dNS4dKGaiO7BKR3%2FLayu1fSB6juEVhP4siYohh%2FMh1d8oy3dZqtH0Oro74ZD62C9U8UCSAiRWsfBdt2rL%2Bu9x7o0%2BTQ3ikSE2Puj3N8Ppk6ntne%2B88q1rbpoHfbCrvxRmQiGvSJwJaz7kli%2BE75eaKY%2B5esw954lWXy8G9HKakZ0cMzGTRkp%2B%2Fj%2BkPmXJFxWOYPk08DMl2n3186b%2F8fRrO%2BqMge&X-Amz-Signature=4c974d7332b49b28ad9ee5974381cb9288056969d471520dbf7dfd168f350a0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHU4WX4R%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T105336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQCI3tJit1IjTNALzxz4R8GFrHrgcTvUXFB3H9Jr9gVuZgIgd%2B6U3QCpYq6I5OUNwSt6fIjH23IguOAKHxUX8T99D7Aq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDLdXZD%2FXZ8pJcyRIFyrcA4CnxLxfcoG0SAxztBZF5O2nOLSsXxosFqVIQdBd3SxlvYVXM9BRcWwBxYcK37z6jmLeeyj1t164yJ1Qk1K6dcxW9pfT8sH5oIA7IEds2tUVSvU%2FUL6807skzNDCC0kCQUQ%2FPd0Egfgodnby0woSrMElywJFMthmcG%2FZWGxc5KSftlSgcW8O7PAWJ7asFpAkptI0H%2Fa0pCDrayiQ0borPHxkp6E6IP3V5DT8bJnJnhEFo8zUQgSfX6SjEq91SgdYFFJ0x64aB06hurxBjFNACUYy5qZlXNhuGugs2MPZBBTf6CSdt7zoTsBDKdwePVihIHSjH1rWPMibA1LPYT0RgT%2FFio0eyKHzNRVYShyrqXOeD1cvf2uvfy2VgftIT0UOfCKPHzzvEFfa18dwZ5QXnN8i6a4n4Iwqnb3mz0vtAAK8ww1Vr5ekjLUrL%2FcfUgp2XIJgQSIqepvPkmBR8pcftLHfCCbB8AeIL7saY3qIOmbvRRThJ%2Bj8bvXDp1z5cq7Vkn8ikmKf3nYL4E0DCe%2BelANCg%2BAfVD9jnHxp%2BUk8rbHpLFI4Yd43NHUZI0RzN8MR7X8887kVI1kYX5t%2Fyj3N%2BtBFRn%2FCf8ej0inmDPGVQATt4IxSes5GRe6MjcvYMKyc6dEGOqUB0dNS4dKGaiO7BKR3%2FLayu1fSB6juEVhP4siYohh%2FMh1d8oy3dZqtH0Oro74ZD62C9U8UCSAiRWsfBdt2rL%2Bu9x7o0%2BTQ3ikSE2Puj3N8Ppk6ntne%2B88q1rbpoHfbCrvxRmQiGvSJwJaz7kli%2BE75eaKY%2B5esw954lWXy8G9HKakZ0cMzGTRkp%2B%2Fj%2BkPmXJFxWOYPk08DMl2n3186b%2F8fRrO%2BqMge&X-Amz-Signature=1b136dc005ff73cb16903ace6df396e0d361c8628047825aec6a61a439e59897&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
