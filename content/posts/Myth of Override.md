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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNN3LXXM%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T012529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGl5H24%2F7c3u5hRlz%2BY9Nu68hEfFOLxj44ELqfbV%2F%2FOwIhAOcW3Cb99DPvIkOXug%2FQE%2F5mgJbdheTP7QMvda1xE0LVKv8DCFIQABoMNjM3NDIzMTgzODA1IgzJSngzPokeoHDUekkq3APYHLjupyaadRMMPnimwIZF6mNn3xoSflBPwf9kUX2cbYmGuUBM%2Fy439oqCD5zmD%2BuqbjYMavXMJ%2B7fGm9KTmosCPf7NQHmKKwq4niFRyPoD3N7fSLfIqm4rjaahrE47ZYEKWcJHchLXqo4H5GsO4b3%2B4ICJ66%2BbNN7HjUA8N8f8wH9ykjSFKnQjOrKJiI952OUMr8WVY4PeFZ2i473DXT0viE2JFfnhYmdNBQThGEgMI6gA5KJ96sl05S%2BRu7swKDc1p0scjVLJ5V5JxLm9%2FZIPreB3SqDdHnPj3hrwCMKcpHOopksjxAuQ%2BAJETmS4%2FT9m8EfnjCYG9H0xM80MPTAuStND3cEzZzeAEpsazMPEskZxtkx8L2cX59VxszSaubOQ0aadJcnu5qH2BNw7xrAkLxqtUfurdz4SE6eF2lEdCdICPsjejLMPuKZAWjrEBJJjhjRzSF6zLKpTg0z6ScwD2xI443%2FcbtR29tTjO681VKMJ6X05rk3Jj87CTiF90UxTO8%2BCD%2Bdl0H5bttJs8b1Z5Zlv%2FQ6SZx7aoWgzRa%2FIiQq72dLq9aCNOosI4lku4l8nWx1QRGkcKkaeKm4W3I%2B6%2FnPbmht%2BgJ4725jDWPQPAqeInYeRt65Ps16mTC28eXSBjqkATlOwOG86TOTXnXP8YmyZya5DpAhfuHeyNQbWjM7xTm2F6cE776WCVMDhBYMJBFvgcm2GqRFR%2FOwUrNnlfx%2BsJ6%2FFnq4N9VEs%2BxLHSLNNFkufFqNXj6i93j4zc9jBMP1lfSpFoEZSJi4eaDzwIxiUgOmEKQL%2FGyNEJRCVH6ouD9CsR7BMO2HECQ9DzcEhSTE%2FGP6qOMXITqBOeWu7lrA1waYKZJl&X-Amz-Signature=4cb07134debbb99808b75594175ca4f5ddd45777edd2b3e9dc1a488599d4d5b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNN3LXXM%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T012529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGl5H24%2F7c3u5hRlz%2BY9Nu68hEfFOLxj44ELqfbV%2F%2FOwIhAOcW3Cb99DPvIkOXug%2FQE%2F5mgJbdheTP7QMvda1xE0LVKv8DCFIQABoMNjM3NDIzMTgzODA1IgzJSngzPokeoHDUekkq3APYHLjupyaadRMMPnimwIZF6mNn3xoSflBPwf9kUX2cbYmGuUBM%2Fy439oqCD5zmD%2BuqbjYMavXMJ%2B7fGm9KTmosCPf7NQHmKKwq4niFRyPoD3N7fSLfIqm4rjaahrE47ZYEKWcJHchLXqo4H5GsO4b3%2B4ICJ66%2BbNN7HjUA8N8f8wH9ykjSFKnQjOrKJiI952OUMr8WVY4PeFZ2i473DXT0viE2JFfnhYmdNBQThGEgMI6gA5KJ96sl05S%2BRu7swKDc1p0scjVLJ5V5JxLm9%2FZIPreB3SqDdHnPj3hrwCMKcpHOopksjxAuQ%2BAJETmS4%2FT9m8EfnjCYG9H0xM80MPTAuStND3cEzZzeAEpsazMPEskZxtkx8L2cX59VxszSaubOQ0aadJcnu5qH2BNw7xrAkLxqtUfurdz4SE6eF2lEdCdICPsjejLMPuKZAWjrEBJJjhjRzSF6zLKpTg0z6ScwD2xI443%2FcbtR29tTjO681VKMJ6X05rk3Jj87CTiF90UxTO8%2BCD%2Bdl0H5bttJs8b1Z5Zlv%2FQ6SZx7aoWgzRa%2FIiQq72dLq9aCNOosI4lku4l8nWx1QRGkcKkaeKm4W3I%2B6%2FnPbmht%2BgJ4725jDWPQPAqeInYeRt65Ps16mTC28eXSBjqkATlOwOG86TOTXnXP8YmyZya5DpAhfuHeyNQbWjM7xTm2F6cE776WCVMDhBYMJBFvgcm2GqRFR%2FOwUrNnlfx%2BsJ6%2FFnq4N9VEs%2BxLHSLNNFkufFqNXj6i93j4zc9jBMP1lfSpFoEZSJi4eaDzwIxiUgOmEKQL%2FGyNEJRCVH6ouD9CsR7BMO2HECQ9DzcEhSTE%2FGP6qOMXITqBOeWu7lrA1waYKZJl&X-Amz-Signature=9a894e66f03658477d456302b38243eefacab88e8456bca92e82bf215900059a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
