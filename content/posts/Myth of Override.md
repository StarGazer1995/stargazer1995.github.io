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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FV45EZI%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T142056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkTf0YZTBhEv3HkvJwo%2BEheG047ZIMe%2FUcfBr45RzFaQIhAMCDyb7eHJHSQOemr0h2iFrbgcyCI7HPO%2Fplx8%2FV6%2FEyKv8DCG4QABoMNjM3NDIzMTgzODA1IgzLtoyxvwpeHl65bqwq3AOgMX6QPR7KqSsNd5AR%2F4OwqIaIXE%2F%2B3AyQjbR6E6HfkXXGpqby0hxWYO67t5dRP4vky1eZKkCpQKD%2BtqUP5O7dmn3E8edRzkQK1mxFBll%2BgorZrGBXH5bv%2F1ywruQH94HArhnlOBg2DWAV92e2EZabhvl%2B%2FJgBLox1M5cg6Y%2BcXMJUCSltIg4oz3EuJB2xZ8Kt6Fy7CeupkrZAEgxr1wr9avL%2F7LUIBFtqgNj0JdGBIq3vl2q84hW8t501dQ27p%2Fis%2F45buFTlJFbfigraKPhiJQxP0vm024%2ByP8j%2FDsoI0dKjcKV071BD4jSkxGwvt9AhqKOdZfkDv2kkyQzZnvRbmAyxw0Vcn1z4jVLkQD%2BYhBYuaRKUJeU8z5U3X%2Bn4rYzPNd8Sv%2FWouA%2FC%2BOlfXD3K72n%2Fh6%2FR0hurI2vvOB8on9rQDTVylBmm0Q2a7kyk8UMJ31sN%2BSII7ohEJC0ZQlCz%2BjwM9ZFwUoXQ9tYHta2FSNCQmm3XwEt5TAShL0oPyYGlfiSbIF3F4qZk5Sp41KxYh13qAUrFUhKDIVbxc3zUgsSIlsHA784R28%2Fd0DR32F5Da5YI1Kf1zNWXumLsLY1QHn%2BHqG%2BtH8pPEdtiifhrt6oqof2JZgTg54Sl5zC5k4vRBjqkASuE7erV31h3q72N5YDYN5sZwhmBe592PuMI%2FWnjVkLwOhwTblb74zsTZmk45%2FyTdQdgx32ClsH2F%2FJc0hJz2a7eCrAVPYiMiW9PlDxEjoaB9%2FVhs8sOnmL6N1da6CjRuTc0fMfk7c%2BfReHChIiuqmj542JKa4zFX6VN5KnR2t%2F4NAPnrA3vNkIICUm%2FZS1tHfyCftwj2Fs%2F06BVJQjQBp5lqLuQ&X-Amz-Signature=70d560812f253b7ebeba8cd4f955a0954e94c8a217163f7e4622b0d2c82511ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FV45EZI%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T142056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkTf0YZTBhEv3HkvJwo%2BEheG047ZIMe%2FUcfBr45RzFaQIhAMCDyb7eHJHSQOemr0h2iFrbgcyCI7HPO%2Fplx8%2FV6%2FEyKv8DCG4QABoMNjM3NDIzMTgzODA1IgzLtoyxvwpeHl65bqwq3AOgMX6QPR7KqSsNd5AR%2F4OwqIaIXE%2F%2B3AyQjbR6E6HfkXXGpqby0hxWYO67t5dRP4vky1eZKkCpQKD%2BtqUP5O7dmn3E8edRzkQK1mxFBll%2BgorZrGBXH5bv%2F1ywruQH94HArhnlOBg2DWAV92e2EZabhvl%2B%2FJgBLox1M5cg6Y%2BcXMJUCSltIg4oz3EuJB2xZ8Kt6Fy7CeupkrZAEgxr1wr9avL%2F7LUIBFtqgNj0JdGBIq3vl2q84hW8t501dQ27p%2Fis%2F45buFTlJFbfigraKPhiJQxP0vm024%2ByP8j%2FDsoI0dKjcKV071BD4jSkxGwvt9AhqKOdZfkDv2kkyQzZnvRbmAyxw0Vcn1z4jVLkQD%2BYhBYuaRKUJeU8z5U3X%2Bn4rYzPNd8Sv%2FWouA%2FC%2BOlfXD3K72n%2Fh6%2FR0hurI2vvOB8on9rQDTVylBmm0Q2a7kyk8UMJ31sN%2BSII7ohEJC0ZQlCz%2BjwM9ZFwUoXQ9tYHta2FSNCQmm3XwEt5TAShL0oPyYGlfiSbIF3F4qZk5Sp41KxYh13qAUrFUhKDIVbxc3zUgsSIlsHA784R28%2Fd0DR32F5Da5YI1Kf1zNWXumLsLY1QHn%2BHqG%2BtH8pPEdtiifhrt6oqof2JZgTg54Sl5zC5k4vRBjqkASuE7erV31h3q72N5YDYN5sZwhmBe592PuMI%2FWnjVkLwOhwTblb74zsTZmk45%2FyTdQdgx32ClsH2F%2FJc0hJz2a7eCrAVPYiMiW9PlDxEjoaB9%2FVhs8sOnmL6N1da6CjRuTc0fMfk7c%2BfReHChIiuqmj542JKa4zFX6VN5KnR2t%2F4NAPnrA3vNkIICUm%2FZS1tHfyCftwj2Fs%2F06BVJQjQBp5lqLuQ&X-Amz-Signature=9a21cb4042b00e2c12daab2c0fedfb73cf8317d8d3fd1c1e0935e17de37a25b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
