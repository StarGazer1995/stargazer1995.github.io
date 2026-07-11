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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WF2QIG3%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T124859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIGkucNdXbkB5RoM%2F%2Fc8a0lTzJ7J0XJCKo9zVmvbwPhlBAiAMyrzSkgkNMsZ5oQ0VYk8Bt8iDB%2B1SjSiS5zyNLQ2LMSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlbpBmhjdPKYxJ7gzKtwDQqTHuMA0VJDIvv6eU510couA7GJrAk%2BVCcatmpyN65A3UipYHKAuvy4wqO7aNz0VaiY93xVWig8xwVV1C2El0U3m83SHkR35pqIaEzLNukgXsrcaq%2FEfuagppED2r5dagJy8lAS2G7s2Zu2%2Fx5XOPZcHR18y89%2FGAiM3%2Fg6Ux6cyiWstkkpRALKpc8aozb1YHbUbv6MsAXjvo7qzkRgQzv6PZezLrr8iNlsDJmJHpljVRyhkmdOPFxMaV03pOZ4bCw7ypgh4tH7asZznAoQc9fyG5dTH5jLRxLF6C6iZFVCXsx2o7OtMt8VLQ2mCIoDcXdv72i2gk9bV33pmsMV%2BX3Sjayyhqpug0ohjN2D22AY44%2ByvUYGvEk0ZRQU2VZ6OcSzsLlmJkIuYTx5rttL39IPH4ZBKyZSrlsRUIYuvC5UJtZu%2BTWjENDSbHPDSdbPP5jy%2B8Cvc%2Bn%2BC6vyWVQaDb6wFrQf8PPS%2FbR1P0F2s8LO3bPeQXL38Y%2FauOfo9ejan1hXJLKPuMpHpgKRPHA4lHiJYK6RIysN3kcY4lwYURMdiFmdtt%2BO7WrEgQ11Be%2Fy9jpCxlQXFyTboNTzP1J6DxS5C%2FNViUpf7a0ewbM2nSm0MxDNH%2FmXpjmG01mkw8aHI0gY6pgGdJu37JwKWze3krwf8z3QJFUE%2Bz4YhA6VC3Akwg4om8jHFshu8MTlJ3uxDGSxZT6ug3aXkmKv3aUDzu9gKnqTJt%2FbQg558mGq3PwrB0V8LuD0qXkeWzOqWNMWMHb0OZbscHXbqkRwaG%2F5ScThd0%2Br%2B%2B1EPhbfnZM6gATlBg2dPcWNGN%2F8dWN5vV9ooZqafunooRE9rvc0v%2FjnEnw%2BporMMvraSrzQt&X-Amz-Signature=37c32a7415e36140c97d89e8037ff3e91afc6487d8786f852700e57fcd08b934&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WF2QIG3%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T124859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIGkucNdXbkB5RoM%2F%2Fc8a0lTzJ7J0XJCKo9zVmvbwPhlBAiAMyrzSkgkNMsZ5oQ0VYk8Bt8iDB%2B1SjSiS5zyNLQ2LMSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlbpBmhjdPKYxJ7gzKtwDQqTHuMA0VJDIvv6eU510couA7GJrAk%2BVCcatmpyN65A3UipYHKAuvy4wqO7aNz0VaiY93xVWig8xwVV1C2El0U3m83SHkR35pqIaEzLNukgXsrcaq%2FEfuagppED2r5dagJy8lAS2G7s2Zu2%2Fx5XOPZcHR18y89%2FGAiM3%2Fg6Ux6cyiWstkkpRALKpc8aozb1YHbUbv6MsAXjvo7qzkRgQzv6PZezLrr8iNlsDJmJHpljVRyhkmdOPFxMaV03pOZ4bCw7ypgh4tH7asZznAoQc9fyG5dTH5jLRxLF6C6iZFVCXsx2o7OtMt8VLQ2mCIoDcXdv72i2gk9bV33pmsMV%2BX3Sjayyhqpug0ohjN2D22AY44%2ByvUYGvEk0ZRQU2VZ6OcSzsLlmJkIuYTx5rttL39IPH4ZBKyZSrlsRUIYuvC5UJtZu%2BTWjENDSbHPDSdbPP5jy%2B8Cvc%2Bn%2BC6vyWVQaDb6wFrQf8PPS%2FbR1P0F2s8LO3bPeQXL38Y%2FauOfo9ejan1hXJLKPuMpHpgKRPHA4lHiJYK6RIysN3kcY4lwYURMdiFmdtt%2BO7WrEgQ11Be%2Fy9jpCxlQXFyTboNTzP1J6DxS5C%2FNViUpf7a0ewbM2nSm0MxDNH%2FmXpjmG01mkw8aHI0gY6pgGdJu37JwKWze3krwf8z3QJFUE%2Bz4YhA6VC3Akwg4om8jHFshu8MTlJ3uxDGSxZT6ug3aXkmKv3aUDzu9gKnqTJt%2FbQg558mGq3PwrB0V8LuD0qXkeWzOqWNMWMHb0OZbscHXbqkRwaG%2F5ScThd0%2Br%2B%2B1EPhbfnZM6gATlBg2dPcWNGN%2F8dWN5vV9ooZqafunooRE9rvc0v%2FjnEnw%2BporMMvraSrzQt&X-Amz-Signature=117d8fe7a1ba25d5135714ea4a6edd063305133c302711c659c3fd9981bde27f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
