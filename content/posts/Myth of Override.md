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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5B7O2LZ%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T211040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEKpzxXnPMy7we6TU1u24Lf6qJ3FHqP3a6u%2FSCkHDZ7oAiBYXMq1YLrCMURYGYqERzJaFdP0UUGchUXfVw%2BUlJVO6Cr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMBfnBUl0gsuOX5GxZKtwDJw5z2tnPsMiEHDWRxgdDXAypbeObMN1VTLt2U34wOLvSyBcy%2BVKl80uDaMF9uJIf5hZj2GmZiAdfCu%2BU5uTLTBsOhUS6ChPATHcS5kT3JBoeC2sBT9pjYEKHqmM6wOlCjg%2FwGcL7PED6HpbRGe6Tnu%2F2DEEYkKMJlhcH3b%2FjjiioNR6n911BSs8rGKGXSQulX7ClQ6rpmJg28r%2Fx76OcI6zJqkWfXjBAoRKwTie4KTpPCkW22E7G%2FrShFFjd4Ti2HS2rNwcP4soW4UkKdhKtjWkYq5t2kQt0xhqenn19ZwNqQxRc5t2DBR0FjymtK9rt8RZhZHLdjccQpDkz%2BGAwralOnTinXgMpSxuzjNRbRBkERpclsw9GOh9LF3xBJqoYRLvwpfoaM17etBTlY9UD8GozKjtzxXU%2B%2FgkWostbpKHZ9tY2h9EiaLkBQrfaqfx1f5AfIRxeS%2B9gKGya2W0F38JezB%2Fzc1htrSGxGoEbeoSaTR13Dia4tzb18TTcO6xlpdJUOCQZJiZXYd4HL3gX9RsqLKeHPHQjV9lbnaL5mir13RObcFMzrH4yYJxJ8drJ%2FwFikAxRGCiPDTiI4W0BdIww0IYcAad16augcme%2BKRFpuEvWTm1lJuCokXgw7Oqv1gY6pgFNwNhw4f4VEnWjF7z62STEgEr%2FiyUizMbPtRDDLh6s2Yp6tXvj319gFcmeJPq3E%2B5uCQ2g%2FfzsSCGRDua0LHR5POiZHAjAGQZ9KNejb03kKqbMGjCsm76VxVH7zRoois4MbYcCg47YC%2BBh8EVWrsQTms%2F5RFEQrwFD%2FHz7e3d9Djnavi19oiif66Ifqrcvr8CvpKJ2yNmffePrraiP%2FcdsriHZb1uj&X-Amz-Signature=79333ac992d756b7de512e64ed43bcf717513a8cf48b80e91b13398d0bb679f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5B7O2LZ%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T211040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEKpzxXnPMy7we6TU1u24Lf6qJ3FHqP3a6u%2FSCkHDZ7oAiBYXMq1YLrCMURYGYqERzJaFdP0UUGchUXfVw%2BUlJVO6Cr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMBfnBUl0gsuOX5GxZKtwDJw5z2tnPsMiEHDWRxgdDXAypbeObMN1VTLt2U34wOLvSyBcy%2BVKl80uDaMF9uJIf5hZj2GmZiAdfCu%2BU5uTLTBsOhUS6ChPATHcS5kT3JBoeC2sBT9pjYEKHqmM6wOlCjg%2FwGcL7PED6HpbRGe6Tnu%2F2DEEYkKMJlhcH3b%2FjjiioNR6n911BSs8rGKGXSQulX7ClQ6rpmJg28r%2Fx76OcI6zJqkWfXjBAoRKwTie4KTpPCkW22E7G%2FrShFFjd4Ti2HS2rNwcP4soW4UkKdhKtjWkYq5t2kQt0xhqenn19ZwNqQxRc5t2DBR0FjymtK9rt8RZhZHLdjccQpDkz%2BGAwralOnTinXgMpSxuzjNRbRBkERpclsw9GOh9LF3xBJqoYRLvwpfoaM17etBTlY9UD8GozKjtzxXU%2B%2FgkWostbpKHZ9tY2h9EiaLkBQrfaqfx1f5AfIRxeS%2B9gKGya2W0F38JezB%2Fzc1htrSGxGoEbeoSaTR13Dia4tzb18TTcO6xlpdJUOCQZJiZXYd4HL3gX9RsqLKeHPHQjV9lbnaL5mir13RObcFMzrH4yYJxJ8drJ%2FwFikAxRGCiPDTiI4W0BdIww0IYcAad16augcme%2BKRFpuEvWTm1lJuCokXgw7Oqv1gY6pgFNwNhw4f4VEnWjF7z62STEgEr%2FiyUizMbPtRDDLh6s2Yp6tXvj319gFcmeJPq3E%2B5uCQ2g%2FfzsSCGRDua0LHR5POiZHAjAGQZ9KNejb03kKqbMGjCsm76VxVH7zRoois4MbYcCg47YC%2BBh8EVWrsQTms%2F5RFEQrwFD%2FHz7e3d9Djnavi19oiif66Ifqrcvr8CvpKJ2yNmffePrraiP%2FcdsriHZb1uj&X-Amz-Signature=26abce62ace3e2c64c71822b5961a1a3f65270c15da208bbe387d98c5b905e25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
