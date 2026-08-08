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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BKXU2W6%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T142237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE2MGH0tN5V1UZhdYZxafgS01sSBYvsWHFIb4vTUBM7eAiEA6WkUpoWzHFFbHUTLDhGALR%2BL3rwhuKBMl4EbOJXzmNoq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDI6GaoJ6b%2F8rfamC1SrcA2z0tTC6RgspxYQMjWbJxGdWnoJiEhQzXyGjzs0gz455Nk034xJ8bNyH4v2shHXtxXTZj%2FA1lQE%2BC101SnJy5JE7AcdsRurKdqHvISiRHF68eEH5d%2Bb1fhi%2FZlReOZOOc6ihLEUe3AnVb8l75ulreK3yTUZCGClIkJb4jLzjyevIqSjnog42oIc3sYQeFghKbY6ZFKr2zR9%2FcPqkcnCpE9ve3yyhpHMZLAeBjI2aiWyl84zisXDNvUbKQhdkBip5u5COgDYB%2Bzr3f%2Bu2JJVQ1b7qRwaB6nlN80uxMd6NdOOffu%2B6W8FZUEfot%2BzV6oRKgLKDwEeZ6kI%2Fpoy2d4oeJzs%2Bz5XxWp2DMuqI3BVvXUzHM5tTBr2vJFLJH%2BcSSLX7mFfygfSt40uDa%2BhYOJP6fcbbn4CUka0JYTXHJSHzyovufYgLGf4IxGCaeqRkbSByj2nNE9SUXpiWCVuZmJy1yMwJz9pLmVO9QbGWmnccrov3TIICHm7vrrMO3xdA91e%2B5LTc4nyECp2yO1qzWRy9VOpuRatMtaDAkuEtYHUcgZFCBVW6kEmoBcO3segXIo7abV2rlFSy1tiXRGuTaSP0v0xPb8E8Mqnn2zGaMySU2L%2B3c6A%2FjLGhbEZ60zNnMI7w3NMGOqUBuu9lzw4dn7cGkiLhuATRCEkZXCnYLMFPIY1NJQrbKyaQe9srA%2FcQZaBJaKtqbEZYS7XyCY4Pz4Kd8lx0LGyDGhKhrzWESli4lOTPSktYBcnZv1F5zFBvXm1il7qTmrBCpmMeiyC12FgnCJlUIrjCerbBOIfa69IA2UNZcHm5KwOhA5%2Bmv2xHcaRNcNorWoQtjvxbtRGlSnGwUfSRX%2BDAMYKEsSRc&X-Amz-Signature=4155037999d33a344126136fc7d684de24bc2926a690da7f6128443b5f5182d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BKXU2W6%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T142237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE2MGH0tN5V1UZhdYZxafgS01sSBYvsWHFIb4vTUBM7eAiEA6WkUpoWzHFFbHUTLDhGALR%2BL3rwhuKBMl4EbOJXzmNoq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDI6GaoJ6b%2F8rfamC1SrcA2z0tTC6RgspxYQMjWbJxGdWnoJiEhQzXyGjzs0gz455Nk034xJ8bNyH4v2shHXtxXTZj%2FA1lQE%2BC101SnJy5JE7AcdsRurKdqHvISiRHF68eEH5d%2Bb1fhi%2FZlReOZOOc6ihLEUe3AnVb8l75ulreK3yTUZCGClIkJb4jLzjyevIqSjnog42oIc3sYQeFghKbY6ZFKr2zR9%2FcPqkcnCpE9ve3yyhpHMZLAeBjI2aiWyl84zisXDNvUbKQhdkBip5u5COgDYB%2Bzr3f%2Bu2JJVQ1b7qRwaB6nlN80uxMd6NdOOffu%2B6W8FZUEfot%2BzV6oRKgLKDwEeZ6kI%2Fpoy2d4oeJzs%2Bz5XxWp2DMuqI3BVvXUzHM5tTBr2vJFLJH%2BcSSLX7mFfygfSt40uDa%2BhYOJP6fcbbn4CUka0JYTXHJSHzyovufYgLGf4IxGCaeqRkbSByj2nNE9SUXpiWCVuZmJy1yMwJz9pLmVO9QbGWmnccrov3TIICHm7vrrMO3xdA91e%2B5LTc4nyECp2yO1qzWRy9VOpuRatMtaDAkuEtYHUcgZFCBVW6kEmoBcO3segXIo7abV2rlFSy1tiXRGuTaSP0v0xPb8E8Mqnn2zGaMySU2L%2B3c6A%2FjLGhbEZ60zNnMI7w3NMGOqUBuu9lzw4dn7cGkiLhuATRCEkZXCnYLMFPIY1NJQrbKyaQe9srA%2FcQZaBJaKtqbEZYS7XyCY4Pz4Kd8lx0LGyDGhKhrzWESli4lOTPSktYBcnZv1F5zFBvXm1il7qTmrBCpmMeiyC12FgnCJlUIrjCerbBOIfa69IA2UNZcHm5KwOhA5%2Bmv2xHcaRNcNorWoQtjvxbtRGlSnGwUfSRX%2BDAMYKEsSRc&X-Amz-Signature=7588d40575a26b6fb7400ca466f9e3769837c0c28c34e3d52a5f0c66eeb627b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
