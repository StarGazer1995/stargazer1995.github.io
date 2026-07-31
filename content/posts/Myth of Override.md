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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667N5DYA4Z%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T161301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBBPl8xRTK09qQBNnJS7Jxd9fItaUFnLiEf4b3xaWGAXAiEAhwsrMR6GdF%2FqLhtOiTSO3plvIsvhaELlZ4TK8raQ5bcqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfZdrhiXTyCT4DLIircA9HySfzPnX9rKepf6%2BjvcWyCY1rmwmYiIsap804Sppj9XmZzCwx9V2Py%2BPOLOoCqA8TgCpFS7vt5Dkp20rRiUbw%2FTH4v4%2FoPjOrJvoLkVV2bJN64akJbm3aR7PrP8vPxrTvS956qV4%2BJEGfRPxLNXQfW82aWJp709W%2BQcu6neTyrA4rJ7qW%2BFY2CV3kSzqgoBhgQ7WwMhbc%2BziYWmSiOi%2B9Vt%2BHAKka6IJZWA09IjDX6jAbHs8tNa700mQ488PW6yjQrewOBshzg6wCXaAxLKCEO5GFeZJYezzwAF7PJFeCf8X654QP%2BIf1G9cSEk5XeEEzrz5HEZimovGthRFhYD1QMY%2BowaUNqB9gk4lyVfb%2FTp9PiwHC0ioHT7BjEWB2ITPJd%2B0OwdhTWiWISqNHd%2FvAsjJweFb7GoStZCK1oRfZFSiVfg%2B4Q5dPP0LPYUFpCE5LyV%2BtKGgPBGOq0RxS%2Fq3e2V8qkTwDdPzHLeUjWeA1WIB62%2B16B2QpKLzW8AbmUdwvjYydyWtvFN4mRhgQtEkG2MB1pikC3Q2q3hCXshvVpN8GZ9wD11p9QrJtUXiybWi0bWjvzri63ygvMJp6VBGcTtzZCCT8GGcGhPYKTxHOuO6RiSD0vnRZjimnDMKDustMGOqUBrF5imt75ZAuxTDFvunFAPSjNY23c10ToS2OPANivlhuLkDy0a0MToi4rzF7xONuF%2FjG%2BzTZcrJuMISqQZ3cv%2BvkgoriGvHwRIQrLXgvbpM66pis3S%2BvimDFXFGb6bnHkBkH7O71Roe2FJVfNnOaV04Fpqu6rStiUHW87RDV8NgP%2Bwhi6fNu39T2r6AzKjnA2%2FoWs5bW8rPO99xjk6w5w56mkkN6K&X-Amz-Signature=3ee0f18cee640e1c515d12afe52440c157466fdf74102be36f2622619a2c1c50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667N5DYA4Z%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T161301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBBPl8xRTK09qQBNnJS7Jxd9fItaUFnLiEf4b3xaWGAXAiEAhwsrMR6GdF%2FqLhtOiTSO3plvIsvhaELlZ4TK8raQ5bcqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfZdrhiXTyCT4DLIircA9HySfzPnX9rKepf6%2BjvcWyCY1rmwmYiIsap804Sppj9XmZzCwx9V2Py%2BPOLOoCqA8TgCpFS7vt5Dkp20rRiUbw%2FTH4v4%2FoPjOrJvoLkVV2bJN64akJbm3aR7PrP8vPxrTvS956qV4%2BJEGfRPxLNXQfW82aWJp709W%2BQcu6neTyrA4rJ7qW%2BFY2CV3kSzqgoBhgQ7WwMhbc%2BziYWmSiOi%2B9Vt%2BHAKka6IJZWA09IjDX6jAbHs8tNa700mQ488PW6yjQrewOBshzg6wCXaAxLKCEO5GFeZJYezzwAF7PJFeCf8X654QP%2BIf1G9cSEk5XeEEzrz5HEZimovGthRFhYD1QMY%2BowaUNqB9gk4lyVfb%2FTp9PiwHC0ioHT7BjEWB2ITPJd%2B0OwdhTWiWISqNHd%2FvAsjJweFb7GoStZCK1oRfZFSiVfg%2B4Q5dPP0LPYUFpCE5LyV%2BtKGgPBGOq0RxS%2Fq3e2V8qkTwDdPzHLeUjWeA1WIB62%2B16B2QpKLzW8AbmUdwvjYydyWtvFN4mRhgQtEkG2MB1pikC3Q2q3hCXshvVpN8GZ9wD11p9QrJtUXiybWi0bWjvzri63ygvMJp6VBGcTtzZCCT8GGcGhPYKTxHOuO6RiSD0vnRZjimnDMKDustMGOqUBrF5imt75ZAuxTDFvunFAPSjNY23c10ToS2OPANivlhuLkDy0a0MToi4rzF7xONuF%2FjG%2BzTZcrJuMISqQZ3cv%2BvkgoriGvHwRIQrLXgvbpM66pis3S%2BvimDFXFGb6bnHkBkH7O71Roe2FJVfNnOaV04Fpqu6rStiUHW87RDV8NgP%2Bwhi6fNu39T2r6AzKjnA2%2FoWs5bW8rPO99xjk6w5w56mkkN6K&X-Amz-Signature=d0927619b0f95e88cf6b9b431070876192eb38ee1fc6ac0acabe3cc8fabcc036&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
