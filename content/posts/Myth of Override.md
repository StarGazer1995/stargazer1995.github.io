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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WRT53QM%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T080724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCICY1ft3orXd%2Fc9REJc0KgYiHGy40KHGYOXdVVBtPXGVLAiB4cBfTi08VRuXS4eyboLBsxyT8QVA2ornWtCtr%2F2tIwSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz7BQcN22BR%2FcXbEUKtwDyMRkb%2FT3TlK6knk5dlkgwE2mmKascfCDDROsOTB4dTRCjkHO6KFPblGzthui%2Bv%2FQl5SM4H%2FIcGiNZwZYFWVoZrpJNjhTLFlYRJEgNSYo9hsav%2FP%2FXN%2B%2FqPCXhWuH5kjENwYwxhg1UIF6muUFQzjaULUHocjxFuGjA%2FlON9vYtJVpi9mvEq1Hf%2Blnl92%2FP0P%2FXfGqtrGlITXkLjjz7bwjPkWTpm2jPhSBwgVUEBiJ25yR3Pb%2BxzAL%2BRhBucUSiIcQM4RlpdK2njwoQgqEI3n%2F34zSA1A50UxFEpySmfYYCedvJ64y%2Bzv5U4yFX2ODtNPa%2FDKTc9bs7gu2obpYjp4y8zeZSCcRVk1enxdg3M%2Bf9ewuevS%2FsDaIIVGauA8%2F5bwRN8nf57It0s9izYMD%2FVCA%2F3z%2BZX%2FhX6ueEbvV1IZkgUIutuWM9Kaxes7YechZPxyS%2Br7iLKJ1SEOMSTD%2FTG8K%2BpNpuvhCBgkFSzPKr1toWgaPJtWgb7ylKfrAXOcmycIallkSUv3S8lmCSDHntwgpYxsHUYU1I55sDU6bJhnATam6e8h5uUc3N3nTSF1YhbijEVZvqviD6ylrwp6C3J3Htekwxb9hQj8ckautgaBqjfYXyioQq%2Bk8Etn2BKgw2NHM1gY6pgFY1kKGAjvH%2BFhfFtJ70e2DFxweLkyHI7ia3vwodQxvzTH7vrOIp1sDyCtc32Kq%2BF75n8QXVX9she9dpriEJPHFDnzSJQkg4pm5ZpRdSozz7%2FfN4y7iaQCO6bBo31vh77TENZ%2BHMnn8G3xsA1F4LKCoXIySobicGAYzQonWJAmprtsQSUpN5ZDKmehhCgjDMx91JpTnEIw8qlcIJ1smqtAnZlKtXKCY&X-Amz-Signature=0ab65786c4c07fd1ca32ecfb2aa015cc68e8847dfd17eb85fcac92b0e4567cf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WRT53QM%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T080724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCICY1ft3orXd%2Fc9REJc0KgYiHGy40KHGYOXdVVBtPXGVLAiB4cBfTi08VRuXS4eyboLBsxyT8QVA2ornWtCtr%2F2tIwSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz7BQcN22BR%2FcXbEUKtwDyMRkb%2FT3TlK6knk5dlkgwE2mmKascfCDDROsOTB4dTRCjkHO6KFPblGzthui%2Bv%2FQl5SM4H%2FIcGiNZwZYFWVoZrpJNjhTLFlYRJEgNSYo9hsav%2FP%2FXN%2B%2FqPCXhWuH5kjENwYwxhg1UIF6muUFQzjaULUHocjxFuGjA%2FlON9vYtJVpi9mvEq1Hf%2Blnl92%2FP0P%2FXfGqtrGlITXkLjjz7bwjPkWTpm2jPhSBwgVUEBiJ25yR3Pb%2BxzAL%2BRhBucUSiIcQM4RlpdK2njwoQgqEI3n%2F34zSA1A50UxFEpySmfYYCedvJ64y%2Bzv5U4yFX2ODtNPa%2FDKTc9bs7gu2obpYjp4y8zeZSCcRVk1enxdg3M%2Bf9ewuevS%2FsDaIIVGauA8%2F5bwRN8nf57It0s9izYMD%2FVCA%2F3z%2BZX%2FhX6ueEbvV1IZkgUIutuWM9Kaxes7YechZPxyS%2Br7iLKJ1SEOMSTD%2FTG8K%2BpNpuvhCBgkFSzPKr1toWgaPJtWgb7ylKfrAXOcmycIallkSUv3S8lmCSDHntwgpYxsHUYU1I55sDU6bJhnATam6e8h5uUc3N3nTSF1YhbijEVZvqviD6ylrwp6C3J3Htekwxb9hQj8ckautgaBqjfYXyioQq%2Bk8Etn2BKgw2NHM1gY6pgFY1kKGAjvH%2BFhfFtJ70e2DFxweLkyHI7ia3vwodQxvzTH7vrOIp1sDyCtc32Kq%2BF75n8QXVX9she9dpriEJPHFDnzSJQkg4pm5ZpRdSozz7%2FfN4y7iaQCO6bBo31vh77TENZ%2BHMnn8G3xsA1F4LKCoXIySobicGAYzQonWJAmprtsQSUpN5ZDKmehhCgjDMx91JpTnEIw8qlcIJ1smqtAnZlKtXKCY&X-Amz-Signature=79632b0a0bb478633ce89ec397fb82572e3fb9950bc97eb35499083b9f59d013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
