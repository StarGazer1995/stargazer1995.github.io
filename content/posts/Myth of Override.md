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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWTZ2PWO%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T020210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGvmviohLO%2BaRv2R8Nq2R8yq5%2F0RXvQ6FvGwhjcWw8EQAiBJuc0aAYXoR29QaMnwFKiH5mrzqFB%2FAGsUHbop0%2Bf7ISr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM6z%2FX5lOx%2F3AB0AYwKtwDC3ynmaUucDM54kNo5z9rS%2BFhgBalpA8ZjZxUIimhjS5feC1rb%2Fv9TDjnwJlE9lljFiB1PSIWNn%2FcCWcVTOTTH9hCo2v0lWr%2Fs%2Fi9%2FBpJOZliKwQmqSGBwaJQ2zjMSIae0PS5hZ98UnMgZA%2BgWyipztSuQvHjkyoTNolATISNSyZ%2FzSG9XRR5qTBGzqsoacf5PnEFYvtsLCYheQqlOkyyDz1kGwQKW4qNnswownY7iLeeqitgf%2FzQz7CElLa%2BODt4ciBrwB9fEakl1zavt2cfZ5ADF46HXE3jnLHC1DuL8srMdoYX%2F8vmh0jMqt0z1TsvXBZ47Cue0oPKFA7129oqZi9IznFNWbl72nQ6WUUEBscseLTtL5FLIJ7e4q6CBQ7roH2XJJ8fcXGssFXAKOwabFbktx7ukvIeCbtPa91Rwq990vE3Xv8HPuS4NkissYe80sb4vm8SPPrWkcyGG1tF%2BZxo4cY0mSnB3TvJfP0n9RBYN3BqhovD%2F9E%2FuRd4PP0h6RIfGcO4RSAIZCklozFJExqZsCn3%2FfVZMWv7FTy0vUcMEM9BFDbyW0Lkv855PiY%2Fvrfx4azoxs4MlK%2F6x8YKPLhAmT%2Fj8rCm76zIvXsjXJdkdVnndmvtjA4byWEwiKnB1QY6pgHkjg%2Bggt2kJmuRxkcqy60paObfU%2FtZhhIvRm9T5bp4fu5peA9pwBLnHHl5lWw67gC5l6dYYEkb4282A5jId%2BJbw1F3TNlsY%2BcQfCti%2Fvq1Vc2EAFGEs1q9wr1fo%2Br4JNvuYHDlMIu5jigUyBpub5zD4u5umzhfASIV5vVSU6WzkMOec%2BwEWIxIhwFtMQrLu2ODPXtYUWp8XhOZ8P7YT4iAkCVGO2Qy&X-Amz-Signature=7141f30e1b34e673d44c7d02a7057e735627154267b14fc22b98cea1099401d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWTZ2PWO%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T020210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGvmviohLO%2BaRv2R8Nq2R8yq5%2F0RXvQ6FvGwhjcWw8EQAiBJuc0aAYXoR29QaMnwFKiH5mrzqFB%2FAGsUHbop0%2Bf7ISr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM6z%2FX5lOx%2F3AB0AYwKtwDC3ynmaUucDM54kNo5z9rS%2BFhgBalpA8ZjZxUIimhjS5feC1rb%2Fv9TDjnwJlE9lljFiB1PSIWNn%2FcCWcVTOTTH9hCo2v0lWr%2Fs%2Fi9%2FBpJOZliKwQmqSGBwaJQ2zjMSIae0PS5hZ98UnMgZA%2BgWyipztSuQvHjkyoTNolATISNSyZ%2FzSG9XRR5qTBGzqsoacf5PnEFYvtsLCYheQqlOkyyDz1kGwQKW4qNnswownY7iLeeqitgf%2FzQz7CElLa%2BODt4ciBrwB9fEakl1zavt2cfZ5ADF46HXE3jnLHC1DuL8srMdoYX%2F8vmh0jMqt0z1TsvXBZ47Cue0oPKFA7129oqZi9IznFNWbl72nQ6WUUEBscseLTtL5FLIJ7e4q6CBQ7roH2XJJ8fcXGssFXAKOwabFbktx7ukvIeCbtPa91Rwq990vE3Xv8HPuS4NkissYe80sb4vm8SPPrWkcyGG1tF%2BZxo4cY0mSnB3TvJfP0n9RBYN3BqhovD%2F9E%2FuRd4PP0h6RIfGcO4RSAIZCklozFJExqZsCn3%2FfVZMWv7FTy0vUcMEM9BFDbyW0Lkv855PiY%2Fvrfx4azoxs4MlK%2F6x8YKPLhAmT%2Fj8rCm76zIvXsjXJdkdVnndmvtjA4byWEwiKnB1QY6pgHkjg%2Bggt2kJmuRxkcqy60paObfU%2FtZhhIvRm9T5bp4fu5peA9pwBLnHHl5lWw67gC5l6dYYEkb4282A5jId%2BJbw1F3TNlsY%2BcQfCti%2Fvq1Vc2EAFGEs1q9wr1fo%2Br4JNvuYHDlMIu5jigUyBpub5zD4u5umzhfASIV5vVSU6WzkMOec%2BwEWIxIhwFtMQrLu2ODPXtYUWp8XhOZ8P7YT4iAkCVGO2Qy&X-Amz-Signature=036e088fb8118263a64d81775d9e40de78777fe44af5557803afa0db3ec2dfb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
