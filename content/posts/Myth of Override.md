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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FD7TBDP%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T122524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCo4yV7UiEBnuisBNaLtaefF8itnvjY1gL69woiFIBewgIgQ3DgtH6461kQN1LaLbKrHR%2Fr6zNEtnd47J3G0lzbL%2FcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL9zOny9fSIdK5I6LircA49HL%2BaGc1w6wHl54voXeytBrH52y1gz41ZQF4HjFl0C3x4m%2B6Y7dcE%2FRawgZdkz323OXEiAtKptbUTmV2yn8IEHdy7%2B129ISkGejqIZSArXHjRl0oL7nQUYKwt7UreT9VO7YREgvK2kLUmjgBDVL4cqbNchyLI2J24CHU6ukQvun8NtbdnQrx6fjl3ZfsNNNuBxUTfAA3m%2FJoOGMTcdGOeWJJqsVMf3EMV8K4nFHTyM8BXxkJ%2FzGjxowtCkdSfI6E2qoitdahKsCrVYDRUg4vcYOOK%2BIA9QVzV3BxD7Aj2SH%2FbCbfPA21i38XnxONJVs5Kttdb5scxpsx7ENcuLLZfbXc%2BLr0tIuceIz1bEF8Nl4LN2WkDVj2C%2BBqopt5zqirCzrHYPnWU0YglG6rTEVwzVqQUPg3KgocODgQJz4iL0%2BxXEXrX8PCm80KJDgfJqYGhW7JvWoq798F%2BYNisrh%2FOfHGvlh%2FNFPg2UXrBRs8tRcKUBq%2B14Tz6vxaCMXVPtD%2BdmviY56SB8Lsd%2FkKH1edRzv7w51Gauqp1xvzjXnRTEOb8OA2LIbWNrD66tYYpBghX4erG4FDIr43xIHxqk5Juok4Q%2F90b1Nc7iXbmr8%2FKzXej9h65GVvnbgVvMMNK6j9UGOqUB2fJw0sFyvjyY%2BKlCWFrrJpk%2Bg473mIhlGtX6WL0uJcyEc%2Bt7kEZjtkivUkow8MhqsMA9fePQeUrnmF9EkZ6Fbf0AId%2FRUBX2TJo4pgEQOuPDz87IyHc30imEC77FrWi4oNvq0JJakwSNHUgEKYnTER1bLGU9tIfM58A8yeR0rMaEpKp2Jp5scCVjXa0C%2B9C6crBB1Fkb8QqS6VLUUqre%2BX0VZ%2BrJ&X-Amz-Signature=b7343287b14e4132ac58dae9c6e0faed22376ce205c4e6b9d6fa7f3a4c53dda8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FD7TBDP%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T122524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCo4yV7UiEBnuisBNaLtaefF8itnvjY1gL69woiFIBewgIgQ3DgtH6461kQN1LaLbKrHR%2Fr6zNEtnd47J3G0lzbL%2FcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL9zOny9fSIdK5I6LircA49HL%2BaGc1w6wHl54voXeytBrH52y1gz41ZQF4HjFl0C3x4m%2B6Y7dcE%2FRawgZdkz323OXEiAtKptbUTmV2yn8IEHdy7%2B129ISkGejqIZSArXHjRl0oL7nQUYKwt7UreT9VO7YREgvK2kLUmjgBDVL4cqbNchyLI2J24CHU6ukQvun8NtbdnQrx6fjl3ZfsNNNuBxUTfAA3m%2FJoOGMTcdGOeWJJqsVMf3EMV8K4nFHTyM8BXxkJ%2FzGjxowtCkdSfI6E2qoitdahKsCrVYDRUg4vcYOOK%2BIA9QVzV3BxD7Aj2SH%2FbCbfPA21i38XnxONJVs5Kttdb5scxpsx7ENcuLLZfbXc%2BLr0tIuceIz1bEF8Nl4LN2WkDVj2C%2BBqopt5zqirCzrHYPnWU0YglG6rTEVwzVqQUPg3KgocODgQJz4iL0%2BxXEXrX8PCm80KJDgfJqYGhW7JvWoq798F%2BYNisrh%2FOfHGvlh%2FNFPg2UXrBRs8tRcKUBq%2B14Tz6vxaCMXVPtD%2BdmviY56SB8Lsd%2FkKH1edRzv7w51Gauqp1xvzjXnRTEOb8OA2LIbWNrD66tYYpBghX4erG4FDIr43xIHxqk5Juok4Q%2F90b1Nc7iXbmr8%2FKzXej9h65GVvnbgVvMMNK6j9UGOqUB2fJw0sFyvjyY%2BKlCWFrrJpk%2Bg473mIhlGtX6WL0uJcyEc%2Bt7kEZjtkivUkow8MhqsMA9fePQeUrnmF9EkZ6Fbf0AId%2FRUBX2TJo4pgEQOuPDz87IyHc30imEC77FrWi4oNvq0JJakwSNHUgEKYnTER1bLGU9tIfM58A8yeR0rMaEpKp2Jp5scCVjXa0C%2B9C6crBB1Fkb8QqS6VLUUqre%2BX0VZ%2BrJ&X-Amz-Signature=1763cb612ef0ed50a8e6324dd9612a1daf2c0630a13937211a06e4b9d4a35187&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
