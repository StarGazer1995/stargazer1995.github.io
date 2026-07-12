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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RYNYC%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T164332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIF48RwW4%2Fh%2FDGaYZKy08mJVg0QXf%2BhHtk2rgE%2BCFE%2BveAiEA5nttZciKGwbkQvoswacln9amn8eRYWR6nHVendOjn30qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuHqMff1QOk15A7vSrcAxMnb%2FC8HAJ9LI67A9dO2TCRjEGph3VyzQYDrfyuf0mzslfMiCoJ%2BGYo6SpWJDGmnqkOLw%2B56mUIrs14OLOKQyus62JmMeLkhFEuEI4fpw5yle%2Bz9%2Fa0kkLlPAx%2FawAxjk4JaQ6vF9H61NlIKpKj%2B3xynXjxRkrHqM9dbxLpk%2BPHAJOcDFYmNil1glwP4cAuMgidlMzqhPxMs7cmUh80ZpeZxlHunfBlMRvEf3rpq0vN9Gvv3B8cb0TJZbrxSF8qQvUxBnODJrY2YYoY%2BU49D1c55ATjzI6y0qScZ5A0hs9JgW2lfSHAk3rcaScIyrgybtOYdQpc40K6cvBA3ZFeMnUi4Zfjh9yABf31epJbC8kYrbNAJ8A7gjvN2DtGF3vQ11rIykjNXFMwx8%2B8CF5eGx88dJBsVdDdWMFIi4PsWM00coj0wwIjA6DJFT%2FZObvQ174i6fUtmxfhpBpBVsAuscx8jbRtFpLO0ycoKvHvf%2FEP32iDxZQHne528s4zjYeVMg4QcVwJoo%2BaWnN63rMhcBQNGBy3GdIigRIVsYOO31xQUVCLk7S9f6x8iYIYlPnJze%2F1TL%2BDPAkvD4Jzpp4UoTCfbS464joaE22QmYClLSaJQRbRSvdb6wp%2FycAiMPmAztIGOqUB%2B6f0E74VzrlfyEI5og0TyV9U%2FPLtMVx6STX%2BmV5RJYsTsiI1HKerY5%2BQW0qB2zRRoXp8J68QW%2F8aFE3qZmn0Nw%2FO%2BhQC1OyMUDQLfM15U80Uauu77jg6uwwTR8gnUT8D27pro6kfTlSOkl9dixXHko5CXS5hEbBHsL0GJOmgEUzid18mr%2FL5kglJxZjN2WIoTee4phNB69Npp%2Bs1HTyMjuDQqEXk&X-Amz-Signature=59c3bb7498e9c9bde9cf53f7168d43cb7b0623628dfb5a8813b6f4214be3fec6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RYNYC%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T164332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIF48RwW4%2Fh%2FDGaYZKy08mJVg0QXf%2BhHtk2rgE%2BCFE%2BveAiEA5nttZciKGwbkQvoswacln9amn8eRYWR6nHVendOjn30qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuHqMff1QOk15A7vSrcAxMnb%2FC8HAJ9LI67A9dO2TCRjEGph3VyzQYDrfyuf0mzslfMiCoJ%2BGYo6SpWJDGmnqkOLw%2B56mUIrs14OLOKQyus62JmMeLkhFEuEI4fpw5yle%2Bz9%2Fa0kkLlPAx%2FawAxjk4JaQ6vF9H61NlIKpKj%2B3xynXjxRkrHqM9dbxLpk%2BPHAJOcDFYmNil1glwP4cAuMgidlMzqhPxMs7cmUh80ZpeZxlHunfBlMRvEf3rpq0vN9Gvv3B8cb0TJZbrxSF8qQvUxBnODJrY2YYoY%2BU49D1c55ATjzI6y0qScZ5A0hs9JgW2lfSHAk3rcaScIyrgybtOYdQpc40K6cvBA3ZFeMnUi4Zfjh9yABf31epJbC8kYrbNAJ8A7gjvN2DtGF3vQ11rIykjNXFMwx8%2B8CF5eGx88dJBsVdDdWMFIi4PsWM00coj0wwIjA6DJFT%2FZObvQ174i6fUtmxfhpBpBVsAuscx8jbRtFpLO0ycoKvHvf%2FEP32iDxZQHne528s4zjYeVMg4QcVwJoo%2BaWnN63rMhcBQNGBy3GdIigRIVsYOO31xQUVCLk7S9f6x8iYIYlPnJze%2F1TL%2BDPAkvD4Jzpp4UoTCfbS464joaE22QmYClLSaJQRbRSvdb6wp%2FycAiMPmAztIGOqUB%2B6f0E74VzrlfyEI5og0TyV9U%2FPLtMVx6STX%2BmV5RJYsTsiI1HKerY5%2BQW0qB2zRRoXp8J68QW%2F8aFE3qZmn0Nw%2FO%2BhQC1OyMUDQLfM15U80Uauu77jg6uwwTR8gnUT8D27pro6kfTlSOkl9dixXHko5CXS5hEbBHsL0GJOmgEUzid18mr%2FL5kglJxZjN2WIoTee4phNB69Npp%2Bs1HTyMjuDQqEXk&X-Amz-Signature=909b4f71f0ae505c20f1e8caa3da1374d687418329e39e864f8d0c2b7da5cd15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
