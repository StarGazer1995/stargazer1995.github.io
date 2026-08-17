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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKI4J3Q%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T121913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIAZDfszz%2FImbRwYKqRUXaCKfSnkP%2FqlMbBahN8KiPq7xAiBhMDjhr1hWrIPbA7ZP7w4mlx7td4AcPzE2xqZAKlQzCyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMRUUy%2B8%2BfBIHqqMI4KtwDZJVespP2yvlvoe0yPzXHDQ61gh63mO7nGK7IGfeI9y2VJdHxA4mav%2FXNVidOpeStyE4bR1CCfQgskAyvS9%2BIoMtjQ9m%2Ffu4GH8ff7k%2BAp3adDAi%2BY%2BkcLbqN1Xkj8ik19cxyYv8RKJmmFfE0usTZv5Z4fvNOkIjDEJK4fF9dvabXknWzKYdZMYIV8q25gbVPmyZhPTM7pytc8JsCBb9pWw5dNdOUHf6zuTzWUX1fs7ZWzmw08%2BeSDJx%2FeINg5I9q2TC6i3sMNewuewXl%2Fez5r2OWt2a2p7vh3wubOFk7k8oseDAVgBBUBoJtARaSyryPNdjSHHhph91CZwJtkSf1%2BM%2FAUqBiLeIjXln4ioZNNNE17hNuzYV721cEtVbWyb4Sn8CozLg%2FoI5%2FuObrX3SVYtLc6N69vLmKG4bBIRG85M3Ey%2BI2jwVtXPouxpZR5cJZ%2BcID6mYzWUwjXqkImaKxGz5Sn78wzsh2WP3OxvuM6oOZWPJi0pBfwE56LeSWdOfaxbIrwr%2FUFRVSBXSgz6ggNsPDKRIJBfxbMUHs6hRIyKkII8htllItRjuAvoLIFHWHXCAQN5GCtkeST2nO6xO08n5KB8IhFME0DPMLTndm9MW2m23VI0oQYF4B5YIw1b6L1AY6pgHFfDFErVzJgAXBvnSjuImcSjaEJ6EYuJpbJ0KwnVjoSlf0kW%2BwpA2MevJ%2FMoup529gmvHuxYZ%2BKuW8Qh5gXmhuRQlE0mweO8D7oWbKKXK65h3d8o92fGhvuSEk5DRXaP7qwNnK5PRJtN%2Bb98G2hAaHdJNDLx8dxcXLu%2FTjO%2FfO%2BC0vCP0k48Pf7twNgevL0LMrA47fVCLpwgEE3LikqUnHLYuVNugS&X-Amz-Signature=6a0f06db1a220439da06695d1c059ec47accaf6feb88de07f6743c2f11fa6ae7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HKI4J3Q%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T121913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIAZDfszz%2FImbRwYKqRUXaCKfSnkP%2FqlMbBahN8KiPq7xAiBhMDjhr1hWrIPbA7ZP7w4mlx7td4AcPzE2xqZAKlQzCyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMRUUy%2B8%2BfBIHqqMI4KtwDZJVespP2yvlvoe0yPzXHDQ61gh63mO7nGK7IGfeI9y2VJdHxA4mav%2FXNVidOpeStyE4bR1CCfQgskAyvS9%2BIoMtjQ9m%2Ffu4GH8ff7k%2BAp3adDAi%2BY%2BkcLbqN1Xkj8ik19cxyYv8RKJmmFfE0usTZv5Z4fvNOkIjDEJK4fF9dvabXknWzKYdZMYIV8q25gbVPmyZhPTM7pytc8JsCBb9pWw5dNdOUHf6zuTzWUX1fs7ZWzmw08%2BeSDJx%2FeINg5I9q2TC6i3sMNewuewXl%2Fez5r2OWt2a2p7vh3wubOFk7k8oseDAVgBBUBoJtARaSyryPNdjSHHhph91CZwJtkSf1%2BM%2FAUqBiLeIjXln4ioZNNNE17hNuzYV721cEtVbWyb4Sn8CozLg%2FoI5%2FuObrX3SVYtLc6N69vLmKG4bBIRG85M3Ey%2BI2jwVtXPouxpZR5cJZ%2BcID6mYzWUwjXqkImaKxGz5Sn78wzsh2WP3OxvuM6oOZWPJi0pBfwE56LeSWdOfaxbIrwr%2FUFRVSBXSgz6ggNsPDKRIJBfxbMUHs6hRIyKkII8htllItRjuAvoLIFHWHXCAQN5GCtkeST2nO6xO08n5KB8IhFME0DPMLTndm9MW2m23VI0oQYF4B5YIw1b6L1AY6pgHFfDFErVzJgAXBvnSjuImcSjaEJ6EYuJpbJ0KwnVjoSlf0kW%2BwpA2MevJ%2FMoup529gmvHuxYZ%2BKuW8Qh5gXmhuRQlE0mweO8D7oWbKKXK65h3d8o92fGhvuSEk5DRXaP7qwNnK5PRJtN%2Bb98G2hAaHdJNDLx8dxcXLu%2FTjO%2FfO%2BC0vCP0k48Pf7twNgevL0LMrA47fVCLpwgEE3LikqUnHLYuVNugS&X-Amz-Signature=288e289585567cf6774ed394cf094520f8245fd3e02e34983cd54990b0610e65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
