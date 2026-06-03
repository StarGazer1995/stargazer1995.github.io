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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NGCMMZ4%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T222401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIAWcH8vTPFcbKI20Wt1lVSv%2BTCiZyNB6oTIH1GcP0N%2B6AiAEA1yE6SPXrERt3n5%2F4vZWZUnGUMcbmS%2Fm0aUQbuHXUCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMTKgahdR33nSizFpwKtwD%2FK4D8UIoYySzqXs7IG6qDLk78OxcIbVm%2Fd1urI7UfpZ7uf8B8KHZmEmc17YLeAbSXJeAAVLg%2F1XMjxvPxwCJhQh%2B1CC3X%2F0PPWIEWPPbVEpKHTfzr6QeKqLR4g2D04MmRhIVrehmguH%2BsUJztYMgFLQNxikAv3Ht7dIptNG9Leur4iurNePXHnXPLMoBYzRMhZU4jQSpBdOATPitwPAUWUoyg6O0jUJt6aIVFmQxShF38NHrH8TS%2B%2FHsLFyaSI4TiOpw6AmyEOzxOqXwH%2FRyiDPHCZFPh5chXkc4IQtwUqjwdZVdRMTaAwe4Bg38xOQq1L2I5rw12rwmLIEXM3n8hdXvG7D4rbXZXWA2bSYT2X0S6dXRHPPh9ckfV0ONuG0v7r6bD7%2BgOeVwRaJgwj9pzZT%2FE5IE1tjCI92TtVfSP%2F0JX6YSZzfk%2FwqVmMiTEDsj96fFkZVdzqZ6Ed4qBRfXpA84NsJFz%2BRfvt94f6F%2F2W6QnaUlfWdvDl5xT5i%2Fq1Y%2F8hl7t2FOPtG7Qhc7kAMEcCrsUDJdyF%2FqibyVs%2BMa4wlg%2BS2VkWAGL2NogJmXSkPG1Qdq8y5GeVkjH%2FQM%2BtMMcIVTiSeJ%2FFgcagmitgWWVX%2FYGhEJie6H675JpMwwl7uC0QY6pgFvJOxP%2FVNcqW0hXZWep0h50vejBU1nG1m4B7C0g74KS1DVk2wq%2B992lgt7ZJdLkPGtBTDPnmS9O6Oz7ePOGIEKcpwJ3m8gq9VzalOsG4F6%2FA2jl4LrPdrsloRK3qdZV3HRqxKpnfeKrfnUk50VzQP%2BYmQ8w95x2efgJ7%2BQS3w83mofF78wD6Eg8rhfBeW4AYHP%2FAbdM9P0UuIz%2FnBaj%2BJ48OrUDQIP&X-Amz-Signature=4d47e2c790c9410ec79ec0d01bf20ce6e64ec356d65bd6d45db3bbfb953b5f57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NGCMMZ4%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T222401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIAWcH8vTPFcbKI20Wt1lVSv%2BTCiZyNB6oTIH1GcP0N%2B6AiAEA1yE6SPXrERt3n5%2F4vZWZUnGUMcbmS%2Fm0aUQbuHXUCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMTKgahdR33nSizFpwKtwD%2FK4D8UIoYySzqXs7IG6qDLk78OxcIbVm%2Fd1urI7UfpZ7uf8B8KHZmEmc17YLeAbSXJeAAVLg%2F1XMjxvPxwCJhQh%2B1CC3X%2F0PPWIEWPPbVEpKHTfzr6QeKqLR4g2D04MmRhIVrehmguH%2BsUJztYMgFLQNxikAv3Ht7dIptNG9Leur4iurNePXHnXPLMoBYzRMhZU4jQSpBdOATPitwPAUWUoyg6O0jUJt6aIVFmQxShF38NHrH8TS%2B%2FHsLFyaSI4TiOpw6AmyEOzxOqXwH%2FRyiDPHCZFPh5chXkc4IQtwUqjwdZVdRMTaAwe4Bg38xOQq1L2I5rw12rwmLIEXM3n8hdXvG7D4rbXZXWA2bSYT2X0S6dXRHPPh9ckfV0ONuG0v7r6bD7%2BgOeVwRaJgwj9pzZT%2FE5IE1tjCI92TtVfSP%2F0JX6YSZzfk%2FwqVmMiTEDsj96fFkZVdzqZ6Ed4qBRfXpA84NsJFz%2BRfvt94f6F%2F2W6QnaUlfWdvDl5xT5i%2Fq1Y%2F8hl7t2FOPtG7Qhc7kAMEcCrsUDJdyF%2FqibyVs%2BMa4wlg%2BS2VkWAGL2NogJmXSkPG1Qdq8y5GeVkjH%2FQM%2BtMMcIVTiSeJ%2FFgcagmitgWWVX%2FYGhEJie6H675JpMwwl7uC0QY6pgFvJOxP%2FVNcqW0hXZWep0h50vejBU1nG1m4B7C0g74KS1DVk2wq%2B992lgt7ZJdLkPGtBTDPnmS9O6Oz7ePOGIEKcpwJ3m8gq9VzalOsG4F6%2FA2jl4LrPdrsloRK3qdZV3HRqxKpnfeKrfnUk50VzQP%2BYmQ8w95x2efgJ7%2BQS3w83mofF78wD6Eg8rhfBeW4AYHP%2FAbdM9P0UuIz%2FnBaj%2BJ48OrUDQIP&X-Amz-Signature=afbf7cd5aed75dbbc7e64e0da90b7cdd55de40c131cdbfe36f38991d6f209137&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
