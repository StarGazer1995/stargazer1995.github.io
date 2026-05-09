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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WCHLRF6%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T014712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIG6vMUQ0znD1iWHOCyHYcVU1V7tAG%2Fuck%2F41JI13JWFNAiB6S0cbmlrBrPbFkc02IdfaOWEbc4ggFgDJD%2FQBlayhJiqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMg82pfRL5I7EbZeNKtwDgIm3UsUpe85NCqldVTxf5PgEWe5SdwIk0NI0u8waZRCeHU89oFjZWf%2B2lvAK6Anpo2ErolWyrcYQDIbkMBqKhKJvWcizVraU4xHEZ%2FXUJYYHRmbktuGVClQ240Gpd54NTFfHfHtDV5hfJtCs5aEdzjfwHOoy7ssD%2F%2FdhB01IuRp10SxQr7sQLyxjDVgw5F1KtuucoJTHWR%2BnIjVQZC7czJ1N%2FKcCQtutp4u9j9hcMXGJAnFEZi93Abro1LuhoFvuu2UARnirglOt8oQV9F6uDdcufjUy1YpCBM9oA%2BxthodKSeN1OE%2BAn2uecVAJHHrWph%2BzK93yjGmfd3faGYzcrsC44I0cLvkGkylWeyOkIjt7FHenXvJsAnk%2BruaWv%2FIWUSd75RX78gIx7gs%2F1CLr8%2FkxN70DinEAdA%2FEDBHlqAGi5k231HeVjP7P%2FcwCz7abTh7VOiZae%2FqPs9KNRmre5nenvKbodwUf15bhvMXJf10W46GJvKkOIv5FLOk5Um%2BbHOWmyrOHRByNOqe7wAgpSK5Pyecd8KiOZ4p0INQy7QBSclM70KDCeXjcdOInAefSH67o6X6qV9IdrhI6Q2Ruuv%2Bv%2BuxggDyBnJzH3C7SsSKVMXVgATBAoFq2ECUwmY36zwY6pgGHLak3MqO4pAF8nVo7d0qAWe5jWUreAY6J%2B0oXh31%2FMkMSAlsbaa%2BOm1jPsZv9DGoyQPw%2BsV0p9U3tz8ZglFjTGAZJj8sejr8O4a%2BrkzylW7etlT%2FMi%2B2ckh5STsd68d83vC3QFqWY06bqAjV%2FqqC3lBsIrRPQ1sBgavjJA4dnthQwKA7UMfDqp2VMoWob5jNeNhjy5OQRmEXC3mkzEpQUdqhwQwd9&X-Amz-Signature=f2dd7ba6f1453716c9701cf243a5035752a178e599871a3dcca98f04d5706425&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WCHLRF6%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T014712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIG6vMUQ0znD1iWHOCyHYcVU1V7tAG%2Fuck%2F41JI13JWFNAiB6S0cbmlrBrPbFkc02IdfaOWEbc4ggFgDJD%2FQBlayhJiqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMg82pfRL5I7EbZeNKtwDgIm3UsUpe85NCqldVTxf5PgEWe5SdwIk0NI0u8waZRCeHU89oFjZWf%2B2lvAK6Anpo2ErolWyrcYQDIbkMBqKhKJvWcizVraU4xHEZ%2FXUJYYHRmbktuGVClQ240Gpd54NTFfHfHtDV5hfJtCs5aEdzjfwHOoy7ssD%2F%2FdhB01IuRp10SxQr7sQLyxjDVgw5F1KtuucoJTHWR%2BnIjVQZC7czJ1N%2FKcCQtutp4u9j9hcMXGJAnFEZi93Abro1LuhoFvuu2UARnirglOt8oQV9F6uDdcufjUy1YpCBM9oA%2BxthodKSeN1OE%2BAn2uecVAJHHrWph%2BzK93yjGmfd3faGYzcrsC44I0cLvkGkylWeyOkIjt7FHenXvJsAnk%2BruaWv%2FIWUSd75RX78gIx7gs%2F1CLr8%2FkxN70DinEAdA%2FEDBHlqAGi5k231HeVjP7P%2FcwCz7abTh7VOiZae%2FqPs9KNRmre5nenvKbodwUf15bhvMXJf10W46GJvKkOIv5FLOk5Um%2BbHOWmyrOHRByNOqe7wAgpSK5Pyecd8KiOZ4p0INQy7QBSclM70KDCeXjcdOInAefSH67o6X6qV9IdrhI6Q2Ruuv%2Bv%2BuxggDyBnJzH3C7SsSKVMXVgATBAoFq2ECUwmY36zwY6pgGHLak3MqO4pAF8nVo7d0qAWe5jWUreAY6J%2B0oXh31%2FMkMSAlsbaa%2BOm1jPsZv9DGoyQPw%2BsV0p9U3tz8ZglFjTGAZJj8sejr8O4a%2BrkzylW7etlT%2FMi%2B2ckh5STsd68d83vC3QFqWY06bqAjV%2FqqC3lBsIrRPQ1sBgavjJA4dnthQwKA7UMfDqp2VMoWob5jNeNhjy5OQRmEXC3mkzEpQUdqhwQwd9&X-Amz-Signature=e91008d561177c11689439eb1249fcc24cf6fe6cf1cb100f418175ae915dee1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
