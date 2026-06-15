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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5RKQOI6%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T023200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGEon04%2FVV%2FfDxJOMeL8mNstgNEZ7Rk%2BxIOhwpFwGNOEAiEA47X%2FPxCHLl35COycgScAKdXrG0elNHRCr5h51V6ktgUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDN%2FlHTjLLpuwPAcMyCrcA2LaIe0%2BSoHguHeKND9Rol3fRSf75LNNY2y0Jg3utOSWLdzq16tgNfGqjN27ic4bd3eaDmzfatY7KlK4RLwCIRrWF%2BLzhkUvAnPgqZPvO2fBJNcuDHm%2BKwpCtay%2BUElcsHFaDE6%2FZYhM8F2N%2FnJr%2BSom91pN6Q1nEiwQ0Gz%2FE570P9zqkarC6TInVzX%2BA6NpC73%2Fgym8GvdQ0TWIKQ8hKqj2zPj2X5O5c63k5i4Jvql36oC6CTqXGbra0yUHB7bZ2bjjkqzb2Nafp7wgkMuTTVfCtOcKLHthoamdDllnRTYZ4hNqXhZJNrUmoA7758NBPelrXrhtqU0Zv2yIFrzhwO3TI9lK5WFOlikR8J4BIRWmb3cAaB4tl4ki9RQWSlr9Q85ocERUlOLNAi4qSMsEUzYOvIsvM%2FE%2BGVgmIEUUqD6WPA6PZEz1B063owetgVyhejllwiM81PVAD7h8%2BdbN4VJTbaodcvzLAD66Y38NJZiKej%2BIsSPTwb5Ou2%2BbF0yJpDhTssc20HWTdvmDTSJRNXfw12v1ZhjJmiJHFws7aJolZiDGWX4jHeUjmC6Y6u5AALVNvhCXukZSqbjwywGzh3HFrujkbXB75A%2BCn%2BB4cGUmw85KeuhFUs3yXfW1MN61vdEGOqUBcqRJogpTKo8kEgs4927LY%2FxAIyCh1rDcvV3F4Nu%2FuvSd2dF5WBgOjZ7xAdTdIsoi%2BYEPZ%2BDb85hcjVK0fNtrb3zYlqCLxgOZ569vAI6S%2BOVU9s%2FMuDRf%2BHu0JSbmMucAk%2BmKXw9GDWDRHFYpV3d1ssqxn7nVgr7w5cwzEZ%2Fx6q2aRSVNJi%2BZNlrRpzxxBhkeLrdG1MAcd1yNyE5d9lJg15m2kSbY&X-Amz-Signature=e9de7fe3c12ae8a63cccbe998015f9825c551e2ccfadbf73ed962cafa6c2514e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5RKQOI6%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T023200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGEon04%2FVV%2FfDxJOMeL8mNstgNEZ7Rk%2BxIOhwpFwGNOEAiEA47X%2FPxCHLl35COycgScAKdXrG0elNHRCr5h51V6ktgUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDN%2FlHTjLLpuwPAcMyCrcA2LaIe0%2BSoHguHeKND9Rol3fRSf75LNNY2y0Jg3utOSWLdzq16tgNfGqjN27ic4bd3eaDmzfatY7KlK4RLwCIRrWF%2BLzhkUvAnPgqZPvO2fBJNcuDHm%2BKwpCtay%2BUElcsHFaDE6%2FZYhM8F2N%2FnJr%2BSom91pN6Q1nEiwQ0Gz%2FE570P9zqkarC6TInVzX%2BA6NpC73%2Fgym8GvdQ0TWIKQ8hKqj2zPj2X5O5c63k5i4Jvql36oC6CTqXGbra0yUHB7bZ2bjjkqzb2Nafp7wgkMuTTVfCtOcKLHthoamdDllnRTYZ4hNqXhZJNrUmoA7758NBPelrXrhtqU0Zv2yIFrzhwO3TI9lK5WFOlikR8J4BIRWmb3cAaB4tl4ki9RQWSlr9Q85ocERUlOLNAi4qSMsEUzYOvIsvM%2FE%2BGVgmIEUUqD6WPA6PZEz1B063owetgVyhejllwiM81PVAD7h8%2BdbN4VJTbaodcvzLAD66Y38NJZiKej%2BIsSPTwb5Ou2%2BbF0yJpDhTssc20HWTdvmDTSJRNXfw12v1ZhjJmiJHFws7aJolZiDGWX4jHeUjmC6Y6u5AALVNvhCXukZSqbjwywGzh3HFrujkbXB75A%2BCn%2BB4cGUmw85KeuhFUs3yXfW1MN61vdEGOqUBcqRJogpTKo8kEgs4927LY%2FxAIyCh1rDcvV3F4Nu%2FuvSd2dF5WBgOjZ7xAdTdIsoi%2BYEPZ%2BDb85hcjVK0fNtrb3zYlqCLxgOZ569vAI6S%2BOVU9s%2FMuDRf%2BHu0JSbmMucAk%2BmKXw9GDWDRHFYpV3d1ssqxn7nVgr7w5cwzEZ%2Fx6q2aRSVNJi%2BZNlrRpzxxBhkeLrdG1MAcd1yNyE5d9lJg15m2kSbY&X-Amz-Signature=175f18d9588d4401246ed607ff3c8c239115bb243a5989ad21e89b1802fae4d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
