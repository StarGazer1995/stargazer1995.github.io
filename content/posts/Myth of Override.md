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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RKC6XA7%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T084600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDNF66AYpBLKbg96wCa5vRw5q2ApbYOHOM5Ivj%2Fn%2FHlNwIhAI1jcBrJw5wIvL%2BjKwTxR8BakEHJ63aSy%2Fs6ZsCT3nZFKv8DCAkQABoMNjM3NDIzMTgzODA1IgzfE3wXg%2BJf%2BchvBAIq3ANwn9AbCJ9fdIBIbgPWTi1tUCMLmzeH%2Fu965mhtIZX0jMnI%2BN5MUpMPg6o4SueJjtDY3uOKeUZqhwECMKydiEP3E1UTuN4IPUviV%2BP1CJGzwcFUKQqWy0YoSJ7U1KCKpYEFqc9Oltchh9YDdrTdBL1JPA4xnIm3CrSUYsI7TCwEi0bgM8wKchbHGfCYfRq0d%2B39LGrnO%2Bnqwxx8pJBMHiZ8m3dp5OBauvgbnCb0Qn3xpWTuYWNb5makQQ57T9EOyN1gbXoYKHnJQxtMjZYsjW1pvwwMtrVcOX725gPBLqQxD8H0DpKiTQr8VIZJSK0%2F2OuuLSXM9Ps8NGtNcR0XYiIuSjMr4AOKRQfJE9ggiJ018AvrpNyxgFK0XaZnj0Prf71VpnU7hBj8izSERYBk407Ev%2BFh21uinnMGu6p%2F8zKBfA07Agi%2FKvAt%2FjZM2blK79FQ1jkCh8KmNFkN4oAVWCDU9jlt1WT6Z3ASLjK7%2B3YR5%2BzTV%2FChBEOV2Mf8bDRWggUdqCz183Nl7c%2BIynoE9Zbw8ogflN0DCGbYJgMD9WFSekJ3Zd1l36ije1wJYcNeZEdT75AimAv56EUhI9hxKjpenfp2Mmz%2FS7a775yLQU1ADT30ihv%2Br4wXyzojcjD1zJ3SBjqkAbpeuK2X6g927Gtkv1KYvvrfFK%2F%2FGs%2B1bfcCzkpTuCvf5qV9CSZaArembhmGRYTFNLmyOQ9InjbYkWH3V%2BJ0VCkD1U%2B9UYd2v5XdZgk0y1q%2BT1Ry9BrwEY9qu63fdJOq0Wem%2Blgf2Ase7JoOAv6B2kZx1QEuUepHvHhNUtNHTlgTNM7B1EaS1t%2BJzcLspUC2MNsPYvWBXmCyj3i1wNXgVw6CcKO1&X-Amz-Signature=052d207c90accb122052de27367b5bcd4a75f2e368ff2c2b27296c8d22de4ac2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RKC6XA7%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T084600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDNF66AYpBLKbg96wCa5vRw5q2ApbYOHOM5Ivj%2Fn%2FHlNwIhAI1jcBrJw5wIvL%2BjKwTxR8BakEHJ63aSy%2Fs6ZsCT3nZFKv8DCAkQABoMNjM3NDIzMTgzODA1IgzfE3wXg%2BJf%2BchvBAIq3ANwn9AbCJ9fdIBIbgPWTi1tUCMLmzeH%2Fu965mhtIZX0jMnI%2BN5MUpMPg6o4SueJjtDY3uOKeUZqhwECMKydiEP3E1UTuN4IPUviV%2BP1CJGzwcFUKQqWy0YoSJ7U1KCKpYEFqc9Oltchh9YDdrTdBL1JPA4xnIm3CrSUYsI7TCwEi0bgM8wKchbHGfCYfRq0d%2B39LGrnO%2Bnqwxx8pJBMHiZ8m3dp5OBauvgbnCb0Qn3xpWTuYWNb5makQQ57T9EOyN1gbXoYKHnJQxtMjZYsjW1pvwwMtrVcOX725gPBLqQxD8H0DpKiTQr8VIZJSK0%2F2OuuLSXM9Ps8NGtNcR0XYiIuSjMr4AOKRQfJE9ggiJ018AvrpNyxgFK0XaZnj0Prf71VpnU7hBj8izSERYBk407Ev%2BFh21uinnMGu6p%2F8zKBfA07Agi%2FKvAt%2FjZM2blK79FQ1jkCh8KmNFkN4oAVWCDU9jlt1WT6Z3ASLjK7%2B3YR5%2BzTV%2FChBEOV2Mf8bDRWggUdqCz183Nl7c%2BIynoE9Zbw8ogflN0DCGbYJgMD9WFSekJ3Zd1l36ije1wJYcNeZEdT75AimAv56EUhI9hxKjpenfp2Mmz%2FS7a775yLQU1ADT30ihv%2Br4wXyzojcjD1zJ3SBjqkAbpeuK2X6g927Gtkv1KYvvrfFK%2F%2FGs%2B1bfcCzkpTuCvf5qV9CSZaArembhmGRYTFNLmyOQ9InjbYkWH3V%2BJ0VCkD1U%2B9UYd2v5XdZgk0y1q%2BT1Ry9BrwEY9qu63fdJOq0Wem%2Blgf2Ase7JoOAv6B2kZx1QEuUepHvHhNUtNHTlgTNM7B1EaS1t%2BJzcLspUC2MNsPYvWBXmCyj3i1wNXgVw6CcKO1&X-Amz-Signature=009272e063680128070163fcfcd4bb4c6027e2c02d129b6ff079d151f8ea0e01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
