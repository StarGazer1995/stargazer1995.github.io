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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO5AEYVI%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T195955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJGMEQCIG%2FqvSUpnG6Q5anZLvSuJVur4n%2Fwdta5DTsYZ9ICYkjPAiAiwpQmy7pv%2FojArwwv2tAt8PY02158MaZZ%2Be9GtuuIdSqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmD0bOdIEftKzwtWvKtwDIJPwl02n4YtwNGYHQLYj7LbvlNyZklWGx03QGlrLUI3Y4ZvYQcQspnD3ld8kFSe2wH49z4MQ6SAmATsRhvt43fEFmBd7uIm65lUgKdfWebsaBCdabaLc9JoTO1cYKzhiurHlaovvAe3XxYzvjR3nYJTTuOJQVszEIqgLv%2BOzfvJz2oA9BbvmSUv8uVajrL07bDuKg%2FPx15SAWDQ3pyOMz8A2bB1Z26CREB%2FQzcMUUfACWOiv0WHR4q691XH3HsF9RieJz%2FRUYPeYKcX9eomth3Et3UL7zA0VxriEl1x6PFpmkKmxIp%2BHybUitX8%2Bpu1O6hMHbRH8XGZPqJfaMCx35MlDkW%2BccMFD073YWwlFVxows%2B8hvxop5AqsYe2j%2F%2FG2pgK7vZziwPCvAwvZbxn0yrext7HKBK0HxM1ut6Sy2hKX3SfL%2FwN7efTpyh3dcSeiEOgBXMliAXBuTyBmymeyZeaaqRHQxekrNnlBqcVP8vgcDjOLJoMFSwEWJFhEEqQYFEt4FSTNTmQd8iyKHmSLqGgvhGojZikP6mCtnqC9zVoxUW4RXef%2BGyuyp7erjbFxHI2yq9jZzP2WlufFo1EmndNH%2FYUJXzHiszYcFW8aLMF%2FTgMLSt5%2BlHarnXcwuLzs1AY6pgGlwQJqNCMtYYIIcynv5OCKtU05Bs8JK4wFYYUAV%2FlGqjOw7hMw1GmrEVu%2Fx3VAqSY0%2Bf0CnUWjHg7HCwfrPLWBzk8gi%2BRugacb31Xi10OxfQ9rZAZ8RexPqGXA%2FvicOgbTvnbbhIINUNwQbADhtYIVIr2ZLa5wdjdKcMlOJRdnxljANFBYUXX35t%2FKkt9uHFONwE8hpOZ0dL0H4U2uKoicjjBtnwMw&X-Amz-Signature=dabf387e520d50d7e29f2048f174d31699ed48b4f3f3fd65f7823124d1426f5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO5AEYVI%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T195955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJGMEQCIG%2FqvSUpnG6Q5anZLvSuJVur4n%2Fwdta5DTsYZ9ICYkjPAiAiwpQmy7pv%2FojArwwv2tAt8PY02158MaZZ%2Be9GtuuIdSqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmD0bOdIEftKzwtWvKtwDIJPwl02n4YtwNGYHQLYj7LbvlNyZklWGx03QGlrLUI3Y4ZvYQcQspnD3ld8kFSe2wH49z4MQ6SAmATsRhvt43fEFmBd7uIm65lUgKdfWebsaBCdabaLc9JoTO1cYKzhiurHlaovvAe3XxYzvjR3nYJTTuOJQVszEIqgLv%2BOzfvJz2oA9BbvmSUv8uVajrL07bDuKg%2FPx15SAWDQ3pyOMz8A2bB1Z26CREB%2FQzcMUUfACWOiv0WHR4q691XH3HsF9RieJz%2FRUYPeYKcX9eomth3Et3UL7zA0VxriEl1x6PFpmkKmxIp%2BHybUitX8%2Bpu1O6hMHbRH8XGZPqJfaMCx35MlDkW%2BccMFD073YWwlFVxows%2B8hvxop5AqsYe2j%2F%2FG2pgK7vZziwPCvAwvZbxn0yrext7HKBK0HxM1ut6Sy2hKX3SfL%2FwN7efTpyh3dcSeiEOgBXMliAXBuTyBmymeyZeaaqRHQxekrNnlBqcVP8vgcDjOLJoMFSwEWJFhEEqQYFEt4FSTNTmQd8iyKHmSLqGgvhGojZikP6mCtnqC9zVoxUW4RXef%2BGyuyp7erjbFxHI2yq9jZzP2WlufFo1EmndNH%2FYUJXzHiszYcFW8aLMF%2FTgMLSt5%2BlHarnXcwuLzs1AY6pgGlwQJqNCMtYYIIcynv5OCKtU05Bs8JK4wFYYUAV%2FlGqjOw7hMw1GmrEVu%2Fx3VAqSY0%2Bf0CnUWjHg7HCwfrPLWBzk8gi%2BRugacb31Xi10OxfQ9rZAZ8RexPqGXA%2FvicOgbTvnbbhIINUNwQbADhtYIVIr2ZLa5wdjdKcMlOJRdnxljANFBYUXX35t%2FKkt9uHFONwE8hpOZ0dL0H4U2uKoicjjBtnwMw&X-Amz-Signature=5e34c7cbe57cb9971ac5a5e8024f12dc5f1c6473503b8eba2ae65770720fcb17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
