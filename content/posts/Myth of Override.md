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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYAEFAI6%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T103327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FDZabRIdWrWKYN4s4w4%2FgvMEGT9SH2%2FQlkpxLTTQIxwIhANR73c0SvaGdXWZBNUDx29skSWTMiw1ul7MgR%2BqbbcREKv8DCEoQABoMNjM3NDIzMTgzODA1IgyJF105k34lc9eiXYQq3ANN%2F2N42h9W9awVWXkpKuHzDLGWI2D8TdzZfxcsce5wMi5CRP%2Ft2lyGTgGjRs7cVCPExOQhCe6Yh9wKSaS8op66rHG5la%2BIp6onJmAAF6yGr5Gf2aD%2Bl7oJV3qUEbi2EW0YmM7shXUTxqvpwGxXZ7Tibj3k4mw4WMeCYsTprd%2BKeNQa1GlEcFzGcdoZP4V8HNdXZEJgYMXwwk8Btp2ee%2BPssaCNn8KQOoapDPnFNWQuwoFgigJkoYyO384oQYCzFiy30UYRZF6t%2BY9%2BgOwTB2tQT94sRdTWd%2B5gGglOnLZ86RE6EOvqYX1ElImsMUmD5CTs%2BonH26ORhcJU%2B0pBAUfyLwfW8HXJXJBT2q%2FMpWYU1kwZ8HyHRYbY5W4OUu%2FFL7HYgRUq0%2BGpJu2jWr5IVMvralAtj0plesYCznS5N1OEx6EQIGjhLvb0vwgKQQJMiJV2S4u6Xemy1BXp3ey%2F473sERQMEt18YsWPhL5Ryj0JHs4jeXmGi0IJv4l3gnxL2HRn1MdZ%2FVEDh2h%2Bt9B9bHvq4i2iZzVUur7yiNUYvCDGdzuj8TANWM4JGKF3GA6ahduIsHq%2FyrI11dQqqO5B8lApaCBL3sXV0GHjEizVdZfpZClGCKW9fSowZGRNSjDhzPPRBjqkATDw6HTDCprDK6Bkxn%2B7Y3PVeQD8XV2PtqY0LBc8kQfhsx4RHu1hSMs183Xm9FZaR4IzF7Cnybxhlayt%2FOGmlTyR4IWF%2B4VxWY9s0PmF8tCQv3NoK4JXgVz0mC1DSaQIC1CHIIdLFvV9dcOY9nyXJtvVUk0snLrsm2kfbSxylKkjFO9tOxMpDpyAQlD0gyJ%2F7C89tD2L4JN6OOsS8PdVlnMlpce8&X-Amz-Signature=d6536f507b0391f5f6518762b40c44fedf7de4b72d79fd923cf5b67f19380926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYAEFAI6%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T103327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FDZabRIdWrWKYN4s4w4%2FgvMEGT9SH2%2FQlkpxLTTQIxwIhANR73c0SvaGdXWZBNUDx29skSWTMiw1ul7MgR%2BqbbcREKv8DCEoQABoMNjM3NDIzMTgzODA1IgyJF105k34lc9eiXYQq3ANN%2F2N42h9W9awVWXkpKuHzDLGWI2D8TdzZfxcsce5wMi5CRP%2Ft2lyGTgGjRs7cVCPExOQhCe6Yh9wKSaS8op66rHG5la%2BIp6onJmAAF6yGr5Gf2aD%2Bl7oJV3qUEbi2EW0YmM7shXUTxqvpwGxXZ7Tibj3k4mw4WMeCYsTprd%2BKeNQa1GlEcFzGcdoZP4V8HNdXZEJgYMXwwk8Btp2ee%2BPssaCNn8KQOoapDPnFNWQuwoFgigJkoYyO384oQYCzFiy30UYRZF6t%2BY9%2BgOwTB2tQT94sRdTWd%2B5gGglOnLZ86RE6EOvqYX1ElImsMUmD5CTs%2BonH26ORhcJU%2B0pBAUfyLwfW8HXJXJBT2q%2FMpWYU1kwZ8HyHRYbY5W4OUu%2FFL7HYgRUq0%2BGpJu2jWr5IVMvralAtj0plesYCznS5N1OEx6EQIGjhLvb0vwgKQQJMiJV2S4u6Xemy1BXp3ey%2F473sERQMEt18YsWPhL5Ryj0JHs4jeXmGi0IJv4l3gnxL2HRn1MdZ%2FVEDh2h%2Bt9B9bHvq4i2iZzVUur7yiNUYvCDGdzuj8TANWM4JGKF3GA6ahduIsHq%2FyrI11dQqqO5B8lApaCBL3sXV0GHjEizVdZfpZClGCKW9fSowZGRNSjDhzPPRBjqkATDw6HTDCprDK6Bkxn%2B7Y3PVeQD8XV2PtqY0LBc8kQfhsx4RHu1hSMs183Xm9FZaR4IzF7Cnybxhlayt%2FOGmlTyR4IWF%2B4VxWY9s0PmF8tCQv3NoK4JXgVz0mC1DSaQIC1CHIIdLFvV9dcOY9nyXJtvVUk0snLrsm2kfbSxylKkjFO9tOxMpDpyAQlD0gyJ%2F7C89tD2L4JN6OOsS8PdVlnMlpce8&X-Amz-Signature=f5a513503e15da099ef42abcc7d51c63b49091da45fbdb2fabbee3c97bc666cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
