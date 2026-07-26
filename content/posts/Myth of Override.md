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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH4BYNTL%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T111317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFVWb%2B6%2BbTMhNT6BBxi9cG1Oi%2Bz%2Fuzx1%2BGYFjg13tYK9AiEA%2FOVPnTuRviu00f1%2FB5P7A5Hw02LFKNdaWulvOfv5YE4q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDKGUkb7IVhhszgKqQSrcA0BmclTLEP8b%2FUtTr2xWaRszLwBhe2pZ6J3tFQIsVIr25XZfltqqKWZkyKVWBSLNP%2F%2BLLTN5mzq1v9aswM5F7rb56xshAWGvt%2BNtxMoijt1XpX8yOChEiJGOguYkZPQQUjJ9MJJ4EZ%2Fc%2FZw5icmvWTsBNZLq%2BgzEzRQqZdIDM%2BLWSlPwClLXFPJ4u1Bq%2BuiVSuWN%2B98VPMMEleqB%2FDe9tq5MAmnYufUBrKS4syw6titFvkZ01WI7x%2BOxnI9p%2BSMt23w4blEeqmzoSoHt4QOedyex9rqPH%2BQGAcSp0o6Z5QYWdxu2YGdvyhRHYIDQjlYAi9RSXUQrwxNgWipSNBGZCGQSrs0D9RI%2Fm86AAX4WdJc9TjplHnXb0yinx4X3UMXkUxISWZ%2BCoA8cwTlDAyHAcV3BZV%2FK%2FOLt7DjMthqa%2BIdHmJymCcAkgxDnqAZqwtNtChbbTewHqNTRfWI7BjaZAlT6RBrPJEJWBfvS1LmkLOjT4UnfxIm%2B0ARiBqEIvCpGHrl9NdhP96l%2B93ZJqwBXym836lvEqV0QqE%2FY5P8QSGUWkzUC9SFDyGJ1e%2BsyLWEkZ5gr3kesLC0b509%2Fax03iim9aVJB%2FEVciesQ%2F50OAZeTN8vJj%2Fe6OZGiPMzVMLHIl9MGOqUB%2BhAEPH3Pg7i9zNhXsJi7ov5PJsjJ5zzMai7RWaXt2BSjo5RcdqMJWmxtR2RUtHaJ66ux4kkt%2BxFLiliFLsfM5ps1De9ToQOsEZIc90NNyLfyye4pjvVLCBsHyGdTs0XRzHDNTCTj8aJY1dgvBBpm9JzUcD%2FvPcWWnLZqfECft5QCio2Uuwg5GNpwkXhsB05xQagz92mvhD%2By2jUIcqSDPoL5LTEd&X-Amz-Signature=97aa971daa49135d6221e62aef3bb19ac70b1e5d2816de13c9271db6c11ea361&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH4BYNTL%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T111317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFVWb%2B6%2BbTMhNT6BBxi9cG1Oi%2Bz%2Fuzx1%2BGYFjg13tYK9AiEA%2FOVPnTuRviu00f1%2FB5P7A5Hw02LFKNdaWulvOfv5YE4q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDKGUkb7IVhhszgKqQSrcA0BmclTLEP8b%2FUtTr2xWaRszLwBhe2pZ6J3tFQIsVIr25XZfltqqKWZkyKVWBSLNP%2F%2BLLTN5mzq1v9aswM5F7rb56xshAWGvt%2BNtxMoijt1XpX8yOChEiJGOguYkZPQQUjJ9MJJ4EZ%2Fc%2FZw5icmvWTsBNZLq%2BgzEzRQqZdIDM%2BLWSlPwClLXFPJ4u1Bq%2BuiVSuWN%2B98VPMMEleqB%2FDe9tq5MAmnYufUBrKS4syw6titFvkZ01WI7x%2BOxnI9p%2BSMt23w4blEeqmzoSoHt4QOedyex9rqPH%2BQGAcSp0o6Z5QYWdxu2YGdvyhRHYIDQjlYAi9RSXUQrwxNgWipSNBGZCGQSrs0D9RI%2Fm86AAX4WdJc9TjplHnXb0yinx4X3UMXkUxISWZ%2BCoA8cwTlDAyHAcV3BZV%2FK%2FOLt7DjMthqa%2BIdHmJymCcAkgxDnqAZqwtNtChbbTewHqNTRfWI7BjaZAlT6RBrPJEJWBfvS1LmkLOjT4UnfxIm%2B0ARiBqEIvCpGHrl9NdhP96l%2B93ZJqwBXym836lvEqV0QqE%2FY5P8QSGUWkzUC9SFDyGJ1e%2BsyLWEkZ5gr3kesLC0b509%2Fax03iim9aVJB%2FEVciesQ%2F50OAZeTN8vJj%2Fe6OZGiPMzVMLHIl9MGOqUB%2BhAEPH3Pg7i9zNhXsJi7ov5PJsjJ5zzMai7RWaXt2BSjo5RcdqMJWmxtR2RUtHaJ66ux4kkt%2BxFLiliFLsfM5ps1De9ToQOsEZIc90NNyLfyye4pjvVLCBsHyGdTs0XRzHDNTCTj8aJY1dgvBBpm9JzUcD%2FvPcWWnLZqfECft5QCio2Uuwg5GNpwkXhsB05xQagz92mvhD%2By2jUIcqSDPoL5LTEd&X-Amz-Signature=f05b6d6cb592f1bfbe3709fbcc53ab3d7d6483df155b2fdfdc60e84cdd5eadca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
