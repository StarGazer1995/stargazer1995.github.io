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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKOSSGRW%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T114725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCUBznb%2BNUvdlSvkBOcCx6%2Fu7wDPhDQt2rC3pPJKPLzBgIhANxUr8CB2ORNSsyMalMsypR0yXWdS7JHhmLhE8mohBnZKv8DCC0QABoMNjM3NDIzMTgzODA1Igzx%2F4kioOEu7i%2B18IEq3AMxVVeB%2FQfi%2BvEQhW%2BKbge%2B0OPKafLcXEM2lms0hW4%2FFfh5HnSgpTLDsa0R4Nwt6C%2BYewQFj9MRnPySaIzajqP%2Bt%2B39F9eVaM4Y1G7cJHhfQloCOqAgIYeVfBURz1XiyChHIFRXS7VIG6Z%2BY9NakRswVQ0tKls%2B0%2BL3PR6zpeGghn%2Bvv1w31MoSC49G%2Bniq75zt1uHdAJsDBbtpTnOSazD%2FmvKKlpEbpWT452rHlqJs4MBJUYcLyFrfDA2bas2N75HhxRCKufrYacBaxi0DHIo3crGE%2FELFGm0JAFvX1CLDByq0Qu259mQ9AND644HXEOxPhNckN2%2Fm%2B2rSvAg6j1z9zpBF1Onmp%2FyEChf9Wz2akKFhU6qusu4V2xiN5cqIVsCDjU0J9wwBFIr7OLSRTDSEbaiPlVNljbZ1vOyUh7b6HZVtnSZS8W8oY%2Ffekw2kZZmpA7r8%2FoXWOqihz23JGe0dMF%2BD30vXdE%2BjGbggHEva%2BBgQxFIzUpO7N6aGkLVp2U66TwLk24TzokF2zWOGL2eql1cCZ6Ob2i3TynkxX0mL8e2LvodH7Ecuwa0aM4L%2F4fRMqVqVtuSHdgC1wcOVIWMFlMeDgdoyQcf3KeZMRffw5OQME9QDdk%2B3AddJ6TCenYzQBjqkAU6NRaKvEVL5onYz1mzyickB6NmlxQmlzgIsKm3t1TJHuJfjxhYZznSsJl5FtUUAGIAlF0MrB2SiK%2BBZIjdpDTciPZcVnI46lx2pUQh%2BzS9kS1Kq0Uq1Zsp2qfGN2xVerf5s0paHhExTY9ZdH7zk5zbQjxqog0Gt4D%2FePU3sfNWDDNipMGMSFGzuY9vXbwg2hBFtYWZ5eekXSNOxrKqjBfZcn0Zq&X-Amz-Signature=b2bd2cbfdb5cd2550e8c428e700d5cb9255ae8094ce23d598b3a4e987cd51ea9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKOSSGRW%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T114725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCUBznb%2BNUvdlSvkBOcCx6%2Fu7wDPhDQt2rC3pPJKPLzBgIhANxUr8CB2ORNSsyMalMsypR0yXWdS7JHhmLhE8mohBnZKv8DCC0QABoMNjM3NDIzMTgzODA1Igzx%2F4kioOEu7i%2B18IEq3AMxVVeB%2FQfi%2BvEQhW%2BKbge%2B0OPKafLcXEM2lms0hW4%2FFfh5HnSgpTLDsa0R4Nwt6C%2BYewQFj9MRnPySaIzajqP%2Bt%2B39F9eVaM4Y1G7cJHhfQloCOqAgIYeVfBURz1XiyChHIFRXS7VIG6Z%2BY9NakRswVQ0tKls%2B0%2BL3PR6zpeGghn%2Bvv1w31MoSC49G%2Bniq75zt1uHdAJsDBbtpTnOSazD%2FmvKKlpEbpWT452rHlqJs4MBJUYcLyFrfDA2bas2N75HhxRCKufrYacBaxi0DHIo3crGE%2FELFGm0JAFvX1CLDByq0Qu259mQ9AND644HXEOxPhNckN2%2Fm%2B2rSvAg6j1z9zpBF1Onmp%2FyEChf9Wz2akKFhU6qusu4V2xiN5cqIVsCDjU0J9wwBFIr7OLSRTDSEbaiPlVNljbZ1vOyUh7b6HZVtnSZS8W8oY%2Ffekw2kZZmpA7r8%2FoXWOqihz23JGe0dMF%2BD30vXdE%2BjGbggHEva%2BBgQxFIzUpO7N6aGkLVp2U66TwLk24TzokF2zWOGL2eql1cCZ6Ob2i3TynkxX0mL8e2LvodH7Ecuwa0aM4L%2F4fRMqVqVtuSHdgC1wcOVIWMFlMeDgdoyQcf3KeZMRffw5OQME9QDdk%2B3AddJ6TCenYzQBjqkAU6NRaKvEVL5onYz1mzyickB6NmlxQmlzgIsKm3t1TJHuJfjxhYZznSsJl5FtUUAGIAlF0MrB2SiK%2BBZIjdpDTciPZcVnI46lx2pUQh%2BzS9kS1Kq0Uq1Zsp2qfGN2xVerf5s0paHhExTY9ZdH7zk5zbQjxqog0Gt4D%2FePU3sfNWDDNipMGMSFGzuY9vXbwg2hBFtYWZ5eekXSNOxrKqjBfZcn0Zq&X-Amz-Signature=54fd0664ad014de790d43fdcd6c06455f16ca10144a293eebcbf24b5b8fed774&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
