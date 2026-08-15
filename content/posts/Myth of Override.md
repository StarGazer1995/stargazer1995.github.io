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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHRNH2GD%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T081428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIBfxWmbdYFuYCF40f68rb7IaY1jZAWXSHOXi08RS8PupAiEAnR6uynoijM6%2FV%2Bw3qUgiRWJzqU7qb8Mq7w9cn6zA7%2Foq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGbGQfT%2FjEm%2BqCRBjSrcA1lVtrGpVhgfgNW6BOWngz1cAJ2isf69Xb64rFt%2BjoS92F6nVfXFAL%2FOmxaIosxv5Twax%2Fvj3GLR7vV8C%2BcK%2F%2BhWIILpdw%2Fus23xa28fRSyjdiSBBC%2Bq%2BHIw%2F1O3D12AP4f6EJWcsqEoixWxHxDMrvO4Lf1WQpwYR%2FixCKCcHY0molKDOIRQdR6RX719prm03ncP%2FVQEh42ZsLUBHSNTQB%2BOWbtqbAOCohyAm3PuOeUyLPaY5r0sU9mmpixcm1Jj1QKHnIXdOK5G3h824T3RioJ5j0%2FNdxq0leNfo0NAyCXCcYchTP%2BV%2BT3Cl6VFyM1OLzhqOFdQkmVjZtxE%2F8D1HwY%2FS8EGn5Ct9cNJ%2FZ%2F9uKEL0JmiQDsN2d5bjU1uKxFrlgR9lebMV7vk9tklro%2BJaOxFOPq5mw24FpJii%2FTVbDvG%2FpNhcCp04LQ0hjXy2p%2FgoRTO9co%2F2Do7gjOpTTQunVIJemQ5okiAUn4vuYcgYISvG%2FAIehdmCWfTznwpjB0gcyJd2YfYoo51zyQCKedWNRgiVT0zlMbzYl9LWPpklyt1clMXqViYTIUCf%2Bve5dQnlHmS%2BK2jfRaGEZGDuSWAaoqcY0SR9TN%2FM%2FM%2FL24lgM%2BxYJk1xrKb38Lx184bMJm4gNQGOqUBjh6pWL9dZkGiUJHTWdswMguhXl5BJdifcWGf0KIQzz6dHQkwV514NuswQYpeF1nc5ZeriEU1%2FVy45PNrSm4iC0ydDqfQaEt7h2SbqPNH%2B2nD05mTVRjgktY3Plh6bzU6vccGOLYJ1N5xbwc6VC33lpt9JFZGBghEC5I9vAiuhepfLGRtM%2B0X5oM9d47NF4HtMEACFrPvltELaJO4cH4tz%2BeJJMMw&X-Amz-Signature=ba35321c774b10f5b6c00c1cdddbf80ef850075d8427b9c4862b55aff4d3ce64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHRNH2GD%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T081428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIBfxWmbdYFuYCF40f68rb7IaY1jZAWXSHOXi08RS8PupAiEAnR6uynoijM6%2FV%2Bw3qUgiRWJzqU7qb8Mq7w9cn6zA7%2Foq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGbGQfT%2FjEm%2BqCRBjSrcA1lVtrGpVhgfgNW6BOWngz1cAJ2isf69Xb64rFt%2BjoS92F6nVfXFAL%2FOmxaIosxv5Twax%2Fvj3GLR7vV8C%2BcK%2F%2BhWIILpdw%2Fus23xa28fRSyjdiSBBC%2Bq%2BHIw%2F1O3D12AP4f6EJWcsqEoixWxHxDMrvO4Lf1WQpwYR%2FixCKCcHY0molKDOIRQdR6RX719prm03ncP%2FVQEh42ZsLUBHSNTQB%2BOWbtqbAOCohyAm3PuOeUyLPaY5r0sU9mmpixcm1Jj1QKHnIXdOK5G3h824T3RioJ5j0%2FNdxq0leNfo0NAyCXCcYchTP%2BV%2BT3Cl6VFyM1OLzhqOFdQkmVjZtxE%2F8D1HwY%2FS8EGn5Ct9cNJ%2FZ%2F9uKEL0JmiQDsN2d5bjU1uKxFrlgR9lebMV7vk9tklro%2BJaOxFOPq5mw24FpJii%2FTVbDvG%2FpNhcCp04LQ0hjXy2p%2FgoRTO9co%2F2Do7gjOpTTQunVIJemQ5okiAUn4vuYcgYISvG%2FAIehdmCWfTznwpjB0gcyJd2YfYoo51zyQCKedWNRgiVT0zlMbzYl9LWPpklyt1clMXqViYTIUCf%2Bve5dQnlHmS%2BK2jfRaGEZGDuSWAaoqcY0SR9TN%2FM%2FM%2FL24lgM%2BxYJk1xrKb38Lx184bMJm4gNQGOqUBjh6pWL9dZkGiUJHTWdswMguhXl5BJdifcWGf0KIQzz6dHQkwV514NuswQYpeF1nc5ZeriEU1%2FVy45PNrSm4iC0ydDqfQaEt7h2SbqPNH%2B2nD05mTVRjgktY3Plh6bzU6vccGOLYJ1N5xbwc6VC33lpt9JFZGBghEC5I9vAiuhepfLGRtM%2B0X5oM9d47NF4HtMEACFrPvltELaJO4cH4tz%2BeJJMMw&X-Amz-Signature=7746e0d5bd224c9b0ca61e338217ea2ed375df8e8fafeab30dbd57a978bb18df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
