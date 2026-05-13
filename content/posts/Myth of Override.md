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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH4YM3EE%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T192956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD56z4edWKw2guRLAYQqCZ7W08GnLII9MVjlKAXmYL2zgIgRXUiMxXbqCuhf2oBpYhJE9sPj5zuOh874vWaeQEmhOMq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDBHouZuC9ftV7SF%2BayrcA3Ey3oZlUCOdDl7mpG0onZ5sRd4EoD4y9tM1Afqet2Mn3sF5rYNvyNw9FPegQgOkhLnPsAUe0hEA7U0gSKfGmbhzHCNaa9Ow7otN%2FDcaf9%2FRgfyDN9isFoNZoOlOzdPu2xCqx2%2FvumNIhUd3i50XzzPQzO44M3Pitpej7Ga7ACfDrZubY8NZ5XpZK1a5k%2FCG3Q2WHFe9KhLJkEa1duBD%2FFiWUR6I7acY797gs%2BSaq%2F96WtEFxg7gfjdaE3yUQ2VO4K4KmJ678dcdUZ3Q2hiE2tD%2BvuD0zIX3wUrF1DfgNsqC4xkKiYMsrRF0Sth7S0bt4N2LfBEMapEAQxIPEJk3tbqL37hLnfUWkK80Pn5Fy4ZuLvku0lB%2FaYjsspmJg7Y7WOesijvfXGGZkEbkqAzVdEDGjoQYyZo%2Bv4wp0eXao6gUYop%2Fmf4r%2BIOEwavRWdY4KNlGc5dRDEhiiF6bZofm%2BqN68M2fD3lmUSUsbQlJBVtYrUqquS1y%2FvlUTGfLiz5pvyHgmwIgfsm8LsX02EcpQAOR%2BMap2h5Rz%2BVn%2BmFCc62jQdSQGzB%2BBYzIEsF0Iz3qvGtU87%2F7IBeiucNJHPLUr4NC4IUmFM0n6TZ66zQ4VHfYiF4p%2BpKXXomNN5PLMOH7ktAGOqUBaHrIukZIPTDbBzEK7sex5iBpFu2GFu5g0US%2FukI%2FHBOIro2Fg7TvT3cTXYaykC3gnC4SS3zeehQ2VxVhyxq5alQracUNWoBJVNq1lNmtdC5udJiazekTPjhy8ANkt6LXQQD0QhDO5bUGagZx7%2Fcl0rsk1X%2BptFqm%2BCV5wwBJyRIJP96QkyEd0ZoUb2sOGBvbAY%2BTvL0PmOv1dBmj8JiuaejxHBil&X-Amz-Signature=ebf3c237636b6ca64dca78c94481aac9d0e8c86fd45c1fb4000ae78a3ce12ad1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH4YM3EE%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T192956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD56z4edWKw2guRLAYQqCZ7W08GnLII9MVjlKAXmYL2zgIgRXUiMxXbqCuhf2oBpYhJE9sPj5zuOh874vWaeQEmhOMq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDBHouZuC9ftV7SF%2BayrcA3Ey3oZlUCOdDl7mpG0onZ5sRd4EoD4y9tM1Afqet2Mn3sF5rYNvyNw9FPegQgOkhLnPsAUe0hEA7U0gSKfGmbhzHCNaa9Ow7otN%2FDcaf9%2FRgfyDN9isFoNZoOlOzdPu2xCqx2%2FvumNIhUd3i50XzzPQzO44M3Pitpej7Ga7ACfDrZubY8NZ5XpZK1a5k%2FCG3Q2WHFe9KhLJkEa1duBD%2FFiWUR6I7acY797gs%2BSaq%2F96WtEFxg7gfjdaE3yUQ2VO4K4KmJ678dcdUZ3Q2hiE2tD%2BvuD0zIX3wUrF1DfgNsqC4xkKiYMsrRF0Sth7S0bt4N2LfBEMapEAQxIPEJk3tbqL37hLnfUWkK80Pn5Fy4ZuLvku0lB%2FaYjsspmJg7Y7WOesijvfXGGZkEbkqAzVdEDGjoQYyZo%2Bv4wp0eXao6gUYop%2Fmf4r%2BIOEwavRWdY4KNlGc5dRDEhiiF6bZofm%2BqN68M2fD3lmUSUsbQlJBVtYrUqquS1y%2FvlUTGfLiz5pvyHgmwIgfsm8LsX02EcpQAOR%2BMap2h5Rz%2BVn%2BmFCc62jQdSQGzB%2BBYzIEsF0Iz3qvGtU87%2F7IBeiucNJHPLUr4NC4IUmFM0n6TZ66zQ4VHfYiF4p%2BpKXXomNN5PLMOH7ktAGOqUBaHrIukZIPTDbBzEK7sex5iBpFu2GFu5g0US%2FukI%2FHBOIro2Fg7TvT3cTXYaykC3gnC4SS3zeehQ2VxVhyxq5alQracUNWoBJVNq1lNmtdC5udJiazekTPjhy8ANkt6LXQQD0QhDO5bUGagZx7%2Fcl0rsk1X%2BptFqm%2BCV5wwBJyRIJP96QkyEd0ZoUb2sOGBvbAY%2BTvL0PmOv1dBmj8JiuaejxHBil&X-Amz-Signature=b2d9a2b946276c41daa574d1f4ab172748aa2a190edea6eaa8ed4526003c9c02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
