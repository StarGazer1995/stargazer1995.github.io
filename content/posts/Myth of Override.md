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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URBTG2OM%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T112021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIESMlWiJFawHOK6Xd1ZfQBb2ov1UeIJ506OrsV%2B06MRsAiBB2p4fiEqMe209UAg5eJelbgYneX5%2F7%2BkfrKubiTTDcSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMOHqlonpyud49Cl44KtwDN9hP8FHNm0uc%2BIotMc0eDt%2FlQVRSew84uX0BfLPtLoZx2LFV3iVruUtqTulDwdGnrXBxGxhOHOAldU5ThyeliuPgtGEpuCtQbDRYRdx4cDEODRmBkgwLHZYEay9zDPV8Ou5LUduD8FawCa8g0ZVH8aaekKu%2BDFBUR%2B%2BTXlaQJLTBeDfUl7SvYUR4DOvv9aF6VTlvttNsvwZfuRUh6b80P%2BqepSE6B%2BVOXG0gkrCM%2BNHjU8gaU6Ug9ZjapjvIt8YPfLT9huv6Vx6wyjMmAImSyK%2BqiYh5xyq476n29jCRW%2B2YozP1yFGOuoB4kmCh14KEsxQoEdSahDLYZB6I9Gm9VBUenjvsk1XdwuTBdPAY9fhWNhgEgTItLd%2FEGx6R6mxeksQlGtddVc5j5YcGeqEfYggGYBpbnV06jGnt5foacK2FQJ%2BDsurcSBms3Zv1flIsLbJCpDnpUAKxnGq8BOVVKavN0UWQdOQYWy2m%2BZUbFaq1BphI4g9eCe9Zsh%2BwzeAKMzAccb0odFJEYm3WkMcQJWelfs49pItI1zxC1YJwK8ftDen1JirLejaHBboU3DaKCMXhfgH2o726UHezmgMGDLvEyTtbHu4ZFibHGIThKDzir8djDEWQpmeaxrww7cXd0gY6pgF54eZBXWvcoRV72cr9V6s0KWt2ERNpNhKr3v3hE2WbFTU3%2FtKwVo1HS0gsOYbFW1JrXpMhyn%2FpkymMyxzw%2FNOy45UU1USfB2m1s%2B9CJ04Q8%2FMBQJ4it%2FzyxMps3h%2BH6ZrWFbuFxaogUEVu7EXF4mF6rFIIBeAZz9wUufVeW0%2FgRrOgwJ6zPcGrSEyyX2NPAGM55jxrv1Z2LE7HuRaxsF3Aye803hQa&X-Amz-Signature=202665c0d87c7c65f1cb913bf4aebb27b74002bd122033e78bf0aadcc4be575f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URBTG2OM%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T112021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIESMlWiJFawHOK6Xd1ZfQBb2ov1UeIJ506OrsV%2B06MRsAiBB2p4fiEqMe209UAg5eJelbgYneX5%2F7%2BkfrKubiTTDcSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMOHqlonpyud49Cl44KtwDN9hP8FHNm0uc%2BIotMc0eDt%2FlQVRSew84uX0BfLPtLoZx2LFV3iVruUtqTulDwdGnrXBxGxhOHOAldU5ThyeliuPgtGEpuCtQbDRYRdx4cDEODRmBkgwLHZYEay9zDPV8Ou5LUduD8FawCa8g0ZVH8aaekKu%2BDFBUR%2B%2BTXlaQJLTBeDfUl7SvYUR4DOvv9aF6VTlvttNsvwZfuRUh6b80P%2BqepSE6B%2BVOXG0gkrCM%2BNHjU8gaU6Ug9ZjapjvIt8YPfLT9huv6Vx6wyjMmAImSyK%2BqiYh5xyq476n29jCRW%2B2YozP1yFGOuoB4kmCh14KEsxQoEdSahDLYZB6I9Gm9VBUenjvsk1XdwuTBdPAY9fhWNhgEgTItLd%2FEGx6R6mxeksQlGtddVc5j5YcGeqEfYggGYBpbnV06jGnt5foacK2FQJ%2BDsurcSBms3Zv1flIsLbJCpDnpUAKxnGq8BOVVKavN0UWQdOQYWy2m%2BZUbFaq1BphI4g9eCe9Zsh%2BwzeAKMzAccb0odFJEYm3WkMcQJWelfs49pItI1zxC1YJwK8ftDen1JirLejaHBboU3DaKCMXhfgH2o726UHezmgMGDLvEyTtbHu4ZFibHGIThKDzir8djDEWQpmeaxrww7cXd0gY6pgF54eZBXWvcoRV72cr9V6s0KWt2ERNpNhKr3v3hE2WbFTU3%2FtKwVo1HS0gsOYbFW1JrXpMhyn%2FpkymMyxzw%2FNOy45UU1USfB2m1s%2B9CJ04Q8%2FMBQJ4it%2FzyxMps3h%2BH6ZrWFbuFxaogUEVu7EXF4mF6rFIIBeAZz9wUufVeW0%2FgRrOgwJ6zPcGrSEyyX2NPAGM55jxrv1Z2LE7HuRaxsF3Aye803hQa&X-Amz-Signature=5783d180035f1aceb32ecf83718791c2202c489acd55efa3fd126679aa42fad3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
