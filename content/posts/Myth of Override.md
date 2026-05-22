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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626YEZRXK%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T073621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDIPNOzPFpm3HXGsxfy4XxR%2FYW9e475PH4pq2bxEqVOBQIgOo6a%2BzFaBea7D0g78kgOr%2BhGZ6SakQCbXmHJehFakqYq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDCh%2BcxvK7%2Bdx3uCrwircA6dSqSEKX9T57LpCiaG08lcBMGOg%2BOI0rXB3qrbZLeLrfcRrQtOGq8fA55rMi0YTAPQZqWXn6vsnuOaDl3ulISY0JL4fSnBkgvvh1YaHSg9Wu7HtJt9aQZl5xbhgNvwdgL2mUqLGEv7Gj6%2B60vhYZi1pZxQuMJ7z%2BEzbdRcDcnJfRW3YeoNH33FxMSLmnDTHeOYIhSmxuqwkNt3gNiQ1Pmg1b2jkpzkUowNHdWTWsfIR6hOH41dS3pVJ5QSHEPj5dJusAh%2FbVYYZ%2FS3aKA7La5jauOXCaLxk%2F5%2FZ6PpHJfLLwOCWznK1x8kdbuzh%2BHFSR2CNWZ4uGmvaKpI3ZNvulZEslMCYvFNX9WtIAT3OyfGvvTVy8r0Vhf5iCx5H12XOPQ3grzNjsLFFG3EF8Vc3Fa%2By7rMn00ZZtDY9aGs7NC9Yn%2Fc7KlryvVB4BXohNrQbzaXpHwHDdt8E4rgRzv%2F6IiY3DmZPx9q6y85Aqyd1a%2Bn%2F7aj6qiTA3u33aOx3gffsBGM91%2F33VylIY3RI0kWZxxu%2B5vQW0tKCGNTYUmP66ZHoKLQ6YTdtAMtbnLtpZgs3jhyL9n%2FWHZRR8kZ6UGECQVys9jLWhHPrzJ1N4XaU2CkmRHu5awP3oPZaGrJpML%2F2v9AGOqUBSyo6eQjL7zRXz9%2FTk4k8%2FugdaQNb2q5OmMEBa2z%2BHlOrnPipReFh482pzK5FhgGVHipofnqxmHj2EfQU6UzC9KwBYtEtcXZ4D2QbNJ5QKZJ%2B6JvhOwT9zohSwF%2BIz2ym5xNJCzcaqaHibNvT2OjS%2FdUB%2FRYOdESBQFPRRfWX8LgxKKHvGv9QNsJ0JvMyqeYRrc2foREB383LAqV%2BfNmHjq1CDPol&X-Amz-Signature=fd581a99e1436ece33984feb4a631da7a8871f2408306a0c1744cd0e029a469a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626YEZRXK%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T073621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDIPNOzPFpm3HXGsxfy4XxR%2FYW9e475PH4pq2bxEqVOBQIgOo6a%2BzFaBea7D0g78kgOr%2BhGZ6SakQCbXmHJehFakqYq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDCh%2BcxvK7%2Bdx3uCrwircA6dSqSEKX9T57LpCiaG08lcBMGOg%2BOI0rXB3qrbZLeLrfcRrQtOGq8fA55rMi0YTAPQZqWXn6vsnuOaDl3ulISY0JL4fSnBkgvvh1YaHSg9Wu7HtJt9aQZl5xbhgNvwdgL2mUqLGEv7Gj6%2B60vhYZi1pZxQuMJ7z%2BEzbdRcDcnJfRW3YeoNH33FxMSLmnDTHeOYIhSmxuqwkNt3gNiQ1Pmg1b2jkpzkUowNHdWTWsfIR6hOH41dS3pVJ5QSHEPj5dJusAh%2FbVYYZ%2FS3aKA7La5jauOXCaLxk%2F5%2FZ6PpHJfLLwOCWznK1x8kdbuzh%2BHFSR2CNWZ4uGmvaKpI3ZNvulZEslMCYvFNX9WtIAT3OyfGvvTVy8r0Vhf5iCx5H12XOPQ3grzNjsLFFG3EF8Vc3Fa%2By7rMn00ZZtDY9aGs7NC9Yn%2Fc7KlryvVB4BXohNrQbzaXpHwHDdt8E4rgRzv%2F6IiY3DmZPx9q6y85Aqyd1a%2Bn%2F7aj6qiTA3u33aOx3gffsBGM91%2F33VylIY3RI0kWZxxu%2B5vQW0tKCGNTYUmP66ZHoKLQ6YTdtAMtbnLtpZgs3jhyL9n%2FWHZRR8kZ6UGECQVys9jLWhHPrzJ1N4XaU2CkmRHu5awP3oPZaGrJpML%2F2v9AGOqUBSyo6eQjL7zRXz9%2FTk4k8%2FugdaQNb2q5OmMEBa2z%2BHlOrnPipReFh482pzK5FhgGVHipofnqxmHj2EfQU6UzC9KwBYtEtcXZ4D2QbNJ5QKZJ%2B6JvhOwT9zohSwF%2BIz2ym5xNJCzcaqaHibNvT2OjS%2FdUB%2FRYOdESBQFPRRfWX8LgxKKHvGv9QNsJ0JvMyqeYRrc2foREB383LAqV%2BfNmHjq1CDPol&X-Amz-Signature=639ae3584e3476c58252acff8350c225bd6df19d7ad2f0643f4d882f0f91a46b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
