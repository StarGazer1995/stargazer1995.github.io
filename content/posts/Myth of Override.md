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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBRWT7PN%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T224839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCXNZdiLcD3dkRes9JV3tJeWTYZigJdzV9MoLn4GgBRMgIgX%2F9jvL76oMcNllwridNW7QSEJdBfhHTQiOxE0MaWlQMq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDLym9LVZxFA5%2BYHrxyrcA85n299FdnC9weH3bFCez%2FoRcXcyP7aXZEvhgPWWmx0h7hbPvSY%2FJ60NakfqToJM9U6rYrULPlUL%2BQ0MMxUXEJXsELcfaZHmjh%2FZbFZStbgXtBFBvXpIC3tdDAzwI1Kkoie8czP3PyvzXXuvxDInZfHi0NuoXxvBNQ9xKWKj4HXQXSTDszwVFWGdn8OfBZUO7mkHzUH7fRz%2F1BtC9hXMhY1n6EgMuTIQj7e7t9278Wp48r6L9UILCRW6I5nGZ%2F%2FiN%2Bu5XGJnZ2auVgWuanI%2FGP2GsrXoRMJXsHWgQCVFbfPIhE5opHvCP1SXphgV0vyo7c3ZFkQeT1Dy3wOWcONMNZ5n%2BDWqdK%2BlLwVLbR0N9TsAtPua54Hbzayq%2BjhupgC%2BEpqT%2BY85JBknbjk7MB0GU3DuoHC7jP5nkjouVJ2Vmy%2F%2FBsJvOjYXruVuJDq75nO8ZUSTnQs7KgS%2Bi5AjgUe8m3nShMAviMT41pZjo4VU55fY58TdveGUzPogLePHkiSETEQrN87pjljd71smCu%2B8EQny9QEzEN0w2v7slUX2Ql1HAAnCw7Mq2IYXnS5Unn6IExExkRGMIWR2ykeoo%2BOkrH28NFjAPI8oJLuNCVkPfn2qkWn45Io0RkRh374wMKmwq9IGOqUBWfZGVC1R8X0siPafhgj2eq4Bej546s20k2%2BenC88P8l3MkI6gqBDEYlKOGKePOkym2rLJjcZbpND%2FhdAib1iQIxM%2FfkjKnvo2I%2BzcdeFLKUGidj8BT8IrUnq2GOzsc6Wgdd2ERpw5V%2FKPVKDK0GULpL%2Fd9%2FzLWJlC9NOzYQoIJwGUq0C%2Fusm4thlT0ITQnppsp0PMkfZUhp91krjJrw771ML%2Bc%2BC&X-Amz-Signature=9cec9f15c2e84243fc83856572d00c7440945a3f0097630b2c912e5b655ec918&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBRWT7PN%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T224840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQCXNZdiLcD3dkRes9JV3tJeWTYZigJdzV9MoLn4GgBRMgIgX%2F9jvL76oMcNllwridNW7QSEJdBfhHTQiOxE0MaWlQMq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDLym9LVZxFA5%2BYHrxyrcA85n299FdnC9weH3bFCez%2FoRcXcyP7aXZEvhgPWWmx0h7hbPvSY%2FJ60NakfqToJM9U6rYrULPlUL%2BQ0MMxUXEJXsELcfaZHmjh%2FZbFZStbgXtBFBvXpIC3tdDAzwI1Kkoie8czP3PyvzXXuvxDInZfHi0NuoXxvBNQ9xKWKj4HXQXSTDszwVFWGdn8OfBZUO7mkHzUH7fRz%2F1BtC9hXMhY1n6EgMuTIQj7e7t9278Wp48r6L9UILCRW6I5nGZ%2F%2FiN%2Bu5XGJnZ2auVgWuanI%2FGP2GsrXoRMJXsHWgQCVFbfPIhE5opHvCP1SXphgV0vyo7c3ZFkQeT1Dy3wOWcONMNZ5n%2BDWqdK%2BlLwVLbR0N9TsAtPua54Hbzayq%2BjhupgC%2BEpqT%2BY85JBknbjk7MB0GU3DuoHC7jP5nkjouVJ2Vmy%2F%2FBsJvOjYXruVuJDq75nO8ZUSTnQs7KgS%2Bi5AjgUe8m3nShMAviMT41pZjo4VU55fY58TdveGUzPogLePHkiSETEQrN87pjljd71smCu%2B8EQny9QEzEN0w2v7slUX2Ql1HAAnCw7Mq2IYXnS5Unn6IExExkRGMIWR2ykeoo%2BOkrH28NFjAPI8oJLuNCVkPfn2qkWn45Io0RkRh374wMKmwq9IGOqUBWfZGVC1R8X0siPafhgj2eq4Bej546s20k2%2BenC88P8l3MkI6gqBDEYlKOGKePOkym2rLJjcZbpND%2FhdAib1iQIxM%2FfkjKnvo2I%2BzcdeFLKUGidj8BT8IrUnq2GOzsc6Wgdd2ERpw5V%2FKPVKDK0GULpL%2Fd9%2FzLWJlC9NOzYQoIJwGUq0C%2Fusm4thlT0ITQnppsp0PMkfZUhp91krjJrw771ML%2Bc%2BC&X-Amz-Signature=e776c4ab6d0c75460dda21210666d7bf82548bdf95c669fede473ef8b824ca6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
