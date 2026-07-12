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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T6IEEXY%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T051456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIBqzn7uMnIDPCloul%2FKkRByqCiQ8EPR1PN7J%2BYeWuMW4AiBP%2BiYRHXQ6ikcxFooTvVW85XTME6Y7heGuDjdEG921SiqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMchwZ9NBTI65wT8zIKtwDP2ItYSmgNu9yvXXuLMZVaHmsSTPPIvQ8K1KXPkaV3%2F%2BVNqePCsBDCCS5hI0nyePTPsKBezVBNqX8d4ysM%2B42yi8qOhQqwal%2FVESFkjgCAt1ynr6OEm7itGOtvmIjHC76xtKHj9ep6jpvIUt60FWc4oI4VpXo0MWV8GPDvDDXzr7%2B%2Fz%2FImyRhcpGQnAeysPA6MwWTQqhUfax3%2BZ7eD5ycsyWunYCacgSJ3WQJrxHqKXkOATeeorEhNLABhXb4t%2BTHKTedTFeaJDLYvusMNAp6%2Ff5TT4SncRQV7DzO79%2B3kTMwUZxb5%2FSDkgAKmpuM7gOk1%2BNZFcbIJOUHHalKTQNxOyw1OuN0lNNBEU6derXCaULTXwePZ6iGS1xJrqBaBmrLcbIZQE7ZCGr2SRKZRGI%2BFDSoVZ12TxXotvgSso7gK3bI4eVLd9kbmTm7%2BPKvvyIPL%2FUi3kcpKzXkcUhr03cIAqytvuOln9ZWnSFsGJb5fwUzsVoHoBKBDmBB1uFSMsG5rAIo34rQOJC9J5ImqIaDGguMAiZ7owGYNN74OxBJvYImzLfZXoJXMfPkvhclupLuuhlOEFuWpdY5VGXTiLgUQHkDTgEpSzy05TNCixZVe%2FE61jj%2BtIJUBL38w%2FQwy6%2FM0gY6pgH5QzQbfqaV8%2FNikmtYyTRbDN%2BZwnChbsaErf5rIuird%2BuJz7cefZAvbTivcchmZ72Z3sWgoi%2BzxA7%2BF0beT%2Fqsa8i9%2Fg%2BB7HofpLStKZWa9xjp83%2BnZTTdvG7%2BcXN3BBPGDMoU5rtsPmis3MUYd2SL8A5O19fC%2BasbnBVKfNH5z3aJQnpD4XGbnF2ruod6Yt8ib1uzaUN97obk%2BDHCtcVySKaNvJVr&X-Amz-Signature=50eff4f8a54d4d7d494685edeb9414a183c1a313ab94fdd25c788185b55b9e85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T6IEEXY%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T051456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIBqzn7uMnIDPCloul%2FKkRByqCiQ8EPR1PN7J%2BYeWuMW4AiBP%2BiYRHXQ6ikcxFooTvVW85XTME6Y7heGuDjdEG921SiqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMchwZ9NBTI65wT8zIKtwDP2ItYSmgNu9yvXXuLMZVaHmsSTPPIvQ8K1KXPkaV3%2F%2BVNqePCsBDCCS5hI0nyePTPsKBezVBNqX8d4ysM%2B42yi8qOhQqwal%2FVESFkjgCAt1ynr6OEm7itGOtvmIjHC76xtKHj9ep6jpvIUt60FWc4oI4VpXo0MWV8GPDvDDXzr7%2B%2Fz%2FImyRhcpGQnAeysPA6MwWTQqhUfax3%2BZ7eD5ycsyWunYCacgSJ3WQJrxHqKXkOATeeorEhNLABhXb4t%2BTHKTedTFeaJDLYvusMNAp6%2Ff5TT4SncRQV7DzO79%2B3kTMwUZxb5%2FSDkgAKmpuM7gOk1%2BNZFcbIJOUHHalKTQNxOyw1OuN0lNNBEU6derXCaULTXwePZ6iGS1xJrqBaBmrLcbIZQE7ZCGr2SRKZRGI%2BFDSoVZ12TxXotvgSso7gK3bI4eVLd9kbmTm7%2BPKvvyIPL%2FUi3kcpKzXkcUhr03cIAqytvuOln9ZWnSFsGJb5fwUzsVoHoBKBDmBB1uFSMsG5rAIo34rQOJC9J5ImqIaDGguMAiZ7owGYNN74OxBJvYImzLfZXoJXMfPkvhclupLuuhlOEFuWpdY5VGXTiLgUQHkDTgEpSzy05TNCixZVe%2FE61jj%2BtIJUBL38w%2FQwy6%2FM0gY6pgH5QzQbfqaV8%2FNikmtYyTRbDN%2BZwnChbsaErf5rIuird%2BuJz7cefZAvbTivcchmZ72Z3sWgoi%2BzxA7%2BF0beT%2Fqsa8i9%2Fg%2BB7HofpLStKZWa9xjp83%2BnZTTdvG7%2BcXN3BBPGDMoU5rtsPmis3MUYd2SL8A5O19fC%2BasbnBVKfNH5z3aJQnpD4XGbnF2ruod6Yt8ib1uzaUN97obk%2BDHCtcVySKaNvJVr&X-Amz-Signature=8803c3224a9ffb37be3e038c6837ea7b6b3a8cf62be5a35e8f7eb1c090a4cb43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
