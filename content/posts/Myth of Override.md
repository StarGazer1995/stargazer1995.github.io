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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624LYFLRR%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T083458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBZ7nvRTpn9giIclpQA0a0qo468R94bhtwuuxIxaaipSAiAhnbIfR8FmdhkJiioAFXTnU362C%2B%2B55HM7LQXqSCzBBiqIBAjo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5cFJ5wYi2T0ZC1XLKtwDL3Qwt%2BDvTgs6e40%2BjZC74YuFeV1AYKbuYBdxx7ZG%2BRkLZvyfIcbXtSC0tC%2B%2Bc0ao2WFZW42q8kjV06P1i%2BLkOW6soqwHD8pNKBjAXScaFnf0ZYKqiVDI9jzLAmMDn4m7oAu5qMEM8XgzdlvEjxwcrd47taR4cJX1dXGl9BRVKxC9tjNXCmA%2FzbUCW1sd%2BDi%2FPA1jYd9HYWY7%2BiYXkn5XSYSfxEoOJ3YZDrN%2BQJASqf1441hPIVnTmtrzvD6ri6kcUsKS48U%2FLpDvZEzX7JI3l0XRPqH1%2F8of3zpwwjeZb3MMGo2QzeGv4rF7TRBaiJzeeQfg2YDWm66pk1Nciq7v8DsyIu49dP8Y4Sn65sYbd2sUl4srdOb5eUzhS%2BlLicyr9BpGzSyipun%2FrkT97lHVlobr3wCM1oP6ebYhR%2FX0v3TnSBbeBhYisdt0%2BmGAA4yOzaajkXbUXELNEPx%2F6Gdj2miiXX4wO1AAlwlJMmCTDf1JN1VE8UllyE5jL2ZGH6Z0pVfITJLRgEt9VrYfjDcPmLRtW5gO5YIH6hFkdugr59LGbC0hXHH8IxPiatWZ64IRY%2BHbIil2%2BxREl0pKvYr5KTvov50uk2MkKZDM1aV3chJywQTZ2CYZlZA3rY4w9%2BCv1AY6pgFmXmO%2FPi9zpMqRXiM2YNGtmgD6p34MDLMkHh0Pvl08y%2BgdO71tChSP%2FzxORNqG5q%2FGCOQKCD6RG4tkz1bgXHFMz5pXFtV6jBrlgrVfb88jAT1GsnL%2BZYhqBwuPhZLirKuID%2B%2BHlwXF2hGS0kLD%2BVhHjVs%2FyI1Nfwn4uORvG3Nq9utntndM0Obc0VOw50owkB%2BPNtSVPglOJzXbIGZpqnyS3r%2ButGBz&X-Amz-Signature=e94d9942dfffc67c202f71a22b8005a7c644f77c933ce8b3052eda3d7169da30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624LYFLRR%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T083458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBZ7nvRTpn9giIclpQA0a0qo468R94bhtwuuxIxaaipSAiAhnbIfR8FmdhkJiioAFXTnU362C%2B%2B55HM7LQXqSCzBBiqIBAjo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5cFJ5wYi2T0ZC1XLKtwDL3Qwt%2BDvTgs6e40%2BjZC74YuFeV1AYKbuYBdxx7ZG%2BRkLZvyfIcbXtSC0tC%2B%2Bc0ao2WFZW42q8kjV06P1i%2BLkOW6soqwHD8pNKBjAXScaFnf0ZYKqiVDI9jzLAmMDn4m7oAu5qMEM8XgzdlvEjxwcrd47taR4cJX1dXGl9BRVKxC9tjNXCmA%2FzbUCW1sd%2BDi%2FPA1jYd9HYWY7%2BiYXkn5XSYSfxEoOJ3YZDrN%2BQJASqf1441hPIVnTmtrzvD6ri6kcUsKS48U%2FLpDvZEzX7JI3l0XRPqH1%2F8of3zpwwjeZb3MMGo2QzeGv4rF7TRBaiJzeeQfg2YDWm66pk1Nciq7v8DsyIu49dP8Y4Sn65sYbd2sUl4srdOb5eUzhS%2BlLicyr9BpGzSyipun%2FrkT97lHVlobr3wCM1oP6ebYhR%2FX0v3TnSBbeBhYisdt0%2BmGAA4yOzaajkXbUXELNEPx%2F6Gdj2miiXX4wO1AAlwlJMmCTDf1JN1VE8UllyE5jL2ZGH6Z0pVfITJLRgEt9VrYfjDcPmLRtW5gO5YIH6hFkdugr59LGbC0hXHH8IxPiatWZ64IRY%2BHbIil2%2BxREl0pKvYr5KTvov50uk2MkKZDM1aV3chJywQTZ2CYZlZA3rY4w9%2BCv1AY6pgFmXmO%2FPi9zpMqRXiM2YNGtmgD6p34MDLMkHh0Pvl08y%2BgdO71tChSP%2FzxORNqG5q%2FGCOQKCD6RG4tkz1bgXHFMz5pXFtV6jBrlgrVfb88jAT1GsnL%2BZYhqBwuPhZLirKuID%2B%2BHlwXF2hGS0kLD%2BVhHjVs%2FyI1Nfwn4uORvG3Nq9utntndM0Obc0VOw50owkB%2BPNtSVPglOJzXbIGZpqnyS3r%2ButGBz&X-Amz-Signature=96757b88b29179dc825f0d4ee278e3d662ec4ba67f6195bb98162f609bbed0cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
