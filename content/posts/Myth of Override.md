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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPX4AFXN%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T125410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCGAQmBNuMDCS4xq5za%2BATRLWA%2FPdP0L1ke2JjHChYuWAIgVnGVGLsKG810E99sKEuLEQpJEU062wyRKrfSoJGlMzwq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPUnZvLqKWMthtvwmircA1oJVxsT%2B5UtRQ%2BqP21LI3dRe9X88CK1wzdE3e9XJxHeG3OlAJHAr5X3vqJhLyLD1g8pjwiH%2F0MHGKFpyAzrC7%2FcjvGZGMqsSPsiz%2FQnz3J9YFErmcMI4HeL0GyqGyXmE8GKfPUU2zcBdQpLI%2FEbSeKYGAFtmtgkbHWHc9VbZOl6zxAwFO5akjF%2B9gY%2F1BcnspXgbuhMFxoqoaoLf7UOD65GN1ic8sx8Jk4mMHbVw8oiEnmDaeVxebOqs%2Bay5qBrfLt4cJI0nWEybPWM5S%2BcEZNKNAfrUJv3RYKIckEYkFbkH%2FEfLQnskr%2BAObQ9ib%2BY3tRqCa9oslevKHXaGk1wnCIf0n3bi43nlOgEWlkyJFQTgimmPdE8RoC8NFZC3Of%2Fz%2F9paAYTzLyXwmUB6rKsY0u780k%2FuWlyVc2xJV%2BFvfsZNCEP79SrmjR0hCVlo7HSKnryVSsFq6OgRVD34nVYjv3lkgy7GY8NBiiWiL%2B12C8YU5OpYZX9c9GhkoK1jbwCR8rhv94jG17Cp4SZitL9w58xo%2FmpGIczzsBE41EMQ8t%2FL2lCbziuJ7mHQH46t7iFljFk1YF7m1HrBMC2CRKUVFG%2BbEgdMdGLwOE0F5F9u%2BkDaaRWj79v3oSgxU8zMOXIl9MGOqUB5pL%2B4Emjy3kvc%2FBdY25prDAiHHV3b75XO3lhxBsCeMacqai9oPxhCg2fgaBEScDjzAf6rtXhUfBZEJQql5cU1hFWPeNCNjgMedw6a7uzTnIj419ZHKWmMX%2FreR9y4%2B4Y5D3qTJfZcxMH6%2B3ZUpsHCagjGsWKeBz1WFHTGKc2bnp7li0IP6Rcrri3Clp%2FjXU7YFlPfosAruusZhBweZNXxDUNpGAx&X-Amz-Signature=88b3e42a6f87ac9e9bf039fa6dd6e17b53d279e284b75da68f485869db417599&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPX4AFXN%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T125410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCGAQmBNuMDCS4xq5za%2BATRLWA%2FPdP0L1ke2JjHChYuWAIgVnGVGLsKG810E99sKEuLEQpJEU062wyRKrfSoJGlMzwq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPUnZvLqKWMthtvwmircA1oJVxsT%2B5UtRQ%2BqP21LI3dRe9X88CK1wzdE3e9XJxHeG3OlAJHAr5X3vqJhLyLD1g8pjwiH%2F0MHGKFpyAzrC7%2FcjvGZGMqsSPsiz%2FQnz3J9YFErmcMI4HeL0GyqGyXmE8GKfPUU2zcBdQpLI%2FEbSeKYGAFtmtgkbHWHc9VbZOl6zxAwFO5akjF%2B9gY%2F1BcnspXgbuhMFxoqoaoLf7UOD65GN1ic8sx8Jk4mMHbVw8oiEnmDaeVxebOqs%2Bay5qBrfLt4cJI0nWEybPWM5S%2BcEZNKNAfrUJv3RYKIckEYkFbkH%2FEfLQnskr%2BAObQ9ib%2BY3tRqCa9oslevKHXaGk1wnCIf0n3bi43nlOgEWlkyJFQTgimmPdE8RoC8NFZC3Of%2Fz%2F9paAYTzLyXwmUB6rKsY0u780k%2FuWlyVc2xJV%2BFvfsZNCEP79SrmjR0hCVlo7HSKnryVSsFq6OgRVD34nVYjv3lkgy7GY8NBiiWiL%2B12C8YU5OpYZX9c9GhkoK1jbwCR8rhv94jG17Cp4SZitL9w58xo%2FmpGIczzsBE41EMQ8t%2FL2lCbziuJ7mHQH46t7iFljFk1YF7m1HrBMC2CRKUVFG%2BbEgdMdGLwOE0F5F9u%2BkDaaRWj79v3oSgxU8zMOXIl9MGOqUB5pL%2B4Emjy3kvc%2FBdY25prDAiHHV3b75XO3lhxBsCeMacqai9oPxhCg2fgaBEScDjzAf6rtXhUfBZEJQql5cU1hFWPeNCNjgMedw6a7uzTnIj419ZHKWmMX%2FreR9y4%2B4Y5D3qTJfZcxMH6%2B3ZUpsHCagjGsWKeBz1WFHTGKc2bnp7li0IP6Rcrri3Clp%2FjXU7YFlPfosAruusZhBweZNXxDUNpGAx&X-Amz-Signature=a852e24e40261f6bb17290d4cc0d0b8629901706f11de8ffc2518632f4877568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
