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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLALMCXO%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T190739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDnCmeagrFkPvw2uwoHDBwdXEuDnpS9WphCO2t%2FpeYeLgIgC2NVnODPXdUW1IdozEs42ZwJhmdD3ivQJtA9MV8QqGsqiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEck9y8RzqQylsuf0yrcAx9Muob2umCrnW1ubqBLxMdF6tayZKqpSdPgfVNihj0a2Ud9CdiE9LDp00FdBtYQgxSS0A%2BrJyl%2BscA6obaE%2F5iooERAd%2B1%2FPLCjekkwSxZWwUe7zCwSxMztPQzTtMY3Vr%2FPvby6%2B4L7FHriUXxkI6xPQRCmPeFh1rk7U9CZlw%2BQ9uIZY5zzJ7GzzTPdAfqgGwb6EcHjeYcoVwqAFGYvb2PBnWQdv4b5EwbfddDwqFJT5%2BpccmT7NvkYx%2BAx0gD62Gh0PR5ZYwHbh1ORh0s0JEJuJrB6hSRlXSmPJDHEuOtJAOZ672eJZHWY3Ke193tU2QPfYbCeIzT%2BYHRCD84tXSV24WqWNXPCvXkLQjSSWW6j63gTK7vF73lqlK546zyJyV4M7D9uQctyqh77iw4HhS8WXigbeUQnrawJspB%2FuZ9O9ddq2iTRVjf2aKkhfgCFnHCDJurnkTpGllIiVrwANXFSbSE%2BepeL8xfUlcznnOhifYHqKRQB3U9D4JKzJm9M1PMf6G0lOPacu%2FSs5nmaXtoBU8U6eiWmTR8U%2By5ZxTLj18fhIWIkIHMw3VN7Np%2FxU71eZFRfNuYdoi8KFeM10k%2F9nbbpjODJG7IrmoH3dasFhA20JTkVyK24JsXlMMq729EGOqUBf%2B5KlUlfIJFKUvqb96BzE5RvQWYFKZI8CPHzdI7LzE%2BBljLh5755mXeP0J7gxeJg1nmX%2BUbAQ6smfXfgitkid2uLK0x5n19Ct%2FMpIr9E%2BVb7AAUfK2EioRf%2FmCk%2BxmfI6oyh1lVPEYxuvJJ6Frt0IQhGZaphcCT%2BFlc87XUdgQ%2BAZHCNQh8u%2FNevIAQnbaB35dXqq8S38kdtlHNj1HQcJQToUkb%2B&X-Amz-Signature=ef1d09e49546567c94ba7be3f7aac0afcee36f4dbd70ff6361e1f23e938ca815&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLALMCXO%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T190739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDnCmeagrFkPvw2uwoHDBwdXEuDnpS9WphCO2t%2FpeYeLgIgC2NVnODPXdUW1IdozEs42ZwJhmdD3ivQJtA9MV8QqGsqiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEck9y8RzqQylsuf0yrcAx9Muob2umCrnW1ubqBLxMdF6tayZKqpSdPgfVNihj0a2Ud9CdiE9LDp00FdBtYQgxSS0A%2BrJyl%2BscA6obaE%2F5iooERAd%2B1%2FPLCjekkwSxZWwUe7zCwSxMztPQzTtMY3Vr%2FPvby6%2B4L7FHriUXxkI6xPQRCmPeFh1rk7U9CZlw%2BQ9uIZY5zzJ7GzzTPdAfqgGwb6EcHjeYcoVwqAFGYvb2PBnWQdv4b5EwbfddDwqFJT5%2BpccmT7NvkYx%2BAx0gD62Gh0PR5ZYwHbh1ORh0s0JEJuJrB6hSRlXSmPJDHEuOtJAOZ672eJZHWY3Ke193tU2QPfYbCeIzT%2BYHRCD84tXSV24WqWNXPCvXkLQjSSWW6j63gTK7vF73lqlK546zyJyV4M7D9uQctyqh77iw4HhS8WXigbeUQnrawJspB%2FuZ9O9ddq2iTRVjf2aKkhfgCFnHCDJurnkTpGllIiVrwANXFSbSE%2BepeL8xfUlcznnOhifYHqKRQB3U9D4JKzJm9M1PMf6G0lOPacu%2FSs5nmaXtoBU8U6eiWmTR8U%2By5ZxTLj18fhIWIkIHMw3VN7Np%2FxU71eZFRfNuYdoi8KFeM10k%2F9nbbpjODJG7IrmoH3dasFhA20JTkVyK24JsXlMMq729EGOqUBf%2B5KlUlfIJFKUvqb96BzE5RvQWYFKZI8CPHzdI7LzE%2BBljLh5755mXeP0J7gxeJg1nmX%2BUbAQ6smfXfgitkid2uLK0x5n19Ct%2FMpIr9E%2BVb7AAUfK2EioRf%2FmCk%2BxmfI6oyh1lVPEYxuvJJ6Frt0IQhGZaphcCT%2BFlc87XUdgQ%2BAZHCNQh8u%2FNevIAQnbaB35dXqq8S38kdtlHNj1HQcJQToUkb%2B&X-Amz-Signature=f2987745d65a8fe35d6e28f93faca50ec658754bc67a12d763cb4d6862e360d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
