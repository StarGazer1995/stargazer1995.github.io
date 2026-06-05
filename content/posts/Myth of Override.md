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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I74SPBC%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T020627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhIdqjxz71eC5r23satr2%2BnZ1Mop6WXgwfH%2BJ8WFwgzAiEApgAMVfeeAXejD8t%2Bp1pL2DW3WCSJWuGatQ0YLV2yZIsq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCiUey5uYYOS80KeICrcA4N85p1edJZhFmR6EG3ai%2FBmuQAjhbZSMusyl%2B5VXNbkaTmZxowGvX0HKPu%2FoFKuEx1OHkPfjE9SoQNZ8Lf8JiZx7da38sRWzlyAzvX0kfqW1gye3lR7yl5I7XAp%2Fd1qEn6B6JHKF7Zyg73cRdq%2FFDxkFDaxznnS1kyE5i0U4KTU1TcD1bYTJg8wPuHq7bhpDZhl46RAtXhKyROrk8Cvv7LYKwfS5w%2FrfuznCqDzRcSbUbEtciyNX7QFz5nohfn02%2F1JKXIz3oy8w1on9dka73b8NMkPAHwTXOdOtw3aFGaaAGUkhxPYQwj8tNeklF%2BqdUXeqQCkhCfy9DJezhPVGv3usNSIHuF%2FteDWq80a1kdrTOknCYpA7pFPv71EzQnpo5MBZS7B%2Fcn8tjjOG982i9u%2Fbv7M5mT%2Br3X9hGq4YT5X27QJboY9gN1%2BccBtABEU3ccKhY2ud2mTzVIc1APrzFBYNAly3zqYi9N2K1iXffob12YAiY1Qse8PrXn8eyil9qARlV9nR78dWn5VB1wIdiO7Lda99twXKEdk8Vkv0c2jUwhzcQCrXXvNT9SF40lPpKlBSdN16KVhziNF7yv3u2JbyWTN3hQiW8r8%2BNu81dn%2BCBLsglBhGkcRSoPTMIPNiNEGOqUB8hhLIAQa2OQi3o%2B%2FaGqETAIRwlU%2FfaGEyxvB5OzHlv1A%2BF5aJ8G0VbtY6zt8EKd2MuOOXomXibJnTQP9ugK27j3ulyQ%2B9HSHqTujGvc2jd3gKM%2BbcDmh3JRLBlbUvTrQv526xY2RbqHvv3ZCxzEDpRz9eifn3yMqCHESPPY%2BME277%2BlwXRG8eRnjru7mwz46uARtMXmwjATrWxnboCLiuwiZQzER&X-Amz-Signature=778d5cdf3fbb15261729a19c6b6659870b30cdc5b86f4575eaa61f58781242e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I74SPBC%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T020627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhIdqjxz71eC5r23satr2%2BnZ1Mop6WXgwfH%2BJ8WFwgzAiEApgAMVfeeAXejD8t%2Bp1pL2DW3WCSJWuGatQ0YLV2yZIsq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDCiUey5uYYOS80KeICrcA4N85p1edJZhFmR6EG3ai%2FBmuQAjhbZSMusyl%2B5VXNbkaTmZxowGvX0HKPu%2FoFKuEx1OHkPfjE9SoQNZ8Lf8JiZx7da38sRWzlyAzvX0kfqW1gye3lR7yl5I7XAp%2Fd1qEn6B6JHKF7Zyg73cRdq%2FFDxkFDaxznnS1kyE5i0U4KTU1TcD1bYTJg8wPuHq7bhpDZhl46RAtXhKyROrk8Cvv7LYKwfS5w%2FrfuznCqDzRcSbUbEtciyNX7QFz5nohfn02%2F1JKXIz3oy8w1on9dka73b8NMkPAHwTXOdOtw3aFGaaAGUkhxPYQwj8tNeklF%2BqdUXeqQCkhCfy9DJezhPVGv3usNSIHuF%2FteDWq80a1kdrTOknCYpA7pFPv71EzQnpo5MBZS7B%2Fcn8tjjOG982i9u%2Fbv7M5mT%2Br3X9hGq4YT5X27QJboY9gN1%2BccBtABEU3ccKhY2ud2mTzVIc1APrzFBYNAly3zqYi9N2K1iXffob12YAiY1Qse8PrXn8eyil9qARlV9nR78dWn5VB1wIdiO7Lda99twXKEdk8Vkv0c2jUwhzcQCrXXvNT9SF40lPpKlBSdN16KVhziNF7yv3u2JbyWTN3hQiW8r8%2BNu81dn%2BCBLsglBhGkcRSoPTMIPNiNEGOqUB8hhLIAQa2OQi3o%2B%2FaGqETAIRwlU%2FfaGEyxvB5OzHlv1A%2BF5aJ8G0VbtY6zt8EKd2MuOOXomXibJnTQP9ugK27j3ulyQ%2B9HSHqTujGvc2jd3gKM%2BbcDmh3JRLBlbUvTrQv526xY2RbqHvv3ZCxzEDpRz9eifn3yMqCHESPPY%2BME277%2BlwXRG8eRnjru7mwz46uARtMXmwjATrWxnboCLiuwiZQzER&X-Amz-Signature=b94e9d15267f206e585077db79a64f53c230f223a4e538b6cbf9c80c383ba581&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
