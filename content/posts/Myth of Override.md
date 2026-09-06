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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWV6ENWZ%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T175101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCPAIefzXf%2BZ345kKe4Kpj7CcaWL6mQPPsxcSFeONkMrgIhALpfYxnEdpScIGi5EHOnmnqLRNqwRFrxjh%2BZmQrTUG86Kv8DCCoQABoMNjM3NDIzMTgzODA1IgyOLQlq33aeEQI%2FORwq3AM%2FLsaYKsZopBhE3WrT9k5XOwjPb%2F43T%2Fmrww0RobhHDlugaHJnPSZkL0pE7fT2DXxRo%2FLPPkYZ4TKlvbQ%2B721P4sPC4piLX%2FJZZArjHr8Cmn9z4XsSZAjo5t%2FDYeVfP7Wy8JVHxha09YSd4bXrFnpxAVZGWKlFM0Y4Fl1mPShBWCXR%2BZ8KHSOrnPyXMxQmbFk7RB%2FnGZVyC%2F%2F%2B3kMF7UFH927Vxny%2B5rDrdmEwVJxdfV%2BpI83zkd6evWCUxeUwHIXZ5695sKMn4HDtZBcQsFnV3159Nb14JxoG%2F%2BArSQ8GVYrprcuoQI2b4um1Ctl8WQTKgjJ2lietk%2FMrzo0ZU3jMbM5wufh1AFe0IgHUYwNfO3gAgMeQ83g5pckxTsQXqL8te%2FN8LWB%2B5Dl0HjNEjgCL922R1%2BPPPS%2F6qIz5YBVAa36FMEk7QZRdbMLjvwp4FzmgIypbN1sE9oVlB2p5Hq2Ny7qYiGZ0Jmy3jy9Cjagxzo%2BP7bI7nudKG8sStmCmABQYffcOu3uAyxewHwF4rL9ZD0nxQ%2BaVgr9Bta9KkaqPrmNkR%2BDZbZ92pJOKxWTT%2FsK69k%2Fo1k7aR8EXxjPy4GVbeq2MbYx28nsPwNAj8XVzX5QlM1rUSL1vloqWTTCsuvbUBjqkATpEX%2FLpvgPFkeipoqoLdYCUP%2BNfX1TZM%2BKVBHobMHuXpcJ6ITfPuyCblDa%2Bero7DT5zCFIkOcGvNie19J2p9gigdWHOjOpaxBN22DBkUWNl69WSipxTwwmMVv9fhdE4m4O%2BC4hv3UKZHO5a%2BJHP4GoZ67PL1gNO%2BCUREY1imrkRHo59isfLRuLP7vhvDP6yciAa29MkYfKNA0yYFsCW3nWG9A5Y&X-Amz-Signature=60003bb12d151795f518205c849fd8568d2f95a6382fbbb379ff075cd363519b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWV6ENWZ%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T175101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCPAIefzXf%2BZ345kKe4Kpj7CcaWL6mQPPsxcSFeONkMrgIhALpfYxnEdpScIGi5EHOnmnqLRNqwRFrxjh%2BZmQrTUG86Kv8DCCoQABoMNjM3NDIzMTgzODA1IgyOLQlq33aeEQI%2FORwq3AM%2FLsaYKsZopBhE3WrT9k5XOwjPb%2F43T%2Fmrww0RobhHDlugaHJnPSZkL0pE7fT2DXxRo%2FLPPkYZ4TKlvbQ%2B721P4sPC4piLX%2FJZZArjHr8Cmn9z4XsSZAjo5t%2FDYeVfP7Wy8JVHxha09YSd4bXrFnpxAVZGWKlFM0Y4Fl1mPShBWCXR%2BZ8KHSOrnPyXMxQmbFk7RB%2FnGZVyC%2F%2F%2B3kMF7UFH927Vxny%2B5rDrdmEwVJxdfV%2BpI83zkd6evWCUxeUwHIXZ5695sKMn4HDtZBcQsFnV3159Nb14JxoG%2F%2BArSQ8GVYrprcuoQI2b4um1Ctl8WQTKgjJ2lietk%2FMrzo0ZU3jMbM5wufh1AFe0IgHUYwNfO3gAgMeQ83g5pckxTsQXqL8te%2FN8LWB%2B5Dl0HjNEjgCL922R1%2BPPPS%2F6qIz5YBVAa36FMEk7QZRdbMLjvwp4FzmgIypbN1sE9oVlB2p5Hq2Ny7qYiGZ0Jmy3jy9Cjagxzo%2BP7bI7nudKG8sStmCmABQYffcOu3uAyxewHwF4rL9ZD0nxQ%2BaVgr9Bta9KkaqPrmNkR%2BDZbZ92pJOKxWTT%2FsK69k%2Fo1k7aR8EXxjPy4GVbeq2MbYx28nsPwNAj8XVzX5QlM1rUSL1vloqWTTCsuvbUBjqkATpEX%2FLpvgPFkeipoqoLdYCUP%2BNfX1TZM%2BKVBHobMHuXpcJ6ITfPuyCblDa%2Bero7DT5zCFIkOcGvNie19J2p9gigdWHOjOpaxBN22DBkUWNl69WSipxTwwmMVv9fhdE4m4O%2BC4hv3UKZHO5a%2BJHP4GoZ67PL1gNO%2BCUREY1imrkRHo59isfLRuLP7vhvDP6yciAa29MkYfKNA0yYFsCW3nWG9A5Y&X-Amz-Signature=b0a630e4f78c95810131ebd023eae57d50dff78bde62ca39a8805ba916d57f36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
