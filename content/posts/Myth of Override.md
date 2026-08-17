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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFF7J33M%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T141719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCICu%2BIEr%2BwxAxIeR7fs%2BIaGXVSSQ3yPVjFpJ4%2BsxYCZDmAiEAiT3Q1rttAYXEETSRqyM3DqVpSbtUSdHZwA1vByUOgqkq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDH8H%2BDGmfH%2Bxz7ZizyrcA9r9AUtA2vheje%2BlpCb0Wm6JdW5Rl8mY72HTv5UU0XYv7Kf5U3uhnildBNU%2BiSpdjc9GEZUVv5KCVP3azic1e%2BMqOiX1n9NiQNhwT7GF658eWr9CTCJVVVh2iTakae1a2fsESqenbKzPTxwOqLygFSAmuumzNKXl2CDsxIiV1fBUoVmZzt82Z1dx5zB%2Bafs7OgLClndv0F4sRhZzYyCDHtw93sBm2mUMZelcYg6GNd57W2sp4vxEnSoPCsQVEhd9UW34hT3ODtG%2BmKDSN6IsIJgswuruIeO6NL8%2Bdci32cAwSwGFBrimLFBpw0g34zkYXYLZq7sBwja7VMS1ktTmUo9TjGV2R1kwEo45RoI1Q8hjxMHGzbzJX2QdL352YNgnNCKloyrSWBgrCyif9emPrXj24ofVt2LUt4ZYci56NyFiO%2B27k0XbNd2hrWzd2tDvYBDsW2foGjVTVPf0xlhLkGVRfcIkUAssqTmI2DmutOM4niDjqz4MHURZ7RbldL1VTli2hkKuqlgeH4%2BW38yM28SXNmOhsW8k9YfxBjY1IimCDW5NfJpD35JtG%2FXj9vx0JYvOI9uwp83lAXOwx9hqsLbm7L8oQpOKtU5NcB8ncqUe9nidLv0a7BNkl1MqMIf5i9QGOqUBnAJ5gBPFa%2FZDK%2FH5pf43j8OyEWCZ1AzFriJqZW9VP6v64X7Dc1U23c9LOfLUuRq1Mknz9W%2FaQ2nQjWRjsLHg5FMCFE17paLBKhy%2B0244ZQeE28D36kPJYDGF8QJy7G8vAPmm%2FZZgLgekFCX0%2FuFRrvSSaTx7XXQhYoxRt%2FnU5s2UX5U0Qih%2Fp%2BIOlZAfcst3UqkV6u9EoWJDj8E2r5nlY9mSGItC&X-Amz-Signature=fbd32d1817c1d31f94654a184df84e3076e83b55bea7ab06022d19c4a0b1cf2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFF7J33M%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T141719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCICu%2BIEr%2BwxAxIeR7fs%2BIaGXVSSQ3yPVjFpJ4%2BsxYCZDmAiEAiT3Q1rttAYXEETSRqyM3DqVpSbtUSdHZwA1vByUOgqkq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDH8H%2BDGmfH%2Bxz7ZizyrcA9r9AUtA2vheje%2BlpCb0Wm6JdW5Rl8mY72HTv5UU0XYv7Kf5U3uhnildBNU%2BiSpdjc9GEZUVv5KCVP3azic1e%2BMqOiX1n9NiQNhwT7GF658eWr9CTCJVVVh2iTakae1a2fsESqenbKzPTxwOqLygFSAmuumzNKXl2CDsxIiV1fBUoVmZzt82Z1dx5zB%2Bafs7OgLClndv0F4sRhZzYyCDHtw93sBm2mUMZelcYg6GNd57W2sp4vxEnSoPCsQVEhd9UW34hT3ODtG%2BmKDSN6IsIJgswuruIeO6NL8%2Bdci32cAwSwGFBrimLFBpw0g34zkYXYLZq7sBwja7VMS1ktTmUo9TjGV2R1kwEo45RoI1Q8hjxMHGzbzJX2QdL352YNgnNCKloyrSWBgrCyif9emPrXj24ofVt2LUt4ZYci56NyFiO%2B27k0XbNd2hrWzd2tDvYBDsW2foGjVTVPf0xlhLkGVRfcIkUAssqTmI2DmutOM4niDjqz4MHURZ7RbldL1VTli2hkKuqlgeH4%2BW38yM28SXNmOhsW8k9YfxBjY1IimCDW5NfJpD35JtG%2FXj9vx0JYvOI9uwp83lAXOwx9hqsLbm7L8oQpOKtU5NcB8ncqUe9nidLv0a7BNkl1MqMIf5i9QGOqUBnAJ5gBPFa%2FZDK%2FH5pf43j8OyEWCZ1AzFriJqZW9VP6v64X7Dc1U23c9LOfLUuRq1Mknz9W%2FaQ2nQjWRjsLHg5FMCFE17paLBKhy%2B0244ZQeE28D36kPJYDGF8QJy7G8vAPmm%2FZZgLgekFCX0%2FuFRrvSSaTx7XXQhYoxRt%2FnU5s2UX5U0Qih%2Fp%2BIOlZAfcst3UqkV6u9EoWJDj8E2r5nlY9mSGItC&X-Amz-Signature=e34cd04e8f79bc2dcf0559b981bc77bf48e326d328fb89ff29d7874abf336151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
