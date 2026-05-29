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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGKCHMVL%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T020026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBibw6l2RmCMPAIcpENcPGdRBrlezACWVV%2FogDA%2F5G%2B5AiEAjud8xqAltmk%2FDA4EBsHNvkYo6PAayZQpgVfkvIvp%2BZwqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqKpRKnccNo6NQ5SyrcAwiZtVPoWXU5zI%2Fx0iDVzc3N06guJ57a7Qs0mLmCsuqtufvCPL%2FBnfCk%2FmsTg1uDZ4oukfhIcH2azF4MhQjDTEE%2Fn8kS9iBKpZ%2BZwCDh9%2BzLE8xrDHfvWsn%2Fp4efmccYGErFrLOLWQEvouwmowXCpWINHCX5DqllozOMc0Kmn5ZXunvoD79dBy0PRBMJ%2FFfW1TldQ%2FGqcjgLs59roCzE3JC8Tp%2FwdAI1JEpFozuBJ98PIKyQ%2Fjo10uDQ22sWObxLcb5EyiudluJnexZDk%2Bq2p6ETcAfkUyNq88c0U4YAXaEzXY6%2FaRZHnW555jHtWqsbI9kKaVSk6vyOkMwGKqUjxlu%2F%2BXP5Ha9dsuxALggrjnRD4u2Gv8YOLSGIJRw9MVFaDqNicvvPP8RsfGEdlAqoChKG6FYY8mkDKXPRPv9MMSfyZfEj95BusMLEbHzZ1Umnx4kehwo7aRjKBkqj1K7jqOzXAd6zrUeJN6zsn3KciynHmRiG0BOJ6aH2sVh0Yqkj5%2FlUud%2Bth2muYU04JDs8fFZ5DKdkoPXXgR95eIvZ%2FfdOJnTKNJA0me3NHmjGWBC1rtoxGQwQ3RwYom9ouBvxd8HKVu%2F84tDoQRn786eVN6gt5Ks1f9ngHnOX1iqBMJTh49AGOqUB6jNwD3%2BRzhuBzeTxyvd5F0IEs88l4LMxp5%2F6b9rb0y9Yr0UlQ%2FGh3UdZ87wU%2FoircOt2d1fE3hVd8BIHwLt%2B9G6ozOy8odvDMF88UVn2ggAF7dUolTpyRmvONHJZT%2BTZ8hdEAe%2BSm15SXWX6DLEIHNZlNwGLl4x%2BUYDCuYCOTvFdZcIvUhZN2nCbvXPEEOk3TTxNWetQglZgIHqmLGy1lyvFw1UD&X-Amz-Signature=21f8d18b49b9475d1f798476d71b3d1bd8c7556628dc03da1d3256a84f334795&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGKCHMVL%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T020026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBibw6l2RmCMPAIcpENcPGdRBrlezACWVV%2FogDA%2F5G%2B5AiEAjud8xqAltmk%2FDA4EBsHNvkYo6PAayZQpgVfkvIvp%2BZwqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqKpRKnccNo6NQ5SyrcAwiZtVPoWXU5zI%2Fx0iDVzc3N06guJ57a7Qs0mLmCsuqtufvCPL%2FBnfCk%2FmsTg1uDZ4oukfhIcH2azF4MhQjDTEE%2Fn8kS9iBKpZ%2BZwCDh9%2BzLE8xrDHfvWsn%2Fp4efmccYGErFrLOLWQEvouwmowXCpWINHCX5DqllozOMc0Kmn5ZXunvoD79dBy0PRBMJ%2FFfW1TldQ%2FGqcjgLs59roCzE3JC8Tp%2FwdAI1JEpFozuBJ98PIKyQ%2Fjo10uDQ22sWObxLcb5EyiudluJnexZDk%2Bq2p6ETcAfkUyNq88c0U4YAXaEzXY6%2FaRZHnW555jHtWqsbI9kKaVSk6vyOkMwGKqUjxlu%2F%2BXP5Ha9dsuxALggrjnRD4u2Gv8YOLSGIJRw9MVFaDqNicvvPP8RsfGEdlAqoChKG6FYY8mkDKXPRPv9MMSfyZfEj95BusMLEbHzZ1Umnx4kehwo7aRjKBkqj1K7jqOzXAd6zrUeJN6zsn3KciynHmRiG0BOJ6aH2sVh0Yqkj5%2FlUud%2Bth2muYU04JDs8fFZ5DKdkoPXXgR95eIvZ%2FfdOJnTKNJA0me3NHmjGWBC1rtoxGQwQ3RwYom9ouBvxd8HKVu%2F84tDoQRn786eVN6gt5Ks1f9ngHnOX1iqBMJTh49AGOqUB6jNwD3%2BRzhuBzeTxyvd5F0IEs88l4LMxp5%2F6b9rb0y9Yr0UlQ%2FGh3UdZ87wU%2FoircOt2d1fE3hVd8BIHwLt%2B9G6ozOy8odvDMF88UVn2ggAF7dUolTpyRmvONHJZT%2BTZ8hdEAe%2BSm15SXWX6DLEIHNZlNwGLl4x%2BUYDCuYCOTvFdZcIvUhZN2nCbvXPEEOk3TTxNWetQglZgIHqmLGy1lyvFw1UD&X-Amz-Signature=f2b509455707f16c5542ae8e76f9c4a7ccaacc7f23c292dcc5671d0f0fe39fce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
