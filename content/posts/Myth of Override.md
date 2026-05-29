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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7MDLB5G%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T230326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIHIF81kjY0cpedOprXCvhuwjmBe8xDnLirdMueFBdkFpAiAHPDPZJLmxOxgXedcIVFwpJNAGZ9clfZaAvladVOY7iSqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMzqPbWB%2BV%2BAs7N85KtwDIyvliZMY0GpQrtb%2BkAvAwtcC0KR16ERVDt%2Fb8cRIA8pN0tHLFUy6pHbGNpfrNvlGVDaKERdcVuLNW7QpdssJ%2FUkJX6p50rfOzAr%2BV%2BsVLdzizHpjyoZrM9RRdmHwtn5%2BbwduuQeW2mCPRrlabeUY3OabLxbb7s1PrwFx%2BjEH8vxoaW5MyBd1wGDraKOxw9lE%2B3KSrVdhhc%2FmJCTsX82GbMMFRDAeN7r88tiuX%2FlN1UBX2hcIra1yCvWdLlsVBTsya2aUzv93aCdvDIoIT69ooQgLdMdM%2FU9fjdm35G5xR%2F%2FmvqD1atmZpOI4fWxiprC5Jvqa6Ty6Oejsd0RuXwIyVmfs1EG3lQObsA8VxMsyMtsOw6gL09IuvSsBJqP43LHwMWN0QaXaa0GaBn0%2F5%2Bh1sGlVVAebBZ9XUtHAR4ESRELcDnzYuK5JIELXk3JLh%2BO182AivyskzNQSqTqRteTf9BS507GVtowMN2PkldAMqBwP8jegHF1ydBYZTovCl%2F5h9EA09FaopzIUGNMINUVQL9NqCYvDfDlcIXTlLZTTTw2pgntEVi9k%2FC9NT7rQyvJW3tgjeSrV%2BOK36xrslp%2B74gnrk%2BRtZ%2BkN03fIn1NHd1hqcviaJPvUoFfMW5Mw15zo0AY6pgFH%2F8zfjPN8KKTea5bEdSuLlpXDC2MT121cOr7JpkS7kDmPXAjk8wMhYe0pfSciYxKgumWPYBgWsMJJS7bSF0kv2ZxJS80%2BwyYx%2FRAdW7V4HWVzb1BslZSpDrjjeN9hAZ8JhjMqXxWP7AVJ9lgEjw76y1f5mNBzZT3NsYh4%2Fsmj%2F5IM7u%2B%2F5WqB6qfn6KNxLFxQ1ws6qaQLmjZKa2U7jzNGX%2B4GSQKt&X-Amz-Signature=8af065ab4716429a1693fd4dab4260b56e9f70ecda7bf8342f3e26418d6a3788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7MDLB5G%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T230326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIHIF81kjY0cpedOprXCvhuwjmBe8xDnLirdMueFBdkFpAiAHPDPZJLmxOxgXedcIVFwpJNAGZ9clfZaAvladVOY7iSqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMzqPbWB%2BV%2BAs7N85KtwDIyvliZMY0GpQrtb%2BkAvAwtcC0KR16ERVDt%2Fb8cRIA8pN0tHLFUy6pHbGNpfrNvlGVDaKERdcVuLNW7QpdssJ%2FUkJX6p50rfOzAr%2BV%2BsVLdzizHpjyoZrM9RRdmHwtn5%2BbwduuQeW2mCPRrlabeUY3OabLxbb7s1PrwFx%2BjEH8vxoaW5MyBd1wGDraKOxw9lE%2B3KSrVdhhc%2FmJCTsX82GbMMFRDAeN7r88tiuX%2FlN1UBX2hcIra1yCvWdLlsVBTsya2aUzv93aCdvDIoIT69ooQgLdMdM%2FU9fjdm35G5xR%2F%2FmvqD1atmZpOI4fWxiprC5Jvqa6Ty6Oejsd0RuXwIyVmfs1EG3lQObsA8VxMsyMtsOw6gL09IuvSsBJqP43LHwMWN0QaXaa0GaBn0%2F5%2Bh1sGlVVAebBZ9XUtHAR4ESRELcDnzYuK5JIELXk3JLh%2BO182AivyskzNQSqTqRteTf9BS507GVtowMN2PkldAMqBwP8jegHF1ydBYZTovCl%2F5h9EA09FaopzIUGNMINUVQL9NqCYvDfDlcIXTlLZTTTw2pgntEVi9k%2FC9NT7rQyvJW3tgjeSrV%2BOK36xrslp%2B74gnrk%2BRtZ%2BkN03fIn1NHd1hqcviaJPvUoFfMW5Mw15zo0AY6pgFH%2F8zfjPN8KKTea5bEdSuLlpXDC2MT121cOr7JpkS7kDmPXAjk8wMhYe0pfSciYxKgumWPYBgWsMJJS7bSF0kv2ZxJS80%2BwyYx%2FRAdW7V4HWVzb1BslZSpDrjjeN9hAZ8JhjMqXxWP7AVJ9lgEjw76y1f5mNBzZT3NsYh4%2Fsmj%2F5IM7u%2B%2F5WqB6qfn6KNxLFxQ1ws6qaQLmjZKa2U7jzNGX%2B4GSQKt&X-Amz-Signature=b1f798a9a4e6b06599235d0344882cfa27211b944113efab27785561ea46ec0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
