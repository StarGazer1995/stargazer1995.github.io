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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVAUOMDM%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T012744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIAyns65AUXeb1gfq%2FTn7YngxL%2FHxXb6yHc0M7eOr3vGJAiAxCUjm2Y7F0cVQguT8Mg%2F84JszTRJuG5rOi7AXHGamyCqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBgfXXYUUEAlSULMeKtwDmp%2F3kBs51WW7dyYrS566mYSkiPCSIRIgxfs68Z75EjKSf8%2BUSd6mENGRsW1lI2m%2B5fjqv2s3XdCiYpEHrDdS6fKrWrjk7sbE%2FOY36O7r42Jcm46Zmqlme36lIAfTaeSlsOxN%2B%2FnIHD7CeNM3xsYTjSTrx36p911ZWek6l5r4N4THmDKizwwGBV6JUlq8fr91bw31Kp4whbRIt3UirLjnIr0VHmf84ehiD%2BFZ%2FKUljbIRQZ8D0FWuuefrRqd%2BsF4FbCKJWYLHeA%2Bc1HJhwO921tabRdigDS1ePdjyFdz%2FWRMC9pgI87gG2pUo%2BWZ8GbPtMcOBUVuHF7APIPFUaYJKItFINQoYCA%2FKG%2FsUzVPtO8xgbn12ywz3fNpV908HupaMre6N6L3dSntUyb42XPNZV827oHi%2Fnz6kzcr24wlnfLgHqjlVdtkl8hiDeQHX8q2tpBtGM55y1zPQibeSioTHc80vUw6mJGnXvOjJb3856gJoQs8Wx%2FBmun21ZixyFpm2pGDHAzMyfm4p5V2nty%2B1B6gDYy50Koja9dha95y%2F0IRNLVzL%2BSkGxFNyu0l%2FG2rks8hkCw6g3VnH2uI5wRl9djDQJBGUUpUwwA9QkHu6ae0bT0t%2FHJzNPhcljgUw79G50wY6pgFfQ%2BQIjcnJGV2lWh66hVEEWVt9Xddggbp6TkIAbCeDzFFtPYKEZMMnmrac4LRApkw9M5W9BHmXuH1YTtQnzMRhw%2Fa7yRX8TWpSiYMARH8uB5u4VneuuWB8Dswf8hsLOV5q3W6I6Vb2Nx0RQlfqGwpeugXtO1DhWPsqy6Sp1mqsEtMKzEouh0mih9USM0C1K1lLP7D9dXHgk3Sk%2BJsHernkhPXCdIWY&X-Amz-Signature=73245ec00fb1a0135ca0c125b240918bec4fdad73408c3a51be0976e050802a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVAUOMDM%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T012744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIAyns65AUXeb1gfq%2FTn7YngxL%2FHxXb6yHc0M7eOr3vGJAiAxCUjm2Y7F0cVQguT8Mg%2F84JszTRJuG5rOi7AXHGamyCqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBgfXXYUUEAlSULMeKtwDmp%2F3kBs51WW7dyYrS566mYSkiPCSIRIgxfs68Z75EjKSf8%2BUSd6mENGRsW1lI2m%2B5fjqv2s3XdCiYpEHrDdS6fKrWrjk7sbE%2FOY36O7r42Jcm46Zmqlme36lIAfTaeSlsOxN%2B%2FnIHD7CeNM3xsYTjSTrx36p911ZWek6l5r4N4THmDKizwwGBV6JUlq8fr91bw31Kp4whbRIt3UirLjnIr0VHmf84ehiD%2BFZ%2FKUljbIRQZ8D0FWuuefrRqd%2BsF4FbCKJWYLHeA%2Bc1HJhwO921tabRdigDS1ePdjyFdz%2FWRMC9pgI87gG2pUo%2BWZ8GbPtMcOBUVuHF7APIPFUaYJKItFINQoYCA%2FKG%2FsUzVPtO8xgbn12ywz3fNpV908HupaMre6N6L3dSntUyb42XPNZV827oHi%2Fnz6kzcr24wlnfLgHqjlVdtkl8hiDeQHX8q2tpBtGM55y1zPQibeSioTHc80vUw6mJGnXvOjJb3856gJoQs8Wx%2FBmun21ZixyFpm2pGDHAzMyfm4p5V2nty%2B1B6gDYy50Koja9dha95y%2F0IRNLVzL%2BSkGxFNyu0l%2FG2rks8hkCw6g3VnH2uI5wRl9djDQJBGUUpUwwA9QkHu6ae0bT0t%2FHJzNPhcljgUw79G50wY6pgFfQ%2BQIjcnJGV2lWh66hVEEWVt9Xddggbp6TkIAbCeDzFFtPYKEZMMnmrac4LRApkw9M5W9BHmXuH1YTtQnzMRhw%2Fa7yRX8TWpSiYMARH8uB5u4VneuuWB8Dswf8hsLOV5q3W6I6Vb2Nx0RQlfqGwpeugXtO1DhWPsqy6Sp1mqsEtMKzEouh0mih9USM0C1K1lLP7D9dXHgk3Sk%2BJsHernkhPXCdIWY&X-Amz-Signature=3f2d78f47a6334401c07be9abbd7c82524e46a726e9536e8b3da97a0f3574780&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
