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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCWZSUW%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T145156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnAEbnq%2FtxTySfbb7u9LDiOQwmQ8T%2BMmKhHEsEA0cJIAiEAgicwDrHvtyNTE6yw4spZ%2BIuzswN%2F466MBbW%2BeFaOQ1wqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJcegJOhR%2BkRO7qpkyrcAy9bElAY0bFR7%2BVh4QWXFTnVbYR%2BzLKF8OIGCEmc8sFbm9IM8kcXkTD3pOBxvzKXiliFngZqhIwBRCpizkfVlvv7CwJCqhkF12cD9%2BdzNQGagpN%2FdD5S1c9BxdChr5h2SYzorL%2F1%2BUmhZKCTNvJV%2BmCr60TzAV5B9NtUtA3c%2Ftnm9gV%2BUGORM7zvgozfKGHMKp%2FJgNu3pyRPCFqNMvHYZo81RHC6%2Fl980DK5tXi9C1WCpUw4%2BO9nUrGCG7JyttiDTvHYKhHC54m995Mtzxrs7jjvad%2BTOjOBxKaLeCyQco7gO3OE3SgzSyRvZ6wNoqkfAnvSsEGcbQYBeai3lLCWUxXhmfyGO6imvn80b0w7oHH6bwoEdmI0AalKkYNN31LEkS6e3fd%2BQLsv6BFWb4wF1DIrGOerXhKSjQpLBSuwkK9kLm1rh5MuH124OImxBSXL%2BX12RIBGM2Orw8fJzu0YbhUcfBcFuZ1JufuaA%2FqaOXj6OXH1ygm6JYgcrMCmDiHcbx%2BnyUAHP1PN3RAcimtIZs%2FhUu6ASPVIm%2BM3mqNa6ksyOlCX0%2FOd3lritNYTfHW%2BRVDJgC8%2FtYN6DsJbW3pAL7AS%2BqAbRFbSpZH7V5AFK1l44QDCU9DlN6QL1dVMMIjz29AGOqUBSYB9VN9d7YIamyuC21LFSSUkEEIOerApz5p%2FRj7My7%2BjSQ4%2FiZminnLpEnVGQ7lAAm8o4t5isnmB0WLiKR%2BhkJHhvLg4dy7EPPPxwlbG6eF7m75OfAe108TkM1TjSL8rx5ukUfEGssW5qgXPe4YK%2FU8P8Xi3KKZHyiSLieAbW6%2BfXEEympQPjIAI9F39jBWmacp0Bu815SeRiOGNXc2dVTHPhWU1&X-Amz-Signature=d6c9c5088cc36df0022a8ad7394548c765584a3ae82a133c8faee337080e6fe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HCWZSUW%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T145156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnAEbnq%2FtxTySfbb7u9LDiOQwmQ8T%2BMmKhHEsEA0cJIAiEAgicwDrHvtyNTE6yw4spZ%2BIuzswN%2F466MBbW%2BeFaOQ1wqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJcegJOhR%2BkRO7qpkyrcAy9bElAY0bFR7%2BVh4QWXFTnVbYR%2BzLKF8OIGCEmc8sFbm9IM8kcXkTD3pOBxvzKXiliFngZqhIwBRCpizkfVlvv7CwJCqhkF12cD9%2BdzNQGagpN%2FdD5S1c9BxdChr5h2SYzorL%2F1%2BUmhZKCTNvJV%2BmCr60TzAV5B9NtUtA3c%2Ftnm9gV%2BUGORM7zvgozfKGHMKp%2FJgNu3pyRPCFqNMvHYZo81RHC6%2Fl980DK5tXi9C1WCpUw4%2BO9nUrGCG7JyttiDTvHYKhHC54m995Mtzxrs7jjvad%2BTOjOBxKaLeCyQco7gO3OE3SgzSyRvZ6wNoqkfAnvSsEGcbQYBeai3lLCWUxXhmfyGO6imvn80b0w7oHH6bwoEdmI0AalKkYNN31LEkS6e3fd%2BQLsv6BFWb4wF1DIrGOerXhKSjQpLBSuwkK9kLm1rh5MuH124OImxBSXL%2BX12RIBGM2Orw8fJzu0YbhUcfBcFuZ1JufuaA%2FqaOXj6OXH1ygm6JYgcrMCmDiHcbx%2BnyUAHP1PN3RAcimtIZs%2FhUu6ASPVIm%2BM3mqNa6ksyOlCX0%2FOd3lritNYTfHW%2BRVDJgC8%2FtYN6DsJbW3pAL7AS%2BqAbRFbSpZH7V5AFK1l44QDCU9DlN6QL1dVMMIjz29AGOqUBSYB9VN9d7YIamyuC21LFSSUkEEIOerApz5p%2FRj7My7%2BjSQ4%2FiZminnLpEnVGQ7lAAm8o4t5isnmB0WLiKR%2BhkJHhvLg4dy7EPPPxwlbG6eF7m75OfAe108TkM1TjSL8rx5ukUfEGssW5qgXPe4YK%2FU8P8Xi3KKZHyiSLieAbW6%2BfXEEympQPjIAI9F39jBWmacp0Bu815SeRiOGNXc2dVTHPhWU1&X-Amz-Signature=2d0fe06ca16110a3ebfc596b868c057a0c6c26ce378d7210a04a04ba35bfc5a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
