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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T4HTVUG%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T152036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDE2yqj9mFmXE%2F2isqDgDAfPsLlqq%2BkNCejcgI0drqzJAIhAJbRBgj2kETxEs7raGKC9fvw4xgwXUsXV2SbhFL1LOFAKv8DCC8QABoMNjM3NDIzMTgzODA1Igxe%2F%2BfJxTvyrLseREgq3APCFZ2PAImR474nulpU2y5V7cyIAcp27O5nxE4s%2F8fq%2FWo11levLYV%2BuQMiDwxvIYe7%2FSicqTmWe6y%2F0FuzYXwCkURjw8lLT%2FfV8F9UiNYELZ4x%2Bn6YHkk3srCMet8ltbfAwQqaJtsuvIMQK%2F54CWkv%2Fb%2FPjXHdC6%2BVfGwe1se5aZBfDc5d%2F%2BXpZGOj4jg6%2Fv2W7JZCmhKG9%2BJOlZcSFIYXjxDkK8FN4zXYMsqoDWRk1XTWiFGNvfLjVwbW03qya36XjhFdWCHQ2f%2Fqamej5eq5wM2GXVVRd6WN2CdjQvLIl6oiNlY%2BWwywnZIGJUyMYJxC9Y5x8GVsh7G3P%2BXYoERogEtdC55wkBHBY8tv8bH3yFUZuUJcr%2FctMEZgt29HZI5V7QMZV4pVefnbkfqQVPMHlQZw%2FNeBp8XJltcsPZn7WtBgRHRaiIs11q%2BC19GzxuF9%2FRmH8P%2B21ctpE74U%2FHgDbcLNwCq9X2JFCXhLsKFYnfcRwDUdx%2BzfIaPoLXHi9zDJSZDWGl%2B6i4Exwj7lR9t6JwTcNTRmcZcOBLjMYbPucYTGfXcwhdTOQLX%2BHCVPzt6eQulKLuVhWFXs2JmFONvGGxvCm3PiRiliXUAI7oEzFneXlIJP8MPSbfJNJDCDq97SBjqkAZotgnCdiZLypMgIWzlFPNTKMTqRwj6DpUNVc4VzIOOQjgCFh%2F6OxeoGJJeunb4CgborGBwu%2BIMNaOTjy9yse94dPs2mnQcUtvCivrhGVz4FeIodudOmf8PLVrLTQdv8KdQPwIPC5Q6RqKM4swL5Rjxj3r%2BzKi0K4w2CEX%2FoPaMu95iFpLXr3uCZg%2BgHnTmpJDkVIYoMhpB0SCkAm2SihrKByEQT&X-Amz-Signature=4ad99c3d8120a594d48835816aa6b63e920a0c1295399584f190020b809ed9a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T4HTVUG%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T152036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDE2yqj9mFmXE%2F2isqDgDAfPsLlqq%2BkNCejcgI0drqzJAIhAJbRBgj2kETxEs7raGKC9fvw4xgwXUsXV2SbhFL1LOFAKv8DCC8QABoMNjM3NDIzMTgzODA1Igxe%2F%2BfJxTvyrLseREgq3APCFZ2PAImR474nulpU2y5V7cyIAcp27O5nxE4s%2F8fq%2FWo11levLYV%2BuQMiDwxvIYe7%2FSicqTmWe6y%2F0FuzYXwCkURjw8lLT%2FfV8F9UiNYELZ4x%2Bn6YHkk3srCMet8ltbfAwQqaJtsuvIMQK%2F54CWkv%2Fb%2FPjXHdC6%2BVfGwe1se5aZBfDc5d%2F%2BXpZGOj4jg6%2Fv2W7JZCmhKG9%2BJOlZcSFIYXjxDkK8FN4zXYMsqoDWRk1XTWiFGNvfLjVwbW03qya36XjhFdWCHQ2f%2Fqamej5eq5wM2GXVVRd6WN2CdjQvLIl6oiNlY%2BWwywnZIGJUyMYJxC9Y5x8GVsh7G3P%2BXYoERogEtdC55wkBHBY8tv8bH3yFUZuUJcr%2FctMEZgt29HZI5V7QMZV4pVefnbkfqQVPMHlQZw%2FNeBp8XJltcsPZn7WtBgRHRaiIs11q%2BC19GzxuF9%2FRmH8P%2B21ctpE74U%2FHgDbcLNwCq9X2JFCXhLsKFYnfcRwDUdx%2BzfIaPoLXHi9zDJSZDWGl%2B6i4Exwj7lR9t6JwTcNTRmcZcOBLjMYbPucYTGfXcwhdTOQLX%2BHCVPzt6eQulKLuVhWFXs2JmFONvGGxvCm3PiRiliXUAI7oEzFneXlIJP8MPSbfJNJDCDq97SBjqkAZotgnCdiZLypMgIWzlFPNTKMTqRwj6DpUNVc4VzIOOQjgCFh%2F6OxeoGJJeunb4CgborGBwu%2BIMNaOTjy9yse94dPs2mnQcUtvCivrhGVz4FeIodudOmf8PLVrLTQdv8KdQPwIPC5Q6RqKM4swL5Rjxj3r%2BzKi0K4w2CEX%2FoPaMu95iFpLXr3uCZg%2BgHnTmpJDkVIYoMhpB0SCkAm2SihrKByEQT&X-Amz-Signature=710b2ee400ca4998cedf4f7fcff5e9464eb32879a1d71979206c339418b08ece&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
