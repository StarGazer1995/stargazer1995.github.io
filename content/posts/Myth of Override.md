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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVJY57NG%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T045217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPzSFpOxtYYQyzsqUIKwNFE5DpYAl7wgU4kenppXy%2F%2BwIgIyXcWjbBSIw03Ulsh5nHcnZSs55NuJDJ5iEhO4kg6E4qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3XuWoN21eIA8IwuCrcA4rv7KnNTOg3u%2B%2F%2BHyPOTHk4vPas%2FFpZI41DDKm3Zr2muC3sDN%2Fz7LtSMXbjPXW2sUPqR1r3w57UGOEHcBiBWiwQs1%2F3y0%2FnGsmmlSK08qn%2F7gbcyTQ3xM4359zA%2BNwz%2F6fQuTNPxPTRRHCL71MfnkTFVYHp9aBROesYwYmV%2BBOZoqm9olYFijEg%2Fet2lke1PveKHgwcyae%2BTJ02yO0cN5pYVeSntfucBMrmjGQBJ9a%2FVFzfEZR5YaGHPVn8Haw0YgpVQ4VgFKJHjeV9tvDkknxIFR4Vccxn4YIDREx2Wy1Au00adS9qLrehu5wDncUdFyLrhvCSWYyZDASM6yl%2Fzc891UlWtyF58Jmc2JOnYsZkWVsS%2Br0Xka%2FNzaPaw%2B5TvgEInNUIWXi4c1IE9pL%2BaQOw0wWmKMdJNXZgy4yuPYP79sOldhrtmuwxBZZOqNRsrgRLRjNRxs9pGOrqBMgqMqphA6d30VKweaKEP6XB4ga%2Bfz8q3M9ptjrdka9zkA06yE9GxC5UL5zPV1V%2BpkSjC7NLAmYwyuu78D3lpgUit5IFoBy3blBYc7eO0r8QI3Zwe%2B7MhMjCrERalf0SQtXXAHYAakNy1r6EjFa5yV%2FhOava2%2FgB7QoWyudUnfH7MKPNxtIGOqUBdIxYdYWzBXVc2DXYBziLc4IOREr9g6%2FgS%2BZ6%2FVj33wZuHIB793CM74KcYBs9o9wNrMfKTdG5gwUj65VOXQKoMy4B294jItKfyjH2Y2xjo0acaJrIpl0kN7xtP8S8lgjupmsuu1k7NhOajjKQZUDra1KXup1Gn%2BcmKbAHM0Y7%2FHWZ5DUtarMxSk9z9ntNQ7n74l1T%2B0a9shGFufztqvmuz1VAWX%2F5&X-Amz-Signature=5745341345e2ad33b87cca195f55c3e43720c5d456b5c07c14fb19eb1cae4c96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVJY57NG%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T045217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPzSFpOxtYYQyzsqUIKwNFE5DpYAl7wgU4kenppXy%2F%2BwIgIyXcWjbBSIw03Ulsh5nHcnZSs55NuJDJ5iEhO4kg6E4qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB3XuWoN21eIA8IwuCrcA4rv7KnNTOg3u%2B%2F%2BHyPOTHk4vPas%2FFpZI41DDKm3Zr2muC3sDN%2Fz7LtSMXbjPXW2sUPqR1r3w57UGOEHcBiBWiwQs1%2F3y0%2FnGsmmlSK08qn%2F7gbcyTQ3xM4359zA%2BNwz%2F6fQuTNPxPTRRHCL71MfnkTFVYHp9aBROesYwYmV%2BBOZoqm9olYFijEg%2Fet2lke1PveKHgwcyae%2BTJ02yO0cN5pYVeSntfucBMrmjGQBJ9a%2FVFzfEZR5YaGHPVn8Haw0YgpVQ4VgFKJHjeV9tvDkknxIFR4Vccxn4YIDREx2Wy1Au00adS9qLrehu5wDncUdFyLrhvCSWYyZDASM6yl%2Fzc891UlWtyF58Jmc2JOnYsZkWVsS%2Br0Xka%2FNzaPaw%2B5TvgEInNUIWXi4c1IE9pL%2BaQOw0wWmKMdJNXZgy4yuPYP79sOldhrtmuwxBZZOqNRsrgRLRjNRxs9pGOrqBMgqMqphA6d30VKweaKEP6XB4ga%2Bfz8q3M9ptjrdka9zkA06yE9GxC5UL5zPV1V%2BpkSjC7NLAmYwyuu78D3lpgUit5IFoBy3blBYc7eO0r8QI3Zwe%2B7MhMjCrERalf0SQtXXAHYAakNy1r6EjFa5yV%2FhOava2%2FgB7QoWyudUnfH7MKPNxtIGOqUBdIxYdYWzBXVc2DXYBziLc4IOREr9g6%2FgS%2BZ6%2FVj33wZuHIB793CM74KcYBs9o9wNrMfKTdG5gwUj65VOXQKoMy4B294jItKfyjH2Y2xjo0acaJrIpl0kN7xtP8S8lgjupmsuu1k7NhOajjKQZUDra1KXup1Gn%2BcmKbAHM0Y7%2FHWZ5DUtarMxSk9z9ntNQ7n74l1T%2B0a9shGFufztqvmuz1VAWX%2F5&X-Amz-Signature=72ca9b319583ec289558dd2c7d72356738ce3823530533c1bd286c8f25901b19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
