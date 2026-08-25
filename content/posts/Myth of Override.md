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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO255VJF%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T042746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIE4%2BEsdaF6oMD510yGPuWHpo5%2BOW%2Fq6KtnTHxB6XuRDZAiEA7ZiexhuuatFK4G6UA3mIZlyFYun0O54WfNbMIHPTgkgqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJzVJDM30P2oHukExCrcA5mPkLRoHy9ggkVLTwqQlOQBEbQb4S8behWtsWqHa0KhfjVT5%2B9%2BYn7Ak2PLk%2Bqw4pCS7JK5llHeG7%2BIrq8qDFjWvFAz73pYoQ4Qo%2BFWkcBW9N6DVBg8JasT87vkK9tSaQ9aWh%2FXzZdkpG%2FMlFYUsgTVS9yhISqiqYs8FLA6bW0ln%2FoaPv%2BBYtmluDYIjN25ZQ3%2F7N4gwZ9JvNmKURGWl4muWIPSWjcBrk1HLLJljgaApa47vfYBqdfqSVYa%2Bnzei3lYBs970%2FFFGBHR4z8aU3BGdaTqTgg4Zm7sP5ImQEjaSBbk5RE3aPDgKfVih4hL4k%2BMstMtgRyTktRyBbWBf2nA7j6YSKvDhUcVeEXO7A%2FP6p%2BwooFU9KFKR5LwEdsg6USXHHId9QS6cFEGswkiVI8YQad25xC2CK3gKbI%2B%2BBWt%2Bb98Mnnr%2FqsyOlWQX3gE3lgVi2NAJT4op3PSUH2PdRsG9wBvH%2FmYAVhV8JlVnvSvgorRtTC1Dj3SPMp2iRYEPRrRpExSDzKiBRRup2JgYOqv6XHSytpoXGAUcMBZQLbeThjvnl0x3Fb75VRrRQRKzi4AyLf1GmjdiT%2BtfNzHnWTi%2FkU0xPrZDv%2B69gEsChHqWpYchL4Yy5UZTasqMPzRs9QGOqUBnbCHYW6PmNwh2ZN1lIlBpSSoCWdq7qq90Tm%2FZJidlFNMDJ44MiTUtZq4LtqeNtR3Xlpw8sRFzmAYHkO6%2F3jtCN3TSuRHBviRmxyY2N4eTLWTwNLZ2%2B3RpZRv7xoS769jcMUr2XeokKR9GT37IJt7KooTae%2FBQe48G%2FKOdC7z87rQs11pApn0dZC9tSrCBALNzssQVh4%2FhOYNq6YLNLQ0ayxmAAV0&X-Amz-Signature=e703bffd8172d6596d6d55d379d175738c3fa4fa2d018395ef5a6ce98cf8353a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO255VJF%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T042746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIE4%2BEsdaF6oMD510yGPuWHpo5%2BOW%2Fq6KtnTHxB6XuRDZAiEA7ZiexhuuatFK4G6UA3mIZlyFYun0O54WfNbMIHPTgkgqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJzVJDM30P2oHukExCrcA5mPkLRoHy9ggkVLTwqQlOQBEbQb4S8behWtsWqHa0KhfjVT5%2B9%2BYn7Ak2PLk%2Bqw4pCS7JK5llHeG7%2BIrq8qDFjWvFAz73pYoQ4Qo%2BFWkcBW9N6DVBg8JasT87vkK9tSaQ9aWh%2FXzZdkpG%2FMlFYUsgTVS9yhISqiqYs8FLA6bW0ln%2FoaPv%2BBYtmluDYIjN25ZQ3%2F7N4gwZ9JvNmKURGWl4muWIPSWjcBrk1HLLJljgaApa47vfYBqdfqSVYa%2Bnzei3lYBs970%2FFFGBHR4z8aU3BGdaTqTgg4Zm7sP5ImQEjaSBbk5RE3aPDgKfVih4hL4k%2BMstMtgRyTktRyBbWBf2nA7j6YSKvDhUcVeEXO7A%2FP6p%2BwooFU9KFKR5LwEdsg6USXHHId9QS6cFEGswkiVI8YQad25xC2CK3gKbI%2B%2BBWt%2Bb98Mnnr%2FqsyOlWQX3gE3lgVi2NAJT4op3PSUH2PdRsG9wBvH%2FmYAVhV8JlVnvSvgorRtTC1Dj3SPMp2iRYEPRrRpExSDzKiBRRup2JgYOqv6XHSytpoXGAUcMBZQLbeThjvnl0x3Fb75VRrRQRKzi4AyLf1GmjdiT%2BtfNzHnWTi%2FkU0xPrZDv%2B69gEsChHqWpYchL4Yy5UZTasqMPzRs9QGOqUBnbCHYW6PmNwh2ZN1lIlBpSSoCWdq7qq90Tm%2FZJidlFNMDJ44MiTUtZq4LtqeNtR3Xlpw8sRFzmAYHkO6%2F3jtCN3TSuRHBviRmxyY2N4eTLWTwNLZ2%2B3RpZRv7xoS769jcMUr2XeokKR9GT37IJt7KooTae%2FBQe48G%2FKOdC7z87rQs11pApn0dZC9tSrCBALNzssQVh4%2FhOYNq6YLNLQ0ayxmAAV0&X-Amz-Signature=09506c0545499285f9861c1e9f9e9dfcab096961a8ff98e6f678c39df5fa8faa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
