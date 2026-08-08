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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQDJEAVW%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T201617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEeMriB4Y9s33CXAtFZ3e%2FbFTVm08ZyMybsz8jrKfbsNAiEA0pMmFkmiH77g%2Fyic%2BoGhaYtqM7%2BITEeN6qbE6uvMjHkq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDF6HUVGB6IFDBEcQgSrcA6WWywMWqgY5ewmYRkW6I1t4i6CncCnphh%2Fg2iiE74ov6%2F1wsoKe3%2B%2BZuD5w4nT9L3vtgzp9z%2B2RX7PbXski4K0IKeP5RhxN5aSv%2FFLWVyoRsUbtTvB1ON4DhqrIHTo2KU%2FM5pAVbFgCV3R50IKBYLY3cNM0XbgeyZtqdEVbruox%2Fh6W46HKiA09XBdn64ghWYDVh1Mm9IDWVAmUQ34u6ATwYR4H1z2G7AjgpBQjSHW928ifUZL%2FPEMjVaJHAZCw4ADVfWtOlzjIaweX8DOpImb9vBRQGVUpGdkYVDHaEMuRPrXaMFKJweAuX8N3KJys9ED%2FJqDNcE6A69V3p0qrorguNygJI14Wtr1sRRzKYAyQx6Am%2BeujtB3CC17%2BS1EMr8nTQzLDJEywH2QSpDa6LEOrhX3kq1p2ivbA3yPDGOJVVP%2BqYJtWgE5n3kclxgPsIb%2BMyY5F8p9YPDP99DcWbGPK%2BobRxRFTrQxuDcos0aREZt%2FTIh%2BJJqCICWEGCkyvwzKTY%2BdV%2FfSW%2F6Zu17etqDShfJF1OWhE4skk%2FIWHPnVhqDdjQ1MoLkBF8aN6ErhJ1WffzdPsg1WW4PJI5FaRPQ373flzuetVkyYrKd2iJVtfvyHUJQ%2FA9sPyER3JMO6F3tMGOqUBE3ExsU9jrxdFpgVcS7eVnHg%2BetYuS9HJmnDdF2sEm2YuqJ%2Bccu8kvou3pU%2Fip%2F57wTGwegEoSVHZx7dPFJp8fvDOQH%2FMiUHHfdD4EWoC3uTtKd4OTgfGdaSjaT9eL3hA%2BKVAcDwB89j4%2FJQc95jFr2IcMfeigGdqc8o%2Bs3cnoczR0tSBBLMosbJSGtILgwi74NAdSSBFTS7TRdbta%2BsGWKqhIOG3&X-Amz-Signature=293218cb5d10ece38b517bff65fb14771070cbc973bb9154f68a476323cd415a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQDJEAVW%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T201617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEeMriB4Y9s33CXAtFZ3e%2FbFTVm08ZyMybsz8jrKfbsNAiEA0pMmFkmiH77g%2Fyic%2BoGhaYtqM7%2BITEeN6qbE6uvMjHkq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDF6HUVGB6IFDBEcQgSrcA6WWywMWqgY5ewmYRkW6I1t4i6CncCnphh%2Fg2iiE74ov6%2F1wsoKe3%2B%2BZuD5w4nT9L3vtgzp9z%2B2RX7PbXski4K0IKeP5RhxN5aSv%2FFLWVyoRsUbtTvB1ON4DhqrIHTo2KU%2FM5pAVbFgCV3R50IKBYLY3cNM0XbgeyZtqdEVbruox%2Fh6W46HKiA09XBdn64ghWYDVh1Mm9IDWVAmUQ34u6ATwYR4H1z2G7AjgpBQjSHW928ifUZL%2FPEMjVaJHAZCw4ADVfWtOlzjIaweX8DOpImb9vBRQGVUpGdkYVDHaEMuRPrXaMFKJweAuX8N3KJys9ED%2FJqDNcE6A69V3p0qrorguNygJI14Wtr1sRRzKYAyQx6Am%2BeujtB3CC17%2BS1EMr8nTQzLDJEywH2QSpDa6LEOrhX3kq1p2ivbA3yPDGOJVVP%2BqYJtWgE5n3kclxgPsIb%2BMyY5F8p9YPDP99DcWbGPK%2BobRxRFTrQxuDcos0aREZt%2FTIh%2BJJqCICWEGCkyvwzKTY%2BdV%2FfSW%2F6Zu17etqDShfJF1OWhE4skk%2FIWHPnVhqDdjQ1MoLkBF8aN6ErhJ1WffzdPsg1WW4PJI5FaRPQ373flzuetVkyYrKd2iJVtfvyHUJQ%2FA9sPyER3JMO6F3tMGOqUBE3ExsU9jrxdFpgVcS7eVnHg%2BetYuS9HJmnDdF2sEm2YuqJ%2Bccu8kvou3pU%2Fip%2F57wTGwegEoSVHZx7dPFJp8fvDOQH%2FMiUHHfdD4EWoC3uTtKd4OTgfGdaSjaT9eL3hA%2BKVAcDwB89j4%2FJQc95jFr2IcMfeigGdqc8o%2Bs3cnoczR0tSBBLMosbJSGtILgwi74NAdSSBFTS7TRdbta%2BsGWKqhIOG3&X-Amz-Signature=3c49e268e4b4bbb8602e3637fa3b05c433be89f7e8968d23574f325149e7ef12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
