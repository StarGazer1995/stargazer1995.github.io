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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ3OTUAV%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T192950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIE8Vr%2F6CgeK1M9h6X0OjvBWwasLfnaJhgczmBXs8S4WmAiEAnvdAI3dMpOB6n%2Fvlj0WAnR%2B5tWJRfpcPbyux3KiCjRMqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDLGp6DYD9X5x95HlCrcAyB9SP%2Fqm1Q94Vy09NG1WqfzL2nn0k24%2B6Gid0mZzFJODrBusf%2FyiZxC%2FuqheN%2BcBDSWQaHcLNY9lrLl5k4aQN3c5ExdR5Y13nkbLoo5Bzk4Tx0%2FgXol%2FKPEjCjOLbC6TwD0ZO9AqIEk%2FeCvz11LpxV%2BbsDRh1XVowFEp3Do%2FjMBKUhLmI2%2BqNuQSct69gtYaykWQpzYpC3XRKDgbvLnh%2FeXeO7wFXMJscrvFR2ySnFkCL4V%2BOM5yC0iy0unT2ZQ5L4jJywSLE0sG7qlPVNCRLiouYhJEjtu%2FaU14fbBL4ougmi4plqfmhE8rX4IqgItuzADFCFFE7lNS%2BH%2BRwN4BtaPYvEM4qb10XJc5dlW2a8ZvUFC3y5IGRAdF8kj0iXiBd43NQ4ksG%2Biu1xb3sYKRyi125rcc7R9Bzg9UnBGJAb65z2EQcwTT3QnGLsonh2Pa0qDzgHzzF%2FF2hxTtFSixLBHs2SneygiJM4%2F6GFoiObBAYfskqva1ozmxmagCpRovWK%2FyCoPfXTlkDGPE%2FBt%2FLAA55Gc1QjJBkq%2FeY%2BUtL6CWN43Fkvf6GbieP3Gc78V%2FhTy9c%2B7ZtHehpRYRj9vdB08ozYh4Qfsg6Dtj2VpWfWKXG2kWeOlzVjtYsIxMNvcj9IGOqUBW2fPnR8SnQ3DLdLV6S54FCsSQuoBcM6CPhxa%2Futj7rsrO4YgQ9WVwNcOWqf0hektXIou%2BBJ6k35dcKeBzMdUYxh4aos0oFBNhDRhvOT7XizSn3plDmrXa%2F%2B04Q4pWl0RgJ%2B3WitZQmvpScXU7pQGZD%2FfOLvUH4%2BympHRltpQOH9SQfxCiGHZwJv9TNjHsIQczXKaKxMO0JVMaemfryOhakjUAPQV&X-Amz-Signature=aee31d0af138c9f07dbd1874d5752e3b2cf0cbd595711925ce91c1a726b65aed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ3OTUAV%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T192950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIE8Vr%2F6CgeK1M9h6X0OjvBWwasLfnaJhgczmBXs8S4WmAiEAnvdAI3dMpOB6n%2Fvlj0WAnR%2B5tWJRfpcPbyux3KiCjRMqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDLGp6DYD9X5x95HlCrcAyB9SP%2Fqm1Q94Vy09NG1WqfzL2nn0k24%2B6Gid0mZzFJODrBusf%2FyiZxC%2FuqheN%2BcBDSWQaHcLNY9lrLl5k4aQN3c5ExdR5Y13nkbLoo5Bzk4Tx0%2FgXol%2FKPEjCjOLbC6TwD0ZO9AqIEk%2FeCvz11LpxV%2BbsDRh1XVowFEp3Do%2FjMBKUhLmI2%2BqNuQSct69gtYaykWQpzYpC3XRKDgbvLnh%2FeXeO7wFXMJscrvFR2ySnFkCL4V%2BOM5yC0iy0unT2ZQ5L4jJywSLE0sG7qlPVNCRLiouYhJEjtu%2FaU14fbBL4ougmi4plqfmhE8rX4IqgItuzADFCFFE7lNS%2BH%2BRwN4BtaPYvEM4qb10XJc5dlW2a8ZvUFC3y5IGRAdF8kj0iXiBd43NQ4ksG%2Biu1xb3sYKRyi125rcc7R9Bzg9UnBGJAb65z2EQcwTT3QnGLsonh2Pa0qDzgHzzF%2FF2hxTtFSixLBHs2SneygiJM4%2F6GFoiObBAYfskqva1ozmxmagCpRovWK%2FyCoPfXTlkDGPE%2FBt%2FLAA55Gc1QjJBkq%2FeY%2BUtL6CWN43Fkvf6GbieP3Gc78V%2FhTy9c%2B7ZtHehpRYRj9vdB08ozYh4Qfsg6Dtj2VpWfWKXG2kWeOlzVjtYsIxMNvcj9IGOqUBW2fPnR8SnQ3DLdLV6S54FCsSQuoBcM6CPhxa%2Futj7rsrO4YgQ9WVwNcOWqf0hektXIou%2BBJ6k35dcKeBzMdUYxh4aos0oFBNhDRhvOT7XizSn3plDmrXa%2F%2B04Q4pWl0RgJ%2B3WitZQmvpScXU7pQGZD%2FfOLvUH4%2BympHRltpQOH9SQfxCiGHZwJv9TNjHsIQczXKaKxMO0JVMaemfryOhakjUAPQV&X-Amz-Signature=8a03c653f0f364526c71a035952804c7525497e61ea4838748986a7770f7b236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
