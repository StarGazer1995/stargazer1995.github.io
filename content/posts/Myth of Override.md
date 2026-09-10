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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCU3JEHW%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T172348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFb5LCSclOSwIDFI%2BYGIg8Lg3eSsPgYtifpjm4Koi0LAiEAkcy8zf3vHz%2F4%2Bi0DvMCihRJmWQUXtkAaMRMSQJTAeX8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfYirnZlGVbYawefCrcA4ZMvePmhzS77XD2DyW3P1XO9cih376M2Jj6VANZPJfytN11ES186ag2Vdk4O%2Fp6eHE0tK3VB31ApVi0wfvq4AQqcGF32%2FFjdZ7jEjhsJQVXD23DT7X5g%2Fcle5zd8pYDTnlwbkhuvGP9CRecLobAX5cQzIfGvJ4v8TNG%2BZ%2F3TD%2FyLtfb5dXURuN1%2BJo%2FI%2BQxewlSbd53X7Z2P0jNco5jL7ObZEiV8amGPZDqkDeYAyU1CC2etdkRzUHFOs6p5Hb7leZo%2B7so7o4%2FJBgITd2ytH65k6i3xXhw%2BoICUqS72fWYaSDR33bipLC9QcVVI0y5eX2vZ%2FLw1QCYtnMwnhuoYFgs4ymitE9sbWEVAYWZpKiceDOklg43aH%2BXJBXTabhEzyGqFn3W%2F5FGrypg8WSbMCsFpS%2FHkF8JUmHCDT9peflPzurSZauOv9xWTy92nLIeHevB5kkECnuZTbGWY4%2BSsB6GeE4kJB%2FuSbtu9lW7mmJZ%2B0JfqDQ5e4fKSMAVLAJ8m2nYX8Nr%2FFY9ROBJiFseWzuPmIkwb642%2BFfAbo9jpph%2BAJw3dTMYzBpb%2FLash%2BA09VkYwTE4w8ZlGp2jIvUzRBDb2nIa8XMGTKtqahIsCVgv7YYUzO2gQ7CpTZpUMLviitUGOqUBii%2FoOgV96QIb6mW7lx7xjWdWk3S38iNOpaKMu6qzGfekqkouWiZqcGbjS0ITsWmjPJvjML71Ee94g8JLVEywZdotsrTgqwaoGk%2FPS3L6adBEYfunywG38I%2BaL4YdhwJZOUccEzzAmchIUkYS4%2FH83cSN21FN23w%2B0qCF%2FGtaETReAZaAbt5J7qEGx1GV4X6WO5ISDV4R9Za4rhM4yAReFNdukLiJ&X-Amz-Signature=59b56458b41df99a408e6b3b550a3e28f2e3a293073c045fcbcbcc6e433fa685&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCU3JEHW%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T172348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFb5LCSclOSwIDFI%2BYGIg8Lg3eSsPgYtifpjm4Koi0LAiEAkcy8zf3vHz%2F4%2Bi0DvMCihRJmWQUXtkAaMRMSQJTAeX8qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDfYirnZlGVbYawefCrcA4ZMvePmhzS77XD2DyW3P1XO9cih376M2Jj6VANZPJfytN11ES186ag2Vdk4O%2Fp6eHE0tK3VB31ApVi0wfvq4AQqcGF32%2FFjdZ7jEjhsJQVXD23DT7X5g%2Fcle5zd8pYDTnlwbkhuvGP9CRecLobAX5cQzIfGvJ4v8TNG%2BZ%2F3TD%2FyLtfb5dXURuN1%2BJo%2FI%2BQxewlSbd53X7Z2P0jNco5jL7ObZEiV8amGPZDqkDeYAyU1CC2etdkRzUHFOs6p5Hb7leZo%2B7so7o4%2FJBgITd2ytH65k6i3xXhw%2BoICUqS72fWYaSDR33bipLC9QcVVI0y5eX2vZ%2FLw1QCYtnMwnhuoYFgs4ymitE9sbWEVAYWZpKiceDOklg43aH%2BXJBXTabhEzyGqFn3W%2F5FGrypg8WSbMCsFpS%2FHkF8JUmHCDT9peflPzurSZauOv9xWTy92nLIeHevB5kkECnuZTbGWY4%2BSsB6GeE4kJB%2FuSbtu9lW7mmJZ%2B0JfqDQ5e4fKSMAVLAJ8m2nYX8Nr%2FFY9ROBJiFseWzuPmIkwb642%2BFfAbo9jpph%2BAJw3dTMYzBpb%2FLash%2BA09VkYwTE4w8ZlGp2jIvUzRBDb2nIa8XMGTKtqahIsCVgv7YYUzO2gQ7CpTZpUMLviitUGOqUBii%2FoOgV96QIb6mW7lx7xjWdWk3S38iNOpaKMu6qzGfekqkouWiZqcGbjS0ITsWmjPJvjML71Ee94g8JLVEywZdotsrTgqwaoGk%2FPS3L6adBEYfunywG38I%2BaL4YdhwJZOUccEzzAmchIUkYS4%2FH83cSN21FN23w%2B0qCF%2FGtaETReAZaAbt5J7qEGx1GV4X6WO5ISDV4R9Za4rhM4yAReFNdukLiJ&X-Amz-Signature=45b97878db0133f5f7c574bc293624225a2deca520093c9c6b203bef7eef0392&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
