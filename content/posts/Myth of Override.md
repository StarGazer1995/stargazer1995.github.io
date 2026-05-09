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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV7I2DMW%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T073115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCGBSHhb%2FGeb0dyoSZBEfLMc4ZWcnR7Lw3VlJJnppEraAIhAOpAO7ik62SobgrjwklxGwP9FmF%2F5hc77qKHlANoSiZAKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFAaeWP%2FRByXoUCpYq3ANJ%2BR9Pj5Apwf5NaM4UXbDWKRbSXYigdw2YsjnO2EHJ2m2W5fXBEHZ86O2fr5UxdK%2FCXeIM7bsrDFadpfInX6EUyyI9oDE0SPlJJb56F%2FtsJH%2FENnal%2FLcyhEvkM13klK0Wrpx4rVkyqlvMk%2F7HygMz7gb1y3w4c39AQwckjlClnJP9bX7zalDK5p2WxXqMD%2FT61fKH%2FGpK4OZzIqZirbU%2Bsujcxmj2kAsofgSdYNK3yTXo28Zouimf5q9dWhpzgb9j%2BTe%2FXwWHPoT3PoQcjnWzGir%2FBctUS7rtSjyvKHH4lGWbEVMmABQhKbrUh8Ukm%2B%2ByaROw09WemiW4XgrGIJAkWy3cmcVVH2UW%2Ba%2FQfECwaP8f3uU2D9Wky%2BXdGjfpLxFIuN1Tv%2Fo6srO6OAoXUB1Wqh52LvlA6r8siDI00Znk%2FEno4Po9saJyaeYHthR3BU4ce1eaRvloY%2FdjQpBFc75WsgGb3TIgC7%2BJy8q%2F02pEDMJ8yGFJwoKPBMAOeQc4N2kdgqPzj7Bu3%2F%2B2aBx%2B6iTJy6ANzTfq%2F5PlAZFjFr%2FOiwufwus1xtpAeCqFAaOvtIs5mVH7UfWzLh7qMQdP6y9tmYbVo5G5dEFw4S3bFBNuHKlLXxzKex9wP%2BS7gDDHtvvPBjqkAbrjyF3MpbqSJY3Z5YevTJAzstgwmbXG3Z36JbHqUGhM%2FmeDvRvNGw3WbZd75Xzgr3Y31Io7u1%2Fe81faT%2BZwMwBiDpQ3vePZZQV%2FuFVDpJRDxnTE3zyXgxGodRFG5UPwhG9kP1IferebaMTAFuKvgieZUECwPT4KvHLujQT%2Ft7NTV5UAOCY9jfrMoat4jOvRuFHVIToI2NVm3FxTy8wNnddoOXY8&X-Amz-Signature=972a2fa45ee4e71f81f6395f3b4cceb2fb81652d8764fb0c4060c513e0f9c391&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YV7I2DMW%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T073115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQCGBSHhb%2FGeb0dyoSZBEfLMc4ZWcnR7Lw3VlJJnppEraAIhAOpAO7ik62SobgrjwklxGwP9FmF%2F5hc77qKHlANoSiZAKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFAaeWP%2FRByXoUCpYq3ANJ%2BR9Pj5Apwf5NaM4UXbDWKRbSXYigdw2YsjnO2EHJ2m2W5fXBEHZ86O2fr5UxdK%2FCXeIM7bsrDFadpfInX6EUyyI9oDE0SPlJJb56F%2FtsJH%2FENnal%2FLcyhEvkM13klK0Wrpx4rVkyqlvMk%2F7HygMz7gb1y3w4c39AQwckjlClnJP9bX7zalDK5p2WxXqMD%2FT61fKH%2FGpK4OZzIqZirbU%2Bsujcxmj2kAsofgSdYNK3yTXo28Zouimf5q9dWhpzgb9j%2BTe%2FXwWHPoT3PoQcjnWzGir%2FBctUS7rtSjyvKHH4lGWbEVMmABQhKbrUh8Ukm%2B%2ByaROw09WemiW4XgrGIJAkWy3cmcVVH2UW%2Ba%2FQfECwaP8f3uU2D9Wky%2BXdGjfpLxFIuN1Tv%2Fo6srO6OAoXUB1Wqh52LvlA6r8siDI00Znk%2FEno4Po9saJyaeYHthR3BU4ce1eaRvloY%2FdjQpBFc75WsgGb3TIgC7%2BJy8q%2F02pEDMJ8yGFJwoKPBMAOeQc4N2kdgqPzj7Bu3%2F%2B2aBx%2B6iTJy6ANzTfq%2F5PlAZFjFr%2FOiwufwus1xtpAeCqFAaOvtIs5mVH7UfWzLh7qMQdP6y9tmYbVo5G5dEFw4S3bFBNuHKlLXxzKex9wP%2BS7gDDHtvvPBjqkAbrjyF3MpbqSJY3Z5YevTJAzstgwmbXG3Z36JbHqUGhM%2FmeDvRvNGw3WbZd75Xzgr3Y31Io7u1%2Fe81faT%2BZwMwBiDpQ3vePZZQV%2FuFVDpJRDxnTE3zyXgxGodRFG5UPwhG9kP1IferebaMTAFuKvgieZUECwPT4KvHLujQT%2Ft7NTV5UAOCY9jfrMoat4jOvRuFHVIToI2NVm3FxTy8wNnddoOXY8&X-Amz-Signature=8dc8ad01f57d16399d5e73bcabbdd192380ca91d675e2df5e0ddd36887ef4c6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
