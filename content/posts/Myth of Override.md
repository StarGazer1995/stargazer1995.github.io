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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMSGUIR%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T014823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyYgCdUBZyKvTgmBBB94jHG%2FSbl9dZ4RDNVF9D2yClawIgP5kY47raBJ8xt65%2F8uhHnapO8qlarKjbaq1GBPQm27Mq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNEzwo%2FUrt4KSz%2BjbircAx7ZLFoCWqHvByiKl6yctpu1WA2i2eo52j376kMjSGT5wldHf7CKcQNTtqpRk8HJbaXhoJfAw1StOX4X7zG6xtpzKVagM7KpsgxLGWy3svhPxXG9ucPebRAXEKtC70y8OejwDlo28DsmPQQyJNTHpsxdBCKLsN%2BEq8f3M3NscOQr%2FKIp7oZ87ZAJ0MHxPZwk%2F5QxCvLqyaTl7d8bVc5dBUwGyicPu5qtceYfxbgCb%2FzWrZdxP9pJrekt%2FoTQpT%2FnCU1puo1YUvsD%2FqtM9ABMS32grmvBeXUYI7mIxBMCxKAH%2F8wh%2FjN1ki%2FnEBd9BIA%2Fjsg7eeF1e6KihHl%2FmawZ2L0oMOTMqQ736blZUt8YubhEIW2MdtanKKkeDneKzG%2BB7XOrUB1%2BmcUrwHIB3tGqESQYd6F%2BWJxOwAoMBgJ3oBMCzRo6aSpYX3J3xTSBSlHaX54izDKcNg5NRGsPA7rdB%2B66oHGuNZtC2BQ109NCZI2lHy7vh5VlA8h0RImAnAoQx6lQmyb4tJHP7jG0nCxP%2FbwvoS5dmEzOPCPepjA%2BizLvFR5obKyNoCK39QDb6uF2pGg0DCbobsHmz1QT3g5kYfaNOIDe3TmHJFvHhokfhLWB8dMdFt46dgse2WRvMKTvh9UGOqUB7ZWTHcKs%2BTirgqouFsoSqEcH6sQHoV5OWOrVzcvDmsMPmbV%2Fm8g273Dmi6pgW%2Flf25GOelWmpRph5ZWg1ebedE7%2F%2FbFZSIop85tuk5rS6uJ2bgRoVkmx16LksoQqDpVaTkuPT2w9x3An6RVout7rA%2BjNL0qktU07p5Al3l48wwwlZhZLWVD5ebC3vukWdHaeIffC3qBaPtDyOQPQ%2FciS9ILiQljT&X-Amz-Signature=a9e04f61625a54b3f92a4c8270beeb8890135d8ce0f5281d9591682ee8423ca3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMSGUIR%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T014823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyYgCdUBZyKvTgmBBB94jHG%2FSbl9dZ4RDNVF9D2yClawIgP5kY47raBJ8xt65%2F8uhHnapO8qlarKjbaq1GBPQm27Mq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNEzwo%2FUrt4KSz%2BjbircAx7ZLFoCWqHvByiKl6yctpu1WA2i2eo52j376kMjSGT5wldHf7CKcQNTtqpRk8HJbaXhoJfAw1StOX4X7zG6xtpzKVagM7KpsgxLGWy3svhPxXG9ucPebRAXEKtC70y8OejwDlo28DsmPQQyJNTHpsxdBCKLsN%2BEq8f3M3NscOQr%2FKIp7oZ87ZAJ0MHxPZwk%2F5QxCvLqyaTl7d8bVc5dBUwGyicPu5qtceYfxbgCb%2FzWrZdxP9pJrekt%2FoTQpT%2FnCU1puo1YUvsD%2FqtM9ABMS32grmvBeXUYI7mIxBMCxKAH%2F8wh%2FjN1ki%2FnEBd9BIA%2Fjsg7eeF1e6KihHl%2FmawZ2L0oMOTMqQ736blZUt8YubhEIW2MdtanKKkeDneKzG%2BB7XOrUB1%2BmcUrwHIB3tGqESQYd6F%2BWJxOwAoMBgJ3oBMCzRo6aSpYX3J3xTSBSlHaX54izDKcNg5NRGsPA7rdB%2B66oHGuNZtC2BQ109NCZI2lHy7vh5VlA8h0RImAnAoQx6lQmyb4tJHP7jG0nCxP%2FbwvoS5dmEzOPCPepjA%2BizLvFR5obKyNoCK39QDb6uF2pGg0DCbobsHmz1QT3g5kYfaNOIDe3TmHJFvHhokfhLWB8dMdFt46dgse2WRvMKTvh9UGOqUB7ZWTHcKs%2BTirgqouFsoSqEcH6sQHoV5OWOrVzcvDmsMPmbV%2Fm8g273Dmi6pgW%2Flf25GOelWmpRph5ZWg1ebedE7%2F%2FbFZSIop85tuk5rS6uJ2bgRoVkmx16LksoQqDpVaTkuPT2w9x3An6RVout7rA%2BjNL0qktU07p5Al3l48wwwlZhZLWVD5ebC3vukWdHaeIffC3qBaPtDyOQPQ%2FciS9ILiQljT&X-Amz-Signature=8d6502ac83ff4b0d076f43673eba5e1c5c363fc1d633f835f5c8b450c677dd80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
