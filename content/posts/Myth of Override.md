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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7ZZQ2ZH%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T051542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKADzOAjdFeoeQ9zgp4VkIY%2BAUe05wKEupssCjlIaO0gIhAIH0CaHvdR%2F%2Bb4B7rFAue58A4yiRA7pVFJ1Clf3ujCZVKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzT5t2ZHj9%2BrXuv7NAq3AOWGqG5TQYD8eORNb%2BbCTuMih9QUZ%2FISAFKcOZOE9kzU%2FWrJMLIzhhpxiM0Q%2BI%2B2%2FwDoJGBTvzCF4e2Q0W8%2F%2FYFJV%2FlMl%2BeaP8PRN4yry23%2BDFtEPdZxeU2%2B9jvBOZ53wPs9YtiXR%2FvhYgmkpInfNbW%2FIiid4E57L3ZHbulxv6oUEs0m0lO0g%2FgbvyapIG210MFxRl06VgudQTwGgFNekrTIxeJG%2FnUNJBX1jwNKYQvaKmyHjh3sV56ArL3IyBTCi9wkft7L0z19HJwlxlVJhGtClzEVJz9AJa3ycspqMEYwkAqTUNGYWtZBuqujCtcubtFn2q8%2FLM8mWHi0Y5tPdIsp%2FsavBSZQee%2F%2BKrLff0LapTzqKVlkMwQ7%2Bh7It9Mwnm766%2BV%2BRXmSxDrBXBzwfOLFaqHsGicVDsHnMwMaIGgA2HkE%2BWEKnVrfe8GHAZMIV94umF2eTYePAJIDguOagpBgmZgNBMrIH%2BOioBIoSCw6GSQVRpHJ3WlPxJAvP0DvMa4QrUscX%2F%2B0CL%2B%2BXCcaV3xCnnbWhyoWvZk4oV%2BhLMv2rDB7RsM7m6X4S31HNwBMXmDKyzVSqaWJLVNGd8f%2BVZ3mLiNYg%2F7drLW1wg3Bkz8Ti58avNchZnkDTLiZTDdluXTBjqkAX573%2F91TDFU8WEdiq7jl1uauqhDU%2Fh16XHqshWt2odAPNQJiAg5uyvSnlVu%2FQOlhnOwb1VOj1%2B2oVqcKSND8d9ZG12DDDMvLT9A3D4LVnqJaZWss%2B%2FAEf057nuXBwoRfvF7nCspnfZ%2BJI6SCV1CNJFeZ%2BAiIEXrmRcgyRbH%2Bjn4vE81q5rStJmXBBLb%2BWpIYNSPtkWHJIAOTKg%2BiEOl120Un9ia&X-Amz-Signature=fdafef6a01e6384fd840d6305f1fdd60b279b2c0b468b4eb5e8c617b3c820d69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7ZZQ2ZH%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T051542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKADzOAjdFeoeQ9zgp4VkIY%2BAUe05wKEupssCjlIaO0gIhAIH0CaHvdR%2F%2Bb4B7rFAue58A4yiRA7pVFJ1Clf3ujCZVKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzT5t2ZHj9%2BrXuv7NAq3AOWGqG5TQYD8eORNb%2BbCTuMih9QUZ%2FISAFKcOZOE9kzU%2FWrJMLIzhhpxiM0Q%2BI%2B2%2FwDoJGBTvzCF4e2Q0W8%2F%2FYFJV%2FlMl%2BeaP8PRN4yry23%2BDFtEPdZxeU2%2B9jvBOZ53wPs9YtiXR%2FvhYgmkpInfNbW%2FIiid4E57L3ZHbulxv6oUEs0m0lO0g%2FgbvyapIG210MFxRl06VgudQTwGgFNekrTIxeJG%2FnUNJBX1jwNKYQvaKmyHjh3sV56ArL3IyBTCi9wkft7L0z19HJwlxlVJhGtClzEVJz9AJa3ycspqMEYwkAqTUNGYWtZBuqujCtcubtFn2q8%2FLM8mWHi0Y5tPdIsp%2FsavBSZQee%2F%2BKrLff0LapTzqKVlkMwQ7%2Bh7It9Mwnm766%2BV%2BRXmSxDrBXBzwfOLFaqHsGicVDsHnMwMaIGgA2HkE%2BWEKnVrfe8GHAZMIV94umF2eTYePAJIDguOagpBgmZgNBMrIH%2BOioBIoSCw6GSQVRpHJ3WlPxJAvP0DvMa4QrUscX%2F%2B0CL%2B%2BXCcaV3xCnnbWhyoWvZk4oV%2BhLMv2rDB7RsM7m6X4S31HNwBMXmDKyzVSqaWJLVNGd8f%2BVZ3mLiNYg%2F7drLW1wg3Bkz8Ti58avNchZnkDTLiZTDdluXTBjqkAX573%2F91TDFU8WEdiq7jl1uauqhDU%2Fh16XHqshWt2odAPNQJiAg5uyvSnlVu%2FQOlhnOwb1VOj1%2B2oVqcKSND8d9ZG12DDDMvLT9A3D4LVnqJaZWss%2B%2FAEf057nuXBwoRfvF7nCspnfZ%2BJI6SCV1CNJFeZ%2BAiIEXrmRcgyRbH%2Bjn4vE81q5rStJmXBBLb%2BWpIYNSPtkWHJIAOTKg%2BiEOl120Un9ia&X-Amz-Signature=e973c101fecbb4a7866996215815dd91f87f22e5a096e5710050a9259fa75d43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
