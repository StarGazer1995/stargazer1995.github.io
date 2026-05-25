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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636HAGLHN%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T225155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFzB3%2BgEsodeMjfKKV5pFVNRk7oCe9N9w7X8%2FIuessTuAiAjNxWmlzJ7bvgYoHA2OTMOb9GRHkRI8X2N8bpRp%2B6DNCr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIM6%2FGXVCfn%2BVyQw73HKtwD4GoW7jeBvUwMf7Yx4cNfxkcxZjanjG3WSMv6aeEhWaSdRcfiNuGVCIrO0u3pYGFnl2PCS3NPuakmrfK2CsWMfNkFFns7IxPu7mmnzLiYqMWKIb42IXjZnf6KvNUpp1yT2DXjWLFrAHyYJINntMWul46pQC5gc7b%2BTefLHX7DRY68e4YkD%2FTIAiBF5dxWMGuC5pDBufKF2%2F6YxKPKhXsp7PH%2Bl6peuaiJv522vn7FKn4n8f8442yb%2FcPnWIQQ3s7KbF8FwkaUoTC3mG0niVCVsUnVMjiPrHH%2FkYbXJ8cfwxXaBO%2FKnsomMlsMCLDmsgzgE9z4m2%2BcMXYaKJK9EWGimHaDj3%2BuNyLIUn9ZaXrDbWc0WGQCuF9k8I%2BrlbixqcOQZlo%2FSKVmbevVIb84zkJoKQLpDO972pkOZKKzIdzlrm7mBh4j58j5lPjIDDSu0hSuzdc55oUsBFLKm1GmZb3zZk6WJMUVFVJiN5izLFbZ85Uq1mUg9lADlG2tMIN8hAjI6%2FWrxbsYGcCJiM%2FXKCowJ72GhvpoRrGso7FeKdIGNK%2BOekneG5o2F7rZ8eBI5jpciopQ3si1yfvyGRrYW2xSJQxI1QaeWQT5PyZaFDuHaO5v4WhfRLoDWblwnEow1PzS0AY6pgEdmrSlX43yXb9Vp%2FtY5j3hHkA1dxOEYDhWtmnx278PJe0Jk1jq7qbic4MdAeq%2FQGCFhomDnjFUlBwrt8Vlu4rj%2FrBrwNt4DNrVoR4OdMJ7iChjBzGt5UFn1H%2Btqt5TilllBQ2%2Bdi%2FQTjhEUH5GxbQCAggCI%2BqIhInACaUZFAwzw%2FdFP8mZ14kdz9ZLZoAdJNeCya8hbxC0lH8eRjV4H8wmq3%2BArMsP&X-Amz-Signature=38b1203482cab23fb83571f37b681668e2a7c9f7911e15b0e755b8173e6e70eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636HAGLHN%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T225155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFzB3%2BgEsodeMjfKKV5pFVNRk7oCe9N9w7X8%2FIuessTuAiAjNxWmlzJ7bvgYoHA2OTMOb9GRHkRI8X2N8bpRp%2B6DNCr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIM6%2FGXVCfn%2BVyQw73HKtwD4GoW7jeBvUwMf7Yx4cNfxkcxZjanjG3WSMv6aeEhWaSdRcfiNuGVCIrO0u3pYGFnl2PCS3NPuakmrfK2CsWMfNkFFns7IxPu7mmnzLiYqMWKIb42IXjZnf6KvNUpp1yT2DXjWLFrAHyYJINntMWul46pQC5gc7b%2BTefLHX7DRY68e4YkD%2FTIAiBF5dxWMGuC5pDBufKF2%2F6YxKPKhXsp7PH%2Bl6peuaiJv522vn7FKn4n8f8442yb%2FcPnWIQQ3s7KbF8FwkaUoTC3mG0niVCVsUnVMjiPrHH%2FkYbXJ8cfwxXaBO%2FKnsomMlsMCLDmsgzgE9z4m2%2BcMXYaKJK9EWGimHaDj3%2BuNyLIUn9ZaXrDbWc0WGQCuF9k8I%2BrlbixqcOQZlo%2FSKVmbevVIb84zkJoKQLpDO972pkOZKKzIdzlrm7mBh4j58j5lPjIDDSu0hSuzdc55oUsBFLKm1GmZb3zZk6WJMUVFVJiN5izLFbZ85Uq1mUg9lADlG2tMIN8hAjI6%2FWrxbsYGcCJiM%2FXKCowJ72GhvpoRrGso7FeKdIGNK%2BOekneG5o2F7rZ8eBI5jpciopQ3si1yfvyGRrYW2xSJQxI1QaeWQT5PyZaFDuHaO5v4WhfRLoDWblwnEow1PzS0AY6pgEdmrSlX43yXb9Vp%2FtY5j3hHkA1dxOEYDhWtmnx278PJe0Jk1jq7qbic4MdAeq%2FQGCFhomDnjFUlBwrt8Vlu4rj%2FrBrwNt4DNrVoR4OdMJ7iChjBzGt5UFn1H%2Btqt5TilllBQ2%2Bdi%2FQTjhEUH5GxbQCAggCI%2BqIhInACaUZFAwzw%2FdFP8mZ14kdz9ZLZoAdJNeCya8hbxC0lH8eRjV4H8wmq3%2BArMsP&X-Amz-Signature=08f8322c0f3f6cc0607b4f7710ce53d983d4ce7db926444a233248c84a381967&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
