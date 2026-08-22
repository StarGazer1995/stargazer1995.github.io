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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSP5X7I%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICS%2B5PElNaAf%2Bk0V1WaCtbM4UCZD2iLI1z8sq5ltCt0UAiBiM4kiyaIL9isZ2qf8XvwyHNjrNLRtzJvxb0IIXh69KyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxFPut1r8qC5GyWiKtwDGE%2BjU0oZleGR8wmb7OKL6epoDtL%2BNfIjnt%2F1BmzN9MyLGlOjj%2BLtd79coftb1UMv5dr4ejBuGcQrFBxmTlVeLGtKnFKiPh3qPycjzRXKRezBMIoz595phPNc%2F9z3cqVkZYftcDnIWp5KEyU1o%2Fb9IYU7hUyGBiuoYp%2FzzIX67PKxMcTWaMalmnSWDhTElWadiO8XTFPpYcEu4YuS0xXVT0mfRoDDUG%2BWtSBy%2FRa4qKxCyYb3m0kJyiqpaAEu4XN5Le77ngjSavGKSxu8seLWg2bSgeCX9cEqgvCXTW8vaEonb1Ohbvq0xf%2BOGCu7qFnMBWsqkiyemp8oC5wJA090WgbsLdYpd8%2Bjli1eU7XuWUst8i3Fc10%2Fg%2BtHm7bE5FBxW8Y6Acbkm0gkiiUDh7fHJgtXCKO3vOoPnpfelG7eIpZfFHnI5T80WMuwqRnPEMsCd7DA2WLh7dHeUOuJA2iJlS%2BB2G1eSe7%2B0LiHFAWQDdMs4SyN8hlcBxg82CbgWHwfGOSFv0aylz2Q6pr30GzQgiPVpm6Kg49xh7GWtJpeua%2FJV1TlZzm4p9U1S4j%2B7a1CxaqgmivUpNZO4GHAElKUlhi5sGy5U3F1ZKYuylySjQ8ZEF3egY%2BRFtgjAQsw%2FICk1AY6pgGS4zlKs5rEu45Q6wTbBE9s%2F%2FRSsLlxaVZLfcii3hMpurvDkZ3C5rBLKOuIg4G%2F9eJ4VlQGOxYaGxkFKmCwCehwDdNEsqFpCtGqYqOMQAPuEIi1Zfps1kwkvWIBQoCRYOEgiY5fB5CxKT4tKk2mokBTwetFmtkdphcVpU2nzN2Q5lTOsSTdEdl99NizedIlDOLpZvjljyvdn9Yn0wMZA%2BFwrh81b8Yu&X-Amz-Signature=b6623a18e1e3e297f8f69f06075819d045621c6e428aaeb8f33d2a84eda691a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSP5X7I%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICS%2B5PElNaAf%2Bk0V1WaCtbM4UCZD2iLI1z8sq5ltCt0UAiBiM4kiyaIL9isZ2qf8XvwyHNjrNLRtzJvxb0IIXh69KyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUxFPut1r8qC5GyWiKtwDGE%2BjU0oZleGR8wmb7OKL6epoDtL%2BNfIjnt%2F1BmzN9MyLGlOjj%2BLtd79coftb1UMv5dr4ejBuGcQrFBxmTlVeLGtKnFKiPh3qPycjzRXKRezBMIoz595phPNc%2F9z3cqVkZYftcDnIWp5KEyU1o%2Fb9IYU7hUyGBiuoYp%2FzzIX67PKxMcTWaMalmnSWDhTElWadiO8XTFPpYcEu4YuS0xXVT0mfRoDDUG%2BWtSBy%2FRa4qKxCyYb3m0kJyiqpaAEu4XN5Le77ngjSavGKSxu8seLWg2bSgeCX9cEqgvCXTW8vaEonb1Ohbvq0xf%2BOGCu7qFnMBWsqkiyemp8oC5wJA090WgbsLdYpd8%2Bjli1eU7XuWUst8i3Fc10%2Fg%2BtHm7bE5FBxW8Y6Acbkm0gkiiUDh7fHJgtXCKO3vOoPnpfelG7eIpZfFHnI5T80WMuwqRnPEMsCd7DA2WLh7dHeUOuJA2iJlS%2BB2G1eSe7%2B0LiHFAWQDdMs4SyN8hlcBxg82CbgWHwfGOSFv0aylz2Q6pr30GzQgiPVpm6Kg49xh7GWtJpeua%2FJV1TlZzm4p9U1S4j%2B7a1CxaqgmivUpNZO4GHAElKUlhi5sGy5U3F1ZKYuylySjQ8ZEF3egY%2BRFtgjAQsw%2FICk1AY6pgGS4zlKs5rEu45Q6wTbBE9s%2F%2FRSsLlxaVZLfcii3hMpurvDkZ3C5rBLKOuIg4G%2F9eJ4VlQGOxYaGxkFKmCwCehwDdNEsqFpCtGqYqOMQAPuEIi1Zfps1kwkvWIBQoCRYOEgiY5fB5CxKT4tKk2mokBTwetFmtkdphcVpU2nzN2Q5lTOsSTdEdl99NizedIlDOLpZvjljyvdn9Yn0wMZA%2BFwrh81b8Yu&X-Amz-Signature=fa8fee13686fa22f66602932b9cf611456810467327e4a1e24ca6622079287c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
