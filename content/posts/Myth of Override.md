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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5VBEFAY%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T003623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHZiU5LezL%2B9kKoOfrahbEZZ3bnsagFKqfWaF5wrtJonAiEAupPzEZUe8xHU%2Bt1CSwiaUmsJfmZKUwbcSHOeMpDa8iAq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDE1AFh9m0kMUqycNfSrcA55mcRgZ51V7NFy%2Bue%2F9E%2B%2BK7iSWvAB4Tv1r1bv2clDZvIYiCV3si3LgR6GRHtwpwjd%2FE%2F88gUhwIFhiEqNuO6EOqeN9qizA%2FDcXe8yNH%2Bkngq9iCdl2qyGPTMf5n%2FVtA4F7%2FAYFVlabL%2F%2BZHCcu79pXhYHBF7R885W1XfvRLRX0Eq7NF9UMJ%2FwxTPtTxFiZI9lVZM8v446m8oDGTAvTr8RK8tTqVk7myzrqNrz6%2BS41tAVT3GrVoPgEzSaZd%2F91%2Fjg%2Fv%2F9bk7nuA36BGHKLqIu4%2BUijxzTprI03RiBk1UTYCvZOXOiNoIjZqn2QzfF%2BEj5ulkwEsC8pgC2chywqgk4ZHwZXBEVz3VkoebV%2BrFQj230wf54l3SpqdvtsNRkvcFr5OSM%2BQ%2FYiQHOKRFZiUAT64GWU4C5xvDJ3hfCqalF4Zl4BJxZCw9eknG0KIsHEUDCu%2FvlsrFYHAgKNVnVWJFNhSDPSxxnlqFUJpT%2BO5t89C5ykB6hB1deeCMyPwJzO5%2FhQvOjai2tBkA63EDxukAI42Y%2FPRV05Vv5h85k%2FRayWscO6zoLVtGfoQTvqKC2OWyA6htalIMr9TF0qXP6U59JyT%2BDHm4s3M7yvjIK6%2B0B8MIehslm2oEDki2VOMPidjtQGOqUBV57O7yieYwhgj9OleqQ7cNUVHSQZuj8Zw3D82V7mYznMMuyo4t%2F1brb0aGYjVnZ8zw7d6Z4Vl43U1KRF%2Fk1DWgSb%2F2Uo1RDbziBb2QFP2yurvUMsjk2oAZGMqbhY461VpmyMaU15f1fC%2B1XadzKkGz0%2FWkbmR0%2Bcl7f39Z0pTzPksh4cZNJqXXS35nfw2HO4tWJRNezUIu1HttSd%2BoJLUjA0kEch&X-Amz-Signature=c5bbf87a62d4000a96e34d52b6af3e1d1d3e534b16fb268933058aaa98c9f938&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5VBEFAY%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T003623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHZiU5LezL%2B9kKoOfrahbEZZ3bnsagFKqfWaF5wrtJonAiEAupPzEZUe8xHU%2Bt1CSwiaUmsJfmZKUwbcSHOeMpDa8iAq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDE1AFh9m0kMUqycNfSrcA55mcRgZ51V7NFy%2Bue%2F9E%2B%2BK7iSWvAB4Tv1r1bv2clDZvIYiCV3si3LgR6GRHtwpwjd%2FE%2F88gUhwIFhiEqNuO6EOqeN9qizA%2FDcXe8yNH%2Bkngq9iCdl2qyGPTMf5n%2FVtA4F7%2FAYFVlabL%2F%2BZHCcu79pXhYHBF7R885W1XfvRLRX0Eq7NF9UMJ%2FwxTPtTxFiZI9lVZM8v446m8oDGTAvTr8RK8tTqVk7myzrqNrz6%2BS41tAVT3GrVoPgEzSaZd%2F91%2Fjg%2Fv%2F9bk7nuA36BGHKLqIu4%2BUijxzTprI03RiBk1UTYCvZOXOiNoIjZqn2QzfF%2BEj5ulkwEsC8pgC2chywqgk4ZHwZXBEVz3VkoebV%2BrFQj230wf54l3SpqdvtsNRkvcFr5OSM%2BQ%2FYiQHOKRFZiUAT64GWU4C5xvDJ3hfCqalF4Zl4BJxZCw9eknG0KIsHEUDCu%2FvlsrFYHAgKNVnVWJFNhSDPSxxnlqFUJpT%2BO5t89C5ykB6hB1deeCMyPwJzO5%2FhQvOjai2tBkA63EDxukAI42Y%2FPRV05Vv5h85k%2FRayWscO6zoLVtGfoQTvqKC2OWyA6htalIMr9TF0qXP6U59JyT%2BDHm4s3M7yvjIK6%2B0B8MIehslm2oEDki2VOMPidjtQGOqUBV57O7yieYwhgj9OleqQ7cNUVHSQZuj8Zw3D82V7mYznMMuyo4t%2F1brb0aGYjVnZ8zw7d6Z4Vl43U1KRF%2Fk1DWgSb%2F2Uo1RDbziBb2QFP2yurvUMsjk2oAZGMqbhY461VpmyMaU15f1fC%2B1XadzKkGz0%2FWkbmR0%2Bcl7f39Z0pTzPksh4cZNJqXXS35nfw2HO4tWJRNezUIu1HttSd%2BoJLUjA0kEch&X-Amz-Signature=0564c2c8693df14b11f605468f9def50352ce53fa65d39cbab3a1d54782561c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
