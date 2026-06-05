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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGEEYDF%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T112434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZKiMlu9%2FPHSTjZN0rP8o96VcwuuUYNg%2FCZ7o5fz6v7wIgRvLDu4t7FLzK8%2B3d7Grjhhz8ecF1oFVTsL9QQZSodYoq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDKOrEOBlWMl5pgV88CrcA4iuARFDrVGEr0NHWRgmY5ESl%2B2Bd9jzF2CcEa5NeSCFDgLpbjiCQ2%2FzlyoXDNrhxOfTqy99Q2Mbkq9Wi%2FDaNCYsvHzz5hCIAqmr8Tyl%2BIHmplFEjnimSPk2NAk8a%2FAiAAjHOhY9c8o%2F%2FnWXHIA53PFHWINo59uG%2FNzwhBWkoPQP0ND57tZMDuJUQjr%2Bz4idZ2MeRWMetcLBG9hBDtPIPLo6usWozZE9LNdHSGMMmupqoiwjFy1q4T0tZEUFSapj6ztex8vn7IIJ%2B33KEnAqU9oSUK%2F4YAOzcr1TSixdjFRrpAo3njZ9asU03rCOu7cpm3x0N%2F1EhrA9liprL8JpiK9bJGu2sycFBHReSL2clVXM9ofAyZC93tiIvlJinFINRzcnyZ2koLaTCtHkjZ52I%2FBM885u%2BDEWW02FHemgaeAASV5Kj%2FTcc%2FtElGCb4pKbyw44GfAK%2B08PUf0uOCHb%2Fb52l%2B8n1mBB4qvrMxw5mpdmmcwK9QGvpawlHZQWATOa2eK7OCwN6aBtJ0ANHA2wdD8yHZlR80ny7gihdF5jQjQ07NaCQDZcksDAB%2FiDXRKcxt4Ua4Oa%2BcUdzCx59xQ5iUvnqYZZulmtiNC0woSTOO%2FhUnl6feofm9s4LOBCMIO8itEGOqUBP9jrRRL%2F7hM3FHlCF%2BbqpPP8HL0%2BVPS5byDPpvqVzwvOYfEoCjBrF8Gm0H4AIjBNTbFiKA9jPoSaMm1ciN5%2F6gOODItVhpO4wCdWPiktti2M4ZA0jHe5LmrxJit0KsMIW6itVdAtGCEAi6SCXbSDr6PyYf%2Bqb2vnEDdPwn%2BXE9NAEIpLGAGxYtnTKQP%2FaRVSfEbeX7BewLqgiAdKB0MeOowaxsHR&X-Amz-Signature=68e6b00a233ae7cc0e9792d500f6779f5e5f45d2ab0dcfda7f2cf4daa90e4317&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGEEYDF%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T112434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZKiMlu9%2FPHSTjZN0rP8o96VcwuuUYNg%2FCZ7o5fz6v7wIgRvLDu4t7FLzK8%2B3d7Grjhhz8ecF1oFVTsL9QQZSodYoq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDKOrEOBlWMl5pgV88CrcA4iuARFDrVGEr0NHWRgmY5ESl%2B2Bd9jzF2CcEa5NeSCFDgLpbjiCQ2%2FzlyoXDNrhxOfTqy99Q2Mbkq9Wi%2FDaNCYsvHzz5hCIAqmr8Tyl%2BIHmplFEjnimSPk2NAk8a%2FAiAAjHOhY9c8o%2F%2FnWXHIA53PFHWINo59uG%2FNzwhBWkoPQP0ND57tZMDuJUQjr%2Bz4idZ2MeRWMetcLBG9hBDtPIPLo6usWozZE9LNdHSGMMmupqoiwjFy1q4T0tZEUFSapj6ztex8vn7IIJ%2B33KEnAqU9oSUK%2F4YAOzcr1TSixdjFRrpAo3njZ9asU03rCOu7cpm3x0N%2F1EhrA9liprL8JpiK9bJGu2sycFBHReSL2clVXM9ofAyZC93tiIvlJinFINRzcnyZ2koLaTCtHkjZ52I%2FBM885u%2BDEWW02FHemgaeAASV5Kj%2FTcc%2FtElGCb4pKbyw44GfAK%2B08PUf0uOCHb%2Fb52l%2B8n1mBB4qvrMxw5mpdmmcwK9QGvpawlHZQWATOa2eK7OCwN6aBtJ0ANHA2wdD8yHZlR80ny7gihdF5jQjQ07NaCQDZcksDAB%2FiDXRKcxt4Ua4Oa%2BcUdzCx59xQ5iUvnqYZZulmtiNC0woSTOO%2FhUnl6feofm9s4LOBCMIO8itEGOqUBP9jrRRL%2F7hM3FHlCF%2BbqpPP8HL0%2BVPS5byDPpvqVzwvOYfEoCjBrF8Gm0H4AIjBNTbFiKA9jPoSaMm1ciN5%2F6gOODItVhpO4wCdWPiktti2M4ZA0jHe5LmrxJit0KsMIW6itVdAtGCEAi6SCXbSDr6PyYf%2Bqb2vnEDdPwn%2BXE9NAEIpLGAGxYtnTKQP%2FaRVSfEbeX7BewLqgiAdKB0MeOowaxsHR&X-Amz-Signature=5cb5df4286c8565e94bdb901d4c5e372cc27e929541c48ac1e56486499d48444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
