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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBXS3OPJ%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T063207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZTYPc5Z42S6phA9KxRhUpF1vSaZjGovL4uR8XgXTPcgIhAJxayOgWi9R7ZkIpspGoougv%2B7FxzapugeKRx%2FMA0pUKKv8DCGYQABoMNjM3NDIzMTgzODA1IgxuXROrGwknLT7Z31Iq3AO%2FgPLzI33%2Fe6PhPn4QTfcWsZQ9wcQZHa1FTaZOYtD3CqnPPG%2FUM16Jorp2MEzsfnDUeSv1KcxKQ8S8GyfD0FYfHHgQJMRxBSfyqt6hDXwmbVBEHiG3dTXGMhiiyNLW4QCVSS7a1YcspBe0a2OLV3cHHLusf2Ri4WH%2BJ1JdNRxPOUyjlqv83g3PUUacdw%2FqVoVSR7a%2FTr2Te2lu2ywLmQAgdU2HbxuZHsXjMATsxVWIXuX7SSfMQz%2Fd%2FgkcDixHE9bc%2FUSTfyKoHT2KJNiVxb7HChC0%2FKwtlRB43RrJ2eH3ZDp1kBirBQ%2FtNimH7KmUtVghJiE9T6o7xpscNrfQd90STImdvHiNBxicYU2aPd6sZpi9HPIaUeXGEd4kH9Vv4FNuikWupA4eaCzUZJFWImML9kG4ARXrcUSrCzuxQQZMZvHWiD9H%2Frbss2Lrgf4F8483Wv2hhFdRoq1fi9gq0xbMiziFgUBKUctdxA4DcwtKq%2BKtFrB%2Ff1AhCExsNO0CZf7B4ZUvzwYiyOCqbpEn%2FLC2EIjUtu3TeFuLb0EasSfMVVu4LQcR4pgCSOGMpQAqx3OxKlc6a3jRk34pwwAvDj8S72A0kceQ%2FjSqRenxWXCSoxTs6kcx%2FCcfyBrhsjDG7drTBjqkAdCS5JV%2FWdu4b1q1Lbqt42KFFtFyDKw2JNu2Se1iainUXOqSPU59AW3Px93oydJNh6xMjiglcPfhf8%2F4sjeMx5PBnaZCsiT77C%2BYLd2NKEn8v3lL3bBGnKY4WURf2JHw6glNdS7arhmuxOOvhFM1D7T7esQpYEzfeFhU0bnRqJMNfxd4YFW31%2FN5m5k0nDSDf3KDFdSz8TSqKxydyHkd32ZJt82f&X-Amz-Signature=47d1baf1516ff08ac918d65cc57da6f1feb9233ee76a6f1d7a625987a05248c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBXS3OPJ%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T063207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZTYPc5Z42S6phA9KxRhUpF1vSaZjGovL4uR8XgXTPcgIhAJxayOgWi9R7ZkIpspGoougv%2B7FxzapugeKRx%2FMA0pUKKv8DCGYQABoMNjM3NDIzMTgzODA1IgxuXROrGwknLT7Z31Iq3AO%2FgPLzI33%2Fe6PhPn4QTfcWsZQ9wcQZHa1FTaZOYtD3CqnPPG%2FUM16Jorp2MEzsfnDUeSv1KcxKQ8S8GyfD0FYfHHgQJMRxBSfyqt6hDXwmbVBEHiG3dTXGMhiiyNLW4QCVSS7a1YcspBe0a2OLV3cHHLusf2Ri4WH%2BJ1JdNRxPOUyjlqv83g3PUUacdw%2FqVoVSR7a%2FTr2Te2lu2ywLmQAgdU2HbxuZHsXjMATsxVWIXuX7SSfMQz%2Fd%2FgkcDixHE9bc%2FUSTfyKoHT2KJNiVxb7HChC0%2FKwtlRB43RrJ2eH3ZDp1kBirBQ%2FtNimH7KmUtVghJiE9T6o7xpscNrfQd90STImdvHiNBxicYU2aPd6sZpi9HPIaUeXGEd4kH9Vv4FNuikWupA4eaCzUZJFWImML9kG4ARXrcUSrCzuxQQZMZvHWiD9H%2Frbss2Lrgf4F8483Wv2hhFdRoq1fi9gq0xbMiziFgUBKUctdxA4DcwtKq%2BKtFrB%2Ff1AhCExsNO0CZf7B4ZUvzwYiyOCqbpEn%2FLC2EIjUtu3TeFuLb0EasSfMVVu4LQcR4pgCSOGMpQAqx3OxKlc6a3jRk34pwwAvDj8S72A0kceQ%2FjSqRenxWXCSoxTs6kcx%2FCcfyBrhsjDG7drTBjqkAdCS5JV%2FWdu4b1q1Lbqt42KFFtFyDKw2JNu2Se1iainUXOqSPU59AW3Px93oydJNh6xMjiglcPfhf8%2F4sjeMx5PBnaZCsiT77C%2BYLd2NKEn8v3lL3bBGnKY4WURf2JHw6glNdS7arhmuxOOvhFM1D7T7esQpYEzfeFhU0bnRqJMNfxd4YFW31%2FN5m5k0nDSDf3KDFdSz8TSqKxydyHkd32ZJt82f&X-Amz-Signature=8d936e567ed9391deea4d06e9752d0188edcf43ad349d6798624f1d8b737a0c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
