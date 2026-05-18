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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV3TL3NB%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T113709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEY94ITAlu%2FXVXeqtha2YNcdKcxodOxuXRAwF4ATQDKeAiA%2BuBFa%2F%2F68vVhpZhAHBb351YIi3LVNVJtcUvR0GkolGiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhJ00EbfPh3iOhZgEKtwD2rxOGTc5JgdvpBdSLfao2HtJwWYKt8e%2BynCY8wc33eLgBDX9EhOwrstQUL0QpPJbyzkgu26B2FLZLnM1sgK9yHoPVQGwQFJmS6iWYblWWriq0L2%2FvsC8b7SCiL0OkJMQGD76syDtGJyyIy3ce8PvF00tNI9Gjpj0kiA0EPiy59dUvDRbzoz%2FBeeeTwrjQzWcLpPYBXqXP9tx9erLE%2BYCcd7vhDTYX6uoC6qv0MhqjLQH1%2Fj0hdVUVoJdDoEEVD%2BuzFgeN7cGtUhnCVtvBF2aRe5VkC4Z4R8GGY3Jwr5dvWN5RbNxcvIeoLq87rLaknKUYzpWnFSz4DjVFCRyzh5LmFXnAxCtvKbNdDKoATuNupQSD4AlFNaazcCGqZ8c%2BNYZGRKyWrS%2BPtHXhgVREbnxqVxVuOjoGWYQon8MAfBU4wKDI7L25REyT%2Fh%2FbmSwH61Y%2BSkFp3K%2FuNeL2YOJAqOJjyyYH4anxWJXTuKAUvnNhWi5Hzxb0DxESyRLvcxhSf1j1yylylCQPTRB3wkN6ZgJ3IbXkvsevLmunHjk%2B5ETNuXVdVn2%2BGcwc13SpUgGEdYE13ZH%2B2UFSzbZDGfnCPTrG3WXEAyutmgW2O2JrPdWpQoz3%2BebRZxFPykzGXAwyemr0AY6pgHuAsg3HrtFTaEhxRllqUtDn%2BK1cwC%2FTDigfynDLzfHhl6zbxADn0BTTMtkQJXaqyFRpfFEU%2FSL%2BCQP63qonkKkPXzNfcyohJKQTR7FUs38Z%2B96S2SWSL%2FNME9fLHFmaMzT9ujs2Ktx%2BOF3T3bgNWrEGmyr4DoS7Kfm%2BzLIB4KS3ePZYBQJoCrFh0%2FGqY7bke8r2xWZHZ8QejLGvgJVLWQa1xYmDya9&X-Amz-Signature=1f5b4a32228c477e5483b2e4be793f94a3c9b1636f8ab5f75eedd316430741dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV3TL3NB%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T113709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEY94ITAlu%2FXVXeqtha2YNcdKcxodOxuXRAwF4ATQDKeAiA%2BuBFa%2F%2F68vVhpZhAHBb351YIi3LVNVJtcUvR0GkolGiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhJ00EbfPh3iOhZgEKtwD2rxOGTc5JgdvpBdSLfao2HtJwWYKt8e%2BynCY8wc33eLgBDX9EhOwrstQUL0QpPJbyzkgu26B2FLZLnM1sgK9yHoPVQGwQFJmS6iWYblWWriq0L2%2FvsC8b7SCiL0OkJMQGD76syDtGJyyIy3ce8PvF00tNI9Gjpj0kiA0EPiy59dUvDRbzoz%2FBeeeTwrjQzWcLpPYBXqXP9tx9erLE%2BYCcd7vhDTYX6uoC6qv0MhqjLQH1%2Fj0hdVUVoJdDoEEVD%2BuzFgeN7cGtUhnCVtvBF2aRe5VkC4Z4R8GGY3Jwr5dvWN5RbNxcvIeoLq87rLaknKUYzpWnFSz4DjVFCRyzh5LmFXnAxCtvKbNdDKoATuNupQSD4AlFNaazcCGqZ8c%2BNYZGRKyWrS%2BPtHXhgVREbnxqVxVuOjoGWYQon8MAfBU4wKDI7L25REyT%2Fh%2FbmSwH61Y%2BSkFp3K%2FuNeL2YOJAqOJjyyYH4anxWJXTuKAUvnNhWi5Hzxb0DxESyRLvcxhSf1j1yylylCQPTRB3wkN6ZgJ3IbXkvsevLmunHjk%2B5ETNuXVdVn2%2BGcwc13SpUgGEdYE13ZH%2B2UFSzbZDGfnCPTrG3WXEAyutmgW2O2JrPdWpQoz3%2BebRZxFPykzGXAwyemr0AY6pgHuAsg3HrtFTaEhxRllqUtDn%2BK1cwC%2FTDigfynDLzfHhl6zbxADn0BTTMtkQJXaqyFRpfFEU%2FSL%2BCQP63qonkKkPXzNfcyohJKQTR7FUs38Z%2B96S2SWSL%2FNME9fLHFmaMzT9ujs2Ktx%2BOF3T3bgNWrEGmyr4DoS7Kfm%2BzLIB4KS3ePZYBQJoCrFh0%2FGqY7bke8r2xWZHZ8QejLGvgJVLWQa1xYmDya9&X-Amz-Signature=29692fcb2a01b70b5cbe024da5072f6d8ed7a4803e933ce782fc84e12bf8782d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
