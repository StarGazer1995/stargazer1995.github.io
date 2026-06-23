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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD5MWQUR%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T174502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJHMEUCIH%2Fs9jKAfM%2Fkq83vP0Yw1c9Lg7V2r6wUVDQgHTxEluKCAiEA3o7PprHIsqNPL%2Bcv%2BAPoZo1S%2FHLJ4QOV9G8KhgIh8ssq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPkft7pdVxz4RucvUSrcA0TCutxrDejUTv0weMM0b9Hq74YXI1uSQlmhZlWCbkSrs4CY9Jv5%2Friy7yeykIMxUmWv4RyDS7%2BGhLF%2BSB0qVQRCb3Vss8mROtPCsamCPjhSodPZYSv7lJex9V%2FPJbmYVbIhqmMb4JKHw2xnbsNbw0QcTryjnFQ4nzIG9yVOosHaE3lyrx5KmypVQ%2BFOZf8HtGG%2Fw0Ud7WSXCmFOcRev3WOORZvJsUx6KoB6mFqoNKo4R9kgKz5mvvA8QU5i3IbXuCBREMCJLo1gUXbxPbqisljd5JvespS8cknmgL22%2FUeZlStm9tOkYz%2Fa7peQRMhOAdWOQNhbeShUReU26WXJ%2FNI9ETJeUAl%2Fr2y%2FKQM%2B8bYrS9HgGx2bWI4u%2FHXOh%2BczPT0SEW8VEVCwAN9QVhfahtUcEQzI7NcXIR%2Bou5SyT8idugFM18yNP00huAAjzrRwYqvxxZXShMVmLXpZKbuMU1gbr1U3dmOOhio%2F6MYhQY5x5r8%2FUc2vsOyYT1My4lHoAl63xqLrEYRTOs5EsQFghn49rW4a9BXeqbDu0TVvlQKlXgYxzJNY%2FFRd4kgm%2FFiRz4aHXIkOaBxnZSmnuvfjDo82f8WE5okXwcD7PJWxv6DU%2BXGYpZPkQebwIYffMNCB69EGOqUBK8hkNy1ayMld8aYoLF%2BLz1dJ%2Fo5ueDGy1l%2BSoajbtfN79xeu2dZo%2FwqeFjpSvEPxXwT5gToGGy9MQGLzXKKZxSOBhi5LUD0RL5p8msguz4G5UjFyVKd27VNF%2Fm%2FjyLJg56KtT06B8YQ%2FOKGT6RU99JTdQQGFN%2Bm28pQS6YxPRweNKJvdztk8%2FPtqA5joVD27PkyxIvH4mf6ts0csvRPPxq7O%2BTiY&X-Amz-Signature=6b9a6723d1c0388ca9d0192ab92440dab636430d4d9df62ed58338ff1a381ac1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD5MWQUR%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T174502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJHMEUCIH%2Fs9jKAfM%2Fkq83vP0Yw1c9Lg7V2r6wUVDQgHTxEluKCAiEA3o7PprHIsqNPL%2Bcv%2BAPoZo1S%2FHLJ4QOV9G8KhgIh8ssq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPkft7pdVxz4RucvUSrcA0TCutxrDejUTv0weMM0b9Hq74YXI1uSQlmhZlWCbkSrs4CY9Jv5%2Friy7yeykIMxUmWv4RyDS7%2BGhLF%2BSB0qVQRCb3Vss8mROtPCsamCPjhSodPZYSv7lJex9V%2FPJbmYVbIhqmMb4JKHw2xnbsNbw0QcTryjnFQ4nzIG9yVOosHaE3lyrx5KmypVQ%2BFOZf8HtGG%2Fw0Ud7WSXCmFOcRev3WOORZvJsUx6KoB6mFqoNKo4R9kgKz5mvvA8QU5i3IbXuCBREMCJLo1gUXbxPbqisljd5JvespS8cknmgL22%2FUeZlStm9tOkYz%2Fa7peQRMhOAdWOQNhbeShUReU26WXJ%2FNI9ETJeUAl%2Fr2y%2FKQM%2B8bYrS9HgGx2bWI4u%2FHXOh%2BczPT0SEW8VEVCwAN9QVhfahtUcEQzI7NcXIR%2Bou5SyT8idugFM18yNP00huAAjzrRwYqvxxZXShMVmLXpZKbuMU1gbr1U3dmOOhio%2F6MYhQY5x5r8%2FUc2vsOyYT1My4lHoAl63xqLrEYRTOs5EsQFghn49rW4a9BXeqbDu0TVvlQKlXgYxzJNY%2FFRd4kgm%2FFiRz4aHXIkOaBxnZSmnuvfjDo82f8WE5okXwcD7PJWxv6DU%2BXGYpZPkQebwIYffMNCB69EGOqUBK8hkNy1ayMld8aYoLF%2BLz1dJ%2Fo5ueDGy1l%2BSoajbtfN79xeu2dZo%2FwqeFjpSvEPxXwT5gToGGy9MQGLzXKKZxSOBhi5LUD0RL5p8msguz4G5UjFyVKd27VNF%2Fm%2FjyLJg56KtT06B8YQ%2FOKGT6RU99JTdQQGFN%2Bm28pQS6YxPRweNKJvdztk8%2FPtqA5joVD27PkyxIvH4mf6ts0csvRPPxq7O%2BTiY&X-Amz-Signature=d5292710a00e75957c9b88fa8ba314b63b73f1be2cfb501fe65f251cb542b9fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
