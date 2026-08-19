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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHBLZMBK%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T161959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B%2FoCg4IE5%2BNb4nKW6a0ilV2Kcv8TByariD1YNphvftwIhAPiQdcsynwd9Yban%2BxZ4gEv3qPiERYkMOHkJnriJCDjDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyCobVvGO5C3TKuPpsq3AOR8i9oE5N6iN6kz%2F2nbRfkKDKYxu4w3JQk4ko58MG7X%2FyY2DY1mfYEqDGZRdgVxT0ngO1eMpKjOUd1OL3qqxawFgIiWILJElQeea4hw0W4VYyUJ7CPLgidK98jfFaC7NTR3bSY4djeE2dhY6uPKXIrpxSYkooBN7nYu31CYsK%2B%2B%2FLjZa4kOAe5aqNS4%2FmMtuz6uO91O%2FPTZmXaGVnjA8NEV4%2FNpF5pQUDsXs6MtMn26CT7cPSTzF32atZe8S1J3GMKDWe1dKBe%2F0R7JdBHLXba5xJhhJP4ve6KmIMIxc8nVIeoSYnA2Fv9kn%2Ffob%2FULgZB37rZMuzK0qmXQZrmao15xuFMhiSRXpInU7ClSVT23khlKhAqrlnIEI05TFFSPJtzKZyTL0OVl2kkJGWVrYWDEwFylkTxojQpu75JPJOD2du0yc9gjiQpATZyajZi5S4S%2F%2B%2BDdAJLR0DXVb1hF8eL3%2FkofLfs2lyM7pQYdqg6SL%2Ff1jD88P12komppo6o285FJtSccmXiPcVVgo2kFu79L6%2B%2BrPzvzeGsVTDRwX2ZXcw9s%2F9yDKDUF1gxfQ7unerjPP9uvmPBol5awcY%2F3U84Rwh7brtpc2s%2FeWFkKnQ39QnOqksmpJlp1U4gLjDzlpfUBjqkAfN%2BnO92AUWl09UreCL9qv%2B1oAhpkYV6jlM0BujeEGxA1%2BQjQdbtWxIqQaDpbgarxlhY7zgAzYV8qVh%2Bbp0HYTYtheMU9hLMK0zYp4N4DMSV6qHEGxBl2X8Wq1W3dY4%2BTfXs1NXeSZGfJ1I8BX5zIX%2BKDp50l5gwvTf%2BbWV73O9YcEddYj3fDE62%2BxZ2xXzanGbf7mOD%2BwxVeloTUYZR%2Fvy0yFCa&X-Amz-Signature=eebc6446c3a7af2a83e5f8ddfad6e58bd2890556d7c42f6f165c1a23479b5202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHBLZMBK%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T161959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B%2FoCg4IE5%2BNb4nKW6a0ilV2Kcv8TByariD1YNphvftwIhAPiQdcsynwd9Yban%2BxZ4gEv3qPiERYkMOHkJnriJCDjDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyCobVvGO5C3TKuPpsq3AOR8i9oE5N6iN6kz%2F2nbRfkKDKYxu4w3JQk4ko58MG7X%2FyY2DY1mfYEqDGZRdgVxT0ngO1eMpKjOUd1OL3qqxawFgIiWILJElQeea4hw0W4VYyUJ7CPLgidK98jfFaC7NTR3bSY4djeE2dhY6uPKXIrpxSYkooBN7nYu31CYsK%2B%2B%2FLjZa4kOAe5aqNS4%2FmMtuz6uO91O%2FPTZmXaGVnjA8NEV4%2FNpF5pQUDsXs6MtMn26CT7cPSTzF32atZe8S1J3GMKDWe1dKBe%2F0R7JdBHLXba5xJhhJP4ve6KmIMIxc8nVIeoSYnA2Fv9kn%2Ffob%2FULgZB37rZMuzK0qmXQZrmao15xuFMhiSRXpInU7ClSVT23khlKhAqrlnIEI05TFFSPJtzKZyTL0OVl2kkJGWVrYWDEwFylkTxojQpu75JPJOD2du0yc9gjiQpATZyajZi5S4S%2F%2B%2BDdAJLR0DXVb1hF8eL3%2FkofLfs2lyM7pQYdqg6SL%2Ff1jD88P12komppo6o285FJtSccmXiPcVVgo2kFu79L6%2B%2BrPzvzeGsVTDRwX2ZXcw9s%2F9yDKDUF1gxfQ7unerjPP9uvmPBol5awcY%2F3U84Rwh7brtpc2s%2FeWFkKnQ39QnOqksmpJlp1U4gLjDzlpfUBjqkAfN%2BnO92AUWl09UreCL9qv%2B1oAhpkYV6jlM0BujeEGxA1%2BQjQdbtWxIqQaDpbgarxlhY7zgAzYV8qVh%2Bbp0HYTYtheMU9hLMK0zYp4N4DMSV6qHEGxBl2X8Wq1W3dY4%2BTfXs1NXeSZGfJ1I8BX5zIX%2BKDp50l5gwvTf%2BbWV73O9YcEddYj3fDE62%2BxZ2xXzanGbf7mOD%2BwxVeloTUYZR%2Fvy0yFCa&X-Amz-Signature=fac740ed20185cb7f20e200c77293ae86f880e85bf2d66b48ca6a59914d87dd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
