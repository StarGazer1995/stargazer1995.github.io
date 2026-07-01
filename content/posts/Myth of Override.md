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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YX4CZK3Y%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T021003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCID7HNdYlkhTCjOCwNY84E0gNen9qeA5HaQfSmp5UqK2WAiEAiUbXwhb3PSnD0t1UQnWnkEKqNAK90wALvicNqtyI3ZsqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzymConNFwhmZFdryrcA6JcouEgMU1zaGa2i8n6f6D4isyxdaAw%2B4CbBIruyOt4XSZAOKs6fA980eDjlJ34FWVuCdPa0NOa7xuzjSS4I8EtX1Q1wItDDsspWpD%2FgBn6SL8GGEDy%2FeYGbJUYlUTLef0ze%2FOvdithP8oEkH5L9%2FcsLpDj%2FtsGGPq1zMz2Y0KAoaCibZpHryBlTLjFQyPfnSZyvMVaR2hJZ%2Fvb1wfHx5RkLC8A34cA9bCZHAPxSeOXn%2F%2B%2Bvkl9lnQvhwQ9hfUJ24WNGZLnHVvQuPDOyzVF8AwOfe3YTFpOjs%2BoWQt3um6cu0S4%2B72yvHlmtz%2BRIgyovDtGKwtGn04eIL8PK%2B%2FlI1%2BtMgmRvO1uesHtD6lHsS%2F%2B4f8KpXoDV3nPdiv1zdRdEpqWNVI4nKWGVVxdwkOZ8FDnorc4yCpOkjGHz4akF0uLmcpGXH7hc1E2X5RlF1gQNcsMl3OGu3lElHrzrnJbbiZnhyIFxKWv6V8Eh7tOwQXIi6wGQr46ve0wGiKZBLE7lRV0%2FnavKQ61HyUgXmX%2FF3uV73fwo71S9WPHdL1Q99sAZ9V8q8vFeKLHskjI%2BCyYcODaKUq3j4Q9mOo1tYqnOp781Q17r92PcULxHry9kbXtCDG5%2Ff9m%2FACKZJR%2FMNnokNIGOqUBabC42D0geb%2BXJJzLZQUyOXMRwbChEEEbKAzQ4CACnw4WenVGMngw5L2Y9xwh0r7PMJV17vN8GnsXVfvFEDIfmcl%2B2Xb3S1K08X%2BIrdCzqmRrftomduu5I4SV6TDr%2Bx4AKYsIUe6gThUsZnoMmVOGnmd9vtP2JV2WnNGfqAqtE6ULbDDclMwUG26wUv4SVibrSMnMmiub7s6qZBkmcS1tp4Z27isc&X-Amz-Signature=000d82721673bfc84fe455abbcbb7e46b357d382e69cbe956d3981c331d8a0d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YX4CZK3Y%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T021003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCID7HNdYlkhTCjOCwNY84E0gNen9qeA5HaQfSmp5UqK2WAiEAiUbXwhb3PSnD0t1UQnWnkEKqNAK90wALvicNqtyI3ZsqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzymConNFwhmZFdryrcA6JcouEgMU1zaGa2i8n6f6D4isyxdaAw%2B4CbBIruyOt4XSZAOKs6fA980eDjlJ34FWVuCdPa0NOa7xuzjSS4I8EtX1Q1wItDDsspWpD%2FgBn6SL8GGEDy%2FeYGbJUYlUTLef0ze%2FOvdithP8oEkH5L9%2FcsLpDj%2FtsGGPq1zMz2Y0KAoaCibZpHryBlTLjFQyPfnSZyvMVaR2hJZ%2Fvb1wfHx5RkLC8A34cA9bCZHAPxSeOXn%2F%2B%2Bvkl9lnQvhwQ9hfUJ24WNGZLnHVvQuPDOyzVF8AwOfe3YTFpOjs%2BoWQt3um6cu0S4%2B72yvHlmtz%2BRIgyovDtGKwtGn04eIL8PK%2B%2FlI1%2BtMgmRvO1uesHtD6lHsS%2F%2B4f8KpXoDV3nPdiv1zdRdEpqWNVI4nKWGVVxdwkOZ8FDnorc4yCpOkjGHz4akF0uLmcpGXH7hc1E2X5RlF1gQNcsMl3OGu3lElHrzrnJbbiZnhyIFxKWv6V8Eh7tOwQXIi6wGQr46ve0wGiKZBLE7lRV0%2FnavKQ61HyUgXmX%2FF3uV73fwo71S9WPHdL1Q99sAZ9V8q8vFeKLHskjI%2BCyYcODaKUq3j4Q9mOo1tYqnOp781Q17r92PcULxHry9kbXtCDG5%2Ff9m%2FACKZJR%2FMNnokNIGOqUBabC42D0geb%2BXJJzLZQUyOXMRwbChEEEbKAzQ4CACnw4WenVGMngw5L2Y9xwh0r7PMJV17vN8GnsXVfvFEDIfmcl%2B2Xb3S1K08X%2BIrdCzqmRrftomduu5I4SV6TDr%2Bx4AKYsIUe6gThUsZnoMmVOGnmd9vtP2JV2WnNGfqAqtE6ULbDDclMwUG26wUv4SVibrSMnMmiub7s6qZBkmcS1tp4Z27isc&X-Amz-Signature=fea5805d23c9df01e490870ba598964189e1e7d33a8508c753a0d0935f9892e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
