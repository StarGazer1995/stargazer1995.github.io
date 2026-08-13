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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKXGDLRR%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T052930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIAWEXQ3FLY3Hg8H3pb4jht7cTHFlSTGXGdkP0e5jtekHAiEAzRR4bRtZnPgOSIODFkRQdSwOb%2B7q4bu4iNZs%2BtkRBuIqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYVzFhhnXGl5zR73yrcA53m249WhynFCHN%2F%2BIY10BzK9dQK19k3m3dzl4SEhYE3H6ePwPLUnO46qXAggDQrLNiJkkpx6dc2ww9JPIddZ0ZBHi2IwMP9boAWf1CQPVM9ErsKHUr3FDf6yKGIA8wEnweiJxKjSTzryS6TkaMbDAkf3cRYIoDnSsvii8v8iJe4ovLhJjei0av%2BvvzS%2F8L0hW6PPVVf2KK7WN9U37E%2F5Rc%2Fsu30%2BZ26DtIJz8fLTPrelcKQrRDpExAxK98gtrLyy3bflNvdCFsz8XNgv52WTp19xmlvtnW7Bm8eamLfZNbBH7PbzsNPNk1bSUdmm5JE6zOgAzPC9gRTDVP0aZBYSyznajWUSv%2BRAByCbDpH9eOhF0Kr76jpI4Oit0cdh8D4n%2Bzohj3LZGb7PjkB1oYPRRUCjtxi8WErICqYJ8PIAuENIEnl2YDnCS2JwK6zMNf0JqTcqDtDnqXl3t4nMzlrsvNU2ZW85Iv%2F%2FbAdjTyE3eM2aG17IZKRGn%2FVYnZ0c2VgnMAP6L%2FcQNhtQpityLK7Hir7RCqrhqbSp9v0x%2FZl5cWuo94AvudXvX8Sz1%2FKci7frrHdZFf9B9O0ATM8SQArsPXqiF4P1PiJ%2BnYz6bGAHwcVAotwQ%2FW8Q499nxFrMLDF9NMGOqUB52Gb3qYfELORM8yORaNaKdR%2F08y2WZdZEbAksvm5TCN2YKGFkKyr79wZcJaoX%2BMd%2B%2FLITEShASJHlXvM%2Fvqyu0TS0Iw3vR7eKQKBPOgpP9r5DuHfpnqRxOlD1nN%2FRjhsjK%2BxYZgKB4Cpp%2FYp%2BGUgjdztU%2B081h2o2jEujw%2B4Znul6B196E1autmcucUnPSVTUu%2BUDh6J0h5LvluApbA3AZ1bBmyI&X-Amz-Signature=0f476f0fb667579214151c4c0014f041505e5eb61664f65de7e734e33cf76cd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKXGDLRR%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T052930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIAWEXQ3FLY3Hg8H3pb4jht7cTHFlSTGXGdkP0e5jtekHAiEAzRR4bRtZnPgOSIODFkRQdSwOb%2B7q4bu4iNZs%2BtkRBuIqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYVzFhhnXGl5zR73yrcA53m249WhynFCHN%2F%2BIY10BzK9dQK19k3m3dzl4SEhYE3H6ePwPLUnO46qXAggDQrLNiJkkpx6dc2ww9JPIddZ0ZBHi2IwMP9boAWf1CQPVM9ErsKHUr3FDf6yKGIA8wEnweiJxKjSTzryS6TkaMbDAkf3cRYIoDnSsvii8v8iJe4ovLhJjei0av%2BvvzS%2F8L0hW6PPVVf2KK7WN9U37E%2F5Rc%2Fsu30%2BZ26DtIJz8fLTPrelcKQrRDpExAxK98gtrLyy3bflNvdCFsz8XNgv52WTp19xmlvtnW7Bm8eamLfZNbBH7PbzsNPNk1bSUdmm5JE6zOgAzPC9gRTDVP0aZBYSyznajWUSv%2BRAByCbDpH9eOhF0Kr76jpI4Oit0cdh8D4n%2Bzohj3LZGb7PjkB1oYPRRUCjtxi8WErICqYJ8PIAuENIEnl2YDnCS2JwK6zMNf0JqTcqDtDnqXl3t4nMzlrsvNU2ZW85Iv%2F%2FbAdjTyE3eM2aG17IZKRGn%2FVYnZ0c2VgnMAP6L%2FcQNhtQpityLK7Hir7RCqrhqbSp9v0x%2FZl5cWuo94AvudXvX8Sz1%2FKci7frrHdZFf9B9O0ATM8SQArsPXqiF4P1PiJ%2BnYz6bGAHwcVAotwQ%2FW8Q499nxFrMLDF9NMGOqUB52Gb3qYfELORM8yORaNaKdR%2F08y2WZdZEbAksvm5TCN2YKGFkKyr79wZcJaoX%2BMd%2B%2FLITEShASJHlXvM%2Fvqyu0TS0Iw3vR7eKQKBPOgpP9r5DuHfpnqRxOlD1nN%2FRjhsjK%2BxYZgKB4Cpp%2FYp%2BGUgjdztU%2B081h2o2jEujw%2B4Znul6B196E1autmcucUnPSVTUu%2BUDh6J0h5LvluApbA3AZ1bBmyI&X-Amz-Signature=2317982781e8d6f995504a33f8791e5d2555895ae8ac43a0406ac92bbcf8c81c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
