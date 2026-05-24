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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BLZKVON%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T204250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGf1D4x2JJNdhX70nP%2FE9d8k9CG%2B0Wkm9QwUckQ%2FXtR%2BAiEAuCKAb36BUomHKmvdt7xqCdq4oH3GPHapTy8oldLpmx8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEAvrhbwxMg87nJiTCrcA%2FRr3E6bdAcXLM5MUdVdvkR1KsAufUkMn64i4qn5xFGb53ZLkGqoKBmNciN4IVrP6ipXjlAZeSBhwD3%2FqXuPGRDXr7ZtKuAWEM0wZarzGEOl1Zl5g2YAC5m5iBHJ7FTRlUOGKR9eA0IjDApNpLr0kdAFpzMpCnfTV4Crk8namqRRB8UKi8bOW4ASjm0W%2BNxszjBtBnGL%2Fbc7Kx1GT139F3pMx7XtBq0fjgwhePiROZ6DYAIthWDOp4D2R8owH9rX1mruu49J8LTBEbgq617kLgKEWpnniF3ucBq8t02AsuXmzYGUJx7VxcV6mGCcd2x1eRder0gTfgtEVyUF%2BPRZuUZb7jOS9Rqu%2B9uvcycNW9oW4HnbXfbyJDm4k6%2FEnYmF2T9AHud%2BCuMLNScvPQNMonKvOGEEy8ACfTUkpgx%2FnCkWF%2FrQY8PBWRpCcsunLMcFRbEql6pHVKeP7V2SriQBcO7cBRI50GMXgPF7LJcz8A3vDVbFutPvamtTWtndCsrHA6zCInZGXAXJk5DigGwX8z6LbI076KZGvL0IFok1Pss2YMU2rl2KuKm72ou5jPLOWY9L%2FHAz32jscgy7%2BmrEMsi7MvVRCcIYjzsCunpr4t4mFk13ynRO7YOdRWegMOqmzdAGOqUBVQW37T0dlUa7kKNMHoKS8h0GaxiS4qPPP3aw0PtXmSaZFIWjRg9xjD2ELl0GSbjUYvHljTpESSI8bbSeE9ahB1Wb0zWU0L%2BGf05TTMmTB84u5htSxxBBKMPAFSD3yzWP0QYEaujh4tC7p8LP9ayhYf%2BO4qCYRKTiCwqJHZhNbf7zkgj%2Faid42NqALt%2FSn6ygya8oV74MBVxsbWW1%2BUAJu7v8R%2Bnr&X-Amz-Signature=575ab0e082271d781cf266e8ab05cad8388e22608c6675b11d79db045352e6cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BLZKVON%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T204250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGf1D4x2JJNdhX70nP%2FE9d8k9CG%2B0Wkm9QwUckQ%2FXtR%2BAiEAuCKAb36BUomHKmvdt7xqCdq4oH3GPHapTy8oldLpmx8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEAvrhbwxMg87nJiTCrcA%2FRr3E6bdAcXLM5MUdVdvkR1KsAufUkMn64i4qn5xFGb53ZLkGqoKBmNciN4IVrP6ipXjlAZeSBhwD3%2FqXuPGRDXr7ZtKuAWEM0wZarzGEOl1Zl5g2YAC5m5iBHJ7FTRlUOGKR9eA0IjDApNpLr0kdAFpzMpCnfTV4Crk8namqRRB8UKi8bOW4ASjm0W%2BNxszjBtBnGL%2Fbc7Kx1GT139F3pMx7XtBq0fjgwhePiROZ6DYAIthWDOp4D2R8owH9rX1mruu49J8LTBEbgq617kLgKEWpnniF3ucBq8t02AsuXmzYGUJx7VxcV6mGCcd2x1eRder0gTfgtEVyUF%2BPRZuUZb7jOS9Rqu%2B9uvcycNW9oW4HnbXfbyJDm4k6%2FEnYmF2T9AHud%2BCuMLNScvPQNMonKvOGEEy8ACfTUkpgx%2FnCkWF%2FrQY8PBWRpCcsunLMcFRbEql6pHVKeP7V2SriQBcO7cBRI50GMXgPF7LJcz8A3vDVbFutPvamtTWtndCsrHA6zCInZGXAXJk5DigGwX8z6LbI076KZGvL0IFok1Pss2YMU2rl2KuKm72ou5jPLOWY9L%2FHAz32jscgy7%2BmrEMsi7MvVRCcIYjzsCunpr4t4mFk13ynRO7YOdRWegMOqmzdAGOqUBVQW37T0dlUa7kKNMHoKS8h0GaxiS4qPPP3aw0PtXmSaZFIWjRg9xjD2ELl0GSbjUYvHljTpESSI8bbSeE9ahB1Wb0zWU0L%2BGf05TTMmTB84u5htSxxBBKMPAFSD3yzWP0QYEaujh4tC7p8LP9ayhYf%2BO4qCYRKTiCwqJHZhNbf7zkgj%2Faid42NqALt%2FSn6ygya8oV74MBVxsbWW1%2BUAJu7v8R%2Bnr&X-Amz-Signature=88aff14deceb71e5c9e23051bf2d43f0d23e4751a36d532f6f8f27b6054a28e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
