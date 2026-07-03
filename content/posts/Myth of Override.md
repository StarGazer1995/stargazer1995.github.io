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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T3LMFQY%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T014629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCbDnLGn4IIhixSfIxs3u4PucZid9OeR5Z16ftqPqLd6wIhAN6b52IBNR481qmfP52%2BVABNeubzYvNZvlTcMbqWEWVbKv8DCAAQABoMNjM3NDIzMTgzODA1IgxJvLRPL7l9H4Ms%2FJcq3ANqDdL81v8UzApVJK%2BuxWSafX0hbYw39akjf3R%2BtWCcEfOyCY%2FPp3Tuu0fHTZlNHd7XUIyeSI10qAPI78QVLqrJ2jtSILuDLzFYoTYVwYl9%2Bev03H4Ytwbh%2FrpI9zw2Elz%2BXhexRqZudbUtY9xV3Yx3OTMrPTYqD8zUUAF7zNklEtIsHUombJpdbfRpPlr1vY5lGmW5Ka5E8LAMMPVxN3voi%2BFj4aY6rn1mZ90U7CRb2t178CrNfY5MU%2FtGPim2Wj3keo%2FAORxLpYVyTozbtbxQdH77GBYyoDd2n%2FurQMCeT0rbJpbZjTMVufJkgtpyOcw%2F9vbHuRGtQvW3uHIwK7%2FPc1F1RyGbdvnPeqiVX6cI43sbV9hmzjdwVCKIEdCmOlmWp8Qf1%2FFWZ7tcwke6LpUKKEbhLNCq3Vf2%2FZasQSDjTgoi%2Bgdr6S0v%2BjN%2F%2BuBeCBDyuo84%2Bo7%2FOV8G%2BrpCdynZPnLdDYMth3wQP4Vxw1BdXKHavyj9xu5vdjF3%2Ff3WDkr1dQptuN1b9WZoYS7g8mP%2BZOGHUhNyD07w6dT6ILRVD2QFSI%2BP3v3E1hvf70xUnev2xDn%2F%2BvNApGhZzCH4d8ErRLh%2FjLBpYSZFRntFh%2BJaPHVyrbnE1h9YHZ0EKDC11ZvSBjqkAUXOXuxYkYibUUV%2B5OCTP1nSpP%2BfSiKqHdb58%2BcBrEug4KYjwv8p9GayzveOWLA9KsgOCJ8Bq1C5wfi9uE7vk3kwu3i4bwomtDVyjZt%2Bb%2FfSX6VRZg3K1d0wCeNqX7DFAqjawTwy1l8bj2r1cmurZ9SzSUeyrE8UWf4THF2Q%2BKZ2zzfBPpYfM2EgxJZkqvti3wqpR%2BgQiKeh32ROL69lVcoG8UyB&X-Amz-Signature=4afc6f8c42a4273e82c20e9be64117de304c3385f231f832d7a6329ebc7d7bc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665T3LMFQY%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T014629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCbDnLGn4IIhixSfIxs3u4PucZid9OeR5Z16ftqPqLd6wIhAN6b52IBNR481qmfP52%2BVABNeubzYvNZvlTcMbqWEWVbKv8DCAAQABoMNjM3NDIzMTgzODA1IgxJvLRPL7l9H4Ms%2FJcq3ANqDdL81v8UzApVJK%2BuxWSafX0hbYw39akjf3R%2BtWCcEfOyCY%2FPp3Tuu0fHTZlNHd7XUIyeSI10qAPI78QVLqrJ2jtSILuDLzFYoTYVwYl9%2Bev03H4Ytwbh%2FrpI9zw2Elz%2BXhexRqZudbUtY9xV3Yx3OTMrPTYqD8zUUAF7zNklEtIsHUombJpdbfRpPlr1vY5lGmW5Ka5E8LAMMPVxN3voi%2BFj4aY6rn1mZ90U7CRb2t178CrNfY5MU%2FtGPim2Wj3keo%2FAORxLpYVyTozbtbxQdH77GBYyoDd2n%2FurQMCeT0rbJpbZjTMVufJkgtpyOcw%2F9vbHuRGtQvW3uHIwK7%2FPc1F1RyGbdvnPeqiVX6cI43sbV9hmzjdwVCKIEdCmOlmWp8Qf1%2FFWZ7tcwke6LpUKKEbhLNCq3Vf2%2FZasQSDjTgoi%2Bgdr6S0v%2BjN%2F%2BuBeCBDyuo84%2Bo7%2FOV8G%2BrpCdynZPnLdDYMth3wQP4Vxw1BdXKHavyj9xu5vdjF3%2Ff3WDkr1dQptuN1b9WZoYS7g8mP%2BZOGHUhNyD07w6dT6ILRVD2QFSI%2BP3v3E1hvf70xUnev2xDn%2F%2BvNApGhZzCH4d8ErRLh%2FjLBpYSZFRntFh%2BJaPHVyrbnE1h9YHZ0EKDC11ZvSBjqkAUXOXuxYkYibUUV%2B5OCTP1nSpP%2BfSiKqHdb58%2BcBrEug4KYjwv8p9GayzveOWLA9KsgOCJ8Bq1C5wfi9uE7vk3kwu3i4bwomtDVyjZt%2Bb%2FfSX6VRZg3K1d0wCeNqX7DFAqjawTwy1l8bj2r1cmurZ9SzSUeyrE8UWf4THF2Q%2BKZ2zzfBPpYfM2EgxJZkqvti3wqpR%2BgQiKeh32ROL69lVcoG8UyB&X-Amz-Signature=0c55feab86e561c961f5a7c19353ada08de1354b506fcd8199aa3c9f13262613&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
