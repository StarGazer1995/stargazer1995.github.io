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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ5I5KXW%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T000424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDwNmKzEyTl6f7ek3MOFs04TUi%2F%2BAPbnx6LhtYjU3n3zQIgJOOl8v5pd43ok0FzCMROwJe%2FhNT5Ftr9G6DV1LaBAccqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5jqJOLYERvBh6%2BZCrcA1gk19rjY3CJpIMa11qQHkKoKVFvW3MYuKI%2FnAxJ7InD1oBU652rtrTX3s%2FmVkH0ZyTVAdewZnLhEs8pbUdhbv1JMuTOeboq4hdRhCrOlEmxn9V3cIAu%2FmRmpwhuCKUjXCYc%2F8XCfxoiEcCD7GMLHobdJD3pf6rjYVvwrGhUyacALRnMtYRpXij%2BIGx37LIZS3%2F0XSidVQHGUFx%2BfhdphIn4trY9h5TCoIOMExXnnsXYTURhDItnyL%2B0Ah8P%2FAJkJttvcfvPYvaHE%2BAvW4uKqqC1J1Q6OiLKmxvccR6X8qdeo%2F0EFI6CXqgSGvSNpjj9aOL707U9ty%2BA5u4CPJ4Dzg4T1Z%2FwiKlmUkobi6tS6HvSeR64mA82E1ek%2B6KPIKHimZr2xz1bqya%2FpoNrWDjkWmLjTW4SGPaT3Zs38hRNS%2B8gHsOv9vMWtyGUHsn7jCkjywWOvZTTO%2BvNgf7LwcD0eS3bguY6zFBo%2BNhgjouu2Rg1HcHQ08yHQ10ScgnogzqE3efZWS7o6DsP%2BCOQh167KyYGQ6BDz5qIRWpGpeE6LUgCNfrX2TH4DX%2BfNZ39aqFg9aK%2BwSJMKxnB8W9ep4uVz48Pwrr9%2Fko6K0JhZ%2FhS%2BfeMn1zZONYFIWLZhp6BMIv8odUGOqUBE5lY4g7QqhuexgGdqKb3fWfv4oo3J2bC7s0W%2FINdHpW3IgGt%2FdPPr0xcfwHeQFx4SdCMu%2F3TS9NV2qiJTc18joTE%2BdpMVuLkA7pHcK8czoayyOvJEhXrJE6bgIWBd393wCdp7ETd6VFQjjP8u8VhGX8nUb2OWaUTBAfSDpZQ58wCK1cI5iP4jpdGb5vkE%2FwdB6gX0Lo4HVM5sc%2BnoLH9s3B1hniJ&X-Amz-Signature=ca0c957fc35792a9334817930df3372bc885350600dfe7d0e5a2ae026303f5ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ5I5KXW%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T000424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDwNmKzEyTl6f7ek3MOFs04TUi%2F%2BAPbnx6LhtYjU3n3zQIgJOOl8v5pd43ok0FzCMROwJe%2FhNT5Ftr9G6DV1LaBAccqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5jqJOLYERvBh6%2BZCrcA1gk19rjY3CJpIMa11qQHkKoKVFvW3MYuKI%2FnAxJ7InD1oBU652rtrTX3s%2FmVkH0ZyTVAdewZnLhEs8pbUdhbv1JMuTOeboq4hdRhCrOlEmxn9V3cIAu%2FmRmpwhuCKUjXCYc%2F8XCfxoiEcCD7GMLHobdJD3pf6rjYVvwrGhUyacALRnMtYRpXij%2BIGx37LIZS3%2F0XSidVQHGUFx%2BfhdphIn4trY9h5TCoIOMExXnnsXYTURhDItnyL%2B0Ah8P%2FAJkJttvcfvPYvaHE%2BAvW4uKqqC1J1Q6OiLKmxvccR6X8qdeo%2F0EFI6CXqgSGvSNpjj9aOL707U9ty%2BA5u4CPJ4Dzg4T1Z%2FwiKlmUkobi6tS6HvSeR64mA82E1ek%2B6KPIKHimZr2xz1bqya%2FpoNrWDjkWmLjTW4SGPaT3Zs38hRNS%2B8gHsOv9vMWtyGUHsn7jCkjywWOvZTTO%2BvNgf7LwcD0eS3bguY6zFBo%2BNhgjouu2Rg1HcHQ08yHQ10ScgnogzqE3efZWS7o6DsP%2BCOQh167KyYGQ6BDz5qIRWpGpeE6LUgCNfrX2TH4DX%2BfNZ39aqFg9aK%2BwSJMKxnB8W9ep4uVz48Pwrr9%2Fko6K0JhZ%2FhS%2BfeMn1zZONYFIWLZhp6BMIv8odUGOqUBE5lY4g7QqhuexgGdqKb3fWfv4oo3J2bC7s0W%2FINdHpW3IgGt%2FdPPr0xcfwHeQFx4SdCMu%2F3TS9NV2qiJTc18joTE%2BdpMVuLkA7pHcK8czoayyOvJEhXrJE6bgIWBd393wCdp7ETd6VFQjjP8u8VhGX8nUb2OWaUTBAfSDpZQ58wCK1cI5iP4jpdGb5vkE%2FwdB6gX0Lo4HVM5sc%2BnoLH9s3B1hniJ&X-Amz-Signature=8821b491e767c417cbafdd1dd988345ab143eeddb440c766ecc999ce2738d3c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
