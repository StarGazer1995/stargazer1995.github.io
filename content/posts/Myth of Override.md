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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663EDZB4F%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T075317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDG%2BSHeNx0SCexii46NC00MtBg8qWZ23IFrRHsqxH902AIhAP%2BiZ3T4CwQhidcDd6vCpME%2FfwIhpIsE0Flj8jxuPQfjKv8DCD8QABoMNjM3NDIzMTgzODA1IgyczEis82lTIkICVYMq3APTFdBuCEjYj3xVUlG9s6yIBgbeKWkk7kdwub9xwyVer1QIJXNvY57%2F3wYgbVyBQY0UHtT%2FBfYDLEgYt7F3ftEpA68ydcvUwESWUTcufK82Msfbr3wtzMWLli14dAbyOb0zkvLW4GpNMiF3lErwhjn55bbemSrRFp8rC%2FXFR8mx5U%2B8IbqM7p3ji2Sm1iG070F%2BX7KFr%2B1IvlzgZqcabXhJh8KhRotcKxzksPE7sN0O8BxVLPfOy98fao88murfswX12Z5uIzRGDSgqVbINFtQhgic1r%2FQjvh%2BcqC1oDsGX2TNr0VVVMiaEAgQ%2FzOPeK9vvWu6O%2FGeP1YRyF2w9gj9BgEC%2Buo4%2F59SCIwtDSf4%2BthflgTYKWIQ7PyKV%2Fg1kZdj3FC6m2TeJo%2B6ANiYt%2Ftrwlv41ebsIJR%2FJNMyMm24%2FUVUt7dZxMJCWbx2VPu%2BmX0o%2F9pmIgy%2FYVH3vCS64g9U8y0psIhYnMhEu%2BGdF3XmC7dNuL73t6MFcMIZK9M6TCKz6b0gghaLEZF3pQZuX1sysH03X1%2FB1OvTVm3JkktAaMRixB%2B5SLuwOO392bBfgpdeMIKKhpwZmWjVSlhfP1pvlQ1s20sxZPeqOK%2F2RzUYCngAYcpq8ZqzBOovTpjCN8uHSBjqkAVSJ6MNVou7weoxS%2F9qvHj0F1l4woYxzqMXhmUhyQAbs7%2B4bl6CFTE3gjICP3G0ZosEb0vpEZRKHifnpIuTKl%2BTTyQ6we47pucRRTs6o04PtfNTLKZHGegepW0NrsfSm0Vwa6FV%2FZz2FTL2YJoB6GCcv7%2B9r641%2BX1KPTFCrIEgF9%2B5fVOhaiGfLB3ZkSRvsiqnTGQ6oyxs0n34gN3O91wQNzIQh&X-Amz-Signature=23885cec113e2e5488a092119871d80ee6d54f1c3a73a6cbe587249fd8694afa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663EDZB4F%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T075317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDG%2BSHeNx0SCexii46NC00MtBg8qWZ23IFrRHsqxH902AIhAP%2BiZ3T4CwQhidcDd6vCpME%2FfwIhpIsE0Flj8jxuPQfjKv8DCD8QABoMNjM3NDIzMTgzODA1IgyczEis82lTIkICVYMq3APTFdBuCEjYj3xVUlG9s6yIBgbeKWkk7kdwub9xwyVer1QIJXNvY57%2F3wYgbVyBQY0UHtT%2FBfYDLEgYt7F3ftEpA68ydcvUwESWUTcufK82Msfbr3wtzMWLli14dAbyOb0zkvLW4GpNMiF3lErwhjn55bbemSrRFp8rC%2FXFR8mx5U%2B8IbqM7p3ji2Sm1iG070F%2BX7KFr%2B1IvlzgZqcabXhJh8KhRotcKxzksPE7sN0O8BxVLPfOy98fao88murfswX12Z5uIzRGDSgqVbINFtQhgic1r%2FQjvh%2BcqC1oDsGX2TNr0VVVMiaEAgQ%2FzOPeK9vvWu6O%2FGeP1YRyF2w9gj9BgEC%2Buo4%2F59SCIwtDSf4%2BthflgTYKWIQ7PyKV%2Fg1kZdj3FC6m2TeJo%2B6ANiYt%2Ftrwlv41ebsIJR%2FJNMyMm24%2FUVUt7dZxMJCWbx2VPu%2BmX0o%2F9pmIgy%2FYVH3vCS64g9U8y0psIhYnMhEu%2BGdF3XmC7dNuL73t6MFcMIZK9M6TCKz6b0gghaLEZF3pQZuX1sysH03X1%2FB1OvTVm3JkktAaMRixB%2B5SLuwOO392bBfgpdeMIKKhpwZmWjVSlhfP1pvlQ1s20sxZPeqOK%2F2RzUYCngAYcpq8ZqzBOovTpjCN8uHSBjqkAVSJ6MNVou7weoxS%2F9qvHj0F1l4woYxzqMXhmUhyQAbs7%2B4bl6CFTE3gjICP3G0ZosEb0vpEZRKHifnpIuTKl%2BTTyQ6we47pucRRTs6o04PtfNTLKZHGegepW0NrsfSm0Vwa6FV%2FZz2FTL2YJoB6GCcv7%2B9r641%2BX1KPTFCrIEgF9%2B5fVOhaiGfLB3ZkSRvsiqnTGQ6oyxs0n34gN3O91wQNzIQh&X-Amz-Signature=c2ed0c6029bdb2b0bae74a2eb48984f6f2da502d10dc6d411966e1da2ca2ab13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
