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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDPO7DCX%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T160707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBB8UD6vRglH1zk1qREKq5kaG6CsdCIlsm2aGYXQDF%2FoAiEAod1cxV5SuRV4qH9zScyMEgW4WXl1jnrdy5cm5623qswq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMQQuMlIF2T34BFZeircA6iQVC6nixcvSYIUzZg4ohN0Uq5cV6bApXVpY28zgqiZlOY05PgJ0uCXASZLCrYHgD80Y%2Bq6NYY77%2BMay%2Fq%2Fgiex6R5trgC9%2Fzp7SPD3RBMSqIWkNWUzZKaJ1N7ogFy1%2BuJY7tF%2B%2BpFzYcu1B2Rd2X%2B1kCLGvB3DloYfxdpUnI9QMePDLHWo%2BMP6L8CYNnTKe3rByzrTZAEOYQOvMV7cC7QE%2FaI5ELvpsNGasqOAJvn3IzjhOx%2FeGt27M4jNA%2BLq43RSBGDluCuTCKJ4dU72tcXkbvldkadUVnvmw%2Fjg6YWtVwpB3DltKW%2B%2BBNfsqC20EV3D%2FP0XJUWDzPZebAXPmkQp5DspYvdKztwFt%2B3ghTE%2FsHxznu%2BfuI1aHnkgRzvHvygBbJJGn6hmy0POWqtHmjcKJPyyZzLCp%2BScVcur2GwoAasKL4Vxe9SQPGWnCFiaM1lNR66DYEdSJE%2BP5cuFAYMFXCik2BAKxFGhrodUb7VB0TEBlGHEVbCTVpe2gQyMROECozcf6KE5k2rGCHLsKyKq78LEgjMKJdXYFpWUoKO3A%2F6YENpAv8dPo8ftfSLNRb9amx2Di1fuJW77tydnZaHcXijDCkz2DO8QDxP6udrAwlWvvcRtqWYa5EJKMJiCntMGOqUBzNZKR0XyyC1dbUQbidaFbisj75XiS8xS4q7Vfs1DKmJa91HxPab9mDISDbLvQz%2BZGoV4IqsCylVtCMDQxA%2BWtUL0wUKbcVUlLqm3UnOKzd8nhMozDv4uifwW0lNWPPWpPxLlI%2F9wAjJyt1VrdSVD9OMwZEj65NFdy8obiCMRnnoIj4C4XfRDR0jxeTE%2Fsg0J0tI8wWD4%2BzKRktUGviiQt7M%2FPS40&X-Amz-Signature=8948740fbea89fc78b5950e6cc85dce19dde9ae777166df04cf00ab3315dd5a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDPO7DCX%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T160707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBB8UD6vRglH1zk1qREKq5kaG6CsdCIlsm2aGYXQDF%2FoAiEAod1cxV5SuRV4qH9zScyMEgW4WXl1jnrdy5cm5623qswq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMQQuMlIF2T34BFZeircA6iQVC6nixcvSYIUzZg4ohN0Uq5cV6bApXVpY28zgqiZlOY05PgJ0uCXASZLCrYHgD80Y%2Bq6NYY77%2BMay%2Fq%2Fgiex6R5trgC9%2Fzp7SPD3RBMSqIWkNWUzZKaJ1N7ogFy1%2BuJY7tF%2B%2BpFzYcu1B2Rd2X%2B1kCLGvB3DloYfxdpUnI9QMePDLHWo%2BMP6L8CYNnTKe3rByzrTZAEOYQOvMV7cC7QE%2FaI5ELvpsNGasqOAJvn3IzjhOx%2FeGt27M4jNA%2BLq43RSBGDluCuTCKJ4dU72tcXkbvldkadUVnvmw%2Fjg6YWtVwpB3DltKW%2B%2BBNfsqC20EV3D%2FP0XJUWDzPZebAXPmkQp5DspYvdKztwFt%2B3ghTE%2FsHxznu%2BfuI1aHnkgRzvHvygBbJJGn6hmy0POWqtHmjcKJPyyZzLCp%2BScVcur2GwoAasKL4Vxe9SQPGWnCFiaM1lNR66DYEdSJE%2BP5cuFAYMFXCik2BAKxFGhrodUb7VB0TEBlGHEVbCTVpe2gQyMROECozcf6KE5k2rGCHLsKyKq78LEgjMKJdXYFpWUoKO3A%2F6YENpAv8dPo8ftfSLNRb9amx2Di1fuJW77tydnZaHcXijDCkz2DO8QDxP6udrAwlWvvcRtqWYa5EJKMJiCntMGOqUBzNZKR0XyyC1dbUQbidaFbisj75XiS8xS4q7Vfs1DKmJa91HxPab9mDISDbLvQz%2BZGoV4IqsCylVtCMDQxA%2BWtUL0wUKbcVUlLqm3UnOKzd8nhMozDv4uifwW0lNWPPWpPxLlI%2F9wAjJyt1VrdSVD9OMwZEj65NFdy8obiCMRnnoIj4C4XfRDR0jxeTE%2Fsg0J0tI8wWD4%2BzKRktUGviiQt7M%2FPS40&X-Amz-Signature=70ac636b8ea9136db254757b45b63e43dca37ec6e07b3dde94ec14e9197b5ead&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
