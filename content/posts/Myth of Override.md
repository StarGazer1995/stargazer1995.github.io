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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644LGSMYW%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T015648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoCGO0YmaDOMoNWbReuhCLa3Dt4mzQ12pDBecykKoLhAiEAmXfWSd7ysM%2F2X1QLUwuF1WvMLfZSeLuwIqZKJiw1iOQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDIewGqnysjI3%2BPXPLCrcA%2FDGBUrIYtyel4dUOIY4pmG1I2zWi1ljuo1Z%2Flwp%2BoBkPY5%2F5TdCsWQQymL2%2F5vRLjxZqfWDhUr62wRM6n2MEMHNW9ROJu2fkWsKA4zdvpqGjQe91dtS9ZVdLkydDrbwJ64SXd7XQOSQ%2BMjbYqmOj7%2FJ9kmPL52jBKCsWM72I7BtkOsQRPEabYPomUOY56SGBTH8ZjplU6HHSwsqjOTbOXv5CkQLM0t0XflpkBgpP1SqZ0U3nCdxEzuzks%2Beo%2FFrzlFpi4AnK2s62fOeWYWrjeew9z7aE8UyOR9jx0CaMLlLkT39t4DUnxJjsTz4HlO9h3U8n0ev%2BI0oQrCsLVb39gPg%2BO%2BsFgquAnxgu5OF3tR%2FLs6j7M2%2BsaY6j1HpeYy2LLDOP%2Bo379arG7ygHzNZ1vV8UbanWLwipGUfyIQFedoGFcog2qTphwfjBEZ6YhBAJW%2Fs2BNn%2B2NznAmhSuGOqML0OT%2BR0XQ6p9b2xTgAru2nBL1OSsWu2aUWHbYVU%2BQgfDthiwD%2Ffnr5OYmBqlIJOK4%2F3xzZT8rZ%2FdwTfwUihM4IPSQ8gyUkrpDj0Yyb2fXM0dfA0xQefyHU6v6jAhy2XU2LtCxrJBr%2FQUDufD7YSSf7P098kkHgPn8b%2BhxaMKKOrNIGOqUBNwoXiuuSpeKjk0y00k8NZHtHJuOhaRtURWnVWxRmwfaQpf3YEqHJ5DY51xwC23wdxUruG%2Bi8gX1%2FMzb4sTjn%2BR8F6AXdPeBusGPzAawDO7fyRtRPQVMyDKyJP0zgzrwvaH2UOPPULC9si7bBx3pPCxRuyTY%2B1wU287%2BjlTDnX5ORiezFuv61YLn95Sn5%2B8Q6vk46GPolRcmHf5i1faKawEkCTr6y&X-Amz-Signature=cc6ef5e3b8ce0fba04c4fbeb729b673242ba44870b2375fac1d7e41d4ce299cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644LGSMYW%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T015648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoCGO0YmaDOMoNWbReuhCLa3Dt4mzQ12pDBecykKoLhAiEAmXfWSd7ysM%2F2X1QLUwuF1WvMLfZSeLuwIqZKJiw1iOQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDIewGqnysjI3%2BPXPLCrcA%2FDGBUrIYtyel4dUOIY4pmG1I2zWi1ljuo1Z%2Flwp%2BoBkPY5%2F5TdCsWQQymL2%2F5vRLjxZqfWDhUr62wRM6n2MEMHNW9ROJu2fkWsKA4zdvpqGjQe91dtS9ZVdLkydDrbwJ64SXd7XQOSQ%2BMjbYqmOj7%2FJ9kmPL52jBKCsWM72I7BtkOsQRPEabYPomUOY56SGBTH8ZjplU6HHSwsqjOTbOXv5CkQLM0t0XflpkBgpP1SqZ0U3nCdxEzuzks%2Beo%2FFrzlFpi4AnK2s62fOeWYWrjeew9z7aE8UyOR9jx0CaMLlLkT39t4DUnxJjsTz4HlO9h3U8n0ev%2BI0oQrCsLVb39gPg%2BO%2BsFgquAnxgu5OF3tR%2FLs6j7M2%2BsaY6j1HpeYy2LLDOP%2Bo379arG7ygHzNZ1vV8UbanWLwipGUfyIQFedoGFcog2qTphwfjBEZ6YhBAJW%2Fs2BNn%2B2NznAmhSuGOqML0OT%2BR0XQ6p9b2xTgAru2nBL1OSsWu2aUWHbYVU%2BQgfDthiwD%2Ffnr5OYmBqlIJOK4%2F3xzZT8rZ%2FdwTfwUihM4IPSQ8gyUkrpDj0Yyb2fXM0dfA0xQefyHU6v6jAhy2XU2LtCxrJBr%2FQUDufD7YSSf7P098kkHgPn8b%2BhxaMKKOrNIGOqUBNwoXiuuSpeKjk0y00k8NZHtHJuOhaRtURWnVWxRmwfaQpf3YEqHJ5DY51xwC23wdxUruG%2Bi8gX1%2FMzb4sTjn%2BR8F6AXdPeBusGPzAawDO7fyRtRPQVMyDKyJP0zgzrwvaH2UOPPULC9si7bBx3pPCxRuyTY%2B1wU287%2BjlTDnX5ORiezFuv61YLn95Sn5%2B8Q6vk46GPolRcmHf5i1faKawEkCTr6y&X-Amz-Signature=04c0935829b3d10ce303b6c621b9059abcc042a7ceda8571bbaa91fd2cf7c7ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
