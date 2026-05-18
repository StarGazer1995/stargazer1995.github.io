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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDHZ5SKV%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T210128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHneJu7jv9NrDxKlaDaDqkWRDPnp46lkQn11JXDleQk9AiASmcYasZa2kOwXlCrABhQQcoQnjAIGol5v2CRS4sfwCiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCaLts1qcPl92xkFJKtwD4JJcZWhw27Eawc%2BQ52JxDe8e1y5rBijmb5N8%2BfspNmHAc%2FoEHZ3K36QQ3JMWShRx8Xs47EG5eHWMpypYQw5w842osVUpye7Qo0LXUIItUkfgyKuoDaaCxoVxOQxtcoi17iJAziyh6vIODsa9Xj5sDVljAqVQ4v0D8QSehDxmr3cnmu66L%2FOjb4IgbA3ygHLfKo8RbEkUU7JG3bwgtzci3sFdWqLhsPjAWEpI1p2HNzeQAmGZVuXTkyH8zETrMPcbwzeEStLzDzg48%2F3SEZe2XENY7KMxtc0cjVZPfuLHrlw8Lbbd41LfIWXsLOMnysa3TPBhboQ99xUpfzOHIvry560NSdL86hoZ%2BshGJ1b8RrCuXQRKmMMEOtbmB7kJRsgOhdXy0wjVOptnPZiKBPh25mBulvH1o8ov1S0r6KNIhaxDCEEIi1v75bJkVaImMCQ7gsRXCumInW4vSpLTQhSMIzRXDjkDidJWkBoImcCQaOoVMCRshe4Te3i2npxYnVdbXV9FjW%2BNTkshlA%2Fz1996I87826aHkF%2F5oHDyjXAxevZUaFa6XA2Ukjzc1popCw25vZG1kjQyxiX8MKyiMLXb14MeFSdBYnLxDj5sP%2FIwyQAmhXT%2FVK9lNYvs0%2BEw%2BuCt0AY6pgFSDEN0ICs6fhEBGoO4WuJPP5x4XcVyDW9sifyt7CIW9DArPHiwN5tsqP%2B4hh3mVyOzDbOKRPKGVi3v5scrl0LtTULbHlEVH3m91%2FGefDpmaLoLi9RLAffFU88ih0H2NYonliPEOnWUo6cQUz7KTNdDL0BBLYZK3whXRQybPHUOF2R6iBfcID2mo30aJPptrLnIaUWU5BmdBo4tGrAMXypDiHnApLyr&X-Amz-Signature=6b5b8641531b7f98bbc2a4a59db1d0bd39d1741291f11c88665dfeaa7d46ceb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDHZ5SKV%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T210128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHneJu7jv9NrDxKlaDaDqkWRDPnp46lkQn11JXDleQk9AiASmcYasZa2kOwXlCrABhQQcoQnjAIGol5v2CRS4sfwCiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCaLts1qcPl92xkFJKtwD4JJcZWhw27Eawc%2BQ52JxDe8e1y5rBijmb5N8%2BfspNmHAc%2FoEHZ3K36QQ3JMWShRx8Xs47EG5eHWMpypYQw5w842osVUpye7Qo0LXUIItUkfgyKuoDaaCxoVxOQxtcoi17iJAziyh6vIODsa9Xj5sDVljAqVQ4v0D8QSehDxmr3cnmu66L%2FOjb4IgbA3ygHLfKo8RbEkUU7JG3bwgtzci3sFdWqLhsPjAWEpI1p2HNzeQAmGZVuXTkyH8zETrMPcbwzeEStLzDzg48%2F3SEZe2XENY7KMxtc0cjVZPfuLHrlw8Lbbd41LfIWXsLOMnysa3TPBhboQ99xUpfzOHIvry560NSdL86hoZ%2BshGJ1b8RrCuXQRKmMMEOtbmB7kJRsgOhdXy0wjVOptnPZiKBPh25mBulvH1o8ov1S0r6KNIhaxDCEEIi1v75bJkVaImMCQ7gsRXCumInW4vSpLTQhSMIzRXDjkDidJWkBoImcCQaOoVMCRshe4Te3i2npxYnVdbXV9FjW%2BNTkshlA%2Fz1996I87826aHkF%2F5oHDyjXAxevZUaFa6XA2Ukjzc1popCw25vZG1kjQyxiX8MKyiMLXb14MeFSdBYnLxDj5sP%2FIwyQAmhXT%2FVK9lNYvs0%2BEw%2BuCt0AY6pgFSDEN0ICs6fhEBGoO4WuJPP5x4XcVyDW9sifyt7CIW9DArPHiwN5tsqP%2B4hh3mVyOzDbOKRPKGVi3v5scrl0LtTULbHlEVH3m91%2FGefDpmaLoLi9RLAffFU88ih0H2NYonliPEOnWUo6cQUz7KTNdDL0BBLYZK3whXRQybPHUOF2R6iBfcID2mo30aJPptrLnIaUWU5BmdBo4tGrAMXypDiHnApLyr&X-Amz-Signature=c909a88002ee69b8b42ea4f72c8264863286bf988aa02b391545208618b5f2d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
