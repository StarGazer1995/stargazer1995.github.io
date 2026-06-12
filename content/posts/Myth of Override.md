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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQIZL367%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T230710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDTqQafL%2FXBI%2BqGI%2BVZCG447ferH%2FCJIG4smPi0NY7N%2FAIgYJyRlE2tTjWg4TFs6aKDF1sI2RhTUBIL1Rdl1re10z4q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLXV0pqOnVeXDv0XUircAy8o2IJgceHmX0nCmQQ4Be9duK9iGR%2FY9fkii4ZmjXuAH4BPBjBdjz8YCAAHzUlX9KKYbl8dJLQ0H%2FcMVlZTzn9STGp2ftznoQmQr%2BYwqSQUMnn77XNLgVKMAik7Hq5N87EiqEzpEM38HSyTIf8vf1D39lo4sa8npBq514jB%2BEkVkrz24ILQTmljw%2BLulfw8Xbnpih0oLUgrA2lXESo2JAplW%2Bqxy%2FEVLRNwC5coYZNPP41XNdlE1kjgvov146SW1gswWf5UClASpwQg1CxYR4X5D8jZ5RMubQLF2FqgCzAzzvFMA%2FKDTMdpNwDzkbvZGfIUDtSRi1lXfbnekA9JhF0zazzuNOIzxsRNdoW4nX%2BvAu8jEfkCi2Vf56AIe1xaalYCLU8gtbw04BCP3jaJDdHPzZZYnZcouSeRBfzAkwvryNX4UmdqFzOeQJFyU9pkkNWLzU7GunWTpIFQRQp64aQ1csO6y34lluIy1Lsd%2BQHC478i4hwqQNJTqEjv8D69zGuDaXOcexDd%2F1ksM5fnG6Vek39HS9Ala2ymDshGxCKAaXC11vl94gol%2Fb4hP5PDALoDCFnoopmiagDb1%2BWQaAs8FmErOT7SPXk4HUVShMkXoKlJ21C9U8gVXKcYMI%2BXstEGOqUBuhsvl6ZEWiDb4ONRMENsUceoHgJugIt1nOdJZqbZa2LZWQzGJfT6KYj9GQv71wEA3Q%2BNDC%2FUSkxToBp0vIwWYhzS9J5vEAhnT%2B4v3jhmBTDBnalXGYdPUdrpD1VVFnihubFvCfx1C1rJ%2BRbCvDafItcoZo5S0uQqwHiKs0lFip%2BqfGUBOCim3UILnBqvvvcwvXD0m3VdfPgde6jAMIAB0GeYTv3Z&X-Amz-Signature=96d53cec319c0356a58d2026c9cc2c84b015f68fd65b62a224cc3cb39b88c8a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQIZL367%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T230710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDTqQafL%2FXBI%2BqGI%2BVZCG447ferH%2FCJIG4smPi0NY7N%2FAIgYJyRlE2tTjWg4TFs6aKDF1sI2RhTUBIL1Rdl1re10z4q%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLXV0pqOnVeXDv0XUircAy8o2IJgceHmX0nCmQQ4Be9duK9iGR%2FY9fkii4ZmjXuAH4BPBjBdjz8YCAAHzUlX9KKYbl8dJLQ0H%2FcMVlZTzn9STGp2ftznoQmQr%2BYwqSQUMnn77XNLgVKMAik7Hq5N87EiqEzpEM38HSyTIf8vf1D39lo4sa8npBq514jB%2BEkVkrz24ILQTmljw%2BLulfw8Xbnpih0oLUgrA2lXESo2JAplW%2Bqxy%2FEVLRNwC5coYZNPP41XNdlE1kjgvov146SW1gswWf5UClASpwQg1CxYR4X5D8jZ5RMubQLF2FqgCzAzzvFMA%2FKDTMdpNwDzkbvZGfIUDtSRi1lXfbnekA9JhF0zazzuNOIzxsRNdoW4nX%2BvAu8jEfkCi2Vf56AIe1xaalYCLU8gtbw04BCP3jaJDdHPzZZYnZcouSeRBfzAkwvryNX4UmdqFzOeQJFyU9pkkNWLzU7GunWTpIFQRQp64aQ1csO6y34lluIy1Lsd%2BQHC478i4hwqQNJTqEjv8D69zGuDaXOcexDd%2F1ksM5fnG6Vek39HS9Ala2ymDshGxCKAaXC11vl94gol%2Fb4hP5PDALoDCFnoopmiagDb1%2BWQaAs8FmErOT7SPXk4HUVShMkXoKlJ21C9U8gVXKcYMI%2BXstEGOqUBuhsvl6ZEWiDb4ONRMENsUceoHgJugIt1nOdJZqbZa2LZWQzGJfT6KYj9GQv71wEA3Q%2BNDC%2FUSkxToBp0vIwWYhzS9J5vEAhnT%2B4v3jhmBTDBnalXGYdPUdrpD1VVFnihubFvCfx1C1rJ%2BRbCvDafItcoZo5S0uQqwHiKs0lFip%2BqfGUBOCim3UILnBqvvvcwvXD0m3VdfPgde6jAMIAB0GeYTv3Z&X-Amz-Signature=d55e1e326f03038f3c25907a0be80973b6658c1af51788280336c61203f715e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
