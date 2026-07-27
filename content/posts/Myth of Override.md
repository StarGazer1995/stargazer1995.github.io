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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEJ5C54G%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T224949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDxkKX7SKHmUYhpO417kwEPP2NE9sCNZbkHdGMTMN1uVAiEA%2Bbp%2Fx7h9tgAD%2FuVxBb1HfsdyYdD6lsQ3dBqxADf6ngMq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDCuQGY7GcGbYk8mxNCrcA720Sg5oCT18dL5XFFNIJ4rcXef6Fsy6wXGgNuo7gx%2FBe%2FwTxL8JCN8A3G%2F9PZ3Ee3cQHazdTKSwH7ilf3qK65JwkhNhlilV1tzotEcD0QewQwkMuYQG5EhsJMbH5lRRt5U3xXRvSCxJMpqlo%2B3mAs2bVNRvRunI5Gn8kBhV%2ByNetu76gnY3AHb3iXwWPVHVl49Q6kxoUtVjpuGou5UUbo39JK5kK72NnHMWJSF0w8xWVzz0XPRweJ3lcgSLnNDciGm%2BSnCfvAG3OY2jultH6wV6XUDiwzHga6TaSOTPEf9eM01YWL9yba5wPZBa%2B1WAeYu9ekTSnFgsw8wIgu6z6jHZ5p7kpzAtuaMyn4RW5tF2po9opzBdlG24oZWlrU6MNBVYOjYtH3bmoEcNiEsOFyOiZJOVxU1Meaq90I4c%2BTfwHQExNL3Fjd8xhS0aKQ%2FpPoZUzHtf9I%2FCaSGkaOnArK6KGeQv0XkUwI55Pa6%2BWLA602EIEc1cjXjUBFE82zk3bRI0bQ8VavF397Ap9Ig2nDI6pxZsXJnYYl%2BE%2BSBYktzh0G7d49bLR4m0%2BQAESVcjUxlYeUn3o06PTG4N94hfX6xWlGNqYvzN%2FsSk39My%2FsFRBu3ufY%2BkXoaUHwRfMIbrntMGOqUB3Ly0%2Bic%2FpMudl0ucqUzzP3PqxGosOmyOi2Yv4iesI%2BO2fMs2cS2ZoeZIrr5szhEyxpElWGrMedLVtdo6PVTlqTh%2BHIa3tjSvknX1hSR5Z2JZglwJW%2FQukrLOD8pApFVJgk8e15u%2Bkw0V%2BRqFlOw4M%2BrTpwGPRtzVrA1SHteUSgvEzgD%2F2LW7tzWgnyY1gL4aLba5XCxUZZazoPR%2B5xohTNHu2GM%2F&X-Amz-Signature=a110d85f5b78ba880ee11d4f589877af43b6a63c245c420fd380ce491cc6a8b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEJ5C54G%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T224949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDxkKX7SKHmUYhpO417kwEPP2NE9sCNZbkHdGMTMN1uVAiEA%2Bbp%2Fx7h9tgAD%2FuVxBb1HfsdyYdD6lsQ3dBqxADf6ngMq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDCuQGY7GcGbYk8mxNCrcA720Sg5oCT18dL5XFFNIJ4rcXef6Fsy6wXGgNuo7gx%2FBe%2FwTxL8JCN8A3G%2F9PZ3Ee3cQHazdTKSwH7ilf3qK65JwkhNhlilV1tzotEcD0QewQwkMuYQG5EhsJMbH5lRRt5U3xXRvSCxJMpqlo%2B3mAs2bVNRvRunI5Gn8kBhV%2ByNetu76gnY3AHb3iXwWPVHVl49Q6kxoUtVjpuGou5UUbo39JK5kK72NnHMWJSF0w8xWVzz0XPRweJ3lcgSLnNDciGm%2BSnCfvAG3OY2jultH6wV6XUDiwzHga6TaSOTPEf9eM01YWL9yba5wPZBa%2B1WAeYu9ekTSnFgsw8wIgu6z6jHZ5p7kpzAtuaMyn4RW5tF2po9opzBdlG24oZWlrU6MNBVYOjYtH3bmoEcNiEsOFyOiZJOVxU1Meaq90I4c%2BTfwHQExNL3Fjd8xhS0aKQ%2FpPoZUzHtf9I%2FCaSGkaOnArK6KGeQv0XkUwI55Pa6%2BWLA602EIEc1cjXjUBFE82zk3bRI0bQ8VavF397Ap9Ig2nDI6pxZsXJnYYl%2BE%2BSBYktzh0G7d49bLR4m0%2BQAESVcjUxlYeUn3o06PTG4N94hfX6xWlGNqYvzN%2FsSk39My%2FsFRBu3ufY%2BkXoaUHwRfMIbrntMGOqUB3Ly0%2Bic%2FpMudl0ucqUzzP3PqxGosOmyOi2Yv4iesI%2BO2fMs2cS2ZoeZIrr5szhEyxpElWGrMedLVtdo6PVTlqTh%2BHIa3tjSvknX1hSR5Z2JZglwJW%2FQukrLOD8pApFVJgk8e15u%2Bkw0V%2BRqFlOw4M%2BrTpwGPRtzVrA1SHteUSgvEzgD%2F2LW7tzWgnyY1gL4aLba5XCxUZZazoPR%2B5xohTNHu2GM%2F&X-Amz-Signature=fee06d467d3dd6c9e718e0e430897b80a77944938aa60e80939f8a69d161d728&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
