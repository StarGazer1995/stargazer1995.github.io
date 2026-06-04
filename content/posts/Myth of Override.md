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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663BIWNSM%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T195335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGBgK0kzBGMPHBKx8UaUNWPec4X8x2ziJRMQdQGtr09AAiEAioTWi4KC5zUpBqTU0c84ZpgmhKMHSYcimtXixO3sVC4q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDIIYimnSfo7q2qCWTSrcA4GdCCPFHR0cZJRS%2FPBduK3ZiWhvg0udf5CdTvOiIB3TiQNmWOYwCCPTcQuFStZvLyP1XFy3PYA4rqPF3ao%2Fw0kFTc5ZfUAIoxeVJeNp3HE5Z5h8SmNxKx5P29fA%2FoK5JuqH%2Fi%2BA7r%2Fo4NUmhxNrJ6gXiA7gtHghTV7bOZqtdgl3QvXwbBP0X%2FFRYlbIL9aO0Pt4f9hwnwz1uT%2BbjUNZbmFqsmtBXvnslWZbDDx0Nj9%2BJ56Gmf9YVQPg8T%2FKmbHpm2GEKbhtQzGYtqVVAlimspYZOs5I39bA%2FCjop8tKDORMJ5ONHGujeuOUBYsmKli%2BrIV24KsBGG7D%2BswlKeMwyBL9jtUYi59%2F%2FEkcdJtY2KgfSxOkZNfXVi%2BeWqwWZZPY3tzP594Ya9QUG6Sv7RR1GYy217%2Bc295OqEkAGt%2BqWy1u69obTneSBpGuQe3VBmbrYyZStuROGplSYFffvcnrpNh1qfvgAOOVfCzdiG6RUQZ7IhkpKelYTxLcMmQiqQisbyaPWV%2FGUgey8U0GFljWnoCr8Y0zj7vzEOKVCzQjlkh4khz3TkE8F6dXiAjG5oRr9ienz%2BxLiUk559mtF1XamJArIS7CEOOX5fqR%2BIiNcYG6JRDM0ey0JGlnxRUyMPCohtEGOqUBtBiHhOtvinYpAq8d77X20JJdt3Ti426Q87pjsHF8P2P6hr2G3Q7COd%2Bcrr5v%2Fn0VlSbU6YAjfH5XUdipMyrJ96heZmPyFK%2BBIYwSQcremsvtJPYda9eSj%2Ff1TAuQP%2FMnmMUQ5iQwfQlsJu3LfBHj4WgrBE29wnm9jTuEaksa6OpZ%2BGLApjzP1RZfGHd%2B8YiUM3PClcxTdqZ8Sa2Sb7ho84TJrG1r&X-Amz-Signature=52b0b443cd494803186edcce2eada9e0abb870ddca23d719794b1fd2be623ac6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663BIWNSM%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T195335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGBgK0kzBGMPHBKx8UaUNWPec4X8x2ziJRMQdQGtr09AAiEAioTWi4KC5zUpBqTU0c84ZpgmhKMHSYcimtXixO3sVC4q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDIIYimnSfo7q2qCWTSrcA4GdCCPFHR0cZJRS%2FPBduK3ZiWhvg0udf5CdTvOiIB3TiQNmWOYwCCPTcQuFStZvLyP1XFy3PYA4rqPF3ao%2Fw0kFTc5ZfUAIoxeVJeNp3HE5Z5h8SmNxKx5P29fA%2FoK5JuqH%2Fi%2BA7r%2Fo4NUmhxNrJ6gXiA7gtHghTV7bOZqtdgl3QvXwbBP0X%2FFRYlbIL9aO0Pt4f9hwnwz1uT%2BbjUNZbmFqsmtBXvnslWZbDDx0Nj9%2BJ56Gmf9YVQPg8T%2FKmbHpm2GEKbhtQzGYtqVVAlimspYZOs5I39bA%2FCjop8tKDORMJ5ONHGujeuOUBYsmKli%2BrIV24KsBGG7D%2BswlKeMwyBL9jtUYi59%2F%2FEkcdJtY2KgfSxOkZNfXVi%2BeWqwWZZPY3tzP594Ya9QUG6Sv7RR1GYy217%2Bc295OqEkAGt%2BqWy1u69obTneSBpGuQe3VBmbrYyZStuROGplSYFffvcnrpNh1qfvgAOOVfCzdiG6RUQZ7IhkpKelYTxLcMmQiqQisbyaPWV%2FGUgey8U0GFljWnoCr8Y0zj7vzEOKVCzQjlkh4khz3TkE8F6dXiAjG5oRr9ienz%2BxLiUk559mtF1XamJArIS7CEOOX5fqR%2BIiNcYG6JRDM0ey0JGlnxRUyMPCohtEGOqUBtBiHhOtvinYpAq8d77X20JJdt3Ti426Q87pjsHF8P2P6hr2G3Q7COd%2Bcrr5v%2Fn0VlSbU6YAjfH5XUdipMyrJ96heZmPyFK%2BBIYwSQcremsvtJPYda9eSj%2Ff1TAuQP%2FMnmMUQ5iQwfQlsJu3LfBHj4WgrBE29wnm9jTuEaksa6OpZ%2BGLApjzP1RZfGHd%2B8YiUM3PClcxTdqZ8Sa2Sb7ho84TJrG1r&X-Amz-Signature=205c9d6a78fe4d47e5bace8ccaf1fedf255fbef17aa21c880ddad3b4a90ad2ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
