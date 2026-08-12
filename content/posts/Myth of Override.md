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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US423R6U%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T124038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQD9UeTCb0xSibNzdaaUaEtIR37gsSFPON%2Ft6mc0MeocEgIhANdnTIe%2BJ8D4aARMf44eHkKhpx84P%2Fz%2BEopkCoecbf5rKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjE%2FezbpY8MZrgrrEq3AMfZrY8PAKiXa4Ixo2WV5bGQtKWQnLPdfdg%2Fr9aZjBNxIe6mClSQW8Vw7kaSM4%2F2ZzjgDdbZyLdUk8BjmG2K%2BHAx7%2B8Zee4Vyk1IBppjTDF%2FxPpvzqkWuX3Vz7nVo0hPlMPmvWANyeY%2BBBYYungun%2BtbQduNWgmBBs8ddevf%2FDlXgtp4jCgkd36p85014crgGF2d4SFIFqk6rQUOlAe2cHLAgVb0aair0mvAzLY%2B5xzYps6yvjsUt0GUaMs%2BPCTnAaFZu3f12mrtVcqW0lrnARFJJPiwbMmgLjgpA3wl1PhPKhbjJdK5Dzk%2F3YyTBUTo5H1ZOsVxv3VUBoTV1QapMsn0vVzMAMUAe3Him2E9KG0bo2iQHlruREJIAdrWFkHl%2Bc%2F5dySpWjL6eHEeyTs8PIAwRzt55YALmcZY9xtCHpvgzG2E%2BnpC0PHbMow5Vk8pLK4S19P3zuO5GDYoVP%2F7KTQW4wuqsFfIKMhz2S1jvX1jjJaZ%2Bgl%2BgAakMu5kEJYEf6TF1jSGjhdLFZzXRjcrlsN88iOzU6ukSZqTeCO903aFht6C17NujOs4FFdtOXQariY6Ym2nahqP536fIEwAGARBm78qRCt8biwR79CznxR42dgkMNVxrSvOV3iZTD7nfHTBjqkAbLc3%2BK6ntl7CCRpca7HfqDPuFkPtDt9IOwhrllvbXhto%2BImgPSzFxwhXszc2IMWOSvxRt4kuYnoFiniDHmapf8u14j9etWn5%2Fdp%2FizIUuc0io%2BWTdrhI4Vv2Po00gAiracb7oa8M4FPUFW%2BjXPtEaML4j2tmcMYvCMVdfje71A4oY5FasXfa1VHS3zTPwZbUvwA2nsTSE15ZeFloz7wOn%2BF6n0h&X-Amz-Signature=9f99249528fec8601b9def582bd7d14d6250ec0f16d00adc52219103839a09a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US423R6U%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T124038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQD9UeTCb0xSibNzdaaUaEtIR37gsSFPON%2Ft6mc0MeocEgIhANdnTIe%2BJ8D4aARMf44eHkKhpx84P%2Fz%2BEopkCoecbf5rKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjE%2FezbpY8MZrgrrEq3AMfZrY8PAKiXa4Ixo2WV5bGQtKWQnLPdfdg%2Fr9aZjBNxIe6mClSQW8Vw7kaSM4%2F2ZzjgDdbZyLdUk8BjmG2K%2BHAx7%2B8Zee4Vyk1IBppjTDF%2FxPpvzqkWuX3Vz7nVo0hPlMPmvWANyeY%2BBBYYungun%2BtbQduNWgmBBs8ddevf%2FDlXgtp4jCgkd36p85014crgGF2d4SFIFqk6rQUOlAe2cHLAgVb0aair0mvAzLY%2B5xzYps6yvjsUt0GUaMs%2BPCTnAaFZu3f12mrtVcqW0lrnARFJJPiwbMmgLjgpA3wl1PhPKhbjJdK5Dzk%2F3YyTBUTo5H1ZOsVxv3VUBoTV1QapMsn0vVzMAMUAe3Him2E9KG0bo2iQHlruREJIAdrWFkHl%2Bc%2F5dySpWjL6eHEeyTs8PIAwRzt55YALmcZY9xtCHpvgzG2E%2BnpC0PHbMow5Vk8pLK4S19P3zuO5GDYoVP%2F7KTQW4wuqsFfIKMhz2S1jvX1jjJaZ%2Bgl%2BgAakMu5kEJYEf6TF1jSGjhdLFZzXRjcrlsN88iOzU6ukSZqTeCO903aFht6C17NujOs4FFdtOXQariY6Ym2nahqP536fIEwAGARBm78qRCt8biwR79CznxR42dgkMNVxrSvOV3iZTD7nfHTBjqkAbLc3%2BK6ntl7CCRpca7HfqDPuFkPtDt9IOwhrllvbXhto%2BImgPSzFxwhXszc2IMWOSvxRt4kuYnoFiniDHmapf8u14j9etWn5%2Fdp%2FizIUuc0io%2BWTdrhI4Vv2Po00gAiracb7oa8M4FPUFW%2BjXPtEaML4j2tmcMYvCMVdfje71A4oY5FasXfa1VHS3zTPwZbUvwA2nsTSE15ZeFloz7wOn%2BF6n0h&X-Amz-Signature=48641b546de85536a3a54f31bdaf30c42cebab21cf133df1587cc385598eed82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
