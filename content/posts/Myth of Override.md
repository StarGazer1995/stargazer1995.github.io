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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMF66FVZ%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T204938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDt7Mgq%2BNwMGlCFlZB4x3fYqFfijQrc4vbTt9Uzaf1fpAiAZCEL1UFaGppjxsxImqqjOxSFqlLW8zhcOjMTda%2BtaYyr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMSBu%2BzLLtT5JABWquKtwDjtEJFfmcBTTr5qqV2GywQUhVqhC2Jp4BuBcRcdxY%2FTxkgjdAXF6aN5%2FXN%2FaG5fj6O9k7G9OeN14VFiE19q6iYlB8m%2FMZOm1A%2BC8TanhQE1508UIlx6lJ0z1%2B%2Fs5lE1FRyuicm4gfMSPrF5i4WSgaACWQ2T%2BAbwqxFvC5OAsHXlstSPgtwnMcY8hDiFe4YJZG9E6ypPwADLMWSBsaFw1sU%2FFuzD2snk5OnNsaHEBC6wNQaokjGxIv56pXRkHpm68%2F19YDlgc3Mnm6wCr1L605Qpl18WEyOSoW7NRwLNcLHdpML7oLTOOg%2BUiMk32HLzRClzbxyRfF1WDN6UN0pETouel9iXotM%2BNf4%2BEATQ6wpEgWbDWAdEZs5KazUqh0MB2nLZEj3eegTBnWC8KFpJChgxoihFGeEdgsSq8qHd9UZnA0eN2LwSUgmqezZEZ7iSzv6F7ubHA%2F%2FabiKZYKAlys20z7LvNu3GwsV%2FMtOG7pfVWrIZouhoW%2FIJd8S%2Fj%2BLFWnETDA5NpZUUo9vehVGmkMsSPrSdF6X8X5nF3Rf6mfeS%2F9sVIs1vXUj7c7PbUJ2KHXPvPXZt9zb7alNqz9NIXucPtCekU7hnwxbOS3kTNcS1fbnPnUOKnsI%2FSsNN0w9%2BGd0AY6pgFabqZqjPi9GW8M08KVPeyCKRqM%2F5F6s9kqMomaNiagT5rQnjBiXsO8%2BYN7LE%2FCpJgKc%2FtnZ9EmtFE%2Fm%2F5%2By24MbxTvG8ypc8YOZJ1QsSAP62M%2FKAg2nWA5z9c%2FD2rVuT0e0yyLOdX7JGznGAKJJXHhYIP1kL6Xn1x9uDw1rJuasnEJVKBoCVlXH2oHCrck5DUrPLfD34DVAGFZY1s4vS9%2ByzWtFwUJ&X-Amz-Signature=861e8e060f2b31fbfb85a53e54ed59d2cfbe31ec631ceffa24e973261ecbf1b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMF66FVZ%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T204938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDt7Mgq%2BNwMGlCFlZB4x3fYqFfijQrc4vbTt9Uzaf1fpAiAZCEL1UFaGppjxsxImqqjOxSFqlLW8zhcOjMTda%2BtaYyr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMSBu%2BzLLtT5JABWquKtwDjtEJFfmcBTTr5qqV2GywQUhVqhC2Jp4BuBcRcdxY%2FTxkgjdAXF6aN5%2FXN%2FaG5fj6O9k7G9OeN14VFiE19q6iYlB8m%2FMZOm1A%2BC8TanhQE1508UIlx6lJ0z1%2B%2Fs5lE1FRyuicm4gfMSPrF5i4WSgaACWQ2T%2BAbwqxFvC5OAsHXlstSPgtwnMcY8hDiFe4YJZG9E6ypPwADLMWSBsaFw1sU%2FFuzD2snk5OnNsaHEBC6wNQaokjGxIv56pXRkHpm68%2F19YDlgc3Mnm6wCr1L605Qpl18WEyOSoW7NRwLNcLHdpML7oLTOOg%2BUiMk32HLzRClzbxyRfF1WDN6UN0pETouel9iXotM%2BNf4%2BEATQ6wpEgWbDWAdEZs5KazUqh0MB2nLZEj3eegTBnWC8KFpJChgxoihFGeEdgsSq8qHd9UZnA0eN2LwSUgmqezZEZ7iSzv6F7ubHA%2F%2FabiKZYKAlys20z7LvNu3GwsV%2FMtOG7pfVWrIZouhoW%2FIJd8S%2Fj%2BLFWnETDA5NpZUUo9vehVGmkMsSPrSdF6X8X5nF3Rf6mfeS%2F9sVIs1vXUj7c7PbUJ2KHXPvPXZt9zb7alNqz9NIXucPtCekU7hnwxbOS3kTNcS1fbnPnUOKnsI%2FSsNN0w9%2BGd0AY6pgFabqZqjPi9GW8M08KVPeyCKRqM%2F5F6s9kqMomaNiagT5rQnjBiXsO8%2BYN7LE%2FCpJgKc%2FtnZ9EmtFE%2Fm%2F5%2By24MbxTvG8ypc8YOZJ1QsSAP62M%2FKAg2nWA5z9c%2FD2rVuT0e0yyLOdX7JGznGAKJJXHhYIP1kL6Xn1x9uDw1rJuasnEJVKBoCVlXH2oHCrck5DUrPLfD34DVAGFZY1s4vS9%2ByzWtFwUJ&X-Amz-Signature=3431d9ce363b9b139fa2094cc5873b538f2327203570a95483da16a9214e95d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
