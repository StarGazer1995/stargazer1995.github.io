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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7NB4OVB%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T015811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDevgiitM0yJi4Bh8WOGm8W%2F4Lk2UV3gIbp3gVJr0RtPQIgNt3HYP%2BPG1ZDwhY6KuMRI4MxccH%2FtK0fj5ceLhUV4awq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDHkuGgidIC1FghLQMircA6GRvRZlADOQHQSxSiWfvmvrSbBVcHbYhvX2CsmKfhq48CAXpVvLAf58fDLZPmDZXOMeY2I0%2BZnBmfOux6369Pp8uBEHmEZWrob0SZgmch46Zg7r9SLgy2AtO9cKfH9SbMMFZX7KEjNlzyvvu4dernroo1HHH9I6Y51GCt6tvVYGD6XZcZivQvYXcxjrE0EPtBEoHrJNh8Pl%2BgGGGycH%2FaCj35XOm64%2F4lkEp54a6KQCSvwB36LbcBtd89pqUKWY%2FRRIW0%2FdNtl6bx6yQrgIj7J7BiputoNBx0lXc7S3dioQTZ6r9LJn8AKioHXC98Vuty5aQIrjTMsqOK4L%2FXngHnv4SAZkmhjMVH6diY5Qgq434e%2Bfmy2kL5YLGPGYsifiE8jt4E19ej1PLl%2FTDcZfj8Iuf7BO5lVO6VqWO79EeXzLjhhgM44o8a2loNW%2BHefb6Nn7mq%2BDinozq1cZirZsyITOhg6B%2BvcT31ygFQEv695imDe%2BUfW6sQLpGrgnTHYhrJ402GMu75Psb8Gz8MGHBdFvURaUVVzSj1qsyNQ2t1XBMcfOPe4phqNLcITLlQdObCFlrmDV4yjzuj9WJWgRsGxD1H1%2B30yoWMcyEqslmcZDy6ZG4jRK1CEYgx2VMOHYk9AGOqUBwgNSrm6kl%2FvETSD2RAidBSs3wf5ZN30yA7Z5AiSvBsjGgJa08HkQ8OB1g1PgYtpJSnWxlRPlDRF5irW4faemvTmJ23QIBLBxYvNi%2BGxQ7gIHMV%2BVThYdFzQ94zLXyGGZDZ0O0XAwpkkSXLRtnCNSdeOezuO5xwVr9T69A1fiDfx7z2LgENyg%2BOMXQvdddDn0KTkupo%2BVu%2FD%2BwHtEWFrAC9x2Bz6f&X-Amz-Signature=70324c0b65ab7a1e2461a5dada8b40761e73cab4f2dcab63ee5035ac0fbfa20d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7NB4OVB%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T015811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDevgiitM0yJi4Bh8WOGm8W%2F4Lk2UV3gIbp3gVJr0RtPQIgNt3HYP%2BPG1ZDwhY6KuMRI4MxccH%2FtK0fj5ceLhUV4awq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDHkuGgidIC1FghLQMircA6GRvRZlADOQHQSxSiWfvmvrSbBVcHbYhvX2CsmKfhq48CAXpVvLAf58fDLZPmDZXOMeY2I0%2BZnBmfOux6369Pp8uBEHmEZWrob0SZgmch46Zg7r9SLgy2AtO9cKfH9SbMMFZX7KEjNlzyvvu4dernroo1HHH9I6Y51GCt6tvVYGD6XZcZivQvYXcxjrE0EPtBEoHrJNh8Pl%2BgGGGycH%2FaCj35XOm64%2F4lkEp54a6KQCSvwB36LbcBtd89pqUKWY%2FRRIW0%2FdNtl6bx6yQrgIj7J7BiputoNBx0lXc7S3dioQTZ6r9LJn8AKioHXC98Vuty5aQIrjTMsqOK4L%2FXngHnv4SAZkmhjMVH6diY5Qgq434e%2Bfmy2kL5YLGPGYsifiE8jt4E19ej1PLl%2FTDcZfj8Iuf7BO5lVO6VqWO79EeXzLjhhgM44o8a2loNW%2BHefb6Nn7mq%2BDinozq1cZirZsyITOhg6B%2BvcT31ygFQEv695imDe%2BUfW6sQLpGrgnTHYhrJ402GMu75Psb8Gz8MGHBdFvURaUVVzSj1qsyNQ2t1XBMcfOPe4phqNLcITLlQdObCFlrmDV4yjzuj9WJWgRsGxD1H1%2B30yoWMcyEqslmcZDy6ZG4jRK1CEYgx2VMOHYk9AGOqUBwgNSrm6kl%2FvETSD2RAidBSs3wf5ZN30yA7Z5AiSvBsjGgJa08HkQ8OB1g1PgYtpJSnWxlRPlDRF5irW4faemvTmJ23QIBLBxYvNi%2BGxQ7gIHMV%2BVThYdFzQ94zLXyGGZDZ0O0XAwpkkSXLRtnCNSdeOezuO5xwVr9T69A1fiDfx7z2LgENyg%2BOMXQvdddDn0KTkupo%2BVu%2FD%2BwHtEWFrAC9x2Bz6f&X-Amz-Signature=24a692e78f73f47c09e9468fffaac4cb814616033dc43494146061bc5cdb0a44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
