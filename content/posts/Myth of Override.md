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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUU25M6J%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T225511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ%2FKb5bXS%2BjUvoZweX4i5MHDKPimaKrWEFkbXo2tBSKwIgds%2FfaC0maf6g9EB0dcxq%2FW9qrL%2FpoyWKP9bOpg7IgR0qiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8FMbXVz1chOi1MZSrcA89HmL5DhybO6dnk1qWeH6a2hjyjOxbSKs8jlgxoTU0ZF0bd5bMo1NKvZj5DG1KSZva0hafHaN7k8eNjFe7FGwE%2B5T5qxia990yPwPEnyiUO0FddVeAwt%2FQ61is3y%2Btye1gBlcOgwewSHtO5N5SD9uS%2FWW08qiURPIMtuTkIfq%2B%2FIgDCMdGGv0tXsu9mlpLG8yUuZBJSz0scrVkEW47lQTym2GN6igxDfDUnKgoJcVnUMIjYK3zq1JM0wGKyE4rUfjExkWGPgLbbCUS1cbKS81JuzoIWX%2FqFpJ3nnFw4ysgOaa8KWn3ve%2Bw0CMNmquaqsqKgAUBTPLI%2BtocKvrMARQRjq5IlRsW%2FO%2FbHh4rkUAdeD3BgErikGtoANGqgEIewMmcCwqo%2FvQBrw3PDuwVncgzOCmp%2FQS%2FJtWAKWlRpyAyqg1zu6y0Bmv9j7woUYAeHg1mpS%2BlcxJhkPzxP%2FHu8%2FDaeMjLRf8ElfHv7%2FrhwcIVZSv479H411y8e09HcAWytwzNMSSa8cLpAHqlI4pcCtIL5kEsof2%2FQc8QBGWnzjJC%2BpFydWwN9gk%2Bi3sLwlOvlvtvWCFln76ykW98woxvN4RBHEs6ugH3aWGk%2FruWW0JCU6v6d0uHLm7Wm7gEZMISkr9MGOqUBYxZi0%2FusBcviSBOsVsuleH6tBronMeY0l%2FGgT85MCx5eblA7pD7gnai6oJHzUR4ABKKDxjWBDfkZ20RqJtSgJJh9LkY9STBXZBsHNDyPK8%2FXCyWNvl49S1kWkLM030R07zI3%2BHGu%2FP8%2BV5i%2B6K9XdcfKHH2g0FW43qKf%2BEK26H8QgCYgDJOzf%2BP4B0ZMIcQ8%2BZ1hWysY8yzCSUVKPGK%2F1j4Zfn9i&X-Amz-Signature=8ffa9ecffe77050131efb3784883b9ed47f43b95c17453542554c6ceacd9a97d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUU25M6J%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T225511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ%2FKb5bXS%2BjUvoZweX4i5MHDKPimaKrWEFkbXo2tBSKwIgds%2FfaC0maf6g9EB0dcxq%2FW9qrL%2FpoyWKP9bOpg7IgR0qiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8FMbXVz1chOi1MZSrcA89HmL5DhybO6dnk1qWeH6a2hjyjOxbSKs8jlgxoTU0ZF0bd5bMo1NKvZj5DG1KSZva0hafHaN7k8eNjFe7FGwE%2B5T5qxia990yPwPEnyiUO0FddVeAwt%2FQ61is3y%2Btye1gBlcOgwewSHtO5N5SD9uS%2FWW08qiURPIMtuTkIfq%2B%2FIgDCMdGGv0tXsu9mlpLG8yUuZBJSz0scrVkEW47lQTym2GN6igxDfDUnKgoJcVnUMIjYK3zq1JM0wGKyE4rUfjExkWGPgLbbCUS1cbKS81JuzoIWX%2FqFpJ3nnFw4ysgOaa8KWn3ve%2Bw0CMNmquaqsqKgAUBTPLI%2BtocKvrMARQRjq5IlRsW%2FO%2FbHh4rkUAdeD3BgErikGtoANGqgEIewMmcCwqo%2FvQBrw3PDuwVncgzOCmp%2FQS%2FJtWAKWlRpyAyqg1zu6y0Bmv9j7woUYAeHg1mpS%2BlcxJhkPzxP%2FHu8%2FDaeMjLRf8ElfHv7%2FrhwcIVZSv479H411y8e09HcAWytwzNMSSa8cLpAHqlI4pcCtIL5kEsof2%2FQc8QBGWnzjJC%2BpFydWwN9gk%2Bi3sLwlOvlvtvWCFln76ykW98woxvN4RBHEs6ugH3aWGk%2FruWW0JCU6v6d0uHLm7Wm7gEZMISkr9MGOqUBYxZi0%2FusBcviSBOsVsuleH6tBronMeY0l%2FGgT85MCx5eblA7pD7gnai6oJHzUR4ABKKDxjWBDfkZ20RqJtSgJJh9LkY9STBXZBsHNDyPK8%2FXCyWNvl49S1kWkLM030R07zI3%2BHGu%2FP8%2BV5i%2B6K9XdcfKHH2g0FW43qKf%2BEK26H8QgCYgDJOzf%2BP4B0ZMIcQ8%2BZ1hWysY8yzCSUVKPGK%2F1j4Zfn9i&X-Amz-Signature=047649a733f6c4e196e0b43c13dd5fcfe0056efafda86f4b87f98dbb47054c58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
