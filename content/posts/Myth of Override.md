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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YG7KJAB%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T020030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICLAsfkf7Mmi9DM136mBtYWZkyop2mbzbXEScie0WiusAiAa%2FRVlSY%2BlRlTLT4Yh7yBtD4Q6nliAqbaUTtq%2BV9c5Tyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMWLES1m54maZm%2BQnaKtwDcs5i0ZjudUKjW%2BV%2BMkPIDz2m3%2B%2BimIyeiegS23ZEC1%2B1Y5%2FschZ%2F0sSUudJSCk0wW6nf90n6MjUfV2pZvf3bOFZT5nhAe3XfO2Ue5PbNKVrUEjTZlmYSQPpS%2BulCSqJepNs1AAIACt5NRnBvNgMIcyvPYZOqqyCSqncCkoq8%2F4hx0Fi9axk0nXGp49eqdwpuAVr1huCqltSeweA%2FoT4fRb769XoQT%2FWl%2Bhnm9WtlhtAqgPyfuUF3bGUrbQAk%2BGkIR5%2BKZlxCy1oDtqVVpEybvaaZBwzfWd%2BQClCPZ3V65MYNxzhOO6kC82jrLlhlXYS7xv%2BflkPZV3zquBnNB63WHxH2v9xq035uSwjbpOVWTjHoyWdyZakMPsS9mDzurHPmuq9VgYxS2A%2BY%2B%2BkAQY5MS%2FOcTvXq5ACYFr3zUDmpucRFhpb4SjREUDapvSnl7GHPPR0Eh9w9V%2Bda%2FVNsAw6rYKuk0shtpUnXMQDuZAhsVSBTDK0ybIv9LrUwhxp3OysFbw%2BVz70aLTARCJ8nNJqL%2BX%2BKx5N1SwhQXS4x4sRNls9wFr4hy%2FPo98UUHe22hI6cpgVOGTXKznDrO3T6FRawrfTblt%2B%2FHlEE9VW4OPtxVPDXHMlmkXiJkUwLkOMw36jJ0AY6pgFdhEtlRlTVlwzSPbPHUritQGxSjCy7at7QOqTLw1Y740qeWMfa9PfPXany64vYW4lZOo%2F%2FuzbtPhJlUw0T8w2x3qTaLJx8%2FrenzQTBlqzgrE2lASS4pfmnDGA0ayBzFVwvgi%2FLon7ag451UO0YdQOO95LqLriFFTGEiZxNcizCCbcNWXbrg7Aj9VLNt0UXlYZYBu6lkmy6rPnJh75IMJ7utpZwXRhg&X-Amz-Signature=3f9c6a1de28e5f2dadf3e445d0d232180dd77bd86e729b8127a7965da656ce34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YG7KJAB%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T020030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICLAsfkf7Mmi9DM136mBtYWZkyop2mbzbXEScie0WiusAiAa%2FRVlSY%2BlRlTLT4Yh7yBtD4Q6nliAqbaUTtq%2BV9c5Tyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMWLES1m54maZm%2BQnaKtwDcs5i0ZjudUKjW%2BV%2BMkPIDz2m3%2B%2BimIyeiegS23ZEC1%2B1Y5%2FschZ%2F0sSUudJSCk0wW6nf90n6MjUfV2pZvf3bOFZT5nhAe3XfO2Ue5PbNKVrUEjTZlmYSQPpS%2BulCSqJepNs1AAIACt5NRnBvNgMIcyvPYZOqqyCSqncCkoq8%2F4hx0Fi9axk0nXGp49eqdwpuAVr1huCqltSeweA%2FoT4fRb769XoQT%2FWl%2Bhnm9WtlhtAqgPyfuUF3bGUrbQAk%2BGkIR5%2BKZlxCy1oDtqVVpEybvaaZBwzfWd%2BQClCPZ3V65MYNxzhOO6kC82jrLlhlXYS7xv%2BflkPZV3zquBnNB63WHxH2v9xq035uSwjbpOVWTjHoyWdyZakMPsS9mDzurHPmuq9VgYxS2A%2BY%2B%2BkAQY5MS%2FOcTvXq5ACYFr3zUDmpucRFhpb4SjREUDapvSnl7GHPPR0Eh9w9V%2Bda%2FVNsAw6rYKuk0shtpUnXMQDuZAhsVSBTDK0ybIv9LrUwhxp3OysFbw%2BVz70aLTARCJ8nNJqL%2BX%2BKx5N1SwhQXS4x4sRNls9wFr4hy%2FPo98UUHe22hI6cpgVOGTXKznDrO3T6FRawrfTblt%2B%2FHlEE9VW4OPtxVPDXHMlmkXiJkUwLkOMw36jJ0AY6pgFdhEtlRlTVlwzSPbPHUritQGxSjCy7at7QOqTLw1Y740qeWMfa9PfPXany64vYW4lZOo%2F%2FuzbtPhJlUw0T8w2x3qTaLJx8%2FrenzQTBlqzgrE2lASS4pfmnDGA0ayBzFVwvgi%2FLon7ag451UO0YdQOO95LqLriFFTGEiZxNcizCCbcNWXbrg7Aj9VLNt0UXlYZYBu6lkmy6rPnJh75IMJ7utpZwXRhg&X-Amz-Signature=a57216623ffd650cdd9e83702b7068857637bdacfced66c48d1832dc1329a568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
