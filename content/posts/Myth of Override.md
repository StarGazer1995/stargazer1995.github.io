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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBNWPXQJ%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T185412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSd6LcYI7MUuRnoFpnNLyrHI89udGU1OYz4DwYIkpVGAiBbHEhMfK3Q8KCMnJOPaChK54v1FhptE5nM%2BBNeQg1JoCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML7cHRAGbgXtvCWaQKtwD4XkUQFMlfcGODbaZ%2BY32fTQkNpKqWPfsfX%2F%2FfrJUrZqX6Pj9TVl%2B0vmJolPXfemGyf0WMacy80CKHR9%2B3t0KD8VOHvF6xH%2BpTW6HHpTzAU4fyEubYFV%2BWi0ezAxXnj0XMvhhPzvnKxUAU5d%2Bidpo63J6fQ1%2BCRz3SgqOeFTHiU2knkRkwMELiMLKFsqdhBC6u%2FpDKewdhqI49kyZwsBpVWi8BHRKrRh3ME0ivrsO6U%2BFQynNH4SM5ZonEussdmVWXzYfmwmHfsFPY3b2T8iG1h4v4PZhopV%2F%2FuCTYVD%2BiJCfI0MPaFJHv8mHE5s3s4IOSgaxI9E815qx21yMjPY2B0s20xiMW7bAm81xo1SFhI%2FOGKacJbEyYsBjvMqvK3GV7JTDS3bQPggr49BAWMvTbvyS86EE2ZVWNsNdZ8UZ1cjsFP9AmqmYFbnw4%2FSG%2FgF6pNiGuJ9izR3pq%2BUQKysnotZo2VpXmT4Xp%2B3fgU8Date33W8cQ0qG7MqF%2Bmy%2FVj7LP62BRrBB9U5tWsu0fZ7S3upG%2FObEG4%2FOSnXiAzYR1KXVXjsgp9%2Fr6a1XH51ITVBKXazWsnlJ8ryOYE3Gux0LLvzg5vn4%2F3eDqeVu7V3owXEdvCFTxUu6RHTbqA8w9Ljo0wY6pgGZUslePadrRcb6infirkD%2Fueys2BVHt5teTE85cs0M2Wv%2BtX0fabukeflXeTgbe%2BqIh53N7fuqsRSLsVBOcy7zU%2BUe0AuBVn2kvc3DA4sCn7%2Fzia9K%2B2rsIc38z%2BWQWfx%2Fjwjz6JfIScP%2BB%2F0EV601lhDJdQ89Aod5vo9wpP37bdWB7CYinLlUWaC0efRg1lTdLQHD7E%2FRA9w8k7nmQVwYYhpKuDVY&X-Amz-Signature=fc12e91250819177308b9ee7b8372added1c5254efa3b7a9a93371a2b5031b2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBNWPXQJ%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T185412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSd6LcYI7MUuRnoFpnNLyrHI89udGU1OYz4DwYIkpVGAiBbHEhMfK3Q8KCMnJOPaChK54v1FhptE5nM%2BBNeQg1JoCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML7cHRAGbgXtvCWaQKtwD4XkUQFMlfcGODbaZ%2BY32fTQkNpKqWPfsfX%2F%2FfrJUrZqX6Pj9TVl%2B0vmJolPXfemGyf0WMacy80CKHR9%2B3t0KD8VOHvF6xH%2BpTW6HHpTzAU4fyEubYFV%2BWi0ezAxXnj0XMvhhPzvnKxUAU5d%2Bidpo63J6fQ1%2BCRz3SgqOeFTHiU2knkRkwMELiMLKFsqdhBC6u%2FpDKewdhqI49kyZwsBpVWi8BHRKrRh3ME0ivrsO6U%2BFQynNH4SM5ZonEussdmVWXzYfmwmHfsFPY3b2T8iG1h4v4PZhopV%2F%2FuCTYVD%2BiJCfI0MPaFJHv8mHE5s3s4IOSgaxI9E815qx21yMjPY2B0s20xiMW7bAm81xo1SFhI%2FOGKacJbEyYsBjvMqvK3GV7JTDS3bQPggr49BAWMvTbvyS86EE2ZVWNsNdZ8UZ1cjsFP9AmqmYFbnw4%2FSG%2FgF6pNiGuJ9izR3pq%2BUQKysnotZo2VpXmT4Xp%2B3fgU8Date33W8cQ0qG7MqF%2Bmy%2FVj7LP62BRrBB9U5tWsu0fZ7S3upG%2FObEG4%2FOSnXiAzYR1KXVXjsgp9%2Fr6a1XH51ITVBKXazWsnlJ8ryOYE3Gux0LLvzg5vn4%2F3eDqeVu7V3owXEdvCFTxUu6RHTbqA8w9Ljo0wY6pgGZUslePadrRcb6infirkD%2Fueys2BVHt5teTE85cs0M2Wv%2BtX0fabukeflXeTgbe%2BqIh53N7fuqsRSLsVBOcy7zU%2BUe0AuBVn2kvc3DA4sCn7%2Fzia9K%2B2rsIc38z%2BWQWfx%2Fjwjz6JfIScP%2BB%2F0EV601lhDJdQ89Aod5vo9wpP37bdWB7CYinLlUWaC0efRg1lTdLQHD7E%2FRA9w8k7nmQVwYYhpKuDVY&X-Amz-Signature=f3ddab597c09c147bfcc49c65d8829c02228afa355e063fb1821e9ac53df433a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
