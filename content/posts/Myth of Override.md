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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OCOCMSR%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T194322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDmsovdlNrz93fYYl1au8v1gqA3dT80J21gOEe4EcpSQgIhAJKEVdrD7C5VvUj2PUnQCXhr7%2B6uETqW7d4H3u5caCTUKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyf9%2Fk1f3dB6AW3JXoq3APDIN2%2FPExh7FZTXWg7H3crn6wFj059rXFxmNG7RiD5R3HnyprNNuYSewghgNPRKb8dHcm%2F9muiWWfiLNAo30IO5cJRdaXbLfg37rJfpUDMwhEKhnh9oYLuqDSk6jcJUsZ%2B2xU6HKz7FAT1aUN0h1OlOratII9XTh5JUQLKROfsrwJ48zNPp8GnTMBtjGsI3HGHOY2IdAAaxDMOlO7y05K7%2B2odII5C2YaQAQDD9hQfTViu1F42APmi%2FAU1lKf9jNyvb58x0ICIMxpGb3Ef4kA9WEyZxlVLeiLORgNrsG3P4oYnR5cbh42ulZIb%2BnP9EhVTv3%2BHStTZP%2FYShAmY8hdSsGoxGAc1M4Fg%2BRYde9bCIBV%2FSCabeIyCdQWe0dF%2BSUfI1soVZYi4cKzVW%2Bf5BCT2RU5v6c7AIdwQhSaOdcy2LqWMudYY7OU0K%2FI1odgKix%2BZx6S3K2kFr8KVwYwijbJZ2QHDIyAm8Gg2BULP%2BET3aURuhrLXGn%2F%2BCp3FpRT0%2F6PDawuh3td9eSsdbcfRyrV7AmKqGO%2BjCLhOa9HnM%2BXvx8OCVAnzqXHP%2BXMGJcomk861pcbAMZeEUqk4h399LQxGDOKOMG%2BwRxVw5XfZP1jdxtUrNsWHzZvYLCS0%2FDCR27LQBjqkAdNBzHxxALUqJwJakhq5mTLtbZhqCuTeqAflq5l1Pc3IvH0T8r6QMdZhwhBMn%2F2%2BL9ybAyfhjY%2B4z3jVfTq%2Fv1lEXQx5G1ThiRVV4wsm3TURq1uQXJ81VpulDN1eaweYTmBOqBAShasku%2BTD1CmPp3Y8pfTyHiyfVvtfe%2BX9gqHMW%2FO9Lw8PMC3bl4y5bJvUzlo3o%2F%2B0cnjOkCLJ7VOmx08lufDD&X-Amz-Signature=d83921bf0dee3aede848ccb5da4c748e9d781dd79135bd88e0b8c0eb24ea0433&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OCOCMSR%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T194322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDmsovdlNrz93fYYl1au8v1gqA3dT80J21gOEe4EcpSQgIhAJKEVdrD7C5VvUj2PUnQCXhr7%2B6uETqW7d4H3u5caCTUKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyf9%2Fk1f3dB6AW3JXoq3APDIN2%2FPExh7FZTXWg7H3crn6wFj059rXFxmNG7RiD5R3HnyprNNuYSewghgNPRKb8dHcm%2F9muiWWfiLNAo30IO5cJRdaXbLfg37rJfpUDMwhEKhnh9oYLuqDSk6jcJUsZ%2B2xU6HKz7FAT1aUN0h1OlOratII9XTh5JUQLKROfsrwJ48zNPp8GnTMBtjGsI3HGHOY2IdAAaxDMOlO7y05K7%2B2odII5C2YaQAQDD9hQfTViu1F42APmi%2FAU1lKf9jNyvb58x0ICIMxpGb3Ef4kA9WEyZxlVLeiLORgNrsG3P4oYnR5cbh42ulZIb%2BnP9EhVTv3%2BHStTZP%2FYShAmY8hdSsGoxGAc1M4Fg%2BRYde9bCIBV%2FSCabeIyCdQWe0dF%2BSUfI1soVZYi4cKzVW%2Bf5BCT2RU5v6c7AIdwQhSaOdcy2LqWMudYY7OU0K%2FI1odgKix%2BZx6S3K2kFr8KVwYwijbJZ2QHDIyAm8Gg2BULP%2BET3aURuhrLXGn%2F%2BCp3FpRT0%2F6PDawuh3td9eSsdbcfRyrV7AmKqGO%2BjCLhOa9HnM%2BXvx8OCVAnzqXHP%2BXMGJcomk861pcbAMZeEUqk4h399LQxGDOKOMG%2BwRxVw5XfZP1jdxtUrNsWHzZvYLCS0%2FDCR27LQBjqkAdNBzHxxALUqJwJakhq5mTLtbZhqCuTeqAflq5l1Pc3IvH0T8r6QMdZhwhBMn%2F2%2BL9ybAyfhjY%2B4z3jVfTq%2Fv1lEXQx5G1ThiRVV4wsm3TURq1uQXJ81VpulDN1eaweYTmBOqBAShasku%2BTD1CmPp3Y8pfTyHiyfVvtfe%2BX9gqHMW%2FO9Lw8PMC3bl4y5bJvUzlo3o%2F%2B0cnjOkCLJ7VOmx08lufDD&X-Amz-Signature=d83db7d95c024b1ad52e8de06d999d8fd23439f2d03d20cd60a853ed881ad896&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
