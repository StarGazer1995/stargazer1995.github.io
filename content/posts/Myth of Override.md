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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP4SX54Q%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T135752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdY8fKDcrVs0euTF7d1fbwDSj00npNceY4zVV26U58qgIgaFkr%2B%2FQb%2Bo7KhXoPavzyKcm%2Fp93jcaKa4RghRc4z0HQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDNow59ZWQJ83yzcQGyrcA0YwWAaQGjF05rXYWF62WzYc5vQA3Fc7nVg%2BrwRiEFk13jm47WWHZtni1B5oeDvfDnbXrfdGAYqxMP1sNbaG6CDzKAdkL3d358%2F2dMxlXrG4EXGB2l9Swv73GXejUKFusqq32SxPCcEeIIY86sKAv8MZWBEpqSovu6nXP599%2FKjZYBJh5JpfG3NHBK9fagUiDl7i%2FuRZ8fWmtn%2B838ufQHYML%2FoOt8shqiqS%2BWMwxaUizt30FNKpeRgrWnvJNqQTot%2FdSC6TJUZh8DVei8zLFgDLzdgD82A%2FcGTvFcm4Kga5AZbRnYLVbbPb3nEtUVi3nigONMGi%2BWiCQTQ7WEq8Y7b2OFvKWFnjlKL%2BmFfXBplG5TLKd0drR55IvP0KA1q968PIVxPPifrKrghB3TTCIC4sOYjLmJFQOwFhW9xrwYzJgmEaXTR7oikBQLvKLJ708vT1hQ1ce1gHkhVJ%2BHqKkcafc0yHNXIKTm1lBbKNYgFAeh7cq7hct3XYnhO4GbCquobDzmQzEaDxWi%2Fy2SaSOGIsNNNm0cln%2BsSY%2BlvoVpa8%2FxMV8S7xc95HaB8NZpTDUbrxUDwj9yUEf5mnCbpFnvbf7PPmzkvJH8o0b7EZQrmIjkKDYFajBpgLK8p%2FMLzk%2BdEGOqUBuuZu8OKBMX6gW%2BHzGosNUhbC%2FqgjWEAquMvyiru6eesStFh4yKR9PYRm6wvBX%2Fm0dl2OX%2BzQMgioRGbalcASKRcE%2FxUkPLtTtG2ZWluKMf9QsuUDE6ix%2BGzmhYdwAwz77fJQV8pwDDUrVasTPfqRfc95yUDWgXB8%2BkpHRiNPx9OGNhB5UmqnKQyEPTtXxCzMNRcWfQcR%2Brd738MGUud7gCPcPQfV&X-Amz-Signature=43e05ba7455ec594afad65ffab18dbde3eb42318cd80bdae255be600e7728e89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP4SX54Q%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T135752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdY8fKDcrVs0euTF7d1fbwDSj00npNceY4zVV26U58qgIgaFkr%2B%2FQb%2Bo7KhXoPavzyKcm%2Fp93jcaKa4RghRc4z0HQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDNow59ZWQJ83yzcQGyrcA0YwWAaQGjF05rXYWF62WzYc5vQA3Fc7nVg%2BrwRiEFk13jm47WWHZtni1B5oeDvfDnbXrfdGAYqxMP1sNbaG6CDzKAdkL3d358%2F2dMxlXrG4EXGB2l9Swv73GXejUKFusqq32SxPCcEeIIY86sKAv8MZWBEpqSovu6nXP599%2FKjZYBJh5JpfG3NHBK9fagUiDl7i%2FuRZ8fWmtn%2B838ufQHYML%2FoOt8shqiqS%2BWMwxaUizt30FNKpeRgrWnvJNqQTot%2FdSC6TJUZh8DVei8zLFgDLzdgD82A%2FcGTvFcm4Kga5AZbRnYLVbbPb3nEtUVi3nigONMGi%2BWiCQTQ7WEq8Y7b2OFvKWFnjlKL%2BmFfXBplG5TLKd0drR55IvP0KA1q968PIVxPPifrKrghB3TTCIC4sOYjLmJFQOwFhW9xrwYzJgmEaXTR7oikBQLvKLJ708vT1hQ1ce1gHkhVJ%2BHqKkcafc0yHNXIKTm1lBbKNYgFAeh7cq7hct3XYnhO4GbCquobDzmQzEaDxWi%2Fy2SaSOGIsNNNm0cln%2BsSY%2BlvoVpa8%2FxMV8S7xc95HaB8NZpTDUbrxUDwj9yUEf5mnCbpFnvbf7PPmzkvJH8o0b7EZQrmIjkKDYFajBpgLK8p%2FMLzk%2BdEGOqUBuuZu8OKBMX6gW%2BHzGosNUhbC%2FqgjWEAquMvyiru6eesStFh4yKR9PYRm6wvBX%2Fm0dl2OX%2BzQMgioRGbalcASKRcE%2FxUkPLtTtG2ZWluKMf9QsuUDE6ix%2BGzmhYdwAwz77fJQV8pwDDUrVasTPfqRfc95yUDWgXB8%2BkpHRiNPx9OGNhB5UmqnKQyEPTtXxCzMNRcWfQcR%2Brd738MGUud7gCPcPQfV&X-Amz-Signature=f6d6524c2801fa0810adf5aa64f7aee7f70fc08b8d550823c5cdcdb88d7d5c24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
