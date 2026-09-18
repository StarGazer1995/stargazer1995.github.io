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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655QELRQV%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T064908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQDfx4zZNqf8U6wjZ%2Bkl1UCcYd48iZhQ3KZLdVYEYyFX5gIhAOzSHxLpF8AKmvhLt41tQKhnwD6AEV4Gun3zKCl6t56oKv8DCD0QABoMNjM3NDIzMTgzODA1IgzRAaoyBQLGxiyWDHoq3AML5ZXkAuYJei4Zaobv2KMpP8uMlz3zQx1mGRzfWWZyigVDW3%2BNK%2FlP%2FTcgNTJU34hrVvaKQxSjuTSaOgb2UzlRnD8F7r6FO9%2Fdaw4y9C955hrAB6blVeEBK7hg4%2B1oBpymT703MWPWipYOEJ15kDZ9tCy52M4KPQAZNVd%2FK%2BK9kXXAN%2FlRGfZj9moPJMxA6qDC%2BbwalCVMwIb%2FnuRmVfNjPl8BwRpyORAT7XGV5pYUoR95%2BuhOPxdhiIfoBfTc%2FfAjJfIxH1D5ec%2F0LJ5FROLHYvaeU5P9NQeDWcNsK%2FozCQ8MdyCliY%2BuaZLrA376%2BOF9cWSCy8Ej0fhP04ARiU44ytPL8w09ql5xM2UHMlVZ4k8Nms%2FLpGmOAJU8yoIUxMOsoZ%2BkPkgBxQwTo5W7Ay7toCROFiY1xT7QU9cNlngZwU%2FxWG3RGnW3quCF%2BDKpiqZbq3n0Mi8rTkURjUKxvcbuSSeC9CUvvTjuDC3D%2FC%2BNS9uzcgVl5nLX116Ekk8oGJwywflj1VUJgcin7wJIJxK4f0ImFUu8h%2FKfZB0KSkKfxMBLH1OXUKlAX1hWfHxpBZE0p7%2Bvqxlb3qziX5zPt1NxRvCgH2qrLacF68aZCV2Z4EiAaOku6Bnthv8tXDDC97LVBjqkAUJ1rJ4LQaEwQLEdzWzmKTpQy2cDHnFR96oZt9gqdGkqbOsQG1BW%2FRy2OCkqmmN3gfn41zT%2FiEv51tuyqY9gIuCCylegkFcvNArDBc0sDO3%2FO%2BfGOFl7gRrmRXcp6vm2Inje02XyBLSc%2FVcBl51tZXMSNoih5FN8ZylF9d6YXfBmeTHuwRCxUFnpnDlLJZSQztq299fmrZRQTFjkk5Rhy%2B0JggvN&X-Amz-Signature=557c3f5a8d5802dfdf135023f300d2ceb084858ab1f7feb4cc9e824d55a4a5f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655QELRQV%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T064908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQDfx4zZNqf8U6wjZ%2Bkl1UCcYd48iZhQ3KZLdVYEYyFX5gIhAOzSHxLpF8AKmvhLt41tQKhnwD6AEV4Gun3zKCl6t56oKv8DCD0QABoMNjM3NDIzMTgzODA1IgzRAaoyBQLGxiyWDHoq3AML5ZXkAuYJei4Zaobv2KMpP8uMlz3zQx1mGRzfWWZyigVDW3%2BNK%2FlP%2FTcgNTJU34hrVvaKQxSjuTSaOgb2UzlRnD8F7r6FO9%2Fdaw4y9C955hrAB6blVeEBK7hg4%2B1oBpymT703MWPWipYOEJ15kDZ9tCy52M4KPQAZNVd%2FK%2BK9kXXAN%2FlRGfZj9moPJMxA6qDC%2BbwalCVMwIb%2FnuRmVfNjPl8BwRpyORAT7XGV5pYUoR95%2BuhOPxdhiIfoBfTc%2FfAjJfIxH1D5ec%2F0LJ5FROLHYvaeU5P9NQeDWcNsK%2FozCQ8MdyCliY%2BuaZLrA376%2BOF9cWSCy8Ej0fhP04ARiU44ytPL8w09ql5xM2UHMlVZ4k8Nms%2FLpGmOAJU8yoIUxMOsoZ%2BkPkgBxQwTo5W7Ay7toCROFiY1xT7QU9cNlngZwU%2FxWG3RGnW3quCF%2BDKpiqZbq3n0Mi8rTkURjUKxvcbuSSeC9CUvvTjuDC3D%2FC%2BNS9uzcgVl5nLX116Ekk8oGJwywflj1VUJgcin7wJIJxK4f0ImFUu8h%2FKfZB0KSkKfxMBLH1OXUKlAX1hWfHxpBZE0p7%2Bvqxlb3qziX5zPt1NxRvCgH2qrLacF68aZCV2Z4EiAaOku6Bnthv8tXDDC97LVBjqkAUJ1rJ4LQaEwQLEdzWzmKTpQy2cDHnFR96oZt9gqdGkqbOsQG1BW%2FRy2OCkqmmN3gfn41zT%2FiEv51tuyqY9gIuCCylegkFcvNArDBc0sDO3%2FO%2BfGOFl7gRrmRXcp6vm2Inje02XyBLSc%2FVcBl51tZXMSNoih5FN8ZylF9d6YXfBmeTHuwRCxUFnpnDlLJZSQztq299fmrZRQTFjkk5Rhy%2B0JggvN&X-Amz-Signature=7640bee084fad9819d5beb3dcb9c75b59f27ab98809958442f66b33927aeaeba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
