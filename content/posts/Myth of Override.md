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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S43PCDFR%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T163209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDuUHdc%2FCtZgae1w0VnmxzxZi3n5i%2B01iT5pnV6yDSKGAIhAMQuk2F0xJp74FLKk5TGJrsGVvqvPO6QwDXo35UN%2FfLmKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUUCYyEUxUrb27hMEq3AO9PtpWyU%2BVBub94n%2FtvR4Glbo4dhTC8%2FLAkmHmMBOjaMobwm437gjF9LQFL9NvZSbej5dpFytElHcijA6AOH4GBRY9KHDylI0uIWTiDXMBM%2F7bx8pcI6UEqOY7SUBxFTfydn1t3kOm2L3NU5VBF07ku0qvMk1URlrzBUYRFF2VO86zxqJPQloQZG%2BpUq0LfRLaBuf5qk52kU76tS76dzKUrfZspcsTSxQbsrUdY2KNUPQ%2Bs0MqI%2Fxl1O6HSC1W0dy8vBTSYJ3IFpNFyh6aTCregvNuondztlZ6%2BBj%2FUNGTowQJJGFACLN0sLal0JIp9k7zbyt8oE%2B6peqenMMLkME72RKvCsVlVOBY66xvUNxZpcPhUzbSsKI6spAU9ovHFa%2B%2B7wmtJ8XudB6GeyP8CXPGBQAyBbFw5UYpQFt59bzi1rcpRbMldxqXwDy%2FdJTij%2BwpO56cXvXjZLNQaMp6AqS7QWfDKJkjUelsqwGhhlDanYmr%2BjFqZV5FI0AO6yWe9UQTr40jZo58SxWegevydHN74Xn7gq84j4HqbxeiQycAYjhSU3HZZLB1OVig13g2ZzWz7epJyMX%2BNh6QvUf11gdjfyNdfcJP23OIzJOer%2Ft0qaqeJowTtdv%2BwhQ9ejDw9I7WBjqkAfh%2F6biiN2HNvkB31sBwOwI0ZcqEPmEkGfPI5tWGELDHyBBu24vE2LWi%2ByOx%2BWOfodRKb6DuMoEqMyYwcDYakyik4pzO%2BCXVKXxp849Aq1%2B%2Fx0VF1qzM5rDk1YZwb6LwFntawho1lBtIktbWkgwMvMv3fsCLujoIg6i74JY39WpFoQY0xtPAjnXOXrS6mxSpHhk7fZkGR64grHSXvrzwqd3s8JF5&X-Amz-Signature=f8fc29ff7d4142b8c50773bc99da3dcecaff48fdd110d2522860772639ed5a3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S43PCDFR%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T163209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDuUHdc%2FCtZgae1w0VnmxzxZi3n5i%2B01iT5pnV6yDSKGAIhAMQuk2F0xJp74FLKk5TGJrsGVvqvPO6QwDXo35UN%2FfLmKogECOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUUCYyEUxUrb27hMEq3AO9PtpWyU%2BVBub94n%2FtvR4Glbo4dhTC8%2FLAkmHmMBOjaMobwm437gjF9LQFL9NvZSbej5dpFytElHcijA6AOH4GBRY9KHDylI0uIWTiDXMBM%2F7bx8pcI6UEqOY7SUBxFTfydn1t3kOm2L3NU5VBF07ku0qvMk1URlrzBUYRFF2VO86zxqJPQloQZG%2BpUq0LfRLaBuf5qk52kU76tS76dzKUrfZspcsTSxQbsrUdY2KNUPQ%2Bs0MqI%2Fxl1O6HSC1W0dy8vBTSYJ3IFpNFyh6aTCregvNuondztlZ6%2BBj%2FUNGTowQJJGFACLN0sLal0JIp9k7zbyt8oE%2B6peqenMMLkME72RKvCsVlVOBY66xvUNxZpcPhUzbSsKI6spAU9ovHFa%2B%2B7wmtJ8XudB6GeyP8CXPGBQAyBbFw5UYpQFt59bzi1rcpRbMldxqXwDy%2FdJTij%2BwpO56cXvXjZLNQaMp6AqS7QWfDKJkjUelsqwGhhlDanYmr%2BjFqZV5FI0AO6yWe9UQTr40jZo58SxWegevydHN74Xn7gq84j4HqbxeiQycAYjhSU3HZZLB1OVig13g2ZzWz7epJyMX%2BNh6QvUf11gdjfyNdfcJP23OIzJOer%2Ft0qaqeJowTtdv%2BwhQ9ejDw9I7WBjqkAfh%2F6biiN2HNvkB31sBwOwI0ZcqEPmEkGfPI5tWGELDHyBBu24vE2LWi%2ByOx%2BWOfodRKb6DuMoEqMyYwcDYakyik4pzO%2BCXVKXxp849Aq1%2B%2Fx0VF1qzM5rDk1YZwb6LwFntawho1lBtIktbWkgwMvMv3fsCLujoIg6i74JY39WpFoQY0xtPAjnXOXrS6mxSpHhk7fZkGR64grHSXvrzwqd3s8JF5&X-Amz-Signature=7308d3070c83e67351d48cd0400346e5ce02cd91365e87a79b10058d33bbd6fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
