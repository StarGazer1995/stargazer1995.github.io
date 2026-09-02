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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUCQZVGW%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T234036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDoILwlKYIXFOS6HSJXvwwuzajfWDhhy5Pdg9gqbqJ8yAIgSkWJ8TYiMMMBPqlAiQ%2BviwR2y0Txi7oxTGFhpKzC3U4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNXj722dMnJ9Coc%2FtyrcA%2F%2BTbOTdtFUk4WLV%2Fi%2BGUkDSdgHgC6U9Foct1JjThS%2BWWWt0pZUg6IRoVJx246N9Fm59xXW388EpvxRgeK919iSOSFms9XA5kb9pOW8NbEL%2BGvBoOwkSQP0%2BHEaamcIkeZhjTVbgJJOQvhWtGI4EHdZ%2F6IgwCsVMxDq%2FeJpH3MEWJZNhsCawHTH003zFT5M8SHUmGXzz%2Bo1wVQ%2FEnNqoMjIvOh9i3ypvKYBTs9akp55xEd7tlVpbzegNCeD51OY3SGr6aB9NwxU9TR8%2B1CPkM6F%2FiM5ik9v9DZFHMuz78tK2JyeZ15ijyMPg5fL9R%2BUSx1gHSWbInsuugBxj%2Bz%2BcNMOL%2FLgcs77CU36cONPxx1ciYthru2Y%2BsfDVh6Ixhe9jwdekpH6Ym6xkmW0W%2F7qWdOhFhABT5KDKHm4VfRAWIJlxkyBDJRSCDCtCVQDBKCB91RMoGEs2JatQVZj2kCwDgNp5OmaW3VwHwmZymlG2XgemsMv2jL9K1HS5PEv3h7vJTvddZcHYLdw0nemUO2rwawn%2Fhf8A4M1du4C8yYnRHO95O%2Bvf4ZJ2bHe5nXVhbetv22Feui%2Fo08AeOvDt34KQXyyOnzgR%2F807hwl%2B0%2F15rO2YSTVV7PhJCb%2FYv0fZMMLI4tQGOqUB0eJDbkkyT175nXxhrwQ5f%2Bn7%2B7nGw1Ek3x9hWkP8Z7P74PBUfXijGx69sJZDy0RGuIOi0%2BGdpIVwrCtyVwcILGTPXoFi2cKb55%2B0%2BQ2DtCZwNug6XSUpoLnipVpsFEgn4r2%2FSaz5qK9yVoDsQsHmc57XqXEKNndpDTn7mJVelTUnMEE6B5ZGCB8jc%2BwGkTUg7V%2Bl8Go66GXaCtIQJD2fREg2s3b2&X-Amz-Signature=aa3790d1f97476d92250f350df1f79d66ad2d10694d26e8d9712e74f7d49b1f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUCQZVGW%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T234036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDoILwlKYIXFOS6HSJXvwwuzajfWDhhy5Pdg9gqbqJ8yAIgSkWJ8TYiMMMBPqlAiQ%2BviwR2y0Txi7oxTGFhpKzC3U4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNXj722dMnJ9Coc%2FtyrcA%2F%2BTbOTdtFUk4WLV%2Fi%2BGUkDSdgHgC6U9Foct1JjThS%2BWWWt0pZUg6IRoVJx246N9Fm59xXW388EpvxRgeK919iSOSFms9XA5kb9pOW8NbEL%2BGvBoOwkSQP0%2BHEaamcIkeZhjTVbgJJOQvhWtGI4EHdZ%2F6IgwCsVMxDq%2FeJpH3MEWJZNhsCawHTH003zFT5M8SHUmGXzz%2Bo1wVQ%2FEnNqoMjIvOh9i3ypvKYBTs9akp55xEd7tlVpbzegNCeD51OY3SGr6aB9NwxU9TR8%2B1CPkM6F%2FiM5ik9v9DZFHMuz78tK2JyeZ15ijyMPg5fL9R%2BUSx1gHSWbInsuugBxj%2Bz%2BcNMOL%2FLgcs77CU36cONPxx1ciYthru2Y%2BsfDVh6Ixhe9jwdekpH6Ym6xkmW0W%2F7qWdOhFhABT5KDKHm4VfRAWIJlxkyBDJRSCDCtCVQDBKCB91RMoGEs2JatQVZj2kCwDgNp5OmaW3VwHwmZymlG2XgemsMv2jL9K1HS5PEv3h7vJTvddZcHYLdw0nemUO2rwawn%2Fhf8A4M1du4C8yYnRHO95O%2Bvf4ZJ2bHe5nXVhbetv22Feui%2Fo08AeOvDt34KQXyyOnzgR%2F807hwl%2B0%2F15rO2YSTVV7PhJCb%2FYv0fZMMLI4tQGOqUB0eJDbkkyT175nXxhrwQ5f%2Bn7%2B7nGw1Ek3x9hWkP8Z7P74PBUfXijGx69sJZDy0RGuIOi0%2BGdpIVwrCtyVwcILGTPXoFi2cKb55%2B0%2BQ2DtCZwNug6XSUpoLnipVpsFEgn4r2%2FSaz5qK9yVoDsQsHmc57XqXEKNndpDTn7mJVelTUnMEE6B5ZGCB8jc%2BwGkTUg7V%2Bl8Go66GXaCtIQJD2fREg2s3b2&X-Amz-Signature=e80beac085a8b7ef0e23893b41c037e0b3f980fd9209aec54a95509a44204310&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
