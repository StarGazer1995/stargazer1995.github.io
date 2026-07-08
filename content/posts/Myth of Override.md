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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGLWDSHK%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T045719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO6zQEKmlg14s6h%2FfPk3rwZb%2Fy13UpVti1MX%2BWHDd56gIhAJEzlvnqxH%2FJbPf1U3JXRiIveLQXfC6io7BN1vVVsTLNKv8DCH0QABoMNjM3NDIzMTgzODA1IgxXBS1FMSKQbg%2FTRnIq3AN8%2BryO%2F4OxRRzSkE%2FHSElVLSeE9j7FO39dRby4Q%2Fg%2FSXkdVs2%2Fn0tn12QzNGwvTnuo5mcFA590kuOfJpGKXGBrXrXE5ir0A1s%2BOcIWyYyB1cpilnCermDUOxN6rzJb4woxMLUwNqEC9XXZQHJmlKhbDdhoNGc4DEaHzzq6w61bnJ89ll49PTorZvVY5sxDx6n9dKkF1yKK6H0dCAQndZt%2FRF1BmzmNHlG8uNCZ3o9weBY5WgMuX%2Bpbsu7jHQa0uFMXfnqM3ZCrJooG4fbfXR%2BzEmOR1lOw%2BNnl2QjGgEKN9RncYBROne%2FJ4SfNyzbnKRB7gJe1BKGWcK%2BuuJvlU%2FfzMOVllNZtF3bTayWheeP3aqIwDDzWiv9Fmgf7iPL3CkrLwIc6AihhTHkpfqAQfNsOITPWsOsdVlaeiMXu90kMjSTW8pTjKYl%2B%2BKf53SVKoPaKT6ODGTb%2Fo3odHWolHsJ0yiv8YNNIp%2BIrYml0JrenVRJ%2BH%2BOJg6phHklIfbSwtGb1mNFiqK6eHnZc0Y7tHuTwHmFJMBcVztbA%2Fump3YGX0H84Guer%2Fy%2BXi4pyKVqzx3CBncjrwk8ZDTUDut0POdOQFrWOJSdM3grVTdqhb92Du6QhkbwGFrqbOTo4iDCNnbfSBjqkAfK76mTkQUEL7hW2kq4Ny3i5lCT9m9ITWB4fBZGObp8LToZ2cMJev0WAcxAiBJAH7pSiSQ4cOIsp7%2FoKT49xdZPrwEgAQoT7jTBzLbxnlH4n4JWmXg6mNm869%2Bs0cGfuFDOxjv%2FMJVqrWcNLHXyuApHaJ0dMw1RMOnMQ%2BHuURW5XdsajXwU9Ec5Iry5bpz%2BYZBjWhNMTzfr%2BgcH9TE9ppDMPjKaO&X-Amz-Signature=7c16fbb57e30fd2762581b806808c64dda2225a0595204d08dafd7477ee65049&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGLWDSHK%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T045719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO6zQEKmlg14s6h%2FfPk3rwZb%2Fy13UpVti1MX%2BWHDd56gIhAJEzlvnqxH%2FJbPf1U3JXRiIveLQXfC6io7BN1vVVsTLNKv8DCH0QABoMNjM3NDIzMTgzODA1IgxXBS1FMSKQbg%2FTRnIq3AN8%2BryO%2F4OxRRzSkE%2FHSElVLSeE9j7FO39dRby4Q%2Fg%2FSXkdVs2%2Fn0tn12QzNGwvTnuo5mcFA590kuOfJpGKXGBrXrXE5ir0A1s%2BOcIWyYyB1cpilnCermDUOxN6rzJb4woxMLUwNqEC9XXZQHJmlKhbDdhoNGc4DEaHzzq6w61bnJ89ll49PTorZvVY5sxDx6n9dKkF1yKK6H0dCAQndZt%2FRF1BmzmNHlG8uNCZ3o9weBY5WgMuX%2Bpbsu7jHQa0uFMXfnqM3ZCrJooG4fbfXR%2BzEmOR1lOw%2BNnl2QjGgEKN9RncYBROne%2FJ4SfNyzbnKRB7gJe1BKGWcK%2BuuJvlU%2FfzMOVllNZtF3bTayWheeP3aqIwDDzWiv9Fmgf7iPL3CkrLwIc6AihhTHkpfqAQfNsOITPWsOsdVlaeiMXu90kMjSTW8pTjKYl%2B%2BKf53SVKoPaKT6ODGTb%2Fo3odHWolHsJ0yiv8YNNIp%2BIrYml0JrenVRJ%2BH%2BOJg6phHklIfbSwtGb1mNFiqK6eHnZc0Y7tHuTwHmFJMBcVztbA%2Fump3YGX0H84Guer%2Fy%2BXi4pyKVqzx3CBncjrwk8ZDTUDut0POdOQFrWOJSdM3grVTdqhb92Du6QhkbwGFrqbOTo4iDCNnbfSBjqkAfK76mTkQUEL7hW2kq4Ny3i5lCT9m9ITWB4fBZGObp8LToZ2cMJev0WAcxAiBJAH7pSiSQ4cOIsp7%2FoKT49xdZPrwEgAQoT7jTBzLbxnlH4n4JWmXg6mNm869%2Bs0cGfuFDOxjv%2FMJVqrWcNLHXyuApHaJ0dMw1RMOnMQ%2BHuURW5XdsajXwU9Ec5Iry5bpz%2BYZBjWhNMTzfr%2BgcH9TE9ppDMPjKaO&X-Amz-Signature=010d873ead09436122e20f34a2d86c8f0b1980da2284ff47f65f6be1083ef1eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
