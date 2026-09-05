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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OLTH4LH%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T062617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFizNB38afJCwtVvah50eHpD27KD5EaanfEsw7NQRLI7AiBmOHavcuTCz3jeDXB5cvMrQiChj%2FJoc09V1JtzX9J4USr%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMD4aJW4TmyxXj9RY0KtwD4qiWBgbZEtYq6FE5c9H4r67YdGYcwQX%2FK3L8PTSIx73W9BNXMU9%2B%2BD2H3elxmayLCNYB9upGDq07MdOtZe4GsJcQv9zJ%2BZtqzTeLqtijkL0z7FL7OQSq1BV7IWoAMcWWXU1eDgkVnVAMULp%2BK%2BnNq3KJz8rtoXHKy8kHiOUeE5Xhp4yIvngBdpFy6Cvfr6Dd44f6%2B4sYkCz8oK3QJojhv7pC5XJL92wScS%2B5iCW%2B2FW5mj0lAZk7xqDHJoQwKSDl4%2FdKnE6o6Q4jyAqQoyBcntUoz1vbY71WMLa3YXEKKgbpVnFlyfPR70APOhajHOw6Z3YUlWe9cXs%2Fnud9FiIqJ%2BWj0b0YZZV5OBjntNzCSCOVAO35pCgfeWYQKjBluuWxhELfEIaNRFpkaBi4ZjAK2KCxAsjuKCrDLTU5hhCzJ%2B0kSX0jhU8NISPOwU7QDAVFMeXA%2FIvvqDx%2BvQkIzrrcLTIkg3MBUqDVo5K%2FpJ9wYa8No5CIpci6m%2BOM%2FAGjo30HCbKWcgxpMG52BMFiFXyaBo9BiEn0TZKMEadVLS%2B3OBLKXb2kzj3V7dhaX%2FytKFspplErETKf%2F%2FDmoQBmmmnszE0HNqS80IjrqFeeS36r5%2FZPe%2BHrNEFKXD9NdwAw4Lnu1AY6pgErYiVRBqMVZGtc%2Fa0oYdliLYf%2FkWj%2BlHL4EV37isdr5xOUMrzxlTMZ%2FSgpcE%2BOMNHUV%2B0QliFb19DSWZ18srkzHzWv4pX7BvdIytK9HGBY4u7tTzc9K3lWJAMHDLna9NLzDZsPn0cUyPeKQJNgoNbBwOJxBlubK7lGa2%2F9OuL3H2OG1faujK%2FL%2BZxa8J5Mi3yoPazf0mtFkgJDN%2Bo6iEe31fUxuLqy&X-Amz-Signature=c16bcfc803f525656702b1bcbecb0d460e4f52af46abc7d5ac556e553eb8f5da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OLTH4LH%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T062617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIFizNB38afJCwtVvah50eHpD27KD5EaanfEsw7NQRLI7AiBmOHavcuTCz3jeDXB5cvMrQiChj%2FJoc09V1JtzX9J4USr%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMD4aJW4TmyxXj9RY0KtwD4qiWBgbZEtYq6FE5c9H4r67YdGYcwQX%2FK3L8PTSIx73W9BNXMU9%2B%2BD2H3elxmayLCNYB9upGDq07MdOtZe4GsJcQv9zJ%2BZtqzTeLqtijkL0z7FL7OQSq1BV7IWoAMcWWXU1eDgkVnVAMULp%2BK%2BnNq3KJz8rtoXHKy8kHiOUeE5Xhp4yIvngBdpFy6Cvfr6Dd44f6%2B4sYkCz8oK3QJojhv7pC5XJL92wScS%2B5iCW%2B2FW5mj0lAZk7xqDHJoQwKSDl4%2FdKnE6o6Q4jyAqQoyBcntUoz1vbY71WMLa3YXEKKgbpVnFlyfPR70APOhajHOw6Z3YUlWe9cXs%2Fnud9FiIqJ%2BWj0b0YZZV5OBjntNzCSCOVAO35pCgfeWYQKjBluuWxhELfEIaNRFpkaBi4ZjAK2KCxAsjuKCrDLTU5hhCzJ%2B0kSX0jhU8NISPOwU7QDAVFMeXA%2FIvvqDx%2BvQkIzrrcLTIkg3MBUqDVo5K%2FpJ9wYa8No5CIpci6m%2BOM%2FAGjo30HCbKWcgxpMG52BMFiFXyaBo9BiEn0TZKMEadVLS%2B3OBLKXb2kzj3V7dhaX%2FytKFspplErETKf%2F%2FDmoQBmmmnszE0HNqS80IjrqFeeS36r5%2FZPe%2BHrNEFKXD9NdwAw4Lnu1AY6pgErYiVRBqMVZGtc%2Fa0oYdliLYf%2FkWj%2BlHL4EV37isdr5xOUMrzxlTMZ%2FSgpcE%2BOMNHUV%2B0QliFb19DSWZ18srkzHzWv4pX7BvdIytK9HGBY4u7tTzc9K3lWJAMHDLna9NLzDZsPn0cUyPeKQJNgoNbBwOJxBlubK7lGa2%2F9OuL3H2OG1faujK%2FL%2BZxa8J5Mi3yoPazf0mtFkgJDN%2Bo6iEe31fUxuLqy&X-Amz-Signature=38d76f0e683d4b15259e716c4e884d208870ba6757f24ca9ae6c872efe1a74f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
