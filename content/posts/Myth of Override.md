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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAYU7GBS%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T020430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDu%2FDHny0avjEGTWQ%2Ft4UuRPPoxcMpUG28%2BfCLJ7X04AgIgbscYKra%2B%2Bu%2Fo%2FNJkGUgA5t%2BS%2FmqwI6fmfNqLvICRcB8qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3pcq6yc%2FswuQm1WyrcA1F7HyLQo65RRG%2BoMhOSWm8sgX%2FJF2EQ6tG9YxlMu5SmlsddApCcI8Ajtr3JxpX78KNKLeMwI12xUPq5WUgmbcpdhb1BRRpl03rE2gm3fEQs3wXsrT2Sn25FbXl9zjSW78BUsPAMDWxI3%2BBkF5F4vCMqiY3TJsjfW0E9KVTmZn%2BpN6SDpk8Xs5f8LVkBtrZ98hZ2Z358ozknJl3LFoLWtVz%2FPAPo73zk1ga3uQZsZaG%2BPmIMYiBnSvqI5S8PgxFlFRqf3Xc0ODqzgnFWoAN1gX9W8kG5pfPVnesou%2FKf%2Fn%2FYh65wg9huFQhcU%2F69em3ZdoqKeet%2BNU%2BJnBy1qaYwZQeeL%2FZAjfQQUHUCEPGX39Uv10jf5yda1ckrOZwSCsQ2ONiw2c3mQMeHmNIDb91bv%2FXEKqsFHKxMHKw5aL52OPVWSLke6qiGi34Z0XjM2YJclBW%2FFVQT7ptXT4jS0IWEGgyeeXuyOevgHQHjbe5U2KD4itk%2FdfUkwtFyjGgcxfei4svKSFVVJmzGVj%2FMyEFJofSZXW7Ym9LB3NbNn7LrFNdcg9ikw6SD8eYLjDjCHnonH9yC9pz0wMLCT8d6ImY73idhv97WFZ7ggYRxoJzopdSzIKg0sHV8LKDYyLTTMI%2B2jNIGOqUBfsVL1K82L0qhYbrrXkMIECmz62hjGN%2Bn4rYE%2FC3E8nCfTMTSCkLXThX6qlAo7u6RYpH5d0AVLMchPDQxlBwXR12kBgwUb%2BDEFnOihAivgkHDLlLsYGfSq56owaVVvy4T1saX9GYd%2F8OMsyEXiWi9oVN9l8XZW4Zbo81Zpxw18w435DVok6jwPZa%2FdbRIpYYNYTlGtphhviW6gUY59HJ%2F4UCyXbrW&X-Amz-Signature=9d216784b2000f01f7cc67b9dc4318a39de7c8394f1887245c46a6e77088c1a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAYU7GBS%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T020430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDu%2FDHny0avjEGTWQ%2Ft4UuRPPoxcMpUG28%2BfCLJ7X04AgIgbscYKra%2B%2Bu%2Fo%2FNJkGUgA5t%2BS%2FmqwI6fmfNqLvICRcB8qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3pcq6yc%2FswuQm1WyrcA1F7HyLQo65RRG%2BoMhOSWm8sgX%2FJF2EQ6tG9YxlMu5SmlsddApCcI8Ajtr3JxpX78KNKLeMwI12xUPq5WUgmbcpdhb1BRRpl03rE2gm3fEQs3wXsrT2Sn25FbXl9zjSW78BUsPAMDWxI3%2BBkF5F4vCMqiY3TJsjfW0E9KVTmZn%2BpN6SDpk8Xs5f8LVkBtrZ98hZ2Z358ozknJl3LFoLWtVz%2FPAPo73zk1ga3uQZsZaG%2BPmIMYiBnSvqI5S8PgxFlFRqf3Xc0ODqzgnFWoAN1gX9W8kG5pfPVnesou%2FKf%2Fn%2FYh65wg9huFQhcU%2F69em3ZdoqKeet%2BNU%2BJnBy1qaYwZQeeL%2FZAjfQQUHUCEPGX39Uv10jf5yda1ckrOZwSCsQ2ONiw2c3mQMeHmNIDb91bv%2FXEKqsFHKxMHKw5aL52OPVWSLke6qiGi34Z0XjM2YJclBW%2FFVQT7ptXT4jS0IWEGgyeeXuyOevgHQHjbe5U2KD4itk%2FdfUkwtFyjGgcxfei4svKSFVVJmzGVj%2FMyEFJofSZXW7Ym9LB3NbNn7LrFNdcg9ikw6SD8eYLjDjCHnonH9yC9pz0wMLCT8d6ImY73idhv97WFZ7ggYRxoJzopdSzIKg0sHV8LKDYyLTTMI%2B2jNIGOqUBfsVL1K82L0qhYbrrXkMIECmz62hjGN%2Bn4rYE%2FC3E8nCfTMTSCkLXThX6qlAo7u6RYpH5d0AVLMchPDQxlBwXR12kBgwUb%2BDEFnOihAivgkHDLlLsYGfSq56owaVVvy4T1saX9GYd%2F8OMsyEXiWi9oVN9l8XZW4Zbo81Zpxw18w435DVok6jwPZa%2FdbRIpYYNYTlGtphhviW6gUY59HJ%2F4UCyXbrW&X-Amz-Signature=35117c5e425c72bbcb38f5e4aef578f8f32b73d71a1ba5c62c6331d84d55a7a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
