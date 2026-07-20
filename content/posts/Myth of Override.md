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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WEFRM6X%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T052818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeFpzj2ulLDXAWywgGPJwT2que%2BTpkoDSHcKS7EEJd0AIhAI42rZMFucq2lRbG4BvtQzT%2BfJb%2FvP8LYAi8RKTrC03XKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj7Uju7HZB1IA%2B1agq3APmwK4wzl3C9yzMIu1n%2FO%2BE1F0p94NKtd8MTWz8wAIFG83Yj871O%2FODBgrY9kvg7knPnCVr1M7Sb4s%2FBFMMGFhgIJAUdzlt%2BtJHd2keC1swuz15IRAREGHGRLYO7g4t1LlIN1w7sg4Rcc6zM%2BxQTduxVwDrGCRfB1VhYoe0xD4lNKwvHLK0xodwXjMqE1B4VrpYLobxCi00hH5FwYE3UkuGWjU8x1CVSiKp5x1ggH%2BvgV1EvOOsAb58CDjvQfHQ9TZB8ZNMUZWBVR7j6MkwDFZa0opVwaqiBMZQd2vnh7z5KzPwwxhGplsJReW0A%2Bf4fTYS5HTsjgnzzdQgQ0zwFq5HNZPA99kR3EC4eqmUPGqP2iedOpO%2FZ26wm2PMXu7TIfP6XdU%2BOpDEHeReYI8BAnfxjWE8Y%2BdNOuZf6JPxzNASn89ZDxbe5FYndJHKQ1Fi2eb1XmstbR1vHR6SHyVrEZcaHrtu3s69p0AcQUR83rBlz%2FcjUtqYYUaVK6li0f2y1U91pgxv%2F5a5kHTi8c0l4kLqB5cEzbi2d8Ruh%2BB%2BwnPTY%2B9qgPbSS23jTGXoKo2UmG0pSdj%2Fwo71qiiYEy6N%2FE3dQCsauOt3Nyc2qRXgmcbKs1SuWRkyZKoj49hAuTDjr%2FbSBjqkAT2ufrrURozRzuocmQiNFW70VYchRyLY290%2FGKUvYfJezS%2F6Khwm0jFuqRo9NbhfE63TnQBGBDG3xkrJCnJb66osSK0pMwJ5GSxfchsTLyf1xIEKljhNsWi8WKNTsWtyhIVhEetqiyxzg%2F%2BpBAzrUwMdVxwFsIZjPIhB8S0LPqCId%2F%2FVgNqHxjbD9Qq0pvL%2FUIMqbNUXmmYQIm%2Fo0ilEVysgAWxt&X-Amz-Signature=7a25ada54920dce133e883876e1ecba39cda03516e427c6ef67304257d366f9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WEFRM6X%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T052818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeFpzj2ulLDXAWywgGPJwT2que%2BTpkoDSHcKS7EEJd0AIhAI42rZMFucq2lRbG4BvtQzT%2BfJb%2FvP8LYAi8RKTrC03XKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj7Uju7HZB1IA%2B1agq3APmwK4wzl3C9yzMIu1n%2FO%2BE1F0p94NKtd8MTWz8wAIFG83Yj871O%2FODBgrY9kvg7knPnCVr1M7Sb4s%2FBFMMGFhgIJAUdzlt%2BtJHd2keC1swuz15IRAREGHGRLYO7g4t1LlIN1w7sg4Rcc6zM%2BxQTduxVwDrGCRfB1VhYoe0xD4lNKwvHLK0xodwXjMqE1B4VrpYLobxCi00hH5FwYE3UkuGWjU8x1CVSiKp5x1ggH%2BvgV1EvOOsAb58CDjvQfHQ9TZB8ZNMUZWBVR7j6MkwDFZa0opVwaqiBMZQd2vnh7z5KzPwwxhGplsJReW0A%2Bf4fTYS5HTsjgnzzdQgQ0zwFq5HNZPA99kR3EC4eqmUPGqP2iedOpO%2FZ26wm2PMXu7TIfP6XdU%2BOpDEHeReYI8BAnfxjWE8Y%2BdNOuZf6JPxzNASn89ZDxbe5FYndJHKQ1Fi2eb1XmstbR1vHR6SHyVrEZcaHrtu3s69p0AcQUR83rBlz%2FcjUtqYYUaVK6li0f2y1U91pgxv%2F5a5kHTi8c0l4kLqB5cEzbi2d8Ruh%2BB%2BwnPTY%2B9qgPbSS23jTGXoKo2UmG0pSdj%2Fwo71qiiYEy6N%2FE3dQCsauOt3Nyc2qRXgmcbKs1SuWRkyZKoj49hAuTDjr%2FbSBjqkAT2ufrrURozRzuocmQiNFW70VYchRyLY290%2FGKUvYfJezS%2F6Khwm0jFuqRo9NbhfE63TnQBGBDG3xkrJCnJb66osSK0pMwJ5GSxfchsTLyf1xIEKljhNsWi8WKNTsWtyhIVhEetqiyxzg%2F%2BpBAzrUwMdVxwFsIZjPIhB8S0LPqCId%2F%2FVgNqHxjbD9Qq0pvL%2FUIMqbNUXmmYQIm%2Fo0ilEVysgAWxt&X-Amz-Signature=57358eafd2dfdfe91cdd0036ce1246815e99512f2c44f3e3ec6317d19a61873d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
