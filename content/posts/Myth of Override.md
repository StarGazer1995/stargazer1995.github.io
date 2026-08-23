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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCW2CEKU%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T161150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIER7aFhU4cTBSKrbh52REqJKRBYaDUzi6lgEt3vYHlLTAiEApvMkW5vzDFuGMKQqpdoRPpboDhNA4tdv4RWNsYKM81EqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1ODMPvvpoJsyTYVSrcA7MiVaH%2F5gCl7j1cQbMs3%2F5bxiWZpCgaOONUlDFfgP%2FaoIwsj25yLRBy6nuqnYp3T5FfPooIgKR3J3mJVAPswrWA69JwLk8eQ2lJ90EtAjydvnUFjDVi6R0csZohUGlggt1%2F1GSrFlk7zrSX9YgAGWDA%2F54G7yPYFXC5KLGPOrkAbia2nWEjlM6cIiPkGwR90Qggxyuv2jPr02OoOJVCdLuBJ9CmG6zcRY%2Fj3AMRnbTdPNiZUoW2CgP7ShNNkyoHQ1eSKqaDTOROZNBNZQoTc4a2WGQ8LBNpvS4qe9OEcHNA%2Be8NSYV2j9ephUuOrZ4%2FjV6JqxNzdrsfkZPRJYIrOd5hkpIhqZBxFjBjY%2Fa9RtDqkkl5AEEWAdkEHezvHipvHlVMIXVnsje4l%2BZ7vgM9rvJX9Zs91lgJQMXc1N5RwIJr9MO8B5FC3ZTwEedbdLrXKDCFZuSi9pbLGT9YZz4uEIitY1hLUl048Xn6Ds2tbyZTLEvuWng92HaUThCk9J6StWuze2SLCHIGrMKF%2BbkZZHp%2FxQew0pE3frWPpXON5C01IJoV5idXfyISLvCDkoXhscgAWargJbN%2FPoPmPegDEWUsq5OYFHR3RLyL58NFZbD0LiO0Ev7Jjer9C4IoMOb4q9QGOqUBIiH2%2FwVKd93uKxY9RkyiHKYSSqOgU7OS3c00LIFMhQxxvkmlI%2BKIq%2BeHsQiRpslbRLrbJibeSHYFD6RehR8o9%2FYCdvZ8Ht5af%2B9zzeoCDsKnEwb2qn%2FY%2FNz12ba1qPps%2BbcDYR%2FTPTz7v68bnr9DIINBefB5%2BcfFqI15GqYUBp2cuFMy4S7fIdbjZnwvzZg2%2BDQrbb%2FtmTlO3fmZNqa3BgHmjHKb&X-Amz-Signature=c643bc8886ae7f36f3fd06e0d883eb54ef25252e74878a8b675fee7af7690a55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCW2CEKU%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T161150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIER7aFhU4cTBSKrbh52REqJKRBYaDUzi6lgEt3vYHlLTAiEApvMkW5vzDFuGMKQqpdoRPpboDhNA4tdv4RWNsYKM81EqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1ODMPvvpoJsyTYVSrcA7MiVaH%2F5gCl7j1cQbMs3%2F5bxiWZpCgaOONUlDFfgP%2FaoIwsj25yLRBy6nuqnYp3T5FfPooIgKR3J3mJVAPswrWA69JwLk8eQ2lJ90EtAjydvnUFjDVi6R0csZohUGlggt1%2F1GSrFlk7zrSX9YgAGWDA%2F54G7yPYFXC5KLGPOrkAbia2nWEjlM6cIiPkGwR90Qggxyuv2jPr02OoOJVCdLuBJ9CmG6zcRY%2Fj3AMRnbTdPNiZUoW2CgP7ShNNkyoHQ1eSKqaDTOROZNBNZQoTc4a2WGQ8LBNpvS4qe9OEcHNA%2Be8NSYV2j9ephUuOrZ4%2FjV6JqxNzdrsfkZPRJYIrOd5hkpIhqZBxFjBjY%2Fa9RtDqkkl5AEEWAdkEHezvHipvHlVMIXVnsje4l%2BZ7vgM9rvJX9Zs91lgJQMXc1N5RwIJr9MO8B5FC3ZTwEedbdLrXKDCFZuSi9pbLGT9YZz4uEIitY1hLUl048Xn6Ds2tbyZTLEvuWng92HaUThCk9J6StWuze2SLCHIGrMKF%2BbkZZHp%2FxQew0pE3frWPpXON5C01IJoV5idXfyISLvCDkoXhscgAWargJbN%2FPoPmPegDEWUsq5OYFHR3RLyL58NFZbD0LiO0Ev7Jjer9C4IoMOb4q9QGOqUBIiH2%2FwVKd93uKxY9RkyiHKYSSqOgU7OS3c00LIFMhQxxvkmlI%2BKIq%2BeHsQiRpslbRLrbJibeSHYFD6RehR8o9%2FYCdvZ8Ht5af%2B9zzeoCDsKnEwb2qn%2FY%2FNz12ba1qPps%2BbcDYR%2FTPTz7v68bnr9DIINBefB5%2BcfFqI15GqYUBp2cuFMy4S7fIdbjZnwvzZg2%2BDQrbb%2FtmTlO3fmZNqa3BgHmjHKb&X-Amz-Signature=581b32889dcaf3eadbd4d5b7b8ae1c1bf9a1e2172212af6a5bf55af6df4a8366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
