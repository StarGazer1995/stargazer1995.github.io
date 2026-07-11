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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IW2X2JF%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T105313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDjGiXS%2FtYRrvlSD2IwQD1NGTTO9Bxk3nsLpClM%2FvOR0AIhAMvOo7dGBJelzhiJd95Jz0jsh0Qs1%2BBxlrh%2FvSa0ryIJKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBMbVvd%2Bso3LibNjUq3APohfPePqdg1N8MRrTdgKmObRZiHxYlrSWaS1tuEcREvWsM7TZ4xso5e7ajn8RmqPG0MS34I8Yo3Z%2FK1OtJkYD97gsY1rQYuHYjyAzKdl%2Bia9KXDisUigIqLpXu3ALopzd95FJWMOiMbqlPA%2FkKNs%2BIL6MkGHFVujVpCAWTuAoBrjXCV6n6CTr9f%2FqBsOjbxkaZljJ5U8llJGm4aWVoZqUAo%2BchNJ7%2Fngizqh8UJ4vcE75S%2FyEuePJ8sX9ablcFEekGiK%2FNaTWi26Hgf5J2BbNldaTiYwA8spo5t%2BpS2ZCqDt96k0zEb8FtCaISf%2FYE7PRE%2BItPyU8%2Bf787uK5DyAyeX3LbhcCEd0x6X56IH1aAk1dHRvOjamqQ3SF8R4uB75rJ4fWvXiZiRRD4rQEv2wIRfGZmIXJcE7gQtqSciGFwivTCi0Xcw9rh8MdulR3tM73q5nZS60FEoSRCOycGObh2PnmmVahK9g6rqXamcCq1xIlAKquGpUBbqc%2BvFuC1PaKKvT%2FvfbYoH7Xsf%2BLyjvOBTYBeZT4NMzSCuHgoCOB3%2B%2B6HC5TfHso6geUKwyOwukqV6cKLBN0SycRs27j30WxLH29sLwYYlrH9mzE%2F7twndFUNaJvUMk%2FqijucgTD4osjSBjqkAZc9kXta79egRRnXE7DbvbccLtFYgrZQAmK7Uj7oZWzLabW0dbBRHyaKKVy%2F1soHLS4%2F9xh64QLqz1BS%2B7CJbqnzJJ8%2BBFDmL98szFT%2BzmfF5O2MeRwD0s%2F0aeRF7jlEzKlA2ots9xnQE5fpQkEs3IUfNr%2BcHz16KO9ryh7dIuWeK%2F8s9RPXlOzOM7gOtWEkJFA4035LDAGMoQ5BE5%2FA6nepZ7J%2F&X-Amz-Signature=4cda7fe83b1ec11e23657d459adb3efc36a162ec510fd22f03b95780010d0960&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IW2X2JF%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T105313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDjGiXS%2FtYRrvlSD2IwQD1NGTTO9Bxk3nsLpClM%2FvOR0AIhAMvOo7dGBJelzhiJd95Jz0jsh0Qs1%2BBxlrh%2FvSa0ryIJKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBMbVvd%2Bso3LibNjUq3APohfPePqdg1N8MRrTdgKmObRZiHxYlrSWaS1tuEcREvWsM7TZ4xso5e7ajn8RmqPG0MS34I8Yo3Z%2FK1OtJkYD97gsY1rQYuHYjyAzKdl%2Bia9KXDisUigIqLpXu3ALopzd95FJWMOiMbqlPA%2FkKNs%2BIL6MkGHFVujVpCAWTuAoBrjXCV6n6CTr9f%2FqBsOjbxkaZljJ5U8llJGm4aWVoZqUAo%2BchNJ7%2Fngizqh8UJ4vcE75S%2FyEuePJ8sX9ablcFEekGiK%2FNaTWi26Hgf5J2BbNldaTiYwA8spo5t%2BpS2ZCqDt96k0zEb8FtCaISf%2FYE7PRE%2BItPyU8%2Bf787uK5DyAyeX3LbhcCEd0x6X56IH1aAk1dHRvOjamqQ3SF8R4uB75rJ4fWvXiZiRRD4rQEv2wIRfGZmIXJcE7gQtqSciGFwivTCi0Xcw9rh8MdulR3tM73q5nZS60FEoSRCOycGObh2PnmmVahK9g6rqXamcCq1xIlAKquGpUBbqc%2BvFuC1PaKKvT%2FvfbYoH7Xsf%2BLyjvOBTYBeZT4NMzSCuHgoCOB3%2B%2B6HC5TfHso6geUKwyOwukqV6cKLBN0SycRs27j30WxLH29sLwYYlrH9mzE%2F7twndFUNaJvUMk%2FqijucgTD4osjSBjqkAZc9kXta79egRRnXE7DbvbccLtFYgrZQAmK7Uj7oZWzLabW0dbBRHyaKKVy%2F1soHLS4%2F9xh64QLqz1BS%2B7CJbqnzJJ8%2BBFDmL98szFT%2BzmfF5O2MeRwD0s%2F0aeRF7jlEzKlA2ots9xnQE5fpQkEs3IUfNr%2BcHz16KO9ryh7dIuWeK%2F8s9RPXlOzOM7gOtWEkJFA4035LDAGMoQ5BE5%2FA6nepZ7J%2F&X-Amz-Signature=92790a6511f470d2cb625d3c1ee5f680d2e61a86fe2b723d8633662679e5879f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
