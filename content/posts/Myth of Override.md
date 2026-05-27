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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQIBCTYA%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T112812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQ7xHrCpAyfT2wdANLy8pSI0SWkP6CEKPo%2Bw0O8fj%2B2gIhAMn5pIZt%2BEdzeqHYpmeVckShwXWtIvtQjYH9w7BdzhfYKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzISbwgY5iPQLcVlmgq3APWA8a4hQrLm7CPZv%2Bu%2BXm0io47j1uVcpqffybMMn%2BJW7iIqaVNapQhZCdTZ8wPl9TfNLs%2F7dHZUG%2BUMwu%2Frh9CR4yYBDUWhbDsjtOzKt72QBdTpb5ZIXM0VAP9o5NIX0iifFrtbJEmE0ocuC4Rr%2BcTgsWynmgA9NmNjuvQWJmsBGAfdQBS440%2F5V15eArQCz8%2BgnHJt9U33pDt9MQbTDmSzvFDYE6DQfvnj2xttW%2BpZS7krYxYQmITAXxdtis9sOSd65JFXnBzoLNmz%2Fijdzsfu1%2BD3QgPJyUQTNECov8bBS4RyTMnPqL%2BttYWM0hw3O1Vb6wFNZTm%2BlaMEssqCyGLluYvfWsz9l8Gqb1tknYukOEl8pw6aS1LzX3ghS%2F2t9O0conRPH3GEI%2FRvd7FL%2B5cKIpudlGdnvLGFZSk8IqySPZHxrBPdqgYSOX31%2FVC%2F6o720kJ0mWxGqqmIhs8jY7UH%2BWXlhzTnIaWa5ABKHxvmYZdN3KPp5SvXUk9tsEZ3R%2Fps7dZ5H8aYmrHYOq%2FgZHzilDd4apbZyYrZLF3YQAJywfKBtNOgicqZMP2YAn4TsAca1WO5HF23V96DLsGYjRKcVKLnoE9UUVsOA83jC%2BjU257cOX9B6HdxVkCzzDhpdvQBjqkAd5rkCK61AS8OiNnwQxoU6etMy9%2BIQ0YbCDVSM9PJwK0EonlRXVKR84CG7WiZ9v9eY7ExWSp1Zr9makS2A4CRkVan2J6M2YiqIka%2BpubMJbpMAJFO8xUyx3GoM45O08FLyCSjsyYGB3pLkAzaqvrk%2BdTiTPpmxhzXDf%2FV2hOn7VtEfivafvjjgLTqoRpAk8E%2BRuxXrgEJCqgp45djDyURMXhhJy3&X-Amz-Signature=b8ae5632fc38702b01af7d8c8f7e74972290b0b68961556a90fc21d77909604f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQIBCTYA%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T112812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQ7xHrCpAyfT2wdANLy8pSI0SWkP6CEKPo%2Bw0O8fj%2B2gIhAMn5pIZt%2BEdzeqHYpmeVckShwXWtIvtQjYH9w7BdzhfYKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzISbwgY5iPQLcVlmgq3APWA8a4hQrLm7CPZv%2Bu%2BXm0io47j1uVcpqffybMMn%2BJW7iIqaVNapQhZCdTZ8wPl9TfNLs%2F7dHZUG%2BUMwu%2Frh9CR4yYBDUWhbDsjtOzKt72QBdTpb5ZIXM0VAP9o5NIX0iifFrtbJEmE0ocuC4Rr%2BcTgsWynmgA9NmNjuvQWJmsBGAfdQBS440%2F5V15eArQCz8%2BgnHJt9U33pDt9MQbTDmSzvFDYE6DQfvnj2xttW%2BpZS7krYxYQmITAXxdtis9sOSd65JFXnBzoLNmz%2Fijdzsfu1%2BD3QgPJyUQTNECov8bBS4RyTMnPqL%2BttYWM0hw3O1Vb6wFNZTm%2BlaMEssqCyGLluYvfWsz9l8Gqb1tknYukOEl8pw6aS1LzX3ghS%2F2t9O0conRPH3GEI%2FRvd7FL%2B5cKIpudlGdnvLGFZSk8IqySPZHxrBPdqgYSOX31%2FVC%2F6o720kJ0mWxGqqmIhs8jY7UH%2BWXlhzTnIaWa5ABKHxvmYZdN3KPp5SvXUk9tsEZ3R%2Fps7dZ5H8aYmrHYOq%2FgZHzilDd4apbZyYrZLF3YQAJywfKBtNOgicqZMP2YAn4TsAca1WO5HF23V96DLsGYjRKcVKLnoE9UUVsOA83jC%2BjU257cOX9B6HdxVkCzzDhpdvQBjqkAd5rkCK61AS8OiNnwQxoU6etMy9%2BIQ0YbCDVSM9PJwK0EonlRXVKR84CG7WiZ9v9eY7ExWSp1Zr9makS2A4CRkVan2J6M2YiqIka%2BpubMJbpMAJFO8xUyx3GoM45O08FLyCSjsyYGB3pLkAzaqvrk%2BdTiTPpmxhzXDf%2FV2hOn7VtEfivafvjjgLTqoRpAk8E%2BRuxXrgEJCqgp45djDyURMXhhJy3&X-Amz-Signature=498485bf68f43b093a4703d417e548df5d64346d73d334ebde3050c763c53d0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
