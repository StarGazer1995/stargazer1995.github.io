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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HKU63AM%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T171312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGY%2FXCbhi2mUgUSYpJwP5cGlw6oc0%2F3%2BDNTl6RtgwrzAAiAtt1%2FXAk12F%2FOfkaTj0iyzhJEHQEFtI%2BZdItfxx3U1wiqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdc5ZyZOHLz5zBx9%2FKtwDnfGtVJIALrEdMM%2BbD8q6kpeCmQwsttM6De7dno9ADpWKulJZ0koOhooj0xMxTaGWuwGMxHz4qVe5LJw8jqzyWTvfu6u58VsH4AfSXBRmzpSeaQabyRXX2scqIp%2FSVbXWiffqUzAWuI67AZejSFvucgSO%2F5U5ZoB5AxjVp747W9CM1%2BWJlObAPqx%2Bxr84pBKx6vY4FRdwjr9I3VjTjvtj7S4gvk9oOrsVEvb9Kd5Ch%2BYJrzFCojwWZ1KlIry2%2FT4nbpwfTqFET23gIPQRHaSFmT1yKLjmP710faObfD6RjFXPLrfzOgvjEw2bn4F1Lh97IqgyPzlFS6856AsaIMITOdyOCpcVGSEJ%2B62kLFelC2PqbBG93rc35YHrGIjbSDOG0DASI0e09Q3MSPC7cu5FEizXC7jcEK01%2BgDG%2BfMK3VS1TmxVgNKmciJUkSyvRnKKHjV072b%2BZC%2FYP3GboE6GuGRWwlgMcpA2ypCDIn3GTFfMHMcqVq0BgVG7V1H4EVfyWyfNdI5KIbbZ16xUeXQZoaA1zUfKAdTRrrq6vee7oZXkNy6PHgEh28XqOgtlaWuwCADDNt3KlvLhcN5Z5eYy%2FqGH2ayvHl6VSIkUJvVV7PqY3Jh8WMFhsrDVAd4wiJ%2B51gY6pgHEhwJiQWOpL4hB0VavvEm13zP6Tm4rbU%2FbiZ%2FzjgWqwfo8Bepg8Xg5T8nJbdn8AZaLl6TKYaNqc7PUYSmrVb0zj1POeZdYP831RyPFwlPxh22UWJer90VM6T%2F51JkaKxUCORzjx8gREgpvYMPtqZEHRIjYAhV8CalAqC0n2455FCc3X8435SA09FJ4WfsW%2Bv73WbxcAuRCuhmVr1Xd9rf5togsO1kC&X-Amz-Signature=046c85782c35171a727a574e4cdd6000bdb21d6c74b0f17ecb10b2a8f28ab4f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HKU63AM%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T171312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGY%2FXCbhi2mUgUSYpJwP5cGlw6oc0%2F3%2BDNTl6RtgwrzAAiAtt1%2FXAk12F%2FOfkaTj0iyzhJEHQEFtI%2BZdItfxx3U1wiqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdc5ZyZOHLz5zBx9%2FKtwDnfGtVJIALrEdMM%2BbD8q6kpeCmQwsttM6De7dno9ADpWKulJZ0koOhooj0xMxTaGWuwGMxHz4qVe5LJw8jqzyWTvfu6u58VsH4AfSXBRmzpSeaQabyRXX2scqIp%2FSVbXWiffqUzAWuI67AZejSFvucgSO%2F5U5ZoB5AxjVp747W9CM1%2BWJlObAPqx%2Bxr84pBKx6vY4FRdwjr9I3VjTjvtj7S4gvk9oOrsVEvb9Kd5Ch%2BYJrzFCojwWZ1KlIry2%2FT4nbpwfTqFET23gIPQRHaSFmT1yKLjmP710faObfD6RjFXPLrfzOgvjEw2bn4F1Lh97IqgyPzlFS6856AsaIMITOdyOCpcVGSEJ%2B62kLFelC2PqbBG93rc35YHrGIjbSDOG0DASI0e09Q3MSPC7cu5FEizXC7jcEK01%2BgDG%2BfMK3VS1TmxVgNKmciJUkSyvRnKKHjV072b%2BZC%2FYP3GboE6GuGRWwlgMcpA2ypCDIn3GTFfMHMcqVq0BgVG7V1H4EVfyWyfNdI5KIbbZ16xUeXQZoaA1zUfKAdTRrrq6vee7oZXkNy6PHgEh28XqOgtlaWuwCADDNt3KlvLhcN5Z5eYy%2FqGH2ayvHl6VSIkUJvVV7PqY3Jh8WMFhsrDVAd4wiJ%2B51gY6pgHEhwJiQWOpL4hB0VavvEm13zP6Tm4rbU%2FbiZ%2FzjgWqwfo8Bepg8Xg5T8nJbdn8AZaLl6TKYaNqc7PUYSmrVb0zj1POeZdYP831RyPFwlPxh22UWJer90VM6T%2F51JkaKxUCORzjx8gREgpvYMPtqZEHRIjYAhV8CalAqC0n2455FCc3X8435SA09FJ4WfsW%2Bv73WbxcAuRCuhmVr1Xd9rf5togsO1kC&X-Amz-Signature=dd8635074c2fc7c6c09602d418c1f74e06dc66753e4ea5b37ce2098fe15d6a78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
