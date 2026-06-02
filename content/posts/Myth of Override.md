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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXOLSFPF%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T232641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCG3IUDPhfnU06zM7Gp7of%2F5zUYj8cc9YYnHePNy4dq9wIgVKU4MkZRheFQZWqY3JYN0TD%2F1hffqWrh7Q7hILEN1ckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDP3TSCZjmsTM91ATbCrcA%2BnjffxJhjisOSZRwrxh42YCc%2FxBX1RTtCYYMxr5AosN2a6EI2kEv7YNatniWO1pRRZAr6KcmuEG%2Bg1ySGmC3mVgeNriU4BOd482aV%2Bn53rECUaGGhJ12cZxYKvjQpwuotLBZik4eG2ew8leAKbrI5AAKXbk9wCIIzr7x1egsFXQSgqufDKadvF1NRKwaH2WWeIosZjCS08Uuo%2B%2FTsWUeeZZkREMkBbStB8D7wI6KdJtgQ34vsRDSrB4alWGotcs68twD6ckOSho78zz6oQtPzwVOU2YIBF6HITh4TflIGA89Z%2B8WOVdQXPQONIhGxD7g093tXzjsA5GQUhGUPobNxiYa2ZgORsKNoES%2BXEcb9zs6TnoUA1fAUEEUUD%2F7yGAfK0Iq99agsFaLXCqb4t%2FaR7JVEY92fRzui8wTTAFOgfMQYos7%2B%2FbrpyqYot48Xymh0He47%2FNNNqMDWCh%2BK0aOzTvhmxCgh%2Bw%2FA5uk2TgH1Z55MsBM9V35bnYYjmS9fz0qbnisawmwXBuJfnUvk2QgCBrZ7QyJMr7RzyoxAm56pvkW3E4L7y7OPdFBbuOjaGsZ6qoaKb02%2BDxbYuq5cPsHM7MQVOapi4ovrd1sL9PIwHuL7ceaJiKL%2Fx9iI84MKfS%2FNAGOqUBAjYqnPkeugtZCgu8uV8KAJJLJpmROI2h9tZFknDpX%2FfIdXbqtzwmvFiisGlV6r8xXMPPm2JrChVAXJq8mk3CUx930fIT3jyPrOVZPW%2FTpcGsPgto5kofLSZHkmXMgEEE4aByZgknj2M2Icz3weuM5pk7vosp5DaJdB4u3hR8Zq%2BK0VNJjFWFEvmHh6zCzHIJtPHXFxzKbQ%2FdzPcl%2Bb4OIXREgKJF&X-Amz-Signature=c0534a48d5e4c2b384226f5bf6ef274ae7c28362ac898fcb84cb351c71013230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXOLSFPF%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T232641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCG3IUDPhfnU06zM7Gp7of%2F5zUYj8cc9YYnHePNy4dq9wIgVKU4MkZRheFQZWqY3JYN0TD%2F1hffqWrh7Q7hILEN1ckq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDP3TSCZjmsTM91ATbCrcA%2BnjffxJhjisOSZRwrxh42YCc%2FxBX1RTtCYYMxr5AosN2a6EI2kEv7YNatniWO1pRRZAr6KcmuEG%2Bg1ySGmC3mVgeNriU4BOd482aV%2Bn53rECUaGGhJ12cZxYKvjQpwuotLBZik4eG2ew8leAKbrI5AAKXbk9wCIIzr7x1egsFXQSgqufDKadvF1NRKwaH2WWeIosZjCS08Uuo%2B%2FTsWUeeZZkREMkBbStB8D7wI6KdJtgQ34vsRDSrB4alWGotcs68twD6ckOSho78zz6oQtPzwVOU2YIBF6HITh4TflIGA89Z%2B8WOVdQXPQONIhGxD7g093tXzjsA5GQUhGUPobNxiYa2ZgORsKNoES%2BXEcb9zs6TnoUA1fAUEEUUD%2F7yGAfK0Iq99agsFaLXCqb4t%2FaR7JVEY92fRzui8wTTAFOgfMQYos7%2B%2FbrpyqYot48Xymh0He47%2FNNNqMDWCh%2BK0aOzTvhmxCgh%2Bw%2FA5uk2TgH1Z55MsBM9V35bnYYjmS9fz0qbnisawmwXBuJfnUvk2QgCBrZ7QyJMr7RzyoxAm56pvkW3E4L7y7OPdFBbuOjaGsZ6qoaKb02%2BDxbYuq5cPsHM7MQVOapi4ovrd1sL9PIwHuL7ceaJiKL%2Fx9iI84MKfS%2FNAGOqUBAjYqnPkeugtZCgu8uV8KAJJLJpmROI2h9tZFknDpX%2FfIdXbqtzwmvFiisGlV6r8xXMPPm2JrChVAXJq8mk3CUx930fIT3jyPrOVZPW%2FTpcGsPgto5kofLSZHkmXMgEEE4aByZgknj2M2Icz3weuM5pk7vosp5DaJdB4u3hR8Zq%2BK0VNJjFWFEvmHh6zCzHIJtPHXFxzKbQ%2FdzPcl%2Bb4OIXREgKJF&X-Amz-Signature=d9ec81ca62a60ca5400809232959d87141b9a1e465785db0befa5e684c5f56f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
