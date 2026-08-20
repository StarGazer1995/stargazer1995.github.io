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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2QJOOXV%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T164507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkNR1pVJdpfEezC6p6edQf%2FDASgDj1qNsfZONQ0m930AiEA7RTm798NnehG71PXbs0wDno5Uc3nehX2NFvydmtYzE4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO44so5aSb9oTu2DCCrcA3Qao0LV%2FRyMv4NXIurJtMNPtEP86KJK%2B7FdhKl5rEdgYWC%2BH7AeZuOVROGZ%2BxuJM4IpZqINmaPqwliUTg4gIaHsRCkLjBv6j1mzHj9KqN7hAbw9ZMe628tl%2FEGT2rc78bmf%2BaLItLUE7pfJnPHHn7Mznfb83EfD5s%2FcjajvIBFkKF1xmD36YMVS7HaUnYAeRSI7Lsi5N4fHyaCMq7bM7Al7EIuufsyGrxAFLUhlNr1va4sZ2pZaDerRyI%2Fdkj0M5TXLPlip3t3nY2oqxiPehdSlbQx6f5PlHH60faADNBC%2BCGCM5FqA75hzvAxhQFDRSBULS90tG5X2jQlM%2FPtaWKXp3cjC%2BO5myr%2F5y5xH3XZg%2BuK69aeepfkCF7QcgFOk9pdgG%2F%2FF1FYqZl4BhHrGt3Y7FftVyhPXW5FNwOVA5xinerFqgbL%2BSCWEcn7cpgGMeJuk1CZZJBpqIgFOHzUR1Lm30KkwIMpeC9Ool76GnR4e1qI%2FgPWS2Z2Kj0Y4FjrI8%2FDMKOF4kNbLhDX7nF5HVs5pwrWys8LrcMXcDyLUCL9UnK05eDUYaT8Iiwe0EF%2BhFxksw%2FBM%2Bb7UzPiDQxr9xipB4Y%2Fkki3r72k7CoWR9xWh4nO89lUIsNw%2FH8vxMPGrnNQGOqUBDXf9%2BT6NyW%2BIbluJFyDH5tE1mzwdxywFczEfLvlffmXoP3p2KBPQ8moBtXbW2O8orcXzfk22v%2F8pvtr7hIlHXJVEplJquX3Z9vmrMcToLTCxz1%2BrtVw6AY6IZOojJbXE8m57Ou%2FoKZlofatOESuiTGDZsOI33X1yPSVX%2FgmqjHV%2FofJ5pwxA7vCK4crrzcKEt5k5RQ1VVpmnxd7XlWjQ40QOqZas&X-Amz-Signature=71b5743549c8b0edb68cc71db8f5c70c2dcf2698b8bbdeab0fdbd99db038db76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2QJOOXV%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T164507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkNR1pVJdpfEezC6p6edQf%2FDASgDj1qNsfZONQ0m930AiEA7RTm798NnehG71PXbs0wDno5Uc3nehX2NFvydmtYzE4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO44so5aSb9oTu2DCCrcA3Qao0LV%2FRyMv4NXIurJtMNPtEP86KJK%2B7FdhKl5rEdgYWC%2BH7AeZuOVROGZ%2BxuJM4IpZqINmaPqwliUTg4gIaHsRCkLjBv6j1mzHj9KqN7hAbw9ZMe628tl%2FEGT2rc78bmf%2BaLItLUE7pfJnPHHn7Mznfb83EfD5s%2FcjajvIBFkKF1xmD36YMVS7HaUnYAeRSI7Lsi5N4fHyaCMq7bM7Al7EIuufsyGrxAFLUhlNr1va4sZ2pZaDerRyI%2Fdkj0M5TXLPlip3t3nY2oqxiPehdSlbQx6f5PlHH60faADNBC%2BCGCM5FqA75hzvAxhQFDRSBULS90tG5X2jQlM%2FPtaWKXp3cjC%2BO5myr%2F5y5xH3XZg%2BuK69aeepfkCF7QcgFOk9pdgG%2F%2FF1FYqZl4BhHrGt3Y7FftVyhPXW5FNwOVA5xinerFqgbL%2BSCWEcn7cpgGMeJuk1CZZJBpqIgFOHzUR1Lm30KkwIMpeC9Ool76GnR4e1qI%2FgPWS2Z2Kj0Y4FjrI8%2FDMKOF4kNbLhDX7nF5HVs5pwrWys8LrcMXcDyLUCL9UnK05eDUYaT8Iiwe0EF%2BhFxksw%2FBM%2Bb7UzPiDQxr9xipB4Y%2Fkki3r72k7CoWR9xWh4nO89lUIsNw%2FH8vxMPGrnNQGOqUBDXf9%2BT6NyW%2BIbluJFyDH5tE1mzwdxywFczEfLvlffmXoP3p2KBPQ8moBtXbW2O8orcXzfk22v%2F8pvtr7hIlHXJVEplJquX3Z9vmrMcToLTCxz1%2BrtVw6AY6IZOojJbXE8m57Ou%2FoKZlofatOESuiTGDZsOI33X1yPSVX%2FgmqjHV%2FofJ5pwxA7vCK4crrzcKEt5k5RQ1VVpmnxd7XlWjQ40QOqZas&X-Amz-Signature=9c6386d196a2c0d5f4301454af4269cbe0c1ce8e5482a73072a03ca1cd3afdc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
