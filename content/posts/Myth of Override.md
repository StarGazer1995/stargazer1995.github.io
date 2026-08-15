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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O3UKMQC%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T201016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIDrNOVqgWWgf4ZfT0DZuQd%2F6%2FBw8%2B6kyVjbPZTL33yZlAiEAtcA3L3xkZx3uQNtMpa7W3UnBw78qw0GtgMFJb%2B%2FhZ7Qq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFitibKFqHAWbmxdzyrcA2MG6I8DYf14iEM7KWyukxvESRC72HPViyzJYTGPqg2aoxFOyk1E0QB7GQxPnO7X5eO6lbPgqiHgp8nIkH%2BQ2ZVF4g3DP9%2FiMgBnLIS7E1v%2FMb9bNnU0%2F%2FVlyg818H7QyV9RLYAN0cM8da6Qb5EQt7JHxjnuNtXIzcSJgSTb8u90NkKCdhrN49j5GQMo8Ip%2BGkR7bDgv15UK0LtfzAyaazmAv7oIavmr%2FPKiYMcSXBoth6d%2Fr5HZ1RlbZ%2BZ4H%2FgExIQNI9poxtuHlqeJ2bzpYTlEEXL6WmKGfRrq1RMz9YQfwVuVJAiDJuqRuQkS1wNC6rs%2BP%2BHRwy82kvtedZT8puvSZPpxJn7PBwBEpDSWGpx6CMX3CHyVkgOC58Z7KqZQ2KZyRg2fPkSWHsiJwvPnxD%2FmvAyhxupwi91T022ktZv40uLPsRsyf9FX%2BLXs1Yn6CbofrYA3m%2BtCF%2FYkbo8y8RgFbRP13VGDI8qbUZOQZ0BbIyTBGAO29Qdg8ZIoXWwbyMtqTgL1VRSw4uj6gcTLzk2BFMpWq%2F1P1XFApMVsMSTPx5tvkEQqu3TfhZYWTfAsTiZerOS6QzSMCd28B4aYUtkOC%2FjD2d1y7cYW9izOvbDAtsgYex6N6%2Bh%2FVJL2MNL4gtQGOqUBY9jPSnQrVSFXd954V737yQk9kY9%2FIF3e%2FNa%2FD9hW0DxaOhxGwrAUM8K3eTbZ%2FAX9hr9l8%2FidxyrvnSMD4EmP1jWGoZxXJ8ohcHWmWY3kKPPgWO3V1nQFSQqg8m5j7GQ8IMWAeOSG5xNDtXtirt2GO1QhZI5pk63zeF%2FQ0aQSpPdeqlOoF6iZag9veel1tKjEnAPPkUNuG4dy272FYxGJoCGR%2Bl%2BB&X-Amz-Signature=217a415e1c64b4921bd22084ac7dbfc77361012e1eb622115f8cbf0dda4fabd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O3UKMQC%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T201016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIDrNOVqgWWgf4ZfT0DZuQd%2F6%2FBw8%2B6kyVjbPZTL33yZlAiEAtcA3L3xkZx3uQNtMpa7W3UnBw78qw0GtgMFJb%2B%2FhZ7Qq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFitibKFqHAWbmxdzyrcA2MG6I8DYf14iEM7KWyukxvESRC72HPViyzJYTGPqg2aoxFOyk1E0QB7GQxPnO7X5eO6lbPgqiHgp8nIkH%2BQ2ZVF4g3DP9%2FiMgBnLIS7E1v%2FMb9bNnU0%2F%2FVlyg818H7QyV9RLYAN0cM8da6Qb5EQt7JHxjnuNtXIzcSJgSTb8u90NkKCdhrN49j5GQMo8Ip%2BGkR7bDgv15UK0LtfzAyaazmAv7oIavmr%2FPKiYMcSXBoth6d%2Fr5HZ1RlbZ%2BZ4H%2FgExIQNI9poxtuHlqeJ2bzpYTlEEXL6WmKGfRrq1RMz9YQfwVuVJAiDJuqRuQkS1wNC6rs%2BP%2BHRwy82kvtedZT8puvSZPpxJn7PBwBEpDSWGpx6CMX3CHyVkgOC58Z7KqZQ2KZyRg2fPkSWHsiJwvPnxD%2FmvAyhxupwi91T022ktZv40uLPsRsyf9FX%2BLXs1Yn6CbofrYA3m%2BtCF%2FYkbo8y8RgFbRP13VGDI8qbUZOQZ0BbIyTBGAO29Qdg8ZIoXWwbyMtqTgL1VRSw4uj6gcTLzk2BFMpWq%2F1P1XFApMVsMSTPx5tvkEQqu3TfhZYWTfAsTiZerOS6QzSMCd28B4aYUtkOC%2FjD2d1y7cYW9izOvbDAtsgYex6N6%2Bh%2FVJL2MNL4gtQGOqUBY9jPSnQrVSFXd954V737yQk9kY9%2FIF3e%2FNa%2FD9hW0DxaOhxGwrAUM8K3eTbZ%2FAX9hr9l8%2FidxyrvnSMD4EmP1jWGoZxXJ8ohcHWmWY3kKPPgWO3V1nQFSQqg8m5j7GQ8IMWAeOSG5xNDtXtirt2GO1QhZI5pk63zeF%2FQ0aQSpPdeqlOoF6iZag9veel1tKjEnAPPkUNuG4dy272FYxGJoCGR%2Bl%2BB&X-Amz-Signature=baf5b2f6d43df39c33615493aae199475143bf18953f70c46a51539392bc97ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
