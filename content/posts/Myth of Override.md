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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZJ5XEAU%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T211307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIHRad%2BQ0gmX0fTHbynePV6fzRUjZILTJQNcyBY86QV3iAiEA%2FaJANRDm6K9p9HMcDgNyP3h9eOaOtKcnFEdWDl%2FSbBMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDE%2F0tX5%2BCayV7OBtyyrcA6SYW%2FYKGZaWZC1l3W3lxmvcBwwwC5ghyrDk%2BuuhVeyQHHBsai%2BfWZ%2BobQXCXmzx5%2BgwE6OOpc5kctCNzlhqS16THeB7kkaGxQbjJ1S2pqQERwgw5YDCiK1FlKekyfxMq50g32QVtcJt3XhWdisDEfT3c0yz6%2FdlHohpgXk3dDVvr6DrME6caUGNmvpb7M5B2853TDi5vUkGE%2F8Cdo45Apzw6LELftn6P5zfceLK%2B2fylCsbUnTj%2Bf9RW6TvozCRuIi6nOV5ONQt0SCB4gnzLM%2FS9ADE2v3yjI8NIIK%2FN%2BHDyVV4eO%2FLw4PY%2Bi7MdIB513RRPzC%2BzNU4m1WhgRRzNa13aYcx%2FtX6QdR%2BKtm%2B97RNP01gZnfhokaoItE3Jjte9UyPUoY7u2W5dsKpLAtA7FiQ%2FUJ03%2FPVdlWzY4aqUnKCeSa7aRlNbpvrO1zwP9m6o4dS5E5fiuiAvbTjRkCAyHDHyMYIWCDXfm%2Ffv6Ea%2FoIimM7xf%2BtZZF%2BfccWhVg1HA0DT0WnrpYQV4E3U4LvztNfAv4A%2Bu1r21ywtSkpjE0zluMdxcl3L0vrqMrJujnj%2Flg%2BBmHnlvKXAQUsWKlU9iTxshVbrqUlhzbZzGLXgs4R%2FA8EmEWumQ3k3qpetMNidjtAGOqUB2cn8fX36A0E5ABPzI5xSAL0gpt5kOXvKuTDIpGg9%2FsdQ59LV%2Ffjk563g7vpHG82izRlWLw6qJUobqUHssAvZ7Lg3jbiMDmt9kj3t%2Fgile%2BBKFRNHI3p2SkSgUSUTQFAum%2Bhk%2FW9UFZKzbvFkBNFRaRx6v87ExLvJmQahQee4paM5JMxO39%2BE8Q8Qc8H6NXcdnHfEdeQGB%2FG7PoeayDL48Wr9%2BQNi&X-Amz-Signature=9b0ad7443b3a8d1f046eb97436a9cf2ff1dcc83300dbd01d753431dd5022f1f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZJ5XEAU%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T211307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIHRad%2BQ0gmX0fTHbynePV6fzRUjZILTJQNcyBY86QV3iAiEA%2FaJANRDm6K9p9HMcDgNyP3h9eOaOtKcnFEdWDl%2FSbBMq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDE%2F0tX5%2BCayV7OBtyyrcA6SYW%2FYKGZaWZC1l3W3lxmvcBwwwC5ghyrDk%2BuuhVeyQHHBsai%2BfWZ%2BobQXCXmzx5%2BgwE6OOpc5kctCNzlhqS16THeB7kkaGxQbjJ1S2pqQERwgw5YDCiK1FlKekyfxMq50g32QVtcJt3XhWdisDEfT3c0yz6%2FdlHohpgXk3dDVvr6DrME6caUGNmvpb7M5B2853TDi5vUkGE%2F8Cdo45Apzw6LELftn6P5zfceLK%2B2fylCsbUnTj%2Bf9RW6TvozCRuIi6nOV5ONQt0SCB4gnzLM%2FS9ADE2v3yjI8NIIK%2FN%2BHDyVV4eO%2FLw4PY%2Bi7MdIB513RRPzC%2BzNU4m1WhgRRzNa13aYcx%2FtX6QdR%2BKtm%2B97RNP01gZnfhokaoItE3Jjte9UyPUoY7u2W5dsKpLAtA7FiQ%2FUJ03%2FPVdlWzY4aqUnKCeSa7aRlNbpvrO1zwP9m6o4dS5E5fiuiAvbTjRkCAyHDHyMYIWCDXfm%2Ffv6Ea%2FoIimM7xf%2BtZZF%2BfccWhVg1HA0DT0WnrpYQV4E3U4LvztNfAv4A%2Bu1r21ywtSkpjE0zluMdxcl3L0vrqMrJujnj%2Flg%2BBmHnlvKXAQUsWKlU9iTxshVbrqUlhzbZzGLXgs4R%2FA8EmEWumQ3k3qpetMNidjtAGOqUB2cn8fX36A0E5ABPzI5xSAL0gpt5kOXvKuTDIpGg9%2FsdQ59LV%2Ffjk563g7vpHG82izRlWLw6qJUobqUHssAvZ7Lg3jbiMDmt9kj3t%2Fgile%2BBKFRNHI3p2SkSgUSUTQFAum%2Bhk%2FW9UFZKzbvFkBNFRaRx6v87ExLvJmQahQee4paM5JMxO39%2BE8Q8Qc8H6NXcdnHfEdeQGB%2FG7PoeayDL48Wr9%2BQNi&X-Amz-Signature=84533be1fcf8aa2ac9913185088293baa4327af7ad9eb8908787e778ea20c008&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
