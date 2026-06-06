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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVSVLHIC%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T205404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAo6MeQuEXCmmLMQ23qf92XK9iQsNJJL8CKj5PdhkqvWAiEAnVGdQDc3DCdNF%2Bm8XG5%2BOO6U4TcEenWRX1njK3GWDNsqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVsxr6ULjRFMjpp2CrcAw0%2FqmGkkIEuLDubpa4%2FsBLpBFhdD26ARzHmCRdCSNpqB2t%2FwTpcaEktwtl%2FyCQKgnZNx37GNQ5F5HWKvnJxwQN6LDOS4lcX3amRF7ArnA7nFhk4RJVDncns9mTyacDumVc5rojHTxSrlQ7o9iN55Gf5Ko1SKeVXkYmrxFuk7%2B0Q8JRbfHujJLlsgee6kYo8ghpFotIZOefqJ5GjnMhwDtgcBpSb49x3KYWmrdpC5t%2Bwp5G4a6gEbtZ3DQ%2FawovPKjkfe%2BcghL%2F5Ki0BkspGC%2Bpz8qYB4c0TApgl7ZHKWJciMnaMdBiRE8%2FHNuBy%2FVR6UxwJrSEvoWsbmPh2W2AMTAdFp%2B1pYp1mDUKK82FrzVrI0LlsAN4HrqJC7OHrLF7ZvCEtyROsjAKFjlMXqVwvwrhRfpHLV1pUKTUxB9Z%2BWX9kNgWO5rnWKMyZuz27zfbYJFuDepKhKg6Jd5VlEyxVNFr13Ra45YgsfmimxxniLQ%2FspRzqjaohTIs0%2Fwsg6QSkzgqRDnwJd611irSF%2FwRjV0oJFuWFywwXfepybg4ObSenDHRPj8PB8nVCgcakWSP3IWBuwvJzV6z219n2%2BL2uih1aGAUDLkGR0s9UR0ltec%2FEQj%2By638LSy6nc%2FOQMMj0kdEGOqUBHJjFD9TNcSwLujtZZueVPI%2BCQwr44hz3boRzGyBjJU3h7MdsJuHqXrt4zS%2FsSQ4Ta%2Fs7RkBavh5PsqGiwUS0pgD2ckPQJWTF5NrwaSaoeKxE21RweGZHyjjDLFiULX3NUp%2Fw0CZorm6pvG%2B9qa6A9q23lc7HzKeqgT%2B9eT4KzABglQ7KQXOTZN00pI%2Bgq7YtwbqQFWL2f8Q3CzZpPjzr62nSkft4&X-Amz-Signature=906c23dd8649fdc9fdb7b966e01d73d56225988793512c4aebf195e903eb3067&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVSVLHIC%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T205404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAo6MeQuEXCmmLMQ23qf92XK9iQsNJJL8CKj5PdhkqvWAiEAnVGdQDc3DCdNF%2Bm8XG5%2BOO6U4TcEenWRX1njK3GWDNsqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVsxr6ULjRFMjpp2CrcAw0%2FqmGkkIEuLDubpa4%2FsBLpBFhdD26ARzHmCRdCSNpqB2t%2FwTpcaEktwtl%2FyCQKgnZNx37GNQ5F5HWKvnJxwQN6LDOS4lcX3amRF7ArnA7nFhk4RJVDncns9mTyacDumVc5rojHTxSrlQ7o9iN55Gf5Ko1SKeVXkYmrxFuk7%2B0Q8JRbfHujJLlsgee6kYo8ghpFotIZOefqJ5GjnMhwDtgcBpSb49x3KYWmrdpC5t%2Bwp5G4a6gEbtZ3DQ%2FawovPKjkfe%2BcghL%2F5Ki0BkspGC%2Bpz8qYB4c0TApgl7ZHKWJciMnaMdBiRE8%2FHNuBy%2FVR6UxwJrSEvoWsbmPh2W2AMTAdFp%2B1pYp1mDUKK82FrzVrI0LlsAN4HrqJC7OHrLF7ZvCEtyROsjAKFjlMXqVwvwrhRfpHLV1pUKTUxB9Z%2BWX9kNgWO5rnWKMyZuz27zfbYJFuDepKhKg6Jd5VlEyxVNFr13Ra45YgsfmimxxniLQ%2FspRzqjaohTIs0%2Fwsg6QSkzgqRDnwJd611irSF%2FwRjV0oJFuWFywwXfepybg4ObSenDHRPj8PB8nVCgcakWSP3IWBuwvJzV6z219n2%2BL2uih1aGAUDLkGR0s9UR0ltec%2FEQj%2By638LSy6nc%2FOQMMj0kdEGOqUBHJjFD9TNcSwLujtZZueVPI%2BCQwr44hz3boRzGyBjJU3h7MdsJuHqXrt4zS%2FsSQ4Ta%2Fs7RkBavh5PsqGiwUS0pgD2ckPQJWTF5NrwaSaoeKxE21RweGZHyjjDLFiULX3NUp%2Fw0CZorm6pvG%2B9qa6A9q23lc7HzKeqgT%2B9eT4KzABglQ7KQXOTZN00pI%2Bgq7YtwbqQFWL2f8Q3CzZpPjzr62nSkft4&X-Amz-Signature=8c52757a3e50fdace37e5c279cd39961dc35e2512d4fb0ceb9cc5b3f3d94f696&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
