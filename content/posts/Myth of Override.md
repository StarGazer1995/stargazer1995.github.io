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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTV5SGNK%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T170322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIFu4nVXuu2AkwDZ%2B7g2fFSvFZOnJSJT5sa4ImxhBg9EVAiAjprmdg4lQ0qert8UA0RUNw79ncpQhBSzP6lxsIcrnrSr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMKSqoL2%2Fepmdiyf%2BDKtwDCL5KmGZnx%2FtzIUxah8WHNeo435mB3YGnh1HpqnEDG2rXjl4ONkmCEBL7KdZK%2FdPaJ6Lfh5MXCqd8FUKVLjp9cj0JCNc9QiP508KUnK5feMlm4JZrWIUVutkR9OJlGNal4YTgmlEKyUPGNdOe4r02PgMVSavV6IyA5lxmLd8Q9C%2BQPetnAqaydUWbx1MjduTivkvN1xTxP8nyIrOrWYx0GiH80iPV8mnz%2BUp6XkiWsIKNk%2B3hDstWc59pt%2FfZTl4NMjGlRrASK713FliShpmvxH9swoPpEsRy08ILXeQtfXs%2BvXUjkWFuxTfb6L03qCKpiw%2F7kHkHtdI8nIRO%2FNkrIRoZsfomvkDGw9U4U%2BZl1rwBwUUu%2F5r1vWDkANv8VEWLbxcnvysh8zgzTBWMr1qwpmYvlXzq62niPLxJCn9bR1p8EVcX%2BEXLlQ2%2FD8qdALJcHMuu8Z7TFuRR7trW%2BEwGG0CZwh6grg%2BCWWL9zvctkaNxhT82%2BVA5dGk8CgD5YhdxEWNI1T%2BBuOHulRgY7AfBY1yGB8DyiBWj3lsZS60p2SOZ4U0spFSa2U%2FHGIw4J3E62lf09cPz%2FGLmBk7Epn7umPQSz3SfSXq4R25OhRMe1WJoHIFoU6wxsomnBrQwuOve0gY6pgEQPWfLHID1YQ8M9wISe7DCRkWPsDpa92AkEVybNYpoSTCKIA3ilEx%2BH9j9JoA2v7NXNZcqo83lXuUv8yfjRM%2Fiv2XKpOUudb7dv6mzjUhFIzrJ9PVakjXJ0U3usXanwB8pTxlocLJr%2BNI7Lge3hdgv5U%2Bj7E93WNiRjX0190N8dxI7s3Sje%2F%2FYeMsBsxIK4nF9Hm6B1dKBJwbx5r7geGPKpEKIANc7&X-Amz-Signature=3dfd01941c6afa3151422d3185bfe3466a2f2e4dc9ea2e2be130f41eb8e764f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTV5SGNK%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T170322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIFu4nVXuu2AkwDZ%2B7g2fFSvFZOnJSJT5sa4ImxhBg9EVAiAjprmdg4lQ0qert8UA0RUNw79ncpQhBSzP6lxsIcrnrSr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMKSqoL2%2Fepmdiyf%2BDKtwDCL5KmGZnx%2FtzIUxah8WHNeo435mB3YGnh1HpqnEDG2rXjl4ONkmCEBL7KdZK%2FdPaJ6Lfh5MXCqd8FUKVLjp9cj0JCNc9QiP508KUnK5feMlm4JZrWIUVutkR9OJlGNal4YTgmlEKyUPGNdOe4r02PgMVSavV6IyA5lxmLd8Q9C%2BQPetnAqaydUWbx1MjduTivkvN1xTxP8nyIrOrWYx0GiH80iPV8mnz%2BUp6XkiWsIKNk%2B3hDstWc59pt%2FfZTl4NMjGlRrASK713FliShpmvxH9swoPpEsRy08ILXeQtfXs%2BvXUjkWFuxTfb6L03qCKpiw%2F7kHkHtdI8nIRO%2FNkrIRoZsfomvkDGw9U4U%2BZl1rwBwUUu%2F5r1vWDkANv8VEWLbxcnvysh8zgzTBWMr1qwpmYvlXzq62niPLxJCn9bR1p8EVcX%2BEXLlQ2%2FD8qdALJcHMuu8Z7TFuRR7trW%2BEwGG0CZwh6grg%2BCWWL9zvctkaNxhT82%2BVA5dGk8CgD5YhdxEWNI1T%2BBuOHulRgY7AfBY1yGB8DyiBWj3lsZS60p2SOZ4U0spFSa2U%2FHGIw4J3E62lf09cPz%2FGLmBk7Epn7umPQSz3SfSXq4R25OhRMe1WJoHIFoU6wxsomnBrQwuOve0gY6pgEQPWfLHID1YQ8M9wISe7DCRkWPsDpa92AkEVybNYpoSTCKIA3ilEx%2BH9j9JoA2v7NXNZcqo83lXuUv8yfjRM%2Fiv2XKpOUudb7dv6mzjUhFIzrJ9PVakjXJ0U3usXanwB8pTxlocLJr%2BNI7Lge3hdgv5U%2Bj7E93WNiRjX0190N8dxI7s3Sje%2F%2FYeMsBsxIK4nF9Hm6B1dKBJwbx5r7geGPKpEKIANc7&X-Amz-Signature=9a374ac44fdb329ff985cbf76d26fcd798384829a5783dd41e2e345e3eb25b12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
