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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SIJE2QB%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T185327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQD5WlwQSt39IK%2F4UMPVu9jTk4%2Bhjjy9%2FdfXLHblvhjIKwIhANUAvt1BrjuGPAa7rFL3AdOaXz7y0ll13qJoxYnw1f9rKv8DCDkQABoMNjM3NDIzMTgzODA1IgzBJr1r3jFzMbEPU6Qq3AN1Jbvvz7IicxUHsPc3jQDiKSELeIbjnZtFEOwxOWGcqjo8lCPzWo2NRT3N4VJD5LdYUYAyeEItWIw25ACQvHfQA2CMRXYckg35RLOGIIK7qHy%2BxAWhJiVX86fm4Nk0jqx6%2FPO5FTnH8sat3HjflGkiAwAN%2BehZpt5lXrs6SkyMs0UgGRtJRPDcRdMs77RW0AzvvFXjm1lqo%2FBLvRKilL8%2BBUVryAOCIqb91OQCozky5Hey6JMKpPExyhzQS%2Ft6SlzVMBCQkb4U%2BMJtbbI5DOIopacKO58ufo%2B1S%2B6Ur7BAW00Q7AaXft96egnQpPpQ40hXXmAXKS6BpT93FNEZMUWqpYo7pvyshuTM%2FeQh%2FHYANeytNeC5kdUejo9AhbiEqZllyc0IvrXHkNS6b0Unkvvs6AT7KE6ChI2wdcHCjzc09BSY0D%2F5OtvT7Sib3bJlKWl0x4Nn%2B3JDY8cKYKj%2BkgIrb4f9ORzwmAv2L0J7c4v1H7RRnspxdcfQFZsml48hVCSmHTRs3FH%2FJ3xzg%2F4wJsBnybWoDsarmODLGyQmd1TvrAOql%2BdBemFNQCMmC7UDt1P5zQeRS%2B%2B1azPpjV73aFNZrsjXJlOewrdGN71pyMlkRtMV5hP65ORvu2ZktTCa6JjTBjqkAXBg9GxsyF36yvcxeMwHH6PVYa%2BYsjH%2FVE6ES9DN8i6XzCaw6hcaxyvxLPp924hRJI%2BGO2NMcSCyJuK%2BQb1A0a9tmCYn72DPYuhGDWQ3TncKdUcrSxJ4NcEw4XOYLHZKHk2IzHUghIImrZYaTac4njfDsmkV1x%2FA%2B9P0HT0X1n2v5nb1PBlHvl164klz%2Btdy8VlgBLTNcFMarPLJHRLRt6J1I3%2Fc&X-Amz-Signature=e9a8367fcbb6a16a4aab2d052b5075920d30b667950bc6b6d9239d146c1b3ddc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SIJE2QB%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T185327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQD5WlwQSt39IK%2F4UMPVu9jTk4%2Bhjjy9%2FdfXLHblvhjIKwIhANUAvt1BrjuGPAa7rFL3AdOaXz7y0ll13qJoxYnw1f9rKv8DCDkQABoMNjM3NDIzMTgzODA1IgzBJr1r3jFzMbEPU6Qq3AN1Jbvvz7IicxUHsPc3jQDiKSELeIbjnZtFEOwxOWGcqjo8lCPzWo2NRT3N4VJD5LdYUYAyeEItWIw25ACQvHfQA2CMRXYckg35RLOGIIK7qHy%2BxAWhJiVX86fm4Nk0jqx6%2FPO5FTnH8sat3HjflGkiAwAN%2BehZpt5lXrs6SkyMs0UgGRtJRPDcRdMs77RW0AzvvFXjm1lqo%2FBLvRKilL8%2BBUVryAOCIqb91OQCozky5Hey6JMKpPExyhzQS%2Ft6SlzVMBCQkb4U%2BMJtbbI5DOIopacKO58ufo%2B1S%2B6Ur7BAW00Q7AaXft96egnQpPpQ40hXXmAXKS6BpT93FNEZMUWqpYo7pvyshuTM%2FeQh%2FHYANeytNeC5kdUejo9AhbiEqZllyc0IvrXHkNS6b0Unkvvs6AT7KE6ChI2wdcHCjzc09BSY0D%2F5OtvT7Sib3bJlKWl0x4Nn%2B3JDY8cKYKj%2BkgIrb4f9ORzwmAv2L0J7c4v1H7RRnspxdcfQFZsml48hVCSmHTRs3FH%2FJ3xzg%2F4wJsBnybWoDsarmODLGyQmd1TvrAOql%2BdBemFNQCMmC7UDt1P5zQeRS%2B%2B1azPpjV73aFNZrsjXJlOewrdGN71pyMlkRtMV5hP65ORvu2ZktTCa6JjTBjqkAXBg9GxsyF36yvcxeMwHH6PVYa%2BYsjH%2FVE6ES9DN8i6XzCaw6hcaxyvxLPp924hRJI%2BGO2NMcSCyJuK%2BQb1A0a9tmCYn72DPYuhGDWQ3TncKdUcrSxJ4NcEw4XOYLHZKHk2IzHUghIImrZYaTac4njfDsmkV1x%2FA%2B9P0HT0X1n2v5nb1PBlHvl164klz%2Btdy8VlgBLTNcFMarPLJHRLRt6J1I3%2Fc&X-Amz-Signature=44405c7b30a01c438ca0cd6b99c5555b8b46684a5add76d6291bfba70f171838&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
