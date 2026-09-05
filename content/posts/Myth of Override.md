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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLUEYSRD%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T214626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJIMEYCIQDofARZCef7CJ0v3jB262qMzbm1V8OekNlFlYOZKpcy1gIhAPzvESyWkb1lbQI132aPaieXnWno1CbEZKgDZH%2FJFbMbKv8DCBUQABoMNjM3NDIzMTgzODA1IgzvEz%2Fm7Z4I986Qgcwq3ANwNbi44wg6LTWFkezMFTFVOll3VUKsXheTmmgGIGtA4f38gLmv15pHozpYHTOj3xUz4n8%2FimikmmjwgiHGTzzAUpUU0GvVpR%2B8wgWmkZ6dYFCNZqhWN%2FEEhA34wYTStsZvc%2FkxzfUC7M5Md%2FDC3UdnZ8B%2BHpVP3MesnXoQtA8prbQaeUJ3eJ5AHnWDQtozuNPtCYLbCVE%2FoZxYjDGyiyAiMWsmzvjfGfHnHKyF5%2FYJw%2BURVZtpjsuWgX2olEi8np6AGh3GkYRhN%2F82%2B904tqJ24ccFk9UachaGbKqJYlHVpI2jxi%2F9PbNaI8OV%2FccxDh2WGnxueHgFfDalbB%2FYo9Lu%2FKye0HARJIP2bIzW4JGybyA08QtQuFFX3iZpLZvb1lmFQlKH568QoLU64YcEp1v7vbxIR1C82ELMhDKcsHtFetbw3Qt8TRsVR%2BoSYCsILeAH8Z%2FicL9oVWGHT35lZE4Ei2T5s%2FDgEjkAKxByp9GwbQ7U2RHUlFKa4xGUyH%2BWOSU6VLo1W49dVm35EKQF6YQN8FNyJ0W9tIH9BA1LOtRe5H4U0gJkIh5LO65ubJEfS3gsWZGGqfG0dukL2LSyk6BXn1kYR6JXQXblKij%2FwRrN6LmJ8oE7f81ffiT8ZzDh6PHUBjqkAWwiRKsTPynUhGFr5wCue6%2BlsL7aC4ekTZGHw3yYzqQWvh0ZFWwCXlxqRH3MTR5mLerKvmnVjolOk75Owh6Yxp8ThRImnURxUKkVN5McrBHEXysQRqm2yylNzUrnjSr3iVg%2FIedpwIk3lHcuxNvKpz9qkESd7vi3F0wFl4jfGFbE8NuRE%2FPbi%2F471FPKTSvQn0oKLumQvm9pNY9HghdMthAU9j82&X-Amz-Signature=8088083c215535eda792c93cea3eab12b2b1c3652fc8a265c0e9993ca9712b0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLUEYSRD%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T214626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJIMEYCIQDofARZCef7CJ0v3jB262qMzbm1V8OekNlFlYOZKpcy1gIhAPzvESyWkb1lbQI132aPaieXnWno1CbEZKgDZH%2FJFbMbKv8DCBUQABoMNjM3NDIzMTgzODA1IgzvEz%2Fm7Z4I986Qgcwq3ANwNbi44wg6LTWFkezMFTFVOll3VUKsXheTmmgGIGtA4f38gLmv15pHozpYHTOj3xUz4n8%2FimikmmjwgiHGTzzAUpUU0GvVpR%2B8wgWmkZ6dYFCNZqhWN%2FEEhA34wYTStsZvc%2FkxzfUC7M5Md%2FDC3UdnZ8B%2BHpVP3MesnXoQtA8prbQaeUJ3eJ5AHnWDQtozuNPtCYLbCVE%2FoZxYjDGyiyAiMWsmzvjfGfHnHKyF5%2FYJw%2BURVZtpjsuWgX2olEi8np6AGh3GkYRhN%2F82%2B904tqJ24ccFk9UachaGbKqJYlHVpI2jxi%2F9PbNaI8OV%2FccxDh2WGnxueHgFfDalbB%2FYo9Lu%2FKye0HARJIP2bIzW4JGybyA08QtQuFFX3iZpLZvb1lmFQlKH568QoLU64YcEp1v7vbxIR1C82ELMhDKcsHtFetbw3Qt8TRsVR%2BoSYCsILeAH8Z%2FicL9oVWGHT35lZE4Ei2T5s%2FDgEjkAKxByp9GwbQ7U2RHUlFKa4xGUyH%2BWOSU6VLo1W49dVm35EKQF6YQN8FNyJ0W9tIH9BA1LOtRe5H4U0gJkIh5LO65ubJEfS3gsWZGGqfG0dukL2LSyk6BXn1kYR6JXQXblKij%2FwRrN6LmJ8oE7f81ffiT8ZzDh6PHUBjqkAWwiRKsTPynUhGFr5wCue6%2BlsL7aC4ekTZGHw3yYzqQWvh0ZFWwCXlxqRH3MTR5mLerKvmnVjolOk75Owh6Yxp8ThRImnURxUKkVN5McrBHEXysQRqm2yylNzUrnjSr3iVg%2FIedpwIk3lHcuxNvKpz9qkESd7vi3F0wFl4jfGFbE8NuRE%2FPbi%2F471FPKTSvQn0oKLumQvm9pNY9HghdMthAU9j82&X-Amz-Signature=d83a847ba9a3fc8216adb011ce6e7e918a8efa1bc797470996e07ffb87b8f414&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
