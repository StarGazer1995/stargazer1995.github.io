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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5P67VPK%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T202203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMMD2MA%2FF6rTjGSFxYNvgtxcDkpmrA3nCV1BGHAiPX2wIgRjElTgTK239nxHSEXMX85s%2BAjFCRbb4FH8FdNwN4C3wqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOn%2BIKDGhbphvFDAnSrcAztwoIe%2BERuhLdrwaMXp9ATFkQ5xc%2FBw%2FkvK4Rezb5MWLH%2FScjedYDHjLWMa0ZQ4DU3Ch53m1Cy5s9txKYf8fQthFVoLUEkSW2XiWLe8xOm1kiB%2Ferx6pWdhNEebCI7xJhSIar%2BAi9ptkJzGZ7Edo5CKUvQImScrgCM3NvcCt54t4PfiensNhMUEsiZnAnHDUS29FK4o2dyry%2FYNhYTH2RA1nEtD7zstZtb4xHo4qK0wkZRmW7PzTz%2BEiHYrVRxa%2BV1j0x6eEOmbVs7ASm6nGkbnIA9kAHMNMlknKrvVcrX5z7SEeDK7ZY7Ijhkbp55FlJU5I1fqopz3OFse9Sk8CYQINx7mo6TP7rF2evHfQz85fjBE9HZAn2pesK9YPrXfC7UJkPItvtqREIpfALdHwpkwSAFg7HaNxtr6ZamZq9T8%2BRVT%2BcrEyeQUyljQyHV4copwhgu12tYUubnjDg4tdvXeip87UxvjOE9HdsLB9PfVJ2gMYgKa5J0L5KqtQT9e4eYwP2aiKSj%2BTkn0okPd3%2B55XU%2BvURymjUpnVVxZXPqF1IVOotwI52SuefKto8dmfhIkXjiwL%2BTw0KYIkBPA8HKbpIviVD34UxgPWX5CU4rN3fumwMotwbB53L4hMJLGotQGOqUBPUc8npCZMzlmcD%2BjLjdo0yrGNZinxHPQGjP1h3Ggv25u0rMqyythqeirRi67ZlQtBy%2BscgHMepY55nPvIcoJfV0Yb08BhqaVWHKch0YW6w3Y6bbhHoGtA3uFIrQRHRgrHm8YAxIMUwb1EPb4Rt74LLUkPZzuZS5BEqN2QqAGr54FdEQV%2B%2FhqMwc0WOf4gHXvVkLFlVVO%2BeOeJ2mV2yatDxBeX%2Bee&X-Amz-Signature=d620c4e7e6a61d1fd5bcdb88997ed28465360e58281a6e43c0fbc62741fafb4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5P67VPK%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T202203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMMD2MA%2FF6rTjGSFxYNvgtxcDkpmrA3nCV1BGHAiPX2wIgRjElTgTK239nxHSEXMX85s%2BAjFCRbb4FH8FdNwN4C3wqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOn%2BIKDGhbphvFDAnSrcAztwoIe%2BERuhLdrwaMXp9ATFkQ5xc%2FBw%2FkvK4Rezb5MWLH%2FScjedYDHjLWMa0ZQ4DU3Ch53m1Cy5s9txKYf8fQthFVoLUEkSW2XiWLe8xOm1kiB%2Ferx6pWdhNEebCI7xJhSIar%2BAi9ptkJzGZ7Edo5CKUvQImScrgCM3NvcCt54t4PfiensNhMUEsiZnAnHDUS29FK4o2dyry%2FYNhYTH2RA1nEtD7zstZtb4xHo4qK0wkZRmW7PzTz%2BEiHYrVRxa%2BV1j0x6eEOmbVs7ASm6nGkbnIA9kAHMNMlknKrvVcrX5z7SEeDK7ZY7Ijhkbp55FlJU5I1fqopz3OFse9Sk8CYQINx7mo6TP7rF2evHfQz85fjBE9HZAn2pesK9YPrXfC7UJkPItvtqREIpfALdHwpkwSAFg7HaNxtr6ZamZq9T8%2BRVT%2BcrEyeQUyljQyHV4copwhgu12tYUubnjDg4tdvXeip87UxvjOE9HdsLB9PfVJ2gMYgKa5J0L5KqtQT9e4eYwP2aiKSj%2BTkn0okPd3%2B55XU%2BvURymjUpnVVxZXPqF1IVOotwI52SuefKto8dmfhIkXjiwL%2BTw0KYIkBPA8HKbpIviVD34UxgPWX5CU4rN3fumwMotwbB53L4hMJLGotQGOqUBPUc8npCZMzlmcD%2BjLjdo0yrGNZinxHPQGjP1h3Ggv25u0rMqyythqeirRi67ZlQtBy%2BscgHMepY55nPvIcoJfV0Yb08BhqaVWHKch0YW6w3Y6bbhHoGtA3uFIrQRHRgrHm8YAxIMUwb1EPb4Rt74LLUkPZzuZS5BEqN2QqAGr54FdEQV%2B%2FhqMwc0WOf4gHXvVkLFlVVO%2BeOeJ2mV2yatDxBeX%2Bee&X-Amz-Signature=933489dfffff1131a7db62782ac4be6740a8f078df8370686f00e73fb6744f8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
