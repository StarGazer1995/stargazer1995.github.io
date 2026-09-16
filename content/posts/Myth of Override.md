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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO56GGDG%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T020156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGZJyzRC3g19uYClnVNCCfeIiEYvdT9BGeG1SuLBQk9fAiAyt0zVi2qP%2F78dm9H94VhGo4lWld5ZNtUCYsGKfVdVcir%2FAwgKEAAaDDYzNzQyMzE4MzgwNSIMUtt0p2nRjViy1mAWKtwD9u5s0uRhapOh05riLQ79N5KgprhdMsm38nSikprx2GM9kc3P7Jl96peJFcoamhbNbA5ZgHP%2BiQlsQO1f4xRoa6E3lCvpKOUEfySFJiXuKUf7QiDXyqYM8PYvDoeeKran8kk2K5zI2dBb8ulMCvQdnC%2Bh13Wgp4DDpu8VeqEhZlwC4Ywgg6iGPxgxKk6x2zFuXtA3SGCb%2F68XJAJqI%2Fm4kbbE2lVCnC0hqbms5YCN6UBi4AeWFKSt459aKg9uT8nTgimgT50xe0jNM93tyr23uxOpqUKuPuzIcEyLFO6xJu0UVU1%2FiaHb5%2BuOh7ZnjJH%2FTD9AxFn3EkfKr%2F%2Fu9MSg%2B%2FA2PhQmUJX7ghcn3EN5koY2hSNTL5R5Zs%2BFw%2FruEVNYd07tFs5nFGNIpanDmJyffihPwgWQu4%2BilmhaVY6XkOzJZa6c7P%2FG04jb2bJZKG8MnxPkKUpOcQsJmphoDANRRHRICBr5lRHmG3J2YCS%2FQgpUnc35nKuGfCQBvYq5th8PT23dxDCDwywj9B3kGMfZVMRP0sWzbY8lNpImtHrZw3ANOgROCObVmsAEkaxLlRPi69lTjnsYYerx9gN1%2BdgfH3IqS923CQ7IoBFn0Mbxmap9M6FKwZdEIWiKIeMwwcmn1QY6pgGV6yL4VDnt%2BB0TQON%2FGtKJ%2B3YPXQCusj33YJ8isZIuYU36sQMD3UABe6NpxZn5R0CXQmSEcHxHciGUhBj253oOXOeLb6wLWwT46wkt493q9oN9ZRhosp2J172pJVoKA93Z%2BwuDN1vNmPeavG0Dlsh4l%2Bwpj09z6ZR%2BdlaS82F1BzlfwKdKs3su8f1bXK48NH6Dt73n7HBQ%2BchzWNP%2BGeEG32GMCPuf&X-Amz-Signature=dfa0f02b6674bb993ca46803dd03c36a7727b12abc536fce0f63051017bffadf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO56GGDG%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T020156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGZJyzRC3g19uYClnVNCCfeIiEYvdT9BGeG1SuLBQk9fAiAyt0zVi2qP%2F78dm9H94VhGo4lWld5ZNtUCYsGKfVdVcir%2FAwgKEAAaDDYzNzQyMzE4MzgwNSIMUtt0p2nRjViy1mAWKtwD9u5s0uRhapOh05riLQ79N5KgprhdMsm38nSikprx2GM9kc3P7Jl96peJFcoamhbNbA5ZgHP%2BiQlsQO1f4xRoa6E3lCvpKOUEfySFJiXuKUf7QiDXyqYM8PYvDoeeKran8kk2K5zI2dBb8ulMCvQdnC%2Bh13Wgp4DDpu8VeqEhZlwC4Ywgg6iGPxgxKk6x2zFuXtA3SGCb%2F68XJAJqI%2Fm4kbbE2lVCnC0hqbms5YCN6UBi4AeWFKSt459aKg9uT8nTgimgT50xe0jNM93tyr23uxOpqUKuPuzIcEyLFO6xJu0UVU1%2FiaHb5%2BuOh7ZnjJH%2FTD9AxFn3EkfKr%2F%2Fu9MSg%2B%2FA2PhQmUJX7ghcn3EN5koY2hSNTL5R5Zs%2BFw%2FruEVNYd07tFs5nFGNIpanDmJyffihPwgWQu4%2BilmhaVY6XkOzJZa6c7P%2FG04jb2bJZKG8MnxPkKUpOcQsJmphoDANRRHRICBr5lRHmG3J2YCS%2FQgpUnc35nKuGfCQBvYq5th8PT23dxDCDwywj9B3kGMfZVMRP0sWzbY8lNpImtHrZw3ANOgROCObVmsAEkaxLlRPi69lTjnsYYerx9gN1%2BdgfH3IqS923CQ7IoBFn0Mbxmap9M6FKwZdEIWiKIeMwwcmn1QY6pgGV6yL4VDnt%2BB0TQON%2FGtKJ%2B3YPXQCusj33YJ8isZIuYU36sQMD3UABe6NpxZn5R0CXQmSEcHxHciGUhBj253oOXOeLb6wLWwT46wkt493q9oN9ZRhosp2J172pJVoKA93Z%2BwuDN1vNmPeavG0Dlsh4l%2Bwpj09z6ZR%2BdlaS82F1BzlfwKdKs3su8f1bXK48NH6Dt73n7HBQ%2BchzWNP%2BGeEG32GMCPuf&X-Amz-Signature=c70770e019e133f51f12336acf2c18546224df8fb99456d9f17abbcda515d4f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
