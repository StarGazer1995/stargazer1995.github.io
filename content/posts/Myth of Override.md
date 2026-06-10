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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664235EX3N%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T113802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIH89cByWZDZHlKfWmoG2NKy4hepMTyy%2FnhB4%2Bs7MEJsUAiBReQ6vRZ2cAhmb%2FY3X16KBZtR3Ohy61tjg0ndVXJoKVyqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsw0K3ZUwEpdC6Yx9KtwDe3UQ10VLJ3VFugBVor5Vu7A%2BVcH%2FdoaGyS%2FW1XIPgJVXwOA54JgDBPQHitrXPcKnkd%2FpjZ%2FUb1dWUVhyIZ9uFXFAlirNzZRLzq5HAhOTK8P%2B7zWOAawkqQBwUs22m9ch6dNiSVqvoCGfAk319iQQoragejY%2B7Aqv6u3DtrI5SrM%2BkMY%2BO0tUyi7oai%2BSlmbWiHTHK5o6JcznrEzzEpSXeXI%2F7MnF6qOZjLr7hdbbjvIwoZh7iFr3yZQVq9y7iA60g1jLcYOY2KcErIDhr0ekOiLSuXUVMtGhJjVVOGtYzWgAdxKi%2FokZ6Xp5jmBdC1LznFXNLNc2OXYiTdvuqwt8YQ9ATN2I%2FVbZzkMIakM6OQlgJP9kgd7HYHTiKdZFua6iD4YfkfNiiYu9gvG8p3FMyvr3%2Ftf71ZpZUObMt8gPpEkLjRao2JmHxCsaIoaphRoa1qLPBzm7a4xo2ZwO9xPBewsCQD58fI2rFNDzeFFrnMA6BveCwni2rMtCiUlg9GpTBLNWgE3lYRM9oz%2FW%2BtPVCv%2BlqVd%2BzF%2Bm8EgsvSfSgB4EiOj0yA8oy54TWg3NhjUnBjjFImzwyY%2BzeW8%2Bytxxh3RcQou5ROP02m%2Fcu2IU5EjAwIMdPkv3fYp1FOQwhI2l0QY6pgG7qQOYYeU%2FIhoHPMeSxbVMcfeMQhq1R4rSlQm99BaNvy47lPVTsSBniwK2%2FtExM5hhNTchuoZCdeArji50RxOgQRN5RXjz259k3HQkw3bAgh%2FnZFoitC1wHdaOu5fZIqqopshAprrcfeSmvrYYfBVYsTpqRYHDkuhSU2BwMm9d88xT9B7T4dN1x3kLro%2F0ZzAWmgnNerR%2FS%2FIimx6ztmUZi2UzAV0n&X-Amz-Signature=b0b8a923e15835de9c769e43dbc5c501efd8286673ac7086682abc1e5bbbe2ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664235EX3N%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T113802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIH89cByWZDZHlKfWmoG2NKy4hepMTyy%2FnhB4%2Bs7MEJsUAiBReQ6vRZ2cAhmb%2FY3X16KBZtR3Ohy61tjg0ndVXJoKVyqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsw0K3ZUwEpdC6Yx9KtwDe3UQ10VLJ3VFugBVor5Vu7A%2BVcH%2FdoaGyS%2FW1XIPgJVXwOA54JgDBPQHitrXPcKnkd%2FpjZ%2FUb1dWUVhyIZ9uFXFAlirNzZRLzq5HAhOTK8P%2B7zWOAawkqQBwUs22m9ch6dNiSVqvoCGfAk319iQQoragejY%2B7Aqv6u3DtrI5SrM%2BkMY%2BO0tUyi7oai%2BSlmbWiHTHK5o6JcznrEzzEpSXeXI%2F7MnF6qOZjLr7hdbbjvIwoZh7iFr3yZQVq9y7iA60g1jLcYOY2KcErIDhr0ekOiLSuXUVMtGhJjVVOGtYzWgAdxKi%2FokZ6Xp5jmBdC1LznFXNLNc2OXYiTdvuqwt8YQ9ATN2I%2FVbZzkMIakM6OQlgJP9kgd7HYHTiKdZFua6iD4YfkfNiiYu9gvG8p3FMyvr3%2Ftf71ZpZUObMt8gPpEkLjRao2JmHxCsaIoaphRoa1qLPBzm7a4xo2ZwO9xPBewsCQD58fI2rFNDzeFFrnMA6BveCwni2rMtCiUlg9GpTBLNWgE3lYRM9oz%2FW%2BtPVCv%2BlqVd%2BzF%2Bm8EgsvSfSgB4EiOj0yA8oy54TWg3NhjUnBjjFImzwyY%2BzeW8%2Bytxxh3RcQou5ROP02m%2Fcu2IU5EjAwIMdPkv3fYp1FOQwhI2l0QY6pgG7qQOYYeU%2FIhoHPMeSxbVMcfeMQhq1R4rSlQm99BaNvy47lPVTsSBniwK2%2FtExM5hhNTchuoZCdeArji50RxOgQRN5RXjz259k3HQkw3bAgh%2FnZFoitC1wHdaOu5fZIqqopshAprrcfeSmvrYYfBVYsTpqRYHDkuhSU2BwMm9d88xT9B7T4dN1x3kLro%2F0ZzAWmgnNerR%2FS%2FIimx6ztmUZi2UzAV0n&X-Amz-Signature=e38df38d4705a3bff7259f43c64861149683750db13710e4af267dc6bb9577d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
