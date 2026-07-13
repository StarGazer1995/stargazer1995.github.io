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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H52QELP%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T084338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQDuB0%2BPXFHVMlMAetaHUxap%2FjvlMoHbfkhXXJe0rhCKXgIgM6LFzmIGsxuwNEK60cha4iXoR%2FvsJhagmMgklWGvlDoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNEmttRGnhs0PcaYqircA2QC2ugQVao7hIbHgs88bwdJ4uGsDTUHgMX%2Bjmw2w1ls7%2FJuEBm54pxWYGON808RizW9c3Pgsal9rVApk3gtDnER2qaVknjgN%2F3%2FBVct3i2Kj7%2BSZvQUZ9jhQmxtT%2BKEdAuqTKkQxyWEg1zHP25jHssOFUkOUuF84abvUonwPKSQJb6dBlVbzHAAGIlcBc71BKLW8HJobIrfGykfm3Uukh%2FXvpQHNr3PKDs7D5g8NSVC5OK92mUtvqFARfruHvyEA8kDSVxaMvy0WHIdSTXWvT0TTVwmpZEQhzJg7q80JrV%2FQYK0itDwOoR6cWOjlbw%2Ff2Nin2nsOeHMux%2FcURzTH3OhsTf7TTke9DIP6edyWqbVTswgnuPtDZvPr2m7CGvgbS%2FUJhL05TmTIWhDwpO6YH69nvjXS%2B0v%2BCOU93B%2BisMekMuUZ8STrA%2FpDAVZDH9vfd2Jsm8KZbEdJfUiFd3MOoeUpJofdDqXVLU5A7j%2B%2BdK1ABT5p%2BIU3hBAIu2QViOT%2FsGsYRoAqxKEALivy59XlUaKV%2B%2F44GOyd0ztBTrlif0rkmiAi1Sdw3haRobgqYeWYDGCmGidL%2Bjuxx2GHE1uGxcerXSS7%2Fpq3XgUxRfBSX3UVIVT0VgnwLBWZAXIMIOc0tIGOqUBNIP0N%2F89C74WxwS08AhxFzmKhM5rjUkBEkNDzTMlvQPexu2inB1pFmCWSskUapvKB7sc4yU8g%2B0%2BFV8sVbFX8Poa0WWAlLYSfwQoDRT2J5nrx5auRack6e%2BRferVzQoU2npByfACaLB0tbOTEecNvRh4ZgdSrHOcVdMoTczfoZxtcmX2z2OC35zhnDBR0vzWB1sApTAnsG4bUDjLpafPEffOM4uZ&X-Amz-Signature=26046d9ec2d9095f195e98235c22323c73ad27ea74884654b3a8112243ad9e91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H52QELP%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T084338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQDuB0%2BPXFHVMlMAetaHUxap%2FjvlMoHbfkhXXJe0rhCKXgIgM6LFzmIGsxuwNEK60cha4iXoR%2FvsJhagmMgklWGvlDoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNEmttRGnhs0PcaYqircA2QC2ugQVao7hIbHgs88bwdJ4uGsDTUHgMX%2Bjmw2w1ls7%2FJuEBm54pxWYGON808RizW9c3Pgsal9rVApk3gtDnER2qaVknjgN%2F3%2FBVct3i2Kj7%2BSZvQUZ9jhQmxtT%2BKEdAuqTKkQxyWEg1zHP25jHssOFUkOUuF84abvUonwPKSQJb6dBlVbzHAAGIlcBc71BKLW8HJobIrfGykfm3Uukh%2FXvpQHNr3PKDs7D5g8NSVC5OK92mUtvqFARfruHvyEA8kDSVxaMvy0WHIdSTXWvT0TTVwmpZEQhzJg7q80JrV%2FQYK0itDwOoR6cWOjlbw%2Ff2Nin2nsOeHMux%2FcURzTH3OhsTf7TTke9DIP6edyWqbVTswgnuPtDZvPr2m7CGvgbS%2FUJhL05TmTIWhDwpO6YH69nvjXS%2B0v%2BCOU93B%2BisMekMuUZ8STrA%2FpDAVZDH9vfd2Jsm8KZbEdJfUiFd3MOoeUpJofdDqXVLU5A7j%2B%2BdK1ABT5p%2BIU3hBAIu2QViOT%2FsGsYRoAqxKEALivy59XlUaKV%2B%2F44GOyd0ztBTrlif0rkmiAi1Sdw3haRobgqYeWYDGCmGidL%2Bjuxx2GHE1uGxcerXSS7%2Fpq3XgUxRfBSX3UVIVT0VgnwLBWZAXIMIOc0tIGOqUBNIP0N%2F89C74WxwS08AhxFzmKhM5rjUkBEkNDzTMlvQPexu2inB1pFmCWSskUapvKB7sc4yU8g%2B0%2BFV8sVbFX8Poa0WWAlLYSfwQoDRT2J5nrx5auRack6e%2BRferVzQoU2npByfACaLB0tbOTEecNvRh4ZgdSrHOcVdMoTczfoZxtcmX2z2OC35zhnDBR0vzWB1sApTAnsG4bUDjLpafPEffOM4uZ&X-Amz-Signature=c4e09396e0eed205b02e9031bf8d0287af093181fd81aa055f09a195bc110242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
