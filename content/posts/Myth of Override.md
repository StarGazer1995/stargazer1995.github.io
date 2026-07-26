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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EXTGDNE%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T012856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDmuFMoOV9c9UUiukpALMDKEBAviWTWLvxY6aF50SjtjgIhAMKHiQEcfo4OJbq7LltWHawwzYSsYsKk4fbTEgOGxvYkKv8DCCoQABoMNjM3NDIzMTgzODA1Igze8CRfc5T%2FtmvmZF0q3APv8xyV966fxhil32qdqRbYB%2FPX4ie92v51bwnCQvXzEItdp%2BPhb5Aj2F8I%2Fv0Xyfrs9xrFSKmlmxd%2FlFJ5FjZLlJ%2Bi%2FtRWhMHod4suwSlpIk07xO5ygujTMC%2Fk8qdQQ%2FXtjENWTNzJW%2BxjfHB09WIFuRfGKs%2Bx5HLI0ONjXYrxzlNsTluJE6Iks8nYDnHi1AmJv%2BdZYMgmYxe%2FhaepemVzYHLTJkrqwSav7RF5y%2Ftbpy9VKhTskL50HkKQJuZoUhFQ8bBJHS5SD%2F1ykwpRh6e7b3duPzdeuD9HzQfCAzYs3%2F%2B%2BrIrzmg8f2cS5%2FpavLz6U3Lamlgut3%2B%2B4de5KRf%2B4u7%2FeqOCvwvrKhL4877z9iYNL2G4KNcDrU4SNbwf09jj%2Fhk0wS07w%2Btmxtj4sRDtxPoJq%2BbeOkmMgCS4KkvM67g1m9z7o9KYUlvfseFEk9yr5nXhZFo9eB%2BqKdhBBhNeD8aqwSPiqty7BZ99S5Ve0wRl3HHmAPFDp1VBw1lLYPIGwXWxFmXra8wP8i3IAQI%2BrPGXWULOs0FVsZ0wrACgLwfwOGNaA%2FvfEt%2BzZa%2BI5iuYGsFq7aHJvXIZzTyxDBmrhBucbzHacC%2Fc7OpgF05hH%2B2RcsN6khvqe%2FgpJIzDNqZXTBjqkAdyeKoiTG9xPvFK5IGybOzOf9aXoeoi9IkbteNhne03T8xqklUJYOHD9DTrmzGtKUu7PTM6VhXtJhMT%2Fpti6Im%2BRQnYGa0jlVX1UANFF5o8pF2iclAAZa5Iis4VNpeCn4A0RI6jOxbN4mfpZhVtUfFJweR5NBautfieo73bcbdfzWJs5YOKEFJxhGMs%2BUVVUuIN4DeTg2Qjf93OrMAgFDpDr%2BtQl&X-Amz-Signature=a9cb8495267d3ee8aef18b1c5565ffc756e55e0f66ed36977e000fd807964b02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EXTGDNE%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T012856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDmuFMoOV9c9UUiukpALMDKEBAviWTWLvxY6aF50SjtjgIhAMKHiQEcfo4OJbq7LltWHawwzYSsYsKk4fbTEgOGxvYkKv8DCCoQABoMNjM3NDIzMTgzODA1Igze8CRfc5T%2FtmvmZF0q3APv8xyV966fxhil32qdqRbYB%2FPX4ie92v51bwnCQvXzEItdp%2BPhb5Aj2F8I%2Fv0Xyfrs9xrFSKmlmxd%2FlFJ5FjZLlJ%2Bi%2FtRWhMHod4suwSlpIk07xO5ygujTMC%2Fk8qdQQ%2FXtjENWTNzJW%2BxjfHB09WIFuRfGKs%2Bx5HLI0ONjXYrxzlNsTluJE6Iks8nYDnHi1AmJv%2BdZYMgmYxe%2FhaepemVzYHLTJkrqwSav7RF5y%2Ftbpy9VKhTskL50HkKQJuZoUhFQ8bBJHS5SD%2F1ykwpRh6e7b3duPzdeuD9HzQfCAzYs3%2F%2B%2BrIrzmg8f2cS5%2FpavLz6U3Lamlgut3%2B%2B4de5KRf%2B4u7%2FeqOCvwvrKhL4877z9iYNL2G4KNcDrU4SNbwf09jj%2Fhk0wS07w%2Btmxtj4sRDtxPoJq%2BbeOkmMgCS4KkvM67g1m9z7o9KYUlvfseFEk9yr5nXhZFo9eB%2BqKdhBBhNeD8aqwSPiqty7BZ99S5Ve0wRl3HHmAPFDp1VBw1lLYPIGwXWxFmXra8wP8i3IAQI%2BrPGXWULOs0FVsZ0wrACgLwfwOGNaA%2FvfEt%2BzZa%2BI5iuYGsFq7aHJvXIZzTyxDBmrhBucbzHacC%2Fc7OpgF05hH%2B2RcsN6khvqe%2FgpJIzDNqZXTBjqkAdyeKoiTG9xPvFK5IGybOzOf9aXoeoi9IkbteNhne03T8xqklUJYOHD9DTrmzGtKUu7PTM6VhXtJhMT%2Fpti6Im%2BRQnYGa0jlVX1UANFF5o8pF2iclAAZa5Iis4VNpeCn4A0RI6jOxbN4mfpZhVtUfFJweR5NBautfieo73bcbdfzWJs5YOKEFJxhGMs%2BUVVUuIN4DeTg2Qjf93OrMAgFDpDr%2BtQl&X-Amz-Signature=7c8498b578e2f4e5f36739acc34d3f2f1422618d9efa7a954aa707c221ff9176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
