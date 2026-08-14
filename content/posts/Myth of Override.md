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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GXPTABY%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T184556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQC%2Fg9ELoZQGHaNlKWbR3s3wQEH7MdKaXp1Nxn0q%2BTBLzQIhAJBKTE9s4KlyfktG57QobHc7zBxB6%2FfnvrS%2Byprpp0A4Kv8DCAMQABoMNjM3NDIzMTgzODA1IgzKlwArFhy5s%2BMakR8q3AMFwq%2FUBVbEwkTI5FaWZOg%2BK%2FaXGkWgVEoZI5xF%2F4FBx4FduyYTDE4VOj3UCHEV1qydc2%2BY0kbbXT2BioobFdrDAew%2FoM3rwNzQZOgjtKyfmUNb1vJEjtSzfqWXHK99XKvNwUGYM5suVgftFdvdWxiqNyN6PXJPhM%2B1w4ufCwYadWanuEiKszrljLzY02n9iSWKFWNAifiBe2dJqSYXsOXN50Guv8wxIU0F50XVwWYOYmBQugtS%2F3Cm7LLEa3ZQTQSXeCZddZdn8HnAswyQu7wEzxzTOjbV%2B%2FGcihUEeI0gzEEoOUY69%2B6JMvZYRAIFdIVOwVXZqgc%2BLumILHF5tsPfEyA9bApjPWcYxrvbu1GdHjZ8QfcVNYDBcNF2K%2BDECD4eEYXIiXjuiXsnz%2BcovgAdJmn7%2FWLoU7TpmmI%2BdxZvX1b9cLldwwKwk4c5b7WyXnyh5vhqAKDx%2B1nBvvLWlCSXAloYDnwCYUyGiUzaLkNVz6%2B5tak6Ar549K6uDpNGyIH5l2JBaoBf3oqDtGCPThBZnZhunKZS%2FHgRLGdatIZQU4RzSs5FAZU5kHtB9oI8gBYL7q5JiwTwvWXfQvceMLdaeTPFCZIbKr0V8zKPVU9E8rVnsF2ynfshPdb4ljCMuP3TBjqkAQpc6S2ucHJJZ%2BXh65lg8q8FqNKPzunw1%2BWEh0p5HEkf7mPGM3DOj%2FG0yGRLQcKZSu4yfn%2BK8quVilLuD5%2BjbeNyynfdK671hPVXJmFUX8VFxg7tdgB7YxSCLU7YZ4idOZMkXFebvtmttN%2BEetEbz%2B1AgNFwnzvyGPEMsZxkbYqYNDrPCvIuvmyySIPXd99qbDUaU%2F2N%2BWJzX4l7RjnyE64Do%2Bk6&X-Amz-Signature=8cece8ac11b63531e2d45964f27266beb61a6441e493bd87e020cfcdd5365f23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GXPTABY%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T184556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQC%2Fg9ELoZQGHaNlKWbR3s3wQEH7MdKaXp1Nxn0q%2BTBLzQIhAJBKTE9s4KlyfktG57QobHc7zBxB6%2FfnvrS%2Byprpp0A4Kv8DCAMQABoMNjM3NDIzMTgzODA1IgzKlwArFhy5s%2BMakR8q3AMFwq%2FUBVbEwkTI5FaWZOg%2BK%2FaXGkWgVEoZI5xF%2F4FBx4FduyYTDE4VOj3UCHEV1qydc2%2BY0kbbXT2BioobFdrDAew%2FoM3rwNzQZOgjtKyfmUNb1vJEjtSzfqWXHK99XKvNwUGYM5suVgftFdvdWxiqNyN6PXJPhM%2B1w4ufCwYadWanuEiKszrljLzY02n9iSWKFWNAifiBe2dJqSYXsOXN50Guv8wxIU0F50XVwWYOYmBQugtS%2F3Cm7LLEa3ZQTQSXeCZddZdn8HnAswyQu7wEzxzTOjbV%2B%2FGcihUEeI0gzEEoOUY69%2B6JMvZYRAIFdIVOwVXZqgc%2BLumILHF5tsPfEyA9bApjPWcYxrvbu1GdHjZ8QfcVNYDBcNF2K%2BDECD4eEYXIiXjuiXsnz%2BcovgAdJmn7%2FWLoU7TpmmI%2BdxZvX1b9cLldwwKwk4c5b7WyXnyh5vhqAKDx%2B1nBvvLWlCSXAloYDnwCYUyGiUzaLkNVz6%2B5tak6Ar549K6uDpNGyIH5l2JBaoBf3oqDtGCPThBZnZhunKZS%2FHgRLGdatIZQU4RzSs5FAZU5kHtB9oI8gBYL7q5JiwTwvWXfQvceMLdaeTPFCZIbKr0V8zKPVU9E8rVnsF2ynfshPdb4ljCMuP3TBjqkAQpc6S2ucHJJZ%2BXh65lg8q8FqNKPzunw1%2BWEh0p5HEkf7mPGM3DOj%2FG0yGRLQcKZSu4yfn%2BK8quVilLuD5%2BjbeNyynfdK671hPVXJmFUX8VFxg7tdgB7YxSCLU7YZ4idOZMkXFebvtmttN%2BEetEbz%2B1AgNFwnzvyGPEMsZxkbYqYNDrPCvIuvmyySIPXd99qbDUaU%2F2N%2BWJzX4l7RjnyE64Do%2Bk6&X-Amz-Signature=88f54bba0b3b6cd485e14ef934f4c708fd979dd5aeb7f039b6f999a1f72d7991&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
