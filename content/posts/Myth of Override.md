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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SONYQYX%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T084511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEmg%2FlvHqE6Bn1eDS2AYBn9BrZm%2F3pSKybq00ZvJgr7QIhAOYCi7w2W40CUbS%2FvqG4uq%2FRavO6Ab0c%2FggZee%2FFp%2FdMKv8DCFEQABoMNjM3NDIzMTgzODA1Igyw1Irq9wmjWpM6wTEq3APV1aKixXPCKxgtDiS4MqJNr%2BeOU1uTm0FRiipuYiUshCXg7LhcmDpgscLm0dzxgCSMEtAEdCtcGnUXdsfOzT8Cj5mb2UFDW1u9LwhBUJl1Cn2e9wfQNAHuRM%2FptVtk89ke8hSUjk4N%2FT6zxqTR3F%2F6SZ9%2FZLYRp2Br23BuW%2B3vsyHfVd1K8UpjYSMmo46RB5srB6H%2FzxowPkbeJtTD3sHFOSy27QCDb8ehULoKxJuz%2B8TNvJQzNDoFmmrQB0FSPW3p2S97tGWHoDdYD7CRlGTqBWP9ffApb2FXzykGPiO6X3e235T1ZQ3tP0HeDnLL8lsn%2BkED0oCL8KIH5LGnaMznikocWzZQsjXjZ3eKNT%2BAGBN4ieA2FRKDzSWhxHVnHNUEU3lFQL0DDm1kBzL%2BELuZwlBb9awu706AH%2Fitl0pZfPffEkFOQLqVy90q5qC5YF50lECyI76lSMC7YVTjXtIeiOAmqia93ludn7tD%2Ff30bAF8khuiawNRVkFRQ6HmZUBlQuDiJnCFsFbUacbKl7wRkkvgyoFtPcHDvJH38qX8RFjSMUZDN0zWQ%2Bv9pgVF6YvkFt5WJL3bhBc0HaOR3Zpb0ga%2FYTIER2vrJQ9K3YFRX0SRYZXDLHBFqtMP9TC%2BkNbTBjqkATffA7EyV9tutM%2B6FqVBOVVZfKz3q%2BEwm0ayPcmzsdna2vr222OGssmmWtE0KpyVU8jNytXY3U2G6gmkgmFRX%2BmWThjpmECoI53oMhSCS6PTlSCy%2FxCaHWQjnk7Un1rocDM21NdtbXfmzwQ4LuOQGkNEyrEqjjBzFs1%2Fbw3laqlpRYTgqZcHbavaRKO2KQy0BNM8GwkSRgZSHB9QyxHKsq3dek%2B8&X-Amz-Signature=a4a077d239dae1b2df8ad418688c2d59e909665737570e4ceaadaaa9c3b2fe29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SONYQYX%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T084511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEmg%2FlvHqE6Bn1eDS2AYBn9BrZm%2F3pSKybq00ZvJgr7QIhAOYCi7w2W40CUbS%2FvqG4uq%2FRavO6Ab0c%2FggZee%2FFp%2FdMKv8DCFEQABoMNjM3NDIzMTgzODA1Igyw1Irq9wmjWpM6wTEq3APV1aKixXPCKxgtDiS4MqJNr%2BeOU1uTm0FRiipuYiUshCXg7LhcmDpgscLm0dzxgCSMEtAEdCtcGnUXdsfOzT8Cj5mb2UFDW1u9LwhBUJl1Cn2e9wfQNAHuRM%2FptVtk89ke8hSUjk4N%2FT6zxqTR3F%2F6SZ9%2FZLYRp2Br23BuW%2B3vsyHfVd1K8UpjYSMmo46RB5srB6H%2FzxowPkbeJtTD3sHFOSy27QCDb8ehULoKxJuz%2B8TNvJQzNDoFmmrQB0FSPW3p2S97tGWHoDdYD7CRlGTqBWP9ffApb2FXzykGPiO6X3e235T1ZQ3tP0HeDnLL8lsn%2BkED0oCL8KIH5LGnaMznikocWzZQsjXjZ3eKNT%2BAGBN4ieA2FRKDzSWhxHVnHNUEU3lFQL0DDm1kBzL%2BELuZwlBb9awu706AH%2Fitl0pZfPffEkFOQLqVy90q5qC5YF50lECyI76lSMC7YVTjXtIeiOAmqia93ludn7tD%2Ff30bAF8khuiawNRVkFRQ6HmZUBlQuDiJnCFsFbUacbKl7wRkkvgyoFtPcHDvJH38qX8RFjSMUZDN0zWQ%2Bv9pgVF6YvkFt5WJL3bhBc0HaOR3Zpb0ga%2FYTIER2vrJQ9K3YFRX0SRYZXDLHBFqtMP9TC%2BkNbTBjqkATffA7EyV9tutM%2B6FqVBOVVZfKz3q%2BEwm0ayPcmzsdna2vr222OGssmmWtE0KpyVU8jNytXY3U2G6gmkgmFRX%2BmWThjpmECoI53oMhSCS6PTlSCy%2FxCaHWQjnk7Un1rocDM21NdtbXfmzwQ4LuOQGkNEyrEqjjBzFs1%2Fbw3laqlpRYTgqZcHbavaRKO2KQy0BNM8GwkSRgZSHB9QyxHKsq3dek%2B8&X-Amz-Signature=ab425e95a659a79c1fe08b855f3ba73fddfc53fbf9cd9761094c7c2df45beb62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
