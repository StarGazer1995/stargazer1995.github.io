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

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">code_examples/cpp_examples/01_myth_of_override/src/main.cpp at main · StarGazer1995/code_examples</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;">Contribute to StarGazer1995/code_examples development by creating an account on GitHub.</div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://github.githubassets.com/favicons/favicon.svg"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/StarGazer1995/code_examples/blob/main/cpp_examples/01_myth_of_override/src/main.cpp</div></div></div><div style="flex: 1 1 180px; display: block; position: relative;"><div style="position: absolute; inset: 0px;"><div style="width: 100%; height: 100%;"><img src="https://opengraph.githubassets.com/24dae9f0ad65ae788f1f405a6204e98dbfd21a90718b49e4873c8a534314d035/StarGazer1995/code_examples" referrerpolicy="no-referrer" style="display: block; object-fit: cover; border-radius: 3px; width: 100%; height: 100%;"></div></div></div></a></div></div>

My initial thought was, 'How can we override a private virtual function? It wouldn't pass the compilation test.' However, I was surprised by the real compiler's response: PASS.

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VL5OAXRB%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T063652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC20vKMYdRKGQhK6t861Aayp3WxP8hSd%2FPlL5ZxAj2EIwIhAKJP75DEfi%2BkeI3GxlvIVTCtHPyUmAv%2B57uak4YiDsLWKv8DCFYQABoMNjM3NDIzMTgzODA1IgwJyXu4HR3rIS9BACQq3AN0AtiFKD%2Fd%2BZIzJFBZiOKqWy2LZrJbzuP2oHEe0w8LVeqkhIN3rtlNTmFOLO13mA1Fa5jPY1%2BIEKXR%2B4rfdq5VpKU1NuJ3j4vhePbWihxOzeJuoptv%2BeEcAWvx90%2FbzCCfiCe4OS9Xov0%2BoqG%2F4gf%2F0qOMu9U14m309Sl8aoBSpuHilhhMBXlFGsqH59X%2BId0rKPBuRBzW6D9fCXjG%2F1jSw3j3HRCEJVj%2FzgunumpAWeLdFFTYKatbjS4%2F4E8uuI%2FlY7QIqrCtM2N2XZzd1%2Fy9%2BWGEORTkCAxAbJv99LbB61PiJ%2FhQetRK0zXh2g4A%2FhQt1lgOY4DMn6bmlr%2FtD3ZEstlQ5dEmasuQebAWyA%2FsDF8JZf5m9A%2Fi5WG8YggYhvFsScCjwj8bphZhHaH3T7r3JHIb8FHs0Yq0aa7Gy5cWRVCUDSfj61TAnH60ed2R%2FKlA%2FJ%2BJpGWx2s2E5H7SLZu2Nl0WUwDZ8ze%2FOaTztD0OvRM9jwhIJxjVkv3rA9fCfCfKCFqtmM16K6X2kJ6HMic5oJBg9z1dikVz4%2BikSQ5NeMIhI2dBCDW8g3rXweNuUCjd%2FEhyJo0FH4akZM9aEOpLmOtDTLszUM2TpTzGjiQ0XqRht5TAIjLXpv%2BvzDCl7bbABjqkAQFAkJAejQDYgsWFYMmB2ExZ2uIoroqt3Ytu4sRPeX7YcW0o0SEEKtmb12C3fd5F0qoMktKixd949y6z4NZtjV9ILrFf1r4GE2aXaC9nSI%2Bc6pyztUJO5AgIo96WLvD4sc0dUlcEWGaGhChcb7%2FVcsYMkqZWNkjFnZjgTEjwxrN8CzQUpvKSCJPh5nZ7n29QdlLLmIv4uRGfUIDiJFJqHf2ccyQp&X-Amz-Signature=87a4e84fa7e19c43904b6a68e00662a7313617e7e3b5f9e962b9aea1da687454&X-Amz-SignedHeaders=host&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VL5OAXRB%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T063652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC20vKMYdRKGQhK6t861Aayp3WxP8hSd%2FPlL5ZxAj2EIwIhAKJP75DEfi%2BkeI3GxlvIVTCtHPyUmAv%2B57uak4YiDsLWKv8DCFYQABoMNjM3NDIzMTgzODA1IgwJyXu4HR3rIS9BACQq3AN0AtiFKD%2Fd%2BZIzJFBZiOKqWy2LZrJbzuP2oHEe0w8LVeqkhIN3rtlNTmFOLO13mA1Fa5jPY1%2BIEKXR%2B4rfdq5VpKU1NuJ3j4vhePbWihxOzeJuoptv%2BeEcAWvx90%2FbzCCfiCe4OS9Xov0%2BoqG%2F4gf%2F0qOMu9U14m309Sl8aoBSpuHilhhMBXlFGsqH59X%2BId0rKPBuRBzW6D9fCXjG%2F1jSw3j3HRCEJVj%2FzgunumpAWeLdFFTYKatbjS4%2F4E8uuI%2FlY7QIqrCtM2N2XZzd1%2Fy9%2BWGEORTkCAxAbJv99LbB61PiJ%2FhQetRK0zXh2g4A%2FhQt1lgOY4DMn6bmlr%2FtD3ZEstlQ5dEmasuQebAWyA%2FsDF8JZf5m9A%2Fi5WG8YggYhvFsScCjwj8bphZhHaH3T7r3JHIb8FHs0Yq0aa7Gy5cWRVCUDSfj61TAnH60ed2R%2FKlA%2FJ%2BJpGWx2s2E5H7SLZu2Nl0WUwDZ8ze%2FOaTztD0OvRM9jwhIJxjVkv3rA9fCfCfKCFqtmM16K6X2kJ6HMic5oJBg9z1dikVz4%2BikSQ5NeMIhI2dBCDW8g3rXweNuUCjd%2FEhyJo0FH4akZM9aEOpLmOtDTLszUM2TpTzGjiQ0XqRht5TAIjLXpv%2BvzDCl7bbABjqkAQFAkJAejQDYgsWFYMmB2ExZ2uIoroqt3Ytu4sRPeX7YcW0o0SEEKtmb12C3fd5F0qoMktKixd949y6z4NZtjV9ILrFf1r4GE2aXaC9nSI%2Bc6pyztUJO5AgIo96WLvD4sc0dUlcEWGaGhChcb7%2FVcsYMkqZWNkjFnZjgTEjwxrN8CzQUpvKSCJPh5nZ7n29QdlLLmIv4uRGfUIDiJFJqHf2ccyQp&X-Amz-Signature=96c2e4c82bf64a3e3d46210716f5de5f3cf0c1a0e371233c7cd78ee1b99357f2&X-Amz-SignedHeaders=host&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">virtual function specifier - cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://en.cppreference.com/favicon.ico"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
