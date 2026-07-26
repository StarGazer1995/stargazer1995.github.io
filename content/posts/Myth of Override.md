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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5PRT7A%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T204505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQCk6thMgvCEont2Z5Lvf0Bgke5XfR0tSc5AwdkymQc2VwIhAIO3eb3BFm7YPz2zKVJOTT1iAkQiTJuZz4hahx6fmjizKv8DCDkQABoMNjM3NDIzMTgzODA1IgyhOQ2gCxt8QCqJhc0q3AMN8yL8qHbgM9d%2FGryLA1oO82hhCx8TpSnCNbs%2FEfB7psloOizPh1G0cqS3x0poKaKmb52S9tAtIm%2B5q%2ByJcrmFmjJ8clu9V8AxWCQ4zUXZ8H8dNbLDh6FD3rSlDucuUx%2FRrGIUU5R6tuv8QxQiuwJxd8fReGihh3hUFgWb1gCNLqIZxZr0dlc4XABFjBEKFSwCzNiPThZ8ZuOuif1O%2BjUgj435ZrZMXGnU%2B7nh9UKuFJQUT8XIf2ukchqLqYWdxkLoQzAvB6dDBQG75JIkSi4OPmoUS6PcJcOzLC8svF%2BM7Q8Fx1xbBZ1WVOJQiQWPrsM%2BCL803SMqQicc1m%2BLuOHfPbjYvp316VZGYwhw%2B1TIOdJFTsNd8xbG93QNOPL1nL8a%2Bw8eOtcU8kVU5%2Bsh6WCfuXS2hKm71M3Z7Y6GR9e%2FJZXtK2sn65cXcNzajT3ldrJpRg9VkwPM2oKQRTYZp1q2DPdZ%2BoImjkkGCMmPhKz%2F1Qzw4bLaCnU12x%2BfkXhAyzTZNLDyG017aItIKkVQez1Xq7TD842qHal065xmD%2BC7RwvIrOSvVOg%2F%2F9zLsAPBmWCEArK6e12BqBnBF%2Bc4zWEPYw9I6XkxQE7upOyVx4HyvY54cicWaADec%2F1wizDO6JjTBjqkAStxnJBQyQyL5ncusc7hvyjOJJQCx2Bp8snRT%2BC3LlPI%2BDfgglxWECtCXAvhtOguQzHZV1jjl%2FkLH5OZyni8gWCuGb5F1u25e%2B8zhn0NoG67Dv5WDQG5ZYcZP%2BkxTmIy1ruRUbOoN0GP%2F1NW1B8kfNSBWC%2F99fPsUhtA3BQ3aWqZ8R753yqTgPbSHkT4pPgePrE8QSgZ7pVFMn12npItaIy6XqWR&X-Amz-Signature=8fb1afbe03613d8227f84f13682d5ea7aded813c528a9bd63468406f64833127&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5PRT7A%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T204505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQCk6thMgvCEont2Z5Lvf0Bgke5XfR0tSc5AwdkymQc2VwIhAIO3eb3BFm7YPz2zKVJOTT1iAkQiTJuZz4hahx6fmjizKv8DCDkQABoMNjM3NDIzMTgzODA1IgyhOQ2gCxt8QCqJhc0q3AMN8yL8qHbgM9d%2FGryLA1oO82hhCx8TpSnCNbs%2FEfB7psloOizPh1G0cqS3x0poKaKmb52S9tAtIm%2B5q%2ByJcrmFmjJ8clu9V8AxWCQ4zUXZ8H8dNbLDh6FD3rSlDucuUx%2FRrGIUU5R6tuv8QxQiuwJxd8fReGihh3hUFgWb1gCNLqIZxZr0dlc4XABFjBEKFSwCzNiPThZ8ZuOuif1O%2BjUgj435ZrZMXGnU%2B7nh9UKuFJQUT8XIf2ukchqLqYWdxkLoQzAvB6dDBQG75JIkSi4OPmoUS6PcJcOzLC8svF%2BM7Q8Fx1xbBZ1WVOJQiQWPrsM%2BCL803SMqQicc1m%2BLuOHfPbjYvp316VZGYwhw%2B1TIOdJFTsNd8xbG93QNOPL1nL8a%2Bw8eOtcU8kVU5%2Bsh6WCfuXS2hKm71M3Z7Y6GR9e%2FJZXtK2sn65cXcNzajT3ldrJpRg9VkwPM2oKQRTYZp1q2DPdZ%2BoImjkkGCMmPhKz%2F1Qzw4bLaCnU12x%2BfkXhAyzTZNLDyG017aItIKkVQez1Xq7TD842qHal065xmD%2BC7RwvIrOSvVOg%2F%2F9zLsAPBmWCEArK6e12BqBnBF%2Bc4zWEPYw9I6XkxQE7upOyVx4HyvY54cicWaADec%2F1wizDO6JjTBjqkAStxnJBQyQyL5ncusc7hvyjOJJQCx2Bp8snRT%2BC3LlPI%2BDfgglxWECtCXAvhtOguQzHZV1jjl%2FkLH5OZyni8gWCuGb5F1u25e%2B8zhn0NoG67Dv5WDQG5ZYcZP%2BkxTmIy1ruRUbOoN0GP%2F1NW1B8kfNSBWC%2F99fPsUhtA3BQ3aWqZ8R753yqTgPbSHkT4pPgePrE8QSgZ7pVFMn12npItaIy6XqWR&X-Amz-Signature=6e8f6ff4f66b4594f2845a1a1797f3b1dcde591069342118e7d97738782513ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
