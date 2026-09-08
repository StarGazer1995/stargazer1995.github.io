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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3JR4AIX%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T202520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTGG%2FgmkCUEidDKS06alhFZGJLwfV%2FbTf%2FHqM4QDjZUAIgM1HyL%2BRPgu6freJ8E5qMeENVIRmpJ9DLBUnlEE3PmqEq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDKUX2YSpXlSYVgIs%2BircA6W%2BZDDxCbcGDYuATsgRfiGbwY%2BogcPTf2AR5h%2FM2nrTT4NkuEbNM7CwH5bjsIe13N1Z13dfV6MJEEau8Q%2BVYPmnpV41hGh1%2F5ISuHvEWrM2BZ6hlR2bGDgkrB4hqxcs%2FkvKq0jbSYq5IONTzJX%2FA2l%2BU2nkKSNFYJ7VBWeIGGW9yo4fD%2FYfsG%2FbpsTVO%2Fya4MQopFbLPDaUpYkKsq6eLC7u%2Bp%2B%2FmS9DMKydwjaikIP%2F5QRXYgzv6DSUbHS0EQRTD1HvRqGPhmobn7R1p2BsqGAofbx35l5em6M1%2FKC8KH%2F0EQszs9wWObXwW1wXZsVvY7icXDNVkAl5Z4%2FmwzWsbUlLZm0W1qVdufplocaVqz9ZIET6TbihxP6IX30hwZ6AiiYggwIPYnC%2BxAG%2BwkI2%2FfIzRn%2BEp7%2F6TDifxUMxGz3bN1junu6l4tRO0z36Vdskses6RKfcpGPG1VTyVwz57R2cHxqaDkwkWBMyqVA9tiHhTUC0fqPb%2FAYLmczH3BEqmV4ZTI7zVn1BcyU6WazjZPSz0a3Q1TXFxeuFoyduqHcKi%2BHnbOxGBS84n9wGT%2Fi%2BYpClxTSwBhLpc9JN40%2FkDNB5t9%2Feg%2B22JSONhNwWAY53HSGT77FxKjH9AeA8MPf%2FgNUGOqUBl94hZKJJuVrhjnIlQ2DNGe6uOG%2FzU%2B2Yld23M9Rdqlzk%2BrJL3R2a7oHPlg%2BFzFX4Aa9WYaDPrZhKSU6RJT%2BKjXve4703zAgmQpR4ZX8YEIIZq%2B%2B%2FDcjorNrn8UGivX3jy%2B4CMzQFn8ZZgYHHfppMugc9xBcC0N3M1R8BC4C2L6M9F8ht2CZsOqBqnMVAX83OUlhomdGROqWFmX49MXtYay7tokS9&X-Amz-Signature=4921cdcf8df8f5d71df6984bc5459e99488b437b2630c6e91d4d083d066a3e54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3JR4AIX%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T202520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTGG%2FgmkCUEidDKS06alhFZGJLwfV%2FbTf%2FHqM4QDjZUAIgM1HyL%2BRPgu6freJ8E5qMeENVIRmpJ9DLBUnlEE3PmqEq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDKUX2YSpXlSYVgIs%2BircA6W%2BZDDxCbcGDYuATsgRfiGbwY%2BogcPTf2AR5h%2FM2nrTT4NkuEbNM7CwH5bjsIe13N1Z13dfV6MJEEau8Q%2BVYPmnpV41hGh1%2F5ISuHvEWrM2BZ6hlR2bGDgkrB4hqxcs%2FkvKq0jbSYq5IONTzJX%2FA2l%2BU2nkKSNFYJ7VBWeIGGW9yo4fD%2FYfsG%2FbpsTVO%2Fya4MQopFbLPDaUpYkKsq6eLC7u%2Bp%2B%2FmS9DMKydwjaikIP%2F5QRXYgzv6DSUbHS0EQRTD1HvRqGPhmobn7R1p2BsqGAofbx35l5em6M1%2FKC8KH%2F0EQszs9wWObXwW1wXZsVvY7icXDNVkAl5Z4%2FmwzWsbUlLZm0W1qVdufplocaVqz9ZIET6TbihxP6IX30hwZ6AiiYggwIPYnC%2BxAG%2BwkI2%2FfIzRn%2BEp7%2F6TDifxUMxGz3bN1junu6l4tRO0z36Vdskses6RKfcpGPG1VTyVwz57R2cHxqaDkwkWBMyqVA9tiHhTUC0fqPb%2FAYLmczH3BEqmV4ZTI7zVn1BcyU6WazjZPSz0a3Q1TXFxeuFoyduqHcKi%2BHnbOxGBS84n9wGT%2Fi%2BYpClxTSwBhLpc9JN40%2FkDNB5t9%2Feg%2B22JSONhNwWAY53HSGT77FxKjH9AeA8MPf%2FgNUGOqUBl94hZKJJuVrhjnIlQ2DNGe6uOG%2FzU%2B2Yld23M9Rdqlzk%2BrJL3R2a7oHPlg%2BFzFX4Aa9WYaDPrZhKSU6RJT%2BKjXve4703zAgmQpR4ZX8YEIIZq%2B%2B%2FDcjorNrn8UGivX3jy%2B4CMzQFn8ZZgYHHfppMugc9xBcC0N3M1R8BC4C2L6M9F8ht2CZsOqBqnMVAX83OUlhomdGROqWFmX49MXtYay7tokS9&X-Amz-Signature=956587cfb55241b3fa79e9d08f19afb99d22341d06aa0b252769b310e7557e7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
