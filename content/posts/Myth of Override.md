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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR6NQFU5%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T094818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDSq5hzi07MD42tCgNaBXWgjHH5RBh7JNYiBjaXe3sSUAiEA1EJsDdVMxEC8ECGYlg3wbhOz6XWB4pYmsMW9wmyBtv0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDNSvdfOROmG2XI7dWyrcA5apd1DADtxLp6aQ3Xf0dWM%2FblSA6Wv0BlEflwoWvyENKQn5lKRQvO6WIDoIee%2B9f2D67gTPiewUg0qXPk0Ko%2FDH%2Bo8blc4iimcnTPKyuyW8lMqBfbSuaA0vvc12a8ZPu4LvnOi%2Fb%2FKUGBe3Ja9EDN9MH78e5b8eAiOJMUvJJplvR1L7m%2F7zAyqIOm%2Fqd1IHPK0lfFfSOVaqiX%2BivxE0Fapqo%2FsOexnFQQlAGP6VZHqsgJf2XipligZ2fi5ptFj2eorgOj4fn2kmWfUSMk6%2F37fi7k4e6dn9SROLjZBDiSAp6hzNXVhAsYvFn9RpCf5m7BYITSqRtl%2FNL9onuIFJagxuaL6L960jNLukBu1iGmwn%2FeLYyy6TbrTKJr%2B1foL753cGhBBRDaqF%2Bira2zI8QKCYsGEITo4CMLn5oPJ%2BF4ci0PvUK%2Fw20HMJAW4lA8HCSFvcpPBxHSA%2BlxrhxXynzy37Oov4sW5gdpT%2B6FetTU%2BPhe4332Yuv2k8mph6OvbuQB7Ed8fGrYK7Ke1uiIQ%2FrN3RN5x%2F8WlK5uMR4FuvPNCXXHWmqjkZaO%2FfIZ8lmymRN1dCh92yGuFXjU9Ttr3Wh7dL4OOqlvv3lb1kWNMhzGD1mcLqpDAAk3kih7GhMNyS3dIGOqUBIHuuyavCZe3%2Bx2PjaRnMD6ecjSaFvSeRLGLxQAUNNflYKrhcVbqvZVceSKf9kTob43zELx0HIq6VZ3IkjvhPZapIk%2BsKaIIaha417ETgTFLHo0VeNJP%2B14a2uHaIa%2FIOT3tZNqR37bMIXuC6la2xn7JsXJ56rpJtwcgb1SUv2AGLWEE%2Fm5dVMXaIGUzInx37Ixms%2FIIQlV52dNAdOS2x%2B4hYs6wl&X-Amz-Signature=12f94bdc80cc3cccb4523c8d1e186b0aee708266b79aa8a23c842aed375c223b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR6NQFU5%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T094818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIDSq5hzi07MD42tCgNaBXWgjHH5RBh7JNYiBjaXe3sSUAiEA1EJsDdVMxEC8ECGYlg3wbhOz6XWB4pYmsMW9wmyBtv0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDNSvdfOROmG2XI7dWyrcA5apd1DADtxLp6aQ3Xf0dWM%2FblSA6Wv0BlEflwoWvyENKQn5lKRQvO6WIDoIee%2B9f2D67gTPiewUg0qXPk0Ko%2FDH%2Bo8blc4iimcnTPKyuyW8lMqBfbSuaA0vvc12a8ZPu4LvnOi%2Fb%2FKUGBe3Ja9EDN9MH78e5b8eAiOJMUvJJplvR1L7m%2F7zAyqIOm%2Fqd1IHPK0lfFfSOVaqiX%2BivxE0Fapqo%2FsOexnFQQlAGP6VZHqsgJf2XipligZ2fi5ptFj2eorgOj4fn2kmWfUSMk6%2F37fi7k4e6dn9SROLjZBDiSAp6hzNXVhAsYvFn9RpCf5m7BYITSqRtl%2FNL9onuIFJagxuaL6L960jNLukBu1iGmwn%2FeLYyy6TbrTKJr%2B1foL753cGhBBRDaqF%2Bira2zI8QKCYsGEITo4CMLn5oPJ%2BF4ci0PvUK%2Fw20HMJAW4lA8HCSFvcpPBxHSA%2BlxrhxXynzy37Oov4sW5gdpT%2B6FetTU%2BPhe4332Yuv2k8mph6OvbuQB7Ed8fGrYK7Ke1uiIQ%2FrN3RN5x%2F8WlK5uMR4FuvPNCXXHWmqjkZaO%2FfIZ8lmymRN1dCh92yGuFXjU9Ttr3Wh7dL4OOqlvv3lb1kWNMhzGD1mcLqpDAAk3kih7GhMNyS3dIGOqUBIHuuyavCZe3%2Bx2PjaRnMD6ecjSaFvSeRLGLxQAUNNflYKrhcVbqvZVceSKf9kTob43zELx0HIq6VZ3IkjvhPZapIk%2BsKaIIaha417ETgTFLHo0VeNJP%2B14a2uHaIa%2FIOT3tZNqR37bMIXuC6la2xn7JsXJ56rpJtwcgb1SUv2AGLWEE%2Fm5dVMXaIGUzInx37Ixms%2FIIQlV52dNAdOS2x%2B4hYs6wl&X-Amz-Signature=eccf1c036d6dca05a0cc2efeb1a52aae9c3a30c2abe3a2615a2f8b617cdf1191&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
