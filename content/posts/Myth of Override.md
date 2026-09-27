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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQDMQACB%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T093724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQDLxK28MzFiAZBr7JvqTyCUtWVJ7OSbEVHV%2BuqQ9p%2BmfwIgGsxhweZul41JHZ4JxU%2Fo%2F8FXwmur7XWbEn8dTX0AC%2BUq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDNZ4bW9M95jXE8H3jSrcA6WkBqkTNr6Iv9H%2BKu3w%2BFzzo0mQVPmvWfh%2BgXrZWZ4wfpKvToP%2B785RYkdS4%2BYT8a%2FwyvpWmJ2TQQLazugoRItsN%2Fa8pE9jYIYfT%2B0fEXL3Sjamc1DVd0yqZbNhffs0MQoGkmWQe2iLlJAgkkaPKz%2BZmHDaKvATP7uxfOXN7g39KtXYVfqa4OtkOzqPBqpxaP1BLtbz2oGL7vP1vesOncTASZl7dDNJHlzk0pk9bKHDYgJnIzf5dDnah2mfF2Vsn3a9dBAkLZrTpHvBcIy5trmox7bK5PJfbrYfgkb4ZX33vzzemO7YS0vjuomjJed3%2BoUCyRO3RksEAGXZqdrc82f5ofA1NtADiEB4UzbqKvgfW5eQjcTjnQPSlnEToDRAyRVfIfzzjypIlt053M1sHzoIgOFu%2FGbytiNxnVUK5Zn6lnEiPGvRUKewQ24t0TUCn4zs0zO9xSulukaoLkNJFGxw4btGgii9iUtwsAKotM8iDumzTIK2fR8HbDubB6yEJBaorEQhX24W9ZElaku9JGi7Z8AVFyD7ZLfwwzQzvMYgJDvUXsTLqU%2FdjgedXQ%2BWeSpcc8Pf%2Fxzx7rPtJklC7781neTluzuyrk4qzCOYNVlqzVNmr%2F%2B6FQVvqEdMMM6s49UGOqUBPPlOTwLvHMjzXj7wHd94iiu2UbcJkQnpDT%2B5Y%2BC%2BiKIJYSnJOdcM5aKu1a%2FlWbb0YTKzdPYxLn1%2BPRQycA14qr3exuGl3m3IY%2F%2BDe6u3tbUh%2BjVJDc6DlxmYQ%2BFhy5NOTZkbMiV0rCywNvvSDxl154Qip5i2gkSjqCqFJ7dCsd4WSEcNE24WuU9S0YS9BGQ1zC5ib45jAdoell%2Ft3qiK%2B7ZxoMrk&X-Amz-Signature=7447e3f802003f7651773fac1c673245b8cc41a29feb58bb37023825f390396a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQDMQACB%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T093724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQDLxK28MzFiAZBr7JvqTyCUtWVJ7OSbEVHV%2BuqQ9p%2BmfwIgGsxhweZul41JHZ4JxU%2Fo%2F8FXwmur7XWbEn8dTX0AC%2BUq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDNZ4bW9M95jXE8H3jSrcA6WkBqkTNr6Iv9H%2BKu3w%2BFzzo0mQVPmvWfh%2BgXrZWZ4wfpKvToP%2B785RYkdS4%2BYT8a%2FwyvpWmJ2TQQLazugoRItsN%2Fa8pE9jYIYfT%2B0fEXL3Sjamc1DVd0yqZbNhffs0MQoGkmWQe2iLlJAgkkaPKz%2BZmHDaKvATP7uxfOXN7g39KtXYVfqa4OtkOzqPBqpxaP1BLtbz2oGL7vP1vesOncTASZl7dDNJHlzk0pk9bKHDYgJnIzf5dDnah2mfF2Vsn3a9dBAkLZrTpHvBcIy5trmox7bK5PJfbrYfgkb4ZX33vzzemO7YS0vjuomjJed3%2BoUCyRO3RksEAGXZqdrc82f5ofA1NtADiEB4UzbqKvgfW5eQjcTjnQPSlnEToDRAyRVfIfzzjypIlt053M1sHzoIgOFu%2FGbytiNxnVUK5Zn6lnEiPGvRUKewQ24t0TUCn4zs0zO9xSulukaoLkNJFGxw4btGgii9iUtwsAKotM8iDumzTIK2fR8HbDubB6yEJBaorEQhX24W9ZElaku9JGi7Z8AVFyD7ZLfwwzQzvMYgJDvUXsTLqU%2FdjgedXQ%2BWeSpcc8Pf%2Fxzx7rPtJklC7781neTluzuyrk4qzCOYNVlqzVNmr%2F%2B6FQVvqEdMMM6s49UGOqUBPPlOTwLvHMjzXj7wHd94iiu2UbcJkQnpDT%2B5Y%2BC%2BiKIJYSnJOdcM5aKu1a%2FlWbb0YTKzdPYxLn1%2BPRQycA14qr3exuGl3m3IY%2F%2BDe6u3tbUh%2BjVJDc6DlxmYQ%2BFhy5NOTZkbMiV0rCywNvvSDxl154Qip5i2gkSjqCqFJ7dCsd4WSEcNE24WuU9S0YS9BGQ1zC5ib45jAdoell%2Ft3qiK%2B7ZxoMrk&X-Amz-Signature=371df70c9a7b64440410b23ff1e1facae26b276031bbe22f71a901cfc66d6c48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
