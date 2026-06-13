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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMJO6TKF%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T170820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCuiX1Rn0kyA0QMXKpIL18rnAFunKKtBrfPQRA8%2FtegTwIgQax9QUzw51ai9rrYg9boCCbfizAKucXLb7DFwXGE2Wgq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCWXyW%2BRryogcQbUcyrcAyGB2QLi51tH765yi1zbUsVCS1iEw0uEWYp6X%2Bu42%2Fi8rh6JT3UyxPicpKiRunZ78Y1Q4ggda6x23%2F2Ia%2FBtz5hdVFq4%2BAzWVkD92WQNCKDt99zLOEcaIG9blRcxv4SkI8FOJtRpfFwMOuAJemh9xtw3ME3gC9EYj%2Fq3lQOX%2B5SzW5pemoNWRXztbgwvBewy4Jf1KUpTb2zCBxqHtW0O1JfDa9N8nj9pCa1cixr1t8oFj5yx9y7T5KqiYssgm8OBJ5hsntZ9rELy%2FnETD9i%2FPjA6wM6%2B%2BgVKklWDzDO4cGoL40cN%2FxECZWpkhakcvuTWy9FsTpMZK3PfxaPCkbUzDTA0j0FuvZjxFTCQtO4ojuTie5urxp9CP8o8nwAwoZ7FymyEGu4c%2B4DYY91I9U876cY03MOtlhqJIa3VUmdeUZY4YJLY4ifaz1bAKThbdYMun%2B0LnEzweG0ZK9fx1C6OQKv9gFLNUX7DFt2RmDmMzU8bVRrreeZ2tr37J0HwOccEUtMc0Vopeimtt685Ukr2I5HT3P5nf4YvTojm7xwvAcEsUHAenlW%2FyOL5tfRh8q1odm4ZSq8zvpxFkCsBwLHOYPgbaBBzIGmVUu9zTIjY1Aq69OPlul4YvyBNwThVMN%2BWttEGOqUBLOUXop6Jiw4d9jquyHIdGUSoS8glrsaF2yU1FLv2gu1zLKBmuv1j4ncA3WJpbNrVvhp8OttzyjZr3xsDbLuO1vrHas%2FvzzNi%2BMDcNgqQ8iQl%2FWiUatH6TMQcpomK0JoslJGJxUHrlWWW3gEbK2raTgPSt33XSBzM0t0fPj4y1uXGMuQig1IF4A8%2BVsgzP5ktBMXQ%2FzqRRpK0e%2FVXFQjMaPl6Kmh%2F&X-Amz-Signature=4c5a08d28863be5390491049d0413c4f19d40c75918040051c9464bd1c070a3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMJO6TKF%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T170820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCuiX1Rn0kyA0QMXKpIL18rnAFunKKtBrfPQRA8%2FtegTwIgQax9QUzw51ai9rrYg9boCCbfizAKucXLb7DFwXGE2Wgq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCWXyW%2BRryogcQbUcyrcAyGB2QLi51tH765yi1zbUsVCS1iEw0uEWYp6X%2Bu42%2Fi8rh6JT3UyxPicpKiRunZ78Y1Q4ggda6x23%2F2Ia%2FBtz5hdVFq4%2BAzWVkD92WQNCKDt99zLOEcaIG9blRcxv4SkI8FOJtRpfFwMOuAJemh9xtw3ME3gC9EYj%2Fq3lQOX%2B5SzW5pemoNWRXztbgwvBewy4Jf1KUpTb2zCBxqHtW0O1JfDa9N8nj9pCa1cixr1t8oFj5yx9y7T5KqiYssgm8OBJ5hsntZ9rELy%2FnETD9i%2FPjA6wM6%2B%2BgVKklWDzDO4cGoL40cN%2FxECZWpkhakcvuTWy9FsTpMZK3PfxaPCkbUzDTA0j0FuvZjxFTCQtO4ojuTie5urxp9CP8o8nwAwoZ7FymyEGu4c%2B4DYY91I9U876cY03MOtlhqJIa3VUmdeUZY4YJLY4ifaz1bAKThbdYMun%2B0LnEzweG0ZK9fx1C6OQKv9gFLNUX7DFt2RmDmMzU8bVRrreeZ2tr37J0HwOccEUtMc0Vopeimtt685Ukr2I5HT3P5nf4YvTojm7xwvAcEsUHAenlW%2FyOL5tfRh8q1odm4ZSq8zvpxFkCsBwLHOYPgbaBBzIGmVUu9zTIjY1Aq69OPlul4YvyBNwThVMN%2BWttEGOqUBLOUXop6Jiw4d9jquyHIdGUSoS8glrsaF2yU1FLv2gu1zLKBmuv1j4ncA3WJpbNrVvhp8OttzyjZr3xsDbLuO1vrHas%2FvzzNi%2BMDcNgqQ8iQl%2FWiUatH6TMQcpomK0JoslJGJxUHrlWWW3gEbK2raTgPSt33XSBzM0t0fPj4y1uXGMuQig1IF4A8%2BVsgzP5ktBMXQ%2FzqRRpK0e%2FVXFQjMaPl6Kmh%2F&X-Amz-Signature=14c8d6afe78b65764f1edb2bdb7de442974bce82de55acc44d92869606394138&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
