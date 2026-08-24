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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHZLUGRX%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T223523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIDYnzhGAQpJ0XjoZubNA1iQQxeyh7aIaJfpbnfWyQ%2Fd5AiAxP%2BMENcyjm0CAOdW%2BVDW92Z9tEYKjRmgVURWKmr8PIiqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYeQ6vnhYW23XyL3QKtwDpbNmTvtvY3oBAGfYOM6eIcv%2BowcMwbpuRkp1f3%2BN4OBYHwLt9vpdUxu9nfnUHq6w9IKMVyW3QBYm4qDmoRRGw1HFu5%2B3y4izTbT41SCYuCyv2iszvESqyGCfF6dQ5yP7bIOCnWPRsDxKBAn%2BM%2Fdn%2Fq2tmOku3HukYTfivP7RpfqqouTj1Wz01TTQ9C0sLHx%2BxVf8lttRuaiybGXnYBWG1NvjgAz7HscqAd3a4mJgUGZmSvs5aPHPflPjCD7WkFf8ASGmhe33hfasztB6r9A6uROkS%2B1%2BpTYjzxJVsRZIJg1qAZpy6g1AIF7vTvdirza1Xt%2FUS4Qpr7hjjCzpKUTS70f09QsWc0JMGVokC%2BmoOCmez47rfCEnCidloUvO9rUFhL5%2BruJa48KFZt5J9NIdAgACVW18NoqCOjXjQislvkMc3irl5mortLKXltxnKGTkqH1Qq4uhaWw5z8boUdA0FA3c%2Bk0TySn5ulq6x2RcORLGhH9s2yAuRQ73W7KviHR4G%2B9iYhOhrPOnSrdVGqrh%2Fc2ATwQfagBO%2F6HpvSG1KKoYTPzRdIuKjkPK%2Bn2zf%2Ft%2BUhytBfjmOE8opTby1nlqbfx2fD2vAZdndv5U4yt4S9fTtHYdbB3XA1gPy%2BUwqsey1AY6pgGEmGEnV6NRTP5Pj2bn0qINehrVt5OQBoOuzu5BG09RKx1vNTAb5S6XcmYclUT%2FZ0Rgu4CsjMdqsgsSgzcyehu9QGw6jjbrJvp2pBTXTAqowRFT%2FVYEKzs4yp90ZYccCMaW0DASsMCQ4s1nTTEcrr6RgrgbUNVl0yTEjhkT7WMqpPh8bBHUCRVY7SxnPrAVHA%2FI9r%2BKaC7Hpig7ARsk%2BSrZPG8s%2B7QT&X-Amz-Signature=3c6b62a4523373ad8fcf1fdbe2a9817033420873dc247f9932d701a9862c7a75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHZLUGRX%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T223523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIDYnzhGAQpJ0XjoZubNA1iQQxeyh7aIaJfpbnfWyQ%2Fd5AiAxP%2BMENcyjm0CAOdW%2BVDW92Z9tEYKjRmgVURWKmr8PIiqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYeQ6vnhYW23XyL3QKtwDpbNmTvtvY3oBAGfYOM6eIcv%2BowcMwbpuRkp1f3%2BN4OBYHwLt9vpdUxu9nfnUHq6w9IKMVyW3QBYm4qDmoRRGw1HFu5%2B3y4izTbT41SCYuCyv2iszvESqyGCfF6dQ5yP7bIOCnWPRsDxKBAn%2BM%2Fdn%2Fq2tmOku3HukYTfivP7RpfqqouTj1Wz01TTQ9C0sLHx%2BxVf8lttRuaiybGXnYBWG1NvjgAz7HscqAd3a4mJgUGZmSvs5aPHPflPjCD7WkFf8ASGmhe33hfasztB6r9A6uROkS%2B1%2BpTYjzxJVsRZIJg1qAZpy6g1AIF7vTvdirza1Xt%2FUS4Qpr7hjjCzpKUTS70f09QsWc0JMGVokC%2BmoOCmez47rfCEnCidloUvO9rUFhL5%2BruJa48KFZt5J9NIdAgACVW18NoqCOjXjQislvkMc3irl5mortLKXltxnKGTkqH1Qq4uhaWw5z8boUdA0FA3c%2Bk0TySn5ulq6x2RcORLGhH9s2yAuRQ73W7KviHR4G%2B9iYhOhrPOnSrdVGqrh%2Fc2ATwQfagBO%2F6HpvSG1KKoYTPzRdIuKjkPK%2Bn2zf%2Ft%2BUhytBfjmOE8opTby1nlqbfx2fD2vAZdndv5U4yt4S9fTtHYdbB3XA1gPy%2BUwqsey1AY6pgGEmGEnV6NRTP5Pj2bn0qINehrVt5OQBoOuzu5BG09RKx1vNTAb5S6XcmYclUT%2FZ0Rgu4CsjMdqsgsSgzcyehu9QGw6jjbrJvp2pBTXTAqowRFT%2FVYEKzs4yp90ZYccCMaW0DASsMCQ4s1nTTEcrr6RgrgbUNVl0yTEjhkT7WMqpPh8bBHUCRVY7SxnPrAVHA%2FI9r%2BKaC7Hpig7ARsk%2BSrZPG8s%2B7QT&X-Amz-Signature=b1ceee061bb390bc8dd8dba5ceb3f3a0afd380dd4946832ef5e0cdf13f3c46a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
