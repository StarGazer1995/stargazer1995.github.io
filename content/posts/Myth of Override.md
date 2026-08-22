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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRB74HGN%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T101152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1a7kkr2f8P8YU9JTa%2FGp6FWLQAbliciV01rgZ27czggIgL9Cwp32qSfcT1mCBjJZm78c%2Brna%2Bu8TQK%2F4aPeJ%2F14EqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdYWxAPNQZJbn3XNSrcA4QwGl%2FIG5D5254ZMC76RXsH2sb5NHwhg6%2BrjeBJn4VQ%2BUILxgGqS%2Bqlzyr2HV92MgfMnG97pTKzo0hT5ZIhePPf8tP4%2BvgmUS4qN%2FLuYvamz6gQv2ccsp0%2Fxb6Cal8zuNMon%2FR5gv%2FPipzCFZsEkOqPJCwRYNBNZAQiAFIVnLywo0N177MdCwM%2FGildoMpmX%2BNMF7ffkkGimlSLfbAYIW%2FzMoXkbIRkhkXoqinu%2FjF%2FHB5XrgHIDMziLPC7G2Qow90ZDgWs4ax%2B4wU%2FCoC5wlOdEqWvdTWyAO2ZsIH7gUHhqtcu%2BcrwHu1ZQpSaPL60krrXDPmfrd7hPt9eYmrtEMMZJu7XxSJXYTBEZKOlZMWo1uN9Ia3PRcOv14JeDAJtH5x6muy4n3%2BchQRVbon5KG7JuI4PXd7SjQwesiCU1N%2BihpEcmJpUrB80R5eHO2vGtXstn0U9P1Cmk%2FJY5ktSFacKJPvYEgjX2TBrDsXTXlfZt3pWtikvTdAwJNFcdynA04kjj2c46AYNCR%2BytlVKsquuhvP2JJ53t4d8tvWo7K%2FmeppcRANfFrY1eqWSxdm6hwX1%2B%2FeYzPWhTeE7mIIgnfcccXaLMEOS1S0H1GlNO0QiWDRnkSU7Jl4igkiNMLffpdQGOqUBFEgqPfNhUJbj5hPRON9ULUM2G3vH2hnHp%2BIaaFpIbAaDEtAQUw2sMb12xn2%2BlYcawvl5XzxiMhcqa7hgn8vRkskR5kyEWCY9nJNkbyD6bA%2FSTxImRrjrmO44bVRE8Knl96G5wsgpsEMCA6bGUnBmUm64gThBD4MiQMDcF7YrxVEYy8PQ1mtM9tluY78QGJ7zCU12Urr%2BVS7KLRIIoMy9sunr7e%2Fv&X-Amz-Signature=129cfb3d0733b230bf511bfe0201395156e6778f61e50aa335e736b8c367c4f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRB74HGN%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T101152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1a7kkr2f8P8YU9JTa%2FGp6FWLQAbliciV01rgZ27czggIgL9Cwp32qSfcT1mCBjJZm78c%2Brna%2Bu8TQK%2F4aPeJ%2F14EqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdYWxAPNQZJbn3XNSrcA4QwGl%2FIG5D5254ZMC76RXsH2sb5NHwhg6%2BrjeBJn4VQ%2BUILxgGqS%2Bqlzyr2HV92MgfMnG97pTKzo0hT5ZIhePPf8tP4%2BvgmUS4qN%2FLuYvamz6gQv2ccsp0%2Fxb6Cal8zuNMon%2FR5gv%2FPipzCFZsEkOqPJCwRYNBNZAQiAFIVnLywo0N177MdCwM%2FGildoMpmX%2BNMF7ffkkGimlSLfbAYIW%2FzMoXkbIRkhkXoqinu%2FjF%2FHB5XrgHIDMziLPC7G2Qow90ZDgWs4ax%2B4wU%2FCoC5wlOdEqWvdTWyAO2ZsIH7gUHhqtcu%2BcrwHu1ZQpSaPL60krrXDPmfrd7hPt9eYmrtEMMZJu7XxSJXYTBEZKOlZMWo1uN9Ia3PRcOv14JeDAJtH5x6muy4n3%2BchQRVbon5KG7JuI4PXd7SjQwesiCU1N%2BihpEcmJpUrB80R5eHO2vGtXstn0U9P1Cmk%2FJY5ktSFacKJPvYEgjX2TBrDsXTXlfZt3pWtikvTdAwJNFcdynA04kjj2c46AYNCR%2BytlVKsquuhvP2JJ53t4d8tvWo7K%2FmeppcRANfFrY1eqWSxdm6hwX1%2B%2FeYzPWhTeE7mIIgnfcccXaLMEOS1S0H1GlNO0QiWDRnkSU7Jl4igkiNMLffpdQGOqUBFEgqPfNhUJbj5hPRON9ULUM2G3vH2hnHp%2BIaaFpIbAaDEtAQUw2sMb12xn2%2BlYcawvl5XzxiMhcqa7hgn8vRkskR5kyEWCY9nJNkbyD6bA%2FSTxImRrjrmO44bVRE8Knl96G5wsgpsEMCA6bGUnBmUm64gThBD4MiQMDcF7YrxVEYy8PQ1mtM9tluY78QGJ7zCU12Urr%2BVS7KLRIIoMy9sunr7e%2Fv&X-Amz-Signature=4cebb6f431db92879142a99ada5d3b5bf2f16e992a30690a1fa20e7aa8717430&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
