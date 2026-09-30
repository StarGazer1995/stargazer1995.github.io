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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X562BZRO%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T202336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FH7tcdXHR627nAb%2BNCrOzW3c0gNfuFjtg8Fm8f4LwnAIhAJCQDBqHoUNlPNVmZpFDP8W4BI834R3JzbEmNZmF17UcKv8DCG0QABoMNjM3NDIzMTgzODA1IgySBuWzrUl7Oq2EVRUq3AMYKxxiGzJbFOPpNVsFfZMlGRCaZ7hCYPAl8Z5RFJC%2B5icjbV%2FlrS6y%2F16wmFBxrGUCs8ayoGNg4V0hiaglZUkDDsYiVgzcHYwE%2F0xh7mkBD%2BgLBVJCAM2w6766%2BI%2BFmGhDbC7OlJRBpJQMqRLftQ0b3qUWtpdFdNgnZX%2FgH1hs32w9wTu%2FBSwWA7ZvwFeUflc96tU8lngxbPFZsbsUo3j7VSkEOqQivYlJ6%2BV1VimVU52mEaiu4OdBikCFItyu8T4hnljc9W3K0PhP4FRHUiS6ECTmhvqhYmiI50GtzRXovAWlBh9AL7atRIszbFmrRnMGWJQ5sDgCCQl21SREX5QIUKmBJB4N26y0h4a8yDLDWEfMI1yKoO2o%2F4AqQdxii59anCWmS13ZA7KVhGMSzyRmQjNOHF3%2BZMJ7%2FVlObX5T8mKiBROZDFBPfG2swMd3zEdbQurj3HZFDtwj9OlkMD0ahcxQRy6ypnE%2Fli86t7Kd6SSQGk1J4vj5A1XwD5dpz2I1RZ%2BL8Y19odLnfeIbq3%2FAD4BUC%2FbenuCsFE%2F2WjZ5SGo5xAgTQ97%2F1pebJ%2BIpjxUqkMfJoB0E%2ByfYziWHufl2Bqeam03eoAbg9NKxHZeKjSDrue3Qk9DuDXRLzTCi1%2FXVBjqkAXUO%2B5XmxoNxVqtpcfvEWytotYNaBUSOqkHwGjxKmKNt2aZ%2FFnXMvw7sCT5G%2F6yVQM2hyj20SUjKGRhTAJu3pNfEWls67gNUXGWIjZXUmAClvHTiMS2yJyqHtEhG2pgzAsVP9oZPBE3LoffrBsyY%2FaC5nZiK%2Bj7fzBCJJrVhZ8%2F0KtLqXO9sR%2FCNYO23A4%2BUMVJ1Iy5VAWaf8QQUJvW%2FAMH%2Be%2F5h&X-Amz-Signature=b05bdb494901750f8b75bfd004db168f75cc1960b2024e42853a81e01488ed2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X562BZRO%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T202336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FH7tcdXHR627nAb%2BNCrOzW3c0gNfuFjtg8Fm8f4LwnAIhAJCQDBqHoUNlPNVmZpFDP8W4BI834R3JzbEmNZmF17UcKv8DCG0QABoMNjM3NDIzMTgzODA1IgySBuWzrUl7Oq2EVRUq3AMYKxxiGzJbFOPpNVsFfZMlGRCaZ7hCYPAl8Z5RFJC%2B5icjbV%2FlrS6y%2F16wmFBxrGUCs8ayoGNg4V0hiaglZUkDDsYiVgzcHYwE%2F0xh7mkBD%2BgLBVJCAM2w6766%2BI%2BFmGhDbC7OlJRBpJQMqRLftQ0b3qUWtpdFdNgnZX%2FgH1hs32w9wTu%2FBSwWA7ZvwFeUflc96tU8lngxbPFZsbsUo3j7VSkEOqQivYlJ6%2BV1VimVU52mEaiu4OdBikCFItyu8T4hnljc9W3K0PhP4FRHUiS6ECTmhvqhYmiI50GtzRXovAWlBh9AL7atRIszbFmrRnMGWJQ5sDgCCQl21SREX5QIUKmBJB4N26y0h4a8yDLDWEfMI1yKoO2o%2F4AqQdxii59anCWmS13ZA7KVhGMSzyRmQjNOHF3%2BZMJ7%2FVlObX5T8mKiBROZDFBPfG2swMd3zEdbQurj3HZFDtwj9OlkMD0ahcxQRy6ypnE%2Fli86t7Kd6SSQGk1J4vj5A1XwD5dpz2I1RZ%2BL8Y19odLnfeIbq3%2FAD4BUC%2FbenuCsFE%2F2WjZ5SGo5xAgTQ97%2F1pebJ%2BIpjxUqkMfJoB0E%2ByfYziWHufl2Bqeam03eoAbg9NKxHZeKjSDrue3Qk9DuDXRLzTCi1%2FXVBjqkAXUO%2B5XmxoNxVqtpcfvEWytotYNaBUSOqkHwGjxKmKNt2aZ%2FFnXMvw7sCT5G%2F6yVQM2hyj20SUjKGRhTAJu3pNfEWls67gNUXGWIjZXUmAClvHTiMS2yJyqHtEhG2pgzAsVP9oZPBE3LoffrBsyY%2FaC5nZiK%2Bj7fzBCJJrVhZ8%2F0KtLqXO9sR%2FCNYO23A4%2BUMVJ1Iy5VAWaf8QQUJvW%2FAMH%2Be%2F5h&X-Amz-Signature=149016b0eaa6d4efce05886b8d1994d6b880fa7e8471b8352469c7d146d98edc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
