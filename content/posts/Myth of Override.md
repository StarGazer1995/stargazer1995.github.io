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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622L2B77R%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T161107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIHfGdWpSpHxv2CbbKsKtnzLF3b5JMPdzcoBClZG87NXaAiEAt4q6yskBor0jmYA%2FfUco%2BRQfZD1x1tVR23xO64WtRcAq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDKQ6CkTfsuHte%2BGEWircAy1tdZEX%2Bf3WxphZ9mjM0kOxEh00u0xaqU79c8%2FqucXMKv9ZSiWOAO9cN1nmZeGkqzPgP0qDgiqiA6Cs9I47Q0ICX9C4Eet5TXkUy8g7zEWYyjpgvT1aDN02r%2FLWU%2BOjmCmZqxJMtfw%2FN9E0Cy9aOMVSC9gQMRlmC6%2Fqnzwj0U0vRAuBgaJ1H8aAFh%2FGvJdrlAqRyJBs9BLpexK9UtTxcQlm1MHMedLw04NMkF%2FtHj%2FSn5H9RSboQQGHpMj1e52qaAnbzzFTu4MM965qkDOEAJqacwpd7BbqHA9%2FPHyp8ImT5WRUkraLUo87BwOtxV%2B3VlcTte83p3va1pnUZLTqgZHZYVE8tVgOnWVlGonyb0sdp2nxkuNVkVg%2FbsxOXyiCaGuh66RdXG1gabmytFVeFgi7ZZNZ6fv%2Bi6nbpc9iVrG4okbY6F9FOWkTmOLMeyeQSr9XVYorAnub%2FNT56NG7txTJbx%2FOEbgN2x0DoXfVXeas83aQDPnYu4RcK5GCQs3X3meOitPgMtoM7xULFB3aptMpXv7Lx2giErEue7efuC8CpR0445NXBVur1OiTqDrUpmqkBnPU9JZnN6RcP8a98F4uTMCWmHs8KmtNzVzRrKlOGCxWNqTy5MFnfNvqMLOagdQGOqUBdtQKuf37vBih8M8weTNj4UPg0S0yfkXfKjGOCkpmEd35CDv7%2B2W2cxurA9rePHWvlbiYXM4nwKO43rnSOO9gxnE7az1SLdtg0X4a59M%2FRMcVges0ItX8dABEz2YFYwZz7RKY%2FXa2PFC%2B27QgIh32EAJyjB73gRVbUDomeqg8THDBThZdIHHRs9JuWO7Trto2RbgeTsUcOHmxDEgE%2BVjzKWiGgWHw&X-Amz-Signature=1bca2bdf2351236ce4d07001b6e4e6268b8f5ea0e872546bbe833bb7856c59e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622L2B77R%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T161107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIHfGdWpSpHxv2CbbKsKtnzLF3b5JMPdzcoBClZG87NXaAiEAt4q6yskBor0jmYA%2FfUco%2BRQfZD1x1tVR23xO64WtRcAq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDKQ6CkTfsuHte%2BGEWircAy1tdZEX%2Bf3WxphZ9mjM0kOxEh00u0xaqU79c8%2FqucXMKv9ZSiWOAO9cN1nmZeGkqzPgP0qDgiqiA6Cs9I47Q0ICX9C4Eet5TXkUy8g7zEWYyjpgvT1aDN02r%2FLWU%2BOjmCmZqxJMtfw%2FN9E0Cy9aOMVSC9gQMRlmC6%2Fqnzwj0U0vRAuBgaJ1H8aAFh%2FGvJdrlAqRyJBs9BLpexK9UtTxcQlm1MHMedLw04NMkF%2FtHj%2FSn5H9RSboQQGHpMj1e52qaAnbzzFTu4MM965qkDOEAJqacwpd7BbqHA9%2FPHyp8ImT5WRUkraLUo87BwOtxV%2B3VlcTte83p3va1pnUZLTqgZHZYVE8tVgOnWVlGonyb0sdp2nxkuNVkVg%2FbsxOXyiCaGuh66RdXG1gabmytFVeFgi7ZZNZ6fv%2Bi6nbpc9iVrG4okbY6F9FOWkTmOLMeyeQSr9XVYorAnub%2FNT56NG7txTJbx%2FOEbgN2x0DoXfVXeas83aQDPnYu4RcK5GCQs3X3meOitPgMtoM7xULFB3aptMpXv7Lx2giErEue7efuC8CpR0445NXBVur1OiTqDrUpmqkBnPU9JZnN6RcP8a98F4uTMCWmHs8KmtNzVzRrKlOGCxWNqTy5MFnfNvqMLOagdQGOqUBdtQKuf37vBih8M8weTNj4UPg0S0yfkXfKjGOCkpmEd35CDv7%2B2W2cxurA9rePHWvlbiYXM4nwKO43rnSOO9gxnE7az1SLdtg0X4a59M%2FRMcVges0ItX8dABEz2YFYwZz7RKY%2FXa2PFC%2B27QgIh32EAJyjB73gRVbUDomeqg8THDBThZdIHHRs9JuWO7Trto2RbgeTsUcOHmxDEgE%2BVjzKWiGgWHw&X-Amz-Signature=43e62488aee7386d2aa7dd507911166373dda4dbe33343dc8f6ccbb000bbd7be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
