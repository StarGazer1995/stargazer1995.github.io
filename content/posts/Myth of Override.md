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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V25QVD4D%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T045852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQCKV2HyAVrpzan1Rf%2Bbvb1%2BJt%2F9oMYwsLkwyiD5y8cyGgIhAKSq0apNHrfaORzjFwXXoQK2AeMUGZzID8MHCK0W%2FoYwKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQAw%2BbNgydR6Uqfqkq3AMArLDaNikNS8P91Bi5Z0%2BVjUcKd25ncFsKo85HYxxeX%2F0otfaKxZbKkdlekcioq8K41cnCFrCIHHVgLer8Ii28O2O5erivw5gjSst34cn%2BCPZ003Ruzxt0SlZZjNnTkH48AA2HWyCRXTubN0qHI1DwcsF58WSQDdKc9Yaq1qSGulHvTUqKl8H18ffbtRecCZq7RNkeol%2FEVQT4j4MRPvLtmG4YsELxfBIU5350QIaeMOMJLp3W3PCtG2gUvn99Ga2FA09VPCp2CCvwESU1AsLcD1EC6WPvN6vji2st4ZTQWJzYhM1uP35RY7M5XnwfW1jkbBEDuHm15HaKVi3oXwC1SUOzU3BceSNR2H7bNMcGwE75TeLl6j0ExS1RahaWsCqpKjuI9WavL4sC2%2FgA54gkXJz8yo5O9GMxigUQYUKVhwe7mpBqMSxnYx5v63%2FpPNRl%2FIm96iTbOZOS%2BtmK8VcmAkqrIIfo4QLE80XiZFqVqd%2BG03fnVqzjgFtK3RfkKnF8mDdey4AzlikJY2%2FBhgR33oedQ5IwJQD6NzB0n4HHMdRdSjmtstj5m%2F8ZFj0cH1Tj3NOBDnA1A%2BXHCPAA0Oqi%2FXNB%2Ba7w5cWjuby85BNqNsGtrD%2FldhLRLlScLTCly4vTBjqkASaGA3lbDaGiv5gbhIzBcTx4RJ%2FLT87r5e8mGOeuueDHjrRutPDqy%2F%2Bm2kMGRMD97%2BxL97iGyj0Tlqx9e5EvyJ7zlojqIQG5d8ugF2uC4gV3k%2B7BLom8CT9%2FlsVodXxeQZ6TluFnuEMoebVU8%2FIBnBy%2B%2BYe6UXp%2FgMUX%2BZdJtOAaBdONVvY9tJ%2FWgBLKgbf6XU4C6%2B5YuU%2FJwHQFJSeGrkZz8T0s&X-Amz-Signature=b11d325e4f03d220df6b1a53076b037d812999aea61a0cb329598d48b2f97c55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V25QVD4D%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T045852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQCKV2HyAVrpzan1Rf%2Bbvb1%2BJt%2F9oMYwsLkwyiD5y8cyGgIhAKSq0apNHrfaORzjFwXXoQK2AeMUGZzID8MHCK0W%2FoYwKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQAw%2BbNgydR6Uqfqkq3AMArLDaNikNS8P91Bi5Z0%2BVjUcKd25ncFsKo85HYxxeX%2F0otfaKxZbKkdlekcioq8K41cnCFrCIHHVgLer8Ii28O2O5erivw5gjSst34cn%2BCPZ003Ruzxt0SlZZjNnTkH48AA2HWyCRXTubN0qHI1DwcsF58WSQDdKc9Yaq1qSGulHvTUqKl8H18ffbtRecCZq7RNkeol%2FEVQT4j4MRPvLtmG4YsELxfBIU5350QIaeMOMJLp3W3PCtG2gUvn99Ga2FA09VPCp2CCvwESU1AsLcD1EC6WPvN6vji2st4ZTQWJzYhM1uP35RY7M5XnwfW1jkbBEDuHm15HaKVi3oXwC1SUOzU3BceSNR2H7bNMcGwE75TeLl6j0ExS1RahaWsCqpKjuI9WavL4sC2%2FgA54gkXJz8yo5O9GMxigUQYUKVhwe7mpBqMSxnYx5v63%2FpPNRl%2FIm96iTbOZOS%2BtmK8VcmAkqrIIfo4QLE80XiZFqVqd%2BG03fnVqzjgFtK3RfkKnF8mDdey4AzlikJY2%2FBhgR33oedQ5IwJQD6NzB0n4HHMdRdSjmtstj5m%2F8ZFj0cH1Tj3NOBDnA1A%2BXHCPAA0Oqi%2FXNB%2Ba7w5cWjuby85BNqNsGtrD%2FldhLRLlScLTCly4vTBjqkASaGA3lbDaGiv5gbhIzBcTx4RJ%2FLT87r5e8mGOeuueDHjrRutPDqy%2F%2Bm2kMGRMD97%2BxL97iGyj0Tlqx9e5EvyJ7zlojqIQG5d8ugF2uC4gV3k%2B7BLom8CT9%2FlsVodXxeQZ6TluFnuEMoebVU8%2FIBnBy%2B%2BYe6UXp%2FgMUX%2BZdJtOAaBdONVvY9tJ%2FWgBLKgbf6XU4C6%2B5YuU%2FJwHQFJSeGrkZz8T0s&X-Amz-Signature=87fd7e910a017d6c509d8acc6327ebee8c70eac6ad67daa52cb637a7be10ff86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
