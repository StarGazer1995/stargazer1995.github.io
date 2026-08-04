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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672QA5HBQ%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T081559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCQYu3ezho8Uq8XzAFzSP%2F2b8IYVVsCU7ynCDxAWfIzsAIgYu2fYy68jyh5IqFGP8EInvVIwU2cC49nIEYhjpiA250q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDNdKczUa%2BUlc8KV7ICrcA3l6FKxkSVzY5ZEdx%2FGqri8T8D7ms%2BkVccsuodeiQd62%2BoUX%2BeH2EKcyZRwT%2FFhKYJ%2FikbTzcn17MvQiXkcVX0FRi8lkR0IMGTouhQMo5sdik8l5Si267E9I3qkB%2FkwsrKXZiWFIntLe9KunamGfOp%2FUueeZMYrRhUo3xYomRJJQ3sze66g6IaDoJ4MG65qwQ7ZVwqLbC7lbOcbpImT%2FHwsIBWm67db%2BdomKXcsIuPjkGoxblaSaKmxCV%2FQP7tEI4Ffm44S4P9727K6DsGnrvPWYgof4z9qjAt35Slaq02L5s49NjJqzGi9JEZf3L18ib77Lg35EzqyZ4gkUKbtzrfOZuB2nHGKI18eHT1vw1b%2FUSb0R17w29XpoMo4JxmEZTzBzQByQHYu53o%2BL4leGuDXT0j0F1fuBmLpXRsPdhUr3OHfc1S0Y1Z3zWHYr9w3ftqtpozsW9BUSsUd8Sz59tpQQ4grjCd0Gr7D8HH0gtUCgX0aANEMZRfTF%2BbPldHFl%2FSYSePH9LTm6nUCF0ZizPl9Utn8UosZNJIkIlUhBa7iySY%2FErHC8Bio2PTtErcU%2BquZLZoy102zo8h54sbdz1z5Se43BdeT%2FoqycBWgWB%2FOP8Gh0aECn0QWfIzvwMK%2B6xtMGOqUB7jnCy2P3mYkhKF9u%2FKSOHCKllWudaiGy2QCV0iXAqEX8nMSO9BYDKOeE7j4r4xOheDfP9GrRe9sPNT8XDEQMzYYPy8uzpCOhUXRADExJ%2B0Ob5Xci6MHGfj6GXftonnSSWKGaThtLu5XG3icKddQHWl%2B5MMtMJ%2BhliVJGz0Dt1LrSx23VYRAtJVT%2FYzHtdREEQ6os1dTNqfOW19R9liDQ%2Fw2Q7cl%2F&X-Amz-Signature=0125774a3df8fcdafd5f3e2667480b0650f2b598e2e45de864fbec1eb910f354&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672QA5HBQ%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T081559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCQYu3ezho8Uq8XzAFzSP%2F2b8IYVVsCU7ynCDxAWfIzsAIgYu2fYy68jyh5IqFGP8EInvVIwU2cC49nIEYhjpiA250q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDNdKczUa%2BUlc8KV7ICrcA3l6FKxkSVzY5ZEdx%2FGqri8T8D7ms%2BkVccsuodeiQd62%2BoUX%2BeH2EKcyZRwT%2FFhKYJ%2FikbTzcn17MvQiXkcVX0FRi8lkR0IMGTouhQMo5sdik8l5Si267E9I3qkB%2FkwsrKXZiWFIntLe9KunamGfOp%2FUueeZMYrRhUo3xYomRJJQ3sze66g6IaDoJ4MG65qwQ7ZVwqLbC7lbOcbpImT%2FHwsIBWm67db%2BdomKXcsIuPjkGoxblaSaKmxCV%2FQP7tEI4Ffm44S4P9727K6DsGnrvPWYgof4z9qjAt35Slaq02L5s49NjJqzGi9JEZf3L18ib77Lg35EzqyZ4gkUKbtzrfOZuB2nHGKI18eHT1vw1b%2FUSb0R17w29XpoMo4JxmEZTzBzQByQHYu53o%2BL4leGuDXT0j0F1fuBmLpXRsPdhUr3OHfc1S0Y1Z3zWHYr9w3ftqtpozsW9BUSsUd8Sz59tpQQ4grjCd0Gr7D8HH0gtUCgX0aANEMZRfTF%2BbPldHFl%2FSYSePH9LTm6nUCF0ZizPl9Utn8UosZNJIkIlUhBa7iySY%2FErHC8Bio2PTtErcU%2BquZLZoy102zo8h54sbdz1z5Se43BdeT%2FoqycBWgWB%2FOP8Gh0aECn0QWfIzvwMK%2B6xtMGOqUB7jnCy2P3mYkhKF9u%2FKSOHCKllWudaiGy2QCV0iXAqEX8nMSO9BYDKOeE7j4r4xOheDfP9GrRe9sPNT8XDEQMzYYPy8uzpCOhUXRADExJ%2B0Ob5Xci6MHGfj6GXftonnSSWKGaThtLu5XG3icKddQHWl%2B5MMtMJ%2BhliVJGz0Dt1LrSx23VYRAtJVT%2FYzHtdREEQ6os1dTNqfOW19R9liDQ%2Fw2Q7cl%2F&X-Amz-Signature=f3a762ad4266c12535f6958251794e93a6b95b49d6d85701f895ed1e918b24da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
