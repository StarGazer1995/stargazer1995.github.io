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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI4BEFHY%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T141209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIQC74E5WdIMbw8nenI8ShP0FgFo510MRjILGEOeqnzZkkwIgNgBUAwdxaksoNSA%2FcvRRvoSfyx%2FVCbksIxuAAUL7CJEq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDEEcD37aCyqxUExIyyrcA%2BFzWyo3wn7ZrKbO3JV5CUhQMX2Lvv%2F2VsllpA6DeKe7u6gdnjydOEVmoz3gbWgw9ubcXZh%2FNr0s7NfhB%2B4OAIUsfVoGJAuHkPIW6Flsf%2BsA0%2BR3jMMpyEdMYuRB0Tuhf%2BRvkHeTJHuEwHtnG2P4NivN1x9zlI9jq28jcrLGu0jSiakqo9XuJL%2FgdQyT5XJXKrolobq2QUvtuC5bp4q54f4lC36j2Ad71GHCJxeQqmmdQVp%2FUNkJK1iEq0sUUDpdsbKEalxXW%2BbCo0%2Bi9y6xuJWyT1rpO%2BE7S4kXvtWhZZLMSHLuXkIVCd1LN%2BhdIlLXJJeuUZR3ePEfRC3bFvNWegaheHnRQHaHMW%2FgJcJuOc2k%2FBmXwIXhhRo4X544Gs5GebAhwuTHLjJl5xJ8PrW3%2BOwy9r%2B6ugZtOgmUbv8gKFryagVkl4C5jBu5jpmWjgJ1cB6GP%2BwcJ8hvMb17njg5ubvBqG7AcKs4DPFB8SlQsKo7Fjg%2FBfmBL1xGqUs4ang05sbDYH9xCS7qNFm7FA%2Bq81gsn1zQBNhLYfDlBFrLCn3bkeaR9svvPEPT5B7LgPJu5Am4UdPzd92jhJB0DUxC7HwkzpuKI5EymKB9k%2BPvlkBzwSmJNSTaF928t6MgMI6bgdQGOqUBxvpNSUqJMvCa80stcqFiwkfVIscCZXd5VSeZbYODjHQqDdK2Mp2HYuKUuYkWt2P8eS%2Fbkwdc2bJx4rG3MRg6%2FOL75%2FIa%2BD%2F9QhnJ9xJ%2BK4MJ3K4x3k08qwKWfGjmSY0sEvsC5Q1XA77LjajK4mb6oXUwJfvkkS65B7PwQYYumSx4j2EmOyxAin2PShyH82hUdmbLsf459aR60XOkBwm7BjsHWVZ4&X-Amz-Signature=38c0e593413d16fbb74dc286d75e2144d7d06b53da9c7fdd7db5ec94213a5aff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI4BEFHY%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T141209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIQC74E5WdIMbw8nenI8ShP0FgFo510MRjILGEOeqnzZkkwIgNgBUAwdxaksoNSA%2FcvRRvoSfyx%2FVCbksIxuAAUL7CJEq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDEEcD37aCyqxUExIyyrcA%2BFzWyo3wn7ZrKbO3JV5CUhQMX2Lvv%2F2VsllpA6DeKe7u6gdnjydOEVmoz3gbWgw9ubcXZh%2FNr0s7NfhB%2B4OAIUsfVoGJAuHkPIW6Flsf%2BsA0%2BR3jMMpyEdMYuRB0Tuhf%2BRvkHeTJHuEwHtnG2P4NivN1x9zlI9jq28jcrLGu0jSiakqo9XuJL%2FgdQyT5XJXKrolobq2QUvtuC5bp4q54f4lC36j2Ad71GHCJxeQqmmdQVp%2FUNkJK1iEq0sUUDpdsbKEalxXW%2BbCo0%2Bi9y6xuJWyT1rpO%2BE7S4kXvtWhZZLMSHLuXkIVCd1LN%2BhdIlLXJJeuUZR3ePEfRC3bFvNWegaheHnRQHaHMW%2FgJcJuOc2k%2FBmXwIXhhRo4X544Gs5GebAhwuTHLjJl5xJ8PrW3%2BOwy9r%2B6ugZtOgmUbv8gKFryagVkl4C5jBu5jpmWjgJ1cB6GP%2BwcJ8hvMb17njg5ubvBqG7AcKs4DPFB8SlQsKo7Fjg%2FBfmBL1xGqUs4ang05sbDYH9xCS7qNFm7FA%2Bq81gsn1zQBNhLYfDlBFrLCn3bkeaR9svvPEPT5B7LgPJu5Am4UdPzd92jhJB0DUxC7HwkzpuKI5EymKB9k%2BPvlkBzwSmJNSTaF928t6MgMI6bgdQGOqUBxvpNSUqJMvCa80stcqFiwkfVIscCZXd5VSeZbYODjHQqDdK2Mp2HYuKUuYkWt2P8eS%2Fbkwdc2bJx4rG3MRg6%2FOL75%2FIa%2BD%2F9QhnJ9xJ%2BK4MJ3K4x3k08qwKWfGjmSY0sEvsC5Q1XA77LjajK4mb6oXUwJfvkkS65B7PwQYYumSx4j2EmOyxAin2PShyH82hUdmbLsf459aR60XOkBwm7BjsHWVZ4&X-Amz-Signature=2f897e8a918d77a3f2bde643f64a94afbdbb35649f032a41541f811c7f191be8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
