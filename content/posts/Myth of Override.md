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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2GNN3Q%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T004353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FvZThGW%2BBYiwPmeugqZZGtEcRhLn60Imu0ot3f%2Fy3zAIhAPIPB7NrTGs%2FakrmAMqHNr2rZHto0ZtqSHiz9YmTy7zTKv8DCGIQABoMNjM3NDIzMTgzODA1IgwgHkFh0MVoi4PCwRQq3AOP9SqSHHeVMi0ROPaKFJsKIFUmojXCNhKt5gFvbIjhqxVwEqkjtNIr1V4kFF%2BvKHMiGlmzpbjQlAL0k%2FkY9fx75qwAJItfDaqRyaxvxq6aSezR2JlgmXLAuf19bg5lKnKox0EsDT2ByixIrZ2Rq9Gmdnbts50uqRo4ESChL8ghjbZKfwU3ZDjF8VZR6yvDWZF1VleB2KsPVzKZJEqlFRKluFCS2b1EDppmKy2rnrYgn2p7plomsVCYY2dq7m4rMh42qx9VIP0Uec%2BcAND0cqsjA5Txs1sNE624PH8sUUx6rsCuBjHzyBJAh0AlC1PThTEG5P4qdYlRoKgUGm3Ce8A00ajUhcMmjqxz3fbgtaTxc8pF7bTVNPRzTs3mxd%2B8ijEs4tOFJG3t3VaRHzcMxJQqn1Sk0GRS4A0NcfP%2B0AUQHD52p29omOP2dEmrvLfSC4KvGtFsjxJMOIhu0Y9tUbn%2FSZbEu%2BLUHzwUlIR5Yo2115ZsCzLhZdfMN2BwcLRr5oVR8NQ4Ch9PKh%2Bl%2FwqfPfySRfUxEp4h5s3G5Kui776Xc8lQd4EO3DeMN8p1ZMXoH8XveMHr7blPKPZR7SVSsdIAffGN3wzr61HZ0q%2F15QHERfWNMxF2uHsfoUmf7jD679nTBjqkAY1O15q07dxvIzP86M97%2FPdZU%2BE0R6CGabp1IAV9tky6lw0MV4hF1qBGLN70P%2BxBhpY%2Fnz3szmG%2BMvFWfmgXNy5aIASN8oBu466qTQ0VWdvOPy16kI6EaHWqBN4vWYLcUfpmj%2FVaktBsVj0hv%2BKMNmAkaV2XzLzg%2Bo9acn6TWUzqm64d%2B9LC8RW3d%2BBgxweiQOAOu1nCUDfEfLwVcuu27s81Oqj2&X-Amz-Signature=cfbbffd9d91583bd179e6cf879eba3db1ef46608fc2e50eed7d92f3df26df51b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M2GNN3Q%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T004353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FvZThGW%2BBYiwPmeugqZZGtEcRhLn60Imu0ot3f%2Fy3zAIhAPIPB7NrTGs%2FakrmAMqHNr2rZHto0ZtqSHiz9YmTy7zTKv8DCGIQABoMNjM3NDIzMTgzODA1IgwgHkFh0MVoi4PCwRQq3AOP9SqSHHeVMi0ROPaKFJsKIFUmojXCNhKt5gFvbIjhqxVwEqkjtNIr1V4kFF%2BvKHMiGlmzpbjQlAL0k%2FkY9fx75qwAJItfDaqRyaxvxq6aSezR2JlgmXLAuf19bg5lKnKox0EsDT2ByixIrZ2Rq9Gmdnbts50uqRo4ESChL8ghjbZKfwU3ZDjF8VZR6yvDWZF1VleB2KsPVzKZJEqlFRKluFCS2b1EDppmKy2rnrYgn2p7plomsVCYY2dq7m4rMh42qx9VIP0Uec%2BcAND0cqsjA5Txs1sNE624PH8sUUx6rsCuBjHzyBJAh0AlC1PThTEG5P4qdYlRoKgUGm3Ce8A00ajUhcMmjqxz3fbgtaTxc8pF7bTVNPRzTs3mxd%2B8ijEs4tOFJG3t3VaRHzcMxJQqn1Sk0GRS4A0NcfP%2B0AUQHD52p29omOP2dEmrvLfSC4KvGtFsjxJMOIhu0Y9tUbn%2FSZbEu%2BLUHzwUlIR5Yo2115ZsCzLhZdfMN2BwcLRr5oVR8NQ4Ch9PKh%2Bl%2FwqfPfySRfUxEp4h5s3G5Kui776Xc8lQd4EO3DeMN8p1ZMXoH8XveMHr7blPKPZR7SVSsdIAffGN3wzr61HZ0q%2F15QHERfWNMxF2uHsfoUmf7jD679nTBjqkAY1O15q07dxvIzP86M97%2FPdZU%2BE0R6CGabp1IAV9tky6lw0MV4hF1qBGLN70P%2BxBhpY%2Fnz3szmG%2BMvFWfmgXNy5aIASN8oBu466qTQ0VWdvOPy16kI6EaHWqBN4vWYLcUfpmj%2FVaktBsVj0hv%2BKMNmAkaV2XzLzg%2Bo9acn6TWUzqm64d%2B9LC8RW3d%2BBgxweiQOAOu1nCUDfEfLwVcuu27s81Oqj2&X-Amz-Signature=6125c668f41a262977660f1b96a0bec54e7a865d290e0a1d7a1f165fd27a08d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
