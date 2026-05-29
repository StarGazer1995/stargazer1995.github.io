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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U55POQWK%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T213224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDZQt3rkFhgnmXnw0gC1QPBRL6SfN7zIG%2F0uf9g0FSwugIhAMcg93qHKikQvTqvkRQuxkS4okxd1ALou2HxbkVH0rkXKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcU8UN2P0mRq8vYgq3AN8735sMVYiYQYeEwVwykNAwCXd1f50PheVwq4LXdCjZHU0GxQRksQhSnn5CeGtU29khgGqT%2F3%2BJONuEiODsHySazHPD9lOGFbd1rXvheFlx2WbrWUGtegGLCdMPBShO7BtqEVsMz49oneq6tg11gGPetcLmcIFJe8YyLqxWnBPIsV113PIIo7nqvjDzb3Qk3mwJMW4e1lgKf3SQRmrLXVjAskraKo89wYy8eO99kwmlW6EiV9f71PBFzyik1eoWO7%2Bi1YMZWEu7GOChcfDZ0iBn4aLKaOhqSaLaKDhJzsQgmIwpUSTv65wNIQpmRic3zlB%2FtX42lYE9MOrPpmbdJwZ0MP%2FOSMr3Pc%2FNGAX%2FZBLMpdMgRcpOO9DK%2FfL9nBCFfy5l69uT0nUtO%2F8HD4HtUucNN6YrEhlTDh4ESLuq%2BaUQXuz3%2B7JnYLqzQSR9d2qiwSyAvh1ezK516b%2BvHGlUx2iAN3KB0eZ79%2BJ3uH342W%2BK2JR187EWo4bPT4E0v0aBy9UpOUNirbjJ19mJPSz3pC86wvlNi26%2BNsmTD%2FLn6pDjiBkuIHcoPC5d4pFTDif%2Ffq%2BVL%2FjIKbJom%2F0moHUoeAI36zjEiBWfwuyx2CAMp5%2BWCeiIIGDYJCLm93k1jCT3%2BfQBjqkASxVPTSwa9QDMBotdX8x1EvnOwnjb5IGSgUycyfWYnzWMt6YQ4lZaRuGoo50p99QkQHwNZUo%2B18z0F5XsFn6CHuU6RI8R%2BAPQMRyTrcNFXVURbrd1R172v9dB12iNOWXadtnWMVT0lw9lhPOB8KtKuOQmwVsdxdDRF9YdjQg0WihPcpyV7uDIjI0dKu3estml837%2BSaPJX84Zsz%2Bb08sK6q8Xb%2FM&X-Amz-Signature=f9f911561fc3eef10ab2e54deb49461988e1d6c01c4a47f4217765d2ebac73a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U55POQWK%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T213224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDZQt3rkFhgnmXnw0gC1QPBRL6SfN7zIG%2F0uf9g0FSwugIhAMcg93qHKikQvTqvkRQuxkS4okxd1ALou2HxbkVH0rkXKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcU8UN2P0mRq8vYgq3AN8735sMVYiYQYeEwVwykNAwCXd1f50PheVwq4LXdCjZHU0GxQRksQhSnn5CeGtU29khgGqT%2F3%2BJONuEiODsHySazHPD9lOGFbd1rXvheFlx2WbrWUGtegGLCdMPBShO7BtqEVsMz49oneq6tg11gGPetcLmcIFJe8YyLqxWnBPIsV113PIIo7nqvjDzb3Qk3mwJMW4e1lgKf3SQRmrLXVjAskraKo89wYy8eO99kwmlW6EiV9f71PBFzyik1eoWO7%2Bi1YMZWEu7GOChcfDZ0iBn4aLKaOhqSaLaKDhJzsQgmIwpUSTv65wNIQpmRic3zlB%2FtX42lYE9MOrPpmbdJwZ0MP%2FOSMr3Pc%2FNGAX%2FZBLMpdMgRcpOO9DK%2FfL9nBCFfy5l69uT0nUtO%2F8HD4HtUucNN6YrEhlTDh4ESLuq%2BaUQXuz3%2B7JnYLqzQSR9d2qiwSyAvh1ezK516b%2BvHGlUx2iAN3KB0eZ79%2BJ3uH342W%2BK2JR187EWo4bPT4E0v0aBy9UpOUNirbjJ19mJPSz3pC86wvlNi26%2BNsmTD%2FLn6pDjiBkuIHcoPC5d4pFTDif%2Ffq%2BVL%2FjIKbJom%2F0moHUoeAI36zjEiBWfwuyx2CAMp5%2BWCeiIIGDYJCLm93k1jCT3%2BfQBjqkASxVPTSwa9QDMBotdX8x1EvnOwnjb5IGSgUycyfWYnzWMt6YQ4lZaRuGoo50p99QkQHwNZUo%2B18z0F5XsFn6CHuU6RI8R%2BAPQMRyTrcNFXVURbrd1R172v9dB12iNOWXadtnWMVT0lw9lhPOB8KtKuOQmwVsdxdDRF9YdjQg0WihPcpyV7uDIjI0dKu3estml837%2BSaPJX84Zsz%2Bb08sK6q8Xb%2FM&X-Amz-Signature=dccbdbf6f35e8bc4772aa3c7e2cecabac05f900effe76a9300f8827134a0305a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
