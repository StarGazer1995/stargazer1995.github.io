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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IKEG7LV%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T165500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIGAn7YrzJsvxJsn3EyH4%2F%2Byb9EjCG6eBO54jafcXTF7UAiEAicXuC%2FnbwhCTglutGOvghd0OAK8Wjakl8q03rKA%2B7W0qiAQI%2Bf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDuuHITpnMrz4gZc2CrcA5cQ5VX4JRdXOgdGEKmPwBJMgw1XLaLGrCV8qgLZyiEE4JdQO5ntBcZUSmuAbnbo%2FmeuXrwFjxd0M991QYlctAQgB6bAI%2FGWRIPc1xe%2B8QhL1UlQwhDt1d5GQXnAdj%2B0fIPX1F57DZfZm68RP02Sr3IwWKVZKjYxSJSHrpSOGinJLSMVHbjXetHmSpDioA8jFQ3Rt8iGQ0GJZk5ycbvdrNyssHRcTLBlsd2vvjw2ULYEb4JP4iCOL6gK4iBOtZRvZiFVbFI6iEitnkZjRmMBH%2Fft6F3bB1cbDrHPbUJ%2B7GweCI19NWXJKtdyfJ31LGWSoEaDa6fsm%2BBsJE2qMBipq%2BYNSVyUagb1O5VBIA%2BMcdhAti%2BJTXwnUIpfAhRgsczhl0nvIIAo4o%2FvQYMUeh9G6H%2F7VbkZkVHXTEaRPa6q%2BpWrwZMJAoNgZR0VG15bm2Ry6KqNN05O7QY5hnhExAIaA%2FtY%2BbWVUU%2F0piRkx51nxoVFJdcOTfuJN5ihFwLuVDFlq5woc6o6qTGbAdk9UxUqdYTgvi8TaRG1F2HcKI7xfTi4fB6%2FbSQG4827EXG2bFyLadIBaZJIwu17fzka1YwoS0cZZop%2FyMbYE1Y24DWolmhVUZYpTj5LyqYhYGb5MJOv8dAGOqUBa33bZL2ngYMq8FmjXd7aEOFKYkIp%2B8R55XJil7ZBXZTpcEBu7l3EN%2FuLpAsPBgUo2ly%2FF8khZCzUwSOxlyOEADYcE4DxLUhPty9wlHqMEpxwLkY6kLwdXtrcBpkiKEik5ZLAadzzagmITxqTlZnRPJJT%2BxRTHoXK3d%2Bl4pLGUpFp2zv9rlis%2BaKDRWjfvR48yGAr7XyutFd0vrFbB7koWzrEuyH%2F&X-Amz-Signature=8dec588cdacaa0b06b5c88e927e81bfd2c7dacddffb8b29d787e71d4abcd1f7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IKEG7LV%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T165500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIGAn7YrzJsvxJsn3EyH4%2F%2Byb9EjCG6eBO54jafcXTF7UAiEAicXuC%2FnbwhCTglutGOvghd0OAK8Wjakl8q03rKA%2B7W0qiAQI%2Bf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDuuHITpnMrz4gZc2CrcA5cQ5VX4JRdXOgdGEKmPwBJMgw1XLaLGrCV8qgLZyiEE4JdQO5ntBcZUSmuAbnbo%2FmeuXrwFjxd0M991QYlctAQgB6bAI%2FGWRIPc1xe%2B8QhL1UlQwhDt1d5GQXnAdj%2B0fIPX1F57DZfZm68RP02Sr3IwWKVZKjYxSJSHrpSOGinJLSMVHbjXetHmSpDioA8jFQ3Rt8iGQ0GJZk5ycbvdrNyssHRcTLBlsd2vvjw2ULYEb4JP4iCOL6gK4iBOtZRvZiFVbFI6iEitnkZjRmMBH%2Fft6F3bB1cbDrHPbUJ%2B7GweCI19NWXJKtdyfJ31LGWSoEaDa6fsm%2BBsJE2qMBipq%2BYNSVyUagb1O5VBIA%2BMcdhAti%2BJTXwnUIpfAhRgsczhl0nvIIAo4o%2FvQYMUeh9G6H%2F7VbkZkVHXTEaRPa6q%2BpWrwZMJAoNgZR0VG15bm2Ry6KqNN05O7QY5hnhExAIaA%2FtY%2BbWVUU%2F0piRkx51nxoVFJdcOTfuJN5ihFwLuVDFlq5woc6o6qTGbAdk9UxUqdYTgvi8TaRG1F2HcKI7xfTi4fB6%2FbSQG4827EXG2bFyLadIBaZJIwu17fzka1YwoS0cZZop%2FyMbYE1Y24DWolmhVUZYpTj5LyqYhYGb5MJOv8dAGOqUBa33bZL2ngYMq8FmjXd7aEOFKYkIp%2B8R55XJil7ZBXZTpcEBu7l3EN%2FuLpAsPBgUo2ly%2FF8khZCzUwSOxlyOEADYcE4DxLUhPty9wlHqMEpxwLkY6kLwdXtrcBpkiKEik5ZLAadzzagmITxqTlZnRPJJT%2BxRTHoXK3d%2Bl4pLGUpFp2zv9rlis%2BaKDRWjfvR48yGAr7XyutFd0vrFbB7koWzrEuyH%2F&X-Amz-Signature=c0c73184bae129c51ece361ae73d8b5c01a468ca8eed09545ef75dca7fd5a80a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
