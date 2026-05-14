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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633CVFHQ7%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T132612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID6soMSUlm6thqhmiIM0Z86WOOYNYPQySonuHAvl07YfAiEAtZBKa5TuNtG25%2FNc%2FnOp7uAt8T6PLFqvUAdpNooXRHMq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDCJzSOf3arv0YKlQ4yrcA9ta5QU%2FsIAb1N%2B5Buo1FlDlE5VGrPZEQ5audaQgF7aii41y1Jlk3Rq4I4YfLosUjEiB82fkMSU1aXmVE3I6O0yGK6Ipquexumd3077GgiUctMe%2BxUO7nsK8lbjtEYamZc%2Bw%2FgDJMq3vfTznII%2FxtgNqAeY4J%2Fp%2FyOALgARvEbiQ95kARL5aN9TrkpcK7lrdAo%2FdgbZY4ulKlcCgwajDe38NNQ3iH6cQYPYx3fvJAMgPfSZ6b5E%2BbZRKv7WzT2bZblqrg%2Fgj3yXJ5%2BGEe85dBsBtn2KQs7qTNO8n%2B9zKJ2Yl6O2ZBqsUQL88E6SyLQvd60dPgRlMFXXpLEkpmSkGyC7VZzFOyH029HBCIy%2B91RYzZCJolgSiJsJezEX8jmkNsyyQ0lRv0og97l3Uto%2F7SpLDozZk1UNNnxmWAK2Dof65pfnp0M0Dsq8HwrpxMBkiWTqw4KgP2WhRIHM0PJnvFrM0KBJnicqlW5HjKCdxNwuNfThgycZyRXBzdfRKGsoCo9jPviQhk0sEWegbzkkwUqr5z38jUFPfDXubcuEMDcMApAHY6UYGDGqWtlq9JKoDCftUOWWD9M%2FaaVc5M%2FNSUxlDg0Z72oyWUhJYK9V761WuyAEhLXaWLuMJFzcBMPb%2FltAGOqUBZ1OylLxxFhOLcYRmnGO%2Fh7sWpKqHhHgThwyInNnZsLPIlILLtQCe0qogPFSXtcSfIJC7O1ETU8RbBgjN7mD1dldReia7JcL9uIu5HZHmX8W28r2Fs6%2Bwnhae6pvWkWEl1mOOEVN9tMetb8P69av3T0qrhXdL6DclCBJmMuAMMa6Xpq3vHKuG59Ji79XNuwQDaUFBcd%2FUnSxl1x%2FOc365xsjWc5BH&X-Amz-Signature=f71a3eb12a7cfee0ec5f2c6697faa6df121718da1a0fed2471bd32c61ffc413b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633CVFHQ7%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T132612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID6soMSUlm6thqhmiIM0Z86WOOYNYPQySonuHAvl07YfAiEAtZBKa5TuNtG25%2FNc%2FnOp7uAt8T6PLFqvUAdpNooXRHMq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDCJzSOf3arv0YKlQ4yrcA9ta5QU%2FsIAb1N%2B5Buo1FlDlE5VGrPZEQ5audaQgF7aii41y1Jlk3Rq4I4YfLosUjEiB82fkMSU1aXmVE3I6O0yGK6Ipquexumd3077GgiUctMe%2BxUO7nsK8lbjtEYamZc%2Bw%2FgDJMq3vfTznII%2FxtgNqAeY4J%2Fp%2FyOALgARvEbiQ95kARL5aN9TrkpcK7lrdAo%2FdgbZY4ulKlcCgwajDe38NNQ3iH6cQYPYx3fvJAMgPfSZ6b5E%2BbZRKv7WzT2bZblqrg%2Fgj3yXJ5%2BGEe85dBsBtn2KQs7qTNO8n%2B9zKJ2Yl6O2ZBqsUQL88E6SyLQvd60dPgRlMFXXpLEkpmSkGyC7VZzFOyH029HBCIy%2B91RYzZCJolgSiJsJezEX8jmkNsyyQ0lRv0og97l3Uto%2F7SpLDozZk1UNNnxmWAK2Dof65pfnp0M0Dsq8HwrpxMBkiWTqw4KgP2WhRIHM0PJnvFrM0KBJnicqlW5HjKCdxNwuNfThgycZyRXBzdfRKGsoCo9jPviQhk0sEWegbzkkwUqr5z38jUFPfDXubcuEMDcMApAHY6UYGDGqWtlq9JKoDCftUOWWD9M%2FaaVc5M%2FNSUxlDg0Z72oyWUhJYK9V761WuyAEhLXaWLuMJFzcBMPb%2FltAGOqUBZ1OylLxxFhOLcYRmnGO%2Fh7sWpKqHhHgThwyInNnZsLPIlILLtQCe0qogPFSXtcSfIJC7O1ETU8RbBgjN7mD1dldReia7JcL9uIu5HZHmX8W28r2Fs6%2Bwnhae6pvWkWEl1mOOEVN9tMetb8P69av3T0qrhXdL6DclCBJmMuAMMa6Xpq3vHKuG59Ji79XNuwQDaUFBcd%2FUnSxl1x%2FOc365xsjWc5BH&X-Amz-Signature=04d000acf43cdebeae39ae1af5dde0db9a16448a2f087d75bc92be98d07915f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
