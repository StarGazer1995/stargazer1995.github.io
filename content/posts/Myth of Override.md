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

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">code_examples/cpp_examples/01_myth_of_override/src/main.cpp at main · StarGazer1995/code_examples</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;">Contribute to StarGazer1995/code_examples development by creating an account on GitHub.</div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://github.githubassets.com/favicons/favicon.svg"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div><div style="flex: 1 1 180px; display: block; position: relative;"><div style="position: absolute; inset: 0px;"><div style="width: 100%; height: 100%;"><img src="https://opengraph.githubassets.com/24dae9f0ad65ae788f1f405a6204e98dbfd21a90718b49e4873c8a534314d035/StarGazer1995/code_examples" referrerpolicy="no-referrer" style="display: block; object-fit: cover; border-radius: 3px; width: 100%; height: 100%;"></div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPQUSLUD%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6LlpqGUarJh%2FnloUSKveFzy94hkCtK2j0nIRPVuxhzAiAG164QxipN8vb1dtT7tT5Qv%2BG6Ys4sPhInWTvbDJk92ir%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM46GGzXgEgLG4Xw7mKtwDgULtyfx0%2FmxvCI73WQ420tCJ3fo8oWCKh5xEDYq1W7huO9rSebsusPzJl5kKtKeqtqdHrpsr9dTDX0ZxBnRtwLh3RUZiKhZrCbWtSBIzkdrAA5p6mx%2FgBDWx2jP4t4DNA6buNpAYHkgN%2FdWGXD0pqOczLhA3AIYy6gCrdpvvkIxjrjX9Y%2Fz6dFQmUPX27JJMHND1ELyckkLCVb2QtMzDMb6d6bhVLuvnwtMrtcYuQ3QXXmkjd7LVgERPH3I0SMIYr6vz2zbyDy4Q0hWwNG5U5zEdUlhIPlInnLxhApfEzTbNF7cHvwtune6E%2Beg3LsqRzvidlv%2BSlFA%2BTbkemxstZscd%2BAFRavnBhIwimiiDCcRvB4MW5p9xTXa47pTJTXUKg6EshZ7gjNsCvWfSwRXdAG5jbRHf4%2BThcULWJMYZVpaasChekAvSlp5h6tDBm9uLpVuCu2y%2F5iHO1V%2B9z0pMSZKXvIk1KngRLh5Qwuc0n3oJYLHJN5Y%2B%2F4BSe8GOnzSSJDKTHhe%2FfpbmPpnIaR9n4rSh5Mrhmg5eOpkMh4EzQrkaURqdeohvMgRjuDlj%2BGUhHsSpf6pGpD0%2FbNT3T%2Bh7Rq8eoWN%2FWzd9U%2FKkj0rxp94SfKc9M4OXGxNsHBkw7%2By2wAY6pgF0ipIi49VyVZ4WZeQPfgGLsVUGDKbS6K6OmRTpGIULk138SyfITOS4sEoJXMCMVdVpeykL8ctwFldT%2FNgyV%2Fx9BFcMa%2FdMgHTnD%2BT3TMA31YgIAFiTCLFUME0KbHhY6URcKLc2FHAXhY3OPHZ07R0mjSzHA9gNR%2FX0T5Hg7dKDMjbm0YiZHCA4Klgk2dFqPorwatE%2F7dosRW3mYUjx5ID7qIDs8Goo&X-Amz-Signature=56a981784ae605ac3c4cad53e2c92b914c1d6d0dc7da23d4b2b10bfda91d2bfb&X-Amz-SignedHeaders=host&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPQUSLUD%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6LlpqGUarJh%2FnloUSKveFzy94hkCtK2j0nIRPVuxhzAiAG164QxipN8vb1dtT7tT5Qv%2BG6Ys4sPhInWTvbDJk92ir%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIM46GGzXgEgLG4Xw7mKtwDgULtyfx0%2FmxvCI73WQ420tCJ3fo8oWCKh5xEDYq1W7huO9rSebsusPzJl5kKtKeqtqdHrpsr9dTDX0ZxBnRtwLh3RUZiKhZrCbWtSBIzkdrAA5p6mx%2FgBDWx2jP4t4DNA6buNpAYHkgN%2FdWGXD0pqOczLhA3AIYy6gCrdpvvkIxjrjX9Y%2Fz6dFQmUPX27JJMHND1ELyckkLCVb2QtMzDMb6d6bhVLuvnwtMrtcYuQ3QXXmkjd7LVgERPH3I0SMIYr6vz2zbyDy4Q0hWwNG5U5zEdUlhIPlInnLxhApfEzTbNF7cHvwtune6E%2Beg3LsqRzvidlv%2BSlFA%2BTbkemxstZscd%2BAFRavnBhIwimiiDCcRvB4MW5p9xTXa47pTJTXUKg6EshZ7gjNsCvWfSwRXdAG5jbRHf4%2BThcULWJMYZVpaasChekAvSlp5h6tDBm9uLpVuCu2y%2F5iHO1V%2B9z0pMSZKXvIk1KngRLh5Qwuc0n3oJYLHJN5Y%2B%2F4BSe8GOnzSSJDKTHhe%2FfpbmPpnIaR9n4rSh5Mrhmg5eOpkMh4EzQrkaURqdeohvMgRjuDlj%2BGUhHsSpf6pGpD0%2FbNT3T%2Bh7Rq8eoWN%2FWzd9U%2FKkj0rxp94SfKc9M4OXGxNsHBkw7%2By2wAY6pgF0ipIi49VyVZ4WZeQPfgGLsVUGDKbS6K6OmRTpGIULk138SyfITOS4sEoJXMCMVdVpeykL8ctwFldT%2FNgyV%2Fx9BFcMa%2FdMgHTnD%2BT3TMA31YgIAFiTCLFUME0KbHhY6URcKLc2FHAXhY3OPHZ07R0mjSzHA9gNR%2FX0T5Hg7dKDMjbm0YiZHCA4Klgk2dFqPorwatE%2F7dosRW3mYUjx5ID7qIDs8Goo&X-Amz-Signature=2202cd56c732b1ef9982dd812f36e1b22eccc722c7604bfdf69d740f1e1c2bd1&X-Amz-SignedHeaders=host&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">virtual function specifier - cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://en.cppreference.com/favicon.ico"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
