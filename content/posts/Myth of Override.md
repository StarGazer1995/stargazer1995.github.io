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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7G2NJ4W%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T064545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICsUBexqFoUgqKoXLdMjkBqKKcM7%2BrdmxlS30ii76c%2BzAiASvqSh85SBZDBFnlMPk1Lgy3B3gqUTWPYQERQHEuAvAiqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3vXOPjAm0lA63HaQKtwD6XgvpDgRArH%2BeDS9F%2BqfXEC3FX9%2FnU5dVUYZk4DuoaBelxy%2FXFtYd%2BPtiFmCn1u9MLSjou0WSMGIeHDySz1d5AjDof%2BA5NPmuW3WTdl3326or41sHp1Mavgah4pQeiHnFdwfSiJ55%2BjrBbje8x7znY3zzGE54BgoTuwIIAHhmJCGV4mOhVQ6Bq6ELw7aWmzRqdEtjWBGEFeHIg4kodx7kL1RcRJ04hF%2BXzvDUcYb%2B3yOiviHg7j6gXoZ2qnK4at%2F9a97w4qM%2BDJ0pT73OTa7oOH7LhVctCDp3EThPMREMcbuSIrJL0Jt1qIr%2BCGF65gBiMKzoVNzssVr5NVwwGQfd8TOHL1laa%2BohwizFQbPtqeYmR3aWMGjO4YyecSH5ih6uobdP5QB7P3wK7Hx8GBXzapMdWn2VESxf%2BUi72RsfgiHdvfLdnmhQnASAi2GaAtM%2Fb7r4XZQ7cbfkYyaYfgRZ5%2FFFNuO0i45tAxOM39kc30EXiHzc8%2BDbaCHCyoZCzxh2kfzYtIUX1MLbfd3VGol5t2eXY0PxKdDfQPoR8L0okLxqsmvDVN%2BQhiPGQUBtuPP6gwJoOkYtwcu4km%2F2o655ugFwUd5NhbI4xuFve%2F62loxVZmEaoyR1e2khDow85iO1QY6pgGnCLuDyF%2FaElJUM2adiZgZ5apxEDX0w%2ByhZGX8UZ6qy4VYxNiCzarLBMpY%2BWEO4gJzRfSjZbEgFCoDA3Sn7RpsnTJCjUoDIDV4vw0CrAWUr8xrmv0XK7fTszzUhwXPa7a2ywqm9YPZC5D4vnquoWzErrcNDCtl4CzWfnZSjpocwriFzfvZJ8hw%2F48vXkRZjmNpwVtzFTUft5HzbrJVKgZmhD9%2F6hek&X-Amz-Signature=226978bb535d2f6a321369c8a7c6f61b57c54c3147b345145549a5eb1d15b5ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7G2NJ4W%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T064545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICsUBexqFoUgqKoXLdMjkBqKKcM7%2BrdmxlS30ii76c%2BzAiASvqSh85SBZDBFnlMPk1Lgy3B3gqUTWPYQERQHEuAvAiqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3vXOPjAm0lA63HaQKtwD6XgvpDgRArH%2BeDS9F%2BqfXEC3FX9%2FnU5dVUYZk4DuoaBelxy%2FXFtYd%2BPtiFmCn1u9MLSjou0WSMGIeHDySz1d5AjDof%2BA5NPmuW3WTdl3326or41sHp1Mavgah4pQeiHnFdwfSiJ55%2BjrBbje8x7znY3zzGE54BgoTuwIIAHhmJCGV4mOhVQ6Bq6ELw7aWmzRqdEtjWBGEFeHIg4kodx7kL1RcRJ04hF%2BXzvDUcYb%2B3yOiviHg7j6gXoZ2qnK4at%2F9a97w4qM%2BDJ0pT73OTa7oOH7LhVctCDp3EThPMREMcbuSIrJL0Jt1qIr%2BCGF65gBiMKzoVNzssVr5NVwwGQfd8TOHL1laa%2BohwizFQbPtqeYmR3aWMGjO4YyecSH5ih6uobdP5QB7P3wK7Hx8GBXzapMdWn2VESxf%2BUi72RsfgiHdvfLdnmhQnASAi2GaAtM%2Fb7r4XZQ7cbfkYyaYfgRZ5%2FFFNuO0i45tAxOM39kc30EXiHzc8%2BDbaCHCyoZCzxh2kfzYtIUX1MLbfd3VGol5t2eXY0PxKdDfQPoR8L0okLxqsmvDVN%2BQhiPGQUBtuPP6gwJoOkYtwcu4km%2F2o655ugFwUd5NhbI4xuFve%2F62loxVZmEaoyR1e2khDow85iO1QY6pgGnCLuDyF%2FaElJUM2adiZgZ5apxEDX0w%2ByhZGX8UZ6qy4VYxNiCzarLBMpY%2BWEO4gJzRfSjZbEgFCoDA3Sn7RpsnTJCjUoDIDV4vw0CrAWUr8xrmv0XK7fTszzUhwXPa7a2ywqm9YPZC5D4vnquoWzErrcNDCtl4CzWfnZSjpocwriFzfvZJ8hw%2F48vXkRZjmNpwVtzFTUft5HzbrJVKgZmhD9%2F6hek&X-Amz-Signature=6290428a39deda298b7be8548b6dfd8cd4cdcac3f75d59b3826086e3fcb18699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
