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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJCK5ZXH%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEsWchf2wHzKDCZjCqlf3czSG29YjUk8UzJ%2FX%2FQpgcLwIgRGtlJyRaq9SMNk0YGvDTCSDe5HTfFZMszt6%2BD%2BvN91Aq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDNpHc1iqQ%2FK99l82TircA1bRwuipSjk5Lut2N5eRhbSNvWWeZ%2BUsHKp6pM66MxpwFwP93hZ5AQFw9chiwhVydj2RkiSspeCRS%2FVXOPZm5x2bvYcoD%2BikXpidbHcBdKiOlIMzNm1HjVH5jX7u3SJHvVXKBHxsTEdel5B0Zw9HQSN315R6eyiTHI4iJs4YwO4%2Fe1uT3id%2FHSYgZPXwCbWbjylmOb%2FPCcWFnIw9MtZj0WqTG%2FgSZnvKFtXQfIZEByHv9DCzgSuBBPkLwjDUM08Bqa3ln%2BKhUc8oWNIw3TYs54TdfpAK4gpi81IL9gvYmijy5NJpF9yzLNVwIpmkVTB6R%2Bp49eaIeB9j9lFso0A%2BkdasiQcvAhLmqyQW3qFR4GsalSIN8BYZIYs74d2skycVUe6yDgSBbK8pxfsby%2FHftH5WK2HhuAa%2FKHCwYzfl1v7uLXKaXC9JN3osebKotMGoelSCFhEter2lRSjdtgdDCUsfJaKoQ8kumKS7du%2FCA7PalcFgQlaFvBhwd8W8HNEQ5pPtfFaVpSRwMfEc88biKLRPflOtMdiyDz%2Bs9y3QWot%2FVZRsKkEHoRuhZ7QbliZUQZOk8K3Z56HUlr%2FcYIwPN3tjo%2FgK27z51U%2F0N6y6QNb5uW5YwI5%2FCCYJ4y0tMO6dyNQGOqUB7hs3gYjboyfFbJgnQLlQyU4rV5kITGlyRwulvoECXHeDBPp5FG47MJhjOXM0Ld4ciXvnNsLXMR7w7bSbthHysO69d1iwMXyJILEzYgvGJoUU%2B3IFd5v5lwaKTIhOTm37PskWCP5DqvmuevlBUUZ2c%2BCoay5vsnIAhyATZQNKOmUYvB4UFvl7zJTSQmxb7C%2BepqXTLYeEyJJJ3RuUymug2JqWHV18&X-Amz-Signature=d45322162874dafbc00d4bacf6f0ccf7a1ca940a7fec46b424b725ae833ae0d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJCK5ZXH%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T231610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCEsWchf2wHzKDCZjCqlf3czSG29YjUk8UzJ%2FX%2FQpgcLwIgRGtlJyRaq9SMNk0YGvDTCSDe5HTfFZMszt6%2BD%2BvN91Aq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDNpHc1iqQ%2FK99l82TircA1bRwuipSjk5Lut2N5eRhbSNvWWeZ%2BUsHKp6pM66MxpwFwP93hZ5AQFw9chiwhVydj2RkiSspeCRS%2FVXOPZm5x2bvYcoD%2BikXpidbHcBdKiOlIMzNm1HjVH5jX7u3SJHvVXKBHxsTEdel5B0Zw9HQSN315R6eyiTHI4iJs4YwO4%2Fe1uT3id%2FHSYgZPXwCbWbjylmOb%2FPCcWFnIw9MtZj0WqTG%2FgSZnvKFtXQfIZEByHv9DCzgSuBBPkLwjDUM08Bqa3ln%2BKhUc8oWNIw3TYs54TdfpAK4gpi81IL9gvYmijy5NJpF9yzLNVwIpmkVTB6R%2Bp49eaIeB9j9lFso0A%2BkdasiQcvAhLmqyQW3qFR4GsalSIN8BYZIYs74d2skycVUe6yDgSBbK8pxfsby%2FHftH5WK2HhuAa%2FKHCwYzfl1v7uLXKaXC9JN3osebKotMGoelSCFhEter2lRSjdtgdDCUsfJaKoQ8kumKS7du%2FCA7PalcFgQlaFvBhwd8W8HNEQ5pPtfFaVpSRwMfEc88biKLRPflOtMdiyDz%2Bs9y3QWot%2FVZRsKkEHoRuhZ7QbliZUQZOk8K3Z56HUlr%2FcYIwPN3tjo%2FgK27z51U%2F0N6y6QNb5uW5YwI5%2FCCYJ4y0tMO6dyNQGOqUB7hs3gYjboyfFbJgnQLlQyU4rV5kITGlyRwulvoECXHeDBPp5FG47MJhjOXM0Ld4ciXvnNsLXMR7w7bSbthHysO69d1iwMXyJILEzYgvGJoUU%2B3IFd5v5lwaKTIhOTm37PskWCP5DqvmuevlBUUZ2c%2BCoay5vsnIAhyATZQNKOmUYvB4UFvl7zJTSQmxb7C%2BepqXTLYeEyJJJ3RuUymug2JqWHV18&X-Amz-Signature=00358f93be59536ec71dcd4000f5ac8e2aab4193b8914bb166dc0e316ad4c4c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
