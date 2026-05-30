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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DSGVYBY%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIHXyv5fiycdGB7HBPMAiwfJaBhQMg%2FopDeO9c11CztIcAiEAzVXU4D%2Fhqrgv9DKFDLzEgTR6rETJnJiWG8wXJQ%2FMnSoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBUFdqYBPbI7IGiUGSrcA78svUuvdiUkAD3U9hlZ%2FwUHE4JSjmKKMrq5UcTY6VXmvP9ZcGXShv8njJP2L1Cs7bZf6mZFEzDZRVtn5qutSM0NU67AvkY3Df3yGM9l%2Bt1A1oaNbNywm176VAP4Aks7G80GDVS0ltrKWRKp4GDDDFDngRibHuWDmqeg7TuFMqh9uj2uUP4GIzzRA07AivF2U3Qf41XEt57qrcML7vNtXYgJKMZwjN83ium%2FOzerhQqasXIcklrgf2vvA11qccJX%2FAqqlYHjDY2jDSrcN1qKDz2r9%2FlQ7MqfY%2FGxmKIp9RDJl2onE8GaI0O3pwjjsal968nvc0WhyWF377C27AXyZwEMP3BYci0cXH8T28TYghZgfrNfswGFBNCQD%2BDfMe6UsM%2BNcTlfi4RNyBLd%2FWzu%2F%2Fm3ReNmrjluhHo1mjs3QWHDY6nP6rELNGZhrEtoPKn3B9JWIQ4WWU2I8XWh9RT7k8SuZaRjfmaWdgcc0w3SBN9Z%2Bc7trPhABB%2Bmwpu5XWmre7K%2F9oS1h92vAmSyp0M%2F2aEVK54nUsRh27vzBPzmm19yk66E2mkin7487u0dO9t1gawU5XONEcNPo7WH8Penj2kR%2B3vUpm52mUwqjqJFNIwdVYFciubwlbSi4qo9MM776NAGOqUBCYpKkYS5sMrdxIxTUu38%2FWsjm9RjkMebWbZk5W9reS%2F7bBcpE13KIHijxu2WynFEAB%2FN6ipwwDQdZPIGepaIvy1pdpWBLoFuVSRYU0%2F4B7us80h0mz153tAox%2FTiaHjil24e9tZ6pUquuYTHq%2B%2FB5wljxk2iyf7Gx9bECZFR8J%2F%2FxlpdlTQLcc8%2BvJzwKf5U2yF1VDBE8EPONLl9ukNEGqNeBQ0x&X-Amz-Signature=8ca46f89db88040bf95ea0b93407ba2c8e3059502f02423a4c1043cedc034ffc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DSGVYBY%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T015408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIHXyv5fiycdGB7HBPMAiwfJaBhQMg%2FopDeO9c11CztIcAiEAzVXU4D%2Fhqrgv9DKFDLzEgTR6rETJnJiWG8wXJQ%2FMnSoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBUFdqYBPbI7IGiUGSrcA78svUuvdiUkAD3U9hlZ%2FwUHE4JSjmKKMrq5UcTY6VXmvP9ZcGXShv8njJP2L1Cs7bZf6mZFEzDZRVtn5qutSM0NU67AvkY3Df3yGM9l%2Bt1A1oaNbNywm176VAP4Aks7G80GDVS0ltrKWRKp4GDDDFDngRibHuWDmqeg7TuFMqh9uj2uUP4GIzzRA07AivF2U3Qf41XEt57qrcML7vNtXYgJKMZwjN83ium%2FOzerhQqasXIcklrgf2vvA11qccJX%2FAqqlYHjDY2jDSrcN1qKDz2r9%2FlQ7MqfY%2FGxmKIp9RDJl2onE8GaI0O3pwjjsal968nvc0WhyWF377C27AXyZwEMP3BYci0cXH8T28TYghZgfrNfswGFBNCQD%2BDfMe6UsM%2BNcTlfi4RNyBLd%2FWzu%2F%2Fm3ReNmrjluhHo1mjs3QWHDY6nP6rELNGZhrEtoPKn3B9JWIQ4WWU2I8XWh9RT7k8SuZaRjfmaWdgcc0w3SBN9Z%2Bc7trPhABB%2Bmwpu5XWmre7K%2F9oS1h92vAmSyp0M%2F2aEVK54nUsRh27vzBPzmm19yk66E2mkin7487u0dO9t1gawU5XONEcNPo7WH8Penj2kR%2B3vUpm52mUwqjqJFNIwdVYFciubwlbSi4qo9MM776NAGOqUBCYpKkYS5sMrdxIxTUu38%2FWsjm9RjkMebWbZk5W9reS%2F7bBcpE13KIHijxu2WynFEAB%2FN6ipwwDQdZPIGepaIvy1pdpWBLoFuVSRYU0%2F4B7us80h0mz153tAox%2FTiaHjil24e9tZ6pUquuYTHq%2B%2FB5wljxk2iyf7Gx9bECZFR8J%2F%2FxlpdlTQLcc8%2BvJzwKf5U2yF1VDBE8EPONLl9ukNEGqNeBQ0x&X-Amz-Signature=a4971d67cca6477dad5976f135b55dcaab1765a5f3771a63c1979e393e9e6e57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
