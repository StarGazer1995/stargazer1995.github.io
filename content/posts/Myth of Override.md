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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRUZQHW%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T094305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC99oSFL%2F1vLCBHT%2F1GVcsN5rjLL2FUza7WEkJa7BrGXAIhAOZBAJoq9PNqH6E2y04L%2FQr2ZvaVK8%2BOql8P1bGNQ7rDKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5s%2FQTGohUa%2BkIA8Uq3AOb7PPfbke6ZyG65rRMGmPHPlEM1FXxhdBobhR9tUDd4MgIt6JM9vtwHmwief2qRCEk1uHegP8EZ0tOEqaRQVglIlCFH3I3EXpFW3j%2FDzjUbK6Qyy3SF9KLTKSA8vtqWkNL7ohVJF152fEwDojucoq0L0YK%2F%2FjLk2v7798RBxTPcB7431nz%2FrYdyf%2BOt8L%2BTsXTaf2ITKv3gTalBPKn01BIbpBQFyluRrb12ooBKhvGsxRw6sy3CdPIsnOh1nwb3LmC7mp5L2uuc%2BJyAEfgap31ApS3sjxesUuwY2X8a%2FS1FY2v5cOsBo4aavW%2Bb5PuUnwaByxQk8seHkfHSWaT32LF0wMPE3q0HJ%2Fa9393X4or%2FogurWA5ktBmoTRi45SvE30YnIzIzYIkpTMzldANo8wVs2SzG0X6S3OFfqbsYz5HEhs%2FnxkMcD1n5bR031W5KLpGUZEzRnF9xF%2BDP62i6ljD2IzRh61t5BU0fXwyZ%2Bk59DHgN9TsCcIKh8hwF4jCzLZ7hOP68EzlOWNPduJkFbzxsb5zICPZKbUBrNjpPJOzxgNo%2FIkg26QzsVYNglZ6iyfp0Sf6Zqpi7DPWKkeKHN9Rznqzn3B7pNhZhuvIbs2DYY85KeYePwlaKf8lMzCwqPLSBjqkAWuEtRgvNGFuqKlC3a3nA64iKCAvY6HuTl4u3B2MgQqxf%2FHwvujQI0ubdqLeFmVNtTemAYFMp%2BuCB9yW67RqttKONH8b9iRcFe6VZl6QeJAZ7HWHhwIcy6jwOIh4ryrBQcK%2B7HrkK99DMtJ8zwwhudPY0xYvMxXgEaBJVeLVufL3OD%2BqqcIo3P2lM%2FZOPuZAdGHYwyLNxYpr4pkSiB9TvASBf5f9&X-Amz-Signature=6119550bf1eb4ec187e6297bae7405a627f328db701d5de4c175c07a20a6cca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPRUZQHW%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T094305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC99oSFL%2F1vLCBHT%2F1GVcsN5rjLL2FUza7WEkJa7BrGXAIhAOZBAJoq9PNqH6E2y04L%2FQr2ZvaVK8%2BOql8P1bGNQ7rDKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5s%2FQTGohUa%2BkIA8Uq3AOb7PPfbke6ZyG65rRMGmPHPlEM1FXxhdBobhR9tUDd4MgIt6JM9vtwHmwief2qRCEk1uHegP8EZ0tOEqaRQVglIlCFH3I3EXpFW3j%2FDzjUbK6Qyy3SF9KLTKSA8vtqWkNL7ohVJF152fEwDojucoq0L0YK%2F%2FjLk2v7798RBxTPcB7431nz%2FrYdyf%2BOt8L%2BTsXTaf2ITKv3gTalBPKn01BIbpBQFyluRrb12ooBKhvGsxRw6sy3CdPIsnOh1nwb3LmC7mp5L2uuc%2BJyAEfgap31ApS3sjxesUuwY2X8a%2FS1FY2v5cOsBo4aavW%2Bb5PuUnwaByxQk8seHkfHSWaT32LF0wMPE3q0HJ%2Fa9393X4or%2FogurWA5ktBmoTRi45SvE30YnIzIzYIkpTMzldANo8wVs2SzG0X6S3OFfqbsYz5HEhs%2FnxkMcD1n5bR031W5KLpGUZEzRnF9xF%2BDP62i6ljD2IzRh61t5BU0fXwyZ%2Bk59DHgN9TsCcIKh8hwF4jCzLZ7hOP68EzlOWNPduJkFbzxsb5zICPZKbUBrNjpPJOzxgNo%2FIkg26QzsVYNglZ6iyfp0Sf6Zqpi7DPWKkeKHN9Rznqzn3B7pNhZhuvIbs2DYY85KeYePwlaKf8lMzCwqPLSBjqkAWuEtRgvNGFuqKlC3a3nA64iKCAvY6HuTl4u3B2MgQqxf%2FHwvujQI0ubdqLeFmVNtTemAYFMp%2BuCB9yW67RqttKONH8b9iRcFe6VZl6QeJAZ7HWHhwIcy6jwOIh4ryrBQcK%2B7HrkK99DMtJ8zwwhudPY0xYvMxXgEaBJVeLVufL3OD%2BqqcIo3P2lM%2FZOPuZAdGHYwyLNxYpr4pkSiB9TvASBf5f9&X-Amz-Signature=35c094b384b844d899a9d2d7642af482c31a7a757ec8b13941ee108d6cd61a46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
