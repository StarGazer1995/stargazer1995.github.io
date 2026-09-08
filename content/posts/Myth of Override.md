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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ6ROR6P%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T122139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9rS8p6hE2LEhjJBFP0Jzz%2FniBGqFh1V6yhYZnq5p%2BZAIgcjHiWEYqyxTqjRvl8WiCqalqvNuvhkGgI60NizdIZkUq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDLyOVtoaiOdruAOsSircA8WAvw1SAoYUebs%2FY6jI1CTCHPti8kbkSGnhtNGvxC7t7tiPmwg7jYs6gG4mOrgv94at8os8rPj0oiHCPmcjtk5hIpx9%2B88nbE3fgeBK9XD%2Bw%2FKI0KDLbI8mxrNoGdvOFtBnLnlCu0ZNZnTbDfr46QWnF%2Bp52sDrxJqnGE47t6eSSyqqOcbAb7tPX6DD%2F8NNb2x97KjijHXo7TMiS7WW%2BFMt12X6GLBHryjUqeEurj03kkgw0rHXVcxhivIdkizeES%2B8uOuXmFEI7c423m%2Fn%2BM%2BW8tup9niyH03JiZ6YdxCHMg6zp%2B0l7Qh8dndIqBjAQcdFNE2ICKVHsZ6kNYU7Fnhu0dZXqIQVPRDCCDwR3621timD3ZGpXW3LK%2B5cpHt3R%2FfqQejhm4lVvRh0WVKjrW6agPqf%2Fa9MD4nLsBobVi8gLzpPhkifO6nhbRfYt2%2FQkAnuj%2BC1hxJOW8pV3A4vGEgO0GpMxSI8NX7Wp%2Bn0gA9v5z9Ct1u5LTGnLw6ReIbZliUqd7BC4e1lG7c4bhAkg469SI3TkR7R7pN%2BOz69XxKtDNzTa4NyqOzDXENrBEmrXgAXRFmVq54GvQdLTC3j%2BsJJN%2FfadwUsZ5xZzNWpCkGb6AJI%2FZe5wQM7zFMxMNyJ%2F9QGOqUBfgipXKuK8rw6Xjz4CtyuDs2mvRr3cSG3LRRjuWEkuepfdzNAVrw%2BJDWrNzuexU0OqNqfJmw3FZ9e%2FkzER3cgMLuyHt2RqDTJ3BNoqTdb5dCeawSFKYOVyS10gei7oXKZH1vB7o9PNmgOgqwZLcqiezur1Sq2WLuaMIX6%2B2Dc4eXz8k1gDxdN4tQ4zzbUnZ0jVmCmOeCb8rumLfyqTs%2FS8ONqVsDg&X-Amz-Signature=ead5024554414299f4543ba838cca616d6467e3235482c98c2bae7249dbe2c50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ6ROR6P%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T122139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9rS8p6hE2LEhjJBFP0Jzz%2FniBGqFh1V6yhYZnq5p%2BZAIgcjHiWEYqyxTqjRvl8WiCqalqvNuvhkGgI60NizdIZkUq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDLyOVtoaiOdruAOsSircA8WAvw1SAoYUebs%2FY6jI1CTCHPti8kbkSGnhtNGvxC7t7tiPmwg7jYs6gG4mOrgv94at8os8rPj0oiHCPmcjtk5hIpx9%2B88nbE3fgeBK9XD%2Bw%2FKI0KDLbI8mxrNoGdvOFtBnLnlCu0ZNZnTbDfr46QWnF%2Bp52sDrxJqnGE47t6eSSyqqOcbAb7tPX6DD%2F8NNb2x97KjijHXo7TMiS7WW%2BFMt12X6GLBHryjUqeEurj03kkgw0rHXVcxhivIdkizeES%2B8uOuXmFEI7c423m%2Fn%2BM%2BW8tup9niyH03JiZ6YdxCHMg6zp%2B0l7Qh8dndIqBjAQcdFNE2ICKVHsZ6kNYU7Fnhu0dZXqIQVPRDCCDwR3621timD3ZGpXW3LK%2B5cpHt3R%2FfqQejhm4lVvRh0WVKjrW6agPqf%2Fa9MD4nLsBobVi8gLzpPhkifO6nhbRfYt2%2FQkAnuj%2BC1hxJOW8pV3A4vGEgO0GpMxSI8NX7Wp%2Bn0gA9v5z9Ct1u5LTGnLw6ReIbZliUqd7BC4e1lG7c4bhAkg469SI3TkR7R7pN%2BOz69XxKtDNzTa4NyqOzDXENrBEmrXgAXRFmVq54GvQdLTC3j%2BsJJN%2FfadwUsZ5xZzNWpCkGb6AJI%2FZe5wQM7zFMxMNyJ%2F9QGOqUBfgipXKuK8rw6Xjz4CtyuDs2mvRr3cSG3LRRjuWEkuepfdzNAVrw%2BJDWrNzuexU0OqNqfJmw3FZ9e%2FkzER3cgMLuyHt2RqDTJ3BNoqTdb5dCeawSFKYOVyS10gei7oXKZH1vB7o9PNmgOgqwZLcqiezur1Sq2WLuaMIX6%2B2Dc4eXz8k1gDxdN4tQ4zzbUnZ0jVmCmOeCb8rumLfyqTs%2FS8ONqVsDg&X-Amz-Signature=55d69df5c3ec75ac70a4fc9ae2480bf671d4bb0c1ecb4bda88afe88e43b31091&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
