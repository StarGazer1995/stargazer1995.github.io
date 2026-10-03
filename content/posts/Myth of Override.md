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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR2WX4XN%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T125005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIARgW2xsDgXcHKiOBd%2BV%2BYe1bG8q7oPUoqoBkmEmodVGAiAucVmw1mcyLoEcK9ud7ZxlmvsM5ZAX15F%2Fywx7AAeq2iqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BvHJ3VjQ%2B9Z1FNBjKtwDLcSJprb6Nfw%2FKC%2FcGRHZQjIwIPXNLrtjmFf9iSjYPM88P76oWS2yEWkj0Pokb%2BMFl1qiF13V%2BtR6P1tXey5P3rU5QLroY2hQU%2BUavbS15OmigZMP6S7RV0V622avHpAYwMxFUqcOE2apRhUD8PJTqZZL%2Fhy95PwTT4uwy2Yfdu46JC19iO12gHAfqf1em1iOBUy9k3nWIZqEBukJ0aL%2BbvdiTGxgvY6ik5RkNMfjg5XWqoKFm%2FMS3YZtLJmCI0Bm1jozCl%2B20b8vszW6O2knvZmUZNE5D9WxKriZXg8Tl2WRZ6T0otpVrLrW6AAWDWlYDXuykVPLY166txpGznrWFUw4H8bmftCCCCYZ0jswU49YNctOrkS3M8qUCemw3gU%2F7mW6e0NIiI07eCPdc%2FZbMMo0Lp5egooXE%2FRG%2BC%2FRriyjAC1RZZrFRIf3wwD%2F6ItGTS%2FSwAq8KP0HqVH2KH%2FQft5BP6f3FsoS%2FBqbU7C1Zc8dXFZ7zZoaCukQ6cMxEyz1KwMGyo%2FcjCWTW%2BOo2A5uEutWn2p%2BJJ%2FtXpO2cacGk8I7FvJHhqkA2%2Bx6rmGRA5Y1sKdPCCl%2FxI8GYpO8n9UY9K%2B1dLqO%2FH7%2BWV%2F3%2F6SJRIk30tj6rhji4HJSvz4wxrGD1gY6pgH3foV%2BZ%2FGIsAYTKfHtClWOP%2FFi4sPlKEHU4FFdE%2F%2F%2B2g%2BA%2FBzR6UZgCy290nGXV1cPOj4kL%2FJsau8ztGIvq6bp9%2FQxch8T7TqooZjiBDq1W9WHwMFs%2FH6CCWKWCTfVY2d4a7fId69Mf2hGhOmG3OSM3vJyWBEY0UX446mUNLxkQXPFPUtcCVILhk2Uyln7Sk6BkPqseisqEdq0H%2Bwo8SlgAitrd6tW&X-Amz-Signature=9fa7d7e31014c6c00309e8e7014803841a2d9e55c73aab8d4e1fc901af48417e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR2WX4XN%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T125005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIARgW2xsDgXcHKiOBd%2BV%2BYe1bG8q7oPUoqoBkmEmodVGAiAucVmw1mcyLoEcK9ud7ZxlmvsM5ZAX15F%2Fywx7AAeq2iqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BvHJ3VjQ%2B9Z1FNBjKtwDLcSJprb6Nfw%2FKC%2FcGRHZQjIwIPXNLrtjmFf9iSjYPM88P76oWS2yEWkj0Pokb%2BMFl1qiF13V%2BtR6P1tXey5P3rU5QLroY2hQU%2BUavbS15OmigZMP6S7RV0V622avHpAYwMxFUqcOE2apRhUD8PJTqZZL%2Fhy95PwTT4uwy2Yfdu46JC19iO12gHAfqf1em1iOBUy9k3nWIZqEBukJ0aL%2BbvdiTGxgvY6ik5RkNMfjg5XWqoKFm%2FMS3YZtLJmCI0Bm1jozCl%2B20b8vszW6O2knvZmUZNE5D9WxKriZXg8Tl2WRZ6T0otpVrLrW6AAWDWlYDXuykVPLY166txpGznrWFUw4H8bmftCCCCYZ0jswU49YNctOrkS3M8qUCemw3gU%2F7mW6e0NIiI07eCPdc%2FZbMMo0Lp5egooXE%2FRG%2BC%2FRriyjAC1RZZrFRIf3wwD%2F6ItGTS%2FSwAq8KP0HqVH2KH%2FQft5BP6f3FsoS%2FBqbU7C1Zc8dXFZ7zZoaCukQ6cMxEyz1KwMGyo%2FcjCWTW%2BOo2A5uEutWn2p%2BJJ%2FtXpO2cacGk8I7FvJHhqkA2%2Bx6rmGRA5Y1sKdPCCl%2FxI8GYpO8n9UY9K%2B1dLqO%2FH7%2BWV%2F3%2F6SJRIk30tj6rhji4HJSvz4wxrGD1gY6pgH3foV%2BZ%2FGIsAYTKfHtClWOP%2FFi4sPlKEHU4FFdE%2F%2F%2B2g%2BA%2FBzR6UZgCy290nGXV1cPOj4kL%2FJsau8ztGIvq6bp9%2FQxch8T7TqooZjiBDq1W9WHwMFs%2FH6CCWKWCTfVY2d4a7fId69Mf2hGhOmG3OSM3vJyWBEY0UX446mUNLxkQXPFPUtcCVILhk2Uyln7Sk6BkPqseisqEdq0H%2Bwo8SlgAitrd6tW&X-Amz-Signature=b7731936755294a43d963f4eecb719a0df1ee88062e40ab41464e64e267ed70b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
