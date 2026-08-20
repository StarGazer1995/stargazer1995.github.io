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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S626JLK2%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T082337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCues5f4%2FONKtK752Ue2bXiefJbl2ttXAEQzjPKmZrQAgIhAM2JDjj7T4TU1WqBZ7pNju107lUd0xI6cz%2BZjwUXMwKIKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRoe171KQyOj%2BmxSgq3APKmoLZ9tdQv3j2nZNrD56tAGcggcE4TFygNWtTLW1eleFFvWBupyn%2BhGU6iHHvoWsquKdLFotTTo%2Bl1o77E08VYLk7BDuwblz14gzfDQ2p6znYNv3OpGGqkTiD1psTFbIBVgVgXnpXbFvPzl%2FfrkdO0KL39gCOpsZgoFMSeWFSo2GNu%2Bybz%2BSFqVE24wo1%2BRw0qi9jgpXrTI48i8N%2BJ0t%2FCr501TCAy5hkjsS8P5jaDQJbyG3U2A4jUVtoLV7nyjYrC2jKEOEMQf4K%2BWsRJdw5oczjCVvqeWCAFP7O%2F4caFjCetOolOwoWaZZwFEavIb9r9%2BihGfOzpaiJc873Ie3p5UdNgenJvGkt7K1hCE3dOkh%2FtFpUkH7RB%2FAVDzqDRp5xZ%2BiPbn9rGH3qxDFsTzTfATc0zXAPDC4iw7%2BrrS1bLK5YWG1MBLWelvOnR1F4ujQJCspsMNQokfFSl99eZtx3vLWoGQY0L1Vps%2F2nd3o5e6pwihMD5qFfJ%2FZk%2FC%2FM%2BM3Zak%2B77eKE4Fp%2FidgGXrDqBEtozx60OoWwR21oNAwsgGXWaU0MKGlB4aF14yPMq57xcy8bN8XE46gRdqqn5C4OMETzgSVm2VaNAIRo4EK2uofZL3rQzh7ZFiavSzD2qprUBjqkAV%2Fhnvtq2rb2WyOlLxQXUUxMqCSCOMnw0wthELdAC0fwQsbetEJFp8%2BI8EatgWxfGCEaSd1MyuEgwK2ixJAWbUIENPn4Yz3vEHftMVmXjuXT7pAYPziJa1Eq9%2F9Py35B6khk05acQ0FJfBkVd8jFFHs%2B1NCibxyLOI%2BzeuE9ZTsETN2fwzbk0%2BrU5%2Fct8VkX%2BbjCAhkTQZSc%2FZ82nr2%2BW1xu%2FpsE&X-Amz-Signature=bc1b5de81e6ad113760db8f6db2e7d971f0dad9f58f61b5575f160203c9f9f8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S626JLK2%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T082337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCues5f4%2FONKtK752Ue2bXiefJbl2ttXAEQzjPKmZrQAgIhAM2JDjj7T4TU1WqBZ7pNju107lUd0xI6cz%2BZjwUXMwKIKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRoe171KQyOj%2BmxSgq3APKmoLZ9tdQv3j2nZNrD56tAGcggcE4TFygNWtTLW1eleFFvWBupyn%2BhGU6iHHvoWsquKdLFotTTo%2Bl1o77E08VYLk7BDuwblz14gzfDQ2p6znYNv3OpGGqkTiD1psTFbIBVgVgXnpXbFvPzl%2FfrkdO0KL39gCOpsZgoFMSeWFSo2GNu%2Bybz%2BSFqVE24wo1%2BRw0qi9jgpXrTI48i8N%2BJ0t%2FCr501TCAy5hkjsS8P5jaDQJbyG3U2A4jUVtoLV7nyjYrC2jKEOEMQf4K%2BWsRJdw5oczjCVvqeWCAFP7O%2F4caFjCetOolOwoWaZZwFEavIb9r9%2BihGfOzpaiJc873Ie3p5UdNgenJvGkt7K1hCE3dOkh%2FtFpUkH7RB%2FAVDzqDRp5xZ%2BiPbn9rGH3qxDFsTzTfATc0zXAPDC4iw7%2BrrS1bLK5YWG1MBLWelvOnR1F4ujQJCspsMNQokfFSl99eZtx3vLWoGQY0L1Vps%2F2nd3o5e6pwihMD5qFfJ%2FZk%2FC%2FM%2BM3Zak%2B77eKE4Fp%2FidgGXrDqBEtozx60OoWwR21oNAwsgGXWaU0MKGlB4aF14yPMq57xcy8bN8XE46gRdqqn5C4OMETzgSVm2VaNAIRo4EK2uofZL3rQzh7ZFiavSzD2qprUBjqkAV%2Fhnvtq2rb2WyOlLxQXUUxMqCSCOMnw0wthELdAC0fwQsbetEJFp8%2BI8EatgWxfGCEaSd1MyuEgwK2ixJAWbUIENPn4Yz3vEHftMVmXjuXT7pAYPziJa1Eq9%2F9Py35B6khk05acQ0FJfBkVd8jFFHs%2B1NCibxyLOI%2BzeuE9ZTsETN2fwzbk0%2BrU5%2Fct8VkX%2BbjCAhkTQZSc%2FZ82nr2%2BW1xu%2FpsE&X-Amz-Signature=8a07e2f9789c97846dd00ac1ff2911df5364bbe22ee33f95666de5340df2d965&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
