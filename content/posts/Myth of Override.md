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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MGYJ37V%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T173947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIGxRxwJSfyMYrFI%2FCIrOLNwxmq93hhjRYzPTx4uaCU4jAiA%2BljueZ4SxdhEX%2BkJ9%2BpgRrqndu78LljsavoHbLFOqeSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMkVVkjjn1SEDHbf2fKtwDEO9Dx7TJ7tPABvX7vs37uqfWIvjiNQBbGtMzCCH859isAJjIeJoj7sQ%2FBqcFt9lSqfrm1%2ByqXHT%2BxOmuvOccpZm6BJOcAASBw3WyyHZAUxzYtFIsvMSztiBV4r0iRqnJRK32ibvc%2BZfeMyxNsT4r7GuIR8polsAkZCFH35XdAvp8JDN%2BryIBzhk3SgzB3MiKkYDfuijXO6mxZ7mf5V6%2FxtpHOnt9zFyZ%2F3NkvsQYCaEBV5cw8Cx5vlh%2FbB7UOs%2BL5Xqbs53r5D%2BVBCQ0QtDB43bEig4b9yq2LtqB7p7Wuz5Xue9tH2JHRS8YjyVGlQcIvfUA6cr7q0s0WVfR7Mf6ohR7o%2BmrJUS10yFPPvYZ0USnjEL1GDlzOn4yeyYtziYIGFpNv%2BbSZER2ZjN0%2Bm37EhN%2Bc%2FU6%2BaFKWOBbzVwAkemp6bb8%2FgI3mcYn8RBqscYOd6eZqaaU%2BBuZ1tRk7ekFWpel0jzVzLeKF8ZfS%2BkRL9smiceHaCGjwGyHYxdcfu2UqosxO%2F1IzLUSnzzRscPVjsd%2FCiGsasulbgivotmHbMQvSwM2H7N2JPAYC%2FCqBCoroAFf3LiZsL%2FoHr9TtO5uz3lokwPvV8G%2FFlT5itia6CDEQ5Tj5nIeMVV66vEwl7Kk1gY6pgEgzE5EZQ7qF5lEibxIY%2BZMlRp8ZS5CM8HvOUo%2Bt59WYApgmuz8NcNH0oz1xU50BRnMzHB7BXLCyujjCh1N4crYftmjH9YFEQur5ZHX7iyGCkwKm9GsRPkI0V9P4JADWhhrCz7NH8ps2SFU%2B7wALkrvuKNBhDYYwz7HWWTM9jCXGlVob%2FZXScakZPhc%2BXQzdy1%2F5jtWttETr3p47oeGyqF%2BIBTV80fo&X-Amz-Signature=66f1ee7ad7648a7abfb254fce9ed58239c2b491fa28702f45ba9024d2484aba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MGYJ37V%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T173947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIGxRxwJSfyMYrFI%2FCIrOLNwxmq93hhjRYzPTx4uaCU4jAiA%2BljueZ4SxdhEX%2BkJ9%2BpgRrqndu78LljsavoHbLFOqeSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMkVVkjjn1SEDHbf2fKtwDEO9Dx7TJ7tPABvX7vs37uqfWIvjiNQBbGtMzCCH859isAJjIeJoj7sQ%2FBqcFt9lSqfrm1%2ByqXHT%2BxOmuvOccpZm6BJOcAASBw3WyyHZAUxzYtFIsvMSztiBV4r0iRqnJRK32ibvc%2BZfeMyxNsT4r7GuIR8polsAkZCFH35XdAvp8JDN%2BryIBzhk3SgzB3MiKkYDfuijXO6mxZ7mf5V6%2FxtpHOnt9zFyZ%2F3NkvsQYCaEBV5cw8Cx5vlh%2FbB7UOs%2BL5Xqbs53r5D%2BVBCQ0QtDB43bEig4b9yq2LtqB7p7Wuz5Xue9tH2JHRS8YjyVGlQcIvfUA6cr7q0s0WVfR7Mf6ohR7o%2BmrJUS10yFPPvYZ0USnjEL1GDlzOn4yeyYtziYIGFpNv%2BbSZER2ZjN0%2Bm37EhN%2Bc%2FU6%2BaFKWOBbzVwAkemp6bb8%2FgI3mcYn8RBqscYOd6eZqaaU%2BBuZ1tRk7ekFWpel0jzVzLeKF8ZfS%2BkRL9smiceHaCGjwGyHYxdcfu2UqosxO%2F1IzLUSnzzRscPVjsd%2FCiGsasulbgivotmHbMQvSwM2H7N2JPAYC%2FCqBCoroAFf3LiZsL%2FoHr9TtO5uz3lokwPvV8G%2FFlT5itia6CDEQ5Tj5nIeMVV66vEwl7Kk1gY6pgEgzE5EZQ7qF5lEibxIY%2BZMlRp8ZS5CM8HvOUo%2Bt59WYApgmuz8NcNH0oz1xU50BRnMzHB7BXLCyujjCh1N4crYftmjH9YFEQur5ZHX7iyGCkwKm9GsRPkI0V9P4JADWhhrCz7NH8ps2SFU%2B7wALkrvuKNBhDYYwz7HWWTM9jCXGlVob%2FZXScakZPhc%2BXQzdy1%2F5jtWttETr3p47oeGyqF%2BIBTV80fo&X-Amz-Signature=05a6189008f31f6d6b7b2ec51be4a9ec9ba424f3e7d16ba877012946f34b173f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
