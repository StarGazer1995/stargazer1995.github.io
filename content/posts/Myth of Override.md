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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYEMNGTD%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T164054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJGMEQCIC%2FVADgeKHhx9yLJRph6YNzG3%2BSRtwrJRWsB8AD6PqvrAiALqAPF93DdEg4NsNuSjcAKgka4ZkvBpK9m2PVc3IrE9iqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYWhQrS8j0Xn0eWMDKtwDv%2BDZXGu7S7y%2BPbs%2BJhv6NObp%2FKHgD%2FY1NYnHsFyZ0I8LIn7CNmlul77r4aStwB%2BiTO527Ke4ee0bh%2F%2FNserOK9dcvpBzej9VALZyge%2FQyjUSNIJqaBKQIqIMOdDlUfsXn7K1aP1BfaXO0phuAnruCuRmZMbRWxVH%2BOrPXdKMkbkOd5czwipIm%2F%2B66h%2FWapIv4U%2FVKQ4L2OgDOzypKILoRBnHGCx9ip6MoSvyvVetjPNjEhNXWQIi9juh37uTqQ%2BXi403orgB9NXruQHEBNS9lFkk1ROoF%2BBbCGeIV7iuwhdeSF4UwuVZ7wnF4tHd1DQRg6P6KJkvmmkMyi%2BUiGwFmV%2BXyYMIyd8dF%2FAYTFJX%2BNxj7RynT411DW%2B9xY4U6f0bbuyzxsBtg8ThyS3R3u6QMYZrQhahvIUElNavTHMlXgW%2By6bPDtDwcdmMOJvl%2FPR%2Fjv7HkTQb%2FiYVSMXmyfJ1ibo0ZmmXkLwrwS7V92hciySZLKyxZPBM9nU0P%2BOl2mT2%2FFq%2Fa8j3JScm6fAluurh0%2FdKojWyRWI6LOyUbYH4DnXcTtTvoYmiKlVmFZPPucq%2BOc7m6rl5Lw4Qdh%2BdrzkZS%2BbVhiPTY%2FiCt1bvngd8FT5fEDIgsyNsTQKaHlUwz7z9zwY6pgHhfJEdN%2F%2FGu3GA4ON4j%2BNVI142Z2xOHHlLvGOsWOw6UWJpT7aS3G%2B63TYF5kR9wARKkcmeT6K4XkH%2Bc21X1ouOkXxb1MkOCG7%2BOPK8vWpOHyXAcndikFJRjpJuQi6gNBMyUaGZ5G%2FYpRVk0Ab9JSCcU2xnCNNiCTyxpwhyNNKIuWNK3BNaybUhJZJzBNkA%2F9AR1cPc5QZZBQCDqn0b%2FZqS%2BxMQ6Z2q&X-Amz-Signature=4b395a54dd441b81a9a86cd0e08feabd182143d85aa9da30ebf0cf112714a0eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYEMNGTD%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T164054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJGMEQCIC%2FVADgeKHhx9yLJRph6YNzG3%2BSRtwrJRWsB8AD6PqvrAiALqAPF93DdEg4NsNuSjcAKgka4ZkvBpK9m2PVc3IrE9iqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYWhQrS8j0Xn0eWMDKtwDv%2BDZXGu7S7y%2BPbs%2BJhv6NObp%2FKHgD%2FY1NYnHsFyZ0I8LIn7CNmlul77r4aStwB%2BiTO527Ke4ee0bh%2F%2FNserOK9dcvpBzej9VALZyge%2FQyjUSNIJqaBKQIqIMOdDlUfsXn7K1aP1BfaXO0phuAnruCuRmZMbRWxVH%2BOrPXdKMkbkOd5czwipIm%2F%2B66h%2FWapIv4U%2FVKQ4L2OgDOzypKILoRBnHGCx9ip6MoSvyvVetjPNjEhNXWQIi9juh37uTqQ%2BXi403orgB9NXruQHEBNS9lFkk1ROoF%2BBbCGeIV7iuwhdeSF4UwuVZ7wnF4tHd1DQRg6P6KJkvmmkMyi%2BUiGwFmV%2BXyYMIyd8dF%2FAYTFJX%2BNxj7RynT411DW%2B9xY4U6f0bbuyzxsBtg8ThyS3R3u6QMYZrQhahvIUElNavTHMlXgW%2By6bPDtDwcdmMOJvl%2FPR%2Fjv7HkTQb%2FiYVSMXmyfJ1ibo0ZmmXkLwrwS7V92hciySZLKyxZPBM9nU0P%2BOl2mT2%2FFq%2Fa8j3JScm6fAluurh0%2FdKojWyRWI6LOyUbYH4DnXcTtTvoYmiKlVmFZPPucq%2BOc7m6rl5Lw4Qdh%2BdrzkZS%2BbVhiPTY%2FiCt1bvngd8FT5fEDIgsyNsTQKaHlUwz7z9zwY6pgHhfJEdN%2F%2FGu3GA4ON4j%2BNVI142Z2xOHHlLvGOsWOw6UWJpT7aS3G%2B63TYF5kR9wARKkcmeT6K4XkH%2Bc21X1ouOkXxb1MkOCG7%2BOPK8vWpOHyXAcndikFJRjpJuQi6gNBMyUaGZ5G%2FYpRVk0Ab9JSCcU2xnCNNiCTyxpwhyNNKIuWNK3BNaybUhJZJzBNkA%2F9AR1cPc5QZZBQCDqn0b%2FZqS%2BxMQ6Z2q&X-Amz-Signature=f0c5e747e3fc7bdc2796ab036ffe8c37380e04e5364e3e4b482693d1e74cc06e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
