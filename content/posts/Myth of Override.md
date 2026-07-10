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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6HKV4W7%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T085814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDjGsTe%2F9OkW6fG7L8ENhWSQqpu8i2xLARkDqlHV3PAAIgP3uurrQeSsHQINJRrCU5F9oXBhsTMO0%2Fh7MtSFeRlyYqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEud6BO65w6XjCgURSrcA%2BVn4CI33aCIYksucQWejQH31Z%2Btq6FMIBamaVUY3hdhRYH4H%2FiT6063xZPX0rUwihGnqjtgN5odY1%2FQi13f586xpi6bVixDcOitdKvefJz3tbuMQiQyUSyFlnRsysU%2Fk1qEpwbKxHvfB5Zc1NKHvTkiqJwCnSXrARvzcbRzfVEogiv5j5TKO%2FJbcIDxEwesZTEuuyZUayIRWP%2B4DkofAPbCuC3POj5qk3tAn0GM8sUe%2Bda2eqN9yEB28rUCS55g1MjOEBizO2f8%2F2vpW6vQcM%2F%2FFED0DLEk1UX%2Bs0UkOgou7pOcxGsD6u9OhE%2Bq38gX2QKnYgoWlPk9BboJmMNwXgRLu%2FffTzaEBb4MEnpy1jevGUI9k2F7tQwzndzpJMRlCTEbnFB5cj4hsUr1Xc4JOEtRzAAFzEaGB7KWox1mVHXpO0drWjPNKenwze4YC5xqg7J8HJyKEww7P8dPJIJHvOdaPF%2BncESifc6QdJRg4esjckGBne4bBibxoN%2B4DJihBxpsa6T5XBJ6PeLZ2FH7guj9FUV5nxvYgOlBPbGgYtXTi2tRYcR%2BcILHBrYYb2PkPCCkIaBxzhhuO4cNmwBnP3sy6O%2BRauYuINu8GDadvIolkqYGqYGqRbGNuTcJMMPEwtIGOqUB4pnvSFvHU%2Fr0EH9QqpmT1uYDEAPeZUi15MxKnvwTMQ%2BEBiyy3Wdsus2YUZDOMDCaZ5BO1ydaVK1R5NS6W00Gm82DGqwJmF6dfXiS6vd8WuiXgrNxga2PBuPTWmVLX%2F5IiNY%2FS%2BA4JulPf0PDeEI7B4cOwat%2BOb36%2BO62R1c6Mk00crN62NKwjieuX%2BDNKmgZOck5gIGZ%2Bg99fYOf%2FzxIE7pvd%2FuK&X-Amz-Signature=bb3628ce1e74a71fcfc73b856484867a6d18c75934ba91b29db0fd584baa0c1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6HKV4W7%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T085814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDjGsTe%2F9OkW6fG7L8ENhWSQqpu8i2xLARkDqlHV3PAAIgP3uurrQeSsHQINJRrCU5F9oXBhsTMO0%2Fh7MtSFeRlyYqiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEud6BO65w6XjCgURSrcA%2BVn4CI33aCIYksucQWejQH31Z%2Btq6FMIBamaVUY3hdhRYH4H%2FiT6063xZPX0rUwihGnqjtgN5odY1%2FQi13f586xpi6bVixDcOitdKvefJz3tbuMQiQyUSyFlnRsysU%2Fk1qEpwbKxHvfB5Zc1NKHvTkiqJwCnSXrARvzcbRzfVEogiv5j5TKO%2FJbcIDxEwesZTEuuyZUayIRWP%2B4DkofAPbCuC3POj5qk3tAn0GM8sUe%2Bda2eqN9yEB28rUCS55g1MjOEBizO2f8%2F2vpW6vQcM%2F%2FFED0DLEk1UX%2Bs0UkOgou7pOcxGsD6u9OhE%2Bq38gX2QKnYgoWlPk9BboJmMNwXgRLu%2FffTzaEBb4MEnpy1jevGUI9k2F7tQwzndzpJMRlCTEbnFB5cj4hsUr1Xc4JOEtRzAAFzEaGB7KWox1mVHXpO0drWjPNKenwze4YC5xqg7J8HJyKEww7P8dPJIJHvOdaPF%2BncESifc6QdJRg4esjckGBne4bBibxoN%2B4DJihBxpsa6T5XBJ6PeLZ2FH7guj9FUV5nxvYgOlBPbGgYtXTi2tRYcR%2BcILHBrYYb2PkPCCkIaBxzhhuO4cNmwBnP3sy6O%2BRauYuINu8GDadvIolkqYGqYGqRbGNuTcJMMPEwtIGOqUB4pnvSFvHU%2Fr0EH9QqpmT1uYDEAPeZUi15MxKnvwTMQ%2BEBiyy3Wdsus2YUZDOMDCaZ5BO1ydaVK1R5NS6W00Gm82DGqwJmF6dfXiS6vd8WuiXgrNxga2PBuPTWmVLX%2F5IiNY%2FS%2BA4JulPf0PDeEI7B4cOwat%2BOb36%2BO62R1c6Mk00crN62NKwjieuX%2BDNKmgZOck5gIGZ%2Bg99fYOf%2FzxIE7pvd%2FuK&X-Amz-Signature=80db87785cd33dfbb6039563b57af6547f055119dc4db0709d9a5bb360509b3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
