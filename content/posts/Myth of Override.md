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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRCBCATQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDMhZ5GgL7HKtDWczJzdS%2BDQjqN4K7uGgJRHSdhluOZVAiB0dQ7%2BYUsDa5J4ag40lf27WnlivKUXV8cWzlqcPnNpUyqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM192fyufI535sfR4xKtwDZsWpOvPr7Bqkok8Xdh0kSMK%2BuAyD43Hu4ZzC7HXufEz8wZ7DNyofVqm5%2B3q70AWBu0DvTW2x%2Fbg4X%2B5XSNcx1wRS6Cz%2BiPOBJpdr5Qv3ZpHro5WxiV%2FOh9IHN9%2B1yLJ%2FflLzmIaf2HJKB7EOaVtXhYvGy3EYdIZXtkNSUZHj%2FRb2b2JTCmFOirygd8NZpSZoZ1RXWrx75J2B9cZppmqrM%2FBAV286N%2Fevopp%2FjSAIMIvXjKTg4unSGG6uDWbu1IOTy%2F6efFdRxg29nruW8ZElzbwJKElpn90Zt5ppqx2zU2yG8ptlJE13y%2B5yhmC0DzfQmdyuXADzrI5JRWE7syEYhJmTkT6s5ZYtRZB%2BPAyJL1Q%2FK2zWSsSm09szxs8QRuB3PzcXrxsstVeBhGx7ApHgx2hmvhQenXOIin6oVcAOdoAUidPHUXtsU0LfCXXmp07T7uoMq7hS4h91Zlzx9%2FssjAZc3W0JNorAf0HDxwA7RDFFeUU9psrxQumtNsGVyqLpt2wHEEVRFu3CVGNdDIMNR%2FjjREiLqi4jViDsEsh%2BpqpXsPN1%2BIXal3AyR1bcwWPNpRo60iOCZB3m5%2Bwk%2FD56w5dB%2BVeavPU78YVeGcBz4CHUQSRXmdPk6%2BW6UTUwpqv80gY6pgGcHDxbj9QgDwXxo1xekSNk4DBqrBMq2Xpz%2Bz93mbr8PdHwn9%2B6krYLcTWiQj7RIrlgz%2F%2B%2BP%2BW5hYE2ztPcPPpoze04HyZ5sf2JjgKFw%2BziDjpf0Pwkx%2FglY4lJhJIJ4VQIOouoYeYdhYwZA8XNqmydnGqoycecXkmVA7%2FPTV5gTCIuZkIg3aVo%2Fx1tXREYQLQyMzfgJhDMljbuKWCx0begXQdep8f6&X-Amz-Signature=7013060c4763b0173a78061a032470924beae07779a253ac53cae325b4c45411&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRCBCATQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDMhZ5GgL7HKtDWczJzdS%2BDQjqN4K7uGgJRHSdhluOZVAiB0dQ7%2BYUsDa5J4ag40lf27WnlivKUXV8cWzlqcPnNpUyqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM192fyufI535sfR4xKtwDZsWpOvPr7Bqkok8Xdh0kSMK%2BuAyD43Hu4ZzC7HXufEz8wZ7DNyofVqm5%2B3q70AWBu0DvTW2x%2Fbg4X%2B5XSNcx1wRS6Cz%2BiPOBJpdr5Qv3ZpHro5WxiV%2FOh9IHN9%2B1yLJ%2FflLzmIaf2HJKB7EOaVtXhYvGy3EYdIZXtkNSUZHj%2FRb2b2JTCmFOirygd8NZpSZoZ1RXWrx75J2B9cZppmqrM%2FBAV286N%2Fevopp%2FjSAIMIvXjKTg4unSGG6uDWbu1IOTy%2F6efFdRxg29nruW8ZElzbwJKElpn90Zt5ppqx2zU2yG8ptlJE13y%2B5yhmC0DzfQmdyuXADzrI5JRWE7syEYhJmTkT6s5ZYtRZB%2BPAyJL1Q%2FK2zWSsSm09szxs8QRuB3PzcXrxsstVeBhGx7ApHgx2hmvhQenXOIin6oVcAOdoAUidPHUXtsU0LfCXXmp07T7uoMq7hS4h91Zlzx9%2FssjAZc3W0JNorAf0HDxwA7RDFFeUU9psrxQumtNsGVyqLpt2wHEEVRFu3CVGNdDIMNR%2FjjREiLqi4jViDsEsh%2BpqpXsPN1%2BIXal3AyR1bcwWPNpRo60iOCZB3m5%2Bwk%2FD56w5dB%2BVeavPU78YVeGcBz4CHUQSRXmdPk6%2BW6UTUwpqv80gY6pgGcHDxbj9QgDwXxo1xekSNk4DBqrBMq2Xpz%2Bz93mbr8PdHwn9%2B6krYLcTWiQj7RIrlgz%2F%2B%2BP%2BW5hYE2ztPcPPpoze04HyZ5sf2JjgKFw%2BziDjpf0Pwkx%2FglY4lJhJIJ4VQIOouoYeYdhYwZA8XNqmydnGqoycecXkmVA7%2FPTV5gTCIuZkIg3aVo%2Fx1tXREYQLQyMzfgJhDMljbuKWCx0begXQdep8f6&X-Amz-Signature=cf11ed487701b55780a9a46ef4aff7f14c6e8cdf72fb8a7093d452ef32083817&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
