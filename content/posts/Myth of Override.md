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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3XBMPEL%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T023558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQDyQALxiq1E%2BvBH%2FICuRsERspV1cZ2YyBe313HFgcGEnwIgaKjmfMWhmYgzphvmEO2hQ1KF%2BevewhYfTosgJ8spZ%2FMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDJyhdnZpPGLrYDEJ5yrcA3nqGJ8CLQN3KbkQstDWZjhQDudCGSVYsSdnHoZ39fINQncxA9lKtrU9vTaME2wLZzCnhPJO2ziTdBk0zCLfTSovQSaBgRTms8D1KAKfDg66Y5T8V9G5BYi%2BY7%2B5eALaFKbZZvGa2utPy3ZbClzdSJvjGGXysWUyQ5jCsby5pWbxt80iTvWg95C%2F7A1ISTefgVVQp2g0QMBQXDv6x98eFJdYedti5MXOrbSd1fwJyolekzzMUp08nhhZzKiHUfuWLbT4PprBRE20NIDMjQKUFiA2CFijX7aiE5PxKsEg17gAnWs0M0BMLWbwvfCgT9eqYvmJ2bcdP9OB65VHvsvTTDFcT0AYB1wITwP6U3sxFRg3k5PGMJENw1I%2F5f6hG6HeZJ%2FxSPo3LKG%2BM%2BuPeY2eXVsLc8eWe9jvVkLNTu6LBYLRlpAIqXg9s0uV94lvs%2FCeX4kJbawe%2FZnXeB2fECnMVxNLX7Fjtg%2FBU5WFa4qAQ1k1%2BBKkyqiHU9WCgO9q3ddRYG2zAUzRq0P2b0LISRJiStIt%2FMS817FdBKl8pYrlT%2B1bhLbOAMZc%2BUqjzNWBB3XxHwz7lL3ySMl6CBCJ%2BpMvYI49jyL%2BDvzFflgZvgfwq0FP0MPv%2BQCIED1pQ3QeML%2Ba%2FtAGOqUBsj1IwuVOjSlGr4x8grBJzJFs3Vld7XXkbPq8UdLjF8SuPA6sSgKYlc2wflti2dk0nwtNjaIlbTBp2SpO5ph3Gh91w50pT1gziDeT4DqRMI2euZ2LfQ%2F%2FI%2F3nnl%2FRpQ1ZltBk8u2BuP8UAw6nmIiRxqhEKWBA7VDeRGT8a%2F2KqM8rf8O9%2Fooc6Y8R7rLorKzSHC48GH6JAaoZRSqKUMvIkGoEnmT8&X-Amz-Signature=9c11372180cfc0b02da50afad40bb9349590f1714724ce474d25bfe9bbe07242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3XBMPEL%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T023558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQDyQALxiq1E%2BvBH%2FICuRsERspV1cZ2YyBe313HFgcGEnwIgaKjmfMWhmYgzphvmEO2hQ1KF%2BevewhYfTosgJ8spZ%2FMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDJyhdnZpPGLrYDEJ5yrcA3nqGJ8CLQN3KbkQstDWZjhQDudCGSVYsSdnHoZ39fINQncxA9lKtrU9vTaME2wLZzCnhPJO2ziTdBk0zCLfTSovQSaBgRTms8D1KAKfDg66Y5T8V9G5BYi%2BY7%2B5eALaFKbZZvGa2utPy3ZbClzdSJvjGGXysWUyQ5jCsby5pWbxt80iTvWg95C%2F7A1ISTefgVVQp2g0QMBQXDv6x98eFJdYedti5MXOrbSd1fwJyolekzzMUp08nhhZzKiHUfuWLbT4PprBRE20NIDMjQKUFiA2CFijX7aiE5PxKsEg17gAnWs0M0BMLWbwvfCgT9eqYvmJ2bcdP9OB65VHvsvTTDFcT0AYB1wITwP6U3sxFRg3k5PGMJENw1I%2F5f6hG6HeZJ%2FxSPo3LKG%2BM%2BuPeY2eXVsLc8eWe9jvVkLNTu6LBYLRlpAIqXg9s0uV94lvs%2FCeX4kJbawe%2FZnXeB2fECnMVxNLX7Fjtg%2FBU5WFa4qAQ1k1%2BBKkyqiHU9WCgO9q3ddRYG2zAUzRq0P2b0LISRJiStIt%2FMS817FdBKl8pYrlT%2B1bhLbOAMZc%2BUqjzNWBB3XxHwz7lL3ySMl6CBCJ%2BpMvYI49jyL%2BDvzFflgZvgfwq0FP0MPv%2BQCIED1pQ3QeML%2Ba%2FtAGOqUBsj1IwuVOjSlGr4x8grBJzJFs3Vld7XXkbPq8UdLjF8SuPA6sSgKYlc2wflti2dk0nwtNjaIlbTBp2SpO5ph3Gh91w50pT1gziDeT4DqRMI2euZ2LfQ%2F%2FI%2F3nnl%2FRpQ1ZltBk8u2BuP8UAw6nmIiRxqhEKWBA7VDeRGT8a%2F2KqM8rf8O9%2Fooc6Y8R7rLorKzSHC48GH6JAaoZRSqKUMvIkGoEnmT8&X-Amz-Signature=bcc8f8c639957311b30dfa3a5e99353a3537e7b971fe39d6677d7557eed7f382&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
