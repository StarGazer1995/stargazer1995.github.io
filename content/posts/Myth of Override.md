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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSPMHSPI%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T011246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIBZmk%2Bs6LZL2mSGo0jL4Y%2FbGGpCNm448Abcibo%2FQzyVKAiEA4k7wTUIZ2a6I0HucrUmbwpGbfZyBp78f9vQwq%2FCawBMq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDA1EfkrkJi3DjJJp0CrcA3qbRcNx1KoNiwk9SaIbwD5HF0Pk85z6NHi80MCkgWrB%2Bt%2FEt7IKW%2FPoDgg3KxoRe8EVzrvFDYyXvJZhcGYiAHpJGnTm3KjR5YeW6o3MWlqj%2BAybYtydLIUgsWluUf3uhH3WCSuLK7F390XyJO9sfPglUY6w%2BzlxSfW308IhqiK60AsaDSTYzFE1MiWXhlWYVHmpojdp6p2CE84%2B2vtnX0zQd%2B%2FmO8A%2F8rWZplsipGPqIG3EmpltMKCsEefD1GdUhUAYeD%2BKgRQOFHJWZa2hIJJmfkTLXjIhh7rmHo4mkasG5JcsR6gRpUfzk9Rb2pQYbpBGaa9qk3%2FCJenuTEkSG3tsLEuLulT5j3xIBamZXWKtlvgrjC%2BqPMAprROkKJjU7yfsq3H5uw0GQgF8odPxyEmCO6o6qiwBeTE9q7kgnuuWsnzrymGs7Yv5av0QJ6LCmDPnRdQXRAQS%2B%2Bh%2FDqBxmP6pW7CPZohEj2HvCrREC2aKT3X4I54j42TQqbvgh60TA1gfp8HBNxGLmFjvJiRj8ZsThZbs%2BvYXgXfjnRtabYooO%2B3qxGZtZI%2BzDc1zzPum7Sh07hrfzoI5a96nnxfZ4CDhS6383B03TsJQWpVhJWVNlVf9sadPEwW4rEg7MLSH29IGOqUBlAboY4L2kpljovQsdgEkf%2FDB8Baxzm6DgfHB1d61OfNuohiMPARpEvIKuWT9ok9MVDPAnzrLRM%2FyfbJa7VTGzeN1acaS8nbISXMG%2BRT%2FsmmPe%2BsHTBkrpELpB9FJyVUV3EOLb0rEz1qkP7fUCmWKpGW970SbYAtcpNmxfTB01uytNjOypBR8WeulXaiwraS%2BIaC9629OBP0hIAjP%2F7Fhn%2FgCe4BP&X-Amz-Signature=7a537e43c527bda2786ccb943feb013f6acccc9cbc6a9eec9584bd1af513978c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSPMHSPI%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T011246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIBZmk%2Bs6LZL2mSGo0jL4Y%2FbGGpCNm448Abcibo%2FQzyVKAiEA4k7wTUIZ2a6I0HucrUmbwpGbfZyBp78f9vQwq%2FCawBMq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDA1EfkrkJi3DjJJp0CrcA3qbRcNx1KoNiwk9SaIbwD5HF0Pk85z6NHi80MCkgWrB%2Bt%2FEt7IKW%2FPoDgg3KxoRe8EVzrvFDYyXvJZhcGYiAHpJGnTm3KjR5YeW6o3MWlqj%2BAybYtydLIUgsWluUf3uhH3WCSuLK7F390XyJO9sfPglUY6w%2BzlxSfW308IhqiK60AsaDSTYzFE1MiWXhlWYVHmpojdp6p2CE84%2B2vtnX0zQd%2B%2FmO8A%2F8rWZplsipGPqIG3EmpltMKCsEefD1GdUhUAYeD%2BKgRQOFHJWZa2hIJJmfkTLXjIhh7rmHo4mkasG5JcsR6gRpUfzk9Rb2pQYbpBGaa9qk3%2FCJenuTEkSG3tsLEuLulT5j3xIBamZXWKtlvgrjC%2BqPMAprROkKJjU7yfsq3H5uw0GQgF8odPxyEmCO6o6qiwBeTE9q7kgnuuWsnzrymGs7Yv5av0QJ6LCmDPnRdQXRAQS%2B%2Bh%2FDqBxmP6pW7CPZohEj2HvCrREC2aKT3X4I54j42TQqbvgh60TA1gfp8HBNxGLmFjvJiRj8ZsThZbs%2BvYXgXfjnRtabYooO%2B3qxGZtZI%2BzDc1zzPum7Sh07hrfzoI5a96nnxfZ4CDhS6383B03TsJQWpVhJWVNlVf9sadPEwW4rEg7MLSH29IGOqUBlAboY4L2kpljovQsdgEkf%2FDB8Baxzm6DgfHB1d61OfNuohiMPARpEvIKuWT9ok9MVDPAnzrLRM%2FyfbJa7VTGzeN1acaS8nbISXMG%2BRT%2FsmmPe%2BsHTBkrpELpB9FJyVUV3EOLb0rEz1qkP7fUCmWKpGW970SbYAtcpNmxfTB01uytNjOypBR8WeulXaiwraS%2BIaC9629OBP0hIAjP%2F7Fhn%2FgCe4BP&X-Amz-Signature=23a7a9225d851316d9768067435fa1cbbb5f722cb6a151e3d0910b31cb82cc33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
