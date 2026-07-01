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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627HAOKJM%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T192808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHaYOibfwwryQe8W0jLfYLQZkeN4XeYkwT5bhWqpgJiUAiEAtwjqKm0lL5Rgno7TOINhF%2Fs5fPI025nzVR3L1MVVSHcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHAqQXjyv6yoJCKwHSrcA4ymU%2F6LtHiUbBkhaaN%2FT2iyMpO7PoVR8IFqtE3%2FGUvNi2ir5vUrzS%2FlZ0XmKHPUThpaPfYTT6a1DNw%2BkAOL39YJPdDBVfSBWm2Vj0R4eGoilMV8pcSz%2BenVhMUSz1piq2klp7yanzofRsrqWlUu448BV%2FMFsrGMy%2FyK6Xe6GllvV79xGHghFeqLSWz3teExEIKGDZ4YytBgOe7Eja06ZYHDADhK858kIelxSG6BI9cPO0KF9SL%2F%2F8G5h8eZ%2B7fANhI235ZoOW6nBoouYsjBFmeMpyJSEIL9Fe8nF6ElYa%2FAPlZ5ogFG0Cc3kXW27Hm1oE16l433DEoV7kGG1nlhjO4esB3WRO8hIg%2FbbRCmmHuW74OY5d405KrF6a52ScPwXims0wz6rRXmSvp%2BQrNe1izEgmrqNqOVGq%2BxV3P9S8%2FS86wLNeab5S6Gq9MxgeTPTet0zOzQ%2BNlw1mBjJsE%2BJujeWmzw0V%2BfUtNoktnslNN3Zb7Rzs5yK6cc%2F7xKOnWxzqtEYnzAOdzb8YYDc57bvUxOqcC9oxVqjyG8pF3RnoWJ5nr5j%2BtkovY9lTAUJIRm9sj1CvYJrP%2Bqin3CoyVkV%2BM%2FtbBMXF4uQYutGGKCYTBr9IG34y4Q8jaM2w6RMPq8ldIGOqUBOCjyo%2FO2VIyhuXMjqe6lWGcdQnHxPa3FJ0PgNovEZzErfJMnGFfQM02g%2Fhk9r4lrqqkNoj8bhUK8Pfg1MLOmxidl%2FoFbMCfFp7cqFgRjzopGOMzUd%2BMfE991YgZjhBHLZ8XoHa0QmjVtS2k2rJyAGq345Yn8W9%2BM4AullKty%2FYsTrJbJvsNr5M5CUVJKWHJKbqQql%2BqGmu0Asd%2BY4U0nJ4tc9nOy&X-Amz-Signature=a4b6b7ee8e0d5937c8ddbaac382c91328ed57db2c35d582bb4c3ff6c90f9dbcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627HAOKJM%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T192808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHaYOibfwwryQe8W0jLfYLQZkeN4XeYkwT5bhWqpgJiUAiEAtwjqKm0lL5Rgno7TOINhF%2Fs5fPI025nzVR3L1MVVSHcqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHAqQXjyv6yoJCKwHSrcA4ymU%2F6LtHiUbBkhaaN%2FT2iyMpO7PoVR8IFqtE3%2FGUvNi2ir5vUrzS%2FlZ0XmKHPUThpaPfYTT6a1DNw%2BkAOL39YJPdDBVfSBWm2Vj0R4eGoilMV8pcSz%2BenVhMUSz1piq2klp7yanzofRsrqWlUu448BV%2FMFsrGMy%2FyK6Xe6GllvV79xGHghFeqLSWz3teExEIKGDZ4YytBgOe7Eja06ZYHDADhK858kIelxSG6BI9cPO0KF9SL%2F%2F8G5h8eZ%2B7fANhI235ZoOW6nBoouYsjBFmeMpyJSEIL9Fe8nF6ElYa%2FAPlZ5ogFG0Cc3kXW27Hm1oE16l433DEoV7kGG1nlhjO4esB3WRO8hIg%2FbbRCmmHuW74OY5d405KrF6a52ScPwXims0wz6rRXmSvp%2BQrNe1izEgmrqNqOVGq%2BxV3P9S8%2FS86wLNeab5S6Gq9MxgeTPTet0zOzQ%2BNlw1mBjJsE%2BJujeWmzw0V%2BfUtNoktnslNN3Zb7Rzs5yK6cc%2F7xKOnWxzqtEYnzAOdzb8YYDc57bvUxOqcC9oxVqjyG8pF3RnoWJ5nr5j%2BtkovY9lTAUJIRm9sj1CvYJrP%2Bqin3CoyVkV%2BM%2FtbBMXF4uQYutGGKCYTBr9IG34y4Q8jaM2w6RMPq8ldIGOqUBOCjyo%2FO2VIyhuXMjqe6lWGcdQnHxPa3FJ0PgNovEZzErfJMnGFfQM02g%2Fhk9r4lrqqkNoj8bhUK8Pfg1MLOmxidl%2FoFbMCfFp7cqFgRjzopGOMzUd%2BMfE991YgZjhBHLZ8XoHa0QmjVtS2k2rJyAGq345Yn8W9%2BM4AullKty%2FYsTrJbJvsNr5M5CUVJKWHJKbqQql%2BqGmu0Asd%2BY4U0nJ4tc9nOy&X-Amz-Signature=2a7f587fa600e8761c7158071a94722968eb25c9369758ede02c9e2f40091816&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
