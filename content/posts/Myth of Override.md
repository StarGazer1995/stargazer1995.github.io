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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DZOLHSY%2F20260827%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260827T170131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIFjxlBMmVbqkeqesQAv%2FSmWYBtlMp6Q2JI18TTuRDMwYAiBmnVpxQS0jkLMW4AOnrhTZ38jZF7wioalz%2Bd9Un6IOhyr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMv0bVohAdVsu2myEMKtwDb%2FxDl%2Bp1JTvvsladzAnM9zKSSRhKO8oJCpW3AMx8OAPRsHQs7q73Z9aI%2FTCwFMwFos1lbm%2FmqD2L2pJOGTebZm%2BCdleZjNZ84t9EmiSE79jtQr5uO%2FEv%2FtJfxpp08%2FNEabMlPwHS%2Bh2vVLgxYZKZ2gluYuh8TtFjmhsUiMZLc7DF9wz1MPTWEEQxMSH%2FE8u2e%2FnPMjn90UhHr0Lj8izrfQmRr8Ev390F4geRkJuJ3E4YE1xI4wl87gw8DmcbBuovivPRlVDzZyTf%2B7n1nUn279M%2FR0ql512NpCf9zDvBztmdjVlCsMd1y3jyhKjRx5G6JAUFQ%2FAncISeH5XiA33UaSFpIAUEYZN4UT4yz16qnBCzaHhTszEzgYtfOqAHyGXaFopfgvnuhriaRi9L4fJ8UcBH7zoOfk59J%2BLDJVK2nCxIqkLnzM2NlB9G7nNkbLN4KM1x0gBZ305MCFrjCXSyV2iIs3agBwx8nTdcR4DbTqe5rchL3WPV8n9VTKvLhgeOjbADoWxyKThxQTY%2FrFEp2RE55igoxeYfG2pWiF9lZ0mNjLvID1nXVGp%2F3xoU%2B43T1x3ounxNFC82x%2BRIbenMWoimG9Dvfb2ah2wHLGBhE7XamXmMoCj6fxdLzKgwgs7B1AY6pgEXKH2yzZEYEExx2weKy9ON5cAlXukKJ9c4O5R9iC00cR%2BDtaQ7NCx0Gtpiuk5ryBO6sxg4MRvGYAAY37jh%2F0QXWZKj%2FLfkq4ovy6yUZL6NxaaO21xhNXt%2BX0g4Q01X4XXaYlaPykhROvoRgHUBZPt8PXK9LAEO5BVjepXsZ%2FbrqPJH2nGRWs5jQajFWJreJgMiSPXm6NiCm%2FqfOKalXkXafP5Vhxpg&X-Amz-Signature=c730e6e157b13a9c54f14cc2fc90d480c5c6a74ab8c7f6a647f3dc92f941c9d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DZOLHSY%2F20260827%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260827T170131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIFjxlBMmVbqkeqesQAv%2FSmWYBtlMp6Q2JI18TTuRDMwYAiBmnVpxQS0jkLMW4AOnrhTZ38jZF7wioalz%2Bd9Un6IOhyr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMv0bVohAdVsu2myEMKtwDb%2FxDl%2Bp1JTvvsladzAnM9zKSSRhKO8oJCpW3AMx8OAPRsHQs7q73Z9aI%2FTCwFMwFos1lbm%2FmqD2L2pJOGTebZm%2BCdleZjNZ84t9EmiSE79jtQr5uO%2FEv%2FtJfxpp08%2FNEabMlPwHS%2Bh2vVLgxYZKZ2gluYuh8TtFjmhsUiMZLc7DF9wz1MPTWEEQxMSH%2FE8u2e%2FnPMjn90UhHr0Lj8izrfQmRr8Ev390F4geRkJuJ3E4YE1xI4wl87gw8DmcbBuovivPRlVDzZyTf%2B7n1nUn279M%2FR0ql512NpCf9zDvBztmdjVlCsMd1y3jyhKjRx5G6JAUFQ%2FAncISeH5XiA33UaSFpIAUEYZN4UT4yz16qnBCzaHhTszEzgYtfOqAHyGXaFopfgvnuhriaRi9L4fJ8UcBH7zoOfk59J%2BLDJVK2nCxIqkLnzM2NlB9G7nNkbLN4KM1x0gBZ305MCFrjCXSyV2iIs3agBwx8nTdcR4DbTqe5rchL3WPV8n9VTKvLhgeOjbADoWxyKThxQTY%2FrFEp2RE55igoxeYfG2pWiF9lZ0mNjLvID1nXVGp%2F3xoU%2B43T1x3ounxNFC82x%2BRIbenMWoimG9Dvfb2ah2wHLGBhE7XamXmMoCj6fxdLzKgwgs7B1AY6pgEXKH2yzZEYEExx2weKy9ON5cAlXukKJ9c4O5R9iC00cR%2BDtaQ7NCx0Gtpiuk5ryBO6sxg4MRvGYAAY37jh%2F0QXWZKj%2FLfkq4ovy6yUZL6NxaaO21xhNXt%2BX0g4Q01X4XXaYlaPykhROvoRgHUBZPt8PXK9LAEO5BVjepXsZ%2FbrqPJH2nGRWs5jQajFWJreJgMiSPXm6NiCm%2FqfOKalXkXafP5Vhxpg&X-Amz-Signature=b60bbf8eee63347387cb46d813976f4cd3b7e47a432f6b0c7b872f7c48640915&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
