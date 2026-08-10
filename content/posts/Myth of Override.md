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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XWM3XL6%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T090543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmH1vqeiWSJGiZAiJa59Vvl32skoeBNrBVJ8%2FnWNxZaAiEAgK6wS4%2BEIRse3GOuUUDRbhENCc8OGFycIQV4snnG%2BtUqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBs6H5KSYA%2BDvXwvOircA%2FEoUfFib3VKwqzZLvryq5Y2gPgLNw3Q4KOcldEavBt2qSB8aoYCwU9IjvwIVqztLnVnco%2BTi777UUxejCM5EKzwK5r841ZlcU2%2BSHj8%2BV1wxD%2FuZod%2B%2BgtRW4CUXGuXmToBpyNkC8jjjBGPRkpXKcj0rYMOB3EY%2BCCfY%2F3CTehlRYPna1%2Bl5JF9QRQ2VVh0yEgiR4s4sEJ0HMlOKpI0k9jNOCQrF4D5X8jd%2BMom6K8reKZh%2B8OWtyq4XRIxc4LYP9Ez7X9kPV%2BuQ5DkccKAcoJHQDiL%2BOLrnoBUvTAUd1aBkDbRMsOQiG%2Bd%2BTGwAzgl8VWMnO4Ckrc6LUkrPspotMmd%2BnFTijPyfnsTZWqEo9AAVCyB4mVifSqFi0sIxp5hDCFvDOnC1%2FGUADBRowBB%2FwNIm%2BgsqQSqnxogyl5FY%2FZsxAaMbpuAmTsw6S6%2F%2FMRe6349vuyZg8xSxaRFXj3Fx%2FR8b30Snu7gEduyDUOgV%2Ba9jQT2W62vDEPqvNFACw%2Bx1v4YqWWar4n5IFvxw9Q%2BMddheEIQ75zQHHc3NDJxZpUIkSkVM3EwHc26C5RaZ6UXbJT187%2BDKiuwnkMRvYtt0%2FqEan%2FUf8GJtNxOlvoRaeOeFRfX0Up%2F9BrNg3p%2BMN6C5tMGOqUBrNSlzdXbZxwtQgCsZ6cpGckWBMSnUXo8w%2FZFUBIS%2FdKQrzTPct%2FicgdhpAJIM5qr1jVz4omgKhflhyDAI4Qu2jfB9uA3r74r80NoHqVWb9muy4uuATDw3JairndL3T3u1BdizOJVdF3Tc%2FB7CBlz4Tlvd%2BA7%2Fg4xEdJX3Om3rz9vmKxUuIMrQh0lzGDXx7Gql%2BUIWTk5PUvo5%2FZhotzyRvufyRpF&X-Amz-Signature=f2ef80b98717be8f231888783c084932312a392dfe60e5933e5c67cb8e81819d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XWM3XL6%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T090543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmH1vqeiWSJGiZAiJa59Vvl32skoeBNrBVJ8%2FnWNxZaAiEAgK6wS4%2BEIRse3GOuUUDRbhENCc8OGFycIQV4snnG%2BtUqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBs6H5KSYA%2BDvXwvOircA%2FEoUfFib3VKwqzZLvryq5Y2gPgLNw3Q4KOcldEavBt2qSB8aoYCwU9IjvwIVqztLnVnco%2BTi777UUxejCM5EKzwK5r841ZlcU2%2BSHj8%2BV1wxD%2FuZod%2B%2BgtRW4CUXGuXmToBpyNkC8jjjBGPRkpXKcj0rYMOB3EY%2BCCfY%2F3CTehlRYPna1%2Bl5JF9QRQ2VVh0yEgiR4s4sEJ0HMlOKpI0k9jNOCQrF4D5X8jd%2BMom6K8reKZh%2B8OWtyq4XRIxc4LYP9Ez7X9kPV%2BuQ5DkccKAcoJHQDiL%2BOLrnoBUvTAUd1aBkDbRMsOQiG%2Bd%2BTGwAzgl8VWMnO4Ckrc6LUkrPspotMmd%2BnFTijPyfnsTZWqEo9AAVCyB4mVifSqFi0sIxp5hDCFvDOnC1%2FGUADBRowBB%2FwNIm%2BgsqQSqnxogyl5FY%2FZsxAaMbpuAmTsw6S6%2F%2FMRe6349vuyZg8xSxaRFXj3Fx%2FR8b30Snu7gEduyDUOgV%2Ba9jQT2W62vDEPqvNFACw%2Bx1v4YqWWar4n5IFvxw9Q%2BMddheEIQ75zQHHc3NDJxZpUIkSkVM3EwHc26C5RaZ6UXbJT187%2BDKiuwnkMRvYtt0%2FqEan%2FUf8GJtNxOlvoRaeOeFRfX0Up%2F9BrNg3p%2BMN6C5tMGOqUBrNSlzdXbZxwtQgCsZ6cpGckWBMSnUXo8w%2FZFUBIS%2FdKQrzTPct%2FicgdhpAJIM5qr1jVz4omgKhflhyDAI4Qu2jfB9uA3r74r80NoHqVWb9muy4uuATDw3JairndL3T3u1BdizOJVdF3Tc%2FB7CBlz4Tlvd%2BA7%2Fg4xEdJX3Om3rz9vmKxUuIMrQh0lzGDXx7Gql%2BUIWTk5PUvo5%2FZhotzyRvufyRpF&X-Amz-Signature=1f3c4db1d5c4dc6c190d3ba4e3ed8e0fe6bf5f0f825902cc5058e103cd148ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
