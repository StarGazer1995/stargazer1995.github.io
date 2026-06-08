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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VXXAUMY%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T023004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6wNNDN8%2BIJ0Yuk9%2BKG3ZoN9Kz9QSu%2BNvW%2FeGVvas6gQIhAN3iz0hxy3YUzSQtccFoYHsqOopunng2eaHJFEfwuH8hKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKBZmrrOvlVziu3cwq3AMJCpE2cMo04%2F1RS0%2BWiK7ItUyctpzELqGNkUG%2Bu7mfzXaHd%2FM4jBpcnicJYm1dJhhAduOSxZAAFUnf%2F6OoeiMrQyzOL5B%2F%2FevPEK3wBauDW1mt4y%2FaQxe9LQmEpImivDr%2FWcxsgXjD6gb43V%2F%2Bw8jwsz3aVOM844tocBdQ3eKWK6FJB94uW668Wc3uJA2SwUxxew0hnqGn5Z9PuhUB9otqJQgxsZo%2FF96e27KWkaIOJw6f5CNFI1pp5ri5efYwcLg1LXmieOF7EjILK4btpg80d7zlUZx0ID21HVan2hXeipNAlKMv9k5%2BsKrf%2BI7PwA%2FjwPipFaK2rvP6psN4JHR1cvF1HDmwr3GGCXcQUmjgN5nvXuXAeR4uw6Rz47pI7FeLfDq52fTRINZ%2FCfzsAD8Jj8%2FIqhJkHHal6pbtHVc2zdjsfYwStbPGSkA%2FuksiE%2B8Gk70npqwzU%2BJeeeHcTJKIfnUigLPOmR9Yi%2Bsf8lg9gFupf9O%2BDEjhxNjXyFsWR%2B2G8wFvE3k5v4ovtRR6xmT7ITUemYDMmsmllfRkLGjFWgN605A8%2F7zYNpSpG9Ku5OqMJ3qGthJ8gyOUYNJCE1E%2BClv9KELXTuBOBU5lk6Vg3VBzEOrUPwDnZZoXzDDnv5jRBjqkAZg7H72i7n79QqBe7m8CbXF8sGcfmPHK1nmowJuzFgY3f6FymIE2UPaeIxYWaJ61emZKCLiO8BTvaVo1h%2BDqMX75SZi829doKqbwrqCnxb0ZK%2BSjSitmELgwvJorii3Tgrj7pYz5x0f2bf6zkNGXehdd%2F%2FbVAVD0md7%2BwiWt0N1U1SrkUgssPjG1vmTt7a%2F%2B2Olm3uNLOSJ07JYrlRK7au7z%2FCNi&X-Amz-Signature=9133e0b5ba33ededf6b595403e67c45c3da9c7cf15921c2f1219792e5ba11f9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VXXAUMY%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T023004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6wNNDN8%2BIJ0Yuk9%2BKG3ZoN9Kz9QSu%2BNvW%2FeGVvas6gQIhAN3iz0hxy3YUzSQtccFoYHsqOopunng2eaHJFEfwuH8hKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKBZmrrOvlVziu3cwq3AMJCpE2cMo04%2F1RS0%2BWiK7ItUyctpzELqGNkUG%2Bu7mfzXaHd%2FM4jBpcnicJYm1dJhhAduOSxZAAFUnf%2F6OoeiMrQyzOL5B%2F%2FevPEK3wBauDW1mt4y%2FaQxe9LQmEpImivDr%2FWcxsgXjD6gb43V%2F%2Bw8jwsz3aVOM844tocBdQ3eKWK6FJB94uW668Wc3uJA2SwUxxew0hnqGn5Z9PuhUB9otqJQgxsZo%2FF96e27KWkaIOJw6f5CNFI1pp5ri5efYwcLg1LXmieOF7EjILK4btpg80d7zlUZx0ID21HVan2hXeipNAlKMv9k5%2BsKrf%2BI7PwA%2FjwPipFaK2rvP6psN4JHR1cvF1HDmwr3GGCXcQUmjgN5nvXuXAeR4uw6Rz47pI7FeLfDq52fTRINZ%2FCfzsAD8Jj8%2FIqhJkHHal6pbtHVc2zdjsfYwStbPGSkA%2FuksiE%2B8Gk70npqwzU%2BJeeeHcTJKIfnUigLPOmR9Yi%2Bsf8lg9gFupf9O%2BDEjhxNjXyFsWR%2B2G8wFvE3k5v4ovtRR6xmT7ITUemYDMmsmllfRkLGjFWgN605A8%2F7zYNpSpG9Ku5OqMJ3qGthJ8gyOUYNJCE1E%2BClv9KELXTuBOBU5lk6Vg3VBzEOrUPwDnZZoXzDDnv5jRBjqkAZg7H72i7n79QqBe7m8CbXF8sGcfmPHK1nmowJuzFgY3f6FymIE2UPaeIxYWaJ61emZKCLiO8BTvaVo1h%2BDqMX75SZi829doKqbwrqCnxb0ZK%2BSjSitmELgwvJorii3Tgrj7pYz5x0f2bf6zkNGXehdd%2F%2FbVAVD0md7%2BwiWt0N1U1SrkUgssPjG1vmTt7a%2F%2B2Olm3uNLOSJ07JYrlRK7au7z%2FCNi&X-Amz-Signature=c3060bf7d0b8ec9ea6df33f54e1e1b9713a65a6e0503524b326a0fa116efba80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
