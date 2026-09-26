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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PXIJHHD%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T135721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFWyRny3GTgx%2BapO6K4ao3PCBgQNOLlpFfRyO8nSR0AoAiB56nhNz0ezZWt90ZxHOByc5qvWS6IvClkpy9Ycyopvsir%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMKNLgKg7RRnnqIHBPKtwDJ6rOgQ9PpPEc9y4cbxIFmq%2FB5b2UQKjpuCrETe6q8vEcThO4KWw2M97jBVQxF2iI3ugY9fMrRNoqJKwjizuCgYT5%2FOhwLTmMnI65%2B85aN82IoQpGpms9ervBcB01lPUw3Pwnpn0DKteh4OsV4oBX%2Bie9X0aOz9cvcJGy5K311V60CmusF%2F8xoJxJ%2B030VahdIaO0K%2BjC0vjGGZEqxr6D6Zv4XlhBYNmh3nSt0HTeghj%2FzyX26czOk3%2FPG7SIxIeBsWybRFeJO%2F%2BFiBs16NIyDXoTgpj5IMwgmxWlGQozafpKytEenVlGNOomqyeRfWLG%2BF9znus3IUqVHepF6LckECfoI2gSeum5NSVcI4644fgC5zjatlmxOqrkR9l4EylbEgfNfMHQCT597vIyh8A43LXFm8L8iATYadNcwOJUv%2F93TDuidDam%2BEnUkDL37%2BRulh65ANK23itIaSifnNkVO8%2BA7s3oM4DJzc3yUMKB74qZ4jc%2BLvGwmettzQuhxQw%2F%2F4kvUmnxKWcRDtpErDtnyJVAkypVRI%2F8Te2D5QB087QYmD9KYPmEZzq8LlFZYOu%2FWAzDvnsWB%2Fwf84CRJrYdP%2FJpqXklFNMKlp6TVWC8%2Brw4cI%2FJ7pDAe9fwU80w5%2F7e1QY6pgFJT0kSfuUG%2FeSYwE5L2YGwO5OR4SodSb%2B1DQHyHGMZXNqnwjvpncKQRl1fHcWI49lsZlMVzKWcBOpU0h3%2Fh1zaWCE%2BY2d%2FK3yGju%2Fzz9WHDAHe20otOqF21c86e9ZfZADx6rCF%2FsOALtMBoKtDnknR7H1Z2nsW0F8FQqxgfbBofRQJindeMNZfrx10udHV6kpLww%2Bjm4SG1VOdg5em7NvY733L%2BCXa&X-Amz-Signature=9b1a818e534cc2b8746ca2b0bf8357c79e6cb8123657dac864500a0649e42c5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PXIJHHD%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T135721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFWyRny3GTgx%2BapO6K4ao3PCBgQNOLlpFfRyO8nSR0AoAiB56nhNz0ezZWt90ZxHOByc5qvWS6IvClkpy9Ycyopvsir%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMKNLgKg7RRnnqIHBPKtwDJ6rOgQ9PpPEc9y4cbxIFmq%2FB5b2UQKjpuCrETe6q8vEcThO4KWw2M97jBVQxF2iI3ugY9fMrRNoqJKwjizuCgYT5%2FOhwLTmMnI65%2B85aN82IoQpGpms9ervBcB01lPUw3Pwnpn0DKteh4OsV4oBX%2Bie9X0aOz9cvcJGy5K311V60CmusF%2F8xoJxJ%2B030VahdIaO0K%2BjC0vjGGZEqxr6D6Zv4XlhBYNmh3nSt0HTeghj%2FzyX26czOk3%2FPG7SIxIeBsWybRFeJO%2F%2BFiBs16NIyDXoTgpj5IMwgmxWlGQozafpKytEenVlGNOomqyeRfWLG%2BF9znus3IUqVHepF6LckECfoI2gSeum5NSVcI4644fgC5zjatlmxOqrkR9l4EylbEgfNfMHQCT597vIyh8A43LXFm8L8iATYadNcwOJUv%2F93TDuidDam%2BEnUkDL37%2BRulh65ANK23itIaSifnNkVO8%2BA7s3oM4DJzc3yUMKB74qZ4jc%2BLvGwmettzQuhxQw%2F%2F4kvUmnxKWcRDtpErDtnyJVAkypVRI%2F8Te2D5QB087QYmD9KYPmEZzq8LlFZYOu%2FWAzDvnsWB%2Fwf84CRJrYdP%2FJpqXklFNMKlp6TVWC8%2Brw4cI%2FJ7pDAe9fwU80w5%2F7e1QY6pgFJT0kSfuUG%2FeSYwE5L2YGwO5OR4SodSb%2B1DQHyHGMZXNqnwjvpncKQRl1fHcWI49lsZlMVzKWcBOpU0h3%2Fh1zaWCE%2BY2d%2FK3yGju%2Fzz9WHDAHe20otOqF21c86e9ZfZADx6rCF%2FsOALtMBoKtDnknR7H1Z2nsW0F8FQqxgfbBofRQJindeMNZfrx10udHV6kpLww%2Bjm4SG1VOdg5em7NvY733L%2BCXa&X-Amz-Signature=5219d86c548e67192acd63bc853f99649ffcbcb8171a1f3f43227308f8604ab5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
