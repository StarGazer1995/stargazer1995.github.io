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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IC4HEJQ%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T112959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIHS%2Br3DBTvapubdiuwqGnG%2BMqXviDNJf17URQrN3%2BJrxAiEA9O6%2FRzdxkXJkGgnzJVN2yQKWG0D2WdJs1RCbju%2Bu%2BV8q%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDDLJw2Q95RzbSsr8WyrcA4%2Fq40xhX1%2FsVnYV4p4jXZDRF9x5UabMllKmurdtQy23p5I6b%2Bmvxu7e%2B8F7SBMYtK7aD%2BuMk1mu7tmJkRw0xc%2Bp8R6f7itmRXG%2Bix2%2BWB8BlWCo%2BnU8y8vvduNqjqsbw7Gw%2FO8PgYmkYPkeqByM%2B6Nkn624NZ%2FpNvj%2F%2BoxNVHT0bKQZvFvDZTmfqXdN1B1CXowIGC1fhHRF1Vs7Dd%2F%2B1vojAPDfT9R32tQLGNCDGMuRoHH7MBRhIRjuk%2Fx%2B4HDNwwZE7jjwewFm5vZ4jEdQc6J5C1%2FoFIufif%2B1PfuavtTht00sJ88NOfk75f8WZ9flLxPSll3UNU1wdoDUXhJPx400ytcHDBJcdMpS86g2RMQISZv00FTrR6yW8eqhJssRF7GqDlQ8nAXwOAJ6A%2BEJjLHI3CfSml%2Bume2UVjs62IUUM3CYaVnl%2BEKnwg4Cs%2BV390%2BteF%2FImCIoG9RTxvseULY7ZI9ZxC5aCOiSei9eNbWVYomClI9p1QcI%2By0SkU%2FS2uuLK4Q0zoheTWIVXYkrFV0mfLUxZm0P50A3JlE5ipUphU2ziX%2FiniEwPOav7%2BcDRlWfaFIKZvy3Z9K5t0MFyB4Arg%2BP%2BkEANJcUSHIxi2Z%2BE2TwXQfrp%2BwWBTh4MMbkjNMGOqUB1sxmuFBFR2KCI%2FgNBjoB%2FqDYcfZMMmkWBnnMFo5%2F%2FsSfMmoH5WyCltJcdqVavyZ6DafqAz9hklZ%2FfO07urqcOTQqi9DMXw%2Fv2jNERVaTQt6ttW1BX9YGdPsViXRX4M5ZM4vnI5pVTWJZQupMVbQeHs6dpgkoJVB03ifzZb5zYa0gtKdu7Dm%2FCZvlYs8f8NF3ZWBq9LRz9JO%2B9M3qm6IysDNzZ9L0&X-Amz-Signature=be47f1bec0f931d10e22d2b143334761ec3fc25a018aa3b201529c5ddd3c8124&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IC4HEJQ%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T112959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIHS%2Br3DBTvapubdiuwqGnG%2BMqXviDNJf17URQrN3%2BJrxAiEA9O6%2FRzdxkXJkGgnzJVN2yQKWG0D2WdJs1RCbju%2Bu%2BV8q%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDDLJw2Q95RzbSsr8WyrcA4%2Fq40xhX1%2FsVnYV4p4jXZDRF9x5UabMllKmurdtQy23p5I6b%2Bmvxu7e%2B8F7SBMYtK7aD%2BuMk1mu7tmJkRw0xc%2Bp8R6f7itmRXG%2Bix2%2BWB8BlWCo%2BnU8y8vvduNqjqsbw7Gw%2FO8PgYmkYPkeqByM%2B6Nkn624NZ%2FpNvj%2F%2BoxNVHT0bKQZvFvDZTmfqXdN1B1CXowIGC1fhHRF1Vs7Dd%2F%2B1vojAPDfT9R32tQLGNCDGMuRoHH7MBRhIRjuk%2Fx%2B4HDNwwZE7jjwewFm5vZ4jEdQc6J5C1%2FoFIufif%2B1PfuavtTht00sJ88NOfk75f8WZ9flLxPSll3UNU1wdoDUXhJPx400ytcHDBJcdMpS86g2RMQISZv00FTrR6yW8eqhJssRF7GqDlQ8nAXwOAJ6A%2BEJjLHI3CfSml%2Bume2UVjs62IUUM3CYaVnl%2BEKnwg4Cs%2BV390%2BteF%2FImCIoG9RTxvseULY7ZI9ZxC5aCOiSei9eNbWVYomClI9p1QcI%2By0SkU%2FS2uuLK4Q0zoheTWIVXYkrFV0mfLUxZm0P50A3JlE5ipUphU2ziX%2FiniEwPOav7%2BcDRlWfaFIKZvy3Z9K5t0MFyB4Arg%2BP%2BkEANJcUSHIxi2Z%2BE2TwXQfrp%2BwWBTh4MMbkjNMGOqUB1sxmuFBFR2KCI%2FgNBjoB%2FqDYcfZMMmkWBnnMFo5%2F%2FsSfMmoH5WyCltJcdqVavyZ6DafqAz9hklZ%2FfO07urqcOTQqi9DMXw%2Fv2jNERVaTQt6ttW1BX9YGdPsViXRX4M5ZM4vnI5pVTWJZQupMVbQeHs6dpgkoJVB03ifzZb5zYa0gtKdu7Dm%2FCZvlYs8f8NF3ZWBq9LRz9JO%2B9M3qm6IysDNzZ9L0&X-Amz-Signature=ca9ec7fbcfee44f2b3bfc8a479d7111318e85914be806570a9357dc851616293&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
