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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJGT6T5%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T182110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFerR9PfN4ZpCgDeH4DwOz%2BB5ufnnEhW%2F2e%2BEBpkt5VJAiEAr0hp1Vl7PzjAjyCpcgYieRXGZIMJpCOvJd3WxhsBC0YqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCIbNmMm%2F7sBsOvd9ircAyeieoKRWb9ZiL1bfUoxsFqU1BRWPwFoxRRxJwYJQ7yyvqZ%2F60iKzPTufaawmdr9DET35bLL6kFwRAUI0J6soeTRk39Xjp2MmjOctfoJNZEdlTnJvkVpNDrAr%2Fal8pqdTtP%2BKQi%2Fzte0mGP558ixVhBBSwKnEnLtahTAhvj%2FluMkLQDi%2BAndvr3fsmXyKYkplHlr5UVWMu0oFa4yHrhk9oAma%2Fkm%2BxemVNe%2FQPSqygjID9gqI2yL%2F9JbRFdbx29oHG9TYARLbMewV7nti8WLeW5AywfjRjLnBqgYPTqN51aiKZwg8U%2FdVYDKMqs7Wj%2Bsh6cDwSyUQDfvMSgEPeoX1OSi7%2F9yXnOybn8KsgKjFQ4IzmLmne77iWFSED8b17LrD5blQmpLy67pL3uYRn4G7N%2BVsrrm7Su2sTJzencxDq72Qw4FSoLPU8HqbuspzCUtIPmBNFqgobHmTGVDENf7cYRIt9wHrgkeWqExYVnB3CiGxQWOs76Iwo%2B%2FrPFKmUyo0Izinplz1R5FY%2FkTeip%2B9hFSS40IgWc99wHZafBzrB4c4T5f3HplNOa4h67aVA6XO0uwYp68hl%2FLK6vcg5n4o8uhGRGHVlt%2FRSnkyen2ju6wUfeYBV0FtCPXwPxoMJbknNQGOqUBjgUvsTJkl%2BuraDyPpdwPY8qR74p5DJIq8fBgbAeNEuoV7PknHL0RyZuqACtS5gKH%2FpVc565qLgEPAdtgahfSKBdOkhQ9pSAFWJYb%2F%2B9nImjqKsk5IyNnz%2F1iuBsVcoidWNU5ZQA2BBr5C3qCSyBt1n2gTxup%2BOPKrnQv9Q5vlBqhMNlPhm3BKbLRb1v87KjKpJxc2an8Ga61p93ft618qSqoTWjO&X-Amz-Signature=ecea1c353a0ba29c811376c7f554d761ded64d5717842e878bfba27ca44c1daf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDJGT6T5%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T182110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFerR9PfN4ZpCgDeH4DwOz%2BB5ufnnEhW%2F2e%2BEBpkt5VJAiEAr0hp1Vl7PzjAjyCpcgYieRXGZIMJpCOvJd3WxhsBC0YqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCIbNmMm%2F7sBsOvd9ircAyeieoKRWb9ZiL1bfUoxsFqU1BRWPwFoxRRxJwYJQ7yyvqZ%2F60iKzPTufaawmdr9DET35bLL6kFwRAUI0J6soeTRk39Xjp2MmjOctfoJNZEdlTnJvkVpNDrAr%2Fal8pqdTtP%2BKQi%2Fzte0mGP558ixVhBBSwKnEnLtahTAhvj%2FluMkLQDi%2BAndvr3fsmXyKYkplHlr5UVWMu0oFa4yHrhk9oAma%2Fkm%2BxemVNe%2FQPSqygjID9gqI2yL%2F9JbRFdbx29oHG9TYARLbMewV7nti8WLeW5AywfjRjLnBqgYPTqN51aiKZwg8U%2FdVYDKMqs7Wj%2Bsh6cDwSyUQDfvMSgEPeoX1OSi7%2F9yXnOybn8KsgKjFQ4IzmLmne77iWFSED8b17LrD5blQmpLy67pL3uYRn4G7N%2BVsrrm7Su2sTJzencxDq72Qw4FSoLPU8HqbuspzCUtIPmBNFqgobHmTGVDENf7cYRIt9wHrgkeWqExYVnB3CiGxQWOs76Iwo%2B%2FrPFKmUyo0Izinplz1R5FY%2FkTeip%2B9hFSS40IgWc99wHZafBzrB4c4T5f3HplNOa4h67aVA6XO0uwYp68hl%2FLK6vcg5n4o8uhGRGHVlt%2FRSnkyen2ju6wUfeYBV0FtCPXwPxoMJbknNQGOqUBjgUvsTJkl%2BuraDyPpdwPY8qR74p5DJIq8fBgbAeNEuoV7PknHL0RyZuqACtS5gKH%2FpVc565qLgEPAdtgahfSKBdOkhQ9pSAFWJYb%2F%2B9nImjqKsk5IyNnz%2F1iuBsVcoidWNU5ZQA2BBr5C3qCSyBt1n2gTxup%2BOPKrnQv9Q5vlBqhMNlPhm3BKbLRb1v87KjKpJxc2an8Ga61p93ft618qSqoTWjO&X-Amz-Signature=dc3bc3d82d086f68450779d95b79591d6cc1c6f794e5b3e089bd2f6a50df37fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
