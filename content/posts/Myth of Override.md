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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJRDYBEJ%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T112242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIEWyL5EVHZ80AHfRpa2LM%2B5OboE1UqeFHKexaWzU3CohAiEApeK5qLfTQGfre%2F9zmIgSD6Ue1sVP3QOY%2B39ZqOE%2Fvscq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDPCENkkFtdNfFoxUfyrcA7h1IgU8xoQrHBTwyBub6%2BT6d5CeAAHgKVSSmMewOHYuGOpBOtGtWQpw%2FQ18lJ9TUL1gmPCW6pCOlhUClSdAAdgbicGRoDrUxAOV6TTf1bV%2FTZ%2Bb37DesY8i%2BopAw7lajrigxt4YEn%2FP%2F%2FuCUNMJVvJFXc9CCkItiN92RpdF%2Fbx%2BgCU2HXi7%2BdMAAnkd5Epmc%2BpQTgLoUytT8dluYITpoEvUqJEDs%2BAI%2BsxATZ7cQoisow1yv9xNM9cC22TKkdo24k%2Bc1qAVvvUi%2FFPm2KErqBfZKqRiLO3%2FPKj9tl%2FHdlZxo04c21qkRDtuOlyIXHK8vYhghciis5Xqxnmwz%2B%2FWohj4lnKLtB4Unn9ULxBxn2UUZQXEvdgq4RTA3aLnezFR6%2BJHu4RA9v5ZyCWM9C%2Ff2bAobFbX41heBfaifqByqzVg7Ut9xIWEKo1Sdkvxhvjp4F6M3S6FnADpmn0yzpc9nTXim6eI3Dkz647MQLwvvtL2wJC%2Ffbn1p1%2FZr1W381exAEEOmSAbdAXTXDb6iY%2BR0CyGXwm%2Fkekfvv0y7b9DkcMbfFm%2FF4eh7zEeTZpa55SSI1LgzJ6bs9Ffdy8bMY7wIOv48Sq0Tu1H5qA4IXqg5qenL6YFL6BcpCvSW67MMLD3p9IGOqUBr%2BMqGKgq6Msc8VpSJZd19%2B6x3uF7N52orBEUU3Kl562FubJvO6YTcFnDlkgN8Ob0jNx7Rq1LlvKSElrYJqrLrdOmWdhUvpHdguHG7a0UFpDXwyKKazQEjnCeFkgINcEcJGXXsE6lAK05vP4i3mWtXpRb212Xcb%2FD60TFGXNWkxgLh7FUCBxyluonh6yjAHQfxgicyjJ71uS4ecjeO%2B9Z4PPp0A7o&X-Amz-Signature=93792c3179062336184799efd72642e235231e46080fe229b328862417e7f349&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJRDYBEJ%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T112242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIEWyL5EVHZ80AHfRpa2LM%2B5OboE1UqeFHKexaWzU3CohAiEApeK5qLfTQGfre%2F9zmIgSD6Ue1sVP3QOY%2B39ZqOE%2Fvscq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDPCENkkFtdNfFoxUfyrcA7h1IgU8xoQrHBTwyBub6%2BT6d5CeAAHgKVSSmMewOHYuGOpBOtGtWQpw%2FQ18lJ9TUL1gmPCW6pCOlhUClSdAAdgbicGRoDrUxAOV6TTf1bV%2FTZ%2Bb37DesY8i%2BopAw7lajrigxt4YEn%2FP%2F%2FuCUNMJVvJFXc9CCkItiN92RpdF%2Fbx%2BgCU2HXi7%2BdMAAnkd5Epmc%2BpQTgLoUytT8dluYITpoEvUqJEDs%2BAI%2BsxATZ7cQoisow1yv9xNM9cC22TKkdo24k%2Bc1qAVvvUi%2FFPm2KErqBfZKqRiLO3%2FPKj9tl%2FHdlZxo04c21qkRDtuOlyIXHK8vYhghciis5Xqxnmwz%2B%2FWohj4lnKLtB4Unn9ULxBxn2UUZQXEvdgq4RTA3aLnezFR6%2BJHu4RA9v5ZyCWM9C%2Ff2bAobFbX41heBfaifqByqzVg7Ut9xIWEKo1Sdkvxhvjp4F6M3S6FnADpmn0yzpc9nTXim6eI3Dkz647MQLwvvtL2wJC%2Ffbn1p1%2FZr1W381exAEEOmSAbdAXTXDb6iY%2BR0CyGXwm%2Fkekfvv0y7b9DkcMbfFm%2FF4eh7zEeTZpa55SSI1LgzJ6bs9Ffdy8bMY7wIOv48Sq0Tu1H5qA4IXqg5qenL6YFL6BcpCvSW67MMLD3p9IGOqUBr%2BMqGKgq6Msc8VpSJZd19%2B6x3uF7N52orBEUU3Kl562FubJvO6YTcFnDlkgN8Ob0jNx7Rq1LlvKSElrYJqrLrdOmWdhUvpHdguHG7a0UFpDXwyKKazQEjnCeFkgINcEcJGXXsE6lAK05vP4i3mWtXpRb212Xcb%2FD60TFGXNWkxgLh7FUCBxyluonh6yjAHQfxgicyjJ71uS4ecjeO%2B9Z4PPp0A7o&X-Amz-Signature=f3c021d880e9a432241890fccd488285bb3236f4cb14b944374d568bb2fba72b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
