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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFU5IWBR%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T085448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAN2PuUsA2%2Bjrv1TFp8YyO4HNqlhfqBRZc49ftZ9%2BboQAiB10NZ8B7CTV1k2b835Yguvr8KLC0ssnQi13cFy8o8PUir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMG9qGuOEjr0fFzZafKtwDJvjEOnSi%2BW%2B51fdCkE8hH2a7cRkvW8Vb5a4IE1%2Bq%2F8JVYR%2BYg6gHAQNkRxKhXRbodUlactCMvkgYrcM53Dgb1iEWiBAZ7BFvjOlH3drjSiQWiVf6y%2FJNqULTwUulYnlgG2rq8rF78N0nfeuVXE%2F0%2B%2FQZotSFymqw7aqMIOvyAX186FbEmiN0L%2BrEQLGodx24dS0uLUhCV%2FFbXi0qiLNR6eCwvmLlDzaQzJzyOthysxDg4X6I6W4jgA%2FmEJ70QHYZ3r0fxhUb08bJd%2FbOfUOJsmGwOck9hJjNf2Wad5aBORGYD%2BOsHH48IzOe30eOJnS4wAh378GN2NeMDVefdZCPRVksnIbpS%2BstFGHf%2B06l%2FSzzG4uptbj7UxYeL6tExjMB8aC9vU%2Fe4z1uQO5w6XhYg%2F0qeC5LsZmN7Pf2fucPx2fWQfTA45l0CugOJ4Z%2BA%2FVNPPsrllnPeOyHycKoePVZqptU%2BH2wbIcbXD28AfuLBwEdjE1YWia1ci2W7quJqVQR92bFPjJF6tQNdRxcm%2FxeWx106p2gIu%2BQ4tX00ykt9HCutisTwpYXA%2BPal%2F1JbC4yw5YkBVAkxN1hqirvzvnSfDLtScb6RX6RGzcerjD4BVUSQt2e5qEngIgOg%2FEwvZWp1QY6pgHduVT3siSWUSIh5aF5nQEmqB3tL081A0cl34vZQeU0tzTvZPRLM%2FhnuDZGb9R%2Bt0qBqQas8JhBEcUwR4JGKIPkrM1DetjwZ22IowOfHc4Wtw8K4qQ7TokUA8ktytXiu%2FTECUmQZUynQHAjoik3uKhXsjdBGlx4qzrmalWPHTVjekVYFKPXx871TLEPw8WJkd7wYaGHgNhS%2FfUaRSqR38z9CRjwytE9&X-Amz-Signature=40054fd886d0b249d62c50d8581834f347ab16247075e2893662bc1deaa5c8cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFU5IWBR%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T085448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAN2PuUsA2%2Bjrv1TFp8YyO4HNqlhfqBRZc49ftZ9%2BboQAiB10NZ8B7CTV1k2b835Yguvr8KLC0ssnQi13cFy8o8PUir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMG9qGuOEjr0fFzZafKtwDJvjEOnSi%2BW%2B51fdCkE8hH2a7cRkvW8Vb5a4IE1%2Bq%2F8JVYR%2BYg6gHAQNkRxKhXRbodUlactCMvkgYrcM53Dgb1iEWiBAZ7BFvjOlH3drjSiQWiVf6y%2FJNqULTwUulYnlgG2rq8rF78N0nfeuVXE%2F0%2B%2FQZotSFymqw7aqMIOvyAX186FbEmiN0L%2BrEQLGodx24dS0uLUhCV%2FFbXi0qiLNR6eCwvmLlDzaQzJzyOthysxDg4X6I6W4jgA%2FmEJ70QHYZ3r0fxhUb08bJd%2FbOfUOJsmGwOck9hJjNf2Wad5aBORGYD%2BOsHH48IzOe30eOJnS4wAh378GN2NeMDVefdZCPRVksnIbpS%2BstFGHf%2B06l%2FSzzG4uptbj7UxYeL6tExjMB8aC9vU%2Fe4z1uQO5w6XhYg%2F0qeC5LsZmN7Pf2fucPx2fWQfTA45l0CugOJ4Z%2BA%2FVNPPsrllnPeOyHycKoePVZqptU%2BH2wbIcbXD28AfuLBwEdjE1YWia1ci2W7quJqVQR92bFPjJF6tQNdRxcm%2FxeWx106p2gIu%2BQ4tX00ykt9HCutisTwpYXA%2BPal%2F1JbC4yw5YkBVAkxN1hqirvzvnSfDLtScb6RX6RGzcerjD4BVUSQt2e5qEngIgOg%2FEwvZWp1QY6pgHduVT3siSWUSIh5aF5nQEmqB3tL081A0cl34vZQeU0tzTvZPRLM%2FhnuDZGb9R%2Bt0qBqQas8JhBEcUwR4JGKIPkrM1DetjwZ22IowOfHc4Wtw8K4qQ7TokUA8ktytXiu%2FTECUmQZUynQHAjoik3uKhXsjdBGlx4qzrmalWPHTVjekVYFKPXx871TLEPw8WJkd7wYaGHgNhS%2FfUaRSqR38z9CRjwytE9&X-Amz-Signature=02106db73e3dbad7b05826cd0cc3df970711f1b4351ad807df0a102804fc7673&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
