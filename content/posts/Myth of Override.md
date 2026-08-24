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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G2JKPWS%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T063332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIEbvzNkDzouZX1GlH7Q8at04g27LzSxkO66Y%2BqjLtx0sAiBOBV6Y%2BxcFK1VM%2FKXdjnG9oNsiCTcAmNAQ7zB2RRSYxSqIBAjm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML92Uy7CAvtliW1VoKtwDS4EyE9Go%2FzSAU7ETnOrIQ60B4nPmvsrVvu4OThI3fFKkbUmy4ZFgycwFk%2FlodDP9UK32R2je7Zaw7ZF5mD0w6enbSSHXlJb7qY%2BabJqct30HueByeWFn8I8eyfWC8VwFHGDnGXN%2Fu%2BwMWMa83VmBxqPJ6L1mAA4A2j9vgtUVAIoTmyE9LGJjccrwj466%2FPa9%2FMuDA7A3MyX1u%2FuIn0U9ymC5LMvFbI%2Bx6Kcd%2By80GEpy7LptkhB8GTVpbhJWMB4fUum%2BtAUcMa7T8%2FBCk6OkWN64aOfcm2VeDx88y8Cu8PTExyMTTVB7n9v2Uwaa6mbdOPm%2F%2Bb8K1JQOeLw20jpCDi6W1jxzDj5Oi5F83SinLyCzavrju8pf1yRr34ThzT4hZ9cY7PISKhOz8q3MZCj0KRi1PdHhlesc8l29y0WbIHesCOpUdlMXcCnqE4XHfEp7x%2BlmwxCs%2FWPUYyEp%2BJbqvAuvhfW0hv2i5GFLXuMAz0T2JQQyiWfe5xha6ScNhVYWGDxUJu8FmWggkgCK%2Ff2o2%2B26A2qDbIlJpVCxyHS46tMk6JiQl91CuzzQMZcSfAsmjqcjCJ6U0vRMeqj2N%2BYXU5Iiw1A5B47iFZ58QxcoCajfEWfvpW3ONySzdaEw7KGv1AY6pgH3JtEwVAjIyw0%2F0GNyQdjzmPHtbWHB8Vud%2Fxo8jYpyC0p%2BEtVAgyVFjNRrOzDrTuqnb%2B%2BPQxhSfTl%2BgjNS5p%2BesWRQFSJEppiSNbW1yA6Fg4pPsV3P9CS47Nz2VhRNUTW7%2FYR506KZM7j7Rm0GWSiQGGkmupMNMogZTZQ1iLRH%2F5YH80btIVHatNg3Kaq8v2GawjQcXDBuRgNHqtNilfT26mQZ16YA&X-Amz-Signature=e9253893f3aaa4aeb600fc0e641fdb06d7909e9ac75aa8384befef52ddd1d11f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G2JKPWS%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T063332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIEbvzNkDzouZX1GlH7Q8at04g27LzSxkO66Y%2BqjLtx0sAiBOBV6Y%2BxcFK1VM%2FKXdjnG9oNsiCTcAmNAQ7zB2RRSYxSqIBAjm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML92Uy7CAvtliW1VoKtwDS4EyE9Go%2FzSAU7ETnOrIQ60B4nPmvsrVvu4OThI3fFKkbUmy4ZFgycwFk%2FlodDP9UK32R2je7Zaw7ZF5mD0w6enbSSHXlJb7qY%2BabJqct30HueByeWFn8I8eyfWC8VwFHGDnGXN%2Fu%2BwMWMa83VmBxqPJ6L1mAA4A2j9vgtUVAIoTmyE9LGJjccrwj466%2FPa9%2FMuDA7A3MyX1u%2FuIn0U9ymC5LMvFbI%2Bx6Kcd%2By80GEpy7LptkhB8GTVpbhJWMB4fUum%2BtAUcMa7T8%2FBCk6OkWN64aOfcm2VeDx88y8Cu8PTExyMTTVB7n9v2Uwaa6mbdOPm%2F%2Bb8K1JQOeLw20jpCDi6W1jxzDj5Oi5F83SinLyCzavrju8pf1yRr34ThzT4hZ9cY7PISKhOz8q3MZCj0KRi1PdHhlesc8l29y0WbIHesCOpUdlMXcCnqE4XHfEp7x%2BlmwxCs%2FWPUYyEp%2BJbqvAuvhfW0hv2i5GFLXuMAz0T2JQQyiWfe5xha6ScNhVYWGDxUJu8FmWggkgCK%2Ff2o2%2B26A2qDbIlJpVCxyHS46tMk6JiQl91CuzzQMZcSfAsmjqcjCJ6U0vRMeqj2N%2BYXU5Iiw1A5B47iFZ58QxcoCajfEWfvpW3ONySzdaEw7KGv1AY6pgH3JtEwVAjIyw0%2F0GNyQdjzmPHtbWHB8Vud%2Fxo8jYpyC0p%2BEtVAgyVFjNRrOzDrTuqnb%2B%2BPQxhSfTl%2BgjNS5p%2BesWRQFSJEppiSNbW1yA6Fg4pPsV3P9CS47Nz2VhRNUTW7%2FYR506KZM7j7Rm0GWSiQGGkmupMNMogZTZQ1iLRH%2F5YH80btIVHatNg3Kaq8v2GawjQcXDBuRgNHqtNilfT26mQZ16YA&X-Amz-Signature=d23643e37b06ea28870b1842b76111819f5e6fb6cd11d72ec0dcf8a98380c344&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
