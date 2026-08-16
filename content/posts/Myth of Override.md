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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLJLM5ST%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T025152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCIn%2B36xAqfeB%2B1Jr8Xz1aRV8wsVSH%2B7ko9psfZ%2FQy7EgIhAOZYyEtMpne%2Bmnb8F%2FLY54SsIkROIZw8MXPYeFZfET9rKv8DCCEQABoMNjM3NDIzMTgzODA1IgxBH0UG4NYB96h5HsMq3AMwj10vHxYS7WaAm8ztppxcYVUDmuLVBJEN9jTFd%2FlickeCXMAPOaPXQK7TanJPzJ64F5Z%2FzI%2F7qaNDxBWNUl%2Bp%2FdhBdrGAGvXCGDJvRfJs4ZPXYlBjgzn2rNYOdZVDhuAH2KIgMh1R6sL73mVlgYhPcJA2mx0JDngLmylj%2FZbc7aXzgB8VTiu40OT%2B5Ed0M24RIvMdYFzF3gCWpO4tKBxJ9cquIPDZVYsS0nyAnNmMUa1ABNyoB7ZNJaX%2BbXxxPfVFePbItq6lZiXYEkso9UOMUKXcei2VhveqqrTcrbzePuJ%2FQG%2BCAEX65IhNvcvqzGWTr2ZIz0j6ieICr%2B9%2BFZtic0zxx4aci6ElIoQi52JS6HK1Ppsfx2ooVtJJcqd5%2BFRyVRfmM7AZ4IhTM8ZTw9avJYMtdUbaCrA2T8UgRTymTLpiBGsr9wWlAc22rd2gHb%2BoUCP4aWY7RPm8w6EW1l06RnFt278To5U7Ji7zkH%2BBd7mM6rxBEo08yplZyh97wdIe6uEPZE%2FcaWuHDCc0pJnIV7EPU8RUIoIdgSKDOyeYU5bmZ1bcI9IFn04WefoM5rtI353OyA25fj2bjQZosgS0S%2BsbK12g1txfAGEV1YwsHo%2B8uW73QO0nethbsTCj7YPUBjqkAQtCWRXfUlyjldch4ZuCVXOygEibWOeC8bRl3FsiAS2peNtGe%2F92P4tZyOkVZhAkXsBdwToesSq6ngGMt%2BIywWRZygr3UZ2MFR3CSSgxzslg9MLeNVdE6Ami63GhSnzUS8hhnuhtPALUutlUnCV8xEEti4El%2FJp8yi5y3gnXiNkKh91F2odFXAPuFMc0cFaaYa9cAFiYaeFni8H3Dnj0S9PniIFZ&X-Amz-Signature=e84a45c5b4fcdd42019a6a1e4c53d48dd494aefeed05c3c5ee523720f4bfa45c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLJLM5ST%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T025152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCIn%2B36xAqfeB%2B1Jr8Xz1aRV8wsVSH%2B7ko9psfZ%2FQy7EgIhAOZYyEtMpne%2Bmnb8F%2FLY54SsIkROIZw8MXPYeFZfET9rKv8DCCEQABoMNjM3NDIzMTgzODA1IgxBH0UG4NYB96h5HsMq3AMwj10vHxYS7WaAm8ztppxcYVUDmuLVBJEN9jTFd%2FlickeCXMAPOaPXQK7TanJPzJ64F5Z%2FzI%2F7qaNDxBWNUl%2Bp%2FdhBdrGAGvXCGDJvRfJs4ZPXYlBjgzn2rNYOdZVDhuAH2KIgMh1R6sL73mVlgYhPcJA2mx0JDngLmylj%2FZbc7aXzgB8VTiu40OT%2B5Ed0M24RIvMdYFzF3gCWpO4tKBxJ9cquIPDZVYsS0nyAnNmMUa1ABNyoB7ZNJaX%2BbXxxPfVFePbItq6lZiXYEkso9UOMUKXcei2VhveqqrTcrbzePuJ%2FQG%2BCAEX65IhNvcvqzGWTr2ZIz0j6ieICr%2B9%2BFZtic0zxx4aci6ElIoQi52JS6HK1Ppsfx2ooVtJJcqd5%2BFRyVRfmM7AZ4IhTM8ZTw9avJYMtdUbaCrA2T8UgRTymTLpiBGsr9wWlAc22rd2gHb%2BoUCP4aWY7RPm8w6EW1l06RnFt278To5U7Ji7zkH%2BBd7mM6rxBEo08yplZyh97wdIe6uEPZE%2FcaWuHDCc0pJnIV7EPU8RUIoIdgSKDOyeYU5bmZ1bcI9IFn04WefoM5rtI353OyA25fj2bjQZosgS0S%2BsbK12g1txfAGEV1YwsHo%2B8uW73QO0nethbsTCj7YPUBjqkAQtCWRXfUlyjldch4ZuCVXOygEibWOeC8bRl3FsiAS2peNtGe%2F92P4tZyOkVZhAkXsBdwToesSq6ngGMt%2BIywWRZygr3UZ2MFR3CSSgxzslg9MLeNVdE6Ami63GhSnzUS8hhnuhtPALUutlUnCV8xEEti4El%2FJp8yi5y3gnXiNkKh91F2odFXAPuFMc0cFaaYa9cAFiYaeFni8H3Dnj0S9PniIFZ&X-Amz-Signature=427e439b3e721ee14068cfe5aae616578315f686ac15f2dd1a60ce8940c9bd30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
