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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XALVCXMR%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T125039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIBMYr%2F%2F4Qg8s4KTKk6beZ7wWqhRvPLkBl8g3d5jWkWzBAiBznReaLPnYgPIumyMZ3VDC1zxMJoQgGsSGl9VMxil4tyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Fl9O46z2lSPra3AKtwDph70iwnSwnsP%2Fx7DpgQtjLU6EXMr6PNX3IciXtfdN3QzNyYl6TVFy4tTk56E6mgh3FMjjGETjmk%2BQYW9Z6nuXXgdIg3fgApjhlTzHbbdn5O919fuevcF7a%2F8A0RDZgrVFZ6nZbyTBKp4ElAMj9069EovGDudXo7nnp3KKmFqxe233gdu3EuyU%2F2TzDVKDtN85Drly09yMUW5jpoiRGBEFbE0DZqmblt5xx5rDAg6qzQxacG1j4XBlS7H7i9pdzhMQXaduOQD8jN6TJZqkMZwd01rw1zZjwtlRHSQ0dBBM4GTjB%2FWf7Wj%2Bu%2Fq0LEw%2B4geh%2BGlNE8IEbAHPmww38aX9bYfBXLqR0GXuDIKGZLxw3SWosasfK3riua8828xdSEEzusG8HhqI56Gx13UXdCPp238VDeiC1nqtHgqL5SuxIdoUB0uZGZmkNOss9h0i8E6W%2BFJQOwpOlD5RGtJARHdWJTJ5nqKFYtSu%2BVR%2FLDwbQcQO%2FiHAHSZ4LEOMt9XWQLe70XMYKLa31zfSHG2qBGC%2B3Mn%2F%2BwFmksTKF%2BmZkpPP6MUwpYkORGsZuT%2FWf%2FDF9aOpmDnSJR9d8dgBWlrrq%2B948jV4OI%2BvdFXTmd3olJP2GKvOd3Mh%2BRXa%2B%2BO3lcwkbKB0AY6pgEN9SY9bdjYqV5tyXagKxQPjz1t9BdhScP0jlEMEV86jYFQ5UuE59t5%2FJ%2F56wOWP9w%2BUL%2Fo3oZYYVsqGVXIC9qi4mgLaI6RLXs7r%2B3THi0VUTWAkWcsHBM7EE%2B0ErGRX%2F2hZRZww0c6EbWO4W7uOeOThkXwu15ryQZYPxkBXOCtBRSUsHlUoPgbYuHTwhIwOJwUoT68DkyIqmSOhO%2FkDPx6vQviQHL3&X-Amz-Signature=67b7468d7e908cc352158721816cd129e9fda1924ea7314514ebcacefa7e88d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XALVCXMR%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T125039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIBMYr%2F%2F4Qg8s4KTKk6beZ7wWqhRvPLkBl8g3d5jWkWzBAiBznReaLPnYgPIumyMZ3VDC1zxMJoQgGsSGl9VMxil4tyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2Fl9O46z2lSPra3AKtwDph70iwnSwnsP%2Fx7DpgQtjLU6EXMr6PNX3IciXtfdN3QzNyYl6TVFy4tTk56E6mgh3FMjjGETjmk%2BQYW9Z6nuXXgdIg3fgApjhlTzHbbdn5O919fuevcF7a%2F8A0RDZgrVFZ6nZbyTBKp4ElAMj9069EovGDudXo7nnp3KKmFqxe233gdu3EuyU%2F2TzDVKDtN85Drly09yMUW5jpoiRGBEFbE0DZqmblt5xx5rDAg6qzQxacG1j4XBlS7H7i9pdzhMQXaduOQD8jN6TJZqkMZwd01rw1zZjwtlRHSQ0dBBM4GTjB%2FWf7Wj%2Bu%2Fq0LEw%2B4geh%2BGlNE8IEbAHPmww38aX9bYfBXLqR0GXuDIKGZLxw3SWosasfK3riua8828xdSEEzusG8HhqI56Gx13UXdCPp238VDeiC1nqtHgqL5SuxIdoUB0uZGZmkNOss9h0i8E6W%2BFJQOwpOlD5RGtJARHdWJTJ5nqKFYtSu%2BVR%2FLDwbQcQO%2FiHAHSZ4LEOMt9XWQLe70XMYKLa31zfSHG2qBGC%2B3Mn%2F%2BwFmksTKF%2BmZkpPP6MUwpYkORGsZuT%2FWf%2FDF9aOpmDnSJR9d8dgBWlrrq%2B948jV4OI%2BvdFXTmd3olJP2GKvOd3Mh%2BRXa%2B%2BO3lcwkbKB0AY6pgEN9SY9bdjYqV5tyXagKxQPjz1t9BdhScP0jlEMEV86jYFQ5UuE59t5%2FJ%2F56wOWP9w%2BUL%2Fo3oZYYVsqGVXIC9qi4mgLaI6RLXs7r%2B3THi0VUTWAkWcsHBM7EE%2B0ErGRX%2F2hZRZww0c6EbWO4W7uOeOThkXwu15ryQZYPxkBXOCtBRSUsHlUoPgbYuHTwhIwOJwUoT68DkyIqmSOhO%2FkDPx6vQviQHL3&X-Amz-Signature=6e21aa6ebad3147642870b23d8d167491eb442345497a1fc546c5890bb148df7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
