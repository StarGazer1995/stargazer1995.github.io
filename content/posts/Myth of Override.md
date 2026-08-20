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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCHGOCLX%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T003215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOgfQ9S3YL7XGB5xsDN7oo5orpysXvU5j7BYh9w3bcGAiB28rnGuOLWhZAg7Yw7l1kA79VNTCnBDpsYWygPCxmAlCqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6BBdZzBiG2VA20wWKtwDrb7gxsx2geSMbBGD%2FZ95wKHLuCCmmPQu8Zk6MQI4i5lJ1psV6uN3twk6L1%2FQfy6s%2Bc4eCX4RMTlKhqnPn%2BWIjIiOy62hyzFkMB%2BZKXAwDZvZiYOYgFI6ZlwHbe8aSMqzBR0xXdlruJg0stdxyPU900UHUgF2SbJkzTx9JkZHSHia4lmxrDp1eevCL2EhqwoTkUGGyG7A2v%2FwDBmqO2LlPLEuazn9z5nmlRzvABuR8Z8lm9hdlhO3cSugfJOH31tPe6fZwqZyl8s0hd4V0rhpWJYPsoBWN0%2BPtA0UZn9lFXBMI%2BuPorfUlGLxEqi%2BMdyfrq9O%2BA%2BkFQOBLGUAWA3q8IxJtoxNtLG7eLPSkR2JuqSuX5gGqMPjJMoFsKkCiHB2CIfHmXgMk3ufJetjgFCw7x%2FC5qBZ05GLT7sHwRVbdXiK%2BphGbdjA7bxhxVtDpQAlP3wG1jOP7MmFjqnnClwCyHBlGq7bCRXaTiwI633MaZgkzCjqcw%2B7rPs3QrdHVj%2F80azNVsnDMe%2FfsWS31L9GnDGLJtekF5k%2FazD85PLcpMnOLlICtxUu1gESPeE2b7TNNOg0Kt1WZ1PM%2Fj5eEwOWknbqj%2B1lc2e%2FLRJ6L7ZUb4P9Vr%2BWsVeQNm7j5ZAwwOuY1AY6pgETEtH8p9konXek4Af3L2sUKYIag2KRdGwkwAhx%2B7OEZ6CsqRD18B1X9vSlaZ0f2Sfo4vMMez84QRRWiUyu18RW5NTEiSGxdO7rHEcQIBMg%2BKCsPCuQ%2FsVEtvcCz5hpfXFj%2B4kqnq17in0G5QfK%2FrERFSChNyJj0exerhqxlcYWF1VWOqEenw%2FkmmX8BF0nykpNEHeROqi2H0%2Fm339KBHBew0%2F6Eh6y&X-Amz-Signature=148e64e2d639ffe357d9d3051b9d754e462593eb5f78d35bfd297c9f1dbb81b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCHGOCLX%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T003215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOgfQ9S3YL7XGB5xsDN7oo5orpysXvU5j7BYh9w3bcGAiB28rnGuOLWhZAg7Yw7l1kA79VNTCnBDpsYWygPCxmAlCqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6BBdZzBiG2VA20wWKtwDrb7gxsx2geSMbBGD%2FZ95wKHLuCCmmPQu8Zk6MQI4i5lJ1psV6uN3twk6L1%2FQfy6s%2Bc4eCX4RMTlKhqnPn%2BWIjIiOy62hyzFkMB%2BZKXAwDZvZiYOYgFI6ZlwHbe8aSMqzBR0xXdlruJg0stdxyPU900UHUgF2SbJkzTx9JkZHSHia4lmxrDp1eevCL2EhqwoTkUGGyG7A2v%2FwDBmqO2LlPLEuazn9z5nmlRzvABuR8Z8lm9hdlhO3cSugfJOH31tPe6fZwqZyl8s0hd4V0rhpWJYPsoBWN0%2BPtA0UZn9lFXBMI%2BuPorfUlGLxEqi%2BMdyfrq9O%2BA%2BkFQOBLGUAWA3q8IxJtoxNtLG7eLPSkR2JuqSuX5gGqMPjJMoFsKkCiHB2CIfHmXgMk3ufJetjgFCw7x%2FC5qBZ05GLT7sHwRVbdXiK%2BphGbdjA7bxhxVtDpQAlP3wG1jOP7MmFjqnnClwCyHBlGq7bCRXaTiwI633MaZgkzCjqcw%2B7rPs3QrdHVj%2F80azNVsnDMe%2FfsWS31L9GnDGLJtekF5k%2FazD85PLcpMnOLlICtxUu1gESPeE2b7TNNOg0Kt1WZ1PM%2Fj5eEwOWknbqj%2B1lc2e%2FLRJ6L7ZUb4P9Vr%2BWsVeQNm7j5ZAwwOuY1AY6pgETEtH8p9konXek4Af3L2sUKYIag2KRdGwkwAhx%2B7OEZ6CsqRD18B1X9vSlaZ0f2Sfo4vMMez84QRRWiUyu18RW5NTEiSGxdO7rHEcQIBMg%2BKCsPCuQ%2FsVEtvcCz5hpfXFj%2B4kqnq17in0G5QfK%2FrERFSChNyJj0exerhqxlcYWF1VWOqEenw%2FkmmX8BF0nykpNEHeROqi2H0%2Fm339KBHBew0%2F6Eh6y&X-Amz-Signature=713c5234e69e50e41eba846887a2aea044475c524d144032ea19100ddd8a3125&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
