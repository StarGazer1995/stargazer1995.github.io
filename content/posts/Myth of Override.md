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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW6QCE7S%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T014210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdzVc1VzApwozouymw4%2FmRobta4QY2sEOYA9n646hJhgIhAItgAhGno%2BoyiYvfAdxCFM7VYavyjoxVGKXUen6zsZr0KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwX8J12v4cj4Fpwru0q3APsNsA4%2B1yLQoU7GkPxDTnM5CgAK3j9dHeARuzAEyOF%2F%2BPmzVHMs%2F9e15md9nqewDsOEsf7ofDXjdIoDF7Zwi8jCZuYv9gpoZoH7J8%2BQK04amM3zUm55abSJGgZv7SJTgYZIBoEKEUqcHFP94HnQYu99rkvFP9IkjO1xrAeLwzqoPe4L9CR5o9DtxiQVwDXN%2Bps9M6FVLnI3GwRRjCmkLEubDmUbbZZtGkgxRpXkK3i7RU9lPKKlt10Mge84m9bX8VycWfXu1dt4bO%2Fle0o9eu%2FkXBs0NvvFynnQ8oqbcVhzpn5ipX4FsAXRIb%2Fo59TfhGYd2UtQ9ff5pOiCBUHjQ53vs95U9QcvS4oRlubaG%2FfeakcknTAA6o2dCofLjvyMmbJKDl%2BOALgi%2BlU3sle12XnuVKZw2%2FGLm3HJkNdA5i10RT334nhdSj7OuzPXITI0o6HU3H6TpKZf3J%2BGRoMTsbqOrfja7aUF2TsaTiZECUxl1iJzd0rFLJy9d%2BEhJZT35jmd0uXZMU5%2Fqj4Kq4hfpfNWCe%2BaCfuj93jraWEvrWaUmlZYXFei1wAGohDEe%2FusWrhwQVuPwOFNGKfW0X%2F7QlEvFJpV46QoY%2B8aLGgirkgS7kWbqrLHqEaBC%2Fy7zDf3N3UBjqkAbkrSvDdHkEQjUZgjv36OraZtUDqrHjrQN7akRg%2BGoMLHG9%2BHkkkYWBm5aKechwKIAalSZqbTCqndvoa7%2FGhaid25rvSqHVz4zuSqnRaPJue1CgUJL0QLMHhKz%2FTO2ZIX6Laa7N8el1fCnV9mgyU8O2jt7nbNK7yVsgGb730Yk9BDEf%2B23x4bPg2hsYehWPSZJaDfuf3hrmssnAcDDczE6St5W09&X-Amz-Signature=27badb1a59a46e9af4e085fa6d1cbad8b897e4ad8190f1f16c0da5119366397f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW6QCE7S%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T014210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdzVc1VzApwozouymw4%2FmRobta4QY2sEOYA9n646hJhgIhAItgAhGno%2BoyiYvfAdxCFM7VYavyjoxVGKXUen6zsZr0KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwX8J12v4cj4Fpwru0q3APsNsA4%2B1yLQoU7GkPxDTnM5CgAK3j9dHeARuzAEyOF%2F%2BPmzVHMs%2F9e15md9nqewDsOEsf7ofDXjdIoDF7Zwi8jCZuYv9gpoZoH7J8%2BQK04amM3zUm55abSJGgZv7SJTgYZIBoEKEUqcHFP94HnQYu99rkvFP9IkjO1xrAeLwzqoPe4L9CR5o9DtxiQVwDXN%2Bps9M6FVLnI3GwRRjCmkLEubDmUbbZZtGkgxRpXkK3i7RU9lPKKlt10Mge84m9bX8VycWfXu1dt4bO%2Fle0o9eu%2FkXBs0NvvFynnQ8oqbcVhzpn5ipX4FsAXRIb%2Fo59TfhGYd2UtQ9ff5pOiCBUHjQ53vs95U9QcvS4oRlubaG%2FfeakcknTAA6o2dCofLjvyMmbJKDl%2BOALgi%2BlU3sle12XnuVKZw2%2FGLm3HJkNdA5i10RT334nhdSj7OuzPXITI0o6HU3H6TpKZf3J%2BGRoMTsbqOrfja7aUF2TsaTiZECUxl1iJzd0rFLJy9d%2BEhJZT35jmd0uXZMU5%2Fqj4Kq4hfpfNWCe%2BaCfuj93jraWEvrWaUmlZYXFei1wAGohDEe%2FusWrhwQVuPwOFNGKfW0X%2F7QlEvFJpV46QoY%2B8aLGgirkgS7kWbqrLHqEaBC%2Fy7zDf3N3UBjqkAbkrSvDdHkEQjUZgjv36OraZtUDqrHjrQN7akRg%2BGoMLHG9%2BHkkkYWBm5aKechwKIAalSZqbTCqndvoa7%2FGhaid25rvSqHVz4zuSqnRaPJue1CgUJL0QLMHhKz%2FTO2ZIX6Laa7N8el1fCnV9mgyU8O2jt7nbNK7yVsgGb730Yk9BDEf%2B23x4bPg2hsYehWPSZJaDfuf3hrmssnAcDDczE6St5W09&X-Amz-Signature=904672d08f203ae7ca614de23b7f9919449c9816e3ecd5145227f2813cd7b97a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
