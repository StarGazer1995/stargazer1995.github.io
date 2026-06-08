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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJPSN4T7%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T172012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHaR0T6RTHbDBmqnwdoe274g4wiIuZVGcQCvcZ57S%2B7AiBvb0W16iM68x7WMiCGRRaDtYWP1TlWSyUM0wUW2IHR1SqIBAi3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMElTzoxkOcWTMo4WoKtwDmMDt1ua1iUAzPUcUsxP28sbrKO%2BbKkUpBG41xWjPqkpEpf6UPZbZWDePi2hvU%2F9%2B0YaY%2Bl8HsrQSicPG4%2BHWXZgbClNu3Kyf%2FaSZV2G6VGiRPD7M3UE4EUWqr6F%2BNluxi93EAjnj6yEIZyKUIf3gU0kU6pkeIlvJmM8uACq8KdWkWt7vFYew%2Bws7Ccl7W9jR0WATzmDVS2Tj7%2FAa8kmRIC19xJRId94ALFmWk7SCUiC2%2BSYLaY1jkJRrnuQuG3Y90mk7nDAvksJvnY%2FAk%2ByxDvJeZn%2BZUNaCZFWaAbpnGETt0%2BznT56mc6k9hOglCMVzAnVbcYzHSAc1HdV%2BXl6fUjUajeI%2Ft3Q3GbkbRIHO%2FVpRebAq0EwOT6RU1psg13azwyajWKLm38kXonbR36UaI3Ml6o%2FxWDLkWq8zqtDSvnG0jBy4eUt904ktochQ6u24h2gUxZNjcF5WnEjnoqxpmI0SCEqm%2BrkDz33Qp9DRvQp3wG56m%2BMvnjrBlFUvClwQxf0aaKvm2DevXUVNusQxTBbay9UOcnRV1fetfaKA4lNDkrijKREVyYg9f1F%2Fa9DBzz%2FQymWtZ4%2FwEbxU%2FX4UT8koyyrGcPeX21%2BKy5dyXXIf39DBV%2BOFYkP1rGww5J6b0QY6pgE0SOe8OxTJpbZmaqcIKGxsQUB%2FDe0%2B8GJaJ%2FK5pIMnlJchUfhP8cnqQj%2FNNOyQ8aFyPgWxvugvrJxtfG9YkR2N5trzBBhqs%2B77tQr4laUhMRkrAaNraKXO3WtA3OMlxamejCQowkz7x6ybCddv3iRIz8XBiiLHGdlrpclIA8c%2F0CkzKPbhfgJTI6SE%2FHQ9RJmku84NcIIAJGG8M0oNkUEIAR0fOmn2&X-Amz-Signature=39f6bc043f634f6f57b5e5e25eaa53e377aae0ad27cda695ebbaa7dd4de4dfaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJPSN4T7%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T172012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHaR0T6RTHbDBmqnwdoe274g4wiIuZVGcQCvcZ57S%2B7AiBvb0W16iM68x7WMiCGRRaDtYWP1TlWSyUM0wUW2IHR1SqIBAi3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMElTzoxkOcWTMo4WoKtwDmMDt1ua1iUAzPUcUsxP28sbrKO%2BbKkUpBG41xWjPqkpEpf6UPZbZWDePi2hvU%2F9%2B0YaY%2Bl8HsrQSicPG4%2BHWXZgbClNu3Kyf%2FaSZV2G6VGiRPD7M3UE4EUWqr6F%2BNluxi93EAjnj6yEIZyKUIf3gU0kU6pkeIlvJmM8uACq8KdWkWt7vFYew%2Bws7Ccl7W9jR0WATzmDVS2Tj7%2FAa8kmRIC19xJRId94ALFmWk7SCUiC2%2BSYLaY1jkJRrnuQuG3Y90mk7nDAvksJvnY%2FAk%2ByxDvJeZn%2BZUNaCZFWaAbpnGETt0%2BznT56mc6k9hOglCMVzAnVbcYzHSAc1HdV%2BXl6fUjUajeI%2Ft3Q3GbkbRIHO%2FVpRebAq0EwOT6RU1psg13azwyajWKLm38kXonbR36UaI3Ml6o%2FxWDLkWq8zqtDSvnG0jBy4eUt904ktochQ6u24h2gUxZNjcF5WnEjnoqxpmI0SCEqm%2BrkDz33Qp9DRvQp3wG56m%2BMvnjrBlFUvClwQxf0aaKvm2DevXUVNusQxTBbay9UOcnRV1fetfaKA4lNDkrijKREVyYg9f1F%2Fa9DBzz%2FQymWtZ4%2FwEbxU%2FX4UT8koyyrGcPeX21%2BKy5dyXXIf39DBV%2BOFYkP1rGww5J6b0QY6pgE0SOe8OxTJpbZmaqcIKGxsQUB%2FDe0%2B8GJaJ%2FK5pIMnlJchUfhP8cnqQj%2FNNOyQ8aFyPgWxvugvrJxtfG9YkR2N5trzBBhqs%2B77tQr4laUhMRkrAaNraKXO3WtA3OMlxamejCQowkz7x6ybCddv3iRIz8XBiiLHGdlrpclIA8c%2F0CkzKPbhfgJTI6SE%2FHQ9RJmku84NcIIAJGG8M0oNkUEIAR0fOmn2&X-Amz-Signature=3e49c2ed48d7f6f7b4c2a3f3c82bbf4ce52ae7ccdf6e8c65db565a803c3a92aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
