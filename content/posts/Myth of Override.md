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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPWI3DRX%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T054105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGLqjByryBhjcjmp1iJuYdUHCxRXD3hozdGIZRRkt9udAiEAsY1S3oxjqNtMX1Rc00fpx1pj6VsRyOasshNBMUQJwfMq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDKnCDV2wJHL3HuynLSrcAx3voBOg%2BK8NBw9ZR%2FgNKva4%2BkquxPgYVNwUddlt4xq3MXIxXLixj9TL6kNg1sP7lM59IVlDfQYdCusNS7TA3y5ZbreavtQNMGZsZNAxDfMr5aOthC0SAYR%2B6cBPjowQcYfxlKHn%2BPiOL%2F4Jc8ALXLdGs421x7HdScnOZRNjfeVh70qFcCUbkNuBY3%2FGZuZJBKnxP29AYTrZBliuQDxVh0HrxwQaTWh4%2BMZtW9Ta1HLVGc24mDD4ItouZq4L4f7BH83zXV28y8JS4y5Dfpr%2B4qJsjYrpjxYygNskVUHs4uGbLLzYA2isKRGpq06goldI7OG219vjC5Eed5Owm%2B7cVZU9EB6OsMhKjIeZFFrA5i4JIdde1KbWY9uKEybtpU5R4JSJNmeBgpPa9z20vPE4i47LV16QVrKZ5PtxRl4y%2Bi3xrEdiwbWE7cG1uAFii%2BtqF2ys8WYSg5bT9e3JTx7ykS%2B5WZXryC19yM%2F1xxIitbthJDbg117qF21BO2LV7QHRb5UK6xXFafd6Jbsba%2F%2B9HTj1sxlZHQ%2FyRhovGAMWJw1B6x%2BoyZt0YHB9g4y0m96AmYhxRQ6N6HgQ%2FWAeKXy8HZfFegb%2FIb10RGS054dO3V1asLWt4wyi7iXXGUXfMNeGkNAGOqUBgDIjQ8KLntQxtfY3ZjSBSJO57mv15QFf8W24gWFT9xZwx4v4POE9ec997sYZI%2FUDhqxGH3fhETNARhatyKcvbtlXgmG4W0kN9YcTx%2Bl9o8tbqWpGTI8bp%2BMkAcwEAy7oQNwInR52YZaxyYKwWVHavkm6wF96jEHswWdqrckP7%2BWnm1q%2BFHmoBkuZjDemKuPtPnDfH9SEeeju3%2BFiENiHSVxRpYdQ&X-Amz-Signature=100bfe1223f4c89cd0edd21155de4155291fd29a1e0eb0b5ccac859a0885fd8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPWI3DRX%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T054105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGLqjByryBhjcjmp1iJuYdUHCxRXD3hozdGIZRRkt9udAiEAsY1S3oxjqNtMX1Rc00fpx1pj6VsRyOasshNBMUQJwfMq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDKnCDV2wJHL3HuynLSrcAx3voBOg%2BK8NBw9ZR%2FgNKva4%2BkquxPgYVNwUddlt4xq3MXIxXLixj9TL6kNg1sP7lM59IVlDfQYdCusNS7TA3y5ZbreavtQNMGZsZNAxDfMr5aOthC0SAYR%2B6cBPjowQcYfxlKHn%2BPiOL%2F4Jc8ALXLdGs421x7HdScnOZRNjfeVh70qFcCUbkNuBY3%2FGZuZJBKnxP29AYTrZBliuQDxVh0HrxwQaTWh4%2BMZtW9Ta1HLVGc24mDD4ItouZq4L4f7BH83zXV28y8JS4y5Dfpr%2B4qJsjYrpjxYygNskVUHs4uGbLLzYA2isKRGpq06goldI7OG219vjC5Eed5Owm%2B7cVZU9EB6OsMhKjIeZFFrA5i4JIdde1KbWY9uKEybtpU5R4JSJNmeBgpPa9z20vPE4i47LV16QVrKZ5PtxRl4y%2Bi3xrEdiwbWE7cG1uAFii%2BtqF2ys8WYSg5bT9e3JTx7ykS%2B5WZXryC19yM%2F1xxIitbthJDbg117qF21BO2LV7QHRb5UK6xXFafd6Jbsba%2F%2B9HTj1sxlZHQ%2FyRhovGAMWJw1B6x%2BoyZt0YHB9g4y0m96AmYhxRQ6N6HgQ%2FWAeKXy8HZfFegb%2FIb10RGS054dO3V1asLWt4wyi7iXXGUXfMNeGkNAGOqUBgDIjQ8KLntQxtfY3ZjSBSJO57mv15QFf8W24gWFT9xZwx4v4POE9ec997sYZI%2FUDhqxGH3fhETNARhatyKcvbtlXgmG4W0kN9YcTx%2Bl9o8tbqWpGTI8bp%2BMkAcwEAy7oQNwInR52YZaxyYKwWVHavkm6wF96jEHswWdqrckP7%2BWnm1q%2BFHmoBkuZjDemKuPtPnDfH9SEeeju3%2BFiENiHSVxRpYdQ&X-Amz-Signature=0de209e881fc234107d4271631d41fb7972e83a3e4b90db3fe9c6ab88508c303&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
