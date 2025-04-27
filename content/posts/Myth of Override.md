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

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">code_examples/cpp_examples/01_myth_of_override/src/main.cpp at main · StarGazer1995/code_examples</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;">Contribute to StarGazer1995/code_examples development by creating an account on GitHub.</div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://github.githubassets.com/favicons/favicon.svg"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div><div style="flex: 1 1 180px; display: block; position: relative;"><div style="position: absolute; inset: 0px;"><div style="width: 100%; height: 100%;"><img src="https://opengraph.githubassets.com/24dae9f0ad65ae788f1f405a6204e98dbfd21a90718b49e4873c8a534314d035/StarGazer1995/code_examples" referrerpolicy="no-referrer" style="display: block; object-fit: cover; border-radius: 3px; width: 100%; height: 100%;"></div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6LF325P%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T064614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDo1klCl1J3rGttt7DHkWPDnIPnVq2539iDqoXFkP8McgIhANV3xFF7HPW793RmJfjKrkZPFHrA%2FwDLU2VINz6iH6iEKv8DCFYQABoMNjM3NDIzMTgzODA1IgwHimeufGJevd6tDDIq3AO09NMKBO44CBsjZ6QTvD9Lb1s4Q9MyGGs%2FJaLeIuAjJ43EmrzBmdhL9s9m1pSLsJOEzFPWN1%2Fyw5wPyU4yF4L8qReKtL671nYMTkHQ8XouOa%2F9CJBncTEPb6IfjmvfP32TBOUBqdU0PRR9yOHQiyNHdzKWOzt6f6c0OtZ0%2F6iJpIqrOpegGlpmET3KyWuFy7jZv618rJVW54y1A8ASWA2HnpfFZXlMO8sDhxt76oBgr90gY9vtTiSlNO5IZ5TtUgl1cWSw72SYDK23Wh00tvr2lii3KFRvKb5tJy%2F0ROCmgeqIuZQVac6%2BXogoUTX2BdHqeQEeTTPtKLmB0y4rcxiHfxTwTXCp8HY%2FObNlghsa3fnIOanxFud1d679xMVZ4QDYraWpfzqYUWI3Kycus%2BB6ifEjX03m0uFCqVolP0hT%2Bwn3PvNXf1au%2F5iFwzkOes68fDkoqrvsYvPXmzed%2FKedjmLk3Riaye1ELBwmsF%2FncwM8%2F90ONuqQ4XQavlHOs6k6x%2BVCzw77gRQdLlTMmMDD9z0jFwjboY9mQNg1n5isBF3gu8xE8vY%2FCS8yJ3%2FalX6%2Bg9xYpXoUoB5K7UZcbg0h3KddFPoFWaj24uXKH53jJifaJq18pXXM%2B4AMVzCS7bbABjqkAXo0OAZzq%2Fe%2BdrmNw7zFYlug8FcTBhZU9Q7zrEgcf5orPOJ1NL7I%2BsJnEA%2BI%2B%2BWW16IZK6FkolH2oayzeceBgG%2BXZi2UXE60%2FuJawQfLXa6G%2BB3fjXKrkxXcIBw7VA8AStKD%2FOLDdqKE3qwzu2IBw%2F0ovYRO29lc7rferj0oHoVFWCXgT6ktOfih413oSkWRXpcXADK9GpO7C5Vx6X1tJvyWuW73&X-Amz-Signature=7a6df237d7c91877d9d3beb7512c42f1a020484e06834efa77f877a30f645496&X-Amz-SignedHeaders=host&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6LF325P%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T064614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDo1klCl1J3rGttt7DHkWPDnIPnVq2539iDqoXFkP8McgIhANV3xFF7HPW793RmJfjKrkZPFHrA%2FwDLU2VINz6iH6iEKv8DCFYQABoMNjM3NDIzMTgzODA1IgwHimeufGJevd6tDDIq3AO09NMKBO44CBsjZ6QTvD9Lb1s4Q9MyGGs%2FJaLeIuAjJ43EmrzBmdhL9s9m1pSLsJOEzFPWN1%2Fyw5wPyU4yF4L8qReKtL671nYMTkHQ8XouOa%2F9CJBncTEPb6IfjmvfP32TBOUBqdU0PRR9yOHQiyNHdzKWOzt6f6c0OtZ0%2F6iJpIqrOpegGlpmET3KyWuFy7jZv618rJVW54y1A8ASWA2HnpfFZXlMO8sDhxt76oBgr90gY9vtTiSlNO5IZ5TtUgl1cWSw72SYDK23Wh00tvr2lii3KFRvKb5tJy%2F0ROCmgeqIuZQVac6%2BXogoUTX2BdHqeQEeTTPtKLmB0y4rcxiHfxTwTXCp8HY%2FObNlghsa3fnIOanxFud1d679xMVZ4QDYraWpfzqYUWI3Kycus%2BB6ifEjX03m0uFCqVolP0hT%2Bwn3PvNXf1au%2F5iFwzkOes68fDkoqrvsYvPXmzed%2FKedjmLk3Riaye1ELBwmsF%2FncwM8%2F90ONuqQ4XQavlHOs6k6x%2BVCzw77gRQdLlTMmMDD9z0jFwjboY9mQNg1n5isBF3gu8xE8vY%2FCS8yJ3%2FalX6%2Bg9xYpXoUoB5K7UZcbg0h3KddFPoFWaj24uXKH53jJifaJq18pXXM%2B4AMVzCS7bbABjqkAXo0OAZzq%2Fe%2BdrmNw7zFYlug8FcTBhZU9Q7zrEgcf5orPOJ1NL7I%2BsJnEA%2BI%2B%2BWW16IZK6FkolH2oayzeceBgG%2BXZi2UXE60%2FuJawQfLXa6G%2BB3fjXKrkxXcIBw7VA8AStKD%2FOLDdqKE3qwzu2IBw%2F0ovYRO29lc7rferj0oHoVFWCXgT6ktOfih413oSkWRXpcXADK9GpO7C5Vx6X1tJvyWuW73&X-Amz-Signature=9ce9d2f7421d40db9bd199561e7ef4fc548c346c8ced56f6c216cd4714f122c1&X-Amz-SignedHeaders=host&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">virtual function specifier - cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://en.cppreference.com/favicon.ico"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
