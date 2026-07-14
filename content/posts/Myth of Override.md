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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLCC625%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T151517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJIMEYCIQD5sD3EcSlDjzY0smWlh7nUo1OQDwG6u4Spb%2FoovHhx9QIhAJswfG5oaAYcSySDFCuZ9LMtUUq%2F6CxbeT63xH%2FngJsAKv8DCBcQABoMNjM3NDIzMTgzODA1IgzL%2B1SwbqzSvka%2F0Lsq3AMWhEdhAGlSjjbxDBiRIsxOcMqA8jds0%2FPqKd%2F%2BjodrS8swNXXlqmJIrPG2ohHZdZKA3DfsQR7wyxAggNBq6kGOnY4g2zUgsSEpsRuQIy%2BE2hj328Q%2FnjLnoydCWHId7d7Vd6UVJchIhSFC32TUwhlYWqIbHI11hqjfXXm%2BVbRY7ilyU1xgo2w3OiyjiuA5BPi9uZsVGQPWslQclgpjxzC%2B%2Fe8TLF6D%2BKHFv0cU2GirX3z4RdUNwqqaVVqFkbaA0A0uYsB0Ajh5%2BpW6WIZwjrCdEq1lKA88b1wFseWplNzVecvsxXJSLx09MUVQuJ1Ka0HJfSXT6FOaNwEJoGL8CAW7c7CHbdCvDvrbYnSXbMJwaok%2BQoqCscnCZiT8baQHYSqkymOlAlo2uyJ3jTyvFHpP1HQ2DkiK1QK5l2d4rJn%2F5FKH17USGi%2BK%2FhmNQPhqsq1SVhYFAMvfIg9kumisEwpwfkcyYRkfNLcBKlRKZpDMehJcR791%2FriodXPh0QRPhcwUFfg0p3zhVuXSy8mBcJ6%2FsZBhk76vGDfSO5wX5CUwkROnyfhM2p%2BoAgv%2FofEZRYtfjA1%2BsYbDAmBBSa7l1O9ziKiN4XnTKnuRaQlGtgIaLGtziomZfg0pqsDi3TC1%2FtjSBjqkAXufVAQhE%2F3jhR2c7ZIkdcwfPbB02jo8rPp46aOJV9QEeWu%2BOCsYFkwnSMqYtOAyabfn14%2BTsSJBp2V7mE2K1a4LxSEwyTBhqEiUAPJRe48hJ7Oo99J5lcoLLxwnPf8wRM1ldjCDXg3IXPVEUhlzAWc1oA%2FxT%2FzMpnQlxwVNn0OjZScs94FGWVE5zqXEEMtp%2BrCqY%2Fm8xBUUMbmi59kl7tFQs6Bh&X-Amz-Signature=ed58f589e61741867d5d72c94dba7efb54a0a8097cf7234c02b0e32577865ba7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLCC625%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T151517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJIMEYCIQD5sD3EcSlDjzY0smWlh7nUo1OQDwG6u4Spb%2FoovHhx9QIhAJswfG5oaAYcSySDFCuZ9LMtUUq%2F6CxbeT63xH%2FngJsAKv8DCBcQABoMNjM3NDIzMTgzODA1IgzL%2B1SwbqzSvka%2F0Lsq3AMWhEdhAGlSjjbxDBiRIsxOcMqA8jds0%2FPqKd%2F%2BjodrS8swNXXlqmJIrPG2ohHZdZKA3DfsQR7wyxAggNBq6kGOnY4g2zUgsSEpsRuQIy%2BE2hj328Q%2FnjLnoydCWHId7d7Vd6UVJchIhSFC32TUwhlYWqIbHI11hqjfXXm%2BVbRY7ilyU1xgo2w3OiyjiuA5BPi9uZsVGQPWslQclgpjxzC%2B%2Fe8TLF6D%2BKHFv0cU2GirX3z4RdUNwqqaVVqFkbaA0A0uYsB0Ajh5%2BpW6WIZwjrCdEq1lKA88b1wFseWplNzVecvsxXJSLx09MUVQuJ1Ka0HJfSXT6FOaNwEJoGL8CAW7c7CHbdCvDvrbYnSXbMJwaok%2BQoqCscnCZiT8baQHYSqkymOlAlo2uyJ3jTyvFHpP1HQ2DkiK1QK5l2d4rJn%2F5FKH17USGi%2BK%2FhmNQPhqsq1SVhYFAMvfIg9kumisEwpwfkcyYRkfNLcBKlRKZpDMehJcR791%2FriodXPh0QRPhcwUFfg0p3zhVuXSy8mBcJ6%2FsZBhk76vGDfSO5wX5CUwkROnyfhM2p%2BoAgv%2FofEZRYtfjA1%2BsYbDAmBBSa7l1O9ziKiN4XnTKnuRaQlGtgIaLGtziomZfg0pqsDi3TC1%2FtjSBjqkAXufVAQhE%2F3jhR2c7ZIkdcwfPbB02jo8rPp46aOJV9QEeWu%2BOCsYFkwnSMqYtOAyabfn14%2BTsSJBp2V7mE2K1a4LxSEwyTBhqEiUAPJRe48hJ7Oo99J5lcoLLxwnPf8wRM1ldjCDXg3IXPVEUhlzAWc1oA%2FxT%2FzMpnQlxwVNn0OjZScs94FGWVE5zqXEEMtp%2BrCqY%2Fm8xBUUMbmi59kl7tFQs6Bh&X-Amz-Signature=517d119c297249db043b1e4a16c0fea46cf0816713815a77c0c728d8f00455a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
