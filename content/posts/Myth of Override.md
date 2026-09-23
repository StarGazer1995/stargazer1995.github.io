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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647QBA34S%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T143102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxOOPKJJgiGlCpzQvwPHYjioqV4hxouXQi9vKboUKlrgIhAMrO5mcdUkCpaQlH5N7qkyUtK9plyY3jRdpa4usWcnK8KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMw3rk3aUohYklrHsq3ANe7jUgHHtL0SwPgVzRZ6wG%2BG11QlBlzI05e%2FyQ8g2BVJynLsNtg5fUkiuzkLJrBE4v7cSriW6p%2FPGL1ghUMFQfJ8AI0eYK%2FSto%2Bh1Sa0xPIblLljfJ0AJJg7mzSfk6UYlwnl1lv2Kj%2F0y%2BrcZH6G%2BtaZ2SrDQnRZ0nBV%2F3VQ%2B4%2B7kktvkAe2lJKfE1Usa60vlbJkVmgqmb2yQfsN8w3%2Bqa7J6CYV%2FpfuYuCaiF%2BF5iTmmPx1EjbAYl5nYCp%2BwcWGhmcDW2LwMQ%2FcLi%2B17fPNhwtH5jRnPh2jqgzRjZ08ZeaAeyVEyAVpQSURHzaVuyMpGPlm%2BmU2ZMIEMMsHsSinwv4uLp%2BYUx2qDSFGevKW2n5K5UpRwdvp%2BQWW%2FoUnlGnKZW%2Fs02nwQdPil7SpARc8SV6augHL4k4DI7jrZHMrHVefHvD64g%2F82GsSrJBDhYD18K4V29%2BkWdm8dXUdfdvrsbI3Yk4%2BddUozjMZ1NxmdJAT5Nwdg8%2Fj2qHXUv%2FEfTuDTUzHOP5YNZ5JU6Zda3Rk2D5%2Bb4BczNMIXRxn5cYhtlKjBNqjTLsS2YJjmDbe3rg4zcnlJCIXw28GgKv1d1gchNDE903j4vtxS9rv2QQ%2B%2FH1j0Hmx%2Bgfb4uNy26PDCWhc%2FVBjqkAZ7Yts%2Bw8v8IgCjrLNkne1h3TGL3mGdXeM765LLjVW7zGzHzfBblzId8XGf1cFixFbBIPs7W59Q823O1dEDWRXpohIcMZMM5wf%2FsYgwSHWdT0hr4p%2BEq7F49byAlkGg6mZRVcvj8YqBmUAjvvUWV%2Bqa1SGz%2FS%2BV1lKJ%2Bi%2FNwW6844GqWMw7rL9L9i8ySGYfX0aJLn5ZXFoWFrDXRxbexNheq8b3k&X-Amz-Signature=e8073ed6cdefd1e8486d72ef2454c3dc244823d909b077194d9fc0d3e894c3ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647QBA34S%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T143101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxOOPKJJgiGlCpzQvwPHYjioqV4hxouXQi9vKboUKlrgIhAMrO5mcdUkCpaQlH5N7qkyUtK9plyY3jRdpa4usWcnK8KogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMw3rk3aUohYklrHsq3ANe7jUgHHtL0SwPgVzRZ6wG%2BG11QlBlzI05e%2FyQ8g2BVJynLsNtg5fUkiuzkLJrBE4v7cSriW6p%2FPGL1ghUMFQfJ8AI0eYK%2FSto%2Bh1Sa0xPIblLljfJ0AJJg7mzSfk6UYlwnl1lv2Kj%2F0y%2BrcZH6G%2BtaZ2SrDQnRZ0nBV%2F3VQ%2B4%2B7kktvkAe2lJKfE1Usa60vlbJkVmgqmb2yQfsN8w3%2Bqa7J6CYV%2FpfuYuCaiF%2BF5iTmmPx1EjbAYl5nYCp%2BwcWGhmcDW2LwMQ%2FcLi%2B17fPNhwtH5jRnPh2jqgzRjZ08ZeaAeyVEyAVpQSURHzaVuyMpGPlm%2BmU2ZMIEMMsHsSinwv4uLp%2BYUx2qDSFGevKW2n5K5UpRwdvp%2BQWW%2FoUnlGnKZW%2Fs02nwQdPil7SpARc8SV6augHL4k4DI7jrZHMrHVefHvD64g%2F82GsSrJBDhYD18K4V29%2BkWdm8dXUdfdvrsbI3Yk4%2BddUozjMZ1NxmdJAT5Nwdg8%2Fj2qHXUv%2FEfTuDTUzHOP5YNZ5JU6Zda3Rk2D5%2Bb4BczNMIXRxn5cYhtlKjBNqjTLsS2YJjmDbe3rg4zcnlJCIXw28GgKv1d1gchNDE903j4vtxS9rv2QQ%2B%2FH1j0Hmx%2Bgfb4uNy26PDCWhc%2FVBjqkAZ7Yts%2Bw8v8IgCjrLNkne1h3TGL3mGdXeM765LLjVW7zGzHzfBblzId8XGf1cFixFbBIPs7W59Q823O1dEDWRXpohIcMZMM5wf%2FsYgwSHWdT0hr4p%2BEq7F49byAlkGg6mZRVcvj8YqBmUAjvvUWV%2Bqa1SGz%2FS%2BV1lKJ%2Bi%2FNwW6844GqWMw7rL9L9i8ySGYfX0aJLn5ZXFoWFrDXRxbexNheq8b3k&X-Amz-Signature=379afb1221eafab40955e1bd4863fa0d1a2c3fb0f5d0d7187bb3918cf5812c52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
