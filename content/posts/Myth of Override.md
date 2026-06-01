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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QM4BZMP%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T201021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDJs5lfYB8TJkA8Lw5CR57z170uzFJ%2FcHau8UwZTnLClgIgdmBFoOsG3EPGq6cIAPpjGEau8etx4mdfaSLXcfSlbP4q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDEw%2BYwZByEmFirMFHCrcAzlQ%2BS8zUelixbYYWMWpdRJa5vxi%2BoIpDiq91RWzzwcohZLCaJtw5fp8g%2F88fPhyebadBrEO4OJPsChX1QCJYumKgaWkeuhz4fjXjvu2WK8c7ViAiGZ8v%2B%2FhfA9LMSda2XFSDjL4%2BIV74lsY8hEFVK6XlpwkWqF5P4Z1AbQPJ0%2BVf63SnOBubKZFuHBYc2xW7A262Qpq4zyJ0q%2F9R6%2BxOtKMMRhbnb88fqhv%2Bmy2TX7eUksSc2X37XUnTWeD7GAImSBi9NrYge4W7h5Lt1IxjlbO0g9qx8qNzrfXaK2tbsC88LqGuW9zfOdSwnr1GzykBeHlIzl8INPoQ3Hvb6%2FMu47PBl64vnPtXqG%2BB4opkkRkrDu7fKRmPIiR%2FSQXGvPKNrrfril%2FgwiWeTCZLaXWgEAg09iQraeNEnBfhYdr1tFuc5RvUKliAbKi6iWvx8Kaf%2BuBdwqiJxMnmY4ntKFv1bafix54aOZrjJ3AbStDkMz3jfhKYQsN8jPHkwr%2FOTwmki5aBWV5SQP4kRM9kKMmG6wPi%2B1iQiiWgGSW4YxwrfWbM7STrreG%2FnBcYZ6jFQ%2Fija8R%2FgaU6pg%2BTqY61WDY0eaErSeURJAySu7tSd1ADO3n6xl0W%2BnVAKqJG7bvMI6z99AGOqUBvxqWXC2blNG%2FjP08X6v%2BbkuTkvVlTpuZGhiQCuOx1ZhrwqQfMrkCqZtlrUHCoqRz6kabdDHlfh7wi%2FJO0a%2F%2FfXoEwm%2F%2BS2AUKm3mvyIrh42E0haFjsiqH0l3A7umMC3HMWQMYov8QgdZNbMcNYKGSd6Kn47lpi6bbOf6aOeQMlZNA7X4WxDKNhR1%2Bwhgu7s1nE6GhYdqcECpv3BCry2TQWlwzvTn&X-Amz-Signature=c5a05bcfaf68f89e1342aae4db991de8fcbb2f765eb922999d53077aa26ec95e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QM4BZMP%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T201020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDJs5lfYB8TJkA8Lw5CR57z170uzFJ%2FcHau8UwZTnLClgIgdmBFoOsG3EPGq6cIAPpjGEau8etx4mdfaSLXcfSlbP4q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDEw%2BYwZByEmFirMFHCrcAzlQ%2BS8zUelixbYYWMWpdRJa5vxi%2BoIpDiq91RWzzwcohZLCaJtw5fp8g%2F88fPhyebadBrEO4OJPsChX1QCJYumKgaWkeuhz4fjXjvu2WK8c7ViAiGZ8v%2B%2FhfA9LMSda2XFSDjL4%2BIV74lsY8hEFVK6XlpwkWqF5P4Z1AbQPJ0%2BVf63SnOBubKZFuHBYc2xW7A262Qpq4zyJ0q%2F9R6%2BxOtKMMRhbnb88fqhv%2Bmy2TX7eUksSc2X37XUnTWeD7GAImSBi9NrYge4W7h5Lt1IxjlbO0g9qx8qNzrfXaK2tbsC88LqGuW9zfOdSwnr1GzykBeHlIzl8INPoQ3Hvb6%2FMu47PBl64vnPtXqG%2BB4opkkRkrDu7fKRmPIiR%2FSQXGvPKNrrfril%2FgwiWeTCZLaXWgEAg09iQraeNEnBfhYdr1tFuc5RvUKliAbKi6iWvx8Kaf%2BuBdwqiJxMnmY4ntKFv1bafix54aOZrjJ3AbStDkMz3jfhKYQsN8jPHkwr%2FOTwmki5aBWV5SQP4kRM9kKMmG6wPi%2B1iQiiWgGSW4YxwrfWbM7STrreG%2FnBcYZ6jFQ%2Fija8R%2FgaU6pg%2BTqY61WDY0eaErSeURJAySu7tSd1ADO3n6xl0W%2BnVAKqJG7bvMI6z99AGOqUBvxqWXC2blNG%2FjP08X6v%2BbkuTkvVlTpuZGhiQCuOx1ZhrwqQfMrkCqZtlrUHCoqRz6kabdDHlfh7wi%2FJO0a%2F%2FfXoEwm%2F%2BS2AUKm3mvyIrh42E0haFjsiqH0l3A7umMC3HMWQMYov8QgdZNbMcNYKGSd6Kn47lpi6bbOf6aOeQMlZNA7X4WxDKNhR1%2Bwhgu7s1nE6GhYdqcECpv3BCry2TQWlwzvTn&X-Amz-Signature=93ec8e087a08bcb83d5d7c248145399a07eb9f75b23ab5330f11e2d2b4596018&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
