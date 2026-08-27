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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466226EWUVM%2F20260827%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260827T052559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIEYw99j6NTK%2FDBAHxnY3sNHwRVCBVIZu4bX8gvnsQuX4AiEAlLjdKmUNPdZ28wGH%2BNsp1QR96xULuRWmHfSdoGRFBSwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDAFk0EzgrgOvFi4lQircA9XaslQVfO4rx0f0NJPcyVutHgteyaCOLZ6%2BD1tCm1yQpU6dmjxk9Sn%2BAsVUHh4y5c5Lo%2FL0Lf%2F2lXizYD7o94GxkFyHpVAR3X4PQig4nAIsnIRPUP1gr0YPwjkbvVQzfdX0VfaVqm7yaCEfYqErkOkKgZhJFxMG8O82VmCIRb0fzG26hxv%2FrX6VJvf%2BdzaVADkwYRrIVoqXI%2FGqcUayT0vWJK%2FyfE5adXOHY6apiCdGlbeTaC%2BrVeHNvcfexp5lkVnylGbpM7BcFjL7%2F0n05WJiCbZGS5GLJ%2BXd9lpQY0Jy%2BQivs2iB5k%2B9rKhtjux7aoPeNiADcNwC6rVNUZdfbN8GgHz3Vx5bu48O3etI5reTtqNz8OEyh%2FeqkasOucOMiAhtrWdRZ7Vh4jYFiFscDLQv6flsKnp4iFPhl88HpqFm5fMygGh%2FkH42pR1wQ33qek7F4o6LQ0Gd8LrsNWimzunJnz%2FScLBDV6nOD%2BfuhmLLmxNjGj2FsUA%2FHsEVnFUlV0xngs7rnE3WgNqiUaFH%2BTacvRXpteMCXpn4ZvUAH%2F1rVWVgiL0jZaV7EnM1hdQpSFzwbHC0SFWjWdE6nC5sHPQmuVtZUDOGNy5bdDv6p3YAudX4iFB23zFt3g%2BRMJuDv9QGOqUB9e8Ib6V1xED%2Fg8eNK%2Bsofd%2F9g5eyBm5ZfqYXURQhoIfAZCCecoZ0a4y3AKVlt2TWqWri4D9pFvdo%2BGOTMWHKx5az0FU3jwveVnwTT5Oc%2FqeQZe67LKM9d2x0PGwkS9C1Jk3ieCELflag0eQv0F0CUVNvFMRHdmjo1lf7JX7lz2usEQAv0N5unzZLvrcrHitBvaGWqjyX1YBfCiY5CGEfrAB34hiA&X-Amz-Signature=dd19888ef4f99b60f959fbcc2eb89d2874f68e5145f50266316bf0a4d3958411&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466226EWUVM%2F20260827%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260827T052559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIEYw99j6NTK%2FDBAHxnY3sNHwRVCBVIZu4bX8gvnsQuX4AiEAlLjdKmUNPdZ28wGH%2BNsp1QR96xULuRWmHfSdoGRFBSwq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDAFk0EzgrgOvFi4lQircA9XaslQVfO4rx0f0NJPcyVutHgteyaCOLZ6%2BD1tCm1yQpU6dmjxk9Sn%2BAsVUHh4y5c5Lo%2FL0Lf%2F2lXizYD7o94GxkFyHpVAR3X4PQig4nAIsnIRPUP1gr0YPwjkbvVQzfdX0VfaVqm7yaCEfYqErkOkKgZhJFxMG8O82VmCIRb0fzG26hxv%2FrX6VJvf%2BdzaVADkwYRrIVoqXI%2FGqcUayT0vWJK%2FyfE5adXOHY6apiCdGlbeTaC%2BrVeHNvcfexp5lkVnylGbpM7BcFjL7%2F0n05WJiCbZGS5GLJ%2BXd9lpQY0Jy%2BQivs2iB5k%2B9rKhtjux7aoPeNiADcNwC6rVNUZdfbN8GgHz3Vx5bu48O3etI5reTtqNz8OEyh%2FeqkasOucOMiAhtrWdRZ7Vh4jYFiFscDLQv6flsKnp4iFPhl88HpqFm5fMygGh%2FkH42pR1wQ33qek7F4o6LQ0Gd8LrsNWimzunJnz%2FScLBDV6nOD%2BfuhmLLmxNjGj2FsUA%2FHsEVnFUlV0xngs7rnE3WgNqiUaFH%2BTacvRXpteMCXpn4ZvUAH%2F1rVWVgiL0jZaV7EnM1hdQpSFzwbHC0SFWjWdE6nC5sHPQmuVtZUDOGNy5bdDv6p3YAudX4iFB23zFt3g%2BRMJuDv9QGOqUB9e8Ib6V1xED%2Fg8eNK%2Bsofd%2F9g5eyBm5ZfqYXURQhoIfAZCCecoZ0a4y3AKVlt2TWqWri4D9pFvdo%2BGOTMWHKx5az0FU3jwveVnwTT5Oc%2FqeQZe67LKM9d2x0PGwkS9C1Jk3ieCELflag0eQv0F0CUVNvFMRHdmjo1lf7JX7lz2usEQAv0N5unzZLvrcrHitBvaGWqjyX1YBfCiY5CGEfrAB34hiA&X-Amz-Signature=20282efbac31b51edef644d1070be63f83884331662a18340a456ca3066bb2dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
