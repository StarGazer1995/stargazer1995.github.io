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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N435PL7%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T233855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZbrmALvDr%2BQjayFVn%2Bi2DmdohlRzGNYSjhl2GQJK8%2FgIhAKipRdwdPWyL0vRxsbPzlFn5wBOOo3IRMHMGhD%2F0KbWNKogECLf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXnvKtTHkSJWCzkbAq3APj6whn%2B6EV9pT9D9EUDqqsUA0PDV2tg8Lyb7duj3eZibjD%2FpW8UrH6WTURhsb3sShm0muzPrxc4V%2FxjugvbMkhDx1hqzuiKqmfRBaoKM7palnWY27hLU7T6QjhzkVA2vhBnwL0q%2Fw9Nx1DGOELL%2F7VIUYq2DJ14OpH26h%2BGRRSz0WgJofircMm9gzWFKOPKSVJrVp%2BUZAucL2%2BttaENreADp1nhbRG%2BNofeZ6RpH%2BpiuBPY60nPMrrjsOxsGlOEHzr7wIFXCwyzvL6MzUzF2aEGB7JnMOwusNmoVjuYHb0lMUKLt%2FvP7f2Xz2SS1tSUgNj2mW9lvEdZjLmsgSXwGPnW8sYqRXi41D%2BYSd7QdKt1y%2BPQt3xv4f0ulHQ4WU%2BSnZ8ASFKf1zwwFFNMqWK%2Bo7fECXQrP0hlcT0T4pelIxeutHQjPLaza5HNcG3dziOg7Oi7tmPEVe4CyYrB2UaDFKMSl0tAr3dH5IVDKIE%2F%2FYLRd4cgMyvM6h7x4ZFDPKAV9ZbIKEaBu4vU%2BDKWyxKb5yTNF9PSY1SfH%2BH7oJXoZe09d7yScmPve2A9qofRzXlakrtN7c9St3I%2BaF1Qczmh%2BgiJDQmxAFAv9tsahH9rNzFL3vKdun%2B0MJ0oAjd%2BDC5nN3UBjqkAakQyBFLeUmNtKsGkuoViSXyfwkKqMEwjGktjqqXwkIm60qS3hK%2B6eIDyS%2F2D2m%2FkI0ksYfadG9zrU4UOVeTcsITONppFDvwC8ghT%2FhP0gBV29fdLs4zsytw8Trg8pSL5czyyd3uzJQXIPWyl2im7DhvyorKc%2BNmnmSOYnYEM7Ll%2FuyuFHa%2FJYI5NHwr3kkSqHn8Zs2AWQ1rFljqemVX0v7rBuPy&X-Amz-Signature=4ea69a6871bd02e4703eca7943ccfc4c8e9242ad188fc918c32d7b7fa3ceb953&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N435PL7%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T233855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZbrmALvDr%2BQjayFVn%2Bi2DmdohlRzGNYSjhl2GQJK8%2FgIhAKipRdwdPWyL0vRxsbPzlFn5wBOOo3IRMHMGhD%2F0KbWNKogECLf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXnvKtTHkSJWCzkbAq3APj6whn%2B6EV9pT9D9EUDqqsUA0PDV2tg8Lyb7duj3eZibjD%2FpW8UrH6WTURhsb3sShm0muzPrxc4V%2FxjugvbMkhDx1hqzuiKqmfRBaoKM7palnWY27hLU7T6QjhzkVA2vhBnwL0q%2Fw9Nx1DGOELL%2F7VIUYq2DJ14OpH26h%2BGRRSz0WgJofircMm9gzWFKOPKSVJrVp%2BUZAucL2%2BttaENreADp1nhbRG%2BNofeZ6RpH%2BpiuBPY60nPMrrjsOxsGlOEHzr7wIFXCwyzvL6MzUzF2aEGB7JnMOwusNmoVjuYHb0lMUKLt%2FvP7f2Xz2SS1tSUgNj2mW9lvEdZjLmsgSXwGPnW8sYqRXi41D%2BYSd7QdKt1y%2BPQt3xv4f0ulHQ4WU%2BSnZ8ASFKf1zwwFFNMqWK%2Bo7fECXQrP0hlcT0T4pelIxeutHQjPLaza5HNcG3dziOg7Oi7tmPEVe4CyYrB2UaDFKMSl0tAr3dH5IVDKIE%2F%2FYLRd4cgMyvM6h7x4ZFDPKAV9ZbIKEaBu4vU%2BDKWyxKb5yTNF9PSY1SfH%2BH7oJXoZe09d7yScmPve2A9qofRzXlakrtN7c9St3I%2BaF1Qczmh%2BgiJDQmxAFAv9tsahH9rNzFL3vKdun%2B0MJ0oAjd%2BDC5nN3UBjqkAakQyBFLeUmNtKsGkuoViSXyfwkKqMEwjGktjqqXwkIm60qS3hK%2B6eIDyS%2F2D2m%2FkI0ksYfadG9zrU4UOVeTcsITONppFDvwC8ghT%2FhP0gBV29fdLs4zsytw8Trg8pSL5czyyd3uzJQXIPWyl2im7DhvyorKc%2BNmnmSOYnYEM7Ll%2FuyuFHa%2FJYI5NHwr3kkSqHn8Zs2AWQ1rFljqemVX0v7rBuPy&X-Amz-Signature=fa7ad1bcebef43739d46f3a6a576c258c237ae5667c694c05427092165d2a6cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
