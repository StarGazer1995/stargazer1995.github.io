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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RDI44CZ%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T102122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBtdXuOSxmAjSNr%2B1BiBWwoDAprRzhvnpL7TtzWjqt%2BEAiBnBMdcNDuksXNtWR49ZqDhwaS52c%2FohXVkOxIVHQhqGCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMdeXCLGVltkrcj1WaKtwDLdRJdNzGeZd1i4d2NZcxJrWKfRF%2F2Bf%2FlRSTJXTNJTSLv8JjXyyUEvK2DOplN1ooO8cdn0SdY5gQdbmzLQYFdRTsP45eUNfDHgEm2wUcAre4qW%2FzWO7XHImFjumWQs5wAVMqSkqn2VXqyEw%2BR3deIbQtW0n8%2F%2FRopDQgP6cEYiikhVUOOXJncTWRqikcM5wztog6vIPkv8iZqwe8uZkgw%2FCAhL%2B3B%2Bt4WBaj0qN3UTeJakRAGuRRkUIWD%2BkxvnZffVaJW0oKm9cfxYPYXymHz3CkSnMSXXLGTqjTZGbUcfYyzjPHUQH22GVappXj%2BCbHlv0rI5l1M3CPnfZeh%2B1E3eMM4xLB%2F9Fc5havY21p6Colw8se84TvmErGe54UR%2FwO9JOoOxNVllmhVZWglL8TH14OJjP6sXiFsdod0Td4jzxyTPdNyW%2FCJ9BvcRx3s0wSpb3JdvUgZNtA%2BuwmFgX9T9izDfQ8NapfnEmjnI%2BUDrnAVKYjRIc8lDD%2F4FCldzWvQ1Mh3kyYXuuyDkwb4HHhwkuMv7cqDPRktR3Uy2DeY3rO5hn8wkKpeXpcHZ4yFNGxq9aHr%2F8zaAGGJ%2FPrUZrL%2BUhiegMssdYXqT19pfj0NZkaO0nlWBLv2xeYqRIwz8e00QY6pgGVF%2BppPRqLdwJ%2FflyG5R4XUqz2cr2mQ9pi6nhfnckpwOOlUsM7WddbYPW9BdcnXFEAnR3jfaj%2BEPJgE7Hx%2FJ9T11gyoxX0%2F68VYhifudoSWZ0dFGG9PjoCs9b%2F7TtRGwXrb9BiOBst9I0Y1MGH8r6tqccwRX8KZbvI8cZfnjVPirRwSLAHuVxVwaE1KNvDE88dsGr46hpu4Tr9uzCPWgOvnhiX1OD7&X-Amz-Signature=30b4564a434b8d70f08c8ac1a4d7e080a7f9910911eee22020324e767c3ada6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RDI44CZ%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T102122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBtdXuOSxmAjSNr%2B1BiBWwoDAprRzhvnpL7TtzWjqt%2BEAiBnBMdcNDuksXNtWR49ZqDhwaS52c%2FohXVkOxIVHQhqGCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMdeXCLGVltkrcj1WaKtwDLdRJdNzGeZd1i4d2NZcxJrWKfRF%2F2Bf%2FlRSTJXTNJTSLv8JjXyyUEvK2DOplN1ooO8cdn0SdY5gQdbmzLQYFdRTsP45eUNfDHgEm2wUcAre4qW%2FzWO7XHImFjumWQs5wAVMqSkqn2VXqyEw%2BR3deIbQtW0n8%2F%2FRopDQgP6cEYiikhVUOOXJncTWRqikcM5wztog6vIPkv8iZqwe8uZkgw%2FCAhL%2B3B%2Bt4WBaj0qN3UTeJakRAGuRRkUIWD%2BkxvnZffVaJW0oKm9cfxYPYXymHz3CkSnMSXXLGTqjTZGbUcfYyzjPHUQH22GVappXj%2BCbHlv0rI5l1M3CPnfZeh%2B1E3eMM4xLB%2F9Fc5havY21p6Colw8se84TvmErGe54UR%2FwO9JOoOxNVllmhVZWglL8TH14OJjP6sXiFsdod0Td4jzxyTPdNyW%2FCJ9BvcRx3s0wSpb3JdvUgZNtA%2BuwmFgX9T9izDfQ8NapfnEmjnI%2BUDrnAVKYjRIc8lDD%2F4FCldzWvQ1Mh3kyYXuuyDkwb4HHhwkuMv7cqDPRktR3Uy2DeY3rO5hn8wkKpeXpcHZ4yFNGxq9aHr%2F8zaAGGJ%2FPrUZrL%2BUhiegMssdYXqT19pfj0NZkaO0nlWBLv2xeYqRIwz8e00QY6pgGVF%2BppPRqLdwJ%2FflyG5R4XUqz2cr2mQ9pi6nhfnckpwOOlUsM7WddbYPW9BdcnXFEAnR3jfaj%2BEPJgE7Hx%2FJ9T11gyoxX0%2F68VYhifudoSWZ0dFGG9PjoCs9b%2F7TtRGwXrb9BiOBst9I0Y1MGH8r6tqccwRX8KZbvI8cZfnjVPirRwSLAHuVxVwaE1KNvDE88dsGr46hpu4Tr9uzCPWgOvnhiX1OD7&X-Amz-Signature=388bcf67fe8fa588adfa39a63e238963e440f149edcff256aa3895c4cd30b16c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
