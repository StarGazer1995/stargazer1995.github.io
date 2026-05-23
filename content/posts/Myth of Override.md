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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIIR3P53%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T224244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDv61TVIHRTy%2BG0gT6a1gFjimKcvzHPcFJptemwCBDCmgIgB3kxBinGxp03CuFvuo0I%2BcMgR9V4aaQkLUiBjEaL%2Fzoq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDBRKrL1hi87wGUitryrcA2IGK2O6zkQLWjiojHfQEdpTHaU4ik2hLgdZ6kpQCLttAbuSHYxsWpCwm4o%2FUFEQGAumWL81wDv%2BQDfgdYpNjYJvPwwgrDzWzb5v97o73%2BS%2B3ESd4VYNHO0WCmyBbANgt%2BN3t8QegYln0yclQnjI2THqhwLWoTevQs64llAzhYbiM2qHlJ5I%2B%2FR5%2Fo%2BnBytX6WawuGrMGlxLAYFQn8IVKpgtiEQ%2BSZpkSX8xWfVb0TSubtrJiJ6OQec3ujKmYslSRH6RNL6mwQssn%2FKKNqknnemi8SB8YrRB4nSl9d1RumCob0FcMyoTLV8blUj3xGI1Z47iS3YVr5pgch0W8axuXXW1u9N9AOJ3g9V1WMRdQ%2B1tPhn3m5F9rrx3ybup2jiXN3XfJBqyUQndxnXbVJ3lxMPs61hAImyRpTPwZD1GK4ysyWzmFwGFAD5lQqj0CgRulBn6tgR32O7uz1xXuCIEv9hhszqf%2BBUKMhlL8me9rLOIS8StR3E6eHwPuEXBGBkcZg4FhExwzkoG%2BAIWfWqN%2B%2Fnd5PaOc3n38nFp8c%2FYgxY7b7t36feMiDfy%2F7wTY0mmZan9vAP2Ss%2Bv85s%2B1xscmxZwoh%2FJhDn%2FUTm2EQd15KnHeYJVMZcYZVTvtJglMK7MyNAGOqUBnMJGgDuXytBM7UHUcDTq8CHTMyRZKG3TclOhiuAFcXdEaW17%2FNyeBQByV6aIn%2BocwVozGtHhe%2F%2F%2BYwidLLxH1GYlzlM0WI1LU8haJTl5uQTTTcf3S3pu22awTfQ%2B4obAofL74VGVaLzLqkC84niZHUmuRNMT4IeJlz2UCrCLBxhhydd4gwnDW9NEjcKhZXxhM2KdG6JIb6LUxVDb%2FlvZ0bMG1B1P&X-Amz-Signature=058676a958ffdabfd92de265443a7e01e2db59d223d9e546c1fff5eeca014401&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIIR3P53%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T224244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDv61TVIHRTy%2BG0gT6a1gFjimKcvzHPcFJptemwCBDCmgIgB3kxBinGxp03CuFvuo0I%2BcMgR9V4aaQkLUiBjEaL%2Fzoq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDBRKrL1hi87wGUitryrcA2IGK2O6zkQLWjiojHfQEdpTHaU4ik2hLgdZ6kpQCLttAbuSHYxsWpCwm4o%2FUFEQGAumWL81wDv%2BQDfgdYpNjYJvPwwgrDzWzb5v97o73%2BS%2B3ESd4VYNHO0WCmyBbANgt%2BN3t8QegYln0yclQnjI2THqhwLWoTevQs64llAzhYbiM2qHlJ5I%2B%2FR5%2Fo%2BnBytX6WawuGrMGlxLAYFQn8IVKpgtiEQ%2BSZpkSX8xWfVb0TSubtrJiJ6OQec3ujKmYslSRH6RNL6mwQssn%2FKKNqknnemi8SB8YrRB4nSl9d1RumCob0FcMyoTLV8blUj3xGI1Z47iS3YVr5pgch0W8axuXXW1u9N9AOJ3g9V1WMRdQ%2B1tPhn3m5F9rrx3ybup2jiXN3XfJBqyUQndxnXbVJ3lxMPs61hAImyRpTPwZD1GK4ysyWzmFwGFAD5lQqj0CgRulBn6tgR32O7uz1xXuCIEv9hhszqf%2BBUKMhlL8me9rLOIS8StR3E6eHwPuEXBGBkcZg4FhExwzkoG%2BAIWfWqN%2B%2Fnd5PaOc3n38nFp8c%2FYgxY7b7t36feMiDfy%2F7wTY0mmZan9vAP2Ss%2Bv85s%2B1xscmxZwoh%2FJhDn%2FUTm2EQd15KnHeYJVMZcYZVTvtJglMK7MyNAGOqUBnMJGgDuXytBM7UHUcDTq8CHTMyRZKG3TclOhiuAFcXdEaW17%2FNyeBQByV6aIn%2BocwVozGtHhe%2F%2F%2BYwidLLxH1GYlzlM0WI1LU8haJTl5uQTTTcf3S3pu22awTfQ%2B4obAofL74VGVaLzLqkC84niZHUmuRNMT4IeJlz2UCrCLBxhhydd4gwnDW9NEjcKhZXxhM2KdG6JIb6LUxVDb%2FlvZ0bMG1B1P&X-Amz-Signature=4f49e0f89f5b8eb34643a6355a4b61d40544e04e09b7b8bd0c05f2811331a49f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
