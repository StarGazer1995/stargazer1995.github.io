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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4XB24UO%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T084411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf%2FvuuLHD4UqKNC9Ocr0jDuraTPWM2gpLoebSN2XJuQwIhAIsggOPitODcrM37delYFJgGY%2B%2FnKtPLGPLCLoYRTbYHKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzivCknAFe8vLGjjm8q3ANY3Ay%2B2q5jXvxMigF0lve5EJoZVMoVXqk21e6%2BzXsrB1toB%2BtY%2BIwYz9GyRWnt3kSnVfjDCy4UXkRgD%2BTMkB7JRNv5sDlQQ4qWS6yMNKJTjjijGcglWa0muvXRPB9yN%2FLdmKyhDpQNzjSpJhPU5qV4%2FxnCHF7%2FizMgI2b%2FQkepVk1Gltac6uTNDwQBRH6uom0pE4SUcGUTtnQ8INW%2BzzQMkChYWLV45Hhnig7abDWvcf06oVOJfqay%2BK%2F5q1C7jV8FXDl3RtaaIYIrZz4teoBKvxsaY6bVVXmv%2BEv0jks1jx%2BzVXhRVAegunmKEzbchLh2Ew0tkUW%2Fg84Kyjq3xUWOFYiAVDiYE7uA4AiIQ0QCHwFhRfoX3gp%2B6igIMSeExMRSM9O%2B7P5FerfIPmLQl5RIfpuTHFV3hwwwMERV%2Foxn7e%2FO1%2FWOj9tqiai3OK%2FhHqVSj%2FQnjs1YNW8oYofpcrAuv3NwUn6gS9q6tCFiU%2BrwkspLLEk1IVrBOFfE%2BfzICAqN3%2Fs6rzEk07zuS3ZGrRJ9ms6SkICeHXCVf2Y5wcnjeD%2BHXeSLUOFw4xE45zpCFYNgSImdlf8zkuzsr%2B4uD371e%2Bvm5dLKT%2Fq6i7dKB4bZerxcdtfegj7weyFCrDCP5ZnRBjqkAUZpjTsUiUbZ13rlZtLKDN5SyDMVGqWbN8CV5EAvEPxyXg34Wthi1bO%2Frpmq0EFlhHYOQe8QHi8f6LTsbOqdc%2ByoMCt1nIqjIBTovZwUn78GQZ6h80F76jV0F1H9VC%2F%2FlVWa6q3Fwq8KHty3T15vC1iPBbsCo4SL2%2FU0%2FYCujh8N5iqMrat4YG%2BoBX4Eohtlr8JAs9LCq3GB%2FFd6DqxgNnLgOhvb&X-Amz-Signature=6737d3b3894b7ac165fef2eca1686ddf6d18d23756d741878a04225c1d7dee65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4XB24UO%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T084411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf%2FvuuLHD4UqKNC9Ocr0jDuraTPWM2gpLoebSN2XJuQwIhAIsggOPitODcrM37delYFJgGY%2B%2FnKtPLGPLCLoYRTbYHKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzivCknAFe8vLGjjm8q3ANY3Ay%2B2q5jXvxMigF0lve5EJoZVMoVXqk21e6%2BzXsrB1toB%2BtY%2BIwYz9GyRWnt3kSnVfjDCy4UXkRgD%2BTMkB7JRNv5sDlQQ4qWS6yMNKJTjjijGcglWa0muvXRPB9yN%2FLdmKyhDpQNzjSpJhPU5qV4%2FxnCHF7%2FizMgI2b%2FQkepVk1Gltac6uTNDwQBRH6uom0pE4SUcGUTtnQ8INW%2BzzQMkChYWLV45Hhnig7abDWvcf06oVOJfqay%2BK%2F5q1C7jV8FXDl3RtaaIYIrZz4teoBKvxsaY6bVVXmv%2BEv0jks1jx%2BzVXhRVAegunmKEzbchLh2Ew0tkUW%2Fg84Kyjq3xUWOFYiAVDiYE7uA4AiIQ0QCHwFhRfoX3gp%2B6igIMSeExMRSM9O%2B7P5FerfIPmLQl5RIfpuTHFV3hwwwMERV%2Foxn7e%2FO1%2FWOj9tqiai3OK%2FhHqVSj%2FQnjs1YNW8oYofpcrAuv3NwUn6gS9q6tCFiU%2BrwkspLLEk1IVrBOFfE%2BfzICAqN3%2Fs6rzEk07zuS3ZGrRJ9ms6SkICeHXCVf2Y5wcnjeD%2BHXeSLUOFw4xE45zpCFYNgSImdlf8zkuzsr%2B4uD371e%2Bvm5dLKT%2Fq6i7dKB4bZerxcdtfegj7weyFCrDCP5ZnRBjqkAUZpjTsUiUbZ13rlZtLKDN5SyDMVGqWbN8CV5EAvEPxyXg34Wthi1bO%2Frpmq0EFlhHYOQe8QHi8f6LTsbOqdc%2ByoMCt1nIqjIBTovZwUn78GQZ6h80F76jV0F1H9VC%2F%2FlVWa6q3Fwq8KHty3T15vC1iPBbsCo4SL2%2FU0%2FYCujh8N5iqMrat4YG%2BoBX4Eohtlr8JAs9LCq3GB%2FFd6DqxgNnLgOhvb&X-Amz-Signature=3eb9992951ec8f25da47e779304ae7af3e4e6250ab7c4d225d1bbdda571ce7da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
