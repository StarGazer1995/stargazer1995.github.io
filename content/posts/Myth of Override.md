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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZXMRDJJ%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T125450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGS%2FeiHUDBMdvN%2BAYEtIeeC4LTzDPxI6EYhFROC8ns2bAiEA091cCxdl8PmjsyAYJZ0F9yv1s3Ueca7eBKUzuY8bvZcqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPq5p%2FfRAkspMn2IoircA7GApo%2BtZjRsaeYJ3NdjGyeSOhZKwBFAHmb3wWmv4diuiSnG%2B6wDCANoZebnp%2Bfq%2FrvcJNMVPB94YGTViKGn9GLL2L6y6utE2sPGbbcOk5MpiCfkCzzngFyzhCko97hEdWAQoYsHPSZeHf7OtJDTlj%2F%2B6zgMBKENAgv4qqeFxislvHd7cDCTRA57k7OCRpQ4b%2FYZcyKgZu8Y23FTzk%2FgPDDi%2FV0ZOH5mmxNqdLRpvBQNN3tEBdU9fwhCTSZnJPoXLYmKPwUUJWI4Ryrj3GWwQzJoym3LAVTUtt%2BRk95DftLbxCSpv5RY3hmegrrvtaZa3L5cy7p3Tqllxf8cIOSdhrZjda4XBVP9P71paN78O1LTXCwwVvM7BpOaI9ZSu8ZM9uQwhg4wW5MKQ76XYkAGku%2FscvQ7GGUi5Mm1HIblBoosG5z1x3EnafySv7GvyggEOk3Whs5d%2BFc0msnbM58yo6edsf22vb5Ti3R3%2BHZVT9Wlu%2FauixcIca6lFs3QrXlUP1oVdVqf0CZGnJ9kj4Tx2lirGkC3ZHjOYiO6ceKU04Qq2m%2Faiwy8szAoOCsuqdaTaulkftWVL0V%2Bma8ha7e7wNscV%2BnbkYq2UN3%2Bnnsu8QqSoayDcw%2FufCZT7jdbML3bydUGOqUBa2Gs2kQGgNBpVUb1dW4ael6juCJHEtSBrf5KHn57VDfHG6g8PWd487%2FPhDbGWq6PZDUxgrzkvOZoaxYrqrE2N6GEgp4OaygHmQwGAJaPgLhsD%2B8hViQbu3lsT2x6X7KW2SWWeEqPvaKgg088uTO3cd3V81OxA4kzs%2FkJTe2DGnskbL9P6nHK990pQRT3H9tZlgDvJtwUwAwCHxonHgz%2BNei%2FMD4t&X-Amz-Signature=0630d9a5bd75a87281b0b520a3dec5c7e0cf282facf15f0b37d4760c11556f4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZXMRDJJ%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T125450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGS%2FeiHUDBMdvN%2BAYEtIeeC4LTzDPxI6EYhFROC8ns2bAiEA091cCxdl8PmjsyAYJZ0F9yv1s3Ueca7eBKUzuY8bvZcqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPq5p%2FfRAkspMn2IoircA7GApo%2BtZjRsaeYJ3NdjGyeSOhZKwBFAHmb3wWmv4diuiSnG%2B6wDCANoZebnp%2Bfq%2FrvcJNMVPB94YGTViKGn9GLL2L6y6utE2sPGbbcOk5MpiCfkCzzngFyzhCko97hEdWAQoYsHPSZeHf7OtJDTlj%2F%2B6zgMBKENAgv4qqeFxislvHd7cDCTRA57k7OCRpQ4b%2FYZcyKgZu8Y23FTzk%2FgPDDi%2FV0ZOH5mmxNqdLRpvBQNN3tEBdU9fwhCTSZnJPoXLYmKPwUUJWI4Ryrj3GWwQzJoym3LAVTUtt%2BRk95DftLbxCSpv5RY3hmegrrvtaZa3L5cy7p3Tqllxf8cIOSdhrZjda4XBVP9P71paN78O1LTXCwwVvM7BpOaI9ZSu8ZM9uQwhg4wW5MKQ76XYkAGku%2FscvQ7GGUi5Mm1HIblBoosG5z1x3EnafySv7GvyggEOk3Whs5d%2BFc0msnbM58yo6edsf22vb5Ti3R3%2BHZVT9Wlu%2FauixcIca6lFs3QrXlUP1oVdVqf0CZGnJ9kj4Tx2lirGkC3ZHjOYiO6ceKU04Qq2m%2Faiwy8szAoOCsuqdaTaulkftWVL0V%2Bma8ha7e7wNscV%2BnbkYq2UN3%2Bnnsu8QqSoayDcw%2FufCZT7jdbML3bydUGOqUBa2Gs2kQGgNBpVUb1dW4ael6juCJHEtSBrf5KHn57VDfHG6g8PWd487%2FPhDbGWq6PZDUxgrzkvOZoaxYrqrE2N6GEgp4OaygHmQwGAJaPgLhsD%2B8hViQbu3lsT2x6X7KW2SWWeEqPvaKgg088uTO3cd3V81OxA4kzs%2FkJTe2DGnskbL9P6nHK990pQRT3H9tZlgDvJtwUwAwCHxonHgz%2BNei%2FMD4t&X-Amz-Signature=e2106c64c10aad553eaefd580bb0e270e7c57804d856237922ab3afc7add0c6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
