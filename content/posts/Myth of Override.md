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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRR77WE7%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T235957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIHDLgCT1uEAiizB9n6zSqa%2FT0XDwTyuTtmr9uiFE6cqwAiEAnpv%2FTUNE2igaIHP4vBU5ozfg%2FDevo4s6IOxEh%2BuPVEIq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDLLjjDTttA2cZBOAkircAz6PM9HixzvSxjutEqBmcYHwDwcneyX0tSUms3htbnbJ43pY22G%2B8GhPOQnN%2BdYv8UyXohBS6cSOua4G%2FNA0FsXo3CThmwNnaPoSW0RNX0OIwc7qLBZ189WPnpyEQt8IWwyDznbAZ3izJtK1I6BdwsYqE4w4%2Bu7WgNZ1LYIzw36x3Rcb8O5CJwR%2F8v0JyAlJFipj%2B7LdzG38Qo7gtOT8iJHajh8734qwnioe1iU4EbXyixI8m9Vz9xSKu5Rgky2G9X1PURcvEc9FdXo6pVaRlHXBo1lymLy%2F85E4ykb9CwEb3KPp0lrcxx9M%2BNkraJcc6hYcmu1kRih4uijSrD6q437qF6lRZwar%2FmVJY400DAJ5dW9IMl4MMHDmJi%2BkrWYay%2FEG1o9I4%2Fg3kx0cKHjDb56PrS2fIu0n6RnYN5GUCJgj6b1d5lnifSMNSzhgusP0oSNBtg0FS1uRwbGaSyi8yr5%2BO8HK0ZWTApBitpSWQ6ZJL7%2Fk%2BoKGRCIRraZrb%2BxPI6J4DvDa%2FXMxW%2FRfFPr321yqbrWvMFN796ICi1otgLEjpcRD%2Bph%2F2TkWU%2BoFjxLdiW49eZ5pmZNd8tDwLDTAOnH9pVNoz3vxl4qVsPWLUvcjQyMard%2BxtDoLEdYzMP%2Bl4dUGOqUBHBKu8G7EK%2B%2BpdaxOordvCinzMm%2FQRBCrXjEACj8nFORJyVwFkwa3RrCCE8J5aVZ5xnbeTXlPxXcId0XbTrBfiUmyJKhhm7YwkpVB5UTmEEhWMXdrfQRBeG5W7HECcQYLNQjA4n9dnLN7RIhmHe0cHsQeNX9CBT%2BhrRv7Ul1hO9JfrWPHFY7ZyWDo%2BniZqncmyZhQ70a4kbILJ0bHmxIsviV3XJFo&X-Amz-Signature=e6d23a641181d954e49f0b89922ff8534d8f3e5672ce5565e65fa1ba0d1a5acd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRR77WE7%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T235957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIHDLgCT1uEAiizB9n6zSqa%2FT0XDwTyuTtmr9uiFE6cqwAiEAnpv%2FTUNE2igaIHP4vBU5ozfg%2FDevo4s6IOxEh%2BuPVEIq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDLLjjDTttA2cZBOAkircAz6PM9HixzvSxjutEqBmcYHwDwcneyX0tSUms3htbnbJ43pY22G%2B8GhPOQnN%2BdYv8UyXohBS6cSOua4G%2FNA0FsXo3CThmwNnaPoSW0RNX0OIwc7qLBZ189WPnpyEQt8IWwyDznbAZ3izJtK1I6BdwsYqE4w4%2Bu7WgNZ1LYIzw36x3Rcb8O5CJwR%2F8v0JyAlJFipj%2B7LdzG38Qo7gtOT8iJHajh8734qwnioe1iU4EbXyixI8m9Vz9xSKu5Rgky2G9X1PURcvEc9FdXo6pVaRlHXBo1lymLy%2F85E4ykb9CwEb3KPp0lrcxx9M%2BNkraJcc6hYcmu1kRih4uijSrD6q437qF6lRZwar%2FmVJY400DAJ5dW9IMl4MMHDmJi%2BkrWYay%2FEG1o9I4%2Fg3kx0cKHjDb56PrS2fIu0n6RnYN5GUCJgj6b1d5lnifSMNSzhgusP0oSNBtg0FS1uRwbGaSyi8yr5%2BO8HK0ZWTApBitpSWQ6ZJL7%2Fk%2BoKGRCIRraZrb%2BxPI6J4DvDa%2FXMxW%2FRfFPr321yqbrWvMFN796ICi1otgLEjpcRD%2Bph%2F2TkWU%2BoFjxLdiW49eZ5pmZNd8tDwLDTAOnH9pVNoz3vxl4qVsPWLUvcjQyMard%2BxtDoLEdYzMP%2Bl4dUGOqUBHBKu8G7EK%2B%2BpdaxOordvCinzMm%2FQRBCrXjEACj8nFORJyVwFkwa3RrCCE8J5aVZ5xnbeTXlPxXcId0XbTrBfiUmyJKhhm7YwkpVB5UTmEEhWMXdrfQRBeG5W7HECcQYLNQjA4n9dnLN7RIhmHe0cHsQeNX9CBT%2BhrRv7Ul1hO9JfrWPHFY7ZyWDo%2BniZqncmyZhQ70a4kbILJ0bHmxIsviV3XJFo&X-Amz-Signature=9fda0b2922e2cf39ddd136d11425302501d77872499b35e279f26ab4470a4f1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
