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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OVI3KPX%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T122344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICzJj%2FEsNDVwPQydm4l%2FY9psT9kU8q%2BxoA4rs46LfpYRAiB7%2FRtLbVh7CpcAY152jT20OOvhHBBC86RpLugZsbO2zSqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7WrBi1%2BheSG0ijYbKtwDfXMfvYmzvhfk8dDiql3tjNzlIUj58V2foeXAZ1wpI9apDn5LUK9bYQV2c9QU8E%2BKNeteK16ChNwNAfWH60B6dsPMD6%2F2IzJ7RtEVoWpMp3TqwpmZSRrEhqgUuVsOTGXdvWecNaJUpHt3MxxwQuhIwPMkSIHNuDtMwAll9hqEj8KU%2B%2BbshOzs0rrlUfS44Fi4%2FPAGRX0nK35hIgxfzKj47jFf7HEnq00I4wKA5HxIxHUiDZdFNf%2FtsCe0qHdJ2kKRK7%2FWMvLVubkdI13vLKdQ4%2BkwGz2fu6DQrf8khH7nm4I%2F3XmFNuGFejlFREXWXUtlqpG7al5quqKbotPCwalsr8LEbk6W6st3TXyctYq%2BX9pLRL%2FM%2FCJVsBASjItIDxzQgvdUkg1VzLrShHSt0DNuVRtgzVtgzBxsZJQpHU%2FIwUxbcy9abvTDGHRe1aEQcevQdonShHATiea0%2FjNYGQJhxOOsW7NSy6RGYN4VVanT%2BcpJetwtKaLuFrUJaMxBzbCdCcg8KCtGLykKKcc%2F6AAloDcqBWZLAZ%2B5wzXX%2F3RfgNUPGb3%2FeA121sMRiRlmPZcxIUxYU4FITAWbHT9xTEEJGYKC2XdM1fCkMHP7FaSFNRnibRa4L4R22%2Fd2494wqt6g1AY6pgErctvGMT7ND3EzKJYU8EQtXNYIIF9GCxa8Qr4lCtORFh23b3lG6UN89YO8Y0G7YJGtIc%2BmXIDJWcS7dbYf429p1QJHl8fighFa1Gg8Ybv8IO%2BT437wcJIDZRDJioj1UhQ3qdolRTqkOeOhwTv5Giad13WZ5Lf7NEUV1FDQVeA0TgYEW1EAT6l7y%2Bp3n5HrAQ13BbTsTPEp5Cl6YtzEzAX9jhK7cFGh&X-Amz-Signature=bf44a0aec9ae5b24f8f8c478bf6dfbeaadee744da6c56a81ebc6bc1c5fc95c62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OVI3KPX%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T122344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICzJj%2FEsNDVwPQydm4l%2FY9psT9kU8q%2BxoA4rs46LfpYRAiB7%2FRtLbVh7CpcAY152jT20OOvhHBBC86RpLugZsbO2zSqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7WrBi1%2BheSG0ijYbKtwDfXMfvYmzvhfk8dDiql3tjNzlIUj58V2foeXAZ1wpI9apDn5LUK9bYQV2c9QU8E%2BKNeteK16ChNwNAfWH60B6dsPMD6%2F2IzJ7RtEVoWpMp3TqwpmZSRrEhqgUuVsOTGXdvWecNaJUpHt3MxxwQuhIwPMkSIHNuDtMwAll9hqEj8KU%2B%2BbshOzs0rrlUfS44Fi4%2FPAGRX0nK35hIgxfzKj47jFf7HEnq00I4wKA5HxIxHUiDZdFNf%2FtsCe0qHdJ2kKRK7%2FWMvLVubkdI13vLKdQ4%2BkwGz2fu6DQrf8khH7nm4I%2F3XmFNuGFejlFREXWXUtlqpG7al5quqKbotPCwalsr8LEbk6W6st3TXyctYq%2BX9pLRL%2FM%2FCJVsBASjItIDxzQgvdUkg1VzLrShHSt0DNuVRtgzVtgzBxsZJQpHU%2FIwUxbcy9abvTDGHRe1aEQcevQdonShHATiea0%2FjNYGQJhxOOsW7NSy6RGYN4VVanT%2BcpJetwtKaLuFrUJaMxBzbCdCcg8KCtGLykKKcc%2F6AAloDcqBWZLAZ%2B5wzXX%2F3RfgNUPGb3%2FeA121sMRiRlmPZcxIUxYU4FITAWbHT9xTEEJGYKC2XdM1fCkMHP7FaSFNRnibRa4L4R22%2Fd2494wqt6g1AY6pgErctvGMT7ND3EzKJYU8EQtXNYIIF9GCxa8Qr4lCtORFh23b3lG6UN89YO8Y0G7YJGtIc%2BmXIDJWcS7dbYf429p1QJHl8fighFa1Gg8Ybv8IO%2BT437wcJIDZRDJioj1UhQ3qdolRTqkOeOhwTv5Giad13WZ5Lf7NEUV1FDQVeA0TgYEW1EAT6l7y%2Bp3n5HrAQ13BbTsTPEp5Cl6YtzEzAX9jhK7cFGh&X-Amz-Signature=7e9a3a644cfbe60c7bf48708009c9b7da586cd7d5153b3f44ec09acb259a6b14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
