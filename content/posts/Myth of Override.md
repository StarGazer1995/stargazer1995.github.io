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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633FR5H77%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T195522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2G3HYVTQAj5Hn7aT9wwi%2BYJpL3D7iD2DWaW1JM9b7qAIgNLD2T9pZ2wwoxgnbc3I9K4l0khtnYCVVo%2BR3Vy4sQIUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDUkRGjXktxGiupdwyrcA4Qqt2a9D2StgnIS55zMVJ469v8YZsT3VpF4m0rCye7cvG54ODbA3lP%2BMFx%2F9%2BzNiLylmxM8ZU%2FcLubKOm%2FeOn0R63oGVg3PEEGQskzAIsY7eEbL%2Flxa3Qb11ujjv35RIeaVQbk8r6ExuR068f5TMcv1x0O8PCrEh%2F4El6%2BCklM0ehltw7QpGMEbnga8jzKg68CvUhz7zmj%2FodELM9UuoQ6yB8PdZnkTlVe%2Buazg0J2cGN7QOr00Dp98HXmHZr6syIwHTPOk5nGmae3TTckYmLbruJFNnLyLAdb8GM5hrBa%2FuV5l6n2f4LZZ070jv%2Bw%2FRJ1E01kT238YU9mqZXNubaBO2qmRQYT9osoN4T1Ld2BgBLoxKIzNNhqqLa7JF1pFGWJRHyuSz6mponV3cgKlRd6frYQliuTTx3e5fEDFu8TDMYuuYjPB1JLWP7vtcsHM6noA8ygGPmDAfPHZOUnpugjCud6epU3jjZqLhqqfRTiFc87v9YacYbJKE8xZCSu1zWR4OIlsnxJ36oZj2tgK4ClrHLwKyNa98Zh1z44eL8QR3VmrYezvbJN%2BY5xvU2rG7mKFTroUtyvv9zZ91uPFmNs92xz9QvwuxKMdIZpFUlmadNloH5n8vwZo9SAvMO%2FkwNUGOqUBL4fLzvIaRNNnPmifylC3rjiSvzVhsgf2nFznVfLpUPqbC18LvSBy0CXUhTp37xqa6upld5j8VZ2yDyjfep7V3EjN2oWNUicv8t%2BocWM07CxY530RUYh40oz%2FogOrfQ9sLVaAZ3V9glxJS8ZxiZOTkSrHKy34ZpMFrqM1E06oJzHspzAYLcwLJFD%2FOHJ%2BRg2xIHairO1ocqShAD1qHAF13Ydx1N8E&X-Amz-Signature=fd03be77de83f561f8718b94882502ad8ff9c845d1aacae4dfeaa7bc670240e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633FR5H77%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T195522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2G3HYVTQAj5Hn7aT9wwi%2BYJpL3D7iD2DWaW1JM9b7qAIgNLD2T9pZ2wwoxgnbc3I9K4l0khtnYCVVo%2BR3Vy4sQIUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDUkRGjXktxGiupdwyrcA4Qqt2a9D2StgnIS55zMVJ469v8YZsT3VpF4m0rCye7cvG54ODbA3lP%2BMFx%2F9%2BzNiLylmxM8ZU%2FcLubKOm%2FeOn0R63oGVg3PEEGQskzAIsY7eEbL%2Flxa3Qb11ujjv35RIeaVQbk8r6ExuR068f5TMcv1x0O8PCrEh%2F4El6%2BCklM0ehltw7QpGMEbnga8jzKg68CvUhz7zmj%2FodELM9UuoQ6yB8PdZnkTlVe%2Buazg0J2cGN7QOr00Dp98HXmHZr6syIwHTPOk5nGmae3TTckYmLbruJFNnLyLAdb8GM5hrBa%2FuV5l6n2f4LZZ070jv%2Bw%2FRJ1E01kT238YU9mqZXNubaBO2qmRQYT9osoN4T1Ld2BgBLoxKIzNNhqqLa7JF1pFGWJRHyuSz6mponV3cgKlRd6frYQliuTTx3e5fEDFu8TDMYuuYjPB1JLWP7vtcsHM6noA8ygGPmDAfPHZOUnpugjCud6epU3jjZqLhqqfRTiFc87v9YacYbJKE8xZCSu1zWR4OIlsnxJ36oZj2tgK4ClrHLwKyNa98Zh1z44eL8QR3VmrYezvbJN%2BY5xvU2rG7mKFTroUtyvv9zZ91uPFmNs92xz9QvwuxKMdIZpFUlmadNloH5n8vwZo9SAvMO%2FkwNUGOqUBL4fLzvIaRNNnPmifylC3rjiSvzVhsgf2nFznVfLpUPqbC18LvSBy0CXUhTp37xqa6upld5j8VZ2yDyjfep7V3EjN2oWNUicv8t%2BocWM07CxY530RUYh40oz%2FogOrfQ9sLVaAZ3V9glxJS8ZxiZOTkSrHKy34ZpMFrqM1E06oJzHspzAYLcwLJFD%2FOHJ%2BRg2xIHairO1ocqShAD1qHAF13Ydx1N8E&X-Amz-Signature=d77ccbd5358f78c1b71efcc1e9691ca4c0afab8a13b2a7eb30aa53d26f65b242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
