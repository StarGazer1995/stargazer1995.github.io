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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7EJY5J6%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T125541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfsbTvcajqXsoHAS%2BZSdEd%2FFajI6%2B27bFWO3wgCDwC7AiBhdtcjljP%2BOJXyXEaw4%2BRMGLr72WSKncuQdznCFBfjwCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHeTO5%2BOVzcQymdqCKtwDP9suIYh3qgAdGFYl3g%2Bs1Izs4iX03AmTKw8Q9%2BbxJ23I4k26YWUrHEUKLRTuNdmB4nbI4bONeMFzNPYt5In681J0yXSgHRyrjkVMxGnOhWM7M2d7Uw3CwMl3K22ko%2B00cLxsadxLERHO9e1aCN%2FjHAongdPPHJkm3nXw1uxEp%2BVPCaH9EeziYKJlat4%2FgEkleY%2FZz0NdFRbuyg%2FVdkjcFTt6vFJvfQKGjFyiek4iK%2B1GFoLm1jhFy33pgACtMxYuAtu%2BCw2V%2FW%2BUyA%2F0uMsfXYgfPElUW74%2BuFGTvR7eVXpWVFhkBqPxeZ2Xe64bGnwmwapgOv18BulWPzFw8s9UINZNVp0cARKaj4PVFI52js6vD9M8hI8WMa1rGXt4mGryIyH67S3hiu1xe30xN20NdTW5KGdS9bm0rJ%2BCgAX14ULDrMhU%2FaLNtugpHhfUyEDV3j0KqovDpTllGWlOt9hhLMpBGDn8QnxjOl%2BPTBiJ3VefW1FXqervxOA8QFocRglTY8UsUURDgU6ExS6AZJ3mDf5o9ekheNzPC6M8JKtpfkXC9iD8HUtQRN7LFimRJJ6FDRB5TFTGwGpzktFx%2Bc8W7F0a4ifmevw6MiUgWtzlGidO5%2Bb2ksjSeFrep%2BQwr%2Bqg0AY6pgF9N%2Bf4WyfXGQ7z%2B755zpV0O%2BCtJM0dnYhBkUpiERbqHmR7SgiqtGB1RwavDMQmtUVeqq5273vj2qnTc0FilxxWer4f837DSWoV5bWtYDir2uN0e32HaJ%2BIfFCnjg4vG2Z75JotYdvc%2BDEXFK%2BQ6jZllOgn%2BMqkvTsknt70dIvZY9ROqNxe66LRIx6coyYy%2FuPnrv0yQPRBBv88od%2FsRDyvrnUotsFs&X-Amz-Signature=f60306fd9e3128a9a1938e6e932228862fab10612045c4beac41b1aa18d9895c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7EJY5J6%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T125541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfsbTvcajqXsoHAS%2BZSdEd%2FFajI6%2B27bFWO3wgCDwC7AiBhdtcjljP%2BOJXyXEaw4%2BRMGLr72WSKncuQdznCFBfjwCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHeTO5%2BOVzcQymdqCKtwDP9suIYh3qgAdGFYl3g%2Bs1Izs4iX03AmTKw8Q9%2BbxJ23I4k26YWUrHEUKLRTuNdmB4nbI4bONeMFzNPYt5In681J0yXSgHRyrjkVMxGnOhWM7M2d7Uw3CwMl3K22ko%2B00cLxsadxLERHO9e1aCN%2FjHAongdPPHJkm3nXw1uxEp%2BVPCaH9EeziYKJlat4%2FgEkleY%2FZz0NdFRbuyg%2FVdkjcFTt6vFJvfQKGjFyiek4iK%2B1GFoLm1jhFy33pgACtMxYuAtu%2BCw2V%2FW%2BUyA%2F0uMsfXYgfPElUW74%2BuFGTvR7eVXpWVFhkBqPxeZ2Xe64bGnwmwapgOv18BulWPzFw8s9UINZNVp0cARKaj4PVFI52js6vD9M8hI8WMa1rGXt4mGryIyH67S3hiu1xe30xN20NdTW5KGdS9bm0rJ%2BCgAX14ULDrMhU%2FaLNtugpHhfUyEDV3j0KqovDpTllGWlOt9hhLMpBGDn8QnxjOl%2BPTBiJ3VefW1FXqervxOA8QFocRglTY8UsUURDgU6ExS6AZJ3mDf5o9ekheNzPC6M8JKtpfkXC9iD8HUtQRN7LFimRJJ6FDRB5TFTGwGpzktFx%2Bc8W7F0a4ifmevw6MiUgWtzlGidO5%2Bb2ksjSeFrep%2BQwr%2Bqg0AY6pgF9N%2Bf4WyfXGQ7z%2B755zpV0O%2BCtJM0dnYhBkUpiERbqHmR7SgiqtGB1RwavDMQmtUVeqq5273vj2qnTc0FilxxWer4f837DSWoV5bWtYDir2uN0e32HaJ%2BIfFCnjg4vG2Z75JotYdvc%2BDEXFK%2BQ6jZllOgn%2BMqkvTsknt70dIvZY9ROqNxe66LRIx6coyYy%2FuPnrv0yQPRBBv88od%2FsRDyvrnUotsFs&X-Amz-Signature=4bb38793a09776b1f7c2d61044a6381da2fcc29082756711414c1552c02c0532&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
