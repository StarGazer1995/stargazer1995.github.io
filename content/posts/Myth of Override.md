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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPIWYBFA%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T165132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDUU83ovNf%2BsaXxpR3VxBJ8QFI%2Bgo0Sl0jKaNLfQHVCUAIgJVpSLEqkUDvol%2BJnkQcFK%2BSRhekDxae%2BYoUNsLiIWLUq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDEjj%2BVlqk0tAzIWlVyrcA4d7js3cHE6GuF54ZHqu33tVKAfF0OOh3o%2FLPul2%2Fnlpt%2FwG2AyhySAPIT%2FVFibBN9nnchfkbp2rb1v%2F1smX%2BF%2F4NNDQwoGEQYcxodaqU5A5t2Sz1om6AuO5Zobg%2BEXmDTpTmukqKFjXviK4pVmBMBAO88o%2BXyOr8ljWL9bxHIxoe4%2Fo980WeK96GlSVR0GYkyx3wkaOo4JG%2BagCVhB%2B0KPHBwgfyuy20iKXrPEA9UG1zmxJb%2FXf9hidHa6PZCc0pUSBwebAKXPrT2xRDZ2F1d301H81H2zjHHazQ3w9Kw0NsXGnuUUZapkXb8BaXTuARQ3dxVSmEWdFw3aUvgnlmahx2lk6ee7qbDGJLregiOsgXJxtjRwyxiJ4KH9qQOSX%2BtHsKL72Hb7QCgqiwqKIt2q1LFmm5we5wKDf62otAxQtN75HCzy8mIyvwBxm0hETpGHZxoeNJW4aKAA53rUNemH3zKU%2FD5dJWenGrB8wX5bgJqagIfiBVQqu%2FzUMiN2JUR3A5DI%2Fv3hN5aAv77bTkZUgG0pV1PNNkmo4iLMXe1GgoNH%2FKzIVAuOgA%2BKY9RLxwAD1fJk%2FVC5CCuSWZQlOAJdxcr0JQiBw%2BHXyD%2BTTITaeNfcmbWxtbK1ZvXyuMO7CpNIGOqUBCigjZyolu1myNW5C%2BmXYGb9EecR4QT3vMQ5N08Ya3npMEa9CWER3f20V8Vuy47Ci8xPir8TJW2NqkN6WIYyqOR9asHdsyEq0rrImR45RyGGtG9x0fQoVonWPu0KbgqbPYot5IDXw1xewleueSMdntOw1xrZCbk%2F43wr2CKDrF5gAQXw0C47Ft1M7Pg0UAC3mKidOK2OO47gQ8T6r1zxsnKTsc5AM&X-Amz-Signature=ee82fa8977153e8d8aab6d6caa7ce6aa1b592baeffdfd28903bbf81684699f9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPIWYBFA%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T165132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIQDUU83ovNf%2BsaXxpR3VxBJ8QFI%2Bgo0Sl0jKaNLfQHVCUAIgJVpSLEqkUDvol%2BJnkQcFK%2BSRhekDxae%2BYoUNsLiIWLUq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDEjj%2BVlqk0tAzIWlVyrcA4d7js3cHE6GuF54ZHqu33tVKAfF0OOh3o%2FLPul2%2Fnlpt%2FwG2AyhySAPIT%2FVFibBN9nnchfkbp2rb1v%2F1smX%2BF%2F4NNDQwoGEQYcxodaqU5A5t2Sz1om6AuO5Zobg%2BEXmDTpTmukqKFjXviK4pVmBMBAO88o%2BXyOr8ljWL9bxHIxoe4%2Fo980WeK96GlSVR0GYkyx3wkaOo4JG%2BagCVhB%2B0KPHBwgfyuy20iKXrPEA9UG1zmxJb%2FXf9hidHa6PZCc0pUSBwebAKXPrT2xRDZ2F1d301H81H2zjHHazQ3w9Kw0NsXGnuUUZapkXb8BaXTuARQ3dxVSmEWdFw3aUvgnlmahx2lk6ee7qbDGJLregiOsgXJxtjRwyxiJ4KH9qQOSX%2BtHsKL72Hb7QCgqiwqKIt2q1LFmm5we5wKDf62otAxQtN75HCzy8mIyvwBxm0hETpGHZxoeNJW4aKAA53rUNemH3zKU%2FD5dJWenGrB8wX5bgJqagIfiBVQqu%2FzUMiN2JUR3A5DI%2Fv3hN5aAv77bTkZUgG0pV1PNNkmo4iLMXe1GgoNH%2FKzIVAuOgA%2BKY9RLxwAD1fJk%2FVC5CCuSWZQlOAJdxcr0JQiBw%2BHXyD%2BTTITaeNfcmbWxtbK1ZvXyuMO7CpNIGOqUBCigjZyolu1myNW5C%2BmXYGb9EecR4QT3vMQ5N08Ya3npMEa9CWER3f20V8Vuy47Ci8xPir8TJW2NqkN6WIYyqOR9asHdsyEq0rrImR45RyGGtG9x0fQoVonWPu0KbgqbPYot5IDXw1xewleueSMdntOw1xrZCbk%2F43wr2CKDrF5gAQXw0C47Ft1M7Pg0UAC3mKidOK2OO47gQ8T6r1zxsnKTsc5AM&X-Amz-Signature=b3e12c2ae38f0ce4350aa27d56edd4520ed80b0536e28769354d25ddf9648212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
