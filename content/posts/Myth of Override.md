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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DZAHA7J%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T205453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXDLl%2BNDHgEaSeq1s%2BQ52tiRkeLvMZHXh8hgcBIc6flAiBVohhtWJUIHbhp80wBmWiRYTlUJaLaMl5Ykb7exZKEiyqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzW%2FenZAAEMGx6FeOKtwDokx4t4scFOUp2fstInrSle0Re0CSem5xo6Jg9yKqMVQoYeMbfYey4VcSVLKbsiBIP0Ab6gbLfc0NHAv06JaDko0k0dQYDSWApUa54bgzUKGZulija70%2FL5UTa9TBjbUhK%2B8iLk%2BJcnsbTn8QfCdlnKoYm0XW4%2BRK8W03QDNVW%2F%2BoNJeReBegZB9JbTkOOqvRj%2B21laeGaDKYIStFx0VUmAvrSmd9TFZVzdDcsnwu%2FZDe7aoNNyoOsNmnTIydN2RmCDdr3a9WnN%2F0Vy3zHA8n2Vcbhly75ckDV89ElWFC2hFk3JsBM4C2nKmdloFY7x0x9NhSOUJvi7IlCvhLBmoDOy0UR%2B37apK9FFSRyfsJXdhJHSmjacYsUXWsJX1jfGub9NVt3fXiQE86JyUOlhsS1UfWtyqW6uHDAojBxe6DiX6l5WM0CZfOF23kp58NGe%2BP3bMSvni%2BL2iXpf7IH2VgR91ZEUUfLt9hc1xUmcNr4PO6Mz3mmbPqrrGGy4tkFpg%2F2uGIYZT0sO5VO4pcEj9%2FlSnRn6d5I%2BgVTu%2Fj1TS%2BWvUoW7xJY15T2xsbYVk6A%2Fif1H%2FSJooDBRjVfUw9cZpWmH6suGC31OTFYMGqHB6RTpB07qwM1THAsiuWgkcwntiu0wY6pgHrPud80poYMFSM4haj%2FJb5DYEoR8V1%2BYvglvCqWAui13on2YSVzNJ6h1IY1PEgKeY7gAbuM%2FVHRiRvrnwBoHfRzWoL1OLYHf8BDZPx2GVpMjXqKtDwFmwVWpLwFGSfxHYv8E%2FNW50VrAZUcYl7aVtuMmsOE5XLpK%2BwP6ZmaWH70QBGmH%2FXDcuUom0oLteuomiVZkyeth0Wb7ykx0KonU9QKoU3hJN%2B&X-Amz-Signature=801435e393d129a2994b874f8ef71c049a3009302c925e0d2deaa1c4a4c86d14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DZAHA7J%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T205453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXDLl%2BNDHgEaSeq1s%2BQ52tiRkeLvMZHXh8hgcBIc6flAiBVohhtWJUIHbhp80wBmWiRYTlUJaLaMl5Ykb7exZKEiyqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzW%2FenZAAEMGx6FeOKtwDokx4t4scFOUp2fstInrSle0Re0CSem5xo6Jg9yKqMVQoYeMbfYey4VcSVLKbsiBIP0Ab6gbLfc0NHAv06JaDko0k0dQYDSWApUa54bgzUKGZulija70%2FL5UTa9TBjbUhK%2B8iLk%2BJcnsbTn8QfCdlnKoYm0XW4%2BRK8W03QDNVW%2F%2BoNJeReBegZB9JbTkOOqvRj%2B21laeGaDKYIStFx0VUmAvrSmd9TFZVzdDcsnwu%2FZDe7aoNNyoOsNmnTIydN2RmCDdr3a9WnN%2F0Vy3zHA8n2Vcbhly75ckDV89ElWFC2hFk3JsBM4C2nKmdloFY7x0x9NhSOUJvi7IlCvhLBmoDOy0UR%2B37apK9FFSRyfsJXdhJHSmjacYsUXWsJX1jfGub9NVt3fXiQE86JyUOlhsS1UfWtyqW6uHDAojBxe6DiX6l5WM0CZfOF23kp58NGe%2BP3bMSvni%2BL2iXpf7IH2VgR91ZEUUfLt9hc1xUmcNr4PO6Mz3mmbPqrrGGy4tkFpg%2F2uGIYZT0sO5VO4pcEj9%2FlSnRn6d5I%2BgVTu%2Fj1TS%2BWvUoW7xJY15T2xsbYVk6A%2Fif1H%2FSJooDBRjVfUw9cZpWmH6suGC31OTFYMGqHB6RTpB07qwM1THAsiuWgkcwntiu0wY6pgHrPud80poYMFSM4haj%2FJb5DYEoR8V1%2BYvglvCqWAui13on2YSVzNJ6h1IY1PEgKeY7gAbuM%2FVHRiRvrnwBoHfRzWoL1OLYHf8BDZPx2GVpMjXqKtDwFmwVWpLwFGSfxHYv8E%2FNW50VrAZUcYl7aVtuMmsOE5XLpK%2BwP6ZmaWH70QBGmH%2FXDcuUom0oLteuomiVZkyeth0Wb7ykx0KonU9QKoU3hJN%2B&X-Amz-Signature=43217b90ed1bea1cf78e2b42bed1308312d4df45bc5a8396782a37285df02613&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
