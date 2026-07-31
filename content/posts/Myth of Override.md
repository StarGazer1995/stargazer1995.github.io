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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWQ7HM4G%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T132735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3%2FFs57LeSFT%2F1BPHiIl5xVz4udIfciOER%2BqAXdivfzwIhAMOkJ7%2BjaSetqbjo81hywgNjElld%2FG3SQsqE2MOprKlNKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLK2MFF0Z9HHEyUdwq3ANrIZIL0%2BURQRTlIH%2BmhrApEbXBaJfK%2BRR2DBQxEWCIS%2F5%2F%2FxsbsRn70A91iMp%2F3owhfS7YU9LRNkplVyAzaicQYWW2iSYF%2FLD5%2FKZfKp2%2FvRRRyfcUFrAjx7P9YoSBd7qAS2JSX9aRiMUYrP7u3GCV9M%2BVMMsV073oy7c8ks%2BSJR8%2FopL9anLQNUHstelSA2hxlwDIyL71a7EjLOSANyPJfGA2nXqEJonpNOrwJfPNzhP9%2BQ5PF37tYg3R8rnqNVG8Wy3kbCVaOq3AFfqVq7gUB7igg1109dq%2FtmHCNfsBPb%2FrTOMpsc4KP2NW2wEYTWt4pT1JTQ4Ay6UmKRLwaZucp5ptLnL5iex3LXX4YI%2Bp7tJkf6%2Be68rHehptYk00NFiMJTp4dWZPxEa4JQTeq3pwb8Ye1dHmxOUtjvAbCb3rNjlEQp0jwfQ6qW1lAEpo4YDR%2BEA2mVqdoDfZZrpX3KCLjIyfdwPnxQJWRhIE2kzVRvkjMvML13mtEnmueJOewZ1jWnYWPwQgLh%2BvUVSzg0UCJT030EA7JXLtYangAN0S%2FXpgZFeKQRBLNzuf62Vl6qjpeaqxp75xD%2FE0J6kNjLEh6NVSggK4J40zLRgdK1LvvoPHxAfC5O8VmNXxdDCGpLLTBjqkARrTGnBfTO14uc4SLT%2Bf9%2BpRHyp4EvNmxqOFzheLkfmfNVYp5RZg%2FSODK%2FMBqPnE7fOUqrh0N8bEngcPhg5zsUnfs9cvKvIP4zWxUKMK71D6E3IpX1wOebh3gXV4EaeibO49xotsFKwE3AFHwsuZFb1bxBBHvkoBnVZx1HIMyHMz6j%2B6HyGASpCxfPF8b9%2BsTb6bge7A8OSQl4ZWtRJcIO1rskiu&X-Amz-Signature=c1e7a61902c9c7eaffcc82c5d4e2a7b8379b8d9b60068dd59d5a266060801f64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWQ7HM4G%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T132735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3%2FFs57LeSFT%2F1BPHiIl5xVz4udIfciOER%2BqAXdivfzwIhAMOkJ7%2BjaSetqbjo81hywgNjElld%2FG3SQsqE2MOprKlNKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLK2MFF0Z9HHEyUdwq3ANrIZIL0%2BURQRTlIH%2BmhrApEbXBaJfK%2BRR2DBQxEWCIS%2F5%2F%2FxsbsRn70A91iMp%2F3owhfS7YU9LRNkplVyAzaicQYWW2iSYF%2FLD5%2FKZfKp2%2FvRRRyfcUFrAjx7P9YoSBd7qAS2JSX9aRiMUYrP7u3GCV9M%2BVMMsV073oy7c8ks%2BSJR8%2FopL9anLQNUHstelSA2hxlwDIyL71a7EjLOSANyPJfGA2nXqEJonpNOrwJfPNzhP9%2BQ5PF37tYg3R8rnqNVG8Wy3kbCVaOq3AFfqVq7gUB7igg1109dq%2FtmHCNfsBPb%2FrTOMpsc4KP2NW2wEYTWt4pT1JTQ4Ay6UmKRLwaZucp5ptLnL5iex3LXX4YI%2Bp7tJkf6%2Be68rHehptYk00NFiMJTp4dWZPxEa4JQTeq3pwb8Ye1dHmxOUtjvAbCb3rNjlEQp0jwfQ6qW1lAEpo4YDR%2BEA2mVqdoDfZZrpX3KCLjIyfdwPnxQJWRhIE2kzVRvkjMvML13mtEnmueJOewZ1jWnYWPwQgLh%2BvUVSzg0UCJT030EA7JXLtYangAN0S%2FXpgZFeKQRBLNzuf62Vl6qjpeaqxp75xD%2FE0J6kNjLEh6NVSggK4J40zLRgdK1LvvoPHxAfC5O8VmNXxdDCGpLLTBjqkARrTGnBfTO14uc4SLT%2Bf9%2BpRHyp4EvNmxqOFzheLkfmfNVYp5RZg%2FSODK%2FMBqPnE7fOUqrh0N8bEngcPhg5zsUnfs9cvKvIP4zWxUKMK71D6E3IpX1wOebh3gXV4EaeibO49xotsFKwE3AFHwsuZFb1bxBBHvkoBnVZx1HIMyHMz6j%2B6HyGASpCxfPF8b9%2BsTb6bge7A8OSQl4ZWtRJcIO1rskiu&X-Amz-Signature=348028db1f60d89ff593e38d327bd495f32ace58e2b2f9797a11cf7fe3df2002&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
