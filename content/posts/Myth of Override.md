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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCWLKJEZ%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T210332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIEw5QzO5qa6KrKae8v084OuP5VK%2FDmmDqnl%2FBPAROl%2FqAiAEtkVAYtZ0MlVbn6v57aCSEr%2FM2VDdfFxXgotypkoQbir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMBWCWAY8OOCh0vO8nKtwDZhGR3MsLgGY7uOe73MErQenIyaZphwiWoMqq10qcnvfiZ9cU1WUpCcuI2g%2BBY2UD0h79JrF9bPDQCDUxiiGh2BVvuLupazbtmuDilyxpYPzhix%2FWg3rI%2FIh69H6H5Zbi4GjAajbg1WQFi8PhbndkoBeeIyO1ayMsn8oudAMehFaaDNx3xKQoVgweRGKuETXs3xkfmlhflfc8l30dQbDK0%2FSvhdOHa%2F0e1QuhN0T2TxrDnlnU9X9UO1LQsCDjUqgwVsX5Z9vGF1VftTYMSfgHxDzFlD7UEL2mHt95pzGW9hDGrbPcItw1vbXH1LtYrWZgSiZzvllEvPuecZYu4Z6ouJ0afd41FGug96A8dX5%2BsYICKsM8aoT%2BN8hSwDxCKynee84coCmyCTRV7F9tUsw6HScW3sBUE7elV25sQN4LUFfMeeXueN1015ntlP2P9w7Tr%2BnLfDAKK7%2Ffz9ZUtVGuI9kag79pJ2pPLwU%2Fiqb6kuKX9ISVjnvI%2Bl87aQ5M4SvSyKdd9jsx4G0FzwZ9oSv%2BgZX1kyjgiAjXWFHpqZJ7FaGx9kz3Z6UyCpxp2RZ9I%2F6w1FDmys3SP%2BuPTQf1ar9SP0GoBCfg%2F22BTZUj%2Fygj8spke9xA57IDryQAIOEwrp%2FC0AY6pgGulvzLn3WP01S8shpox7Qo99ZpTglcDnEvCYqpY%2B84HJeBQygvfVKiCgLw1WFU6ZmdItkPheccjfJBEktmgWnLAteNqZRL7hvbVuKwGavSisGKvjyYu%2FxTO7X8VeoA%2FmMS%2Frk%2BbTDzLRNVAy1Xe63hCgLA6fcQkJWK9joNN9V44s09QN4wRwA0zhvBHygu1EQ1YuLEN5LIDr1Th4mTSZbpUb4omA1q&X-Amz-Signature=0b446fb1aafe469826508d8f441840a16d2b8fe0984724f3e344a96f7f485f7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCWLKJEZ%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T210333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIEw5QzO5qa6KrKae8v084OuP5VK%2FDmmDqnl%2FBPAROl%2FqAiAEtkVAYtZ0MlVbn6v57aCSEr%2FM2VDdfFxXgotypkoQbir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMBWCWAY8OOCh0vO8nKtwDZhGR3MsLgGY7uOe73MErQenIyaZphwiWoMqq10qcnvfiZ9cU1WUpCcuI2g%2BBY2UD0h79JrF9bPDQCDUxiiGh2BVvuLupazbtmuDilyxpYPzhix%2FWg3rI%2FIh69H6H5Zbi4GjAajbg1WQFi8PhbndkoBeeIyO1ayMsn8oudAMehFaaDNx3xKQoVgweRGKuETXs3xkfmlhflfc8l30dQbDK0%2FSvhdOHa%2F0e1QuhN0T2TxrDnlnU9X9UO1LQsCDjUqgwVsX5Z9vGF1VftTYMSfgHxDzFlD7UEL2mHt95pzGW9hDGrbPcItw1vbXH1LtYrWZgSiZzvllEvPuecZYu4Z6ouJ0afd41FGug96A8dX5%2BsYICKsM8aoT%2BN8hSwDxCKynee84coCmyCTRV7F9tUsw6HScW3sBUE7elV25sQN4LUFfMeeXueN1015ntlP2P9w7Tr%2BnLfDAKK7%2Ffz9ZUtVGuI9kag79pJ2pPLwU%2Fiqb6kuKX9ISVjnvI%2Bl87aQ5M4SvSyKdd9jsx4G0FzwZ9oSv%2BgZX1kyjgiAjXWFHpqZJ7FaGx9kz3Z6UyCpxp2RZ9I%2F6w1FDmys3SP%2BuPTQf1ar9SP0GoBCfg%2F22BTZUj%2Fygj8spke9xA57IDryQAIOEwrp%2FC0AY6pgGulvzLn3WP01S8shpox7Qo99ZpTglcDnEvCYqpY%2B84HJeBQygvfVKiCgLw1WFU6ZmdItkPheccjfJBEktmgWnLAteNqZRL7hvbVuKwGavSisGKvjyYu%2FxTO7X8VeoA%2FmMS%2Frk%2BbTDzLRNVAy1Xe63hCgLA6fcQkJWK9joNN9V44s09QN4wRwA0zhvBHygu1EQ1YuLEN5LIDr1Th4mTSZbpUb4omA1q&X-Amz-Signature=750afaaacb0d707594b7e7130b7c80d2646f3084f92a6ab518362b5a928a39cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
