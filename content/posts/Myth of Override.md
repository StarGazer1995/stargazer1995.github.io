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

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">github.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WABYC5UF%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T115521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIFuPso9cMn4neUcYD9n32yjAxzPFwFpmHZ4uMUBuDft4AiEA7UnWRmBBYIIXqHQcITVNZHV6GxoaCEkUM7aPnNJPH38q%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDO8Ne7I3QqUbVNAwsCrcA9gkrxD1qK02RrqeYRMBqJova7nvgQUQXHpncdHxKgLhGEhIH4Dxc2bbGb0pWWj5bHjaQ5CFA7Lqk9Eg9KslBGAI5VGe60Y2NkdBkWli0r17eeSHnXP9NdOd5Rk9S9EuMiuXVEfbbJOR7CyAbWAPaIi3TlPFY8rIHlKEc3Kro890iAOVMf4T6csN57VDsDVL1cb91gXv3QxO8RoTEPXuHjzLXz9bHAl5TMdhiq%2BL1mfvLHg4Br2hfJ%2B3Cq9D5WWtRcEOHWEW5uJQTula6PNiabN%2B0B2vzZ3njCTqRB%2FdpKEROI1n9P4sn4IvBaazkvO8XdMGpM5cChNEKwdRjAO1o0%2FtwGh9FDeJ5U4SUmZ7sFoM7zVhUfCzVsk3uDvqpko2lwY1djJfktDitiN5CB3MtubKuzeEwk5OQ5WgoJrzCQITLqr4FKcJnCRiiKqkZUgk9%2F3Suylth0rh4FFX00A0Bum1ZW9oP7yY5z%2FCCyr%2FSteMdMPhm4y7k9Vm27b8w2dAAAZU5Q9AAVVYvo6e2mn5faXJPoR871%2FhUFarwMS6kS4OG76Yjdk7feK1QEvLGpkoEfhyErmo8mYpuifvi5EZzWWGudMUohrXkUIP40TKoP5NWVD5Yn1y%2BGSjWoZVMM7LkdAGOqUB0BcYs1C9Cv9jPnkStu%2FDHOBFmMEKXq4yUEvm0m6HsOSvNNtzvnbtkBlbNC%2BQUe7pULuN893NDI56eqK2aPe4%2FweniFU4Em%2FH4Rz%2FA%2FM8v65bZJHd5grrz7pCejQ6tbly6hu%2BYbmR3ZgkbjaGNVUbGbZfyhC1IPSxDR2zXzbg9mmME3DVc5Jf5y2jReAOiHBmK4ZsbXh17WkIDpNY2CDpuw4kpLSv&X-Amz-Signature=aa21ea850facd510f2327c7931bf2c647d055928fb2c58e9a6be780d630c9b4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WABYC5UF%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T115521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIFuPso9cMn4neUcYD9n32yjAxzPFwFpmHZ4uMUBuDft4AiEA7UnWRmBBYIIXqHQcITVNZHV6GxoaCEkUM7aPnNJPH38q%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDO8Ne7I3QqUbVNAwsCrcA9gkrxD1qK02RrqeYRMBqJova7nvgQUQXHpncdHxKgLhGEhIH4Dxc2bbGb0pWWj5bHjaQ5CFA7Lqk9Eg9KslBGAI5VGe60Y2NkdBkWli0r17eeSHnXP9NdOd5Rk9S9EuMiuXVEfbbJOR7CyAbWAPaIi3TlPFY8rIHlKEc3Kro890iAOVMf4T6csN57VDsDVL1cb91gXv3QxO8RoTEPXuHjzLXz9bHAl5TMdhiq%2BL1mfvLHg4Br2hfJ%2B3Cq9D5WWtRcEOHWEW5uJQTula6PNiabN%2B0B2vzZ3njCTqRB%2FdpKEROI1n9P4sn4IvBaazkvO8XdMGpM5cChNEKwdRjAO1o0%2FtwGh9FDeJ5U4SUmZ7sFoM7zVhUfCzVsk3uDvqpko2lwY1djJfktDitiN5CB3MtubKuzeEwk5OQ5WgoJrzCQITLqr4FKcJnCRiiKqkZUgk9%2F3Suylth0rh4FFX00A0Bum1ZW9oP7yY5z%2FCCyr%2FSteMdMPhm4y7k9Vm27b8w2dAAAZU5Q9AAVVYvo6e2mn5faXJPoR871%2FhUFarwMS6kS4OG76Yjdk7feK1QEvLGpkoEfhyErmo8mYpuifvi5EZzWWGudMUohrXkUIP40TKoP5NWVD5Yn1y%2BGSjWoZVMM7LkdAGOqUB0BcYs1C9Cv9jPnkStu%2FDHOBFmMEKXq4yUEvm0m6HsOSvNNtzvnbtkBlbNC%2BQUe7pULuN893NDI56eqK2aPe4%2FweniFU4Em%2FH4Rz%2FA%2FM8v65bZJHd5grrz7pCejQ6tbly6hu%2BYbmR3ZgkbjaGNVUbGbZfyhC1IPSxDR2zXzbg9mmME3DVc5Jf5y2jReAOiHBmK4ZsbXh17WkIDpNY2CDpuw4kpLSv&X-Amz-Signature=fddcc3edb6de203cce0e52572d223bc08d60954b87fd4d8140decd72a067fb6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
