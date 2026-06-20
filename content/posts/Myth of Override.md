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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q24JPFD4%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T210300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDzhXs1deILl3XZ6%2FcytXfTIYczriyyXApMCbAu9A8zVwIgMj%2F3Rktby3IvE6%2BrJwn86ScmkQU6o0ejG1Kx0DgzgpwqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGPk0BbvKpWHBW9qeSrcA2AlLLE1l2xLyz7em23KSp2ZShlF1uUMgl6nSVhyHlYFAsIq9vC4Y7HQA53oS%2FFolE%2BdhBN%2Fjvpb%2Fiy71q89tQHJ8YJHaq9bvcgfE46u%2BFF8Js0P5TlkJfdfxwfGhBPoK3cRsH7nbTg1zMjtfXrpNbr8O7o06peRMtbTTQohQKozzzd2lSQWV%2BJs%2FjniLZejBuIVvWBBh7xxEs4W0Xz3UBIQe%2F4z9w%2Bxn5cH83RVq7ss3aTbPryEOKVZH8mIhneehopi13CDOT3Q67ZTPi9%2FALhf6ah59DybpjH2iR97MCxQ%2FAFoh0DvOhxwqpxkmlz%2BDn2yIqHvryPd9lJJGfdx%2FNKb62ZdefO9MF%2F0P98%2FRIC89oPy6HHJfcrU3Z4eTITAs%2FMCIG0%2FZB%2BA7bpTj77TDeeazvmse9qNDYhdSGmetzetJeGa8ICeAKOU6d0x8oxvXIRycRcJpALTGd0pWYhT00MVWjYI4fCUTNgqJGIDr%2Bw5VkipTkyeh81CawGxwx%2FO5xQqzcocke5%2B8ctVdG5T%2FGKEV5D2ROdWUA4XunAoUZUNv%2F0kJMGoQSafdLWYa1d9riDqCnHBGgMPfY4m46tIGAi1%2BN%2Fx7GH9zft%2Fl4hA72OrDZVcu3bZZjbGWwQTMI7829EGOqUB8qjngokLrKTiiWv4PR0L4qRyNs73XFbVrOswyMod9Ilh2bsEfxIF0r0hC0Df0nyIl0CCFyxpksQxsxDpL05FJI0O1Ur0yR1e5aXCofDJ3AZUP21P4Ty6Grpa2nMTiLGD7px36x9h3BCFyNsz1VbTXHKX2%2BnaPtWNatXAb9vpyV7DIoAh03udNCGleBEveRSuaP09RZJTHrHbiUC%2BXVYOo6X7L6kZ&X-Amz-Signature=41b32eab9daa60a38013d868103bd2a5a666cd32195b5c48d83c798c5030dd67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q24JPFD4%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T210300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQDzhXs1deILl3XZ6%2FcytXfTIYczriyyXApMCbAu9A8zVwIgMj%2F3Rktby3IvE6%2BrJwn86ScmkQU6o0ejG1Kx0DgzgpwqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGPk0BbvKpWHBW9qeSrcA2AlLLE1l2xLyz7em23KSp2ZShlF1uUMgl6nSVhyHlYFAsIq9vC4Y7HQA53oS%2FFolE%2BdhBN%2Fjvpb%2Fiy71q89tQHJ8YJHaq9bvcgfE46u%2BFF8Js0P5TlkJfdfxwfGhBPoK3cRsH7nbTg1zMjtfXrpNbr8O7o06peRMtbTTQohQKozzzd2lSQWV%2BJs%2FjniLZejBuIVvWBBh7xxEs4W0Xz3UBIQe%2F4z9w%2Bxn5cH83RVq7ss3aTbPryEOKVZH8mIhneehopi13CDOT3Q67ZTPi9%2FALhf6ah59DybpjH2iR97MCxQ%2FAFoh0DvOhxwqpxkmlz%2BDn2yIqHvryPd9lJJGfdx%2FNKb62ZdefO9MF%2F0P98%2FRIC89oPy6HHJfcrU3Z4eTITAs%2FMCIG0%2FZB%2BA7bpTj77TDeeazvmse9qNDYhdSGmetzetJeGa8ICeAKOU6d0x8oxvXIRycRcJpALTGd0pWYhT00MVWjYI4fCUTNgqJGIDr%2Bw5VkipTkyeh81CawGxwx%2FO5xQqzcocke5%2B8ctVdG5T%2FGKEV5D2ROdWUA4XunAoUZUNv%2F0kJMGoQSafdLWYa1d9riDqCnHBGgMPfY4m46tIGAi1%2BN%2Fx7GH9zft%2Fl4hA72OrDZVcu3bZZjbGWwQTMI7829EGOqUB8qjngokLrKTiiWv4PR0L4qRyNs73XFbVrOswyMod9Ilh2bsEfxIF0r0hC0Df0nyIl0CCFyxpksQxsxDpL05FJI0O1Ur0yR1e5aXCofDJ3AZUP21P4Ty6Grpa2nMTiLGD7px36x9h3BCFyNsz1VbTXHKX2%2BnaPtWNatXAb9vpyV7DIoAh03udNCGleBEveRSuaP09RZJTHrHbiUC%2BXVYOo6X7L6kZ&X-Amz-Signature=129540e5777c41de9411f4a7753b753bc5abbd2ce4ecdaa9e70ec4017eea7318&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
