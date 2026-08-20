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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJRPZPEV%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T024759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRlDZcBohbYq6WErQ1g90LqkhWhl5ycL1d8J4HV0PwewIgNC1ULriFJwcY9zc85YJaqGVNfBQ%2BTVZhenf0WA93msEqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE29znKru4DxGemZ8SrcA5PWNsBAF4U13fLTQWhg9ZwBL66OWCexJLAhbZYgATdf50UXXmiwvObm09kaFaFcrSe%2BBuBoVFCqRq3GGnU9%2F8QRdBZfrdQEP88qiwCU55jSnmaRZIJCjGBbn2uBxODKHabX3Xl2Pcg3MSpxMzkYlnvPulFG%2BVJDB51j%2FJDegOYKshoB9vGSHSq0oyWTnV3zk1yfVZ6AjdPp%2FzIOE0lCQbNCVTZPfMApf4GQPdMiN%2BUpruTvidx6JWOGgp6EAQMVCdDMdanjj3VsUmxPjPFV6%2F6WmAiDV%2B4xslC%2B5dciGL8mm%2BrAlBHhejXXSCPIpI2hf1hcqkqKJMzD6L1dvn5x1gYnnowyWfHsEeA%2FOsSeUegRIApUM0%2BMnedWe3myCsHzEw6eK12rLmfzaZ8BlYK0PrQhTUIsAnOmzj9L8xgwNZsUwoU8F39MXcV6fbToRvcbUXsx3VyMgtX%2FSzDSv4Ka%2FsSpTavPVFVcu7JI4zXOoco0PH5ht4whU4bChYlzM5vqDjDLbbFFoET2lO23uSv0QJevaiCa5zvI%2BAqMMN3gqQpt3ak%2Biv9xwZlxseUw41%2FdNX1MBlA8zq4Lwdjyv7mujRpkCbm74Ge5WdBQ%2FH5JKcQKkFOIVcAGy0FBFUAKMLXrmNQGOqUBvhTESlkufDCreLLprlwDitYLwJscB69nuuF9cJWKMSkyXePG3Nvhv%2FaLbOxo9lSl779lmcHvh91Po%2FLULlvPost9XdZ7r6vfPr8weffENFjHxuknfVvAlbuySzZOYKrsM5D8uQ9Xk3VidEKXZ4BY%2FROKvdFn97L3NyLxxuiym7S%2BhBfTWhtC%2FeEe3KFo0N%2Bj6OdR9eOWSJ60qFa2%2BdQ%2BObFzS7iH&X-Amz-Signature=fa9b8a3b7d1651896c8d5dae2e658f57e26c6e7f6f4b02bef61687df4534d514&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJRPZPEV%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T024759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRlDZcBohbYq6WErQ1g90LqkhWhl5ycL1d8J4HV0PwewIgNC1ULriFJwcY9zc85YJaqGVNfBQ%2BTVZhenf0WA93msEqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE29znKru4DxGemZ8SrcA5PWNsBAF4U13fLTQWhg9ZwBL66OWCexJLAhbZYgATdf50UXXmiwvObm09kaFaFcrSe%2BBuBoVFCqRq3GGnU9%2F8QRdBZfrdQEP88qiwCU55jSnmaRZIJCjGBbn2uBxODKHabX3Xl2Pcg3MSpxMzkYlnvPulFG%2BVJDB51j%2FJDegOYKshoB9vGSHSq0oyWTnV3zk1yfVZ6AjdPp%2FzIOE0lCQbNCVTZPfMApf4GQPdMiN%2BUpruTvidx6JWOGgp6EAQMVCdDMdanjj3VsUmxPjPFV6%2F6WmAiDV%2B4xslC%2B5dciGL8mm%2BrAlBHhejXXSCPIpI2hf1hcqkqKJMzD6L1dvn5x1gYnnowyWfHsEeA%2FOsSeUegRIApUM0%2BMnedWe3myCsHzEw6eK12rLmfzaZ8BlYK0PrQhTUIsAnOmzj9L8xgwNZsUwoU8F39MXcV6fbToRvcbUXsx3VyMgtX%2FSzDSv4Ka%2FsSpTavPVFVcu7JI4zXOoco0PH5ht4whU4bChYlzM5vqDjDLbbFFoET2lO23uSv0QJevaiCa5zvI%2BAqMMN3gqQpt3ak%2Biv9xwZlxseUw41%2FdNX1MBlA8zq4Lwdjyv7mujRpkCbm74Ge5WdBQ%2FH5JKcQKkFOIVcAGy0FBFUAKMLXrmNQGOqUBvhTESlkufDCreLLprlwDitYLwJscB69nuuF9cJWKMSkyXePG3Nvhv%2FaLbOxo9lSl779lmcHvh91Po%2FLULlvPost9XdZ7r6vfPr8weffENFjHxuknfVvAlbuySzZOYKrsM5D8uQ9Xk3VidEKXZ4BY%2FROKvdFn97L3NyLxxuiym7S%2BhBfTWhtC%2FeEe3KFo0N%2Bj6OdR9eOWSJ60qFa2%2BdQ%2BObFzS7iH&X-Amz-Signature=a0fc8123587a38dcb3448f8a337357efcc474ca348d76f3e8aa1fa7a78fe32cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
