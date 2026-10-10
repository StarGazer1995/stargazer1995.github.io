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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CXDCYAR%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T230304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCztvV2gbMoPkTg0jD2wOVnxwwGezFUHUFVwvdjcxrF8gIhAK41DiO3mTXIe8tt%2B0E3L6JzuZTyfp0ugtOkZOEfUlOvKv8DCF4QABoMNjM3NDIzMTgzODA1IgwmiDfDUHuwqFFkiCEq3ANlllVNYbPxQTL0JyUwPjeA4PgbwflPbq%2BCtRO%2Fkl%2BBJZtm22cEchgduJPWs%2FtgwsyoTvACxCVbeE45dJ0QoeKvy5Z60Ep2cjKpxq1kX88ky6q%2BFIA7quslMutqsoPeT2XdyeSnjQzdW76r4e8u0YHopYE0%2BuLxOtTqht%2Fd4RR7d4wKatPgSrxwmlaBGdYGUZqeQhLrFfQvGZrtzQsGBxRaVCqC5d98IwJQt3cY1mBOKGOKcGTLgu8WDcO48w5Y7lMM540tfGUFv3OnWKI79uNjy8XC3guMdkS4c3zwy90g7Nz5GRxmrgCa7MZwh0Hrl4CkS3Pa%2B5TMK6JxhY70EfVCjtPuMBB7EP9XzDS%2ByW5yAIh3pTfVkrQOetuaM0VSK9MtyH8t8SXBHLzfx%2B628oMLdJm9%2FmpA18IHuhrZFMhApZdrDb%2BF6ZzREC3Nmf%2FJMbrlJ1yubpfeM5JH7WrzyAW97B1x4%2BaEnC421MAgRKhhDM4l1B%2Frv5%2F6vbfuGL5XNC7Nrz%2FhR5etAXmMm2o87FMwmuWNiGVTO6cfdsv2juL6ciZV%2FWM6u73l4dIPaADD2KOLgNejF1I5HipM3E%2BXQBPU5w9UM10AI0etr5gEkEpEYZD9kahzAj9ygX4pRjCC26rWBjqkAbY3YlIb68%2Fn9jDJFan9S3rpJ5otcCjrdCwhDwOgEixVK3k7DTniZNou6fmsHOWR00L9O6GthczHAckpwCjf9BL%2BXY%2FG%2BtpJe2kMS6f1RCAQw%2FwLi%2FkbpdAMAJCphuQIsW%2Fw90PDcAbgdXAl9eDkZ08L5HfizR57aADxFQyZM9uhMW4E%2FNMQ3t%2B5r8%2B70QxKnmJzo06H3BX71XNY1dquml3kaG42&X-Amz-Signature=8140922f0b6dc270e79e1900752b1e5074d13e1cd56b8b02f55db0b6045475d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CXDCYAR%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T230304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCztvV2gbMoPkTg0jD2wOVnxwwGezFUHUFVwvdjcxrF8gIhAK41DiO3mTXIe8tt%2B0E3L6JzuZTyfp0ugtOkZOEfUlOvKv8DCF4QABoMNjM3NDIzMTgzODA1IgwmiDfDUHuwqFFkiCEq3ANlllVNYbPxQTL0JyUwPjeA4PgbwflPbq%2BCtRO%2Fkl%2BBJZtm22cEchgduJPWs%2FtgwsyoTvACxCVbeE45dJ0QoeKvy5Z60Ep2cjKpxq1kX88ky6q%2BFIA7quslMutqsoPeT2XdyeSnjQzdW76r4e8u0YHopYE0%2BuLxOtTqht%2Fd4RR7d4wKatPgSrxwmlaBGdYGUZqeQhLrFfQvGZrtzQsGBxRaVCqC5d98IwJQt3cY1mBOKGOKcGTLgu8WDcO48w5Y7lMM540tfGUFv3OnWKI79uNjy8XC3guMdkS4c3zwy90g7Nz5GRxmrgCa7MZwh0Hrl4CkS3Pa%2B5TMK6JxhY70EfVCjtPuMBB7EP9XzDS%2ByW5yAIh3pTfVkrQOetuaM0VSK9MtyH8t8SXBHLzfx%2B628oMLdJm9%2FmpA18IHuhrZFMhApZdrDb%2BF6ZzREC3Nmf%2FJMbrlJ1yubpfeM5JH7WrzyAW97B1x4%2BaEnC421MAgRKhhDM4l1B%2Frv5%2F6vbfuGL5XNC7Nrz%2FhR5etAXmMm2o87FMwmuWNiGVTO6cfdsv2juL6ciZV%2FWM6u73l4dIPaADD2KOLgNejF1I5HipM3E%2BXQBPU5w9UM10AI0etr5gEkEpEYZD9kahzAj9ygX4pRjCC26rWBjqkAbY3YlIb68%2Fn9jDJFan9S3rpJ5otcCjrdCwhDwOgEixVK3k7DTniZNou6fmsHOWR00L9O6GthczHAckpwCjf9BL%2BXY%2FG%2BtpJe2kMS6f1RCAQw%2FwLi%2FkbpdAMAJCphuQIsW%2Fw90PDcAbgdXAl9eDkZ08L5HfizR57aADxFQyZM9uhMW4E%2FNMQ3t%2B5r8%2B70QxKnmJzo06H3BX71XNY1dquml3kaG42&X-Amz-Signature=3d9a154e1a58e1cf2d8524e72ae9a2ae3517c4bf6eaf4d99607d4f0b14c9aa4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
