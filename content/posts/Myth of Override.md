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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S7PLBNZ%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T182555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCVzDRedYt9OWG%2BHbGU%2Fa%2FQdQGnmJnkJwvwfpH%2FF5UACQIhAKA9LvTVWoihakMitQXAYLgirALM8Uz%2FmByO4y1QvAYNKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BE7VQhAYai48y8DUq3ANiKYBy3mCeQkmH5wrDgxUvkkSzhU9yfl8PFy%2BuIpZnRz6BYtJoN0Y3raWi4%2FHl%2Bld8xolP%2BY%2F0k%2Fyjz%2Ftzgr0zN%2BV7M6gtqre25On%2BBXzFAldh2m%2FBht857DOzwT8yMG85nk1Cq%2FSpi6oZji9LH7mImDFT6ioKL7Q5lwoesQ8tm8HEqSnD5q8LDoL8HG6tJA%2BynfxXYpVXZxYqUG77d5eWwdyQekZmOeekB96JqMWULWP1cU80R96GnbICPO9xndWnfCNmikP9OrpmYE0bWrRw1pk0DltnrctSx9GhEtH3kVHw0IEAlVQOmOoFlD8qGMgyIcmp%2BKYMZz9ekvUg%2B5a7jYpXygM6dP3CveqYClR7KrcjAIfD0R5sErE0aVsGEwlbZ2dBD46i7zGEM3GXSkrvPb%2Fl5qv9Z0UNul%2BgltNQkvmSFHyW3pze8tTHkamqQmif1yZB%2BpEx1JIiTn3zzbibp5byTF8%2BOkebeT22v8kBrodyzwcaUS%2FuapUJvTp89c0l3FHcbfIAKjP3c%2BZKk9%2Fhx7fkPhNkLdxLpa6QswTSwV9ZTa87BXycNmsdOUXE5Xi8mEfV8xh5y%2BNPl0bwihRhwzDnN9QBb5TyF%2FgsgIa9Y%2F680abCQP2VbSvmGjDTgLLUBjqkAVuBSY%2BQUrGIpTpUGnxcfV8ldtGyBpHZ3R1s3EGuOsTW2ikBGMWFmCVk6%2FropJoMxLBbWiI5TF0W3LdF22WwXoRLbYS7WMoeoNtJP5TQKgNmjjAnVCBiZJiBxNi9mAxxSDWrrjpBeOR8LqF%2FyB9dZ%2FIYiSkvHXhA6b2mpf8wzsZLWokJErsQkI8BO76QYJ0eo1scY%2FQ0xLjPz04GJCT%2BnWCID%2Fz6&X-Amz-Signature=4dcbac224b70366dc609b2c4b23c3f05764ce7ace0237ca480a7841eb5a7ae28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S7PLBNZ%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T182555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCVzDRedYt9OWG%2BHbGU%2Fa%2FQdQGnmJnkJwvwfpH%2FF5UACQIhAKA9LvTVWoihakMitQXAYLgirALM8Uz%2FmByO4y1QvAYNKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2BE7VQhAYai48y8DUq3ANiKYBy3mCeQkmH5wrDgxUvkkSzhU9yfl8PFy%2BuIpZnRz6BYtJoN0Y3raWi4%2FHl%2Bld8xolP%2BY%2F0k%2Fyjz%2Ftzgr0zN%2BV7M6gtqre25On%2BBXzFAldh2m%2FBht857DOzwT8yMG85nk1Cq%2FSpi6oZji9LH7mImDFT6ioKL7Q5lwoesQ8tm8HEqSnD5q8LDoL8HG6tJA%2BynfxXYpVXZxYqUG77d5eWwdyQekZmOeekB96JqMWULWP1cU80R96GnbICPO9xndWnfCNmikP9OrpmYE0bWrRw1pk0DltnrctSx9GhEtH3kVHw0IEAlVQOmOoFlD8qGMgyIcmp%2BKYMZz9ekvUg%2B5a7jYpXygM6dP3CveqYClR7KrcjAIfD0R5sErE0aVsGEwlbZ2dBD46i7zGEM3GXSkrvPb%2Fl5qv9Z0UNul%2BgltNQkvmSFHyW3pze8tTHkamqQmif1yZB%2BpEx1JIiTn3zzbibp5byTF8%2BOkebeT22v8kBrodyzwcaUS%2FuapUJvTp89c0l3FHcbfIAKjP3c%2BZKk9%2Fhx7fkPhNkLdxLpa6QswTSwV9ZTa87BXycNmsdOUXE5Xi8mEfV8xh5y%2BNPl0bwihRhwzDnN9QBb5TyF%2FgsgIa9Y%2F680abCQP2VbSvmGjDTgLLUBjqkAVuBSY%2BQUrGIpTpUGnxcfV8ldtGyBpHZ3R1s3EGuOsTW2ikBGMWFmCVk6%2FropJoMxLBbWiI5TF0W3LdF22WwXoRLbYS7WMoeoNtJP5TQKgNmjjAnVCBiZJiBxNi9mAxxSDWrrjpBeOR8LqF%2FyB9dZ%2FIYiSkvHXhA6b2mpf8wzsZLWokJErsQkI8BO76QYJ0eo1scY%2FQ0xLjPz04GJCT%2BnWCID%2Fz6&X-Amz-Signature=23adf62b1bb4204c737e3b910017bfdd466fb0f912e0f45b17637d74d2686440&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
