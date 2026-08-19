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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMYWHLGA%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T122025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIESporejxsGYV2OoLMVUAIC%2Bohs79AFTsb9N2oihuz0sAiEA%2B%2BnEw%2BvMyg00aEOj6MfPDA9sjvHvdWIo5mmjYcDylF0q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDNXRRH3y4wz0lGLanSrcA2T6FaVJxuKs1ODLNDG844TjZQFaibM%2Bpu2sZidCZB4oohlXEJJCG%2B7aVpkgc4mUne6tJv59YwR1F9U0tcqAh3oJwMAOzSwWwSunH7FQH%2B8FsIcEUfZxton4ZA%2FLmx0wuRfXxy4xON38kWGM8ji9zNl2OdXgpk%2F2OG2oqS5cNG12s55PN96Ki0nhcIVyKn4L9KssPC9cv%2BBaqZNC0B989eBouz5zyt5aXRWMVmeZwzMXhmeh9V1QOXxaDvk5nk1emHBWONe1xn8zYX1HB77G9zWhfRLLmFVAwygKbKcLoCj67SE%2BPoM6JAxjN%2Fc7KDZzVAQ4M5%2FPWTEUzMfLKkxojTscdVC4Ae4xmcdG%2FszwqEK%2F7SxZxooqH5OrFPFW7gSgR982KJhLXhVdQLy2l6SAZGNd70o%2FX2N6Pnsw7BT3MeA3wH0ir%2B3%2BkzgkIJnpKn56K%2BtlI9y%2Fj4sL44ZEzYNVSg1jjAd98jTmLOfv6ke4jmbPutK925Bl6EfZ9qjO06THE4F47amhSeu5l%2FmigPcMnjYQCWY2NTq3xq9MpRyCBuK2KOnnGFIL4mOdR4MJ7glg4js4Uy7lcdKeYjECewtkD71ihfwBzq0kJgOIu4nKoZN7in4ygR65%2BJ90vgRgMJGdltQGOqUBx7p2T7esKMeBQg%2F%2FEBut97gJq%2BmTiQ%2F2brvZnycDffMquBKJOIowELiPsNoVZ%2BaCuSSGO88JOY7bMZ4cyW97eFkv8WPHbvNwHbbp%2FxcAmuqwTY8pt2HZM2XkBBOnA4Cr%2BFgUNCCa4Rcq64RD%2FvXDE4Z6JGLBh4skrYoNCsATf8qxNlsbiLQBYxgOP93vymfzWjLsYkNvrWS61ORYJj%2BGsQZojxgy&X-Amz-Signature=305afa6dc5c476f2f9e099bad4a4a7eef9254a3ce66b1d76ae4303e208e7f887&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMYWHLGA%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T122025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIESporejxsGYV2OoLMVUAIC%2Bohs79AFTsb9N2oihuz0sAiEA%2B%2BnEw%2BvMyg00aEOj6MfPDA9sjvHvdWIo5mmjYcDylF0q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDNXRRH3y4wz0lGLanSrcA2T6FaVJxuKs1ODLNDG844TjZQFaibM%2Bpu2sZidCZB4oohlXEJJCG%2B7aVpkgc4mUne6tJv59YwR1F9U0tcqAh3oJwMAOzSwWwSunH7FQH%2B8FsIcEUfZxton4ZA%2FLmx0wuRfXxy4xON38kWGM8ji9zNl2OdXgpk%2F2OG2oqS5cNG12s55PN96Ki0nhcIVyKn4L9KssPC9cv%2BBaqZNC0B989eBouz5zyt5aXRWMVmeZwzMXhmeh9V1QOXxaDvk5nk1emHBWONe1xn8zYX1HB77G9zWhfRLLmFVAwygKbKcLoCj67SE%2BPoM6JAxjN%2Fc7KDZzVAQ4M5%2FPWTEUzMfLKkxojTscdVC4Ae4xmcdG%2FszwqEK%2F7SxZxooqH5OrFPFW7gSgR982KJhLXhVdQLy2l6SAZGNd70o%2FX2N6Pnsw7BT3MeA3wH0ir%2B3%2BkzgkIJnpKn56K%2BtlI9y%2Fj4sL44ZEzYNVSg1jjAd98jTmLOfv6ke4jmbPutK925Bl6EfZ9qjO06THE4F47amhSeu5l%2FmigPcMnjYQCWY2NTq3xq9MpRyCBuK2KOnnGFIL4mOdR4MJ7glg4js4Uy7lcdKeYjECewtkD71ihfwBzq0kJgOIu4nKoZN7in4ygR65%2BJ90vgRgMJGdltQGOqUBx7p2T7esKMeBQg%2F%2FEBut97gJq%2BmTiQ%2F2brvZnycDffMquBKJOIowELiPsNoVZ%2BaCuSSGO88JOY7bMZ4cyW97eFkv8WPHbvNwHbbp%2FxcAmuqwTY8pt2HZM2XkBBOnA4Cr%2BFgUNCCa4Rcq64RD%2FvXDE4Z6JGLBh4skrYoNCsATf8qxNlsbiLQBYxgOP93vymfzWjLsYkNvrWS61ORYJj%2BGsQZojxgy&X-Amz-Signature=def64d4733b097aab91c34766a1758411199856ddb32333a31b2372544023afb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
