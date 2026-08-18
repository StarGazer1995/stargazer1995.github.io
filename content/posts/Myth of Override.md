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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBK2MIEE%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T222941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBkVjaB9nfrhRmMn%2B%2BYBwwJnWrmWzb%2FoyTF%2BgJq7ewYCAiEA3YDIyQ9Zijzy6YwRT2j8Ec2HstPfpZH0arqNXyGo%2Bjgq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDDqfNmxvL%2FdOMxI%2BHyrcA1alxxGFvqWX4sG7ze8LEczGLOsCrrtl4b6Abb48r5CZ3wUjvX7JdTWq2cU62brHDqRJ4fSH1uMVegSTgjKRPPSpVtD6kOFA9dqmUwuwWmCQz8AxrhqFT%2BvF9GczW22W%2Bos1UyVMZ2X13%2Bytiv%2Bx%2BtybcAseOlvw3htVpw7RE%2FfxvANydr65PueCYAXJ49KRjG6O2IbWDqjPXz9H0CmxFqcxzi8lHBmlUHS0okjD42hKx%2FHH9keNI672oz05NEHkS8fn0dq63ZD9O3mSHVoRUZspSJGGfY1t7Ln9kiiTIHfIuQBbK%2Ft2SWs09fPIUvH4YSlioELz5BvTDsGnulJL1VlW1NIib3mAy7XKofXMCrzlApin5mcCm2wvGvo52Plx9XfOlkUS3pgwAg5t0FGwdju5PpVawZ9Xji%2BreBqbU7n6p7Qg5Vypve3r6oL6HnQkK3YVptc%2BUibP3hmINyweXRLvaVXybltJCPtoSnlu25%2BWPEzyoWlqUU0us6za6Bh9BrNIoRKpaJOlwE4STlIhxHlW4iVeJTiOpztHEyzkBSCAyR4kKvkSKv5JXPlPOtiQxZu8Dl4f%2FaLzTyLJpJqk%2Brxze6Eb2%2F5zBKrAHgB27pPy8Mnvc%2FJeL9yQcXa9MIy6ktQGOqUBkClNLz5tcswYXbbIdr5A1M0V5r3XRSWGT35MDT5iAZ90MfIIgMpTEWLHbJbZMBAOedaftYa5chXjeCcl9%2Futte57fIyZXhiY5KLATXkyznZ8AIRfdAuUscWdMKcy4Ocoy36eei5lBlB5%2BYeX3dEuvzoQ5Khzf6MDDhiLd%2FboHzIhxi9LIm2pxm%2Fehi2ZzF5uVHUVrGA7%2F6FsL%2BHu%2FAhNPmO%2Bl0iW&X-Amz-Signature=161ca060f54b60eaf1b0ea4303cd0b409d755155ad1bd87df8a03c11d7224c6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBK2MIEE%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T222941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBkVjaB9nfrhRmMn%2B%2BYBwwJnWrmWzb%2FoyTF%2BgJq7ewYCAiEA3YDIyQ9Zijzy6YwRT2j8Ec2HstPfpZH0arqNXyGo%2Bjgq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDDqfNmxvL%2FdOMxI%2BHyrcA1alxxGFvqWX4sG7ze8LEczGLOsCrrtl4b6Abb48r5CZ3wUjvX7JdTWq2cU62brHDqRJ4fSH1uMVegSTgjKRPPSpVtD6kOFA9dqmUwuwWmCQz8AxrhqFT%2BvF9GczW22W%2Bos1UyVMZ2X13%2Bytiv%2Bx%2BtybcAseOlvw3htVpw7RE%2FfxvANydr65PueCYAXJ49KRjG6O2IbWDqjPXz9H0CmxFqcxzi8lHBmlUHS0okjD42hKx%2FHH9keNI672oz05NEHkS8fn0dq63ZD9O3mSHVoRUZspSJGGfY1t7Ln9kiiTIHfIuQBbK%2Ft2SWs09fPIUvH4YSlioELz5BvTDsGnulJL1VlW1NIib3mAy7XKofXMCrzlApin5mcCm2wvGvo52Plx9XfOlkUS3pgwAg5t0FGwdju5PpVawZ9Xji%2BreBqbU7n6p7Qg5Vypve3r6oL6HnQkK3YVptc%2BUibP3hmINyweXRLvaVXybltJCPtoSnlu25%2BWPEzyoWlqUU0us6za6Bh9BrNIoRKpaJOlwE4STlIhxHlW4iVeJTiOpztHEyzkBSCAyR4kKvkSKv5JXPlPOtiQxZu8Dl4f%2FaLzTyLJpJqk%2Brxze6Eb2%2F5zBKrAHgB27pPy8Mnvc%2FJeL9yQcXa9MIy6ktQGOqUBkClNLz5tcswYXbbIdr5A1M0V5r3XRSWGT35MDT5iAZ90MfIIgMpTEWLHbJbZMBAOedaftYa5chXjeCcl9%2Futte57fIyZXhiY5KLATXkyznZ8AIRfdAuUscWdMKcy4Ocoy36eei5lBlB5%2BYeX3dEuvzoQ5Khzf6MDDhiLd%2FboHzIhxi9LIm2pxm%2Fehi2ZzF5uVHUVrGA7%2F6FsL%2BHu%2FAhNPmO%2Bl0iW&X-Amz-Signature=f99b02bc20e9fd4f70397b14942276bc65a069d52f93c03292aaa0093d2e4de0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
