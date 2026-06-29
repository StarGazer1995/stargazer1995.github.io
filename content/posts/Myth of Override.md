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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466352ZJMNE%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T165136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6F1m0tVgOA3LyddBlw6HNXYLFP2RG12jsy7qBS%2BcItAiB%2FVXGS0RlTzLtIJiS%2FoNIdtloECDUeEFP3WBYsfLui%2BSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgoj0ZdBB87Vo5c77KtwDN6pD%2FWhqzOJc5%2BKhtQ%2FQmyfC%2BtagUQW%2B9pcmRw39JiyLDqj%2BkymJMCRxmY6csPuV5bF415ZOlo4a0A8ErvHsFAmqf7Ngoa%2BLnpvxBqZmUkjsupYNuEIq2mq3pm5W%2F3W%2Btsp2oqbpVU1QRMXD0PlREXon0hAq%2BgM%2BVgjm9fkd7pXF3et8fBam4%2BZBexztan3B1Yy0SIDoPcIk3t0WXrrr7RFnzTGLrdZImxn1jgvXp1EAU5Qs5JbUJ1YsQeUq4hgSdrqK%2FF88mf%2F97peLeqTzkjyU%2B5RLw2ajCiQSB1OchoQmZtSheAVSr1X%2Ftt0zNKXCmpxfYTUmu%2FMAB413ujzgTIYo%2Fatz7wOP9nkFa%2Flr1HTYESY9vBFOOeoYWdCSP2KBQNbuprbaM4VCTgQTsCc6N9zXSy%2BZPy8EkDzYm8b%2BUcTd42%2B0Pkm1G1isW7nkG06lpFZFTxQ5dQbPoyTxzsf0EZicobQ38%2BrajhLzSkBbAikodCPimXh9eXaKyrAo5cjyvWyNhwfDUg5op5gu5J%2F%2F7hYN14C4QD4CIR8gEQWJcZcmnx0tin7n89j%2BIIdhglPI3EaNyH8fnjgaCBvORlsscRhzDRf7aArz3rIuiBmUc7yYCgMiIi0pAgI%2FvgEwr8GK0gY6pgF9wY1ANC2ocZnzsxTNRoRP%2BUqWxv9BEL5mFFg%2BprP7ioT6armX5fTlbQEBSpQ1rSuIBkiVtUR7qgkKpq8X48lyks7Rkka%2FEQ7h0XQSUtKTJ%2F3jURY7i7ULrpbKPgIop0yH6%2FcFr%2BkHyaiqjek1q0TilJ7lxo9GjtMS%2FXDCf1qhbv1YcvBWNG3xLHghO6qTg%2F2uVUAp%2BHmblEjOi5%2BZgpid6QLqH6n%2F&X-Amz-Signature=3d5a55940ef6dda721bab64bc0ec1aac388718f656c231dc3ab5446a868f1a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466352ZJMNE%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T165136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6F1m0tVgOA3LyddBlw6HNXYLFP2RG12jsy7qBS%2BcItAiB%2FVXGS0RlTzLtIJiS%2FoNIdtloECDUeEFP3WBYsfLui%2BSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgoj0ZdBB87Vo5c77KtwDN6pD%2FWhqzOJc5%2BKhtQ%2FQmyfC%2BtagUQW%2B9pcmRw39JiyLDqj%2BkymJMCRxmY6csPuV5bF415ZOlo4a0A8ErvHsFAmqf7Ngoa%2BLnpvxBqZmUkjsupYNuEIq2mq3pm5W%2F3W%2Btsp2oqbpVU1QRMXD0PlREXon0hAq%2BgM%2BVgjm9fkd7pXF3et8fBam4%2BZBexztan3B1Yy0SIDoPcIk3t0WXrrr7RFnzTGLrdZImxn1jgvXp1EAU5Qs5JbUJ1YsQeUq4hgSdrqK%2FF88mf%2F97peLeqTzkjyU%2B5RLw2ajCiQSB1OchoQmZtSheAVSr1X%2Ftt0zNKXCmpxfYTUmu%2FMAB413ujzgTIYo%2Fatz7wOP9nkFa%2Flr1HTYESY9vBFOOeoYWdCSP2KBQNbuprbaM4VCTgQTsCc6N9zXSy%2BZPy8EkDzYm8b%2BUcTd42%2B0Pkm1G1isW7nkG06lpFZFTxQ5dQbPoyTxzsf0EZicobQ38%2BrajhLzSkBbAikodCPimXh9eXaKyrAo5cjyvWyNhwfDUg5op5gu5J%2F%2F7hYN14C4QD4CIR8gEQWJcZcmnx0tin7n89j%2BIIdhglPI3EaNyH8fnjgaCBvORlsscRhzDRf7aArz3rIuiBmUc7yYCgMiIi0pAgI%2FvgEwr8GK0gY6pgF9wY1ANC2ocZnzsxTNRoRP%2BUqWxv9BEL5mFFg%2BprP7ioT6armX5fTlbQEBSpQ1rSuIBkiVtUR7qgkKpq8X48lyks7Rkka%2FEQ7h0XQSUtKTJ%2F3jURY7i7ULrpbKPgIop0yH6%2FcFr%2BkHyaiqjek1q0TilJ7lxo9GjtMS%2FXDCf1qhbv1YcvBWNG3xLHghO6qTg%2F2uVUAp%2BHmblEjOi5%2BZgpid6QLqH6n%2F&X-Amz-Signature=e328fb70f4e799a29838f0415d1be3e32f4c895b3c801ff499ace736b3b5ba08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
