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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RROFLH75%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T020954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvFBphdrzLitOgLwPbnqoAQ6UY7VMcsJrL%2Be2XzDJNwAiBO%2FCFl2l2jTgKphLzTxmmhTCKa8pRcYgXdCk1jA1cT6SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl07IfpJNpv%2FqX%2FXdKtwDBTggvze9gPv0jnHQuMY5pHV7RXpiAulO0MfniQtna%2FEsDvChenLWlG1gZ7SrmHJ%2BibY9GGXIkbi%2BxZfAZce2J7zJk0kwk8b%2F0ZpJUXe0n3e0eYWHeC%2BUWiUMYTEUQtO4Lapa4ksp%2BCO1u5fHLKikZFNtfO%2FWKqZZHqgKMF94xXlD7NqcDoYhvHe1vW%2Bu0K2oBySs4j3zEVA4hA8NSPqBb%2F4vP3p8ehOMcQii8uTnVCJKz1hx9V7UDA5%2FWnmtLC9sRWZPndEFgFDnU672FPTgk86EX93m%2BNJLCSO3LPMEHndox0LyMno4f%2FK9YR9atQ3xHxo3gGESMyIM33ZDSk3HQjhGaDiq6gHhoqL%2FEFFCH22wRKhnvkxMD4OZJ%2BbqDj%2F2%2BGWRgrhToE8d6hRQZXtbxhAlGfOr%2B8gE5k3jrsCCJZU%2BnbbgiwYEWla0ihjb%2FaxCIZqDP4uHSwLQVDd4dCmdaDojAD7tYllCECiB8eQG78HEJplc0n1T8X0OogtOAIiMdtNTVDduspQWQF%2FzfWDrtMhRB1bOIkIVN81pfQLPulav2UPhoqEVwe7JykY1vQqzbltFi6%2BdnzDhKhG51uRp7TKn25FMQ5w3maqy8BMs005rUVxgWneeINnEZYww3saB0gY6pgHBSX0RpmL7QYhiLMRJzc95NxxdFZZRnY6J4y4t%2BrGro%2BciERsalYWMivw6x%2Fln%2FNB%2BXV%2F%2FVY86ukuLHEGeDi5ot1JUZGwTFOi19fXX9JxfNF2su8d5vdpRsf%2BFj0J%2FQy%2F1g%2Fnhxshr1T17Bc7A%2FhIOIMW6IkfGWy%2FSWK6TMlzpDplYuXGQ%2B9nHtM41SZTWY4Fcxgx5pB6pyLhJqIr92GbA1kalHIwi&X-Amz-Signature=6309d2578276bae28918aced27988c0c154540a92867d953f028f3abf53487ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RROFLH75%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T020954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvFBphdrzLitOgLwPbnqoAQ6UY7VMcsJrL%2Be2XzDJNwAiBO%2FCFl2l2jTgKphLzTxmmhTCKa8pRcYgXdCk1jA1cT6SqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl07IfpJNpv%2FqX%2FXdKtwDBTggvze9gPv0jnHQuMY5pHV7RXpiAulO0MfniQtna%2FEsDvChenLWlG1gZ7SrmHJ%2BibY9GGXIkbi%2BxZfAZce2J7zJk0kwk8b%2F0ZpJUXe0n3e0eYWHeC%2BUWiUMYTEUQtO4Lapa4ksp%2BCO1u5fHLKikZFNtfO%2FWKqZZHqgKMF94xXlD7NqcDoYhvHe1vW%2Bu0K2oBySs4j3zEVA4hA8NSPqBb%2F4vP3p8ehOMcQii8uTnVCJKz1hx9V7UDA5%2FWnmtLC9sRWZPndEFgFDnU672FPTgk86EX93m%2BNJLCSO3LPMEHndox0LyMno4f%2FK9YR9atQ3xHxo3gGESMyIM33ZDSk3HQjhGaDiq6gHhoqL%2FEFFCH22wRKhnvkxMD4OZJ%2BbqDj%2F2%2BGWRgrhToE8d6hRQZXtbxhAlGfOr%2B8gE5k3jrsCCJZU%2BnbbgiwYEWla0ihjb%2FaxCIZqDP4uHSwLQVDd4dCmdaDojAD7tYllCECiB8eQG78HEJplc0n1T8X0OogtOAIiMdtNTVDduspQWQF%2FzfWDrtMhRB1bOIkIVN81pfQLPulav2UPhoqEVwe7JykY1vQqzbltFi6%2BdnzDhKhG51uRp7TKn25FMQ5w3maqy8BMs005rUVxgWneeINnEZYww3saB0gY6pgHBSX0RpmL7QYhiLMRJzc95NxxdFZZRnY6J4y4t%2BrGro%2BciERsalYWMivw6x%2Fln%2FNB%2BXV%2F%2FVY86ukuLHEGeDi5ot1JUZGwTFOi19fXX9JxfNF2su8d5vdpRsf%2BFj0J%2FQy%2F1g%2Fnhxshr1T17Bc7A%2FhIOIMW6IkfGWy%2FSWK6TMlzpDplYuXGQ%2B9nHtM41SZTWY4Fcxgx5pB6pyLhJqIr92GbA1kalHIwi&X-Amz-Signature=d27cf171b4d376c8e531bab9befce4c6007a74107e4093316e15b974370a702e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
