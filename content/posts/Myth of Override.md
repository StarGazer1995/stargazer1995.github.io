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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWKKYVR%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T131424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQCmQ%2FC2i72Bv4NeAUl%2BYPwYLCv1Gy%2BKSjJDk0UiDGB5pgIhAK6XSdOS28Fpe86%2FSEmR79getifbjG3ISSM9tzRqB5FKKv8DCAMQABoMNjM3NDIzMTgzODA1IgwPraKM%2Bz3MjT4HL4Eq3APpVavz9NZlR5GTHuVws9lgc5vr6MdEhweASfYHCyRO29%2BZ%2BULYbrfEb6Vsgl%2Bht8ZR5bt6BMctXFnWha1HEpHrE6ZoqXmNjfKHDU5RdQO4m3Hg1Apx7zS5CTe0PfVHOFY3l0CknqBLmbVdQKvEhcc5bPpsgoaDnGm3g9FHSMtZm4bFTLS38m33HJRKutM2x3749In953sBohTTrwpba81dvfS%2F82d%2FDE6XIObyGP7Cdy9rJGOCoyqcAzemQ6I%2B60kLnfYBqapWYRuIcFuekY%2F41eROhNA%2FGz1emMZXi1%2FTm4PyHoGKZWwt%2FH8RQoWKbpio0CUCGLcx9zpdL8hlKJOHbJDULi42n0okvLMcnDOJQHt47Dc17TkVD9TY0a86kcvBA62bEt5XmFafjMjMwHt0KkaWbx%2Bs4kZR9m6BJ8TmIRHO3R8UNHj%2Bal1ViylWGjCKGug44laVao1AafcSKqL6WFXXWOg1T%2BqAoiKLl4ss6m%2BMOBoVjtNuod0NT2WtDYUo%2Ffq7giSLl%2FoENuoeeZ6eY%2B5arAZoSJaTmsFxiGbYl%2BbfmVX6n%2BaOjfSdaJPmMy6si%2Fesk%2BrG054XUseCraw7Cf8iPD0ghAnFcW6%2FI1OQ%2BkLrWv18WokqFYmjHTCU44zTBjqkAcPV9Id4DdPcwqSrRj4BVO8TeC1vcuo65S9HY5bC7LgJ1Q8o%2FHuLIiPKk9JR4A7TQ6jTtjbrXqlB8MRuEPMgahges5EA8yWBjyR01OeK%2F6dhk%2Fz5BB%2FfWhoUc0PpzH01urhqquJfyY3fEDhFLHrrsBnzTZ%2FsIZOPkSYZ540%2BhecLpdkA0%2BIPTUfrdY%2BojVZiew0GKAal3HwnY1jQWtFk82Qfi6nX&X-Amz-Signature=1bedc8fb0f5d456a3a7c9a466b526cba1bd5f9327937c4ea1ee133794a4b4089&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HWKKYVR%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T131424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQCmQ%2FC2i72Bv4NeAUl%2BYPwYLCv1Gy%2BKSjJDk0UiDGB5pgIhAK6XSdOS28Fpe86%2FSEmR79getifbjG3ISSM9tzRqB5FKKv8DCAMQABoMNjM3NDIzMTgzODA1IgwPraKM%2Bz3MjT4HL4Eq3APpVavz9NZlR5GTHuVws9lgc5vr6MdEhweASfYHCyRO29%2BZ%2BULYbrfEb6Vsgl%2Bht8ZR5bt6BMctXFnWha1HEpHrE6ZoqXmNjfKHDU5RdQO4m3Hg1Apx7zS5CTe0PfVHOFY3l0CknqBLmbVdQKvEhcc5bPpsgoaDnGm3g9FHSMtZm4bFTLS38m33HJRKutM2x3749In953sBohTTrwpba81dvfS%2F82d%2FDE6XIObyGP7Cdy9rJGOCoyqcAzemQ6I%2B60kLnfYBqapWYRuIcFuekY%2F41eROhNA%2FGz1emMZXi1%2FTm4PyHoGKZWwt%2FH8RQoWKbpio0CUCGLcx9zpdL8hlKJOHbJDULi42n0okvLMcnDOJQHt47Dc17TkVD9TY0a86kcvBA62bEt5XmFafjMjMwHt0KkaWbx%2Bs4kZR9m6BJ8TmIRHO3R8UNHj%2Bal1ViylWGjCKGug44laVao1AafcSKqL6WFXXWOg1T%2BqAoiKLl4ss6m%2BMOBoVjtNuod0NT2WtDYUo%2Ffq7giSLl%2FoENuoeeZ6eY%2B5arAZoSJaTmsFxiGbYl%2BbfmVX6n%2BaOjfSdaJPmMy6si%2Fesk%2BrG054XUseCraw7Cf8iPD0ghAnFcW6%2FI1OQ%2BkLrWv18WokqFYmjHTCU44zTBjqkAcPV9Id4DdPcwqSrRj4BVO8TeC1vcuo65S9HY5bC7LgJ1Q8o%2FHuLIiPKk9JR4A7TQ6jTtjbrXqlB8MRuEPMgahges5EA8yWBjyR01OeK%2F6dhk%2Fz5BB%2FfWhoUc0PpzH01urhqquJfyY3fEDhFLHrrsBnzTZ%2FsIZOPkSYZ540%2BhecLpdkA0%2BIPTUfrdY%2BojVZiew0GKAal3HwnY1jQWtFk82Qfi6nX&X-Amz-Signature=e99b4c445ced0c631111c0e95fe43d1551a1d7f0939c5fbfa2002592eca6eafc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
