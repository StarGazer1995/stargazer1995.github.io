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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ44AUH2%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T230052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICzbA3WxIhwp2RmdhctwyVs3iIeLNnY64LiwbLtmrV9eAiEAtpKRerKUJSr3aSj1mY99iLkyuFkJYBKxn%2Fz%2BlbOMfxgq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDO6c8acKEhCd%2BwLJTCrcA69FnshVT4a9aDoCBf05SjySYK9Rbk2HyXk7dc%2BT161TNPf9fU5meiAmTceFyIWhk4mrN0MfKICTdFTYM5ONlESABKCeAP7zQV4XfM4M83U69V5IvPpydFrN6BFedYIaA9cjOr009jjo%2BI6aP9dmJwnDvpHztUr8rnfZ9GrENMailh24K21kkweFalT1zLBlIYEN7ha8b4SM7tTb%2FJdtMtJk0lRzUztLAnUSicnyf94A0LnVZHKRK5Ea7Og8cHoRgCjaBsQOGrsYaO%2B7p1ClRz33eGSJN3UCHxvUMytajyRfVSbuLhFSG5UOmxsvmKxlgB5lOYYD7GJhZECmhb3ZiNsLwi8uImqIdiv7WziP%2BRBDQ8yh86SjaHboz3gP029xIKgD38xt3MbWTkHQiEcHWjplL1eYhCrpy5MYtL9WNK%2FlXAX%2FKa5Y10dKSRBq78SE3c5koq33t7PJpetGfLM80CqOX1Ow0k%2FE%2BFg2sDlSAbpRoXBgFbQ4H1JDH4rmRg%2FrEk53NidXgox3%2FPRI7pj6irRRI09%2Bf9aYnNmmsi7lMdSgjrJzTUkbD9eIefuHigJdhGFXRUpEZ8DtcU9eYMWa7NcI20Ls4pDCqVYJuJFtefwO4t09W0PfPa%2FShpkyMInoh9EGOqUBjckhWRCHTkrwIMFrNShgvWyKw1ZO%2F5esEoviY6BhxZTB1ne5q%2B8xXQF1Kbn9uJ2Lf4lycsDSiH82qMdTZx9rVpPtV8AFC0nQsqyKyd4P6h0xn8qBdEdIngCeTGQGH%2BYrsTnUmR74snuwJZ%2Fa8FhuNSnGDJiKwUHAZyGxI0OAnH0AC0K0dyepAI4ICO3mWd4jb95aX6pKp7AlEc3CGxFjR3tYpE9r&X-Amz-Signature=7c2a639c2883eb3226c673014c65d2b3cc20622a55fd535569e7c913ea88810f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ44AUH2%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T230052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICzbA3WxIhwp2RmdhctwyVs3iIeLNnY64LiwbLtmrV9eAiEAtpKRerKUJSr3aSj1mY99iLkyuFkJYBKxn%2Fz%2BlbOMfxgq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDO6c8acKEhCd%2BwLJTCrcA69FnshVT4a9aDoCBf05SjySYK9Rbk2HyXk7dc%2BT161TNPf9fU5meiAmTceFyIWhk4mrN0MfKICTdFTYM5ONlESABKCeAP7zQV4XfM4M83U69V5IvPpydFrN6BFedYIaA9cjOr009jjo%2BI6aP9dmJwnDvpHztUr8rnfZ9GrENMailh24K21kkweFalT1zLBlIYEN7ha8b4SM7tTb%2FJdtMtJk0lRzUztLAnUSicnyf94A0LnVZHKRK5Ea7Og8cHoRgCjaBsQOGrsYaO%2B7p1ClRz33eGSJN3UCHxvUMytajyRfVSbuLhFSG5UOmxsvmKxlgB5lOYYD7GJhZECmhb3ZiNsLwi8uImqIdiv7WziP%2BRBDQ8yh86SjaHboz3gP029xIKgD38xt3MbWTkHQiEcHWjplL1eYhCrpy5MYtL9WNK%2FlXAX%2FKa5Y10dKSRBq78SE3c5koq33t7PJpetGfLM80CqOX1Ow0k%2FE%2BFg2sDlSAbpRoXBgFbQ4H1JDH4rmRg%2FrEk53NidXgox3%2FPRI7pj6irRRI09%2Bf9aYnNmmsi7lMdSgjrJzTUkbD9eIefuHigJdhGFXRUpEZ8DtcU9eYMWa7NcI20Ls4pDCqVYJuJFtefwO4t09W0PfPa%2FShpkyMInoh9EGOqUBjckhWRCHTkrwIMFrNShgvWyKw1ZO%2F5esEoviY6BhxZTB1ne5q%2B8xXQF1Kbn9uJ2Lf4lycsDSiH82qMdTZx9rVpPtV8AFC0nQsqyKyd4P6h0xn8qBdEdIngCeTGQGH%2BYrsTnUmR74snuwJZ%2Fa8FhuNSnGDJiKwUHAZyGxI0OAnH0AC0K0dyepAI4ICO3mWd4jb95aX6pKp7AlEc3CGxFjR3tYpE9r&X-Amz-Signature=97ae6816e96f4c8caa7f1f2b08e7938e516af14c327254a5deda751949358fa4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
