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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XETOUHCR%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T092020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIHnbQrkt81TEFNOPttWM5%2FNfFDLQ4thOyEkhDbkuE0MBAiEA9YRm8m0aWCDNFnznAgd%2B4LLAQthu5V3Qu5W5qqCfifgqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCO8Y1%2Fsdih%2B%2Bcx5yircA35q%2FdzpJTg%2B0XeMEv6O3EDhU3T4MzNoHMiz9gzu7u3uU56LrG4hlVZpxkg0sds4B00%2BVWfxpBMGplXe7AjA449ho2zwHcCyoSm3VFPzM4cJ2VluHiKzdlUP86mdrnBi0fzP34oikPLIc%2Fb3uBij9lNa8GSYyUdXw6djzkauSl9T4DNKM4cYn%2Bn8PnVmy%2Fsl3iPls%2FdppUpLjv8G0yZuq1vJZtP7B%2B4SyGEsLU4gSkVTA%2FxhFKdetH5%2Fkgq%2FwREAOCMKYfaGLbJx%2B%2BHuA32fcWd2wrIEiD5v6T2l%2BYxvg4ZbX76bVKx1mR2Q7QgRBv25PU1EZZ01t869o89Ys6GXHMzTT8nvHtG5M8WAfJtvxjHG0BboWHos8G8zbNeKBamP2vGEXw4F%2B8tIhN%2F5mjdBOS4Wejo4BZ5vQYSPfMGivc%2FPa9H%2Fn4UTahmgAtSDp9nuOTz4LRgzBl4ga11DCXBcQEYJ77yBVB%2FZg1dRC3DUzEODMuEbWDvoR2%2FrOvjiaA0LQf8nuMlGrwbXi9%2FVUhvPJSHMPNq1jb4I4wtqOr5yM4Gr88Do%2Fq1mng0fQNVLzWvBrRZifoveqr3%2BQIji2WiJnlBmNcLsxVqJuWLu4J%2BT1eQ9ana5Vpjnb%2B9zFEdkMNftntUGOqUBkGotVX0LTPr0Y85%2BJts4vvgU77gdL7cD1Q2dwAdJSRMKhobyHDOo0zfy2IyA5TDdJ2qSKtN1j88209P1nlz%2FSx%2BL%2FRDujp%2BsVVq74WRvyE2AiTCMBYrHmfjPjodXFtB58%2B2rYEAwgiS%2FQ%2B3UQBDk9d5FaRr08MTbHfRI7CXhI%2F1xR%2BP6%2BqcPU6Ljz0%2FWHgO%2BD84LB2OELnVsdb4EU6okVjB1otqi&X-Amz-Signature=62760fb989d46e7eb3376951e919699dd4450371c74b146a8096b73eff3aca6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XETOUHCR%2F20260914%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260914T092020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIHnbQrkt81TEFNOPttWM5%2FNfFDLQ4thOyEkhDbkuE0MBAiEA9YRm8m0aWCDNFnznAgd%2B4LLAQthu5V3Qu5W5qqCfifgqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCO8Y1%2Fsdih%2B%2Bcx5yircA35q%2FdzpJTg%2B0XeMEv6O3EDhU3T4MzNoHMiz9gzu7u3uU56LrG4hlVZpxkg0sds4B00%2BVWfxpBMGplXe7AjA449ho2zwHcCyoSm3VFPzM4cJ2VluHiKzdlUP86mdrnBi0fzP34oikPLIc%2Fb3uBij9lNa8GSYyUdXw6djzkauSl9T4DNKM4cYn%2Bn8PnVmy%2Fsl3iPls%2FdppUpLjv8G0yZuq1vJZtP7B%2B4SyGEsLU4gSkVTA%2FxhFKdetH5%2Fkgq%2FwREAOCMKYfaGLbJx%2B%2BHuA32fcWd2wrIEiD5v6T2l%2BYxvg4ZbX76bVKx1mR2Q7QgRBv25PU1EZZ01t869o89Ys6GXHMzTT8nvHtG5M8WAfJtvxjHG0BboWHos8G8zbNeKBamP2vGEXw4F%2B8tIhN%2F5mjdBOS4Wejo4BZ5vQYSPfMGivc%2FPa9H%2Fn4UTahmgAtSDp9nuOTz4LRgzBl4ga11DCXBcQEYJ77yBVB%2FZg1dRC3DUzEODMuEbWDvoR2%2FrOvjiaA0LQf8nuMlGrwbXi9%2FVUhvPJSHMPNq1jb4I4wtqOr5yM4Gr88Do%2Fq1mng0fQNVLzWvBrRZifoveqr3%2BQIji2WiJnlBmNcLsxVqJuWLu4J%2BT1eQ9ana5Vpjnb%2B9zFEdkMNftntUGOqUBkGotVX0LTPr0Y85%2BJts4vvgU77gdL7cD1Q2dwAdJSRMKhobyHDOo0zfy2IyA5TDdJ2qSKtN1j88209P1nlz%2FSx%2BL%2FRDujp%2BsVVq74WRvyE2AiTCMBYrHmfjPjodXFtB58%2B2rYEAwgiS%2FQ%2B3UQBDk9d5FaRr08MTbHfRI7CXhI%2F1xR%2BP6%2BqcPU6Ljz0%2FWHgO%2BD84LB2OELnVsdb4EU6okVjB1otqi&X-Amz-Signature=e9e75bfa229386421f7871bbe9af728e4b600f48b68ed18558e4e8855dbf618e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
