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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQS7666I%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T075922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6wgd1OhdhwnEM1sRnnVgOFCa%2Bgu0xL9ekHRUeXS2tRAiAg8DiTuHvw3s9gx1cysJG59W3yjneK8Kn08YCRZ%2FGi9Sr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMCAhby1ozW2oBp5JrKtwD8PFfexZIuu6RH5ESJuEj6%2FDbLzF2c3gJvRFsC4cZHweBla9BxQnQLMvdtnU6zkPQBEqnX3Y6AVUGnRRv5xYB2sx3lJ2LB7Ks9dgBXdZWXfb4MM8dsgpH8laAXJGp9prAvM%2FEmOL9TN43YlbwUHrnN4hEDxA6CzjhC9E2b1WCoei2K1dsDWtnFkIn3yth4ERI3vhi7rGMGTatSG1P69iTA2ZtPYQ9yCr6WzaV74iJcFgtyWQzhPzIenG2qv2TiuNNAriCd4ebHRFcVLopoN1MWOFzV%2FlJNpmZRobfjVd4RSWk5yMLsiIxgFfXy9%2F7dZ5CeVqkaxk%2BOcJH4f6e%2BNAvA%2BM6CcYAwWeB86IGsQUqmEDEymHPzPMoMTjDco0rkdTbpQDR0QgoLUInExG3kHT7lwJ1oUvidWsmlTTf8GWOO1rL55zK2cJnhoJkhkBBZ4g7wz1NKfskMkL4cVBI4CO4p7eP7BmZJfzfXOrUGAuDdkXD82UIDF3HSTjnfcwEpvYev7mWH4G%2F1eKbr6ysUhDvr4OEGBL4a318tDp5NL%2Fs7iZbwFQmPpYN%2FD4lFn0cReArwiS6xxKH7IS01NQyBkiT2DVouW%2BfVi5OxIzrRm1qmnVKK%2BqvUHPDeGdjpF8wouCJ0QY6pgFpCozQBsCNXH6F3TJrMWE8AUU9Yn1XBYGqXkiXrMETxaawx8ZPstowGyqJnCGhEpE7KsXeuLbb7YAkI%2BJq49wC8zopqRyZtdGNGQMKlT513zV8%2BKyZNPmJqPvkf7F8V8qyulbVhTDACZ77kuOhNVW2K1HGU6KN7DfhcPPQwLVGMYsMn7D8TCbgF9zdlJtYu7JmVMoPrCfRo4xiHvnGesnn1ENdD4SJ&X-Amz-Signature=c6d309371fcbeb38536ffc4cb0da5e942bad1b6abc4dc4b8bc14bb82f2f1e36d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQS7666I%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T075922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6wgd1OhdhwnEM1sRnnVgOFCa%2Bgu0xL9ekHRUeXS2tRAiAg8DiTuHvw3s9gx1cysJG59W3yjneK8Kn08YCRZ%2FGi9Sr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMCAhby1ozW2oBp5JrKtwD8PFfexZIuu6RH5ESJuEj6%2FDbLzF2c3gJvRFsC4cZHweBla9BxQnQLMvdtnU6zkPQBEqnX3Y6AVUGnRRv5xYB2sx3lJ2LB7Ks9dgBXdZWXfb4MM8dsgpH8laAXJGp9prAvM%2FEmOL9TN43YlbwUHrnN4hEDxA6CzjhC9E2b1WCoei2K1dsDWtnFkIn3yth4ERI3vhi7rGMGTatSG1P69iTA2ZtPYQ9yCr6WzaV74iJcFgtyWQzhPzIenG2qv2TiuNNAriCd4ebHRFcVLopoN1MWOFzV%2FlJNpmZRobfjVd4RSWk5yMLsiIxgFfXy9%2F7dZ5CeVqkaxk%2BOcJH4f6e%2BNAvA%2BM6CcYAwWeB86IGsQUqmEDEymHPzPMoMTjDco0rkdTbpQDR0QgoLUInExG3kHT7lwJ1oUvidWsmlTTf8GWOO1rL55zK2cJnhoJkhkBBZ4g7wz1NKfskMkL4cVBI4CO4p7eP7BmZJfzfXOrUGAuDdkXD82UIDF3HSTjnfcwEpvYev7mWH4G%2F1eKbr6ysUhDvr4OEGBL4a318tDp5NL%2Fs7iZbwFQmPpYN%2FD4lFn0cReArwiS6xxKH7IS01NQyBkiT2DVouW%2BfVi5OxIzrRm1qmnVKK%2BqvUHPDeGdjpF8wouCJ0QY6pgFpCozQBsCNXH6F3TJrMWE8AUU9Yn1XBYGqXkiXrMETxaawx8ZPstowGyqJnCGhEpE7KsXeuLbb7YAkI%2BJq49wC8zopqRyZtdGNGQMKlT513zV8%2BKyZNPmJqPvkf7F8V8qyulbVhTDACZ77kuOhNVW2K1HGU6KN7DfhcPPQwLVGMYsMn7D8TCbgF9zdlJtYu7JmVMoPrCfRo4xiHvnGesnn1ENdD4SJ&X-Amz-Signature=cdedcb56abe91d5be44fb56fbe4b6d268b9e3de150ca1e3fa6fc8ce24aecf612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
