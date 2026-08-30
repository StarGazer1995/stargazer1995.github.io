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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVPKNPAQ%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T093234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBjb2AMx5HVEltbYP1di5vOSFc7nWrfItt%2FeVAb2YlBbAiEAkRoIEMnd01VX7%2FAC4ZWXyUm2t0ho4gLz6LUZsQ6GaMsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDO5dmNz%2Byy59rNZ1yCrcA88v3mZNkk7QmiMN5nH75SsL%2BXsylvEve1pO3xPkjDOvH3FrCa%2FmLcloGNlY71e7rTz1%2FAgKbp7eW2fymQgmevvDXWY02xI1XW1yBmyt7zsXTQ9G78yGLbxKsjnxtPze9KK0f4XKoC3bp4YtvAB2gWo%2B3OljoFLzEdfe67BA%2FG%2BNOJgXqlHGz0wb93XZhG%2Fu9TMUODmmfNRTZgUUMA6KkkPcvsNMfIMSs1%2Bo%2FHyR7hQNRQHfQlCX5Yn3RI%2BfiMt0RR72rh%2FfcVbsJrZkr3tp24yWI8PsTbzEfKdvJ9qi7dVhGxco2V4E57jqqYlSwHtz2u9mwK1C24bZzSuHwoeZ3eDsxGem5phopWbO8vPxnXpJkBcPMku3xMGz%2Bs%2BDOXmW5%2FsUGsHIzpQPtKfumTAjzmP%2BNNiTi2vwRq8RjNcH6%2BdQfyBJ9aGhoV%2FIjzItZU01Wc2nCMif%2BpBB002jV%2FEVOVge7Lc%2BiwQzwIk4n%2F%2FK9aI28PKYmbZDyMJWeQzZ8xRxqBLkjEus9SGmLm3FniFmIIt7UdQUR01DkEt22kEfsixxJ9g6F5gm6GB0CCH18xsjKYTgNgc2fF3zmw7CI90itgC1IpvdZ3%2BirRch2%2BBmdg4J9k3DGFvgKzRdehT4MN%2Buz9QGOqUBL3LLpM1C2wZeA8j68tLstKBb%2BDDsitaPpsqF0uaDUtO3zP52ySOyxl45YOF3wYdUgmz6%2By7wg9MNSwBHv%2BpNhbeg6gwCSy%2BWX3nIYMjCIMCZCxEwcl8ggAxWJlUyYqk9eh3avqq9xp65H5D4cmTWtR9OFuXgHOPXc2MZCaKFnxB%2F9Jxmtpigvjl5tC%2BdjFE2rE2QNodzj5NzSTp24STMRegfywql&X-Amz-Signature=23dfea196c02825303b93f1a285ebf909ee56eb1cd60c26c98634ff2a8d54531&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVPKNPAQ%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T093234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBjb2AMx5HVEltbYP1di5vOSFc7nWrfItt%2FeVAb2YlBbAiEAkRoIEMnd01VX7%2FAC4ZWXyUm2t0ho4gLz6LUZsQ6GaMsq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDO5dmNz%2Byy59rNZ1yCrcA88v3mZNkk7QmiMN5nH75SsL%2BXsylvEve1pO3xPkjDOvH3FrCa%2FmLcloGNlY71e7rTz1%2FAgKbp7eW2fymQgmevvDXWY02xI1XW1yBmyt7zsXTQ9G78yGLbxKsjnxtPze9KK0f4XKoC3bp4YtvAB2gWo%2B3OljoFLzEdfe67BA%2FG%2BNOJgXqlHGz0wb93XZhG%2Fu9TMUODmmfNRTZgUUMA6KkkPcvsNMfIMSs1%2Bo%2FHyR7hQNRQHfQlCX5Yn3RI%2BfiMt0RR72rh%2FfcVbsJrZkr3tp24yWI8PsTbzEfKdvJ9qi7dVhGxco2V4E57jqqYlSwHtz2u9mwK1C24bZzSuHwoeZ3eDsxGem5phopWbO8vPxnXpJkBcPMku3xMGz%2Bs%2BDOXmW5%2FsUGsHIzpQPtKfumTAjzmP%2BNNiTi2vwRq8RjNcH6%2BdQfyBJ9aGhoV%2FIjzItZU01Wc2nCMif%2BpBB002jV%2FEVOVge7Lc%2BiwQzwIk4n%2F%2FK9aI28PKYmbZDyMJWeQzZ8xRxqBLkjEus9SGmLm3FniFmIIt7UdQUR01DkEt22kEfsixxJ9g6F5gm6GB0CCH18xsjKYTgNgc2fF3zmw7CI90itgC1IpvdZ3%2BirRch2%2BBmdg4J9k3DGFvgKzRdehT4MN%2Buz9QGOqUBL3LLpM1C2wZeA8j68tLstKBb%2BDDsitaPpsqF0uaDUtO3zP52ySOyxl45YOF3wYdUgmz6%2By7wg9MNSwBHv%2BpNhbeg6gwCSy%2BWX3nIYMjCIMCZCxEwcl8ggAxWJlUyYqk9eh3avqq9xp65H5D4cmTWtR9OFuXgHOPXc2MZCaKFnxB%2F9Jxmtpigvjl5tC%2BdjFE2rE2QNodzj5NzSTp24STMRegfywql&X-Amz-Signature=d3ed78911d97359d0c64c68e66882272cca0e7833738904c5bed91fdaf3cac33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
