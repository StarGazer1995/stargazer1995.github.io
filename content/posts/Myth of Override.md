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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634V7ML2I%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T051830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD00dWx%2Bt1%2BzYj5CQACillz%2Fy1m2dfIDh%2FupF8%2F1vlerAIgNlrLBjRkdN1RjGEZUpdlITQzet0phcHDwAzDGLzo8swqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEAU5s0Llgs72abybyrcA7fdLD%2F3kI5JbHdYdebGqeSufqwMWXeNvT1qLdh2IGrv60XNeA286504AVUv1b2FAo8ZMazAyOHuXYAofGozWWU9O8ThcbTLdX1O%2FrepostH9eYW%2BWyMoV%2BtWlmMIB%2FWufWj5FQdh9ELBxi5y8v9Sg%2B3U7QAIodrLN3sVS99qmi1F8CPeogG%2F0udwNSvEc8lbOmfovvtMDkDbQSuz2sl9YuRn3p78pXHHedhOb3hLrVLJpJNLzqUoKkZYF0T8aNWbC6xVUyf2tFQKtnWnGzjXrwgz0cKaHCtF8Wz2K%2B72nC%2FGDeG5KgTwK%2F6waMrvhPLTlP1WcF9fH5PR%2FesCzsN3Y9OnQ1RFNVUYBqiSoZYYi8Vljx7o0Me7GcdYwGVxmVd%2BDoNfbRGVAYlYjAhslMEgQZjcLyw6bjpSm1S%2FSizekVAmYhsJ3RrwuDegj4wNKXIf4nyR%2BYPiUJN3YQemzUKjDVRNeRX8krLAS1hLN1J4djjPTIqEuLIyxy6g3VvmkWB5SuxHkN%2B2CabPHBn1nFrdpjQlpoxBq97LD3AQZAwzJUrniuO9QLj0ttl3ot8aPhOhU%2BWAhLPjpv%2Fm%2BdTDAjhWei05dCJ5c2CTVzEm%2B9tyfn%2FElOAorgaMHCpxZCPMKfhtdMGOqUB7EfLav2xGkZCJOd3WyMuZAh8x0fK20v3cBsxJcylyz4d6cAPZfAArR9r12HHcjRSuE0eNFXPdkFu2RM42IuyrIXemc3%2BedEr9Njob9Sma3pssoyvBZz3%2FjhAFM6tGFwAPjtORyAvEeqB75%2FLdttRjDmQx6T3XgrtgX49SB9ZLtpKID%2F1nmk7OsLYXdsJ2kOEZshbEHe%2BvpKiwCKrr42Czaye1wfb&X-Amz-Signature=81f664101291870c6508390c64aeaaa3809f64a328bb9bed4dbd1e594bbada15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634V7ML2I%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T051830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD00dWx%2Bt1%2BzYj5CQACillz%2Fy1m2dfIDh%2FupF8%2F1vlerAIgNlrLBjRkdN1RjGEZUpdlITQzet0phcHDwAzDGLzo8swqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEAU5s0Llgs72abybyrcA7fdLD%2F3kI5JbHdYdebGqeSufqwMWXeNvT1qLdh2IGrv60XNeA286504AVUv1b2FAo8ZMazAyOHuXYAofGozWWU9O8ThcbTLdX1O%2FrepostH9eYW%2BWyMoV%2BtWlmMIB%2FWufWj5FQdh9ELBxi5y8v9Sg%2B3U7QAIodrLN3sVS99qmi1F8CPeogG%2F0udwNSvEc8lbOmfovvtMDkDbQSuz2sl9YuRn3p78pXHHedhOb3hLrVLJpJNLzqUoKkZYF0T8aNWbC6xVUyf2tFQKtnWnGzjXrwgz0cKaHCtF8Wz2K%2B72nC%2FGDeG5KgTwK%2F6waMrvhPLTlP1WcF9fH5PR%2FesCzsN3Y9OnQ1RFNVUYBqiSoZYYi8Vljx7o0Me7GcdYwGVxmVd%2BDoNfbRGVAYlYjAhslMEgQZjcLyw6bjpSm1S%2FSizekVAmYhsJ3RrwuDegj4wNKXIf4nyR%2BYPiUJN3YQemzUKjDVRNeRX8krLAS1hLN1J4djjPTIqEuLIyxy6g3VvmkWB5SuxHkN%2B2CabPHBn1nFrdpjQlpoxBq97LD3AQZAwzJUrniuO9QLj0ttl3ot8aPhOhU%2BWAhLPjpv%2Fm%2BdTDAjhWei05dCJ5c2CTVzEm%2B9tyfn%2FElOAorgaMHCpxZCPMKfhtdMGOqUB7EfLav2xGkZCJOd3WyMuZAh8x0fK20v3cBsxJcylyz4d6cAPZfAArR9r12HHcjRSuE0eNFXPdkFu2RM42IuyrIXemc3%2BedEr9Njob9Sma3pssoyvBZz3%2FjhAFM6tGFwAPjtORyAvEeqB75%2FLdttRjDmQx6T3XgrtgX49SB9ZLtpKID%2F1nmk7OsLYXdsJ2kOEZshbEHe%2BvpKiwCKrr42Czaye1wfb&X-Amz-Signature=a7b547b66630aa7139b944b46dcfac5d70c1b9c28ecab1c0287dbc0866cf88e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
