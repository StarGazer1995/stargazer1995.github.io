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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4DF6FQ%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T045653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDeKBaSEg216aQXQm%2FNrgqfrPGOcOAZW1YLhqxKGnL5lAIgBhCHbTQomcAy0YRKPoReY%2Bvu9FhbsDUSCWQdm5o008gqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMpv4f8wCs023HqxvSrcA%2BmMRfP%2FrrVUkz3yeX2l0586iPsCt3E5gKSVi3TzvzefdHwNnD9PKSY8UH4UFTgly8v87g8ZoHKCZlN7sDrvA%2FYzEqOcha9CUupbOtEKv43kohq2Q64zWIQMKnOowhAK16S5gooicPOYDRVhD6SprsjEHre%2FwjMCP5nXEQ5xXZJFHr5VHtKAsK82ZkZ4lrmNqRteMCHf162BGHLEJL9cUH7o8JE3cd8QoVC%2Feae76b5zad2zjxHo85WJ2nFWtZVEKsmTjGKLiMu9SQP99gWKVUMou8bzlIQ4V0LgozGM0eqHTAsxhchwldIglBdbcP1vwh88St71BL%2B1CN9TYsDhsNl5G78HrXN8o62cgoPLWIJeoGPv14qbuObl85feit4fgk76WG6k9gPiEJSGuC9BNF0UlrGnVL9WNLrrtfWpJUDwLYLkc7gtDs0QLmSKFp%2BskKcboen%2BY1LWbiLqVd0X0hFsNNUUbtYYgdAu2jjl8HJYif2dIj23pSWWRMu4x6ovQK%2BZ2UEW6Ksg5IC5jK%2FeMJp5RM%2BH%2B5ioxyoYVmiByFrCWMvrlRg1abO25YuC8yLc7M0Y3AiDTs5CA41Jm%2FYIYronE1earGvjyDJShJLFZ6%2Bkuu8O%2BVO4hHT8H9gfMO78gNMGOqUBNLbZsL4Uc2kksc1g60x67J0ME%2BtGTS2qeHcDwEDB2T065uxhoGMGjlUsSf%2FatEGEL0dbBRX9hJKllG1iUA6sAkQzmXCzS07ilo3CE7dMZ0glW7TkU3jao8lfYZV7jZ%2BjNrE%2BBtrDIwU8%2FIsflbAQkL%2BguKES0kmtLYmt1TJyNrR6nBg75HzbJsuXlSc373pqTWVzul4lpYoDjh6Olla%2F0qCk5be2&X-Amz-Signature=42b26792bef81002027006337aea396b4c0d711bf787bfefb3fd60973a76cbd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4DF6FQ%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T045653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDeKBaSEg216aQXQm%2FNrgqfrPGOcOAZW1YLhqxKGnL5lAIgBhCHbTQomcAy0YRKPoReY%2Bvu9FhbsDUSCWQdm5o008gqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMpv4f8wCs023HqxvSrcA%2BmMRfP%2FrrVUkz3yeX2l0586iPsCt3E5gKSVi3TzvzefdHwNnD9PKSY8UH4UFTgly8v87g8ZoHKCZlN7sDrvA%2FYzEqOcha9CUupbOtEKv43kohq2Q64zWIQMKnOowhAK16S5gooicPOYDRVhD6SprsjEHre%2FwjMCP5nXEQ5xXZJFHr5VHtKAsK82ZkZ4lrmNqRteMCHf162BGHLEJL9cUH7o8JE3cd8QoVC%2Feae76b5zad2zjxHo85WJ2nFWtZVEKsmTjGKLiMu9SQP99gWKVUMou8bzlIQ4V0LgozGM0eqHTAsxhchwldIglBdbcP1vwh88St71BL%2B1CN9TYsDhsNl5G78HrXN8o62cgoPLWIJeoGPv14qbuObl85feit4fgk76WG6k9gPiEJSGuC9BNF0UlrGnVL9WNLrrtfWpJUDwLYLkc7gtDs0QLmSKFp%2BskKcboen%2BY1LWbiLqVd0X0hFsNNUUbtYYgdAu2jjl8HJYif2dIj23pSWWRMu4x6ovQK%2BZ2UEW6Ksg5IC5jK%2FeMJp5RM%2BH%2B5ioxyoYVmiByFrCWMvrlRg1abO25YuC8yLc7M0Y3AiDTs5CA41Jm%2FYIYronE1earGvjyDJShJLFZ6%2Bkuu8O%2BVO4hHT8H9gfMO78gNMGOqUBNLbZsL4Uc2kksc1g60x67J0ME%2BtGTS2qeHcDwEDB2T065uxhoGMGjlUsSf%2FatEGEL0dbBRX9hJKllG1iUA6sAkQzmXCzS07ilo3CE7dMZ0glW7TkU3jao8lfYZV7jZ%2BjNrE%2BBtrDIwU8%2FIsflbAQkL%2BguKES0kmtLYmt1TJyNrR6nBg75HzbJsuXlSc373pqTWVzul4lpYoDjh6Olla%2F0qCk5be2&X-Amz-Signature=e76b63249013d92c2ba1c8ce87c7bfea0f8c360ccf4d7da2181e75dd69997248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
