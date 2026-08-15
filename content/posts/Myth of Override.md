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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4AATBE3%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T024736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQDt3ggSt3F07yt%2BqjAy3JhXUv7KznzP9IEgmeCPb5mMyAIhAOHvpWk%2F5U1AAUzvTdAcBfJt5TmB7Qcx6EbLmIGzqflgKv8DCAoQABoMNjM3NDIzMTgzODA1IgxURGKvO%2FsfPQptic4q3AO1J%2FzNqsyKbNFJ4zL1Yjsl1aNvwxZeZBIWHSU80uVWA7GB0Q7MsjvW8hdEDr1rqqF47sis4rdVLR5qVhj%2FL1pYrxqDrQY8i99DdLjLM5FIIdTDOtNmgkOkVY8Cb4%2BFB7Y%2B%2BxFEwv2wKTThC%2Bnodq7qvnuM46J1OgBR6Bh6d%2BXfjBbvs511U0WA79jyRKbgdiAKWIw%2BiQjukPED64H22DFL5aglZbJgnHqTMfo8374AmtWcFlV%2FL0k%2B2e%2Bb95cwvrZeg9mTZYadKUDf42vPyyXgg5OaRjdMs08HfglS5U9%2B3umkKGBwe0WBQmWbpGrBJ15dCawq9Ktc3YxV6WyelpbHo%2F%2BRxUKuasSf0AbdGSNYwoHXZ%2FTQ%2Fm4VONHn6awXgxm%2FZM9OBnkP60dkXFsz6KtIAonLKwfIW9W5HG%2B8LCGFmwll3NMX9PXFj6nhuUc0d9OVEz%2BGteu5B3oUnTdj%2FWVcj9w2Fvm5hOerPA51V1SC3fBrNfGQfe%2FNCoyHhhGGJjupgqKV7oHDsi0yd6Cq85WqtDy3E8ypwm44WdoOmUUYy5vH6Q2k9uwk%2BgrkdVy2c76sJasgAqSQT03uYwLv8bciru288oMRge9fWKoyKJWbkJa3exNMLLWvGN4ldzDV%2Ff7TBjqkAZyUqW99mGskrvJCDkMvGZEHfyOx7LB9BwH652YyHrYRnYgTwfKnF5xeQeGEoVFclJZJ7Y9bvBV1oR4pN53NlTbWKOS%2B%2F61413oFSVEbNp4aDdOOWAryBGYjwpnAeY3P7YX4gufVha51psApn2%2FxYPV9OmVfUYG3puN6fXl5atg0RBW2HJ1WAN6fxc%2B2beB1vgJJ%2Bv37co7Q13JkpWo60v09IOBO&X-Amz-Signature=13ce3a263a49c5911e5695ab289465b55b2399e0fea5663cec170c3eb6451f1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4AATBE3%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T024736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQDt3ggSt3F07yt%2BqjAy3JhXUv7KznzP9IEgmeCPb5mMyAIhAOHvpWk%2F5U1AAUzvTdAcBfJt5TmB7Qcx6EbLmIGzqflgKv8DCAoQABoMNjM3NDIzMTgzODA1IgxURGKvO%2FsfPQptic4q3AO1J%2FzNqsyKbNFJ4zL1Yjsl1aNvwxZeZBIWHSU80uVWA7GB0Q7MsjvW8hdEDr1rqqF47sis4rdVLR5qVhj%2FL1pYrxqDrQY8i99DdLjLM5FIIdTDOtNmgkOkVY8Cb4%2BFB7Y%2B%2BxFEwv2wKTThC%2Bnodq7qvnuM46J1OgBR6Bh6d%2BXfjBbvs511U0WA79jyRKbgdiAKWIw%2BiQjukPED64H22DFL5aglZbJgnHqTMfo8374AmtWcFlV%2FL0k%2B2e%2Bb95cwvrZeg9mTZYadKUDf42vPyyXgg5OaRjdMs08HfglS5U9%2B3umkKGBwe0WBQmWbpGrBJ15dCawq9Ktc3YxV6WyelpbHo%2F%2BRxUKuasSf0AbdGSNYwoHXZ%2FTQ%2Fm4VONHn6awXgxm%2FZM9OBnkP60dkXFsz6KtIAonLKwfIW9W5HG%2B8LCGFmwll3NMX9PXFj6nhuUc0d9OVEz%2BGteu5B3oUnTdj%2FWVcj9w2Fvm5hOerPA51V1SC3fBrNfGQfe%2FNCoyHhhGGJjupgqKV7oHDsi0yd6Cq85WqtDy3E8ypwm44WdoOmUUYy5vH6Q2k9uwk%2BgrkdVy2c76sJasgAqSQT03uYwLv8bciru288oMRge9fWKoyKJWbkJa3exNMLLWvGN4ldzDV%2Ff7TBjqkAZyUqW99mGskrvJCDkMvGZEHfyOx7LB9BwH652YyHrYRnYgTwfKnF5xeQeGEoVFclJZJ7Y9bvBV1oR4pN53NlTbWKOS%2B%2F61413oFSVEbNp4aDdOOWAryBGYjwpnAeY3P7YX4gufVha51psApn2%2FxYPV9OmVfUYG3puN6fXl5atg0RBW2HJ1WAN6fxc%2B2beB1vgJJ%2Bv37co7Q13JkpWo60v09IOBO&X-Amz-Signature=9ee8527f8d92307d05f390a8a4f784c25c50fa7d13f6d588574bf947f47a4e0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
