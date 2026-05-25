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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HR5W3IN%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T020704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2FJUKJyEADpw5vL%2Bi2tNJ5xqWBbwu8lFppRwaNHiL3QIhAOHajJ7f%2ByA8djazoGKS9G0NsgM9rMJXyrwUkqBhpHjjKv8DCFoQABoMNjM3NDIzMTgzODA1Igy6uWylskiLz1fOEfIq3AOtlCDbpw7x6kLfK1BRGdVqOjM%2F5b%2B2kthPyf2Cag7cHX93Aszske6D9U%2BavjzCECaaXSqU121DDw%2BKwoZEGSZ4F4a27prbUH7qDtrz34oK%2B3rCIZ3%2BmmB9AQGzc2udl8uwUqoNHJ9FuNGekQEqmhacckYr%2FetxQ8bpfPxbaIC9VeEnID41sFiu%2FuJb5K1x8lii1zpm4U7qbhLm0k2H0gssaYrUDr2mVZygX0eCkBhDJcwzu4imQ3BC5qgLgNJBOdUaK%2FButdhsUanaMwbssTn1wuFJHF6aWLX%2B3mZ3Y5qMVs1o7qVdTNKpym1a8kBaEFM6REsP%2FX85T8%2BcQFd%2FOfjlF2gn4BwN8cSm7HljZbfBQCuLfn5jMnSnHLiZrRzYg7VQs5QE%2BOloqsVjM9wcvEDimsczpQ%2FJ1RKu6HkzNIHsQDKH429NzYFUG3J%2FmcSBeUMCJn5eNLhTQDCda02Mv%2B3SXF0FcawLDHhOz297zj5lOPcs4kLo0Uq7xma4838OWFczFvWQaioZmPSUFtRacyJS%2BIdSlSMHXl3H1DOla0SyS%2Btf4MXX8l4sQPnXk%2BxN1iy4IsM5Q5CrSI1JgaLbuOmIvtkK6CcF9TqzQlhrKDfIDc8HOQbv4BpvqK881DDJs87QBjqkAW0JFUhPBWcujdonT7eyrsnWIy%2FSdEEkVoCBnMWwWijFYmDOLoNFTHDKaX1f8A9A3xyE71kxAdXuSLEaWWxDET0TfcmCcddUi1mOK%2FIIF8bVfyzZEo5bJacGYQDqz%2FuIgDTsHThNzyarkLp2otgZj0hwvhWmz6R459WemvCqaQe5I1nWCe3oau%2F9CjwKPRXyfB%2B4PuHUiYdk2yDL5WuyTZqJt%2FlG&X-Amz-Signature=044dd7a9090d0a282d962ccf35f6ce096fb2f5c591da6a051180656feaeabf64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HR5W3IN%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T020704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0%2FJUKJyEADpw5vL%2Bi2tNJ5xqWBbwu8lFppRwaNHiL3QIhAOHajJ7f%2ByA8djazoGKS9G0NsgM9rMJXyrwUkqBhpHjjKv8DCFoQABoMNjM3NDIzMTgzODA1Igy6uWylskiLz1fOEfIq3AOtlCDbpw7x6kLfK1BRGdVqOjM%2F5b%2B2kthPyf2Cag7cHX93Aszske6D9U%2BavjzCECaaXSqU121DDw%2BKwoZEGSZ4F4a27prbUH7qDtrz34oK%2B3rCIZ3%2BmmB9AQGzc2udl8uwUqoNHJ9FuNGekQEqmhacckYr%2FetxQ8bpfPxbaIC9VeEnID41sFiu%2FuJb5K1x8lii1zpm4U7qbhLm0k2H0gssaYrUDr2mVZygX0eCkBhDJcwzu4imQ3BC5qgLgNJBOdUaK%2FButdhsUanaMwbssTn1wuFJHF6aWLX%2B3mZ3Y5qMVs1o7qVdTNKpym1a8kBaEFM6REsP%2FX85T8%2BcQFd%2FOfjlF2gn4BwN8cSm7HljZbfBQCuLfn5jMnSnHLiZrRzYg7VQs5QE%2BOloqsVjM9wcvEDimsczpQ%2FJ1RKu6HkzNIHsQDKH429NzYFUG3J%2FmcSBeUMCJn5eNLhTQDCda02Mv%2B3SXF0FcawLDHhOz297zj5lOPcs4kLo0Uq7xma4838OWFczFvWQaioZmPSUFtRacyJS%2BIdSlSMHXl3H1DOla0SyS%2Btf4MXX8l4sQPnXk%2BxN1iy4IsM5Q5CrSI1JgaLbuOmIvtkK6CcF9TqzQlhrKDfIDc8HOQbv4BpvqK881DDJs87QBjqkAW0JFUhPBWcujdonT7eyrsnWIy%2FSdEEkVoCBnMWwWijFYmDOLoNFTHDKaX1f8A9A3xyE71kxAdXuSLEaWWxDET0TfcmCcddUi1mOK%2FIIF8bVfyzZEo5bJacGYQDqz%2FuIgDTsHThNzyarkLp2otgZj0hwvhWmz6R459WemvCqaQe5I1nWCe3oau%2F9CjwKPRXyfB%2B4PuHUiYdk2yDL5WuyTZqJt%2FlG&X-Amz-Signature=ef874243b6c5d97185a2620869b92da3176fdb2c8453e6a45f6502f9c4050aca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
