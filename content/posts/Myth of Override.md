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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZSXZUD6%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T162438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDuxWanXKe%2Bx%2FY1%2B4reWpS9VKPSTmYb4MGohQa9wcxvCgIhAM7smqDKicJIHQKJkffYiHh%2BgGphbK2RPgKJmQgeFTBkKv8DCBkQABoMNjM3NDIzMTgzODA1IgzSHYmaUCG%2FzZFxYhkq3AMUwjEjxBGeGw0M3Dm83EkhNlf3u3IyqH6MYd5B%2BG7HQpWj3bLtc51jdntGmFOR40xK3eKQdBU6hoY6uED8DViOByG08NFAkb4SStVa77maQGpnec8hZ89LtKmB31k6Y40BXFfSlCpKkfU%2BAJoyhbEgq8bk3zJD%2BZmv7GHEjPA%2B%2Bo4fwDoxSMb9FuOlGToE3z1CtFvQg5PfgfZu5I5MSvaSm0fHcbSkH%2BEzzl365qOYSwWo3sixqdHViL8IfyYtW0RyyOhecCThJ80kJ78uvgYs%2BAa54OEpewCtpAg21YsEPryviOAwZatSlfzf9wJ5DfJMQyjoYOLp5p1MeKPX3CkwlD2Cq1mM%2FaKy3yzgnx3rHd%2FhsEMYFNBCh7PITU%2BvDKXjcTKGMBWkjS82EJfrU4lA9PQRNhg7kDea7sWFkJJAAZASA0hCS%2F7F93lqkNZUpADemhr9%2FntWZopab3TgTZDXI%2BvpAeTdGxLR4mtEVrPdbJ%2B9U93n%2BTSXHQzEhRlkAPPKPw7qICoEyDzGluUJwoTrxi2gRL1bwtjc6lkMIu929a2TcVTC62crf%2Fp6AE3uFiD%2Br6FQL0EDLc%2FtEOcuMY9zBpQa1iMZHyfT9yextbuaEYye56F7ZmUuTPvZuDDE7YfQBjqkAQYSkBgv6IKkeoIXogBvmSbrEAs%2F5JJjua6VJYwY4uyOgMY7i%2BxsWksyiHenZK3ikwN5Wywe8Nt7oyEGEAxl0XJU9G4%2BVxzb3fc3NKhHY372u94SaBhFbr9Xs1zD5qsjTAJSvadCWuzN0eglE2Qr4B2OXCU3Lyxyc5PBMkIjjAJuQHxDRqodg758PPLkkoQshddwbFcwCu5ImVLbmAz%2F5Aaq1iT4&X-Amz-Signature=f394d3ec1e6db577f914c8dd222ac609c95e71b0fed7056cd18b7dcf8f27e95a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZSXZUD6%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T162438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDuxWanXKe%2Bx%2FY1%2B4reWpS9VKPSTmYb4MGohQa9wcxvCgIhAM7smqDKicJIHQKJkffYiHh%2BgGphbK2RPgKJmQgeFTBkKv8DCBkQABoMNjM3NDIzMTgzODA1IgzSHYmaUCG%2FzZFxYhkq3AMUwjEjxBGeGw0M3Dm83EkhNlf3u3IyqH6MYd5B%2BG7HQpWj3bLtc51jdntGmFOR40xK3eKQdBU6hoY6uED8DViOByG08NFAkb4SStVa77maQGpnec8hZ89LtKmB31k6Y40BXFfSlCpKkfU%2BAJoyhbEgq8bk3zJD%2BZmv7GHEjPA%2B%2Bo4fwDoxSMb9FuOlGToE3z1CtFvQg5PfgfZu5I5MSvaSm0fHcbSkH%2BEzzl365qOYSwWo3sixqdHViL8IfyYtW0RyyOhecCThJ80kJ78uvgYs%2BAa54OEpewCtpAg21YsEPryviOAwZatSlfzf9wJ5DfJMQyjoYOLp5p1MeKPX3CkwlD2Cq1mM%2FaKy3yzgnx3rHd%2FhsEMYFNBCh7PITU%2BvDKXjcTKGMBWkjS82EJfrU4lA9PQRNhg7kDea7sWFkJJAAZASA0hCS%2F7F93lqkNZUpADemhr9%2FntWZopab3TgTZDXI%2BvpAeTdGxLR4mtEVrPdbJ%2B9U93n%2BTSXHQzEhRlkAPPKPw7qICoEyDzGluUJwoTrxi2gRL1bwtjc6lkMIu929a2TcVTC62crf%2Fp6AE3uFiD%2Br6FQL0EDLc%2FtEOcuMY9zBpQa1iMZHyfT9yextbuaEYye56F7ZmUuTPvZuDDE7YfQBjqkAQYSkBgv6IKkeoIXogBvmSbrEAs%2F5JJjua6VJYwY4uyOgMY7i%2BxsWksyiHenZK3ikwN5Wywe8Nt7oyEGEAxl0XJU9G4%2BVxzb3fc3NKhHY372u94SaBhFbr9Xs1zD5qsjTAJSvadCWuzN0eglE2Qr4B2OXCU3Lyxyc5PBMkIjjAJuQHxDRqodg758PPLkkoQshddwbFcwCu5ImVLbmAz%2F5Aaq1iT4&X-Amz-Signature=c4a642e72b7c7d0c2bf809a837819275194c0b0c6aa36fa2611cd5513af1db63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
