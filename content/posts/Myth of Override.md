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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY55A6%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T074956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJGMEQCIHE8s96kpDQ1dp1%2B38krOtAGiF2xX8ZuXVzp2ARUotZHAiA4ePplE%2FijZlaI4DlQDERMrAmpGN%2F2HSSwGkI3ADySHyqIBAjY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMolSBPYqHNlU0Dv5tKtwDPELhQQUIZYuFl7ky6hA2cxrvcTGZmy6MmAlc4WRurKswpf%2BusD3rkVtvpEWB%2Fcasj4FSt0fFyaula66V4ulC7T%2FdTieNwpzl09Usps%2BPCkringYvOeKawhF8UHIJZ1924YlmoqZyR%2B%2F6mgzeW4yK89JcZ19Cn6%2BeGrcbIWS9SSRGPY2W89G3UBsrXtQpHk64Tk4R8M9k15E%2B8J%2BsA6HlUTGFmOSDy9%2BC0tMKGQZLZ9NxdTJPS%2BPxrFllMOgoS7Zn6xhN3LfzOrnZrM2Tz3dnbwA%2BC5gtZQ%2Fg0Q9Sa3x0yg6PlZaMdqm4Uou68ILB1XsEsoT%2B%2F2oIZoxuAcqwjN%2FY4aQVEhjKre6KweQKakN4nJTMCNa56zQ7gOac9QzOtimiCIlZIEll%2F1tWqvLfBDmNGwdcthd8lRL9MGdOM47U0mOpOuLyjKu%2BEUcbNjGZnjXlsIc2VQI1B91rjiWwkfubIjPuq3DN556UP1hU1DqYivuRCwn4ckvOtut8IXrFXq1EG6hoFVD4eDNVcA%2FJJITqxfwDMCrUhNvsa%2BD%2BnffvryKg%2FFFBIMGdgOYBx2U%2BKQJMbQE%2BehewPKLtk3lAC3VOXIu3K%2BZnStUKu9KJyD26r%2Bmz%2F7kkwJcu6EaazIswx5qN1gY6pgGFjjRwOq35e1AG%2FJqggSpdDgAFuRueSBs%2Bya%2Fp2GOZX2uvzvu3cFt4hnH0UNcE6SEatx5Z%2FGNl69OP61tEOChKSbc2QbB2WhxS7lweUcZ4kekff5Y5LVZd0A1v0TTuKYA1Tn2LB%2BjdyAhT6MwSFsz5pn06qej%2B6tPD2%2B8tK16a%2FoGJSoT0VhMNaTPatOz0fmqrzwuFafeVBz0SwxnACKnYvI%2B%2Bsm3P&X-Amz-Signature=57f991524e9dccb24959f43c35eaf8569760c363e5dd85dc871fc80614ceec6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBZY55A6%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T074956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJGMEQCIHE8s96kpDQ1dp1%2B38krOtAGiF2xX8ZuXVzp2ARUotZHAiA4ePplE%2FijZlaI4DlQDERMrAmpGN%2F2HSSwGkI3ADySHyqIBAjY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMolSBPYqHNlU0Dv5tKtwDPELhQQUIZYuFl7ky6hA2cxrvcTGZmy6MmAlc4WRurKswpf%2BusD3rkVtvpEWB%2Fcasj4FSt0fFyaula66V4ulC7T%2FdTieNwpzl09Usps%2BPCkringYvOeKawhF8UHIJZ1924YlmoqZyR%2B%2F6mgzeW4yK89JcZ19Cn6%2BeGrcbIWS9SSRGPY2W89G3UBsrXtQpHk64Tk4R8M9k15E%2B8J%2BsA6HlUTGFmOSDy9%2BC0tMKGQZLZ9NxdTJPS%2BPxrFllMOgoS7Zn6xhN3LfzOrnZrM2Tz3dnbwA%2BC5gtZQ%2Fg0Q9Sa3x0yg6PlZaMdqm4Uou68ILB1XsEsoT%2B%2F2oIZoxuAcqwjN%2FY4aQVEhjKre6KweQKakN4nJTMCNa56zQ7gOac9QzOtimiCIlZIEll%2F1tWqvLfBDmNGwdcthd8lRL9MGdOM47U0mOpOuLyjKu%2BEUcbNjGZnjXlsIc2VQI1B91rjiWwkfubIjPuq3DN556UP1hU1DqYivuRCwn4ckvOtut8IXrFXq1EG6hoFVD4eDNVcA%2FJJITqxfwDMCrUhNvsa%2BD%2BnffvryKg%2FFFBIMGdgOYBx2U%2BKQJMbQE%2BehewPKLtk3lAC3VOXIu3K%2BZnStUKu9KJyD26r%2Bmz%2F7kkwJcu6EaazIswx5qN1gY6pgGFjjRwOq35e1AG%2FJqggSpdDgAFuRueSBs%2Bya%2Fp2GOZX2uvzvu3cFt4hnH0UNcE6SEatx5Z%2FGNl69OP61tEOChKSbc2QbB2WhxS7lweUcZ4kekff5Y5LVZd0A1v0TTuKYA1Tn2LB%2BjdyAhT6MwSFsz5pn06qej%2B6tPD2%2B8tK16a%2FoGJSoT0VhMNaTPatOz0fmqrzwuFafeVBz0SwxnACKnYvI%2B%2Bsm3P&X-Amz-Signature=0d15cf0680b382ac8a0dd0229a49ab55bcb4333a78aa9ecf36e6a64e7a4478b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
