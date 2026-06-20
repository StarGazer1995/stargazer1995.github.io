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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZE5AQSR%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T074159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCdr2so%2FNhz%2B33%2FVbxJEXrsHZwiD8gwirvb95mWKg9zXgIhALpvG8wA9r2VWSjpOD2%2FTq72RaNpQ1hU%2B7Gcv9DLgnnVKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzooO%2BiCwCI06NGF%2Fcq3AMH4YAfZgwlnBSbMlFTDDdeKH2p8F4MMxq%2BtgZkZH1YRBP0Hx%2BFZ1A5G%2F6jNfRZAQMEiPtA0zqk7DfZlS%2FlKS41FVb8ROVaOtPWiS7Xb6NJKTMfPj8kTtEw%2Fx822YtmZqwWhoO0Vt80MObi4hvC%2BxbNWtK7bcMLvM7fhDbZMysqiwtA7UIoi55Ln6Y8qTR6ln%2BnQpqSHS0%2BXKES%2F85mywHXR86sQQvO7KO2QeHDbCcoyTcDlPmqiYtJCC78h7QadFmBH2M6Fg3Lr%2F1JU5Sek%2BM9ANDjkHtvmpV3YGswwoMgEbl5R9focwaaDfmPq6yQNg0bAnGp2oP%2BHKDPuFlJt5LlGtFl%2BGHqDiR7SH6AlUu%2Bf03nePb%2BQb6FFUnxXX2J8IOWnCsHRt%2BVTZ6zlk3OTVQAp6bOx%2FtjhpdM%2FJm43IqKzQ%2FoCvtPUHlp6tapqMTEXyurvmVjDvdu7nqJhIFINdTF90FN9BdaAY7SWiEE71wq3HFLdtMyMPtnbeqnM78kMarhbQVU8mu2yIlRq6HZWYa92Zm4%2FNp4T7PJb6PiWlBztv0fM6aAmOlCzP5fhb%2F5r5nEY%2BcwTUgyfaIyRvNalUqVJ874gvd0R%2FWz7DYPhnYIJrlUskwBMeRJS1hMZTDg8NjRBjqkAdmnPmhHFc7HifcShmLlA0GtAwvJbtNeJSU0JUMKICTDsrpioxUgGJyX5V4ay34yWJ5ktdwxSbGxyA3GLMcRhhCa5stykm%2BdwbHjuBrpflxeD04mSpfMQIW1gueZWc2LCDOCNtHo9JdwyXEvFfe%2F1IOQdpEmaxGnNVLLFp0R2Uh9G%2FDhAaetu3rbyd9fZMDsmJDZ8KvQ8ytj%2BmAK6vX73KKGlh5R&X-Amz-Signature=7291134521eeeecd21951c5c456907d65cbd91452ec6cc9870e32965732b4a17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZE5AQSR%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T074159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQCdr2so%2FNhz%2B33%2FVbxJEXrsHZwiD8gwirvb95mWKg9zXgIhALpvG8wA9r2VWSjpOD2%2FTq72RaNpQ1hU%2B7Gcv9DLgnnVKogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzooO%2BiCwCI06NGF%2Fcq3AMH4YAfZgwlnBSbMlFTDDdeKH2p8F4MMxq%2BtgZkZH1YRBP0Hx%2BFZ1A5G%2F6jNfRZAQMEiPtA0zqk7DfZlS%2FlKS41FVb8ROVaOtPWiS7Xb6NJKTMfPj8kTtEw%2Fx822YtmZqwWhoO0Vt80MObi4hvC%2BxbNWtK7bcMLvM7fhDbZMysqiwtA7UIoi55Ln6Y8qTR6ln%2BnQpqSHS0%2BXKES%2F85mywHXR86sQQvO7KO2QeHDbCcoyTcDlPmqiYtJCC78h7QadFmBH2M6Fg3Lr%2F1JU5Sek%2BM9ANDjkHtvmpV3YGswwoMgEbl5R9focwaaDfmPq6yQNg0bAnGp2oP%2BHKDPuFlJt5LlGtFl%2BGHqDiR7SH6AlUu%2Bf03nePb%2BQb6FFUnxXX2J8IOWnCsHRt%2BVTZ6zlk3OTVQAp6bOx%2FtjhpdM%2FJm43IqKzQ%2FoCvtPUHlp6tapqMTEXyurvmVjDvdu7nqJhIFINdTF90FN9BdaAY7SWiEE71wq3HFLdtMyMPtnbeqnM78kMarhbQVU8mu2yIlRq6HZWYa92Zm4%2FNp4T7PJb6PiWlBztv0fM6aAmOlCzP5fhb%2F5r5nEY%2BcwTUgyfaIyRvNalUqVJ874gvd0R%2FWz7DYPhnYIJrlUskwBMeRJS1hMZTDg8NjRBjqkAdmnPmhHFc7HifcShmLlA0GtAwvJbtNeJSU0JUMKICTDsrpioxUgGJyX5V4ay34yWJ5ktdwxSbGxyA3GLMcRhhCa5stykm%2BdwbHjuBrpflxeD04mSpfMQIW1gueZWc2LCDOCNtHo9JdwyXEvFfe%2F1IOQdpEmaxGnNVLLFp0R2Uh9G%2FDhAaetu3rbyd9fZMDsmJDZ8KvQ8ytj%2BmAK6vX73KKGlh5R&X-Amz-Signature=650d2e82a53cd2a84beb2f7bf27c116e61c6780f151ae1399f4b82af31a3d415&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
