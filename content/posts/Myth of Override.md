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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAUBG3KA%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T201137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCO9mMAkhA9eb7DW1BuSc20pchlHldpMGXwLVuH5OdE8gIhAIMhAo9LZSBnlLFS55TRbR2rMysqFqWhQZuxKoAjbJ3kKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy044Xbjkv%2BcrwD2Ggq3ANWhbndyDEu0pPRO6eqJCep0NWsbPs6XXLLg5Pbo7mNmcD0Dh%2FjB4dDoMYCYk7sYYdbAAqCEjbfpHEpdc6S2ji%2BR96zijy3LwzkUJuYrzrGIiYD382zkhfkmIXvHWqtxWi1rf%2BuBeBxiWJHymEgaYuSFfunkPQR%2BC4WIVFo9CDydSnu6NRQPkkMcVbQWxotRWyeBFO55Y7MC1vZMX6DqKKcM5LLsNvGmDpPaIEgzeAYKBkUyd0vwwtJ%2B%2FozO1BimZJHC5Ka%2FN6bmESlk1MjIarlbM8RK6k5MdgC1mzYH%2Fw9zHVDogU2Om8MJ6QzEaOTDraDZjamZ%2Bx5N66Cs6jwe8sovfmcPR%2FlO%2FFK8wTiz19QrVfiWH6EpsdsCKhgZUpyLtel1U%2BtOinoB1%2FV6v9F5kieUexbt1aXnBNjq3iLvmAmCRTj5M5uktAIr3dXgDK6o3LEf6qXdtLHLqGw0o2ooJd1yiVw1VCbQBxp0ESXGYSXGXh1yzFBFgm0WfRcTWcFcRowGP5cOLmYQou8Y02NBtBqhYeyHD8tpCW%2BCWo2w7OeobU4j7Wa9KLX5E1GeEdaOQ2%2BCrHbB7RsTgeJmqNlBovsBLR0C3v4QjrU2wG8daKHaDws4a%2F01w1klZF%2BBDCA7cnWBjqkAfmTtFogU5%2BciceYpBoW1F%2FxpOAmScHQAufGNWq3ScWw70W3%2F8sSpx00u9x5Ym4ufbxu97G0jrBtc6OtJp%2B89xSpOX2Pj2haT%2B5y5tKYcU84o1NxrgSbnkTPgXC5RgasFxfQvggoROlqat5740Gz4cL1j4NDAG9iR9xigAoYWG6Pc91HzeIyNIjAyWXPnBzU0yjlhF1PvaufQxzmrbYDZd561crK&X-Amz-Signature=b377c2d3794459d1a73656d9241e30d0344c547322b6ab05ff5862850f698e66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAUBG3KA%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T201137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCO9mMAkhA9eb7DW1BuSc20pchlHldpMGXwLVuH5OdE8gIhAIMhAo9LZSBnlLFS55TRbR2rMysqFqWhQZuxKoAjbJ3kKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy044Xbjkv%2BcrwD2Ggq3ANWhbndyDEu0pPRO6eqJCep0NWsbPs6XXLLg5Pbo7mNmcD0Dh%2FjB4dDoMYCYk7sYYdbAAqCEjbfpHEpdc6S2ji%2BR96zijy3LwzkUJuYrzrGIiYD382zkhfkmIXvHWqtxWi1rf%2BuBeBxiWJHymEgaYuSFfunkPQR%2BC4WIVFo9CDydSnu6NRQPkkMcVbQWxotRWyeBFO55Y7MC1vZMX6DqKKcM5LLsNvGmDpPaIEgzeAYKBkUyd0vwwtJ%2B%2FozO1BimZJHC5Ka%2FN6bmESlk1MjIarlbM8RK6k5MdgC1mzYH%2Fw9zHVDogU2Om8MJ6QzEaOTDraDZjamZ%2Bx5N66Cs6jwe8sovfmcPR%2FlO%2FFK8wTiz19QrVfiWH6EpsdsCKhgZUpyLtel1U%2BtOinoB1%2FV6v9F5kieUexbt1aXnBNjq3iLvmAmCRTj5M5uktAIr3dXgDK6o3LEf6qXdtLHLqGw0o2ooJd1yiVw1VCbQBxp0ESXGYSXGXh1yzFBFgm0WfRcTWcFcRowGP5cOLmYQou8Y02NBtBqhYeyHD8tpCW%2BCWo2w7OeobU4j7Wa9KLX5E1GeEdaOQ2%2BCrHbB7RsTgeJmqNlBovsBLR0C3v4QjrU2wG8daKHaDws4a%2F01w1klZF%2BBDCA7cnWBjqkAfmTtFogU5%2BciceYpBoW1F%2FxpOAmScHQAufGNWq3ScWw70W3%2F8sSpx00u9x5Ym4ufbxu97G0jrBtc6OtJp%2B89xSpOX2Pj2haT%2B5y5tKYcU84o1NxrgSbnkTPgXC5RgasFxfQvggoROlqat5740Gz4cL1j4NDAG9iR9xigAoYWG6Pc91HzeIyNIjAyWXPnBzU0yjlhF1PvaufQxzmrbYDZd561crK&X-Amz-Signature=77b6bf3e6a4fa1ffdb0e2f9df2e35b8ac40b888c6ce2ebe65be5fa5d610410a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
