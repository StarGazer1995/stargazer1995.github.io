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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UFAM75M%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T144925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDgq%2FcWjL8fEU4TkKMG2b%2FHhbwb%2BCM20wjSmTYaDb9fsAiEAzP4IUNy%2FXH%2FiP%2FVrlAUKRswukdy8FN2%2BzSOYI3R81xMqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIeaCamjno7gwpthqCrcAw52a4FzPfzlGjIAKSps0l0Gc0u2vLnbzeig5IHwkMDoVgVd4G%2F9WvyqYLFScBqD8vYJFI9ciF6KJBjdHNW412zlxiQoWyDibk9rLhJnBHjdOm2V93YQDeAB3z1RDHdlvBg13onuyjqo%2FyIAjaljSkWgofCZMFkjAm7Us2sqAuyxjc%2Fx4Iw2vmNAS7NAqxxgw9w4y%2FkUas2guN1nlcWA7Ony0US4i2qxmnFw7RaADHcT5EWLW9Zmkgg7%2FADWBZlv8IBcr15b4vdKMxaxhb6MCfqtCa%2BazOX4gR7Hlo5rm48nfROPaYC5bszE%2FQFUZmojKMsid3c4zei9F8wh8cRefbvj4xl9NetDjO50fEtp5QVDcBlVpl7%2F9Lwx6dCkH5I3NprTDIm4FW6WTjdYKI6D8FWgi3o9%2BqUMpK2G88bPS6YPpdSPLTDf4VGdBsCohRnwsOUHY4XtHFxnkROaVVo4R4QV6wned1bHHmMrZkXi8DTTNSJe8iFearmi9tTADS%2Ba6xcwz0PhZO2ey1C%2BZeBGH5FYt5EFTgi4QUVEW%2BLK5V%2BBmG0Au4QeZRdWd8QqcDM3g0JuJEDz1x42c5eCqsNL4QGH9%2B82%2FUPXwNZPWhTPva1N7SRI%2BVNQDGX7YYLUMPPO7NMGOqUB1orPySfrY7dr2hfQmvmSA3XwGl%2Fr14t5Qw62JrFrdMv8mV7Wx6BAf2VRVzwD2Nyw9IebS0DkhhDYVZ26tkvDW3Wbu2KKb0%2F9RudugK3pl5gLFiHjHHrKWOv%2FhSAtKHBDaOWb7iZK8OLNgwhCh%2FKGXAZONdRMKwxcVr8TrlEPIJ8%2FCRizHZsJJhxxOb1onlIACq8FDLCDtHixPUM058cU%2BuUvabKV&X-Amz-Signature=a5ab201c3a0591b3521a00f6f0965a4f1753888f6a634798cead18501b10da72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UFAM75M%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T144925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDgq%2FcWjL8fEU4TkKMG2b%2FHhbwb%2BCM20wjSmTYaDb9fsAiEAzP4IUNy%2FXH%2FiP%2FVrlAUKRswukdy8FN2%2BzSOYI3R81xMqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIeaCamjno7gwpthqCrcAw52a4FzPfzlGjIAKSps0l0Gc0u2vLnbzeig5IHwkMDoVgVd4G%2F9WvyqYLFScBqD8vYJFI9ciF6KJBjdHNW412zlxiQoWyDibk9rLhJnBHjdOm2V93YQDeAB3z1RDHdlvBg13onuyjqo%2FyIAjaljSkWgofCZMFkjAm7Us2sqAuyxjc%2Fx4Iw2vmNAS7NAqxxgw9w4y%2FkUas2guN1nlcWA7Ony0US4i2qxmnFw7RaADHcT5EWLW9Zmkgg7%2FADWBZlv8IBcr15b4vdKMxaxhb6MCfqtCa%2BazOX4gR7Hlo5rm48nfROPaYC5bszE%2FQFUZmojKMsid3c4zei9F8wh8cRefbvj4xl9NetDjO50fEtp5QVDcBlVpl7%2F9Lwx6dCkH5I3NprTDIm4FW6WTjdYKI6D8FWgi3o9%2BqUMpK2G88bPS6YPpdSPLTDf4VGdBsCohRnwsOUHY4XtHFxnkROaVVo4R4QV6wned1bHHmMrZkXi8DTTNSJe8iFearmi9tTADS%2Ba6xcwz0PhZO2ey1C%2BZeBGH5FYt5EFTgi4QUVEW%2BLK5V%2BBmG0Au4QeZRdWd8QqcDM3g0JuJEDz1x42c5eCqsNL4QGH9%2B82%2FUPXwNZPWhTPva1N7SRI%2BVNQDGX7YYLUMPPO7NMGOqUB1orPySfrY7dr2hfQmvmSA3XwGl%2Fr14t5Qw62JrFrdMv8mV7Wx6BAf2VRVzwD2Nyw9IebS0DkhhDYVZ26tkvDW3Wbu2KKb0%2F9RudugK3pl5gLFiHjHHrKWOv%2FhSAtKHBDaOWb7iZK8OLNgwhCh%2FKGXAZONdRMKwxcVr8TrlEPIJ8%2FCRizHZsJJhxxOb1onlIACq8FDLCDtHixPUM058cU%2BuUvabKV&X-Amz-Signature=5e8a637bf0a99012409e198f5d49a0f25fbe7d4b0644a0577fe3e31d94ccb703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
