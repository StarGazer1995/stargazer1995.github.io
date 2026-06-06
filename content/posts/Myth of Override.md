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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3TCJOAS%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T130450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD56bY9%2FEyX9ddfbKJlyslwTQVXCyq6DHEq0G2ZCL7O3QIgY%2BN%2BecI4i2SDeAVbUgtL47%2FG7wGd54Jlg5R2WNnhDpUqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzWlMP%2BcgsZtskenyrcA7Za1Q%2BUnyCgXBQCcuDOEsdxMEg2oz5aWIrgJjr%2FnvU8AS2PEjc3wUjTX6DbV8PHPccZJ7g0nMCPVDFQYlZX9cUw%2BSJq%2F0yvG3fBATsVpzxNuAW3y%2BJWkrUu53f4Fx8T7YBKRdaImNUiJeoEyFj807%2BqgYx8Z9AJ291proznSQ0nsMVnjazbijVXyfYqNXmHJtZvH5Ven43BXK9tEECYDPQdgWCs4snptZWEWefj%2F0A%2F7MYjfC1BLofJXoLR8K7IGUyco99yHl0Gp8esfPFpmYsa9qoDLutDYKEs7WoL7dyVPb6aN%2Bq1BZZqcRCnHdZHokvZIjW6d1rmpJER2S%2BrjFkOdF%2FFzDrCvyWFX1StUXc7me%2FcUr14pISWnFr7%2BtVUvcc%2Ft3Lc7%2BPb3C0P9vvG832Zmsw6Zb8N6hupSBYM9EFTtbFIfcg%2BOqTd1Y0eOCsm7sk%2FMVWugteOMEQwX9gmTXt8BE5tTr%2Fgu2IRsFVO4teBdbDCfzYc0G56Sh%2B82PQUYPaXLiKIeVaAStbREpVD5JFCSSuRR1SL2yqDiUIU1Vz6EmZcFDrAUyUDa%2FNtW7Mbc2u3W9l1%2FL6FnRHmkRaRb%2FqBSQXDsO71Oa1%2Fk8kXSsVq6HDvpqBQlKvfZ8tOMJCMkNEGOqUBu2rSqnHdTEWra6HGMD0XT1HJgpow1sea7ucOCfPllkASCtPlJ38uDTDKgVTeQ4gX%2BvYrWF0Lp77%2FsjgqWyNObar5568PR5ckSp9BZpGdIKY2LELLFOGMyjxCTk9M1xoRje1fKPhkmVhhi7hmFB7GMZwLiQKP%2ByWjMRcUkQF%2FAEX5EH3oSl%2BH0LpXByPWdNVMUHQtA16RlbQMuaRE4eMJyOLrbgeI&X-Amz-Signature=6b32bdddc8b79936190b1adb80ff14ee6a21d71c49a3d0556baac2caba6ca80e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3TCJOAS%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T130450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD56bY9%2FEyX9ddfbKJlyslwTQVXCyq6DHEq0G2ZCL7O3QIgY%2BN%2BecI4i2SDeAVbUgtL47%2FG7wGd54Jlg5R2WNnhDpUqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzWlMP%2BcgsZtskenyrcA7Za1Q%2BUnyCgXBQCcuDOEsdxMEg2oz5aWIrgJjr%2FnvU8AS2PEjc3wUjTX6DbV8PHPccZJ7g0nMCPVDFQYlZX9cUw%2BSJq%2F0yvG3fBATsVpzxNuAW3y%2BJWkrUu53f4Fx8T7YBKRdaImNUiJeoEyFj807%2BqgYx8Z9AJ291proznSQ0nsMVnjazbijVXyfYqNXmHJtZvH5Ven43BXK9tEECYDPQdgWCs4snptZWEWefj%2F0A%2F7MYjfC1BLofJXoLR8K7IGUyco99yHl0Gp8esfPFpmYsa9qoDLutDYKEs7WoL7dyVPb6aN%2Bq1BZZqcRCnHdZHokvZIjW6d1rmpJER2S%2BrjFkOdF%2FFzDrCvyWFX1StUXc7me%2FcUr14pISWnFr7%2BtVUvcc%2Ft3Lc7%2BPb3C0P9vvG832Zmsw6Zb8N6hupSBYM9EFTtbFIfcg%2BOqTd1Y0eOCsm7sk%2FMVWugteOMEQwX9gmTXt8BE5tTr%2Fgu2IRsFVO4teBdbDCfzYc0G56Sh%2B82PQUYPaXLiKIeVaAStbREpVD5JFCSSuRR1SL2yqDiUIU1Vz6EmZcFDrAUyUDa%2FNtW7Mbc2u3W9l1%2FL6FnRHmkRaRb%2FqBSQXDsO71Oa1%2Fk8kXSsVq6HDvpqBQlKvfZ8tOMJCMkNEGOqUBu2rSqnHdTEWra6HGMD0XT1HJgpow1sea7ucOCfPllkASCtPlJ38uDTDKgVTeQ4gX%2BvYrWF0Lp77%2FsjgqWyNObar5568PR5ckSp9BZpGdIKY2LELLFOGMyjxCTk9M1xoRje1fKPhkmVhhi7hmFB7GMZwLiQKP%2ByWjMRcUkQF%2FAEX5EH3oSl%2BH0LpXByPWdNVMUHQtA16RlbQMuaRE4eMJyOLrbgeI&X-Amz-Signature=f68bbde668ae845285b7451cf874404a228dcdb1d743aa7c55e3d50788f94558&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
