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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYKBEZCI%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T190408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDf2nYcCcwjj3Q2SSnMwMISkcjEQf%2BNMFPkiiR%2B11laZAiEAvQnW1AZ4TA5p%2BdaQAgVHufAupX8D3xXeXnWX2fQ8wgcqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAkucy5Yz21ARSIEFircA7e4l%2Ff%2FxzTdxnddYBFwu5qwPHmZoBpZzZeIFdZPCvGk1Omn6kAJrBKbo2ODzXLrMobbdwQtSXC6X65BtOrZZnjOtKRgZrW76M8lb35VeJ7Y8uYTwS6%2FZ29S4z%2FaeUQn2jDPqePYSv%2Fogc2Qpkr34DP%2FOtRfMLioMIBwCqTmZ6RNbXCDR3E9gluYWGQkjwcVBDqiYedoGNCZDEgiRZnAIrWLcIJ8Ga3h4ygwp1Ydwf%2FOFjXToCekV0s4o3MmOpOUWOqBkX4fTDPp70XhVWucLE%2BGtVCPs14nUm4rrenf4ZTESCKd3pGfM1lQqeUBUdYPkihQCPcrHULEgzGHkxKFThVffBkDBzfLO7dZ1niuVy6c%2B8UqbJd4mxzZmaI5fZVXkRi4OFO%2BbH9PFlsEx%2FP1AcobKXnOcXvN%2FUEzztXBVtGP3LFAVR5kpDt0jxcu18Kjdpsozu8rNSl%2F5D4%2FvM73QdVOBfHsQbaBldnN%2BLdIo1e73Z%2FwK6tcXLFRcEpY2glUaxYzBbKIO0q%2B1synzYGdDGB%2FQl1uCS5ctgY6jkAzadzTVlt0YC6or%2BRDhtraAJUz%2FmBleMi4C7r8XjmsLCJ%2FUCDq1tXoF3k0zE7FPgo%2FVRDIhsJM954%2FGYTKMVHgMPngltEGOqUB89sEaTSfaR6jADZVLSE4L9HoorTfOaDYry%2Fb858NaZ2u8KhNjo6%2B%2FsdVfbRdQwvc82wglhsmvheFN16o1lOWlX0bAHo9WN7JAKjnXFNqQ6qwzS%2B4JTKQwg6WGyB1Y6Um5rAWvw0w1oCEyvYDLB2O%2B9iG%2FZP0yqN6VTbf7D0zehkd%2BrRN7yoqSAkSWCZmJ5wuZc2E0J%2FfyBeu%2FC32qGbcoc%2Fd06jG&X-Amz-Signature=19f1ce2a1fe5009a17ac313d630bb63684a134d35af89e4ae86252314670b0ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYKBEZCI%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T190408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDf2nYcCcwjj3Q2SSnMwMISkcjEQf%2BNMFPkiiR%2B11laZAiEAvQnW1AZ4TA5p%2BdaQAgVHufAupX8D3xXeXnWX2fQ8wgcqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAkucy5Yz21ARSIEFircA7e4l%2Ff%2FxzTdxnddYBFwu5qwPHmZoBpZzZeIFdZPCvGk1Omn6kAJrBKbo2ODzXLrMobbdwQtSXC6X65BtOrZZnjOtKRgZrW76M8lb35VeJ7Y8uYTwS6%2FZ29S4z%2FaeUQn2jDPqePYSv%2Fogc2Qpkr34DP%2FOtRfMLioMIBwCqTmZ6RNbXCDR3E9gluYWGQkjwcVBDqiYedoGNCZDEgiRZnAIrWLcIJ8Ga3h4ygwp1Ydwf%2FOFjXToCekV0s4o3MmOpOUWOqBkX4fTDPp70XhVWucLE%2BGtVCPs14nUm4rrenf4ZTESCKd3pGfM1lQqeUBUdYPkihQCPcrHULEgzGHkxKFThVffBkDBzfLO7dZ1niuVy6c%2B8UqbJd4mxzZmaI5fZVXkRi4OFO%2BbH9PFlsEx%2FP1AcobKXnOcXvN%2FUEzztXBVtGP3LFAVR5kpDt0jxcu18Kjdpsozu8rNSl%2F5D4%2FvM73QdVOBfHsQbaBldnN%2BLdIo1e73Z%2FwK6tcXLFRcEpY2glUaxYzBbKIO0q%2B1synzYGdDGB%2FQl1uCS5ctgY6jkAzadzTVlt0YC6or%2BRDhtraAJUz%2FmBleMi4C7r8XjmsLCJ%2FUCDq1tXoF3k0zE7FPgo%2FVRDIhsJM954%2FGYTKMVHgMPngltEGOqUB89sEaTSfaR6jADZVLSE4L9HoorTfOaDYry%2Fb858NaZ2u8KhNjo6%2B%2FsdVfbRdQwvc82wglhsmvheFN16o1lOWlX0bAHo9WN7JAKjnXFNqQ6qwzS%2B4JTKQwg6WGyB1Y6Um5rAWvw0w1oCEyvYDLB2O%2B9iG%2FZP0yqN6VTbf7D0zehkd%2BrRN7yoqSAkSWCZmJ5wuZc2E0J%2FfyBeu%2FC32qGbcoc%2Fd06jG&X-Amz-Signature=37071214bf30da46a6de7b494a6f9f3a95d01d6c1b336e90d256a5d6bc6b5428&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
