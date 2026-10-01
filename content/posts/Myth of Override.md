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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EA3RF6Q%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T075609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgOCbHKiPDkXVNXHlvB9XgoCrlHigJpTCIJAjyIFc8WQIhAIZI3R2tEsxgkHZpdERuwYbu%2B9ay4urZUl%2BMzLmTDWDhKv8DCHgQABoMNjM3NDIzMTgzODA1IgzYJvQKcaMDIJ%2BImhsq3AMLTS4Nx%2BZIcpcEEPeHiMBTiprnYBfimnSpsk39GY00bOXJ9XIBArnUQ3pU14qKnYQ0KPtpQ6zxVbBS%2FFyqtf9tebqBnEgHlRezx52vMOSMHXQtP29aQND5kSEDgwBD0h2sX9Rd1RNX2%2F4oohOU7xp5%2FDvpsgs49Zo6JvEIT3SvrUXoKxMG64JAM5EcIFE51bGd0KKgtmPqM8gxDEASYgHhNvvXTNh00iarThLSqre30QL9tf9%2B13gqonis2huweY5hsHm2rl2Xotx%2BlePX52HZFVAiJZRvLtzrB1iGHv89BGY1lriCA%2BrWcorlLBBartznMSHkjESCbgiKQq7F72rByRwOMTwhZ52eIZSx1%2B6dTWe9DSwnHzmuyukDhBDQbjVQe1bGjwARBbc7bYZyIHcSx5uXgcDy5eZa%2Bi7rhWTWKD3ySAEdf75ISQEZht%2Bs5H%2Bmtm%2FQtzwVp5dSUcAAZ3yQcXSOhsKV7OLakyfciMNcvJ8os%2BbZnj9ohlLqbgZCllra%2FsWRgTBsMI59EaGQ%2BxLz67K3EM7WB8EaECNkeI1alUElQrmXbtk2z0DQc4cKnI%2F6rApvtQ0GYmukT2kUBRA1JJaul3jIWaQe%2BGXmHWNo09w7Vnc811eyC9b7mTCki%2FjVBjqkASAqEUi%2FQ89KCE0DLDSU6L4ZevUnlbKobdr3PTPg4LZLiAtb41nOOmP4SKoOw0xTM4MXXr%2BcIJZDcIheMXheWjAK1w1%2BGvw3bFfDBtPtoVws0QqMQ9uLnO2mZ0C66B4Nb7ed1kT6bUqdvRYs%2FKDhzHIL9K2hwpuxJ9O7VSlM7hl2ClcsHX17d9ZGJWz8%2FHor0Wa5%2F7A92z1QR3H13bNWLvV%2BF5kp&X-Amz-Signature=5c7ab2441e1df37f0e8119be6e0d31f3f4bc14a6f7978c00063c8d468f60c880&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EA3RF6Q%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T075609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgOCbHKiPDkXVNXHlvB9XgoCrlHigJpTCIJAjyIFc8WQIhAIZI3R2tEsxgkHZpdERuwYbu%2B9ay4urZUl%2BMzLmTDWDhKv8DCHgQABoMNjM3NDIzMTgzODA1IgzYJvQKcaMDIJ%2BImhsq3AMLTS4Nx%2BZIcpcEEPeHiMBTiprnYBfimnSpsk39GY00bOXJ9XIBArnUQ3pU14qKnYQ0KPtpQ6zxVbBS%2FFyqtf9tebqBnEgHlRezx52vMOSMHXQtP29aQND5kSEDgwBD0h2sX9Rd1RNX2%2F4oohOU7xp5%2FDvpsgs49Zo6JvEIT3SvrUXoKxMG64JAM5EcIFE51bGd0KKgtmPqM8gxDEASYgHhNvvXTNh00iarThLSqre30QL9tf9%2B13gqonis2huweY5hsHm2rl2Xotx%2BlePX52HZFVAiJZRvLtzrB1iGHv89BGY1lriCA%2BrWcorlLBBartznMSHkjESCbgiKQq7F72rByRwOMTwhZ52eIZSx1%2B6dTWe9DSwnHzmuyukDhBDQbjVQe1bGjwARBbc7bYZyIHcSx5uXgcDy5eZa%2Bi7rhWTWKD3ySAEdf75ISQEZht%2Bs5H%2Bmtm%2FQtzwVp5dSUcAAZ3yQcXSOhsKV7OLakyfciMNcvJ8os%2BbZnj9ohlLqbgZCllra%2FsWRgTBsMI59EaGQ%2BxLz67K3EM7WB8EaECNkeI1alUElQrmXbtk2z0DQc4cKnI%2F6rApvtQ0GYmukT2kUBRA1JJaul3jIWaQe%2BGXmHWNo09w7Vnc811eyC9b7mTCki%2FjVBjqkASAqEUi%2FQ89KCE0DLDSU6L4ZevUnlbKobdr3PTPg4LZLiAtb41nOOmP4SKoOw0xTM4MXXr%2BcIJZDcIheMXheWjAK1w1%2BGvw3bFfDBtPtoVws0QqMQ9uLnO2mZ0C66B4Nb7ed1kT6bUqdvRYs%2FKDhzHIL9K2hwpuxJ9O7VSlM7hl2ClcsHX17d9ZGJWz8%2FHor0Wa5%2F7A92z1QR3H13bNWLvV%2BF5kp&X-Amz-Signature=cdd8c960a96859f979d46f2036d003a256b1477eded4721978f44470969822c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
