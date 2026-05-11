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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGF6HKLC%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T015524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCIEf0CtEcPncSuHMf7%2BKyXPPWGbRopVA%2Bn2v6%2BUyTEcSkAiAx990GhVEsjT4hRmmYGF%2BqZS0uUBj6HSVNEQFR6Zm0cSr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIM%2Fsab0H%2B0xFH%2Fd0EMKtwDo%2FQfu3AHY%2FjKJ80u97JjZditNaKOIaZTlrJ1WPgQoT%2FzbfD6hIDTfFsPNaYu%2BAIUMnDGBA7PFI7ReixsXGZ4BsPqleXrFgfxENs2eOyi7LxtVPkB6W8jmugYpFBahdQfnDDp57o6aJWrwi1DeyxYkeT4uVp8x84MIrlO%2FbTmVLrxvm7aa1qd5V5YE6fdzVxxHkgb6PBwGcYnfQitfpiXhMJZAQP8jmwJ0pRLKjB2e2UIbADB9hAWqEHZJpaLI1SbsInIquNjwRMWq3DrJyyLv1lDCtAGpvwA%2BAEW17RQN5aLT54Pa0IRgOobHx35uE3IonWZBX68S5oWFYynF89FrvV81PsNyMq3d4mzYWjSs5i9kjKnX6YFTY5UbbkIDUioOnxypFpxYsoQ62jzQwQQei50zH3%2FVO3p52FxNZAnLmPd%2FyfDQmk6gTAIMkttQArkYmWa25KwuDsxkHI28IJPrS%2FANaKk4xI7%2BwiSufpYKkjuEVd%2BI08Wa3T%2F1Eb5tQ0diZoAdKI%2BVt0vaQmMaNj4n0eLDAuAWV69VpB%2Bq67TyRhovv3aYYviJGHNczxyuuSRGAWMF6AhfM4czy3emlfNgqk%2BNfnaNsCBDdO2BMRCBeVqUFGaig%2B6%2B%2BdUAHIwm%2BKE0AY6pgG4zo4lO5oE9g7rsSO5SPYDjHaprHk0BTaFSlF%2ByU%2Bg5VnP%2FkLVAbvYrVKn4DPFZFY6KfCc7CIvpQXRmR4QcCDjzGlcaRCMF4LHDda%2FtBhFPhrMIEndIc0cp%2BXdZjTHJAY%2BZcgRvXoas7ecvPFToyylDRjOi1YCLf43ij3ONSG39l%2FQld%2Bgsv%2BFhikmjIZ6EgSv4tpHd%2Bvon823%2FXXF01JxkuO2xORh&X-Amz-Signature=d29e3ba27f827323e215e248a950a89a7f5320ba19d1a2dd48773376683fb96d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGF6HKLC%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T015524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCIEf0CtEcPncSuHMf7%2BKyXPPWGbRopVA%2Bn2v6%2BUyTEcSkAiAx990GhVEsjT4hRmmYGF%2BqZS0uUBj6HSVNEQFR6Zm0cSr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIM%2Fsab0H%2B0xFH%2Fd0EMKtwDo%2FQfu3AHY%2FjKJ80u97JjZditNaKOIaZTlrJ1WPgQoT%2FzbfD6hIDTfFsPNaYu%2BAIUMnDGBA7PFI7ReixsXGZ4BsPqleXrFgfxENs2eOyi7LxtVPkB6W8jmugYpFBahdQfnDDp57o6aJWrwi1DeyxYkeT4uVp8x84MIrlO%2FbTmVLrxvm7aa1qd5V5YE6fdzVxxHkgb6PBwGcYnfQitfpiXhMJZAQP8jmwJ0pRLKjB2e2UIbADB9hAWqEHZJpaLI1SbsInIquNjwRMWq3DrJyyLv1lDCtAGpvwA%2BAEW17RQN5aLT54Pa0IRgOobHx35uE3IonWZBX68S5oWFYynF89FrvV81PsNyMq3d4mzYWjSs5i9kjKnX6YFTY5UbbkIDUioOnxypFpxYsoQ62jzQwQQei50zH3%2FVO3p52FxNZAnLmPd%2FyfDQmk6gTAIMkttQArkYmWa25KwuDsxkHI28IJPrS%2FANaKk4xI7%2BwiSufpYKkjuEVd%2BI08Wa3T%2F1Eb5tQ0diZoAdKI%2BVt0vaQmMaNj4n0eLDAuAWV69VpB%2Bq67TyRhovv3aYYviJGHNczxyuuSRGAWMF6AhfM4czy3emlfNgqk%2BNfnaNsCBDdO2BMRCBeVqUFGaig%2B6%2B%2BdUAHIwm%2BKE0AY6pgG4zo4lO5oE9g7rsSO5SPYDjHaprHk0BTaFSlF%2ByU%2Bg5VnP%2FkLVAbvYrVKn4DPFZFY6KfCc7CIvpQXRmR4QcCDjzGlcaRCMF4LHDda%2FtBhFPhrMIEndIc0cp%2BXdZjTHJAY%2BZcgRvXoas7ecvPFToyylDRjOi1YCLf43ij3ONSG39l%2FQld%2Bgsv%2BFhikmjIZ6EgSv4tpHd%2Bvon823%2FXXF01JxkuO2xORh&X-Amz-Signature=adbf0caa0220e29e2cd6ff9cc28e741b602f0b10f8c21b3e238779efec00af3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
