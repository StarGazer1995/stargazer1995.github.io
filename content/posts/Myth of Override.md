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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ4NSEKI%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T085940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCyiUGD6dGeSyDsqdnmGB3JEGr9qNy26Zk7CSh%2FLJAAxwIhAOO2cSBkLZatWHbyq3tI4%2B2gAgnq5hvCPPXBDTBUpsbFKv8DCCoQABoMNjM3NDIzMTgzODA1IgxbSkXIL6WSnCfb85sq3AN5m%2Foq%2Bf12HtWP9ltVwFQziZ%2BHWhJQxYPFpd3ZLFFsIGrcLZA8%2FHeQQh4khVtf0umB0UT%2BUFLSFwX021jAegLpOUz5MRbRjgY2qtE4iVqe1%2B7v7ASqTCFH%2BAOyBjpmfALNELD9HPx6yINMSUwTDzdt7%2F9hGS7bxs6VA5FHH9aZZ%2BBvsdhKdWOqtnrnhm4eaRJtJe4ZZCLxYpSAgPnP4T%2BYPTdc4lZ0ffeKdhjC6ounWS2r1H0QiGXGteS752zYGs2ESt6HvVhppKbmVgqsbNaPnPvZYrY0%2Fx68q1kwDGnRVw%2FINee%2Fm7EImzUFbE9jBIMMjpPo8prP2xYh23ahcghSq%2Bb4Scv9ippkZmfcuxOqxUvWl2kmTnl9A0JHNNagSzMzSD9HLydj4Fur3F5Z7QM8%2FZ4Nc4%2FU%2BYuLaxvJOswptTYvSFbJqiMo%2FgAPRwoK8Tz%2BP%2F28rH4hM1eRtuo4dpMLr6TIlxy2bt6PHh7DbHdjSeRxkHe28VtH0%2FaGSTOs0cBJhi5Ktgh29qvUqAeGfCvhHwgsSX7hsJ2PUGQIGW3jZpohNfrroRq3Jjg3o8J1cinpusVdMdVSBHsXw6PEDHk0IPDsUd9q865DhPJI9u4xeSrFA8cWxjdjShz%2BHzCsza7VBjqkAVbfqQIh0K6pxaJLccXaKktAnmuV97InuaxaUr%2BlBYyiH5qzzi87HPOer1q0a57iA2bJnViB2qY2BAwrIE3nRL1FYe1xHJjyRO%2FdgYdqQWB2%2Bea4YB6hmVywj7AUuDU28ZVA7YRYJ0pVHWLZKYfzWHBRgMvR107auafrEalrLZEeW1ads4CfTiJ6GizuBV0x2xV5Hhq89bZjS%2B8RgHYixLLQhZCc&X-Amz-Signature=d4052d7c025f4e4caa82df119f1818c757ceaf71b9a9839ed1e2906754092aa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ4NSEKI%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T085940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCyiUGD6dGeSyDsqdnmGB3JEGr9qNy26Zk7CSh%2FLJAAxwIhAOO2cSBkLZatWHbyq3tI4%2B2gAgnq5hvCPPXBDTBUpsbFKv8DCCoQABoMNjM3NDIzMTgzODA1IgxbSkXIL6WSnCfb85sq3AN5m%2Foq%2Bf12HtWP9ltVwFQziZ%2BHWhJQxYPFpd3ZLFFsIGrcLZA8%2FHeQQh4khVtf0umB0UT%2BUFLSFwX021jAegLpOUz5MRbRjgY2qtE4iVqe1%2B7v7ASqTCFH%2BAOyBjpmfALNELD9HPx6yINMSUwTDzdt7%2F9hGS7bxs6VA5FHH9aZZ%2BBvsdhKdWOqtnrnhm4eaRJtJe4ZZCLxYpSAgPnP4T%2BYPTdc4lZ0ffeKdhjC6ounWS2r1H0QiGXGteS752zYGs2ESt6HvVhppKbmVgqsbNaPnPvZYrY0%2Fx68q1kwDGnRVw%2FINee%2Fm7EImzUFbE9jBIMMjpPo8prP2xYh23ahcghSq%2Bb4Scv9ippkZmfcuxOqxUvWl2kmTnl9A0JHNNagSzMzSD9HLydj4Fur3F5Z7QM8%2FZ4Nc4%2FU%2BYuLaxvJOswptTYvSFbJqiMo%2FgAPRwoK8Tz%2BP%2F28rH4hM1eRtuo4dpMLr6TIlxy2bt6PHh7DbHdjSeRxkHe28VtH0%2FaGSTOs0cBJhi5Ktgh29qvUqAeGfCvhHwgsSX7hsJ2PUGQIGW3jZpohNfrroRq3Jjg3o8J1cinpusVdMdVSBHsXw6PEDHk0IPDsUd9q865DhPJI9u4xeSrFA8cWxjdjShz%2BHzCsza7VBjqkAVbfqQIh0K6pxaJLccXaKktAnmuV97InuaxaUr%2BlBYyiH5qzzi87HPOer1q0a57iA2bJnViB2qY2BAwrIE3nRL1FYe1xHJjyRO%2FdgYdqQWB2%2Bea4YB6hmVywj7AUuDU28ZVA7YRYJ0pVHWLZKYfzWHBRgMvR107auafrEalrLZEeW1ads4CfTiJ6GizuBV0x2xV5Hhq89bZjS%2B8RgHYixLLQhZCc&X-Amz-Signature=8a366354f9a54be6a37d7e0126945c2f99776406eb1324ae08ba3eb6a228a89b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
