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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRDYXDIC%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T043439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDpSd5B%2BAr%2B%2BF%2FQL1jS87PUFMIZLls9SH2A1NcK8pWVKAiEA4IhlY8QRfvzibLvBmVzoniptsI4bsCiaUCUOpUXL%2FfEqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAUm%2FwXLdQY0BUCSBSrcA%2Bk2d%2BqCbbYE2w1F4jy136QTfQGZtuFDYfY9Fm4ura%2BUwP6cT5nPeatT%2FftGQPEZvmgaSkbVBukMmA%2Bx9Xh8JfZ3ZjFgNlGRccFBMEGwRY36SeNxqh5H%2B%2BRUX7dWBq78XqwF%2FBqjXPmy3ebFtqaAaO30VWP35UqqXaDDnY5KA6UDpBvS3tUlkDaYhECa8DPMgFdNBwSHg%2BSKNBzro3zNkhApx9GKnkCV96tfQeDz3XIxBljawFvEAcaUG2AiK%2FDQ2q9jKNvzPGgu4CLpUtizvvecRkq%2Bv%2FcyFb%2FlDruVAjFHkxFZvTAoTW%2FdS4RG8hqyRLKivkXOh9Vp6BxtmBIZNyLOux47QsBXWMdfGu2Uca5FLU595nnUSy%2BEimGQ80NjDSqrHupKbDJZKGOIInSe0VGeucmcAoQ9LAZV9uaZ49Uz%2FuODuWMXBkCCWEeS3Vco4RFf5iMllpqQrItPHxMcXXGDC04BI42OempZI0rdZTCWqwkCnjU%2F9T2GmifJj%2FCbVI375H%2F3VqaPyuiDNbvAm6AAERwd6qverENrzQ8gbgK78tyybSEHTPiOJPD2Lmj7KODi8IL%2B%2BxBu9enPJE40YQ6DDUcx6auNIXCBbBE7wDdFYwyND7pYZdDak%2F%2F%2BMMDtrtQGOqUBx8aX2oi9jG4eTmwqDfZsklK8jM8J2DXHZy6LHQs1bF3JPsDfuxYClIv1SnMwdasBURgpS3o%2FwVTHcj1OcObsuKp0xDrYMIN4%2BdD3FAGaRRB4oLFxrV9tCJ%2Fr9V8l6BXH63SAHNx7ivF0IzqgHG1A2Z0Q1vRctpe4m6y4yh2nB5haeY1Mt2gO1C%2FGlKIlSR0HzzO0UmFaVwDjnp5m%2F3Ws1iL2O4pt&X-Amz-Signature=e1182574f2b8fa7b10a3a2a867e8ef6f46076a51060bac3814c15f7119b597aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRDYXDIC%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T043439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDpSd5B%2BAr%2B%2BF%2FQL1jS87PUFMIZLls9SH2A1NcK8pWVKAiEA4IhlY8QRfvzibLvBmVzoniptsI4bsCiaUCUOpUXL%2FfEqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAUm%2FwXLdQY0BUCSBSrcA%2Bk2d%2BqCbbYE2w1F4jy136QTfQGZtuFDYfY9Fm4ura%2BUwP6cT5nPeatT%2FftGQPEZvmgaSkbVBukMmA%2Bx9Xh8JfZ3ZjFgNlGRccFBMEGwRY36SeNxqh5H%2B%2BRUX7dWBq78XqwF%2FBqjXPmy3ebFtqaAaO30VWP35UqqXaDDnY5KA6UDpBvS3tUlkDaYhECa8DPMgFdNBwSHg%2BSKNBzro3zNkhApx9GKnkCV96tfQeDz3XIxBljawFvEAcaUG2AiK%2FDQ2q9jKNvzPGgu4CLpUtizvvecRkq%2Bv%2FcyFb%2FlDruVAjFHkxFZvTAoTW%2FdS4RG8hqyRLKivkXOh9Vp6BxtmBIZNyLOux47QsBXWMdfGu2Uca5FLU595nnUSy%2BEimGQ80NjDSqrHupKbDJZKGOIInSe0VGeucmcAoQ9LAZV9uaZ49Uz%2FuODuWMXBkCCWEeS3Vco4RFf5iMllpqQrItPHxMcXXGDC04BI42OempZI0rdZTCWqwkCnjU%2F9T2GmifJj%2FCbVI375H%2F3VqaPyuiDNbvAm6AAERwd6qverENrzQ8gbgK78tyybSEHTPiOJPD2Lmj7KODi8IL%2B%2BxBu9enPJE40YQ6DDUcx6auNIXCBbBE7wDdFYwyND7pYZdDak%2F%2F%2BMMDtrtQGOqUBx8aX2oi9jG4eTmwqDfZsklK8jM8J2DXHZy6LHQs1bF3JPsDfuxYClIv1SnMwdasBURgpS3o%2FwVTHcj1OcObsuKp0xDrYMIN4%2BdD3FAGaRRB4oLFxrV9tCJ%2Fr9V8l6BXH63SAHNx7ivF0IzqgHG1A2Z0Q1vRctpe4m6y4yh2nB5haeY1Mt2gO1C%2FGlKIlSR0HzzO0UmFaVwDjnp5m%2F3Ws1iL2O4pt&X-Amz-Signature=2c1871f4e075ef66f28a976389d665e2f94ef637710f53c87e482c53c1ac7ae2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
