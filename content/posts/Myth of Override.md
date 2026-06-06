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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QWS63NN%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T165752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDeqFrgBDxOMLzcXY6DsJs7IjnsVvu2XbnuGlAdJtcvAiBOR0Edye0rF8dk5d5huRMwvg92KxKtsHm1ULoHaTPodyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8%2Fq6w6843s9zhWhrKtwDFv6oKAJuyAevbWbP6YNra%2BcQLQnoFEwAFAa9It0YWsbGNag4sRpJU6jBPITuLWC2VAAOImDzJ%2FYahABbPACyuNY2wS0fSAGOcVjm043yXTCkBvC%2Fo8WjdbbQv3D7YmcKlZIwLAF43xVpJiklDcIFA2V3dvdhgyAnjjd223HY8vTrnbkFDW326M8Pvn6Ai0kPZyKCx0cNCwxFTXh%2Fk8P7qj%2BEst5%2BdMg6K%2B3LsQCZ%2BwRuBy2tA5%2FYTXohYNWM8sFgSMYM1Z%2FpgLxdjaL0p2Cpal4SZTOpD%2B%2FXm0vTcIHnuGOvqlPVRkveJaWOEhLv4ADtXECjY3wEq1WpMBrn2dN62jnp4nmPzTY%2Bk1ra7iXF%2Ft1dUotX%2BlCG%2BqvDvJ9JDGqoLIOR5WWSRQGMCfNVqZSzeIdZ9TUKKT4Ws%2Bqhacjn62H27ETq3gHowu8wnqB7m2%2BkpanSaQXG4i2RcpTB2Lu0paqSZUYS9HdtrUHdDlCHPiOC5W%2BWq6qaThL52fFSP6sYI6CsMcaLIHruE%2BD2s2mbyYpkh6hctCAiE1nS6bRe011SIe3ix%2BNZwTVxkd%2Fc9lYTq501SE2eNuSU%2FunY13apEZW3UbrXmFqYwngIHam50KfjJY4Axsk1cdRJgmAwq5eR0QY6pgFvQtpx80vQzXrxb%2B1UBlW8JIlRPXxN44E3f%2FoOpxeENniiCOJ8AjyZv40u2XoqaaOAUvEP8VabqwelWzkg69Ej5%2BXv8bxqEa2II3dLktn2suAfsUIZfB%2FQhVntbrGwbjdqYpCtI9kqplqZ82Qe4rPDAdmFanarhZpih0D%2FdNsbZdGZ3QDbA%2BkKBeL7p7sKM%2FO2KyMMhCVz1CrlF7VEqTNCnyTgdouj&X-Amz-Signature=7565f7ddc20553e6980a00a5b2f86747ed275d54173f013e1e62f96f80483cab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QWS63NN%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T165752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDeqFrgBDxOMLzcXY6DsJs7IjnsVvu2XbnuGlAdJtcvAiBOR0Edye0rF8dk5d5huRMwvg92KxKtsHm1ULoHaTPodyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8%2Fq6w6843s9zhWhrKtwDFv6oKAJuyAevbWbP6YNra%2BcQLQnoFEwAFAa9It0YWsbGNag4sRpJU6jBPITuLWC2VAAOImDzJ%2FYahABbPACyuNY2wS0fSAGOcVjm043yXTCkBvC%2Fo8WjdbbQv3D7YmcKlZIwLAF43xVpJiklDcIFA2V3dvdhgyAnjjd223HY8vTrnbkFDW326M8Pvn6Ai0kPZyKCx0cNCwxFTXh%2Fk8P7qj%2BEst5%2BdMg6K%2B3LsQCZ%2BwRuBy2tA5%2FYTXohYNWM8sFgSMYM1Z%2FpgLxdjaL0p2Cpal4SZTOpD%2B%2FXm0vTcIHnuGOvqlPVRkveJaWOEhLv4ADtXECjY3wEq1WpMBrn2dN62jnp4nmPzTY%2Bk1ra7iXF%2Ft1dUotX%2BlCG%2BqvDvJ9JDGqoLIOR5WWSRQGMCfNVqZSzeIdZ9TUKKT4Ws%2Bqhacjn62H27ETq3gHowu8wnqB7m2%2BkpanSaQXG4i2RcpTB2Lu0paqSZUYS9HdtrUHdDlCHPiOC5W%2BWq6qaThL52fFSP6sYI6CsMcaLIHruE%2BD2s2mbyYpkh6hctCAiE1nS6bRe011SIe3ix%2BNZwTVxkd%2Fc9lYTq501SE2eNuSU%2FunY13apEZW3UbrXmFqYwngIHam50KfjJY4Axsk1cdRJgmAwq5eR0QY6pgFvQtpx80vQzXrxb%2B1UBlW8JIlRPXxN44E3f%2FoOpxeENniiCOJ8AjyZv40u2XoqaaOAUvEP8VabqwelWzkg69Ej5%2BXv8bxqEa2II3dLktn2suAfsUIZfB%2FQhVntbrGwbjdqYpCtI9kqplqZ82Qe4rPDAdmFanarhZpih0D%2FdNsbZdGZ3QDbA%2BkKBeL7p7sKM%2FO2KyMMhCVz1CrlF7VEqTNCnyTgdouj&X-Amz-Signature=7b9995313db447cbd2723a4f00d08d3526cf73f7942c9f1a230a28a17f398bed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
