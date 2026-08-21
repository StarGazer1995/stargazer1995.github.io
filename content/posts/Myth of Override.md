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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634EZB4DL%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T182032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD92zhZoQ%2BRc6p4bJcS6b4nYKh9kJts8k9aWf%2BFG2du6AIhAN2sMjysJxQB04%2FwgroTpPfo2ERxm6gitYG2yW7G12RTKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtyNMn1Oelu2379ysq3AO5GqkOC9GQHTLNHcFuiV9GBIUafQiKSjmqQWbxL%2F8l6nx3QLN4E7m9UCSNCPL43mmSwLEnfMHfvHB7LHkCm2O8ptKK5Js%2FmbiYjQLXThxS4POkbZqPZeIb7HPWMCVxhTkjV0eISQeKM2JYGw4VH6jQSazGC%2FMtifzbVFYl%2FBiI3y4K3YMLprtyeeycY3ogAuvQT661ZC0p47VYYLLLAsWV%2BHgS6Sl3cMXPaqoBR7B6orZJL5A0bhAM9sVZyQTVX0q3nnEFiqX3HfSJbw8CqbpP5wsT7OCtauUoWblkuRgv2j%2BJ8QvrlpVzBmAC7a0ZuQsDiy4nf1mVFZijx6XhUsI7nDBz2fMA3he8tddjoZ%2Bp9O4rcp%2FYfXraE43YFvk27aQoLk%2Fra0AsPzDL8HntYeal6%2FKgerMepZ0IoAzYLG5wywkiAmOvs3qcX3j2aAGSYHgfUnEsLxwK30N98POmOtfuoSQ8dM6eSnVeKjqsW%2BhIS%2FAvEkhrXQTVsnToS3Oz4YM1QOrMvzw1WUb8K%2B4RQ6VHs1OqwzT9U0Wl8k0AZjnr16ar8k418TCrHrfryG8XqnZaVJgfi%2BBv2eycunPAg%2BDRS0luYU6EkRgJf4MYSYy7Z5%2FV4uPu%2F1ir1sSm1TCh%2FKHUBjqkAazn3G6evanIgi8p5pYZyjcpyJpvQdxor3BQnjTsnpHeGwulg3n6DiqU8k80HVHtizxI5nBkCT1Zr7RtZz9lnbGZ7gwBOr3Jvk3UDUALxzYH2KmEL54AbTrEeC4pQ2ulYeOL3CGA1TZf%2FU1yrJr5%2B1V8BlfUUrhPJa7UWcifIcuglQDUcsSmEQfQ%2FeEeGBTrJoqSSVyKYa1SyMy19042CgaPmAC4&X-Amz-Signature=83570257d399a5cf55787979cc43867c7d0d232057ebad83f572bb17bdec1a2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634EZB4DL%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T182032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD92zhZoQ%2BRc6p4bJcS6b4nYKh9kJts8k9aWf%2BFG2du6AIhAN2sMjysJxQB04%2FwgroTpPfo2ERxm6gitYG2yW7G12RTKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtyNMn1Oelu2379ysq3AO5GqkOC9GQHTLNHcFuiV9GBIUafQiKSjmqQWbxL%2F8l6nx3QLN4E7m9UCSNCPL43mmSwLEnfMHfvHB7LHkCm2O8ptKK5Js%2FmbiYjQLXThxS4POkbZqPZeIb7HPWMCVxhTkjV0eISQeKM2JYGw4VH6jQSazGC%2FMtifzbVFYl%2FBiI3y4K3YMLprtyeeycY3ogAuvQT661ZC0p47VYYLLLAsWV%2BHgS6Sl3cMXPaqoBR7B6orZJL5A0bhAM9sVZyQTVX0q3nnEFiqX3HfSJbw8CqbpP5wsT7OCtauUoWblkuRgv2j%2BJ8QvrlpVzBmAC7a0ZuQsDiy4nf1mVFZijx6XhUsI7nDBz2fMA3he8tddjoZ%2Bp9O4rcp%2FYfXraE43YFvk27aQoLk%2Fra0AsPzDL8HntYeal6%2FKgerMepZ0IoAzYLG5wywkiAmOvs3qcX3j2aAGSYHgfUnEsLxwK30N98POmOtfuoSQ8dM6eSnVeKjqsW%2BhIS%2FAvEkhrXQTVsnToS3Oz4YM1QOrMvzw1WUb8K%2B4RQ6VHs1OqwzT9U0Wl8k0AZjnr16ar8k418TCrHrfryG8XqnZaVJgfi%2BBv2eycunPAg%2BDRS0luYU6EkRgJf4MYSYy7Z5%2FV4uPu%2F1ir1sSm1TCh%2FKHUBjqkAazn3G6evanIgi8p5pYZyjcpyJpvQdxor3BQnjTsnpHeGwulg3n6DiqU8k80HVHtizxI5nBkCT1Zr7RtZz9lnbGZ7gwBOr3Jvk3UDUALxzYH2KmEL54AbTrEeC4pQ2ulYeOL3CGA1TZf%2FU1yrJr5%2B1V8BlfUUrhPJa7UWcifIcuglQDUcsSmEQfQ%2FeEeGBTrJoqSSVyKYa1SyMy19042CgaPmAC4&X-Amz-Signature=1b414512ccd948a7ff40371a2836f304d038b0e2cd0857507c16b149cb46b79f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
