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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7VTXCZU%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T201421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B3zt6hjgfdXtO46Cdf8K%2FyAG0M3vLgTP5wjknjTSGCwIga29jRVC%2FrZno5bsFxWSe%2BB3S4z7A8UsjLog%2Fi0dUdwkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQ6v18evvzpR%2FsA0yrcA%2F%2BN10N4RBV0qWjAFdRBLbtrAyqhHxQvq4tqCRrLqmHu3niDL5FS7CCK%2Bz9%2FBqNMl9dc9VsUosCuzODqINTaTKT2WxcXzlC70qFrT9pHjYB4Rk0r4wONPYN48O%2BNyIY%2BjliBrXGuGY%2B1wD8WGF%2FAlopdzx7jlgljQEleoISGMCf9ouyDfHwLdsZQTitWGKCisiFBxtEbSG9dHtlIWvyK9wtUJiWhMyO1jbHtlPp6NjV0iyFjUknZy7PKBwYCPtcm69OsuEQSJG9O%2Bkw4%2BDhZ1cqjWnLyPXFnUkVJmNiGMX2dktnGXjo3Xcg2FRtGzqmWlDMU5t1bJsykBVC9j4qj9V%2FpVAQUwDUlf7OWH8vhHAdZdEfGY%2BI9Hr8jREBfLiI%2B92NSe3mxj4zUGmA2ZR%2B4QmTiNB5MlZG8Gx4hoCQnCwcGOtBz26xD3wma6vJ8fo5C%2B5nLzPYHX0H6mPCjKhRlcWccUFdqk09Gzoomw3YhDJserLUiMUAGuehZTBH7ym%2ByQkd0rcfCidh3xaZIp6KmusXirPp2MpeFooxAsng%2Flf2hfW6ydvX5R%2BQNwIijk%2F1Zs9J4LCRHKPJv46si2d4kW5tN487RRTNKaQ4RCcPH%2F6he3K5VYDy3E2pe8rU8MKz%2F%2F9UGOqUBBmpQlkNqMJ%2BzAL1nnVj68vA%2BuMnvgLeVoaL9nPXb0lmG%2BashK517Ow5FqLHfCad5L57rUKxoRxMATtXEStfQi%2Fy7nWDWhaNB2ajaUmFE9tHPXPa46MlUfQrEVakPpCQQLbiUiTkrWCWmbzpgmsR7dagilptZ1tdhsHeEZ81oYgYkWrc4n9Oh%2FGU1Zr5DDB07%2FszurGEpyaa%2FKlIGka6TS%2Bz6XUQB&X-Amz-Signature=97d0b2d9d2f0f2d9bd501a3f20349601f8d2edd98d13ce8e199dc3a053b0ebce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7VTXCZU%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T201421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B3zt6hjgfdXtO46Cdf8K%2FyAG0M3vLgTP5wjknjTSGCwIga29jRVC%2FrZno5bsFxWSe%2BB3S4z7A8UsjLog%2Fi0dUdwkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQ6v18evvzpR%2FsA0yrcA%2F%2BN10N4RBV0qWjAFdRBLbtrAyqhHxQvq4tqCRrLqmHu3niDL5FS7CCK%2Bz9%2FBqNMl9dc9VsUosCuzODqINTaTKT2WxcXzlC70qFrT9pHjYB4Rk0r4wONPYN48O%2BNyIY%2BjliBrXGuGY%2B1wD8WGF%2FAlopdzx7jlgljQEleoISGMCf9ouyDfHwLdsZQTitWGKCisiFBxtEbSG9dHtlIWvyK9wtUJiWhMyO1jbHtlPp6NjV0iyFjUknZy7PKBwYCPtcm69OsuEQSJG9O%2Bkw4%2BDhZ1cqjWnLyPXFnUkVJmNiGMX2dktnGXjo3Xcg2FRtGzqmWlDMU5t1bJsykBVC9j4qj9V%2FpVAQUwDUlf7OWH8vhHAdZdEfGY%2BI9Hr8jREBfLiI%2B92NSe3mxj4zUGmA2ZR%2B4QmTiNB5MlZG8Gx4hoCQnCwcGOtBz26xD3wma6vJ8fo5C%2B5nLzPYHX0H6mPCjKhRlcWccUFdqk09Gzoomw3YhDJserLUiMUAGuehZTBH7ym%2ByQkd0rcfCidh3xaZIp6KmusXirPp2MpeFooxAsng%2Flf2hfW6ydvX5R%2BQNwIijk%2F1Zs9J4LCRHKPJv46si2d4kW5tN487RRTNKaQ4RCcPH%2F6he3K5VYDy3E2pe8rU8MKz%2F%2F9UGOqUBBmpQlkNqMJ%2BzAL1nnVj68vA%2BuMnvgLeVoaL9nPXb0lmG%2BashK517Ow5FqLHfCad5L57rUKxoRxMATtXEStfQi%2Fy7nWDWhaNB2ajaUmFE9tHPXPa46MlUfQrEVakPpCQQLbiUiTkrWCWmbzpgmsR7dagilptZ1tdhsHeEZ81oYgYkWrc4n9Oh%2FGU1Zr5DDB07%2FszurGEpyaa%2FKlIGka6TS%2Bz6XUQB&X-Amz-Signature=acefb94befad04971c540a4094c8bdc6524105ee95b22f5f3d7a83b70086a4c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
