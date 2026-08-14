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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5BCR3U3%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T202105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQCHsEp4D%2BO9uIpGl3Dt4QVWP06c%2FClYTSi%2F5nPxCRKKUgIhAOyhTfDQ%2FFn%2FCH03k%2BC2Sod4Dr4aSQm64UOAjpoTBqj8Kv8DCAMQABoMNjM3NDIzMTgzODA1IgyipbIvibnyQ%2BPw0YIq3AOXQhmbXY5kR2Ah4uuzXi4bBCpJnV6kDbWU93RcVDvBn1aY%2FSIW5wMQD2wa48hUN9WYWmP0SR2JSMPa9NJEluG%2BwtGBjnS7G1FVyKWwjudzzsLtH%2Fph%2BG8O73Jykn%2BauzSNcFpZ%2Bd95s6aX%2FKOYgF3IErKjdvj7hg80IYpTFGRgqtAkL%2Bv0UtSbfOaxtKHgbH39FGnTv4IKV2J0Glq3Ao7L3OWg3IMy2k2HToCQOzgxRy%2FaMRHKyrsMtdTCxiR8%2BI1oADohdXh25E4uF33UyDxJuoxgBHT%2B6VKHC6Ae2wBr%2BomH8IVgNJDozVDLK9s577EfDVQCgB2PO2VvX5PGUzNYawa0CbBGNikYEgM7PZQY5q7%2BcJYQKBARmiNGHCozmbL0%2B5EMX3mQ47JgqU4KPMxBvTpVeIQH9jVK5dQ3npU%2Bl9T2%2FYvesGh10BEwJsbMizv8Ny1nEtUmQopNl7TVLuIwahgRqDopcAcVZQSyL1OCXwHjT3GN9ua3vcuuaD9XPv3%2FKcab6fjxispvF1ixnUOlwkq2rE4jVOJcsSqUKee33fJrZS2lT%2BjOtJFWovUUASKcdpaqeYOzTkQNffIEp1Nhr1kif%2BpBg7v7UACZYR8ERcXrMjJregdkQYTh4DCcuf3TBjqkAaE4rPD2S9JCKEUrQVSheAlujL1y8ot0G%2B4Y5n5YBOQUU0uSNmstUDGbDsHadDga9rURzmQ2h%2BiJSQ0TPsTsXXy8P2NdW%2F8J2n23rFsHTynWpKbJjJD6XNc37bJZJ3%2BZCGC3vua9x2O37%2FsR0JsE6bIfEUuPpOGp8nj5cwHnbxx8CuC32NEX8e6dEcZtIIWo3oxM8YWass7Qc6VekEa3U15lMhOA&X-Amz-Signature=cd6eb3b1393a2cf3194cc01ce89c9a1851e6ea6e723be948d253cf4ad1554563&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5BCR3U3%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T202105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQCHsEp4D%2BO9uIpGl3Dt4QVWP06c%2FClYTSi%2F5nPxCRKKUgIhAOyhTfDQ%2FFn%2FCH03k%2BC2Sod4Dr4aSQm64UOAjpoTBqj8Kv8DCAMQABoMNjM3NDIzMTgzODA1IgyipbIvibnyQ%2BPw0YIq3AOXQhmbXY5kR2Ah4uuzXi4bBCpJnV6kDbWU93RcVDvBn1aY%2FSIW5wMQD2wa48hUN9WYWmP0SR2JSMPa9NJEluG%2BwtGBjnS7G1FVyKWwjudzzsLtH%2Fph%2BG8O73Jykn%2BauzSNcFpZ%2Bd95s6aX%2FKOYgF3IErKjdvj7hg80IYpTFGRgqtAkL%2Bv0UtSbfOaxtKHgbH39FGnTv4IKV2J0Glq3Ao7L3OWg3IMy2k2HToCQOzgxRy%2FaMRHKyrsMtdTCxiR8%2BI1oADohdXh25E4uF33UyDxJuoxgBHT%2B6VKHC6Ae2wBr%2BomH8IVgNJDozVDLK9s577EfDVQCgB2PO2VvX5PGUzNYawa0CbBGNikYEgM7PZQY5q7%2BcJYQKBARmiNGHCozmbL0%2B5EMX3mQ47JgqU4KPMxBvTpVeIQH9jVK5dQ3npU%2Bl9T2%2FYvesGh10BEwJsbMizv8Ny1nEtUmQopNl7TVLuIwahgRqDopcAcVZQSyL1OCXwHjT3GN9ua3vcuuaD9XPv3%2FKcab6fjxispvF1ixnUOlwkq2rE4jVOJcsSqUKee33fJrZS2lT%2BjOtJFWovUUASKcdpaqeYOzTkQNffIEp1Nhr1kif%2BpBg7v7UACZYR8ERcXrMjJregdkQYTh4DCcuf3TBjqkAaE4rPD2S9JCKEUrQVSheAlujL1y8ot0G%2B4Y5n5YBOQUU0uSNmstUDGbDsHadDga9rURzmQ2h%2BiJSQ0TPsTsXXy8P2NdW%2F8J2n23rFsHTynWpKbJjJD6XNc37bJZJ3%2BZCGC3vua9x2O37%2FsR0JsE6bIfEUuPpOGp8nj5cwHnbxx8CuC32NEX8e6dEcZtIIWo3oxM8YWass7Qc6VekEa3U15lMhOA&X-Amz-Signature=866810f4e3e43f31d2739a2d0c9cfa8163333a190cd3473dca30c4b12531f4ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
