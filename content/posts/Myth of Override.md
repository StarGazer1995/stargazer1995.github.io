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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H6V7EOB%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T101202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDruXlqFz6r99cXMDOwPxSozfDRqKaclvIFy77BxP4I8QIgXU3LKLOku4HSajfPHSzYZXsjc8rWXpfn%2BB5dDIYCQuUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDG6ckEe3YvhWdHv5OCrcA3xo2vMiaBdWoSLM%2FdMMRoiUUQOpubb0Fn1OkqhObIHuKxUycuS4sEuBgZ0L0D1NLg07HKU25Z3A9Mk%2BfxUj3jaOA0LnzxQbxKNu7MDTf%2BX2A%2FjbhCz5prJw4A1vPMT24OgvF2QZlTQE%2F4c0%2BXknIEuW%2FghLf86wlhaKR65fuxTvvMhw7lMgEeQksLkchWs6NwciDVd9KkgV0Beb%2BZqQBP%2FVNPONVl6INI1GPNoa4UqbbwB2BuKrNsUQG0TFIE0g6B4CTSPFkK28kj4s%2FRUKtQ%2BMyANiHjY7GtxJpjf51ZX9FwbQqZc0a9Ho%2F52WCaRpxjbVuz7q2FyyKHYgxjxxroaEiyTDY38YkYHpX54IrDDUWiyglVcPNsIfCl3q%2BTBe7%2BJ%2FtXWSVzG9fGe3lK5MmiyQb%2B%2BCvtHMOO8VeLdZ%2BBBDS4Q5f24DGbLggwl7%2FeWQrngGDLyTr4Cpi%2BlA5Tu3Is7hgwyfiQ6j8xeFAuy1lv7jbpuZeKX5dwkVOIoMWt%2FnMTFsyJMA4tliMBcreUHITXPU%2FW7Bv4zMmrj58SJuNia42ormSBF61pyoDKZ4cBSKQCNPZxOigfA4jAfuI2xR%2BWRgH2ayhyPcD4JwVfhyC6pFv9163nuNYCLkcZ8fMKSAhdQGOqUBNVogQE4RNUYWHBBHODpFJFxehSXDICdytcFtS61ZGNft%2FAqAe%2FiHrAvBw%2Fqf0JZC5WsTj70XjJDVx41qT31fhJQcsITHN87Vvc7lUQJMi0jvxsxH145jEBFe3JsQqVjlcuLDSjTBn%2BXklQtTb0oHUA1BkSdxhtGCGZLEfCPHvVpGG7P0k4y7DKpJNZqWt7oMvlLaX8OWrs60WJnK1Q%2BqcVRg9f8L&X-Amz-Signature=e6f156cb82f544cfcfb49b64e82a7079889c29dc221198392f9ecc201232df9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H6V7EOB%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T101202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDruXlqFz6r99cXMDOwPxSozfDRqKaclvIFy77BxP4I8QIgXU3LKLOku4HSajfPHSzYZXsjc8rWXpfn%2BB5dDIYCQuUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDG6ckEe3YvhWdHv5OCrcA3xo2vMiaBdWoSLM%2FdMMRoiUUQOpubb0Fn1OkqhObIHuKxUycuS4sEuBgZ0L0D1NLg07HKU25Z3A9Mk%2BfxUj3jaOA0LnzxQbxKNu7MDTf%2BX2A%2FjbhCz5prJw4A1vPMT24OgvF2QZlTQE%2F4c0%2BXknIEuW%2FghLf86wlhaKR65fuxTvvMhw7lMgEeQksLkchWs6NwciDVd9KkgV0Beb%2BZqQBP%2FVNPONVl6INI1GPNoa4UqbbwB2BuKrNsUQG0TFIE0g6B4CTSPFkK28kj4s%2FRUKtQ%2BMyANiHjY7GtxJpjf51ZX9FwbQqZc0a9Ho%2F52WCaRpxjbVuz7q2FyyKHYgxjxxroaEiyTDY38YkYHpX54IrDDUWiyglVcPNsIfCl3q%2BTBe7%2BJ%2FtXWSVzG9fGe3lK5MmiyQb%2B%2BCvtHMOO8VeLdZ%2BBBDS4Q5f24DGbLggwl7%2FeWQrngGDLyTr4Cpi%2BlA5Tu3Is7hgwyfiQ6j8xeFAuy1lv7jbpuZeKX5dwkVOIoMWt%2FnMTFsyJMA4tliMBcreUHITXPU%2FW7Bv4zMmrj58SJuNia42ormSBF61pyoDKZ4cBSKQCNPZxOigfA4jAfuI2xR%2BWRgH2ayhyPcD4JwVfhyC6pFv9163nuNYCLkcZ8fMKSAhdQGOqUBNVogQE4RNUYWHBBHODpFJFxehSXDICdytcFtS61ZGNft%2FAqAe%2FiHrAvBw%2Fqf0JZC5WsTj70XjJDVx41qT31fhJQcsITHN87Vvc7lUQJMi0jvxsxH145jEBFe3JsQqVjlcuLDSjTBn%2BXklQtTb0oHUA1BkSdxhtGCGZLEfCPHvVpGG7P0k4y7DKpJNZqWt7oMvlLaX8OWrs60WJnK1Q%2BqcVRg9f8L&X-Amz-Signature=bb3c72ea3c33033756dbc35f486683cfd2dc9f6b57459531ae18ee62c3d4672a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
