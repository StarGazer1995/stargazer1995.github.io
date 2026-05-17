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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FEE3WU%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T203943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9cPI9OeDmM1nLz67Irmzwcmx3M9ZE9Ut4DJCsK%2Fa4uAiEAnCKGf5aHYWkw15PwEyrH9lxZGtag2gCecgJXkW7hfM0qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD4kUSNay3kiO1PCCrcA3BD2fbEoTaUrMGK0z4uviEMMQfDX5wOjgSVNJIdz7a7bUq7K8MYSirqaL4jLxZCTOlurtsKtxffctGzqLbYDe3hVFv07a24rvPeHP4pZnVWILu8tpWVPCrjl9ov%2BZ8%2BQqfJmaQ4ySsdeaenk%2B1Pvkrw%2BtTzq9DwqVrmLkKJVPhuCdYfHeEvJNgzSVqgtdA1bjVN8btebFm7YvBDgYQUCFG3oPs6J6JQOM4%2BGyr2Lnh4gJpQoUAcEprgutFsDcLnFJih%2BFc0v%2B4mbi8eP607SXAz4vOlAph2eA9aPG%2Bh5XkmYoA2gV%2Bv8Pd4bt720f2yYQS7OY95HQUMXzXZi4gQDrniLrt1BVYDp9xV2Ino9mUoGTGoT%2BbRfxVJHMMZiHx1CYDWmCXyeJutl%2Fy7q00wl28Nt9I7Lzji3K1fhlbn7s3u5iRCqM%2ByhK46ZlLxTfTgcJsyufWyGgOt4fI9%2FW0WTtkzGs8SqBjh25bhxUY5M3QzYh4IfYadJJHG3aM3UZoNxbLGOpcX1F5HBJmMv6YQGP%2BZFR6qyOr8uHprxF2Hzh%2BJpVuPIGEsZ2fD4Qs0pKuHIttp3rSlkthq0VZphnYHTJlRmagLwiAgIrxJoNEmYZ2cfKqaYk1FXBF1fVYaMIGTqNAGOqUBpXcrsVjfraSvlVifL7nGjH3mu1oqWFHzTo4VpnJuFTXVlmmwXyGjiDwu2lrspEdue90MmFuPRlkbaHV%2B8F%2FkuFBTZpZLSf95Ph4wkCZ7xZCYwQ%2Fd3utlN%2Fs6CMtC94ClGnkgmtNGLbHoUu5vMynpo8I7ivTck7RWys2FsHb7BZafWUoa8xY45ajd5e%2ByUjDQFPhF3CfDAjlV1vxdrTfWyHV2z46m&X-Amz-Signature=75f81202935a88bb926077e0c8c4f641be4ca58783184e4dfa557ff98d2c5c38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FEE3WU%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T203943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9cPI9OeDmM1nLz67Irmzwcmx3M9ZE9Ut4DJCsK%2Fa4uAiEAnCKGf5aHYWkw15PwEyrH9lxZGtag2gCecgJXkW7hfM0qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD4kUSNay3kiO1PCCrcA3BD2fbEoTaUrMGK0z4uviEMMQfDX5wOjgSVNJIdz7a7bUq7K8MYSirqaL4jLxZCTOlurtsKtxffctGzqLbYDe3hVFv07a24rvPeHP4pZnVWILu8tpWVPCrjl9ov%2BZ8%2BQqfJmaQ4ySsdeaenk%2B1Pvkrw%2BtTzq9DwqVrmLkKJVPhuCdYfHeEvJNgzSVqgtdA1bjVN8btebFm7YvBDgYQUCFG3oPs6J6JQOM4%2BGyr2Lnh4gJpQoUAcEprgutFsDcLnFJih%2BFc0v%2B4mbi8eP607SXAz4vOlAph2eA9aPG%2Bh5XkmYoA2gV%2Bv8Pd4bt720f2yYQS7OY95HQUMXzXZi4gQDrniLrt1BVYDp9xV2Ino9mUoGTGoT%2BbRfxVJHMMZiHx1CYDWmCXyeJutl%2Fy7q00wl28Nt9I7Lzji3K1fhlbn7s3u5iRCqM%2ByhK46ZlLxTfTgcJsyufWyGgOt4fI9%2FW0WTtkzGs8SqBjh25bhxUY5M3QzYh4IfYadJJHG3aM3UZoNxbLGOpcX1F5HBJmMv6YQGP%2BZFR6qyOr8uHprxF2Hzh%2BJpVuPIGEsZ2fD4Qs0pKuHIttp3rSlkthq0VZphnYHTJlRmagLwiAgIrxJoNEmYZ2cfKqaYk1FXBF1fVYaMIGTqNAGOqUBpXcrsVjfraSvlVifL7nGjH3mu1oqWFHzTo4VpnJuFTXVlmmwXyGjiDwu2lrspEdue90MmFuPRlkbaHV%2B8F%2FkuFBTZpZLSf95Ph4wkCZ7xZCYwQ%2Fd3utlN%2Fs6CMtC94ClGnkgmtNGLbHoUu5vMynpo8I7ivTck7RWys2FsHb7BZafWUoa8xY45ajd5e%2ByUjDQFPhF3CfDAjlV1vxdrTfWyHV2z46m&X-Amz-Signature=c4e1424ec69907d846ba21bbea2a37fe064df8517f2d92c945e31e9ae15b90a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
