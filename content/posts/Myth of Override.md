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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I4XOT4R%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T203036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjWuQCuPVDcmGSzjQhdoprcA8ehSuLXKXN97S1bf9XXQIhAJrk6th8JikQVJeM6VFq0kp9qN8YdaK3qxWhqRF%2Fr6XdKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwKRgMrmJeBEp8KcGkq3AOKJtYRVhv06989Dwd2JuvvUgWhScpE%2F8Bk804E8vCwl0xRSpyX%2BxMq8rzyf%2Fw9OIODjx77ODHd4O4Nv8lr0%2F2AEraGaBNf3zsbJ4aSJ2jgPDmvrCzWRw7DplXv8tRCrDxlSmcHjD6dtY5Y%2BIkdhPBz360WQUDkJsK6OXO2%2FE2uyQXV6ZMmoGKMeGms1mxchxUsiq9Do%2F4aJ8iXPoSSZjDLQi4wGYj0EeFYn3cYKAQzTQ0e2mDbokZzOCIRocsviCaFSJ9gzNPs20DPXYXJSIKS1VZVOjOlCV%2BttSeyixLpiSn1M8g8%2FNFyaUIoniiE07HZHawPj1KMKnnJ13Ju8IfqSHuP3eiw%2BMmPd1RqGdqAZXfNc%2BW4n2IlBqU%2B%2FAI5nq6N8hbZAeOEad6o9uZEIliKe1XNHYq0L5oMULcfryBtLxBcL8yxlLwdhQIYp7SKl1NB4ezAMQsfAvk6PgMPln27XcyZguh8Taey67G43XciKwUxWw1psjCAfVZ3oSFZtltDxsOA3LPz1Ry14l3bc6ubxQkHaphPTG6kdJfKhe9HzKlGCXlZGjRKQ7GnijAah8pPQhW4OaUFToovHk0PWFUNxIWZG3GMq9q%2BgV93yeXaAdW86aDtxI5AP57Z4zDLuOjTBjqkASuJCeiapoWCZdi7FZoKs2lvvEbyLptALkc9XG2AqeNow77Gq4oIiJLHcpsNfrj1RAFLfP2ux39mXlzw1fHyC4muvMFA77wJj6ZkCHWL1pcEYjDHc2xhDW%2BwG73Wsi9jRc4jF3MItaqG6FcYYHEGUahbGCg2Cqlflz4ISH7Hs3EDLZqck%2BdDMnvU5IxvH7T1R1YGD14uUWX67l56Vn9s5Kvq0Jbt&X-Amz-Signature=8296856169059e65cd8f1b68d016943587bc0f0076dcb985667a690fd2d2ae40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662I4XOT4R%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T203036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjWuQCuPVDcmGSzjQhdoprcA8ehSuLXKXN97S1bf9XXQIhAJrk6th8JikQVJeM6VFq0kp9qN8YdaK3qxWhqRF%2Fr6XdKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwKRgMrmJeBEp8KcGkq3AOKJtYRVhv06989Dwd2JuvvUgWhScpE%2F8Bk804E8vCwl0xRSpyX%2BxMq8rzyf%2Fw9OIODjx77ODHd4O4Nv8lr0%2F2AEraGaBNf3zsbJ4aSJ2jgPDmvrCzWRw7DplXv8tRCrDxlSmcHjD6dtY5Y%2BIkdhPBz360WQUDkJsK6OXO2%2FE2uyQXV6ZMmoGKMeGms1mxchxUsiq9Do%2F4aJ8iXPoSSZjDLQi4wGYj0EeFYn3cYKAQzTQ0e2mDbokZzOCIRocsviCaFSJ9gzNPs20DPXYXJSIKS1VZVOjOlCV%2BttSeyixLpiSn1M8g8%2FNFyaUIoniiE07HZHawPj1KMKnnJ13Ju8IfqSHuP3eiw%2BMmPd1RqGdqAZXfNc%2BW4n2IlBqU%2B%2FAI5nq6N8hbZAeOEad6o9uZEIliKe1XNHYq0L5oMULcfryBtLxBcL8yxlLwdhQIYp7SKl1NB4ezAMQsfAvk6PgMPln27XcyZguh8Taey67G43XciKwUxWw1psjCAfVZ3oSFZtltDxsOA3LPz1Ry14l3bc6ubxQkHaphPTG6kdJfKhe9HzKlGCXlZGjRKQ7GnijAah8pPQhW4OaUFToovHk0PWFUNxIWZG3GMq9q%2BgV93yeXaAdW86aDtxI5AP57Z4zDLuOjTBjqkASuJCeiapoWCZdi7FZoKs2lvvEbyLptALkc9XG2AqeNow77Gq4oIiJLHcpsNfrj1RAFLfP2ux39mXlzw1fHyC4muvMFA77wJj6ZkCHWL1pcEYjDHc2xhDW%2BwG73Wsi9jRc4jF3MItaqG6FcYYHEGUahbGCg2Cqlflz4ISH7Hs3EDLZqck%2BdDMnvU5IxvH7T1R1YGD14uUWX67l56Vn9s5Kvq0Jbt&X-Amz-Signature=a2b0c7ca7c6d96ac00c0801011c34ad0f2af526c31f78f8203ee2285ae9da9ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
