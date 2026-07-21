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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REA6CFXN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T114157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9PIyrF8tVzTIDraXy3Am973%2FEjd98uAbiiiba6MjhVQIgJkYZxEsMUaa%2FDrWPhWpoHDsiegIU6Xc6a%2By0ll%2FdHtQqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf5LXgw2Y043pfUaCrcAyLddlOb8h0%2BbKti4Sb1DyvYI0nhb4Wwx25jNGYrmuXQk6L3X0QSwIO9K10G%2Fjd06FnWtL7pn7mMJOp%2FVCR9eUmSpXnCfBH%2BOGQ%2FED6IS0OJJzeXAqAFhfuEA7mdhX2a0xjJRqRZJNjPj5lDqNqcvcRrxgLDr6Uj13P6E0qfWgz1YtiZdhjVe5JAHhVFnNIJqM2fGG1wTNefzbHvUOKm8NGDiv9sBSaJm%2FNMwzQWOxQaqlQs8woNK6Qh1p%2BHrbv0cb%2FhvjxoudQkx3GoWEoqaHH04uXL1Sfa%2FGztk%2FfdNpkieCmIVhHIkr7tfkb5tch2FpB1O03CAPQ1trncjmW6glekwEOzamizPJch%2BTl7Ov9z1RSH60haj3qi%2BQCoE9zOw2N%2FvRHONPs5pFjii1ruUZ0EqmnUVxlXurPq2C589iVjzV91KwP0ItGL%2Bp1MY36b8vxV0c1gouxv1vmpP98bfDAlqKRRTQGwJVDDOwvIzZIhAJt0wd%2B5ti3JdwAPb0Xu8hoZEV3l55iO53VXIXOGPovNhsI0ATPCE0DLDamoRX2JKx%2BLWSX1RleNqH%2FJwOPgWTJt%2BlpDeFQRsEkYCnbVIZrfOIPy0CDYEOvk0sZFgeQAQ5DflQ7EVwj6AGOQMK%2BO%2FdIGOqUBUAoBlV7BhPJZXMI9IsaPrKZk4Wmu%2FxC4m4696%2BgZTQzaa%2BRazk%2FKevERui%2F6AiKACo1tAftP%2Barm%2FTQ0KdaFV7oNQ46KoZRKhEep5o8IBvYYERCbwYwEpZsmVnsi%2BMeRy09yZon4yw69cUFwB5qfSt5orxJfcQsBp3djqFQ4axtkltsC%2F7ntc7kCu03AZdq1qQ0mbWyEBWjZShSXzkkdimrPbujY&X-Amz-Signature=dacce99181a10b54fc94cab8f02bfa93b29cd8a0be932281c9f5802d2fea8ec4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REA6CFXN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T114157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9PIyrF8tVzTIDraXy3Am973%2FEjd98uAbiiiba6MjhVQIgJkYZxEsMUaa%2FDrWPhWpoHDsiegIU6Xc6a%2By0ll%2FdHtQqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNf5LXgw2Y043pfUaCrcAyLddlOb8h0%2BbKti4Sb1DyvYI0nhb4Wwx25jNGYrmuXQk6L3X0QSwIO9K10G%2Fjd06FnWtL7pn7mMJOp%2FVCR9eUmSpXnCfBH%2BOGQ%2FED6IS0OJJzeXAqAFhfuEA7mdhX2a0xjJRqRZJNjPj5lDqNqcvcRrxgLDr6Uj13P6E0qfWgz1YtiZdhjVe5JAHhVFnNIJqM2fGG1wTNefzbHvUOKm8NGDiv9sBSaJm%2FNMwzQWOxQaqlQs8woNK6Qh1p%2BHrbv0cb%2FhvjxoudQkx3GoWEoqaHH04uXL1Sfa%2FGztk%2FfdNpkieCmIVhHIkr7tfkb5tch2FpB1O03CAPQ1trncjmW6glekwEOzamizPJch%2BTl7Ov9z1RSH60haj3qi%2BQCoE9zOw2N%2FvRHONPs5pFjii1ruUZ0EqmnUVxlXurPq2C589iVjzV91KwP0ItGL%2Bp1MY36b8vxV0c1gouxv1vmpP98bfDAlqKRRTQGwJVDDOwvIzZIhAJt0wd%2B5ti3JdwAPb0Xu8hoZEV3l55iO53VXIXOGPovNhsI0ATPCE0DLDamoRX2JKx%2BLWSX1RleNqH%2FJwOPgWTJt%2BlpDeFQRsEkYCnbVIZrfOIPy0CDYEOvk0sZFgeQAQ5DflQ7EVwj6AGOQMK%2BO%2FdIGOqUBUAoBlV7BhPJZXMI9IsaPrKZk4Wmu%2FxC4m4696%2BgZTQzaa%2BRazk%2FKevERui%2F6AiKACo1tAftP%2Barm%2FTQ0KdaFV7oNQ46KoZRKhEep5o8IBvYYERCbwYwEpZsmVnsi%2BMeRy09yZon4yw69cUFwB5qfSt5orxJfcQsBp3djqFQ4axtkltsC%2F7ntc7kCu03AZdq1qQ0mbWyEBWjZShSXzkkdimrPbujY&X-Amz-Signature=7c9816e4d1e2548d246abe147498e6c31cb6c1ed9f92ace1b0f3cbba0a032043&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
