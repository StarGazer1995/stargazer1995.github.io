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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOOYFD5Z%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T204803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlwvpoVjQYJPNzqKqLrl4xpT2g8oqLXmbHH%2BZPOsCsxAiEAsnHyGwQV5ARurZGXnf1DMLM%2BdF4cfnmVnWxliy7rz74qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdFxssn%2F%2FKrwBNj4yrcA5zClknUqXw6ighniR9PNmQ82GejeH%2B1qZZdLjrVJ9XR7uf2wxtnIo50arRoQhqA%2B35qcp5GoJUGn9P2vg8H5PfgiCFF%2FfsFXt5PbumzvdZyX8aoJYoIjMbY%2FocLU%2FNPpRMSO4lg8ciaRghupSASOjsP5XZOEEjEmD56rpzA6YDxI3afFz%2FwN1pk%2Bqx1ssjLCvuh22aBLV4aA6RFs%2BWLEiNTIls15b0WikmYbCM8fpOmnEpAjGHw6fxAMZtSeNsgUstneez3s5gS6lN43f6vr7msEWKgczIsPMLgAmnkqGH%2Bpoo%2FEEI5NKbll7Dwk6H58g%2Bymr4fNB9QP%2FFMguDnd1PjdKMN%2B%2Ba3WIOr5pjjaUOkNg0GqixZuaqA9CnfEq6AzObMF0sC40hybbEudv6IneY1Cw%2F1UaCeYzYJS%2F%2Bif7mJ6jFVSkR0pDy%2FVa4t%2FXfp7Bx%2BUvmrSpQiyBTEoMC5bFycZcwS9IzFNjUZbHGX%2BXd83RNjpLV7TiMg5jRyZG1lWV8qaD3nKHJ%2F8TDHQqOJNSt7wMv44PNq7iVg28Fyu8Jzojgd4Cu1EroaEH4BG8wlqVKyEEFvA04xnVeqbOJTQMN%2F9n3k1sPvWPy9TFV9z6bJlwiTrO47qg8Yz5eMMPObgNIGOqUB1hxGoiwLzyPrY5Lgwr1J59KDM3ui9aNKq4Exoecda9KUN6pACo0zHj1Ljtbt%2FtjVauy8NjBkPLROSqCPqv8DojMs%2BLuMHDdC7WYzu8yG0MLqvrGDPLX2G6CAss1%2FetFg6VW5UkBzTcWekoI%2B%2BvKD3smGM%2By506Nwt5rISQ5wua%2BVGd%2BACt8XSK7GFkrPFoUfIFmPF%2BNBdiurqHOaVLJZhpgF2Cy4&X-Amz-Signature=d7d613d81a86af41c918084f66d8effe600593da10a80f7c24bb5e0c62f4a1ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOOYFD5Z%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T204803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlwvpoVjQYJPNzqKqLrl4xpT2g8oqLXmbHH%2BZPOsCsxAiEAsnHyGwQV5ARurZGXnf1DMLM%2BdF4cfnmVnWxliy7rz74qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdFxssn%2F%2FKrwBNj4yrcA5zClknUqXw6ighniR9PNmQ82GejeH%2B1qZZdLjrVJ9XR7uf2wxtnIo50arRoQhqA%2B35qcp5GoJUGn9P2vg8H5PfgiCFF%2FfsFXt5PbumzvdZyX8aoJYoIjMbY%2FocLU%2FNPpRMSO4lg8ciaRghupSASOjsP5XZOEEjEmD56rpzA6YDxI3afFz%2FwN1pk%2Bqx1ssjLCvuh22aBLV4aA6RFs%2BWLEiNTIls15b0WikmYbCM8fpOmnEpAjGHw6fxAMZtSeNsgUstneez3s5gS6lN43f6vr7msEWKgczIsPMLgAmnkqGH%2Bpoo%2FEEI5NKbll7Dwk6H58g%2Bymr4fNB9QP%2FFMguDnd1PjdKMN%2B%2Ba3WIOr5pjjaUOkNg0GqixZuaqA9CnfEq6AzObMF0sC40hybbEudv6IneY1Cw%2F1UaCeYzYJS%2F%2Bif7mJ6jFVSkR0pDy%2FVa4t%2FXfp7Bx%2BUvmrSpQiyBTEoMC5bFycZcwS9IzFNjUZbHGX%2BXd83RNjpLV7TiMg5jRyZG1lWV8qaD3nKHJ%2F8TDHQqOJNSt7wMv44PNq7iVg28Fyu8Jzojgd4Cu1EroaEH4BG8wlqVKyEEFvA04xnVeqbOJTQMN%2F9n3k1sPvWPy9TFV9z6bJlwiTrO47qg8Yz5eMMPObgNIGOqUB1hxGoiwLzyPrY5Lgwr1J59KDM3ui9aNKq4Exoecda9KUN6pACo0zHj1Ljtbt%2FtjVauy8NjBkPLROSqCPqv8DojMs%2BLuMHDdC7WYzu8yG0MLqvrGDPLX2G6CAss1%2FetFg6VW5UkBzTcWekoI%2B%2BvKD3smGM%2By506Nwt5rISQ5wua%2BVGd%2BACt8XSK7GFkrPFoUfIFmPF%2BNBdiurqHOaVLJZhpgF2Cy4&X-Amz-Signature=4bf186133433923ec13ec12af3883f8d45580371d8a31349fefbe7ecd117d45c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
