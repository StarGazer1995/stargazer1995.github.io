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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3D4GWGX%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T102435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFAatI1c1dsmrrsQUH6Om7%2Fjixz%2FVGTc41wyfOcUGgyIAiEArj%2FFSYxvTqcBoe%2FDnJY6Big8Wv3M7ZhqNSibvQbZXpIq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDJxMDNqRMMwAdVbzOircA9IseYGnoxLr2BlXJ0pl5bOz%2BAX9y%2BNt4F3cRN%2BpjfqmMu78UH8dQMcKiFRlJSXCOX4%2BvQvNTpMTAcvb49gFvlgMkplGNFRbERvGHVmt9m7UZMQL%2F5lSofvs7z1ZggERN%2FPCbYZmtZozwRPFX7Ww%2BcoxEEzjEeMLafSSNnGjMrDqcih7p93vfaKpdQyNoJjPMlgfdl5%2B9BQlzexNPpIhfb4GW%2B6AiB06e7O68TrJO4IOUVAZJHahKyEvZ%2B0v86CGQFhX294cqUXEnKLQvXRs8bv5tnhREWC6Wl%2FXzzWtrFPy2SuZKvnWAk65mrYqr8E1KapgXvk1iQE3htlmxTC62Q51tWT68QDxMiqKse%2FNpRW1cjsMGtLWp002TM1aq8EhXOE9aZ81Qnf2yn9oJCK%2B0oQhOPQsJBsMQVvyhfP0vLMDayOS8enZW68uHhMfumAwqzSs3jpIotT%2FbNrJaMRT74gYdA%2FB2GlDUtnlcdPwKSMpRhExd44pl3JjAxpRQjqYxIEbfzrhxsX2eMqS9vpGZjYZpag7%2BgN65N%2Ft9j4%2FUkXn1ZcW9iHE7dls9mKjtImN8z72wlzjH3J8TwZe3a%2BG6PgntlFjHTcDVpLcLirR2%2F%2BKjYU06wCBoeJenf1sMPekrdYGOqUBFE0YVos%2BGH%2FBM3qmk1J%2FAz40Vkc9wISuLqiRHyx4FjPRQNGdKq6afISJZRV95fB3VR4pV4c2pHNCUS61gouWbY%2B3f7b2z0cMFcZ3eM%2FhXq6xZ01s8LM8ByJ5E%2Fgtl7wgdUMXD%2FAr86l6ynWf715cD%2Fk94uyP4BF938XO0LNp2SjdX%2B852hALbGzN89KwgaT05wP7cFGqnXu6q%2BUqKjvUluMPMT3o&X-Amz-Signature=4d761dd3a71f8aa88fd858098a7f31141f98d5c16cc0be79c66909f9541e9e72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3D4GWGX%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T102435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFAatI1c1dsmrrsQUH6Om7%2Fjixz%2FVGTc41wyfOcUGgyIAiEArj%2FFSYxvTqcBoe%2FDnJY6Big8Wv3M7ZhqNSibvQbZXpIq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDJxMDNqRMMwAdVbzOircA9IseYGnoxLr2BlXJ0pl5bOz%2BAX9y%2BNt4F3cRN%2BpjfqmMu78UH8dQMcKiFRlJSXCOX4%2BvQvNTpMTAcvb49gFvlgMkplGNFRbERvGHVmt9m7UZMQL%2F5lSofvs7z1ZggERN%2FPCbYZmtZozwRPFX7Ww%2BcoxEEzjEeMLafSSNnGjMrDqcih7p93vfaKpdQyNoJjPMlgfdl5%2B9BQlzexNPpIhfb4GW%2B6AiB06e7O68TrJO4IOUVAZJHahKyEvZ%2B0v86CGQFhX294cqUXEnKLQvXRs8bv5tnhREWC6Wl%2FXzzWtrFPy2SuZKvnWAk65mrYqr8E1KapgXvk1iQE3htlmxTC62Q51tWT68QDxMiqKse%2FNpRW1cjsMGtLWp002TM1aq8EhXOE9aZ81Qnf2yn9oJCK%2B0oQhOPQsJBsMQVvyhfP0vLMDayOS8enZW68uHhMfumAwqzSs3jpIotT%2FbNrJaMRT74gYdA%2FB2GlDUtnlcdPwKSMpRhExd44pl3JjAxpRQjqYxIEbfzrhxsX2eMqS9vpGZjYZpag7%2BgN65N%2Ft9j4%2FUkXn1ZcW9iHE7dls9mKjtImN8z72wlzjH3J8TwZe3a%2BG6PgntlFjHTcDVpLcLirR2%2F%2BKjYU06wCBoeJenf1sMPekrdYGOqUBFE0YVos%2BGH%2FBM3qmk1J%2FAz40Vkc9wISuLqiRHyx4FjPRQNGdKq6afISJZRV95fB3VR4pV4c2pHNCUS61gouWbY%2B3f7b2z0cMFcZ3eM%2FhXq6xZ01s8LM8ByJ5E%2Fgtl7wgdUMXD%2FAr86l6ynWf715cD%2Fk94uyP4BF938XO0LNp2SjdX%2B852hALbGzN89KwgaT05wP7cFGqnXu6q%2BUqKjvUluMPMT3o&X-Amz-Signature=791b1fb2cd4d3aa0ced0b00f9378909dd45b725c4fd8b0bc240f42e035b4b750&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
