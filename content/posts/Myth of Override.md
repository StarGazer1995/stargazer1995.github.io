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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KQES3O%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T201413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIvDpR4moLI4sM8rb3dsPeL%2BqD4r%2BmhrI8%2FutyD1ou4gIgPpN7VM44AcWnb%2B6OuQbASyraMfMzkTppA23xeYWL0toq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDM0H3KjPKMhWmaTSDyrcA3v0wY2sVgvCz3Ix2FCO%2FeEXm20sXAGnJwgNUXQzJtQ45hcP2H9Ywm2O07INDDudH%2F9rJtYGVrZZA98r2Imqi7ACyYFP7LF3kBN3VL2jZO054z7gJZstSSvvIT54jkuJH4XE316k%2FJ9ey5nj2S9XnFrGMEPrtFouN8CkDWtLxpZZnCh5WR4MbFr71E8emA1EOUK7SyVRbpoGn1S44xEaYs6fbPP5E5zSZnTHhGRGj%2BG5gwDSws1iWBA9VZa1qTmtsf4FTeGuyqmSDGT84AMXWSYXW2RTDTUBtwULvvgScH%2FMluHSZWwRrfrpx28uu2iNQ2VwiwM8pROKpSFMAcfRPq6wRYrcywtO%2FB2qmYSJme1HFzaMkPgJEb6x%2FKIGO8JO0my3Yu8nUqy9MYmwENhuJ9T4L%2BP%2BsDTnLFRpINiO0AsXZfBFyiunByOKPazby%2BN51n0luPQuASVbZnJVdMe7EF1TQqjZgI1Cv9dflx8sEwax8EYKrokC0hHc86u%2F3o%2BgqJyIwn5HtojJh2DkRazKDzUlBEJwfzQs3w9enlLObvV7Z5fE589i5dgjg0s2wU4xvvXG3cMXUnQlD4I9i8ravKqwY8%2FAYhrTtFvuKcemUSU0MDUj2wOuQcQ4OMuMMMWpjdQGOqUBDBKpIK6ev3bxHWmCSoUXV0qfkB96vKPu2kokZJhhqp5TdH%2B%2F8NgZc%2FKTWGMAKZqY1FyFwgNUFajxkcLZE0td7Uo8irLUonjG%2BzV6M9hMYy113zJ5PZppHm4IG5%2Bqkju8WB1kivkMD0wYDWFpTCvVa86ul9gnYHqnJSAEDawy59tduuDjr8dGU0kl2utoMsM34j14rRiBvhtOeRN8CBM%2BrkenwIIv&X-Amz-Signature=5145c208cd30d40859713ddcdc44c0b12c8d920f4dc27eb0759dcd212e0de812&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KQES3O%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T201413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIvDpR4moLI4sM8rb3dsPeL%2BqD4r%2BmhrI8%2FutyD1ou4gIgPpN7VM44AcWnb%2B6OuQbASyraMfMzkTppA23xeYWL0toq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDM0H3KjPKMhWmaTSDyrcA3v0wY2sVgvCz3Ix2FCO%2FeEXm20sXAGnJwgNUXQzJtQ45hcP2H9Ywm2O07INDDudH%2F9rJtYGVrZZA98r2Imqi7ACyYFP7LF3kBN3VL2jZO054z7gJZstSSvvIT54jkuJH4XE316k%2FJ9ey5nj2S9XnFrGMEPrtFouN8CkDWtLxpZZnCh5WR4MbFr71E8emA1EOUK7SyVRbpoGn1S44xEaYs6fbPP5E5zSZnTHhGRGj%2BG5gwDSws1iWBA9VZa1qTmtsf4FTeGuyqmSDGT84AMXWSYXW2RTDTUBtwULvvgScH%2FMluHSZWwRrfrpx28uu2iNQ2VwiwM8pROKpSFMAcfRPq6wRYrcywtO%2FB2qmYSJme1HFzaMkPgJEb6x%2FKIGO8JO0my3Yu8nUqy9MYmwENhuJ9T4L%2BP%2BsDTnLFRpINiO0AsXZfBFyiunByOKPazby%2BN51n0luPQuASVbZnJVdMe7EF1TQqjZgI1Cv9dflx8sEwax8EYKrokC0hHc86u%2F3o%2BgqJyIwn5HtojJh2DkRazKDzUlBEJwfzQs3w9enlLObvV7Z5fE589i5dgjg0s2wU4xvvXG3cMXUnQlD4I9i8ravKqwY8%2FAYhrTtFvuKcemUSU0MDUj2wOuQcQ4OMuMMMWpjdQGOqUBDBKpIK6ev3bxHWmCSoUXV0qfkB96vKPu2kokZJhhqp5TdH%2B%2F8NgZc%2FKTWGMAKZqY1FyFwgNUFajxkcLZE0td7Uo8irLUonjG%2BzV6M9hMYy113zJ5PZppHm4IG5%2Bqkju8WB1kivkMD0wYDWFpTCvVa86ul9gnYHqnJSAEDawy59tduuDjr8dGU0kl2utoMsM34j14rRiBvhtOeRN8CBM%2BrkenwIIv&X-Amz-Signature=3ebe135d2a3dfc2ffbffe8814d3b7169a9f0fd3df107a9d2ba4809820d8b376c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
