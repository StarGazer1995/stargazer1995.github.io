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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672YLR6SZ%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T012912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIFm8CBjRbtbu%2BlqEd8UGpUiaQ8n73RApit4SYih6sVG5AiBJIhcLfyX12hQvDwaMGqyHkXkatMDl3vaN7KhQv%2FsQeSqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMswqZJ2pdNOOlwspVKtwDmJr4xT8HZTNoBH%2BHW5d%2F6RKp4BQw%2B9eGBhlf5dKC5yAGKniJLURYE8%2F5%2FiRw%2FjEpILCF4ppSSyaHF2rbgTiRE4Wxtdadx5SuIAffbwVQthcyppNBmMTux2YBSxVsBjYXWofwxCsEQ2WzhX2Ve%2FEk4i2x0T6HPuDZqBRM9NlFubexLRe%2FQxQOTHjIEUztIrD44u3L9CvOe9TQu9h7N%2FH4LRJ0yBAm7Wkv4v69u4bP%2Bzri9QGAEQsz5gizt7fOSiAiIdBtNElcOWoQxY2P1%2F83CQ%2B55tivFdaI9LisfgLzzOjIjlqhHx%2BU49EduqBuUlSubvzWyVjjKHHJvIrgIafiOlK2LQWAkdX%2FHYhZuG8YBnvN6naBxSsjRqPmYLHRlL4ll%2FyC%2B7xOLigVuAznaIrRrIKnHzeEf1%2FiX%2Bswl773L44u6x4CpXO4zBGEjtZgy1mB0%2FGPntSG7LZxR%2FtQcat65Yx%2Fzl17cIRTGnx1jpQN0NGcJHn596ArPRiKOIwP3Ne9v0RglSsagkS8bflV6xi032zmaqVCdYAUUF36pPRgCn3eU%2BmKFIpMMN8Nn4p0oYg1B97F4KXplqp7FP%2Bm40ZnUl1tRZxob84HhgBWcjeNqZrZrQAxRRTptWpQo7Uw8r6E0wY6pgH%2F9unZUnHXmOsrSZL5XTEkyv6JYe7U5IU2OYJYXvNZ9WpZB9rmGoEchBM9nCaNTkpL5Db0GBhAEjCaMoXS6HL4Zy3WO%2FABJprglsgP5FkdM5WA6SkQhJy3OkPwW95wYESVqEZJrZdVMAytfNfYMZtYWO%2Bt%2FvZEHu0bAweXp9MHvqisu%2BRkPVXRDXG6uNpEC704VOo1aoi3%2FKPjC8gAVm2P01Yyks%2BL&X-Amz-Signature=2fb3ab9bb2d078d4c14335feb72df2081f59823801b6b87b708a05d1d4541512&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672YLR6SZ%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T012912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIFm8CBjRbtbu%2BlqEd8UGpUiaQ8n73RApit4SYih6sVG5AiBJIhcLfyX12hQvDwaMGqyHkXkatMDl3vaN7KhQv%2FsQeSqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMswqZJ2pdNOOlwspVKtwDmJr4xT8HZTNoBH%2BHW5d%2F6RKp4BQw%2B9eGBhlf5dKC5yAGKniJLURYE8%2F5%2FiRw%2FjEpILCF4ppSSyaHF2rbgTiRE4Wxtdadx5SuIAffbwVQthcyppNBmMTux2YBSxVsBjYXWofwxCsEQ2WzhX2Ve%2FEk4i2x0T6HPuDZqBRM9NlFubexLRe%2FQxQOTHjIEUztIrD44u3L9CvOe9TQu9h7N%2FH4LRJ0yBAm7Wkv4v69u4bP%2Bzri9QGAEQsz5gizt7fOSiAiIdBtNElcOWoQxY2P1%2F83CQ%2B55tivFdaI9LisfgLzzOjIjlqhHx%2BU49EduqBuUlSubvzWyVjjKHHJvIrgIafiOlK2LQWAkdX%2FHYhZuG8YBnvN6naBxSsjRqPmYLHRlL4ll%2FyC%2B7xOLigVuAznaIrRrIKnHzeEf1%2FiX%2Bswl773L44u6x4CpXO4zBGEjtZgy1mB0%2FGPntSG7LZxR%2FtQcat65Yx%2Fzl17cIRTGnx1jpQN0NGcJHn596ArPRiKOIwP3Ne9v0RglSsagkS8bflV6xi032zmaqVCdYAUUF36pPRgCn3eU%2BmKFIpMMN8Nn4p0oYg1B97F4KXplqp7FP%2Bm40ZnUl1tRZxob84HhgBWcjeNqZrZrQAxRRTptWpQo7Uw8r6E0wY6pgH%2F9unZUnHXmOsrSZL5XTEkyv6JYe7U5IU2OYJYXvNZ9WpZB9rmGoEchBM9nCaNTkpL5Db0GBhAEjCaMoXS6HL4Zy3WO%2FABJprglsgP5FkdM5WA6SkQhJy3OkPwW95wYESVqEZJrZdVMAytfNfYMZtYWO%2Bt%2FvZEHu0bAweXp9MHvqisu%2BRkPVXRDXG6uNpEC704VOo1aoi3%2FKPjC8gAVm2P01Yyks%2BL&X-Amz-Signature=0b0b1231c7168f885e016b2303a9ba2fd02635ca78e256bf9a44199a070ec4a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
