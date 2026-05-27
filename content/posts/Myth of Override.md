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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRC35MFK%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T181756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkB8T2g%2FcgsAcRMQW6ts6YSnHXay%2FO1pp9HeOwth013QIgENoc1B6yG3FYYH4EcrCCQ%2F6WmoS9tq5pGBd1VTIjaeYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEO9nAVPBOy6uEa6jCrcA4qlhWu64UpqhNipmwTrO9zQoKx0bEU79lMJPU8zjGn4LImepRH2oVQx5U7dkRXjr5ij9NDL2CvmlYSHFBH0Tecz5BVatXD2Zuz74c19kJAznAM30C1l7f%2Bvx4u2oGKtQxoMiHJTR%2FN1VU6eH%2FfLSSKormELI2cMQhcdHCD0ljwgBudbd1UZBJGd32m1qYHnn6%2BRa81pMcMxjFq9yb4g1M71DRZNe4gEgVbf4R6CSbjZyzKyLGlf1ZwM2gF%2B%2Fnek2AKSfp7G8%2F7lK8JztrU%2BKlZGak8venwwga%2B8jQQ%2FQsHGxh%2B9N4c2WNcemA2mmmnJJ2EdPOy4mUW6pe%2FbRMmWco1rXNLvvwlqcVWFYT8xqxA9a%2Bt7xJ8o2sbc3EthZ05I0OkYKrWR4C%2FcmrSCk4wieF6mN0G4O1%2FmBU4b%2B2DB2dFJ3spa%2FzyWGLuSQr38HmpxYcbUAM5I%2Br4HYLEcQj81Nzmj%2FL8QjWPfSZlok01iwrrarZicizi0aWkz2bWB4KqRxv2eM9bkivh6h092I1ScmZ%2BrJ%2Fz2hi7Cl6w74ZpOkwmR%2BJivUzCk7VUrYYqBHFBoVjSGezxwIYhngc9HN%2BSbdnPm8O2kGzhkH9oh3LZImfSoc%2Bgl5acMNkzjUTLzMM3V3NAGOqUBUZZoa8Gem%2FGFjaYgOO3pMtynUVDVJvPGPWytZrkDJlrJu%2BKbeZ8KTANbqWR2m5suoblI%2Fc4BwhOTCLSDtRHe6mOSV1twcSnoVbkUNYyDPUxi6v2KiMzA7UYy%2FnwJxCbf6vtSLS3zrUdhO1fLAus6ILohjo%2Bwf%2FF9tVB%2BzaXki6bXYa98K7QDTq4g0ktT2972sffxanRhxP6M2zN4wLZYnNS1MtyQ&X-Amz-Signature=51755d5a73d25a4e3d5a9be41db2cbf36d9d0320c9ad06bba6afee7c04ce4844&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRC35MFK%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T181756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkB8T2g%2FcgsAcRMQW6ts6YSnHXay%2FO1pp9HeOwth013QIgENoc1B6yG3FYYH4EcrCCQ%2F6WmoS9tq5pGBd1VTIjaeYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEO9nAVPBOy6uEa6jCrcA4qlhWu64UpqhNipmwTrO9zQoKx0bEU79lMJPU8zjGn4LImepRH2oVQx5U7dkRXjr5ij9NDL2CvmlYSHFBH0Tecz5BVatXD2Zuz74c19kJAznAM30C1l7f%2Bvx4u2oGKtQxoMiHJTR%2FN1VU6eH%2FfLSSKormELI2cMQhcdHCD0ljwgBudbd1UZBJGd32m1qYHnn6%2BRa81pMcMxjFq9yb4g1M71DRZNe4gEgVbf4R6CSbjZyzKyLGlf1ZwM2gF%2B%2Fnek2AKSfp7G8%2F7lK8JztrU%2BKlZGak8venwwga%2B8jQQ%2FQsHGxh%2B9N4c2WNcemA2mmmnJJ2EdPOy4mUW6pe%2FbRMmWco1rXNLvvwlqcVWFYT8xqxA9a%2Bt7xJ8o2sbc3EthZ05I0OkYKrWR4C%2FcmrSCk4wieF6mN0G4O1%2FmBU4b%2B2DB2dFJ3spa%2FzyWGLuSQr38HmpxYcbUAM5I%2Br4HYLEcQj81Nzmj%2FL8QjWPfSZlok01iwrrarZicizi0aWkz2bWB4KqRxv2eM9bkivh6h092I1ScmZ%2BrJ%2Fz2hi7Cl6w74ZpOkwmR%2BJivUzCk7VUrYYqBHFBoVjSGezxwIYhngc9HN%2BSbdnPm8O2kGzhkH9oh3LZImfSoc%2Bgl5acMNkzjUTLzMM3V3NAGOqUBUZZoa8Gem%2FGFjaYgOO3pMtynUVDVJvPGPWytZrkDJlrJu%2BKbeZ8KTANbqWR2m5suoblI%2Fc4BwhOTCLSDtRHe6mOSV1twcSnoVbkUNYyDPUxi6v2KiMzA7UYy%2FnwJxCbf6vtSLS3zrUdhO1fLAus6ILohjo%2Bwf%2FF9tVB%2BzaXki6bXYa98K7QDTq4g0ktT2972sffxanRhxP6M2zN4wLZYnNS1MtyQ&X-Amz-Signature=068486ac46af92a12dd38aaf31404128eea437886208ac78643e656143c3c6c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
