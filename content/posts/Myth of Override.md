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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBPJ3NI2%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T211620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIGELLbhOD5MgsSh%2BKtG3W01O3G4BKtCyjyOB%2BltCFQHxAiBmHBXMHrjwo0w6H57ZQbSh8VCDJAWPpCjNAQrEHZI6%2ByqIBAjm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIye5EyQdUDGman4NKtwDNdNA4ailrSe2z2qw%2BtuZIrnbtEz8dGQDMfNIH12ijHb05w6v%2BQOoQIxaTatj5NmENEW7XGdyWIZ3cMrv3I%2FcmGdeq8ayRLuj3ThPGDrSbkeCzr0nc5USnNhFpjPEILWRvKx0G4hCpqncCM4neOWuxeTdTz%2BD9mNyr2GCPB7jlk1ANiBk9bTSHs1xskAsII7KHRF9KtPvPOx%2BncnvUdBb71Sxe0FHllDUb3BMtPWP6CGaKE5Fe77S5XdDQHRTOj9vkRm0nxHzZ6tIt1jWiMx866X8Qt0mMPWZlItwKOowUZCoJG4MErYy9C7MbDlEHcA5kbJ3Ogt9YQKm24%2FHZOEQswGZQGEAcEqx8tlBdLyJnQUlDNbsN2vKnUQawjdZ9w8ykQWKg6jRtgBr56mls8fRX56J%2BCD6WfsIJoftavDzecowmS8GVxMfu3XsYb2iLOh%2BIpbcpQEU1cpU%2FuexA%2FuW92tUIyeCe5XkThQwXjhuRYxwGfZR9TvBNml8W9j0%2FDqbCZNXGNfhEOufyJcSKql7eHgCqVAzK0fZIbjXt9gC3WoSuYuPiiX6B%2BAnZ22kg0OdCu0mzkMA%2FFt7UrSZpXi9PDCqkJyhKVfJhkNNu%2Bv%2FeQIt7PjGKR3bPXl8tXowmP6V0gY6pgH4RqZbgKjsqfWwkwUmUlByt34Qmvpn6p%2BkI4%2BTCjFXyUHgIff5kfj6EykGosHWBJs%2B0m5s2uZRhmqtGICtLBqAxnKXYvw1QE2E%2B0nX8lwxSdgzPqcI5fSFwGVmcc7g6KM%2BMr%2B4kmzW9HSvPkfGJ5kAoGAvTxMuQwh%2BONk9%2BWvaSgAR76Hw8eKvKxN2flWANb6I%2FXso5Yrtkj%2BsZj05jMvP8XZTQ9wl&X-Amz-Signature=faefda80862a3c3d9a4fe46545ed6944562abcd445e42a3912712fae91266b79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBPJ3NI2%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T211620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIGELLbhOD5MgsSh%2BKtG3W01O3G4BKtCyjyOB%2BltCFQHxAiBmHBXMHrjwo0w6H57ZQbSh8VCDJAWPpCjNAQrEHZI6%2ByqIBAjm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIye5EyQdUDGman4NKtwDNdNA4ailrSe2z2qw%2BtuZIrnbtEz8dGQDMfNIH12ijHb05w6v%2BQOoQIxaTatj5NmENEW7XGdyWIZ3cMrv3I%2FcmGdeq8ayRLuj3ThPGDrSbkeCzr0nc5USnNhFpjPEILWRvKx0G4hCpqncCM4neOWuxeTdTz%2BD9mNyr2GCPB7jlk1ANiBk9bTSHs1xskAsII7KHRF9KtPvPOx%2BncnvUdBb71Sxe0FHllDUb3BMtPWP6CGaKE5Fe77S5XdDQHRTOj9vkRm0nxHzZ6tIt1jWiMx866X8Qt0mMPWZlItwKOowUZCoJG4MErYy9C7MbDlEHcA5kbJ3Ogt9YQKm24%2FHZOEQswGZQGEAcEqx8tlBdLyJnQUlDNbsN2vKnUQawjdZ9w8ykQWKg6jRtgBr56mls8fRX56J%2BCD6WfsIJoftavDzecowmS8GVxMfu3XsYb2iLOh%2BIpbcpQEU1cpU%2FuexA%2FuW92tUIyeCe5XkThQwXjhuRYxwGfZR9TvBNml8W9j0%2FDqbCZNXGNfhEOufyJcSKql7eHgCqVAzK0fZIbjXt9gC3WoSuYuPiiX6B%2BAnZ22kg0OdCu0mzkMA%2FFt7UrSZpXi9PDCqkJyhKVfJhkNNu%2Bv%2FeQIt7PjGKR3bPXl8tXowmP6V0gY6pgH4RqZbgKjsqfWwkwUmUlByt34Qmvpn6p%2BkI4%2BTCjFXyUHgIff5kfj6EykGosHWBJs%2B0m5s2uZRhmqtGICtLBqAxnKXYvw1QE2E%2B0nX8lwxSdgzPqcI5fSFwGVmcc7g6KM%2BMr%2B4kmzW9HSvPkfGJ5kAoGAvTxMuQwh%2BONk9%2BWvaSgAR76Hw8eKvKxN2flWANb6I%2FXso5Yrtkj%2BsZj05jMvP8XZTQ9wl&X-Amz-Signature=33d7e375cf43657152d54d67685c3465f964c7e0c01499d7406da68e1d4678ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
