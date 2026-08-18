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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWS4ZEZP%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T062215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSmkMD7yE9j25Ar3%2BFBySxt7LGg%2FrZxaItHO1E9rDzcQIgaTRX6pOtJbrWbAvWqluWfUo%2F7Cr3bepcpO9RP0pNJG8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDKlOkRwEr9d%2Bd2nzPCrcAwdUyYLFNIwyeB4lD%2B59G8TXZ%2B6Mx%2BAl6SxY0KkqLImADOOUxLTOCW1R0hngDzAWAaqE0sSzaZD61pykciXs96rLBWMh1cNuxqWR9a%2FEYftSQ32COo24AiYPHc6bR6X%2Bq0XsH%2BuPntLfJci%2FRGcWgdGj1KRKN1sUIG3%2BnvZDP56VR11sgXYv0009y9WBSJPSfYFbdAEYjC9YbnHAdNSKZdtzDL2ID6MTD9Jf5pH5sGMv87G3afmarMiFF8326sn5d4sknsz1MTWo9U9RYJoMByCYVJm9t2JjZtChTYE%2F%2FlhSXh8Vwx9kUESZ%2FK9gXqzyOYLSoCo1c69khpGpvbf3iiKDItCdqTwEZ%2Fx9WMzd%2BaL%2FWZiXK2FFp1dKQFG6kanetCmO28xI8nEzh0SK3ujnbkyeHrO4ZlgMDmQjORo3hF28aAiJx8c15G3qb9VUYjwcf%2F8gC1ZlwX7GQcZCWZqRuVKeLVKsjpPHHQ2ZKFYDJ5MS%2FnBdd44rhJo7qT5ojTcr%2FI7kuwVp6RNliauuIDTw7R6u%2BUkOSCxhUmc2cjqGiyNoZiKOxDi1EcuVr5pEWITHEH%2BXqbugQ0HrEm3YPy1l5eNJSQbaiEEK81vcXduyM68iLmeJHCUsO2rKecRRMPy1j9QGOqUBex8pp9XoLoE8wmSxt1POps5p6l9TYIhSWYGhid0gxZ6A9f0A%2FdehwYOGMjZOBVC9BxxZOVJT7j2XmJeh869jRzVgoAIxkMyCT4q8DJuBlP1b5KJ5T13nWbJ5jvh04nLaE8RsmY1Fqg1qjiKuR0%2FR%2FBretTJp935IoQnkjr%2FoUn91AdQw5lxPPP89C%2F7ib1zBrrfLcmb60PMLA7e2rkP7U6fPbw2B&X-Amz-Signature=a92d7bd5b04d26f00e660c69c41a1f794b1a1d6733aba806e27d830f0a832511&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWS4ZEZP%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T062215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSmkMD7yE9j25Ar3%2BFBySxt7LGg%2FrZxaItHO1E9rDzcQIgaTRX6pOtJbrWbAvWqluWfUo%2F7Cr3bepcpO9RP0pNJG8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDKlOkRwEr9d%2Bd2nzPCrcAwdUyYLFNIwyeB4lD%2B59G8TXZ%2B6Mx%2BAl6SxY0KkqLImADOOUxLTOCW1R0hngDzAWAaqE0sSzaZD61pykciXs96rLBWMh1cNuxqWR9a%2FEYftSQ32COo24AiYPHc6bR6X%2Bq0XsH%2BuPntLfJci%2FRGcWgdGj1KRKN1sUIG3%2BnvZDP56VR11sgXYv0009y9WBSJPSfYFbdAEYjC9YbnHAdNSKZdtzDL2ID6MTD9Jf5pH5sGMv87G3afmarMiFF8326sn5d4sknsz1MTWo9U9RYJoMByCYVJm9t2JjZtChTYE%2F%2FlhSXh8Vwx9kUESZ%2FK9gXqzyOYLSoCo1c69khpGpvbf3iiKDItCdqTwEZ%2Fx9WMzd%2BaL%2FWZiXK2FFp1dKQFG6kanetCmO28xI8nEzh0SK3ujnbkyeHrO4ZlgMDmQjORo3hF28aAiJx8c15G3qb9VUYjwcf%2F8gC1ZlwX7GQcZCWZqRuVKeLVKsjpPHHQ2ZKFYDJ5MS%2FnBdd44rhJo7qT5ojTcr%2FI7kuwVp6RNliauuIDTw7R6u%2BUkOSCxhUmc2cjqGiyNoZiKOxDi1EcuVr5pEWITHEH%2BXqbugQ0HrEm3YPy1l5eNJSQbaiEEK81vcXduyM68iLmeJHCUsO2rKecRRMPy1j9QGOqUBex8pp9XoLoE8wmSxt1POps5p6l9TYIhSWYGhid0gxZ6A9f0A%2FdehwYOGMjZOBVC9BxxZOVJT7j2XmJeh869jRzVgoAIxkMyCT4q8DJuBlP1b5KJ5T13nWbJ5jvh04nLaE8RsmY1Fqg1qjiKuR0%2FR%2FBretTJp935IoQnkjr%2FoUn91AdQw5lxPPP89C%2F7ib1zBrrfLcmb60PMLA7e2rkP7U6fPbw2B&X-Amz-Signature=95415fadaad33b9c8d4140bfbc05fdf044f0b072a2d95fe8abcf60c8a621381a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
