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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ISAVDE%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T195119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQC2KNF0pg4%2FOU3llztQTzWDS7FHbD0w7IS2SUsEQteCnwIgFzhKQZ8%2BS2fukODLU6GRG0E%2FOYH7YRX5KsCjBrjGdCkq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHCfN16aWIo8%2Bf6gAircA3C%2F1qu682b1NS1l%2FYNJayG8ZFV79fDo%2Fu%2BAmzJMSE1gimpMd6Uonwrdsh983KVRrrf3bVsi1ttw8P3s4mMhxPlaKOjfutg%2FzzvrD6RznOZNJZo1RuAy6ymajx4xD06MhqP%2F%2F3deTToyF5uH03V0ZOvG2A2MIcNIpdb7ZSUEKmvpQH%2BmaiqDgZOcYfEGfqIF26XGZbznItjZK7tYgleuR%2FIcWw1iVaB6Gz7155A9SENK2m1cWmokG0YLNe6DOHiMKiJfDC6XHC%2BXSJZhCGaF%2F3D0uPoDjBogTQw1IezyqmJrFepApHnqGYwUgGmWw3J6QYLyTTxM9risNdhvNDKxDXJoZROlvSt17GptI63Ql8HgPvUmp1F8cUIGKo1v7ICkPHALg711tgOmue%2BZgu3niuTIG9O9%2FVPZb58SkC7vz81F4luGyt03RLaHRahzr%2FiUntxMEfeNnBRJtSyWxSwJritDxH5ynyhM7ddQ9F9mVfVe2u1r5sdBW5D7lSYv4BCiv3VeCJ61f8%2BLOWY7OcmfQ3iXtX9AhW5pZ4lMOLxx1UuCYv%2BvBRv7qGgElqNfgv9Y0JLH%2BXLWuY5O4felRqM3cfKT4Vy33C8hcj%2B37pWFj7lFCM691B%2FiUxmHb3OfMKC3vNQGOqUB9L8sp6MS2wd79tXiAv9MiHXwI3nYRnBumt7Y9808g92iIdali3TvrvKoyaRIT5gHfct%2Fnj6iwTSUoTck1Idt11QCvZZmWhPC%2FOicAqz1exPVrDqN%2BnyJtK2AlTmqswr%2BD5YDLcozarmoPLK12q%2BX2LyZ1s1yiVSOAhRDjAfBpQyZKBY%2FpZIUlhjpV3%2FwrZdUvDXSr460RW%2FSlZNHzzElmKIxYnDb&X-Amz-Signature=86879e77ba07ebf0880658864608c552889597521b61e64002080bc527b8c5e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ISAVDE%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T195119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQC2KNF0pg4%2FOU3llztQTzWDS7FHbD0w7IS2SUsEQteCnwIgFzhKQZ8%2BS2fukODLU6GRG0E%2FOYH7YRX5KsCjBrjGdCkq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHCfN16aWIo8%2Bf6gAircA3C%2F1qu682b1NS1l%2FYNJayG8ZFV79fDo%2Fu%2BAmzJMSE1gimpMd6Uonwrdsh983KVRrrf3bVsi1ttw8P3s4mMhxPlaKOjfutg%2FzzvrD6RznOZNJZo1RuAy6ymajx4xD06MhqP%2F%2F3deTToyF5uH03V0ZOvG2A2MIcNIpdb7ZSUEKmvpQH%2BmaiqDgZOcYfEGfqIF26XGZbznItjZK7tYgleuR%2FIcWw1iVaB6Gz7155A9SENK2m1cWmokG0YLNe6DOHiMKiJfDC6XHC%2BXSJZhCGaF%2F3D0uPoDjBogTQw1IezyqmJrFepApHnqGYwUgGmWw3J6QYLyTTxM9risNdhvNDKxDXJoZROlvSt17GptI63Ql8HgPvUmp1F8cUIGKo1v7ICkPHALg711tgOmue%2BZgu3niuTIG9O9%2FVPZb58SkC7vz81F4luGyt03RLaHRahzr%2FiUntxMEfeNnBRJtSyWxSwJritDxH5ynyhM7ddQ9F9mVfVe2u1r5sdBW5D7lSYv4BCiv3VeCJ61f8%2BLOWY7OcmfQ3iXtX9AhW5pZ4lMOLxx1UuCYv%2BvBRv7qGgElqNfgv9Y0JLH%2BXLWuY5O4felRqM3cfKT4Vy33C8hcj%2B37pWFj7lFCM691B%2FiUxmHb3OfMKC3vNQGOqUB9L8sp6MS2wd79tXiAv9MiHXwI3nYRnBumt7Y9808g92iIdali3TvrvKoyaRIT5gHfct%2Fnj6iwTSUoTck1Idt11QCvZZmWhPC%2FOicAqz1exPVrDqN%2BnyJtK2AlTmqswr%2BD5YDLcozarmoPLK12q%2BX2LyZ1s1yiVSOAhRDjAfBpQyZKBY%2FpZIUlhjpV3%2FwrZdUvDXSr460RW%2FSlZNHzzElmKIxYnDb&X-Amz-Signature=04e44e76e410b997f1a3a7c587dd04020490ea91f04761f9863378d505e543d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
