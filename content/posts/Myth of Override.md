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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNWLMNYV%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T172251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCkZO5exZxX2Ek8ZC%2B37cEAICeUrOAvYuKtRGvCyfPwMQIhAP2PuxkOrv7OqHK1iG3bjYcjWB2XVJAwpV%2FnTYevdcdAKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyP%2Be0a2ynPhrQxH%2Fkq3AM9ygHqnczEpYSv2XefhTfskMqA0OxhXFX7D1mVlaPDj8lsVHfzbUC6YSg362GphivqY6U%2BZxiqo6Wl2uDqlv8MImH%2FwPseKUbBofyujgv7WfmDnfFlASqyNzoNBO7Mp3kjHw43TwKUX%2FMcUhK6BrUGhMPb4wvyuq6VK8rvDNs64B58%2FWZHicazAuwyJpw%2BQLrga0FCEsYhT7MHxcmC39Q%2BvrekkVCvnE5TDjwfpSHEzcGnhSRbY%2FETf9rPQHzIG0W1puUTBuxKSi7tUbjcemRxxXvm6EIFK2xWl4q0Rvl0S8BZmwxd1mw%2FnMB9rKBZdy8jE9buXcZy9RDJdQ1%2Bekj7%2FpVmRPnCSz7xIIE8UF6fMEeRNBtKnfBG8aIFBQC7g8CJPaMx0dPauZTE%2Fup2Sg%2Fo5ulv9JNDmdaUlYPsze7t7dpQrylwoHQPkHx%2FWdc1KnnL1qS63noDOZE5%2BkjIHkBjW2PL6ZLNiMzFgx9CzSXwsuON7vE8dntMG%2F65uJ99zv1zC3kLBTgwXsXeEtkvGzJKtmx4ukeTAQlGo1NBCTL7WuIJeGgySVZXUzSsQjlNlhJR%2FMKs6bGX5tTY4r42ZGbTiKf2Rvx8iO%2BHrNWvrFYHxMY47ClBNVxLxs9UIDCtnubUBjqkAaKoQmw8q9orbQOQCdq46l1rfYeXxEi8rI2m31zDe0%2BPAFz8Hh%2B4fcexSxSO8QSJw4p7725I1UTBuGFOPEpLUEABUGw7OFiePe7dXrXJEeDyjUEH192xRPMfh2FV6OwuTximYkXJEIeGxbuOCmGYrRWOEFWgWP1Yu86HNUS2xxNB6cdP5go8suc%2FC5alUrCBY3EGDB25QSS6k1JAAH%2F6lzQwScFz&X-Amz-Signature=0864bbf65f8636f610abfb51f9400c52107e47b2c6ead158140d330ee03c6655&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNWLMNYV%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T172251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCkZO5exZxX2Ek8ZC%2B37cEAICeUrOAvYuKtRGvCyfPwMQIhAP2PuxkOrv7OqHK1iG3bjYcjWB2XVJAwpV%2FnTYevdcdAKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyP%2Be0a2ynPhrQxH%2Fkq3AM9ygHqnczEpYSv2XefhTfskMqA0OxhXFX7D1mVlaPDj8lsVHfzbUC6YSg362GphivqY6U%2BZxiqo6Wl2uDqlv8MImH%2FwPseKUbBofyujgv7WfmDnfFlASqyNzoNBO7Mp3kjHw43TwKUX%2FMcUhK6BrUGhMPb4wvyuq6VK8rvDNs64B58%2FWZHicazAuwyJpw%2BQLrga0FCEsYhT7MHxcmC39Q%2BvrekkVCvnE5TDjwfpSHEzcGnhSRbY%2FETf9rPQHzIG0W1puUTBuxKSi7tUbjcemRxxXvm6EIFK2xWl4q0Rvl0S8BZmwxd1mw%2FnMB9rKBZdy8jE9buXcZy9RDJdQ1%2Bekj7%2FpVmRPnCSz7xIIE8UF6fMEeRNBtKnfBG8aIFBQC7g8CJPaMx0dPauZTE%2Fup2Sg%2Fo5ulv9JNDmdaUlYPsze7t7dpQrylwoHQPkHx%2FWdc1KnnL1qS63noDOZE5%2BkjIHkBjW2PL6ZLNiMzFgx9CzSXwsuON7vE8dntMG%2F65uJ99zv1zC3kLBTgwXsXeEtkvGzJKtmx4ukeTAQlGo1NBCTL7WuIJeGgySVZXUzSsQjlNlhJR%2FMKs6bGX5tTY4r42ZGbTiKf2Rvx8iO%2BHrNWvrFYHxMY47ClBNVxLxs9UIDCtnubUBjqkAaKoQmw8q9orbQOQCdq46l1rfYeXxEi8rI2m31zDe0%2BPAFz8Hh%2B4fcexSxSO8QSJw4p7725I1UTBuGFOPEpLUEABUGw7OFiePe7dXrXJEeDyjUEH192xRPMfh2FV6OwuTximYkXJEIeGxbuOCmGYrRWOEFWgWP1Yu86HNUS2xxNB6cdP5go8suc%2FC5alUrCBY3EGDB25QSS6k1JAAH%2F6lzQwScFz&X-Amz-Signature=1f0e0d687f99317d3c7ea59469b5d1371759ecb0260c27ddf7450ac300260fe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
