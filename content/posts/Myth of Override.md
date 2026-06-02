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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHHVWIZJ%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T134741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGSaBj2gcb4AUENDG%2Ba3vobhr53oL3B8GVlxqKWJCexoAiEA2D1%2FDCAC3cbILoeQlXndrZYaZtaa3XCEM%2FnMr%2FwEcH0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFEjhsio30ntxFZvIircA1Wo%2BvkWmBmO%2FCnJv3nHStHBbvVutht8cl%2BY%2BBi%2Ba%2FshdIBhrOzcX2CgLJKR6yJvBxnLW%2BMeBVk5bHmcvNWoCHCuDyvEhi8gOMz1Vx8KbivXDQNzkQ9UB4GIQ%2BuCClr7Q1zOGqOenrQ72QEC0rW3iYu24arRgO1bDEqqv3Si9diWg%2BaixOo7ME7urIg3wbFU7u4zHofjQL0inbwVMKMV%2BDSupmWywaN3aI4gMiBbxyLvDTRD1guPcUSWr8dx6Exx127XmpoIShJ8DZlUrNi39842ZQTj2C0Zdkkq71hoCpvpidmWTTA%2F%2BSHUx2VPw4U6dzUwEiLu8fBK63KohIr0IEjqh%2BeCkTsV9iF1M0P9Va5HgixJokuTvj60qtDoo8IajAErdVTaW6sHpHS%2Bm0ynjEllHFdq0Ur7Yydtx%2FUNVcPibx9j%2FGA%2BFzq1Te%2FlTXBcG2xygiBQoR67zJAkTwwg3CMvQPrtVZaQLuq7zHNI6o8CrZTJsuEOeQczwJIgmNjXSk8ujXkehA914bbctArqtzSTzmtZTODFszbU01a88doSay6IvWmKMWD4SZ%2FIAptzcBR6mBJfuQYS1CFQZ9aDawlHm1PSHgTtFoktVXS1ishuKmExbtaBRZ7mSKFHMIKr%2B9AGOqUBEpZcflpLnECBeUC%2F0cTzb3JgA%2Bd6KqSE7cgURSp%2F41I%2FrQ9nBzxGK%2BrkrlOesrqG9huf81IurkG12CWJkAw212DlN%2Bev835ZrX%2FMtdOi%2FGxKmmRQqJM%2Fl5wqqft5xF%2F8gijhWx7BcBskrFsYj3MiJ%2FHlnGiGc%2FvYFrea%2FP6OhFc6W6N6thVRQo7fCEgLiK1GErCVaxTYwOuy3y4UKcUMYBjHGOM2&X-Amz-Signature=3000f834a09db8bef6d2fc3134763feddcc62f5005e846bfca560ce0a61ee4cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHHVWIZJ%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T134741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIGSaBj2gcb4AUENDG%2Ba3vobhr53oL3B8GVlxqKWJCexoAiEA2D1%2FDCAC3cbILoeQlXndrZYaZtaa3XCEM%2FnMr%2FwEcH0q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDFEjhsio30ntxFZvIircA1Wo%2BvkWmBmO%2FCnJv3nHStHBbvVutht8cl%2BY%2BBi%2Ba%2FshdIBhrOzcX2CgLJKR6yJvBxnLW%2BMeBVk5bHmcvNWoCHCuDyvEhi8gOMz1Vx8KbivXDQNzkQ9UB4GIQ%2BuCClr7Q1zOGqOenrQ72QEC0rW3iYu24arRgO1bDEqqv3Si9diWg%2BaixOo7ME7urIg3wbFU7u4zHofjQL0inbwVMKMV%2BDSupmWywaN3aI4gMiBbxyLvDTRD1guPcUSWr8dx6Exx127XmpoIShJ8DZlUrNi39842ZQTj2C0Zdkkq71hoCpvpidmWTTA%2F%2BSHUx2VPw4U6dzUwEiLu8fBK63KohIr0IEjqh%2BeCkTsV9iF1M0P9Va5HgixJokuTvj60qtDoo8IajAErdVTaW6sHpHS%2Bm0ynjEllHFdq0Ur7Yydtx%2FUNVcPibx9j%2FGA%2BFzq1Te%2FlTXBcG2xygiBQoR67zJAkTwwg3CMvQPrtVZaQLuq7zHNI6o8CrZTJsuEOeQczwJIgmNjXSk8ujXkehA914bbctArqtzSTzmtZTODFszbU01a88doSay6IvWmKMWD4SZ%2FIAptzcBR6mBJfuQYS1CFQZ9aDawlHm1PSHgTtFoktVXS1ishuKmExbtaBRZ7mSKFHMIKr%2B9AGOqUBEpZcflpLnECBeUC%2F0cTzb3JgA%2Bd6KqSE7cgURSp%2F41I%2FrQ9nBzxGK%2BrkrlOesrqG9huf81IurkG12CWJkAw212DlN%2Bev835ZrX%2FMtdOi%2FGxKmmRQqJM%2Fl5wqqft5xF%2F8gijhWx7BcBskrFsYj3MiJ%2FHlnGiGc%2FvYFrea%2FP6OhFc6W6N6thVRQo7fCEgLiK1GErCVaxTYwOuy3y4UKcUMYBjHGOM2&X-Amz-Signature=925f0c977fd6e578f27aaa5684fa418f59abfa71cb0c3578a91794a9a70651ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
