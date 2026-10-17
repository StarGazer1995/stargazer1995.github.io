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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNNGFAPN%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T000138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFCtBAl2Yl4LMy4gnPet38wnS4lcxd2Y8pBpyYq%2BA99BAiEAya7SrxQZ%2BNq8VWZtKZtlqlD47GMWbjK59dPC88miKNUqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMnQU6E80p1s8VnNhyrcAy2AfkVql35H9UVYVY9Itl88lQfPAY5pQlMz73ZoO9YyC6qNClPJegyqr1sNKLHQMs%2FThBK3mvPmTiO3cM9dH9ZbOcSG79U18lIroEUs6UbxjWzn0P0uC9vPi4G9L5I8V2PbwDs4hUM0IL8YLhVFacaJlyYzPJVphtelUbmm07%2BHXLnevdHtOgeqV1Hv9vOwInB7Vx6YHqVyrLls1S%2B8kSKhCQEm58IXA0DiAKpinx2jWzqv7lQOoMGVEkhsVMwnB65rw90767LOb7XyxXkciEuH8fTJmEPAic2ducJLbUSEnvUbtIKp5gQrS%2BXdEuYswT0io6bXX07bLXy%2BiQuLvtmG%2F7HCs8%2FrjN5r%2FdpY92cQgrhgWZchMKWBZ5ZmsIwPJRbG12kSHpSNPTlc4KDXEB55YaaRNdAqpY3dViZTcuIf7a9W6O4FPqdN03MHhRxWbW%2B3dhfnHqjnL8z%2BGvsZfaQm1QDwbxWrt%2Bu3ZE%2FhQ8bTVNMe8Bv2UH86%2FI1Hh8ACDsEtNS6oMbUBmzp9QJz%2B50ec2PEqWEKqDyOfUgnlZRRLSbkxIL%2BPaza5kqEDkHF%2BujO7W3lYJA77WTVcZRFC%2BxhQNrFqy6TAHebkbNknVq5xcyYY1YmSZS1TItwcMNi7ytYGOqUB4QrM8bZt0lTv5VH5DOTus1fDYpVoha0ncyl%2BVoZFqQBBEL4eYFtV95yB8jgaGFkOp7OvOORqxrq9YkpeEgFzZwHer4of4jlTzSCpY7HZTGOic0baSshkFjzqKnompf7Q7VnOEdmnmzCqXjLKV5a4zmODwoCdD61mER8yw1CLgSn8TSAWWv3WgcqGT%2BUnLpaup8vOMlaKOsLAXzxcXnmPwrmGOUuT&X-Amz-Signature=4b641a474c41d0abf294ebd2bbcbb1ea09e1fdc7455413bef367ae2d86928049&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNNGFAPN%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T000138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFCtBAl2Yl4LMy4gnPet38wnS4lcxd2Y8pBpyYq%2BA99BAiEAya7SrxQZ%2BNq8VWZtKZtlqlD47GMWbjK59dPC88miKNUqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMnQU6E80p1s8VnNhyrcAy2AfkVql35H9UVYVY9Itl88lQfPAY5pQlMz73ZoO9YyC6qNClPJegyqr1sNKLHQMs%2FThBK3mvPmTiO3cM9dH9ZbOcSG79U18lIroEUs6UbxjWzn0P0uC9vPi4G9L5I8V2PbwDs4hUM0IL8YLhVFacaJlyYzPJVphtelUbmm07%2BHXLnevdHtOgeqV1Hv9vOwInB7Vx6YHqVyrLls1S%2B8kSKhCQEm58IXA0DiAKpinx2jWzqv7lQOoMGVEkhsVMwnB65rw90767LOb7XyxXkciEuH8fTJmEPAic2ducJLbUSEnvUbtIKp5gQrS%2BXdEuYswT0io6bXX07bLXy%2BiQuLvtmG%2F7HCs8%2FrjN5r%2FdpY92cQgrhgWZchMKWBZ5ZmsIwPJRbG12kSHpSNPTlc4KDXEB55YaaRNdAqpY3dViZTcuIf7a9W6O4FPqdN03MHhRxWbW%2B3dhfnHqjnL8z%2BGvsZfaQm1QDwbxWrt%2Bu3ZE%2FhQ8bTVNMe8Bv2UH86%2FI1Hh8ACDsEtNS6oMbUBmzp9QJz%2B50ec2PEqWEKqDyOfUgnlZRRLSbkxIL%2BPaza5kqEDkHF%2BujO7W3lYJA77WTVcZRFC%2BxhQNrFqy6TAHebkbNknVq5xcyYY1YmSZS1TItwcMNi7ytYGOqUB4QrM8bZt0lTv5VH5DOTus1fDYpVoha0ncyl%2BVoZFqQBBEL4eYFtV95yB8jgaGFkOp7OvOORqxrq9YkpeEgFzZwHer4of4jlTzSCpY7HZTGOic0baSshkFjzqKnompf7Q7VnOEdmnmzCqXjLKV5a4zmODwoCdD61mER8yw1CLgSn8TSAWWv3WgcqGT%2BUnLpaup8vOMlaKOsLAXzxcXnmPwrmGOUuT&X-Amz-Signature=c127a666b3c46104bb676bffb552a2e3b4de484e32c9dfcf4d3289c4d4828b6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
