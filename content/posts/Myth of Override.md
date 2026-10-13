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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL65UNMA%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T083854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAwm1YwpmU3rWPi6pdamASAVHFKwBLifhi8mhMW21o5AiAhnKGB0ynj1JppSqu3XdDqIqmt0wOz1DKBK1j5r4yezSqIBAiY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4tOVtiQmvcjlo23qKtwDqGaxb6aYq%2BhYLgxtAe7NUtHrB5cfF0Z7FSrSxSjFo3FCRkiYw9GeP934IWlauPzt1xoU%2BaSjcqs4jJr0nMD6z1Cnv%2F3vR7VfLiS%2BRkTf5tGAOZfvHOdrhviPr4KXD%2FNefe%2Bl84jrFiqm6Gf5jBqhIEbvUFsRzNBvS36CGvPNwuOzdD9Xs5JaVFYi1Bdx0XFBEKXG6V0XDsrtRmdeeteQP9R0Fb%2B1smycuxJv2RojvREWwyJirEPm%2B57eS%2FF%2FxKQZPInv2nwRsj4TDyZlMufN8eepYsAZ0WPNjMmGOvmcKtooujOcyKsXbezDEiN7NlRg5Kk%2FjBwRLQgf2SWe19t9uDmmi77UXJoiLmIqMswMbnKwAyPOrw1iMHmn1LtgBR2YzC7jv9zEx3zW6NCqjSCkSLpY%2B7F79rfQSbzwP90QBMZP3bobNsg5xpVxfgdD8gtXbHrQIyA74tFnH%2FO3knvJ9XiPy3TSA5draeoWZ1VHqAJnaHP3tmmN8uDaRSIIB0Ba9sZ9b16AgYXnBF9XSRejKNT9bh%2B73Rqlz7VxbvCKM2SSjh2FrZrd%2FKrqLlgE1AHVDiQ9%2BJkQmuacbwEDiCnQSzG5nfMNxleXwUBYCqEhBRzb643cQVa3yKGoYqkw7bi31gY6pgHV9mc4NP6N98lz%2BbQ4L8rZ%2BQu%2BpWGvU2XAIlceFWwaXtXTug4sC9zVm4riDsQMgTcYQ5G%2FkUa05AolK4cwMPFukyxw43Bek3ZRiMx7EK2m1h9Lz8XQzq49JEWq40p6itbF2r2pTjyFWe%2BZoWnkV3R004RGIDUQF8HEjNLmU9%2FTYEHGqcKKB8f9Di0EG4eoytsO8fEL0GW14nf22SQrkFBkvCRhWiUm&X-Amz-Signature=300bf93aa4c120f7f1e02cb575bb596765812afd04ffa4b51f0d7a6d77eb01fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL65UNMA%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T083854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAwm1YwpmU3rWPi6pdamASAVHFKwBLifhi8mhMW21o5AiAhnKGB0ynj1JppSqu3XdDqIqmt0wOz1DKBK1j5r4yezSqIBAiY%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4tOVtiQmvcjlo23qKtwDqGaxb6aYq%2BhYLgxtAe7NUtHrB5cfF0Z7FSrSxSjFo3FCRkiYw9GeP934IWlauPzt1xoU%2BaSjcqs4jJr0nMD6z1Cnv%2F3vR7VfLiS%2BRkTf5tGAOZfvHOdrhviPr4KXD%2FNefe%2Bl84jrFiqm6Gf5jBqhIEbvUFsRzNBvS36CGvPNwuOzdD9Xs5JaVFYi1Bdx0XFBEKXG6V0XDsrtRmdeeteQP9R0Fb%2B1smycuxJv2RojvREWwyJirEPm%2B57eS%2FF%2FxKQZPInv2nwRsj4TDyZlMufN8eepYsAZ0WPNjMmGOvmcKtooujOcyKsXbezDEiN7NlRg5Kk%2FjBwRLQgf2SWe19t9uDmmi77UXJoiLmIqMswMbnKwAyPOrw1iMHmn1LtgBR2YzC7jv9zEx3zW6NCqjSCkSLpY%2B7F79rfQSbzwP90QBMZP3bobNsg5xpVxfgdD8gtXbHrQIyA74tFnH%2FO3knvJ9XiPy3TSA5draeoWZ1VHqAJnaHP3tmmN8uDaRSIIB0Ba9sZ9b16AgYXnBF9XSRejKNT9bh%2B73Rqlz7VxbvCKM2SSjh2FrZrd%2FKrqLlgE1AHVDiQ9%2BJkQmuacbwEDiCnQSzG5nfMNxleXwUBYCqEhBRzb643cQVa3yKGoYqkw7bi31gY6pgHV9mc4NP6N98lz%2BbQ4L8rZ%2BQu%2BpWGvU2XAIlceFWwaXtXTug4sC9zVm4riDsQMgTcYQ5G%2FkUa05AolK4cwMPFukyxw43Bek3ZRiMx7EK2m1h9Lz8XQzq49JEWq40p6itbF2r2pTjyFWe%2BZoWnkV3R004RGIDUQF8HEjNLmU9%2FTYEHGqcKKB8f9Di0EG4eoytsO8fEL0GW14nf22SQrkFBkvCRhWiUm&X-Amz-Signature=75cc82bf6e6b802f5d487c6d77c1c21e4a93e0cbed5845b9acc5bb43dcbeda2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
