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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWAIG5IL%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T203938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDB%2B8F1YmjsLyk37pA2zxLFE%2Fd8n142lJC9mJa1P8RPDwIhAKuRCoJjw3D%2B%2B5yUreFaymm4YDF85y5kyQJXMWsERrgRKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZ8pPUPk%2FIPuD%2FBrgq3APCHz5st%2BTU1flplWzwOyrq%2F2VkfuBdPnuCLYD8Fp%2BNuhftPgt05Zy%2F6TanGLAqmsp8OvJTFwBLYWH2tautMDdPec8VQlLbYpOBUx2Bi%2F3ls%2FfwQhUxOEYGYEFMga9ohNjSvHQEfut%2FbEmPTvuJ2WalxTi2hdUcTTEdtYVqSrJmqTg%2BTKf%2BDRHpDfuQzSECK1GzijJA5W%2B7e%2Burf7wQOszsymTD0t9embzMEUlMnte8dVrk5X6YLelDe024UUn8t5aG1YqN0SLMOn1NPtT%2FxZHNeNjj1DxJ0avyLjJexGa4jsIlD%2FnOG9XEJdDgUg6TjtV9dpob68JdY%2B%2F9S1ieLb14646VF1dAdOpRkM1aUTOneGElBS2U%2Bc7UtI%2Fjdg9QH5veeoq0jde%2FUleoK8NODLz9RMaabZWlKz%2BqfQzTwjwRKn1exXVRdXV%2FoIjncFIZcYX9w8MJoABrVwk3jBbVbSqZzu4H3K%2Ftd6Fl4p0439gYhBHEI%2BubMpt87euK6CeDKRCjG6VizMo8CLnOo7Kn3Wj8NPRxPVkHZzkoFvxc3JugF7jix2BoWWKsZEd0DJU%2FVa4bTMof8lFa9xpAp%2FnQfFe0gOQEmU4WGvsY0SijJnSJTpCVbPfoBuKhk4R6RTDFl7nTBjqkAVAns5wLk4vWdPmYpeGwI%2BS5T4U9gRPhVbNiR0xn4m2uAHu423c8hSNXv%2B0Dcemq2QfcJk3aq5Cs0HUDglF0aaPihy2apJfYPgDuwaQu9AgqLZkXmttNAt1imxjrZ397s48amnpGcnQ8jptEsVuGrRb8abLvEP6kD7RTejx6lTdXlapkUzLxwb91iKBWIN8Lk5FnM9jjvxpE36b65wWWs1XJ3lAy&X-Amz-Signature=94223d1ed3004a68900bb2fd2c8b28fce6c517f6f04d284cb78a629d1052e1d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWAIG5IL%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T203938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDB%2B8F1YmjsLyk37pA2zxLFE%2Fd8n142lJC9mJa1P8RPDwIhAKuRCoJjw3D%2B%2B5yUreFaymm4YDF85y5kyQJXMWsERrgRKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZ8pPUPk%2FIPuD%2FBrgq3APCHz5st%2BTU1flplWzwOyrq%2F2VkfuBdPnuCLYD8Fp%2BNuhftPgt05Zy%2F6TanGLAqmsp8OvJTFwBLYWH2tautMDdPec8VQlLbYpOBUx2Bi%2F3ls%2FfwQhUxOEYGYEFMga9ohNjSvHQEfut%2FbEmPTvuJ2WalxTi2hdUcTTEdtYVqSrJmqTg%2BTKf%2BDRHpDfuQzSECK1GzijJA5W%2B7e%2Burf7wQOszsymTD0t9embzMEUlMnte8dVrk5X6YLelDe024UUn8t5aG1YqN0SLMOn1NPtT%2FxZHNeNjj1DxJ0avyLjJexGa4jsIlD%2FnOG9XEJdDgUg6TjtV9dpob68JdY%2B%2F9S1ieLb14646VF1dAdOpRkM1aUTOneGElBS2U%2Bc7UtI%2Fjdg9QH5veeoq0jde%2FUleoK8NODLz9RMaabZWlKz%2BqfQzTwjwRKn1exXVRdXV%2FoIjncFIZcYX9w8MJoABrVwk3jBbVbSqZzu4H3K%2Ftd6Fl4p0439gYhBHEI%2BubMpt87euK6CeDKRCjG6VizMo8CLnOo7Kn3Wj8NPRxPVkHZzkoFvxc3JugF7jix2BoWWKsZEd0DJU%2FVa4bTMof8lFa9xpAp%2FnQfFe0gOQEmU4WGvsY0SijJnSJTpCVbPfoBuKhk4R6RTDFl7nTBjqkAVAns5wLk4vWdPmYpeGwI%2BS5T4U9gRPhVbNiR0xn4m2uAHu423c8hSNXv%2B0Dcemq2QfcJk3aq5Cs0HUDglF0aaPihy2apJfYPgDuwaQu9AgqLZkXmttNAt1imxjrZ397s48amnpGcnQ8jptEsVuGrRb8abLvEP6kD7RTejx6lTdXlapkUzLxwb91iKBWIN8Lk5FnM9jjvxpE36b65wWWs1XJ3lAy&X-Amz-Signature=869d251ad3c3a6696f2d1d69e17e353d3308eaee648edf5b47995297e322a174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
