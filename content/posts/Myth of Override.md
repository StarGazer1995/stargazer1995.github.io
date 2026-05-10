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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665LMTCGR%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T092120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQC4aZTQ9cWladzlLZeFmC2bFLdMBFU3CXUksabuKK5QAgIhAM6su%2BmRPCbMMEI6LEpMtpzbedQsUdguBEQ7m0tgZAyrKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAKmp%2B4a%2Br00EKGZ0q3APfsqaCYa2ogR%2B5d0ISxvVaqjEzZnyN3la%2B94vR62SOojLN0TUVqokErAKNjgArUIIbLIzl%2BHp5PepRGeUZt82zjwi%2FGpxUi5FMMdR6qEFmdTuEOwbFaWZjWSfNWPUY2xllK0MEZOuXnPz6c0iCABIaGJi0u8mKAIQNioHySGXNI36H%2BcB3Sq47IR5buhhpyw54RTGn4jrrWtpkrDFvkU%2F0K4C94423M1GqoKK9HMaC%2FppCE35c%2B4OEHgVk1zGautt6kU0LURX%2BBDnyv3iSrcmXYKLb6D9JjvUBa0hHs%2B9aCuu%2ByBTYDGcwijtVASAzCuUTRcvWUVGazbtNBu%2FMKJqS7fLmdpGJNxBIepfk2WDJkfTnLdjCJHQSZUHxTI3tvmPhXuE7bEqJspNKSBN8i6uEUTSpwH0MQXIwYw8hmeFTygyyYqYKP2PrVyW3%2FDVlDBM7yBNqgco%2FOm6nbARQRmLVtH29GQ91zID7K9uZwvxhT%2BF6cxkHQ1Fak4bmT4m1e%2B8dOlWjued%2F8FbXr4A6aQCP0yXPvZG9Rxvg01ZlystFMzzO%2F4WgDKDp5NZTXqYHUZGQ9%2FOC2aZI7586d7b73ezAKAg9Ba%2FiFHAgFFM52zak0AdjbL3tm3zY5fYoOzC6koHQBjqkAYkUkkN0s1op%2B6eKt9EF3aXMvkc7EXk%2FTXXoM3FGl7wOhO1KqS12jGBoik0uK%2BZPOlmNTP7nWZc8S039KjqKw%2FqziciD4zRGmaI7IO11eHYeNH5V22eKFAfeNBG528NeKJMFCu6yLLVk%2B0IDgR68XE6TfA90R7nqsaHpNyg1nGAZIc4UluhGdrVgeDiSHAqRliorugj3R2%2FNEvzUWOQr%2BBrUNEX3&X-Amz-Signature=f4fbeb814e3f7a54094aa015a0c8a44520a224a2a7222e526ae13144549be481&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665LMTCGR%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T092120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQC4aZTQ9cWladzlLZeFmC2bFLdMBFU3CXUksabuKK5QAgIhAM6su%2BmRPCbMMEI6LEpMtpzbedQsUdguBEQ7m0tgZAyrKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAKmp%2B4a%2Br00EKGZ0q3APfsqaCYa2ogR%2B5d0ISxvVaqjEzZnyN3la%2B94vR62SOojLN0TUVqokErAKNjgArUIIbLIzl%2BHp5PepRGeUZt82zjwi%2FGpxUi5FMMdR6qEFmdTuEOwbFaWZjWSfNWPUY2xllK0MEZOuXnPz6c0iCABIaGJi0u8mKAIQNioHySGXNI36H%2BcB3Sq47IR5buhhpyw54RTGn4jrrWtpkrDFvkU%2F0K4C94423M1GqoKK9HMaC%2FppCE35c%2B4OEHgVk1zGautt6kU0LURX%2BBDnyv3iSrcmXYKLb6D9JjvUBa0hHs%2B9aCuu%2ByBTYDGcwijtVASAzCuUTRcvWUVGazbtNBu%2FMKJqS7fLmdpGJNxBIepfk2WDJkfTnLdjCJHQSZUHxTI3tvmPhXuE7bEqJspNKSBN8i6uEUTSpwH0MQXIwYw8hmeFTygyyYqYKP2PrVyW3%2FDVlDBM7yBNqgco%2FOm6nbARQRmLVtH29GQ91zID7K9uZwvxhT%2BF6cxkHQ1Fak4bmT4m1e%2B8dOlWjued%2F8FbXr4A6aQCP0yXPvZG9Rxvg01ZlystFMzzO%2F4WgDKDp5NZTXqYHUZGQ9%2FOC2aZI7586d7b73ezAKAg9Ba%2FiFHAgFFM52zak0AdjbL3tm3zY5fYoOzC6koHQBjqkAYkUkkN0s1op%2B6eKt9EF3aXMvkc7EXk%2FTXXoM3FGl7wOhO1KqS12jGBoik0uK%2BZPOlmNTP7nWZc8S039KjqKw%2FqziciD4zRGmaI7IO11eHYeNH5V22eKFAfeNBG528NeKJMFCu6yLLVk%2B0IDgR68XE6TfA90R7nqsaHpNyg1nGAZIc4UluhGdrVgeDiSHAqRliorugj3R2%2FNEvzUWOQr%2BBrUNEX3&X-Amz-Signature=971af302b0491405f036366a6a5b64e0d8c83efaadc358acbe5dff4b46fa310c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
