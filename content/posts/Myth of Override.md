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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SXOSOOZ%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T142109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIDkdzLhSs4kUB4ULLG0%2BdvX6%2B4gXyyeT9s38EZa0llZ8AiA16FtZhLAqUEyi35XuapqYDvhUjFOSsKiE7YPF9oI4XSr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMTYHvfGGs3QCxGGsbKtwDWy%2BG1TNXzGKBH48kb0rhefn74KBuiygYG7pl2RCbMArUBy5cy5NY%2FA%2FZLEIepoSIKKVE4mtIBHU9cgF4mNtotkTPi2cbbOYZItfrHf7Ec9IoWaXUX9HjrVly54dDLRi5L2mzxp8kgHluUYWDIK47lJ%2FiPnhcKKLfV%2BAEPnab81TIi6VXNy8LQXxDtoPEJHK2kFmfJa18ChGrTSb0CNUyNdp9mdNTxkjRaGZiOt2TZf%2FOnu0%2F3DJF4nX3wLR%2FC6BKQkvql0PxE9VAOxH%2BlrOPqWPwfztQxeNb6PZcvgm%2F5aPP%2Fvz1HF61UBo7JPvNtP0RM6ajEF1xRT6HF3l%2BYNF12FK3NUGdVkYHPvucsemVk3wWBPGBma4MD%2BDCPsLszcuDzquna6hVSjTGiMlE5bEOxPIUpwF2t5WcDtYdcz3OaVnBVoLwOzXQ0QrNV%2FqsbZ0yLQEX9ciizDSu4BLItSNNhYinEeHEiV4MPd3FSFkR01l%2BuBgy4un%2FiDSMJtqjdsqtZmRXMFP%2BbUhDIpU7rYrf5EQpdR0sndK%2Fhq8yevAnT4pJ%2B9szpBqWeIsPqOUNgcEuCH7X%2B%2BSgu2FJmVnWFlDady6SrH8qQWYLRPoDvxo1gS%2FLMdHJ6qHMY8L0GcMwpej%2F0AY6pgF5UvcgOPWk5focuZGRQ9KZkNB8r7yJwkHKjw%2B4FODdEFP4C%2FSzk0oVYkntlmjDnUBcSCmVlNTCJf4%2Fr3iZ88hFw%2F%2FUgGljmtg1c9XCa6he88kFoi6qvpXrm%2FdwjvejifvWTN4vLGI54z0a%2B8suzVoBjGE85dlGM%2FCTGhsgUNDAwOUsH%2FXElG5t4y%2BoXCCFwrNCbc%2FXFVjOLg6WMag%2Bl3Tocua2E8Ti&X-Amz-Signature=210fe7e88c72c783320db26587112b46e7f160b0677ca7276d801f725db023dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SXOSOOZ%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T142109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIDkdzLhSs4kUB4ULLG0%2BdvX6%2B4gXyyeT9s38EZa0llZ8AiA16FtZhLAqUEyi35XuapqYDvhUjFOSsKiE7YPF9oI4XSr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMTYHvfGGs3QCxGGsbKtwDWy%2BG1TNXzGKBH48kb0rhefn74KBuiygYG7pl2RCbMArUBy5cy5NY%2FA%2FZLEIepoSIKKVE4mtIBHU9cgF4mNtotkTPi2cbbOYZItfrHf7Ec9IoWaXUX9HjrVly54dDLRi5L2mzxp8kgHluUYWDIK47lJ%2FiPnhcKKLfV%2BAEPnab81TIi6VXNy8LQXxDtoPEJHK2kFmfJa18ChGrTSb0CNUyNdp9mdNTxkjRaGZiOt2TZf%2FOnu0%2F3DJF4nX3wLR%2FC6BKQkvql0PxE9VAOxH%2BlrOPqWPwfztQxeNb6PZcvgm%2F5aPP%2Fvz1HF61UBo7JPvNtP0RM6ajEF1xRT6HF3l%2BYNF12FK3NUGdVkYHPvucsemVk3wWBPGBma4MD%2BDCPsLszcuDzquna6hVSjTGiMlE5bEOxPIUpwF2t5WcDtYdcz3OaVnBVoLwOzXQ0QrNV%2FqsbZ0yLQEX9ciizDSu4BLItSNNhYinEeHEiV4MPd3FSFkR01l%2BuBgy4un%2FiDSMJtqjdsqtZmRXMFP%2BbUhDIpU7rYrf5EQpdR0sndK%2Fhq8yevAnT4pJ%2B9szpBqWeIsPqOUNgcEuCH7X%2B%2BSgu2FJmVnWFlDady6SrH8qQWYLRPoDvxo1gS%2FLMdHJ6qHMY8L0GcMwpej%2F0AY6pgF5UvcgOPWk5focuZGRQ9KZkNB8r7yJwkHKjw%2B4FODdEFP4C%2FSzk0oVYkntlmjDnUBcSCmVlNTCJf4%2Fr3iZ88hFw%2F%2FUgGljmtg1c9XCa6he88kFoi6qvpXrm%2FdwjvejifvWTN4vLGI54z0a%2B8suzVoBjGE85dlGM%2FCTGhsgUNDAwOUsH%2FXElG5t4y%2BoXCCFwrNCbc%2FXFVjOLg6WMag%2Bl3Tocua2E8Ti&X-Amz-Signature=9c9e445ba36d295f53d134d5559c4016c9918fde61a09318abbf31ad6aebabbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
