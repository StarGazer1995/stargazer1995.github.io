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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HOC3RMJ%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T045355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIGwTpOBCGgNZNEsZyeEmDBVIYaibgKf5b6jQhhtW52iOAiEA08Yo0MxGC6BElBDsanYxRwwfSsYpm64gNXvI5zHnsV0q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDP6BClme06Uauf44IircAxMAe%2F%2FTvf9opbFu%2FVLd6Q%2B1eb63USK7LmFKslAMAooS5cPhHA7Hm3WhZLvJrW1L%2F%2Fc8pl%2FH9l3YIlhK0IVKFT296wVdIrj51zp2AALtgkjsoSqzhzZKw519VHv1R7z%2FMtweS%2F%2FHHKmF7S0RyUA%2B7KFJlW%2BSRfNM7JOJUN0LwBQ55Oo91XPZ8NVqEHYKgF8uPpXY7q52hqcOPwt8UeNiDCczYC%2BKzp3kh7pFggMd8ORTBG4eQERSarzRqincgX4ACdtOZxez3eJgDyf6cTBNMKMdT9ehZwhlq5lCOnkrnil8HDkJ7yPZSqNyOV2wopp0Aaxi4GLe2bwpHJmkzxi9OS%2BAS97DunK4KyBoUjZScbu47j9U4NVcDf6QPL8inwziluTUTiWU6DGT9jjPEr2GlKm29S06PoqMD%2BnhplE6NMAGcOXPRKvnSCb%2B3pa2ra1k2t2%2B7XhNZgCbEqUwHEVVSJJXCXlyeJlDA6kcr3r1pqwiCcpX5jhL5%2BkveBywh%2BetRAYNV42iMvMh5Af0RRSaMBwmJpFSAU8H%2FLXKyOwdOZ74oX%2FZKv6KDD00s1OhSl0qneHkHqySCCIg4U8stUGD917aPRml4Ra8sjB6Lbf44xGvkvA7J6h2ZF0fCoOBMKqG0NMGOqUB2MINfBmyVSTvr2Qm14vWjJyR5xYKsx3qFb4skHUOk8IzTKbYPouAv24RAziq0C2ApOrffC%2Fppaf7WziKTS%2FBnnrNc4HZz8qC%2F5kn39d4JypXRUfwkJVmJ0MgTW2sIFozZ%2F1QER5JGFIQe5c9zJ2rkv06AtoavO15hwxEudb%2BbNuTGH0x4dkBf3ngGy%2BZK8wuy%2BKxjt%2BSZrrxgvnXUwKfpjgSfSpe&X-Amz-Signature=016ccfff2ebe0c2f7621255bc762fe77659613cef155acb43b02044bd7418ae0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HOC3RMJ%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T045355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIGwTpOBCGgNZNEsZyeEmDBVIYaibgKf5b6jQhhtW52iOAiEA08Yo0MxGC6BElBDsanYxRwwfSsYpm64gNXvI5zHnsV0q%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDP6BClme06Uauf44IircAxMAe%2F%2FTvf9opbFu%2FVLd6Q%2B1eb63USK7LmFKslAMAooS5cPhHA7Hm3WhZLvJrW1L%2F%2Fc8pl%2FH9l3YIlhK0IVKFT296wVdIrj51zp2AALtgkjsoSqzhzZKw519VHv1R7z%2FMtweS%2F%2FHHKmF7S0RyUA%2B7KFJlW%2BSRfNM7JOJUN0LwBQ55Oo91XPZ8NVqEHYKgF8uPpXY7q52hqcOPwt8UeNiDCczYC%2BKzp3kh7pFggMd8ORTBG4eQERSarzRqincgX4ACdtOZxez3eJgDyf6cTBNMKMdT9ehZwhlq5lCOnkrnil8HDkJ7yPZSqNyOV2wopp0Aaxi4GLe2bwpHJmkzxi9OS%2BAS97DunK4KyBoUjZScbu47j9U4NVcDf6QPL8inwziluTUTiWU6DGT9jjPEr2GlKm29S06PoqMD%2BnhplE6NMAGcOXPRKvnSCb%2B3pa2ra1k2t2%2B7XhNZgCbEqUwHEVVSJJXCXlyeJlDA6kcr3r1pqwiCcpX5jhL5%2BkveBywh%2BetRAYNV42iMvMh5Af0RRSaMBwmJpFSAU8H%2FLXKyOwdOZ74oX%2FZKv6KDD00s1OhSl0qneHkHqySCCIg4U8stUGD917aPRml4Ra8sjB6Lbf44xGvkvA7J6h2ZF0fCoOBMKqG0NMGOqUB2MINfBmyVSTvr2Qm14vWjJyR5xYKsx3qFb4skHUOk8IzTKbYPouAv24RAziq0C2ApOrffC%2Fppaf7WziKTS%2FBnnrNc4HZz8qC%2F5kn39d4JypXRUfwkJVmJ0MgTW2sIFozZ%2F1QER5JGFIQe5c9zJ2rkv06AtoavO15hwxEudb%2BbNuTGH0x4dkBf3ngGy%2BZK8wuy%2BKxjt%2BSZrrxgvnXUwKfpjgSfSpe&X-Amz-Signature=0dcf8b7e988e1c4ef833b3e1bdce64e92cfdaa9e0a8b452a4fd197fd03ed1610&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
