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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V64MR6YY%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T180024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC293pBrQ6%2FwRvzuMbOsURHHazhHTMIZyAfrWjHDkcLGgIhAL5Y0oGqfCnZhMiVqn4f%2BkSjDFSm4P7sGLo%2Fu3ecJjILKv8DCCoQABoMNjM3NDIzMTgzODA1IgyhrTnNFJ%2BBtdwOa3gq3APHKZubX1S5zlodxskpfSIJWNRxFizyfHz570zNbi9gDgBhUDq2Y3A%2BUBbECWVVO1ZfL0qOYN3koAwYdbRttiZ0kiKrLcuOhCkFwskLYq%2B92iWyje9QoIa82BHL%2FkUYO5tkn7Za2cXsD38OITvIlQc9J%2FHqT03YOlyTbY0sxn4FMGse3VBRlLHSy4w0QlKfR%2B6bnbrPCwE6VpDGXytVLjfGd1AM%2FZn1h%2B12jV4KFaG2y0TI8RVLX2RS77%2BKTD1fdf%2FNO5V17KdzY2QAgn6xLxiXYTHhJHH%2BeChPLHa5GDVv95uSbMmm991x1vuDwwhRinZBVKCbQoDO25itqicwjGLmE7WiITPSQ3Zb8znqbtlfug21qlUMhalKQpm3Z2NMefgOUtucC%2BKjzukFOpiKAbTmJckAN2j3S2cHuJvvNpwdN8ygpZLzJd5yYYEF6suHNnjfhIJankhk8wuvxA5v5anA19rr7MKbxtGh2smPbhfG2DVJrx9Fp9CTM%2B8Ie6AHNJ46u4z8wyh2%2FGLFaEdg2E%2BAruxJ0wjy0%2F15Y6cVNlcuR%2BoQEdZwlKwpC6jAMHcL24JIRWUNjOmC%2FQssAG9cK8KwqGNWYMQiPc47AOfxOebbO%2FNHEVIanIwBB5feGzDpofzQBjqkAYOxyboz7OfmOiOgs8EvpJHR15i5RBjlYHaeoYA9A0ynBGmyzAHipe2N2M%2BJWjoBr%2B9HMOZc82WyY4fT9RkkZpYNXjMv2HR%2BBVD9SwbPaCzEZ3XBCJGClooKcdOPInJ36XTLcXhuaE2fYoC9TfKraOKmdWq4ZPb2rkZ82i%2BiTk0OhkOf2Je%2FVOm%2F5o4Siy9RqNvbijSM62qAkdqEYf%2FOy%2BfCkdvC&X-Amz-Signature=6ca1ee383d13d49393a3951ec9cd7f8eaf922bc2c8dcee251b44aba20584368c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V64MR6YY%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T180024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC293pBrQ6%2FwRvzuMbOsURHHazhHTMIZyAfrWjHDkcLGgIhAL5Y0oGqfCnZhMiVqn4f%2BkSjDFSm4P7sGLo%2Fu3ecJjILKv8DCCoQABoMNjM3NDIzMTgzODA1IgyhrTnNFJ%2BBtdwOa3gq3APHKZubX1S5zlodxskpfSIJWNRxFizyfHz570zNbi9gDgBhUDq2Y3A%2BUBbECWVVO1ZfL0qOYN3koAwYdbRttiZ0kiKrLcuOhCkFwskLYq%2B92iWyje9QoIa82BHL%2FkUYO5tkn7Za2cXsD38OITvIlQc9J%2FHqT03YOlyTbY0sxn4FMGse3VBRlLHSy4w0QlKfR%2B6bnbrPCwE6VpDGXytVLjfGd1AM%2FZn1h%2B12jV4KFaG2y0TI8RVLX2RS77%2BKTD1fdf%2FNO5V17KdzY2QAgn6xLxiXYTHhJHH%2BeChPLHa5GDVv95uSbMmm991x1vuDwwhRinZBVKCbQoDO25itqicwjGLmE7WiITPSQ3Zb8znqbtlfug21qlUMhalKQpm3Z2NMefgOUtucC%2BKjzukFOpiKAbTmJckAN2j3S2cHuJvvNpwdN8ygpZLzJd5yYYEF6suHNnjfhIJankhk8wuvxA5v5anA19rr7MKbxtGh2smPbhfG2DVJrx9Fp9CTM%2B8Ie6AHNJ46u4z8wyh2%2FGLFaEdg2E%2BAruxJ0wjy0%2F15Y6cVNlcuR%2BoQEdZwlKwpC6jAMHcL24JIRWUNjOmC%2FQssAG9cK8KwqGNWYMQiPc47AOfxOebbO%2FNHEVIanIwBB5feGzDpofzQBjqkAYOxyboz7OfmOiOgs8EvpJHR15i5RBjlYHaeoYA9A0ynBGmyzAHipe2N2M%2BJWjoBr%2B9HMOZc82WyY4fT9RkkZpYNXjMv2HR%2BBVD9SwbPaCzEZ3XBCJGClooKcdOPInJ36XTLcXhuaE2fYoC9TfKraOKmdWq4ZPb2rkZ82i%2BiTk0OhkOf2Je%2FVOm%2F5o4Siy9RqNvbijSM62qAkdqEYf%2FOy%2BfCkdvC&X-Amz-Signature=ddf9a1f7d967502a6ff8cd5ba6894d73f18db4245a91c9553de8537c34c807b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
