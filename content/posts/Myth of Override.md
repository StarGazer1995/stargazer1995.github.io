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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CBD6IJO%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T191406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArcApdHLdpm8xuSnEJXdIP4jHrJqD5l4gEj58%2FU2Gs2AiAssTgeE%2FosNkuZ5Zrv24HuWQILIS4bmB7lInZ%2BnCNocyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLsTohTsEAoa80qRKKtwDuvL5HZ0yPhRevmIci9Dmbt%2BUYorYqNnbf6A%2Bf0GHWefTEsQMukGIFHpGcIt0OIBOhXbAQHpUg2XS4xsqErKA6c7RjMo8oa75t31ZM%2FFaI6hplv8Ju%2F7PQ6Nzzszt0gfPcAzuuRPICCTI1tq%2FpFEg7ws36z%2F6itvez1miYEXXpMbzJLrmza685%2FL0s4bGdMVci2AuCDMiduKb185X8kIsYVGSgPXt2SJRnj6KgzDy4Q%2FDZ3hvvHb4MspaBst0TwPi1VC2RcawhGLwX41PwkLenxqU%2BbFQaoyjY5Mw0K8kkT%2BTGF0wakm66QEAU07O%2FbV%2F2Pq1kNOA%2BC0ygV6u3KfIne8YMVZLfTlg2bVlasgZlI4DGbwpA9dQehPMY1HajYsggZKSpHhMjXIOG7buaCtBGryTmOj3Ognjg5LdKTVKEl139886si8JR1rkv66BkOuUjmwZVrhQB%2FPcMZ4vHnBvSk8PeDD3kcwXDk7zdQKFDu1DXgq%2BGCChDUbCCRwukc2tdS9whImPmTNc7509i%2Bkjlagq4QpXZHFFnh9dfTDsI4MES3lDbLJaebTMwjDyL6xYCXuLnn%2BMSzcdNZZXQjneXBNQjHYqUJfvuGqNcLk0%2B3d5S1Ey3XyRkkBa%2B9ww6O%2FE0gY6pgHzb0NsD%2BefafC%2BLwGJk8gsJ451DeByt%2Btn%2B8V07r9TEB58bt3gZ2Eui9ZfwkeexrE%2BRjwzkfvx%2F5UKl6KTeOr06O%2BbZXrIe4cIbLms6I0haQJXHAelL%2FT2QTQf%2Bnfc%2BGcOWFmmRq1TvBZJo3j%2B2dOadezTCfcD75nuRANaTPZUIKcx398V9yEPMU83T%2BPrU8HGuwFujyzWow4fRA2qL1%2BNi6LrZrPH&X-Amz-Signature=792017a4fce3f56f5019f29cf8ea9e12f541f7db5b409d6f21c706bf7d2ed263&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CBD6IJO%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T191406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArcApdHLdpm8xuSnEJXdIP4jHrJqD5l4gEj58%2FU2Gs2AiAssTgeE%2FosNkuZ5Zrv24HuWQILIS4bmB7lInZ%2BnCNocyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLsTohTsEAoa80qRKKtwDuvL5HZ0yPhRevmIci9Dmbt%2BUYorYqNnbf6A%2Bf0GHWefTEsQMukGIFHpGcIt0OIBOhXbAQHpUg2XS4xsqErKA6c7RjMo8oa75t31ZM%2FFaI6hplv8Ju%2F7PQ6Nzzszt0gfPcAzuuRPICCTI1tq%2FpFEg7ws36z%2F6itvez1miYEXXpMbzJLrmza685%2FL0s4bGdMVci2AuCDMiduKb185X8kIsYVGSgPXt2SJRnj6KgzDy4Q%2FDZ3hvvHb4MspaBst0TwPi1VC2RcawhGLwX41PwkLenxqU%2BbFQaoyjY5Mw0K8kkT%2BTGF0wakm66QEAU07O%2FbV%2F2Pq1kNOA%2BC0ygV6u3KfIne8YMVZLfTlg2bVlasgZlI4DGbwpA9dQehPMY1HajYsggZKSpHhMjXIOG7buaCtBGryTmOj3Ognjg5LdKTVKEl139886si8JR1rkv66BkOuUjmwZVrhQB%2FPcMZ4vHnBvSk8PeDD3kcwXDk7zdQKFDu1DXgq%2BGCChDUbCCRwukc2tdS9whImPmTNc7509i%2Bkjlagq4QpXZHFFnh9dfTDsI4MES3lDbLJaebTMwjDyL6xYCXuLnn%2BMSzcdNZZXQjneXBNQjHYqUJfvuGqNcLk0%2B3d5S1Ey3XyRkkBa%2B9ww6O%2FE0gY6pgHzb0NsD%2BefafC%2BLwGJk8gsJ451DeByt%2Btn%2B8V07r9TEB58bt3gZ2Eui9ZfwkeexrE%2BRjwzkfvx%2F5UKl6KTeOr06O%2BbZXrIe4cIbLms6I0haQJXHAelL%2FT2QTQf%2Bnfc%2BGcOWFmmRq1TvBZJo3j%2B2dOadezTCfcD75nuRANaTPZUIKcx398V9yEPMU83T%2BPrU8HGuwFujyzWow4fRA2qL1%2BNi6LrZrPH&X-Amz-Signature=398e41418c1dbb12cbf36c9e6760631eaafb0bddd3ca7ea9a1b321959a49b1ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
