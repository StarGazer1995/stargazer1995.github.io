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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UBPMPU2%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T135832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BtN62y95NlBK8jTCFzcXUaZcZK%2B6eYN5IU04bF7S4CAiEA%2F%2Bnd34sVcmzr1scoW7OWLOb28D0R4n9HTIimo7aGVyQqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1gJQdA%2B7Xa2u1wXCrcA0c6xM7dn7cPLf0HKZY1YJyUzu250EzKnxhJ%2F%2Bp3%2F7CymVWLRo2mPJw8XY3TbxrPIsk9YokkRUS6J7on3OQeO71Ggw%2FgtroEJO%2Bi8krb8zvbkK89WGSIW4kiu5F7HFjgOnUkf2jB7Dv1c1ZgFApoDIutLbAwWIJLT6R7%2FDWVDiEwKADgU4DeE8IUN9FQnE5IcMCj%2BLRUR%2FD33WEeWK0XGNyHjs6ljNH3X0j5LvGaQZiw6GcyVWa3%2BInXgdqxEvp%2FdKFRE7G3oj4K5wBcSkcErPOlnn0LAE%2BnsjOFPUtJxQmMRjJrUR80SgwfW8c4jW%2BtzEQnEEOFheguNXfoMPJvrWTnN9zFVO4BpGtqVy%2B2UFLrUhWa8qOGDNVnh06d4ccbn8Kq4UT11dQ%2FGj2nedAm2lQeZmcSE%2FJ7gzF%2FXWQukXKUMwwv7XW8z%2BJq60y4MoEgl2C1rbfunX5y0RYM7zznqU1jv3u4q91voGBO29YdE3DwnhEdlcn3SOc8GJiZqZ7eZaMiFwoQN%2BYDAEFEi%2B3a0EhUlTvsYsZg8YJ3zTOJA8tLb0zfA6164vpMlKqbyQeYkxxEuSnrGnRZ7c%2BY%2B9Dws3eC7GuC0P%2B0OMswUHLNy0lZCzJGeqHC32hScvz9MIDfidIGOqUBbgKAwVWmRyQ17pXq%2FMMx6wGnQD95wyp0TrILmh5XkFeViqAvADfMklakLR%2F0DGL%2FXkZbGZWsde%2FHvp189DoWjQItdXdyyZI%2BKShjTsyp3tqNXit68lB9gGa%2BgijCoifAWfInIwWT66vKu7JRqaQjOFAZShC%2F0oEtquCzvWKlupfAyiWXsgI5CnzxAuD%2BZVhlFykxCApELfubXtUD8B1%2FYx273tt1&X-Amz-Signature=24dfd79083d8c745184826338fbd58c38b7f4dbb18cd29a6e8cd62c5a885f6ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UBPMPU2%2F20260629%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260629T135832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BtN62y95NlBK8jTCFzcXUaZcZK%2B6eYN5IU04bF7S4CAiEA%2F%2Bnd34sVcmzr1scoW7OWLOb28D0R4n9HTIimo7aGVyQqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1gJQdA%2B7Xa2u1wXCrcA0c6xM7dn7cPLf0HKZY1YJyUzu250EzKnxhJ%2F%2Bp3%2F7CymVWLRo2mPJw8XY3TbxrPIsk9YokkRUS6J7on3OQeO71Ggw%2FgtroEJO%2Bi8krb8zvbkK89WGSIW4kiu5F7HFjgOnUkf2jB7Dv1c1ZgFApoDIutLbAwWIJLT6R7%2FDWVDiEwKADgU4DeE8IUN9FQnE5IcMCj%2BLRUR%2FD33WEeWK0XGNyHjs6ljNH3X0j5LvGaQZiw6GcyVWa3%2BInXgdqxEvp%2FdKFRE7G3oj4K5wBcSkcErPOlnn0LAE%2BnsjOFPUtJxQmMRjJrUR80SgwfW8c4jW%2BtzEQnEEOFheguNXfoMPJvrWTnN9zFVO4BpGtqVy%2B2UFLrUhWa8qOGDNVnh06d4ccbn8Kq4UT11dQ%2FGj2nedAm2lQeZmcSE%2FJ7gzF%2FXWQukXKUMwwv7XW8z%2BJq60y4MoEgl2C1rbfunX5y0RYM7zznqU1jv3u4q91voGBO29YdE3DwnhEdlcn3SOc8GJiZqZ7eZaMiFwoQN%2BYDAEFEi%2B3a0EhUlTvsYsZg8YJ3zTOJA8tLb0zfA6164vpMlKqbyQeYkxxEuSnrGnRZ7c%2BY%2B9Dws3eC7GuC0P%2B0OMswUHLNy0lZCzJGeqHC32hScvz9MIDfidIGOqUBbgKAwVWmRyQ17pXq%2FMMx6wGnQD95wyp0TrILmh5XkFeViqAvADfMklakLR%2F0DGL%2FXkZbGZWsde%2FHvp189DoWjQItdXdyyZI%2BKShjTsyp3tqNXit68lB9gGa%2BgijCoifAWfInIwWT66vKu7JRqaQjOFAZShC%2F0oEtquCzvWKlupfAyiWXsgI5CnzxAuD%2BZVhlFykxCApELfubXtUD8B1%2FYx273tt1&X-Amz-Signature=06cbc59045b6689220403521291b850ff75b893039b86e793f506e47cb3da015&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
