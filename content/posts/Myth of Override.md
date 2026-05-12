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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665TACNJC%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T161237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIA7Bs1lJAk4TKl0NLi4MxZf0zHk3WA17HhTapULF2hmrAiBEu4kr8UHMY2dIuwMcXxuuVz%2BYV7eIbrO%2FAojD8sphfCr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM8kqNlfsUQVL71suaKtwDD1L%2Fe6M7xt%2BLp4dq%2Fp0kq5pKrZYZ9aG3dzZ9%2BAMMoHmtUFA3pmPfWaAxdvGiktZ2RSCG9qCPFLOhwPVZBzVW9t4iTes1bVD1zH7OrkJwE7P%2BiyZOZYepfKSNMlHvckCL2KqmWVg7b1dHPLz%2FWPZgCrxXrj8rYgzMSKgwUjPCdRXMmslekqmnod%2FPBLHxoXNsi9VNQdo80EYqKX7V5majqV2Ik8nVNWG%2FgcdPyafPLYLhucPVgUx3115zhpNYg4GGA%2FkOooJhrYuyqXJyqM%2FLGtT278t%2FZecytc7acU24q3XCRDVbpk7QURfxIYyTUMEn8Kg7O3%2BrdAyh8tZD8yiAWC7uISZEjdkEGau4HY4zLeO%2Fh%2BwmWT0eY0KApyxllPW7iXOZjSqQwRb%2BjrnRNj5K4bukqi1y3gUjIatdC6xXyHI8mLZ98XPwQGeNf%2FYx2gIxvBndDTQWpYkBlXQm6rkR7aZXKgBT%2BaOz6FfOhRtg5NagoD964Y56AeyIb7Sp9qkPPEdbGzu1LttIuJ07Uwd5AptMsyQSNX6a8id%2B0Lg4PkedPsS%2FHYgoKEqk%2BMidcfgdjLKHGOA7%2FReg0da9pJP436t8TwwWp0dRzM9dB3T49ho53735EK7cMzanp3wwuJyN0AY6pgH%2FInT3Iy30SU9JTnCkuXOTXYAWOUMXP80HypXWnXwkgIssTxuTaG4oNPzt1crbYxI60mXx1392A%2Fypr9ZsPnNBRieAXlGgnyHeyF5ywLlS%2BhtIjltvxxTluywp7qbvFoAibaAx1P2nl00ufSUO81X8BDiDJrsYqXcCxTNyMuHEHEKjLx4%2Ff933J4ATSdGBYt9VLSVHWyjzWkSrOh3%2BXfpYxd7qSZZs&X-Amz-Signature=70c65258f9ca416c11e4d36b6b20bfde757aecf9ed692384ca643c5acc8b66d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665TACNJC%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T161237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIA7Bs1lJAk4TKl0NLi4MxZf0zHk3WA17HhTapULF2hmrAiBEu4kr8UHMY2dIuwMcXxuuVz%2BYV7eIbrO%2FAojD8sphfCr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM8kqNlfsUQVL71suaKtwDD1L%2Fe6M7xt%2BLp4dq%2Fp0kq5pKrZYZ9aG3dzZ9%2BAMMoHmtUFA3pmPfWaAxdvGiktZ2RSCG9qCPFLOhwPVZBzVW9t4iTes1bVD1zH7OrkJwE7P%2BiyZOZYepfKSNMlHvckCL2KqmWVg7b1dHPLz%2FWPZgCrxXrj8rYgzMSKgwUjPCdRXMmslekqmnod%2FPBLHxoXNsi9VNQdo80EYqKX7V5majqV2Ik8nVNWG%2FgcdPyafPLYLhucPVgUx3115zhpNYg4GGA%2FkOooJhrYuyqXJyqM%2FLGtT278t%2FZecytc7acU24q3XCRDVbpk7QURfxIYyTUMEn8Kg7O3%2BrdAyh8tZD8yiAWC7uISZEjdkEGau4HY4zLeO%2Fh%2BwmWT0eY0KApyxllPW7iXOZjSqQwRb%2BjrnRNj5K4bukqi1y3gUjIatdC6xXyHI8mLZ98XPwQGeNf%2FYx2gIxvBndDTQWpYkBlXQm6rkR7aZXKgBT%2BaOz6FfOhRtg5NagoD964Y56AeyIb7Sp9qkPPEdbGzu1LttIuJ07Uwd5AptMsyQSNX6a8id%2B0Lg4PkedPsS%2FHYgoKEqk%2BMidcfgdjLKHGOA7%2FReg0da9pJP436t8TwwWp0dRzM9dB3T49ho53735EK7cMzanp3wwuJyN0AY6pgH%2FInT3Iy30SU9JTnCkuXOTXYAWOUMXP80HypXWnXwkgIssTxuTaG4oNPzt1crbYxI60mXx1392A%2Fypr9ZsPnNBRieAXlGgnyHeyF5ywLlS%2BhtIjltvxxTluywp7qbvFoAibaAx1P2nl00ufSUO81X8BDiDJrsYqXcCxTNyMuHEHEKjLx4%2Ff933J4ATSdGBYt9VLSVHWyjzWkSrOh3%2BXfpYxd7qSZZs&X-Amz-Signature=6a062fceff98ddae274bf398c52e420d21de3c9e1c4a201b8e1e703e9a36846f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
