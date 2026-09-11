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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDTUUKOA%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T014653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVIlhzot9q%2FMmszn7fCOULUvRlqVNlM0MlMAwK4EdORgIgCXSnvCxDyA1Z%2B4F0wjLvLhgX5FH2%2BBjJyQfJ7gYv%2BrIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNG%2F%2BDA%2FyJV7%2BVeBGCrcA311XrvAwakpJ%2BE%2FXTT1DF4zuIILrmGzcRfeZtv6Rce0wKC%2FMYBQVmqSqLDSmIN04P7XqzQo4hkRCRZI9muirehwyKniHbHjRys3Xcaj8dnnMktRF65dl%2F%2F%2BLlDgErr46kH9rtBcUUEqDqT2ka7G%2BX7QLb%2FnOeuVQwQQUzMyENlyDNAXp9a6RpUQDoZGRdTtXOUp7s5iveRnyZbQbkkiOLUTHiVUtz%2FLPjkZvu9UQimO%2FCwcTwuOUlNAm%2BBl%2BZZxuQFGrLptT61btDd4Jc%2BQM5Zg1eclrIcOrgrd8DdkOxWDWfn3OWSd72HPXQlWHWbrxk4BYqzXbWd4OeuqtZ4J6gzCmEvn28DURoFFdwBQGMuetL7HDiQL45TyR5aLR%2FZ6ivaPBgYf8MWxRr0dd3QzFoUeRtg4bysfOVWYbtDIMxNy1TcipxVh3KhNGBC%2FucVsl%2BhmHFxObQAvOI%2BIXdIjzQo2h%2F0ab1l61l0oCKmN4RMxm%2FI7nebD3i7hJzEfLxrkUoja5jmypa4XxwZHIlvl%2FKah4WM%2FreWquJMwzQmtRfJ6meTR%2B%2B9tYwxoIxKwDNj49Hkyt%2B%2BeylY%2FT0nV2gVLQ0ltQBW%2BtCLcjO5l1UgBe7CJIhqpk3J2o6a9HlI1MLfyjNUGOqUB1Eh95KL6t1dZwbFXZt9X1Uz2QjdsA81dSLi6uw6zP062c7Dr%2B6r7CSaDgPXOtefiSAC%2BVxKK%2Fjjqr05vts547EBlNe4WCQnoOxIEaEBv3RkWEL4xUIYtHHAHmYikdME%2FwZBjXL6X3R%2Bhg7iZpA2HEKgLmOyvIW7Fu3xfW5kM7ZvXDSkye5SmSlvD3d1LNh6wWzdnzO8NqZ1q8glB8AYRVaiRj9vA&X-Amz-Signature=9b2c73b4834c27b717669940b56267c4c3277619e97e0fc4adb88ee52f4cf7cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDTUUKOA%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T014653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVIlhzot9q%2FMmszn7fCOULUvRlqVNlM0MlMAwK4EdORgIgCXSnvCxDyA1Z%2B4F0wjLvLhgX5FH2%2BBjJyQfJ7gYv%2BrIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNG%2F%2BDA%2FyJV7%2BVeBGCrcA311XrvAwakpJ%2BE%2FXTT1DF4zuIILrmGzcRfeZtv6Rce0wKC%2FMYBQVmqSqLDSmIN04P7XqzQo4hkRCRZI9muirehwyKniHbHjRys3Xcaj8dnnMktRF65dl%2F%2F%2BLlDgErr46kH9rtBcUUEqDqT2ka7G%2BX7QLb%2FnOeuVQwQQUzMyENlyDNAXp9a6RpUQDoZGRdTtXOUp7s5iveRnyZbQbkkiOLUTHiVUtz%2FLPjkZvu9UQimO%2FCwcTwuOUlNAm%2BBl%2BZZxuQFGrLptT61btDd4Jc%2BQM5Zg1eclrIcOrgrd8DdkOxWDWfn3OWSd72HPXQlWHWbrxk4BYqzXbWd4OeuqtZ4J6gzCmEvn28DURoFFdwBQGMuetL7HDiQL45TyR5aLR%2FZ6ivaPBgYf8MWxRr0dd3QzFoUeRtg4bysfOVWYbtDIMxNy1TcipxVh3KhNGBC%2FucVsl%2BhmHFxObQAvOI%2BIXdIjzQo2h%2F0ab1l61l0oCKmN4RMxm%2FI7nebD3i7hJzEfLxrkUoja5jmypa4XxwZHIlvl%2FKah4WM%2FreWquJMwzQmtRfJ6meTR%2B%2B9tYwxoIxKwDNj49Hkyt%2B%2BeylY%2FT0nV2gVLQ0ltQBW%2BtCLcjO5l1UgBe7CJIhqpk3J2o6a9HlI1MLfyjNUGOqUB1Eh95KL6t1dZwbFXZt9X1Uz2QjdsA81dSLi6uw6zP062c7Dr%2B6r7CSaDgPXOtefiSAC%2BVxKK%2Fjjqr05vts547EBlNe4WCQnoOxIEaEBv3RkWEL4xUIYtHHAHmYikdME%2FwZBjXL6X3R%2Bhg7iZpA2HEKgLmOyvIW7Fu3xfW5kM7ZvXDSkye5SmSlvD3d1LNh6wWzdnzO8NqZ1q8glB8AYRVaiRj9vA&X-Amz-Signature=81527ab67427d036ca57cd8ad6726741180ac8e3f2d0ceecfb82b599d108030b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
