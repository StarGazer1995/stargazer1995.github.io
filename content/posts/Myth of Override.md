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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDOSSQF%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T045733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHHBUnhuoLKwFgKHJ%2FGSJ6oLjskzzhGxn5oewwZC4zesAiAtErQrS5iGTRONEj6tGMHaLc5KjuszceqdU5Z27CgnCiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHtwMY9%2FfSwhLnsjHKtwDZVaNa7yQgIXjt8K260mZePElWhc7x51SZuzZDLMUGjd03dNveEQunEMXtEC6o%2B%2Fkv2w6vC2gY%2BjjR1vBtguhLNRRz%2FpvnFUIIpzTi3DV4%2FM5idElpkv0peVECmb17ZWFuXMU2Id0Wu0his22maAhTw%2BxlZIE%2BB8sqQ87cJp4g1SHGjlyiBlO7j36dA4fsVGQgAb3sGOxoZYz2c65Tq3fV3oLhTiSj2gyFjRzAvqtz%2BVAz01t5KxSqD68zamluR7LNeAlxrJbPjcSQrQ079vFlrY144XsZqcHvU4pcwoTJdp5BZOMuDvMEoCiE%2BYvUzhi5jyqj7z1l89cLf3teQ0ULW42m6xWOcxtF07e%2Bw6NlMDuucleDSN6DWEJQYh0zmu2hYhTKuhrcLkjSsctcZ%2FqofjyMovwgMHspE8Nx2Kp77DxEtWziQYSf7tyyD3bx2jyfMkvzJULHsmcGSiGg4%2Fsq2iJhjAa3Rx2L8OBjxhklYVc2w8Y6Djq5Y1aLSZ3SZyMCxINutCzB%2B8x5XeL6T8gJ2lH%2Fo2OSfsHcNRdZbxTOF1K3NAu3WYBoh2oV7dwrCvGYWK0fCzvjJN48EvuYkEYXLYg%2BU7koHbDrlDdSPcXOWtXeRu3lCBL1PtcQKIw5NLq0wY6pgF58P3L%2FqeEEpdkI352o1yr0W9MAjvfVD6Zfikdf%2F5y%2BdsmHT7ke6oDT7tRrmRohQpKxPrT86Hp8QRt0MUzheo1k40ilXLq7gE2tl0Xy%2F3%2BO7cZdG0ltM8q1vvCaAkaaVLtT3Lt%2BLkX5olFM1srEip%2FhDqBPfO9c3%2B9mLDxehzgs9GCTCaiiXjHRD95k2iRO1g%2BMP74MJvrJP%2FfIwV3xSFBSHez2Rcr&X-Amz-Signature=be3ce49d24e7e4356ef30cd432f18319edfcdaef5e412ec75d8825bf490a53af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDOSSQF%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T045733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHHBUnhuoLKwFgKHJ%2FGSJ6oLjskzzhGxn5oewwZC4zesAiAtErQrS5iGTRONEj6tGMHaLc5KjuszceqdU5Z27CgnCiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHtwMY9%2FfSwhLnsjHKtwDZVaNa7yQgIXjt8K260mZePElWhc7x51SZuzZDLMUGjd03dNveEQunEMXtEC6o%2B%2Fkv2w6vC2gY%2BjjR1vBtguhLNRRz%2FpvnFUIIpzTi3DV4%2FM5idElpkv0peVECmb17ZWFuXMU2Id0Wu0his22maAhTw%2BxlZIE%2BB8sqQ87cJp4g1SHGjlyiBlO7j36dA4fsVGQgAb3sGOxoZYz2c65Tq3fV3oLhTiSj2gyFjRzAvqtz%2BVAz01t5KxSqD68zamluR7LNeAlxrJbPjcSQrQ079vFlrY144XsZqcHvU4pcwoTJdp5BZOMuDvMEoCiE%2BYvUzhi5jyqj7z1l89cLf3teQ0ULW42m6xWOcxtF07e%2Bw6NlMDuucleDSN6DWEJQYh0zmu2hYhTKuhrcLkjSsctcZ%2FqofjyMovwgMHspE8Nx2Kp77DxEtWziQYSf7tyyD3bx2jyfMkvzJULHsmcGSiGg4%2Fsq2iJhjAa3Rx2L8OBjxhklYVc2w8Y6Djq5Y1aLSZ3SZyMCxINutCzB%2B8x5XeL6T8gJ2lH%2Fo2OSfsHcNRdZbxTOF1K3NAu3WYBoh2oV7dwrCvGYWK0fCzvjJN48EvuYkEYXLYg%2BU7koHbDrlDdSPcXOWtXeRu3lCBL1PtcQKIw5NLq0wY6pgF58P3L%2FqeEEpdkI352o1yr0W9MAjvfVD6Zfikdf%2F5y%2BdsmHT7ke6oDT7tRrmRohQpKxPrT86Hp8QRt0MUzheo1k40ilXLq7gE2tl0Xy%2F3%2BO7cZdG0ltM8q1vvCaAkaaVLtT3Lt%2BLkX5olFM1srEip%2FhDqBPfO9c3%2B9mLDxehzgs9GCTCaiiXjHRD95k2iRO1g%2BMP74MJvrJP%2FfIwV3xSFBSHez2Rcr&X-Amz-Signature=be2dcfbabc7e98b48ef94322c67ad3d7b1d88b023cff05cbfcd78b5fcef16eab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
