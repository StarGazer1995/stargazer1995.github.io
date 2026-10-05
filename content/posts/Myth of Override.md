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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WISSLY%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T001830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIFf1UcvJzGVUbKFVmgdNBvRx%2B%2Fc5WAkBA4KRNvuwpTY6AiBsENk6z9giWOtAV6%2BBL8%2BI6NwN5OwvvztJ9YFkE4CeCSqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3LZZBDHdaOP%2FRHlIKtwD8gIO1d4PbUDaj2tV3O8U4hFgcrYrsFcsioy%2FI%2B7%2FP4fnIqaDE2Rt5wgJkj3W1Zx7xXTQILcEyBH14PkKyzdnzG86HftccK0PWop6Mc%2FjT9XQfLBYnvlWyEOmD6vGtAYuTcwHIDBdpmN2fKivbZYoSIm3uE9UfMElGSFM6%2FbCAyorZi2moOb52AKiqIg2cWwfc92F5C47%2B9G1RfXgNwLYhQoN%2Btc7rHiJb9PRZ1PSeyGGt2%2FbvEQLeXR9JXP%2BZztVKE6k9cjHyteUkY%2FVS5fK3ZK893lJWqpU5leujtJmN4P3KsPNcn8QxIVehABcUIQ3NU7%2BfHTfoAHr0Gr4g40oqt85SGb2Bh9tzkwiMUjjXDktfXpF6kXPLH4t8YQYxsYTbof81%2Fuuv5PrlmzTeSCDKocNgZw8YrgvDB6CdfmWomPH1wP8QZqbUeW6PrqpXNJWlpjVJ%2Fr5gCBhMdNif5Pi8e2LpjY%2Fd8sJQ%2BkdULLp6Yj2SN3hYxHtR2UGkNmv895pMCGG7HYnl%2BnpVk5iyIbSmMtq%2Bck3YymbbnfJYEF%2FHdLxAD%2BJw57WraGrhyYGlqEgls63CsaQ%2B7mPE8ZoLR1%2BzKDMOJVn6f5qbJ0gK2UpLJQDbwVux9xswB3jlcQwu5uL1gY6pgHl2d%2F6uOlPf%2FUptTtiA165Xdzo3l%2FYftoQTq3UOq2KJhk6vUFDq9nSwAl4xaXU%2FSh4ItMNMB94Hl7hI1rA1lOCqN6yRKNbo5yFeMDz10jmq5wGPk9qPI0gY11iBWSw0aoi%2F09Wm2b4MV7W9Bk3WZtFQO%2FCMNq9OVdo%2FmAPR0uuxgzjS3Z9ikkg4a%2FfXFQr2XRr1%2BjMBN8%2BzhOcc4ZFPvF06gTuuIs0&X-Amz-Signature=9bbc2dd1e1543e577d8928850cfccacf5c6ec80bae4547755bb33464a61fd41d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WISSLY%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T001830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIFf1UcvJzGVUbKFVmgdNBvRx%2B%2Fc5WAkBA4KRNvuwpTY6AiBsENk6z9giWOtAV6%2BBL8%2BI6NwN5OwvvztJ9YFkE4CeCSqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3LZZBDHdaOP%2FRHlIKtwD8gIO1d4PbUDaj2tV3O8U4hFgcrYrsFcsioy%2FI%2B7%2FP4fnIqaDE2Rt5wgJkj3W1Zx7xXTQILcEyBH14PkKyzdnzG86HftccK0PWop6Mc%2FjT9XQfLBYnvlWyEOmD6vGtAYuTcwHIDBdpmN2fKivbZYoSIm3uE9UfMElGSFM6%2FbCAyorZi2moOb52AKiqIg2cWwfc92F5C47%2B9G1RfXgNwLYhQoN%2Btc7rHiJb9PRZ1PSeyGGt2%2FbvEQLeXR9JXP%2BZztVKE6k9cjHyteUkY%2FVS5fK3ZK893lJWqpU5leujtJmN4P3KsPNcn8QxIVehABcUIQ3NU7%2BfHTfoAHr0Gr4g40oqt85SGb2Bh9tzkwiMUjjXDktfXpF6kXPLH4t8YQYxsYTbof81%2Fuuv5PrlmzTeSCDKocNgZw8YrgvDB6CdfmWomPH1wP8QZqbUeW6PrqpXNJWlpjVJ%2Fr5gCBhMdNif5Pi8e2LpjY%2Fd8sJQ%2BkdULLp6Yj2SN3hYxHtR2UGkNmv895pMCGG7HYnl%2BnpVk5iyIbSmMtq%2Bck3YymbbnfJYEF%2FHdLxAD%2BJw57WraGrhyYGlqEgls63CsaQ%2B7mPE8ZoLR1%2BzKDMOJVn6f5qbJ0gK2UpLJQDbwVux9xswB3jlcQwu5uL1gY6pgHl2d%2F6uOlPf%2FUptTtiA165Xdzo3l%2FYftoQTq3UOq2KJhk6vUFDq9nSwAl4xaXU%2FSh4ItMNMB94Hl7hI1rA1lOCqN6yRKNbo5yFeMDz10jmq5wGPk9qPI0gY11iBWSw0aoi%2F09Wm2b4MV7W9Bk3WZtFQO%2FCMNq9OVdo%2FmAPR0uuxgzjS3Z9ikkg4a%2FfXFQr2XRr1%2BjMBN8%2BzhOcc4ZFPvF06gTuuIs0&X-Amz-Signature=7c984e95ff0286ecd89e687976a65f2d95f1d825c4282c2eee8bdc3c4aed6175&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
