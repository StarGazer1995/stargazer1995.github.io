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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDFBIJ7N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAzE9OMVbN6gX1Y2%2BdgVaN5DzoLyMIhUrX4kj1w0JrFZAiBy4ErDbFaq6TC3neacACPd5k8YBabE8L5cGN%2BCy%2FXQsyqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BSBpvyT9IDin3CmFKtwDaw%2BOM%2BDdBcOUVMTGy3%2BoHANaKXxsJpS2xInKuwTlotIH9CnS2Sq75p%2BMXQSha%2BBXPQepA6osC8Nd2jhuR%2FTXv6E8bodvUUHm7sbb0zD4gTEhBQNAoQlXOtYkK5CujXUHnoNjHzMRSYsGUJsh%2BPOtMfy4vlcQH89W5AgrlpFP1SS%2FGuR7WDMI7Hnzr9wm4cnayivL67ImFEpEiGSCyUXnoejjOMIQcbdB%2F0tL5IVlwjlw4yktKrtPCt3yn501ver1OKVDrPUVh9MO2e7bhZF%2FxFX4olOBnLyj4R4BTeJnLe%2FzAnbM4LPic2p%2Bk2rYpE8hKw8uk8Q6qD9zZ%2BwINEy2nC5KDCvck%2ByzutWC40l5CDqBxDHRnGL4Xnp5D5Bli3Pr0VGkjfEfXZJewwM1vfWHDNS7Q0y3Wmg4qoyfRY23Iuu2B8CDIJy1cynuoCefYuJHhITcNy3%2BNMW9PmQdo90x5K%2FMmN5rvpUh7Hfpqdr04Jx4T7bC%2F4BtcFaZNfJ6fRx8j9F%2FCyGwEy15QzOf%2FIJaPPWeJM%2BPi2w4E5lkS9VcdLlqcyegHzQxAeV4FapOwmLXbvCDILtCp5DF6J58hClHXrSX8DlNVS27eet%2FSty%2FGU0bMDg7fm9mvq3TaUswivj90gY6pgE4pxAFIqGeH1I4iO5oMxE8OZ9StBhyRAQJybKsk9YwhRHJ2PZ%2BtmhiDq3o1YOfPvAmc5Bh3D111JFmhXiSBs4Pis%2FgfD%2B4VafaDGItjDXpqIWLGRS%2FZ0fCPTUtX9VymLCrDxIuUF2vnTZhKk5TYUhiECh5sRrh8g4C55i3hDkvRq7JroeBOIlAstKScLN3sZ0HOdlOn9OocLaJlQHlC2EfsD%2BgeVIM&X-Amz-Signature=0814a57ec29b35db82f8f8b3deb3dd0610ba2e5bf801cda696d6ce2a5c2219a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDFBIJ7N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T152852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAzE9OMVbN6gX1Y2%2BdgVaN5DzoLyMIhUrX4kj1w0JrFZAiBy4ErDbFaq6TC3neacACPd5k8YBabE8L5cGN%2BCy%2FXQsyqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BSBpvyT9IDin3CmFKtwDaw%2BOM%2BDdBcOUVMTGy3%2BoHANaKXxsJpS2xInKuwTlotIH9CnS2Sq75p%2BMXQSha%2BBXPQepA6osC8Nd2jhuR%2FTXv6E8bodvUUHm7sbb0zD4gTEhBQNAoQlXOtYkK5CujXUHnoNjHzMRSYsGUJsh%2BPOtMfy4vlcQH89W5AgrlpFP1SS%2FGuR7WDMI7Hnzr9wm4cnayivL67ImFEpEiGSCyUXnoejjOMIQcbdB%2F0tL5IVlwjlw4yktKrtPCt3yn501ver1OKVDrPUVh9MO2e7bhZF%2FxFX4olOBnLyj4R4BTeJnLe%2FzAnbM4LPic2p%2Bk2rYpE8hKw8uk8Q6qD9zZ%2BwINEy2nC5KDCvck%2ByzutWC40l5CDqBxDHRnGL4Xnp5D5Bli3Pr0VGkjfEfXZJewwM1vfWHDNS7Q0y3Wmg4qoyfRY23Iuu2B8CDIJy1cynuoCefYuJHhITcNy3%2BNMW9PmQdo90x5K%2FMmN5rvpUh7Hfpqdr04Jx4T7bC%2F4BtcFaZNfJ6fRx8j9F%2FCyGwEy15QzOf%2FIJaPPWeJM%2BPi2w4E5lkS9VcdLlqcyegHzQxAeV4FapOwmLXbvCDILtCp5DF6J58hClHXrSX8DlNVS27eet%2FSty%2FGU0bMDg7fm9mvq3TaUswivj90gY6pgE4pxAFIqGeH1I4iO5oMxE8OZ9StBhyRAQJybKsk9YwhRHJ2PZ%2BtmhiDq3o1YOfPvAmc5Bh3D111JFmhXiSBs4Pis%2FgfD%2B4VafaDGItjDXpqIWLGRS%2FZ0fCPTUtX9VymLCrDxIuUF2vnTZhKk5TYUhiECh5sRrh8g4C55i3hDkvRq7JroeBOIlAstKScLN3sZ0HOdlOn9OocLaJlQHlC2EfsD%2BgeVIM&X-Amz-Signature=9ec85f3bcbb5ea8c5f1d9ed772f0057b056368771a7d7c2b5541a0c6ed58421e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
