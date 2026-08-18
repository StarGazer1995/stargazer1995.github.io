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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMYEC7J5%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T042356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH4vT%2FR%2FwiUoecYmevSfHmqMKOeR0lSmanpg%2FC1it7vNAiEAgrprUs2jlTmRN1htDAniYLup4uEeCFoWjQEoiqzCMP0q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDAgGdLym%2FBIoqKaF6CrcAwiSJhv5nb%2Bd6YIWiNKJiZsDKx2Ey%2FEuUbzalrO9tXyw%2FLwWMjU5hz7gRDanrQNZKbZrMnVpmXO7gsWHA2V29n4SbvGnNq7r8K60zmKQfQTRlezWNUxBh5qH%2BFdFtmbeDJbatCmy37EBbI%2FJYdnMX9T4LIYvsnqprM%2BG%2FF5wADuFeA76R0VtMA%2Bm%2BTA%2FqBMmVFMzfajS90X4YDfws%2BMAkokNbyZBU9OSDzPg%2BFnA820tJEpqpmJexxeL7xgYenQQIOECBWyKfN75XfrA%2FKM3g%2B62APgdyMHdzIDGJxfWeIzWHWCXU%2FCEwohJpVRKftH6HVWPU%2FO1AWSiXSSyGft1ooRJsvkE%2F6ULDqVUAcsOBYMt8813epMb7XWRlv9ukp5mN5KSwnt0U4r3xnjdX4XkbDVHpNeqf7uu1LYRCIxe8x82vYNRP7uNc2Yix9YZGLlMoh3j%2F3tmzjH67XHg06EGndzHZpsbESKegB8XFcIYfiYvORfULUvlPtUemCP6492wK0l5HGcD40x3pzqsg%2BHr2jrY6%2BY0dQ6myNQfmlRRke4WeGewqSrTx0dyI9fxn4ZcM0rQ3azaZDlBsxKCRiQ%2FVAncp%2BJ7RLCIqvI0QwvX0ldNkLc2cR6piMMYQ9jhMOeyj9QGOqUBc7%2F5zRhk%2BJ%2F%2FT7dYrEc%2Fc5zqJ%2F8GPBVmdo1NULjwKLdxH4huFq8N%2B74uj4R8pkCJTialU2yXcowhEVfAz9bX%2BqziDxURET2TGGcy7S8BxK2jpHEeDfAeNy%2BdS%2FMI39UuleHZ1ifZZpAcDcva9p82lNhn3IxHlrltWEt1Uj0bhVpIUaPSDBnw0ux3cY0apYNcqecv%2BrVUd9kcKcZCF4xwjKJNK7GO&X-Amz-Signature=cbec867f9224b879ab6741bb381a29b97a889cc368fe4df79679ce75a006535d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMYEC7J5%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T042356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH4vT%2FR%2FwiUoecYmevSfHmqMKOeR0lSmanpg%2FC1it7vNAiEAgrprUs2jlTmRN1htDAniYLup4uEeCFoWjQEoiqzCMP0q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDAgGdLym%2FBIoqKaF6CrcAwiSJhv5nb%2Bd6YIWiNKJiZsDKx2Ey%2FEuUbzalrO9tXyw%2FLwWMjU5hz7gRDanrQNZKbZrMnVpmXO7gsWHA2V29n4SbvGnNq7r8K60zmKQfQTRlezWNUxBh5qH%2BFdFtmbeDJbatCmy37EBbI%2FJYdnMX9T4LIYvsnqprM%2BG%2FF5wADuFeA76R0VtMA%2Bm%2BTA%2FqBMmVFMzfajS90X4YDfws%2BMAkokNbyZBU9OSDzPg%2BFnA820tJEpqpmJexxeL7xgYenQQIOECBWyKfN75XfrA%2FKM3g%2B62APgdyMHdzIDGJxfWeIzWHWCXU%2FCEwohJpVRKftH6HVWPU%2FO1AWSiXSSyGft1ooRJsvkE%2F6ULDqVUAcsOBYMt8813epMb7XWRlv9ukp5mN5KSwnt0U4r3xnjdX4XkbDVHpNeqf7uu1LYRCIxe8x82vYNRP7uNc2Yix9YZGLlMoh3j%2F3tmzjH67XHg06EGndzHZpsbESKegB8XFcIYfiYvORfULUvlPtUemCP6492wK0l5HGcD40x3pzqsg%2BHr2jrY6%2BY0dQ6myNQfmlRRke4WeGewqSrTx0dyI9fxn4ZcM0rQ3azaZDlBsxKCRiQ%2FVAncp%2BJ7RLCIqvI0QwvX0ldNkLc2cR6piMMYQ9jhMOeyj9QGOqUBc7%2F5zRhk%2BJ%2F%2FT7dYrEc%2Fc5zqJ%2F8GPBVmdo1NULjwKLdxH4huFq8N%2B74uj4R8pkCJTialU2yXcowhEVfAz9bX%2BqziDxURET2TGGcy7S8BxK2jpHEeDfAeNy%2BdS%2FMI39UuleHZ1ifZZpAcDcva9p82lNhn3IxHlrltWEt1Uj0bhVpIUaPSDBnw0ux3cY0apYNcqecv%2BrVUd9kcKcZCF4xwjKJNK7GO&X-Amz-Signature=e7d472e45f773342ba1540c55915f315609a01379d4d284c52e01b705fe9eb6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
