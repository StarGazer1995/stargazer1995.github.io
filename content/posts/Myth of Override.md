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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6WLKUYZ%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T091016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIHk6me338qsjwA9vTz9ABNGMQ37YsVWH9HQxtn2mP4QIAiEApj%2Fs7ZCURwTwzJbbiNUwop0kkjI4kG973VfciKaQHGIq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDED%2BejmWXBF%2FfBe5%2FyrcAxzm0I2jDrNHZmXvD%2BgS%2FQHm91kIeD4%2B5f1%2FeqcJOUOaaHlRbPKdJXBf1P0RJj9DCCnIlI6lRJ0SjXdWAW%2FRH6e9czzZFFl0MVYJ%2Fr6oTT0UZWyH%2FYEOygN%2BpNVq8F2F%2Fqp35JhAQNTpJCIux%2FxMyZ7o3iwaTDd5UoFgixFctS205tpjLK1m6Uz71wesD2uPgvCn4GeDjJEgdVkUxoBvnCAFlehbpLUIBxywYLOAlX1CtHlrflUQ1Ls2RDuY%2BHea1gQh973lxtoGaG5XHPh395CCQdA5Ai7WGD5HQVJ48AEL6AxfnOY4a4hNatzDidfTKDU%2Bm%2Fm6nKRKOusAxc7Lg%2Fxy%2BhzOLk6ZuGBFqJPctZECAdhubLVc%2BGDbl6I5%2FAJ3T4LBsovIZ9pHPZp7%2FwmcYtzzvmAHPmffTMkp%2B9fKuItwIfYi1ORdnCEKJfw96qizGQQot8CbpgrKnuqc4d8hVPCxbZPu2NX08xcVA9by%2BXla5dEG2E1s%2FpImrTqSSvhB13Gv2o6oVywZG24waczip%2Bb72cakdu1eLUiCLtAY1vB2dtQhfBowG%2BX6lo12euPvNgb8nsKD70jOGnUAwZhAUzeATB3fkQ8nkU8sHJS1GpsXYZxeXX9Pdimu%2FVxkMLLG9NAGOqUB8qU21awPODv8Bh8X7eyMWGsHZOBdrVec6BPNFtFitC3N010tFbLC%2FZPpKDDEnm2dX94XNPcv%2BAUKFcVs%2BfKrbmba8SuLY5OEAO5uc9f4WhsyGEKhM2afssHpWK%2B1eb%2B%2FksOf5xBLW2UtQWoUVamI2B6JHAVIfRBRcmHTynD1kEmzkNzvFn76i%2BWxBiUoMZExNlYWRaLdD6I2FZQXIMHzUGjjl6ZH&X-Amz-Signature=d93302ec37b0f0b578d675b1eeaf7c5f6fadb80aeb5b9be8db777f7d8187f24a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6WLKUYZ%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T091016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIHk6me338qsjwA9vTz9ABNGMQ37YsVWH9HQxtn2mP4QIAiEApj%2Fs7ZCURwTwzJbbiNUwop0kkjI4kG973VfciKaQHGIq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDED%2BejmWXBF%2FfBe5%2FyrcAxzm0I2jDrNHZmXvD%2BgS%2FQHm91kIeD4%2B5f1%2FeqcJOUOaaHlRbPKdJXBf1P0RJj9DCCnIlI6lRJ0SjXdWAW%2FRH6e9czzZFFl0MVYJ%2Fr6oTT0UZWyH%2FYEOygN%2BpNVq8F2F%2Fqp35JhAQNTpJCIux%2FxMyZ7o3iwaTDd5UoFgixFctS205tpjLK1m6Uz71wesD2uPgvCn4GeDjJEgdVkUxoBvnCAFlehbpLUIBxywYLOAlX1CtHlrflUQ1Ls2RDuY%2BHea1gQh973lxtoGaG5XHPh395CCQdA5Ai7WGD5HQVJ48AEL6AxfnOY4a4hNatzDidfTKDU%2Bm%2Fm6nKRKOusAxc7Lg%2Fxy%2BhzOLk6ZuGBFqJPctZECAdhubLVc%2BGDbl6I5%2FAJ3T4LBsovIZ9pHPZp7%2FwmcYtzzvmAHPmffTMkp%2B9fKuItwIfYi1ORdnCEKJfw96qizGQQot8CbpgrKnuqc4d8hVPCxbZPu2NX08xcVA9by%2BXla5dEG2E1s%2FpImrTqSSvhB13Gv2o6oVywZG24waczip%2Bb72cakdu1eLUiCLtAY1vB2dtQhfBowG%2BX6lo12euPvNgb8nsKD70jOGnUAwZhAUzeATB3fkQ8nkU8sHJS1GpsXYZxeXX9Pdimu%2FVxkMLLG9NAGOqUB8qU21awPODv8Bh8X7eyMWGsHZOBdrVec6BPNFtFitC3N010tFbLC%2FZPpKDDEnm2dX94XNPcv%2BAUKFcVs%2BfKrbmba8SuLY5OEAO5uc9f4WhsyGEKhM2afssHpWK%2B1eb%2B%2FksOf5xBLW2UtQWoUVamI2B6JHAVIfRBRcmHTynD1kEmzkNzvFn76i%2BWxBiUoMZExNlYWRaLdD6I2FZQXIMHzUGjjl6ZH&X-Amz-Signature=665eb587021ebb44ecd014fa5cc50350289bd433320edaa79f224e1162e9cfa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
