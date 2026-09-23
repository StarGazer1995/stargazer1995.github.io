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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YQCO2WP%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T020729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BgxJtVvgb%2FoJ3X8JitKTHpa3KXL%2FiZTq7Fve74fZ3dAIgbRO%2Fue5yxeZ653EazvAwK%2Fyr8Gq8puMasVuiWMvM4UEqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDxQ9JVbg4HwFhaHCrcAwtlxKMA5ggzTDBNItyCtq6ly2vJlE9nRsDm%2FNKf2peec%2FpyzBKyBCfe%2B7ggPioqIBqrbaixd0qbFRZzZmEgHHBprU9k2ePPsu161eFrSUHZR20jAsaQzfpIqOcpn4n0kVHPcyhHgpddUhG5X2NF8vx0rm38mppNIG%2F8TKnbMf46KQediCRHuCwMJBospyknFo2vgfAEIdm3HiJuKbdyefWW3ydKAomUIjOVUYADXEePHCg%2BW2xJ6EbxDFppHG%2Fgit34tJWauIKE7ycv2UTLRgnxE%2FrC4CJkKThwG%2F0QwOSEsMHcvciVqBesNcpWtElfQ9Mm8QFZVUaK3WxZbUD%2B7pOp32ha9%2BGDwe4sBHM4EgTHq%2BRzanTMFZTwkjFDbbk3PI%2FZmZmHwhO%2F%2BCeSa3XJLnjAuLAKq80jfOMzP%2Fnekk%2FQRIbkyLvDXGtsqmGRchG1gNwHZLUovICIH1ajUzlKPVlcM0iYyi7fm%2BOkYWVd5zJIjsEPlP0Quoyd4xrRNkQmcNxUMznUKdmf6X44g4Dw0a8NKc1NXOHSzP98kewKP4V7ZIV2XRHn4U2AqKmYpPcVXPNVSFtGz6vbvk%2Bdo9tpFL%2FxJvsygxNrT8L%2B86Y6tEMtpaP6Bv%2FZGHFbMREfMKDUy9UGOqUBoQ%2BeQj107TCydNk3PEe909jeoSWySfxNs1sO2sAiF8vhiE3iKaHJ4kZKkNmohf1QFhjZbg7yZ7qC0tQviT7CtNKloguE9XIg%2Bgo4%2BLRpfh3RAxydtzGMU2LRtF6EQ6q13r4TrhGN16SyIsUmyR1ijXOGoNzyFIwDrya09sBYWA5EVdI3qvJFCebOcj9Nq0Qw1rUch0R5aAikbVPoV4vuMPXDZR6A&X-Amz-Signature=7365cafa5024a4b3cf81145a1678dbb08235783499c7dec549503e4a09fe17ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YQCO2WP%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T020729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BgxJtVvgb%2FoJ3X8JitKTHpa3KXL%2FiZTq7Fve74fZ3dAIgbRO%2Fue5yxeZ653EazvAwK%2Fyr8Gq8puMasVuiWMvM4UEqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDxQ9JVbg4HwFhaHCrcAwtlxKMA5ggzTDBNItyCtq6ly2vJlE9nRsDm%2FNKf2peec%2FpyzBKyBCfe%2B7ggPioqIBqrbaixd0qbFRZzZmEgHHBprU9k2ePPsu161eFrSUHZR20jAsaQzfpIqOcpn4n0kVHPcyhHgpddUhG5X2NF8vx0rm38mppNIG%2F8TKnbMf46KQediCRHuCwMJBospyknFo2vgfAEIdm3HiJuKbdyefWW3ydKAomUIjOVUYADXEePHCg%2BW2xJ6EbxDFppHG%2Fgit34tJWauIKE7ycv2UTLRgnxE%2FrC4CJkKThwG%2F0QwOSEsMHcvciVqBesNcpWtElfQ9Mm8QFZVUaK3WxZbUD%2B7pOp32ha9%2BGDwe4sBHM4EgTHq%2BRzanTMFZTwkjFDbbk3PI%2FZmZmHwhO%2F%2BCeSa3XJLnjAuLAKq80jfOMzP%2Fnekk%2FQRIbkyLvDXGtsqmGRchG1gNwHZLUovICIH1ajUzlKPVlcM0iYyi7fm%2BOkYWVd5zJIjsEPlP0Quoyd4xrRNkQmcNxUMznUKdmf6X44g4Dw0a8NKc1NXOHSzP98kewKP4V7ZIV2XRHn4U2AqKmYpPcVXPNVSFtGz6vbvk%2Bdo9tpFL%2FxJvsygxNrT8L%2B86Y6tEMtpaP6Bv%2FZGHFbMREfMKDUy9UGOqUBoQ%2BeQj107TCydNk3PEe909jeoSWySfxNs1sO2sAiF8vhiE3iKaHJ4kZKkNmohf1QFhjZbg7yZ7qC0tQviT7CtNKloguE9XIg%2Bgo4%2BLRpfh3RAxydtzGMU2LRtF6EQ6q13r4TrhGN16SyIsUmyR1ijXOGoNzyFIwDrya09sBYWA5EVdI3qvJFCebOcj9Nq0Qw1rUch0R5aAikbVPoV4vuMPXDZR6A&X-Amz-Signature=747312ff757fa149fb14bff2490c776009ac482af123db096b449c9c53764b36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
