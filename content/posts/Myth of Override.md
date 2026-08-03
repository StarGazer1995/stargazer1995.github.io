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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EGQBYTN%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T161346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIEuEzBpEpFM1XiQ%2BBK2xUNBNiGS5t9Im89z6JCHkosAWAiB2vrnBff3Dl81XgvodgzXlXY4B6k4JB2XBd0I3KcQ%2FqCqIBAj5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTPRda6bAu0tjiEVWKtwDxlv%2FrTWtj4k9C5Am93n7meps5alw7WEezV%2FTy4jzD5BuzrNBJmx3IePKn71sv37%2BMF5PQVhR1E7JRkFEAYIICUxG%2FuhyGx9f1joHN9OK1L1iFddKmP0gJOBeLsLXgW9Mq2F2gPbQ%2FF0XP9%2B5kTrSzweDi1iHe1Kqcy0XefnDh3kzkEISIJtZ49OKBuO131JYQ0tr03IpynbVy6zAWIxzPUN8a8GmgcqSXxS2SXGtkmKkEadb1bij%2FTmqPy1GTRzve60eBzAbVSNxJmvhWUwwadTyYnO5YA%2BRsbsCm30EODHeW28%2Fvtl%2FRcnL0R5Cyn%2BNH7ogQs3YTJII%2FJ5Ll4VvhZjdojx4nH8pQ6rx%2BatGFHNTYjwnpyixqikahp%2FCDjSoNwvNhTGNg0Gs2azAxIvufoQnRvUiUam0dnuT%2B6HFJbguT3yyh%2FkjILmBqMBjW31Spdf9D5Q1Pko38sbXyxYAC%2Bn0cX4gUQDOKYfTs6uaEykVX1beDJn7IGJ46863nDDVlqayvVaZgQ7O0oDypKCBBwgIAA9GDDj3PPlY6yktTjkE3DtuC51Nez1LbRLEKS7hi5I83q%2B%2FAroTkWcIShaAWlErzmI6y5VVA%2BznH9b3TiqDuktpGCWOcMbSKQ4wy%2FrC0wY6pgHVBGtJSTkVxd7cqcwZaZ%2FqXJqTM0OSZD2NEWv3Xw%2Fh9Dx6BdGJydExaCBFdLy4N%2BIY0Ni05m4yWtkTHcaVFxvBTz2Cd9T47d5a8m7M6mBdyxyN2o933C0IVw%2F4y4hTXw6Lv20pBhCzuTGIEgau3fiUL6klA7bv7hVbEM2sv5SGGDe88AgfBDz825ZaWPktLSX12wG%2FOqgyYUIoaDDKw0UBPwk2wQM4&X-Amz-Signature=2afcf4c4abedd79171d4aaa7416cf81c7a89b0c99f31acee745add400bc0417d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EGQBYTN%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T161346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIEuEzBpEpFM1XiQ%2BBK2xUNBNiGS5t9Im89z6JCHkosAWAiB2vrnBff3Dl81XgvodgzXlXY4B6k4JB2XBd0I3KcQ%2FqCqIBAj5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTPRda6bAu0tjiEVWKtwDxlv%2FrTWtj4k9C5Am93n7meps5alw7WEezV%2FTy4jzD5BuzrNBJmx3IePKn71sv37%2BMF5PQVhR1E7JRkFEAYIICUxG%2FuhyGx9f1joHN9OK1L1iFddKmP0gJOBeLsLXgW9Mq2F2gPbQ%2FF0XP9%2B5kTrSzweDi1iHe1Kqcy0XefnDh3kzkEISIJtZ49OKBuO131JYQ0tr03IpynbVy6zAWIxzPUN8a8GmgcqSXxS2SXGtkmKkEadb1bij%2FTmqPy1GTRzve60eBzAbVSNxJmvhWUwwadTyYnO5YA%2BRsbsCm30EODHeW28%2Fvtl%2FRcnL0R5Cyn%2BNH7ogQs3YTJII%2FJ5Ll4VvhZjdojx4nH8pQ6rx%2BatGFHNTYjwnpyixqikahp%2FCDjSoNwvNhTGNg0Gs2azAxIvufoQnRvUiUam0dnuT%2B6HFJbguT3yyh%2FkjILmBqMBjW31Spdf9D5Q1Pko38sbXyxYAC%2Bn0cX4gUQDOKYfTs6uaEykVX1beDJn7IGJ46863nDDVlqayvVaZgQ7O0oDypKCBBwgIAA9GDDj3PPlY6yktTjkE3DtuC51Nez1LbRLEKS7hi5I83q%2B%2FAroTkWcIShaAWlErzmI6y5VVA%2BznH9b3TiqDuktpGCWOcMbSKQ4wy%2FrC0wY6pgHVBGtJSTkVxd7cqcwZaZ%2FqXJqTM0OSZD2NEWv3Xw%2Fh9Dx6BdGJydExaCBFdLy4N%2BIY0Ni05m4yWtkTHcaVFxvBTz2Cd9T47d5a8m7M6mBdyxyN2o933C0IVw%2F4y4hTXw6Lv20pBhCzuTGIEgau3fiUL6klA7bv7hVbEM2sv5SGGDe88AgfBDz825ZaWPktLSX12wG%2FOqgyYUIoaDDKw0UBPwk2wQM4&X-Amz-Signature=140a60ddadf9f9db8d81422ab6276c298d1bea31577f4cfb51014729e8f6af9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
