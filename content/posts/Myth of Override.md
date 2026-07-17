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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM42SGBA%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T165808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIdeNjHY1hMjVe%2FPonZCxGheItvTfxHnrU9xiJtMVgkAiEAt04vNlN%2BjirLh4%2F%2FgcQBNe2CFo6JDGyRc2QN1kjHfCQq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDEkknA%2B2fZxviWJq0SrcAwdCyFeqGA4fkmG6YA5yiyWSeEA5k0veXqtAH28EgSWh6cEeRnzopjcXSg0jX5fhQk08HME1GlbYa5nZdtDP%2BLEsjTWqN1EOKtgx9zvq0%2Be7SEPcODONflBHVnwDt3kThHBMQhzX%2BLbrq9G7GuXLoKDUi86bPmQmfsQ%2FwWc8qxVxjQMpdI2vhl%2F3vjMAHiudRSlHfu1KEt2KRlYGrTXu1dihEudOgrdhE3TUoA6BJzoCBm97a%2BnSCjNd95oQ8i79cOwjOOiR3OptWMRheDSxFL%2B27BgrLe3hu5B6K4pamNuUCx0yE2jyPtRs%2BmKGKLzA5NPDJ9duj1Q2Dqu31O1KfSLrMH%2BKwTCFFTVpd6e1P3FwdVbk9w3PqPMxZxBkg%2FFmjKIhcpzIttC9JkZhoyrsrR3eeHrcMNVdwZQ%2FT9qtNIufL8f9vzDDBYj%2BYVG1HVsDsPa5DXV5cQrq7UDbDK3QujJw%2FFvAmhB94XR6MlNQWqXq43BG9l9Y5LQqiLW5Yfhi%2BIQsvN7bluaHLYLVqaBpy3is0QkPRGU9DyYLGLchqNSNjUylPP9KrwnfY8qDe2aA1Qgl7aiRxf7dgIEOrZ3tXpCAp8dEs%2BnGOC1gx6%2Fv5C%2BPCYSdrQNmayuE9mIVMKKX6dIGOqUBu8NlUSS1pL8PCNrExZCVHxezb4BvfLqa49kEW6odaVB4mo28wQ25ziIGyvlMu13znUjtO3KsgCTsUTq9Fj%2BirbRONkAs4WGoNhDTtvCiZFNVTyRCywKxT9Y%2B4mYg%2F2v4oKufSPkF94%2FISqV0rXxQ66Oq4KfOjA%2F7kevDpNqRc74xCg4NqgKPvIR6xk%2FF7U74JBJE6nDaV6bVZiVaAB%2BlsT0MtCW2&X-Amz-Signature=d165282cd1635e1253aad1e24341db701362adfa97ed413707a62b1830ed6e28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM42SGBA%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T165808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIdeNjHY1hMjVe%2FPonZCxGheItvTfxHnrU9xiJtMVgkAiEAt04vNlN%2BjirLh4%2F%2FgcQBNe2CFo6JDGyRc2QN1kjHfCQq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDEkknA%2B2fZxviWJq0SrcAwdCyFeqGA4fkmG6YA5yiyWSeEA5k0veXqtAH28EgSWh6cEeRnzopjcXSg0jX5fhQk08HME1GlbYa5nZdtDP%2BLEsjTWqN1EOKtgx9zvq0%2Be7SEPcODONflBHVnwDt3kThHBMQhzX%2BLbrq9G7GuXLoKDUi86bPmQmfsQ%2FwWc8qxVxjQMpdI2vhl%2F3vjMAHiudRSlHfu1KEt2KRlYGrTXu1dihEudOgrdhE3TUoA6BJzoCBm97a%2BnSCjNd95oQ8i79cOwjOOiR3OptWMRheDSxFL%2B27BgrLe3hu5B6K4pamNuUCx0yE2jyPtRs%2BmKGKLzA5NPDJ9duj1Q2Dqu31O1KfSLrMH%2BKwTCFFTVpd6e1P3FwdVbk9w3PqPMxZxBkg%2FFmjKIhcpzIttC9JkZhoyrsrR3eeHrcMNVdwZQ%2FT9qtNIufL8f9vzDDBYj%2BYVG1HVsDsPa5DXV5cQrq7UDbDK3QujJw%2FFvAmhB94XR6MlNQWqXq43BG9l9Y5LQqiLW5Yfhi%2BIQsvN7bluaHLYLVqaBpy3is0QkPRGU9DyYLGLchqNSNjUylPP9KrwnfY8qDe2aA1Qgl7aiRxf7dgIEOrZ3tXpCAp8dEs%2BnGOC1gx6%2Fv5C%2BPCYSdrQNmayuE9mIVMKKX6dIGOqUBu8NlUSS1pL8PCNrExZCVHxezb4BvfLqa49kEW6odaVB4mo28wQ25ziIGyvlMu13znUjtO3KsgCTsUTq9Fj%2BirbRONkAs4WGoNhDTtvCiZFNVTyRCywKxT9Y%2B4mYg%2F2v4oKufSPkF94%2FISqV0rXxQ66Oq4KfOjA%2F7kevDpNqRc74xCg4NqgKPvIR6xk%2FF7U74JBJE6nDaV6bVZiVaAB%2BlsT0MtCW2&X-Amz-Signature=e146aa1a985b165987d710ebd18ca08665d8fdcae81e11a6dd36bf6f09bc0fa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
