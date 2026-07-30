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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4GSVTY6%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T171348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg7TBSxEdDBymT6qPzjhTYglnZlI%2FGRL1VNxA1J9EYGAiAlQBWlraJLCzHLhGnfgMPu%2FebG58tnJutgN9r1HhFz5iqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNs9trmSWmv8syCthKtwDHdWAgdgZpjXYU905h75x9JILlTWmcAsXljxp8wK4ZT2GMHjazRyrCg5mTfkbTU7vvlBwYZaWWlfoBuluTNva11qQKsHE6S9gKEUufaufUu7R9RaFonZySEIgTwJHtN%2BkOzHvTf4LdXXuBg5WjfyqECdrAK2njxIZrrlzwYMmcycbo9c%2BZj3y6VP2N8dM%2FK8tZttmK84fWDBh3DAMnsm1Fki%2FmIEkwH1Gm2swYQnRB1IEH4Ou7JLT%2B%2FL8%2F9ku%2BOd8JuGjpjrH5tGgXQjimqeKCervycl%2FJWE2ZutJdy4Le4K8Ntd1Ahn7V0gVokQLT8ct3aLOitGdmMPfMhi1%2FT5hb2oFHVPzlYPIqy6FLT6vD85l3TeepFQfEhgTU%2BV3cNXt4VDPtm3%2BEc3%2BNlsfNp%2B0%2FeYWlsarKTN7oTVhFJ2nA4awRzvlYvs6T20Nwkg0JcmOCObyqL3gR1tqyG0vondBz9OtQ5T%2F5wDcW8a5tL8QaGbuY7mfH3sSkN4g7zbeaek%2BBZJeQB5LYFAc0yVbXnAhoO3p%2F5x6o4Bt%2BG1audai7BjwatTD8qm29Ixs8WTQ3gKw8jzzJoAO9%2B437fVKYsFarRnpCBX2rgfCT62N5Ke5thKkxfnL0mNsX42dygAw7eqt0wY6pgFQzZi9dhoOAMu5LCohBlOD%2BBQCExT9YgEZMRclaecP4qk%2F%2F5xbrYkmFRKNeuCTV4qtEO5zlzam%2FAXQunZp1jBB9TqVzM9XfBDxSS%2FcPoUZ3zHNIVIlEyu24yagCV8v2Ijki22OsZBR%2FVGOw21m4M%2BH4vvCEGOKxMSHV%2FDQ8asjALXbpVPb3gzaVvZWbqad0yaenuypk4VYFV9O3VLgEYpUnRBBDuVW&X-Amz-Signature=e2c058c42074f5534c510c1b890ea54e581b8a75249db257e10259e207938765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4GSVTY6%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T171348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg7TBSxEdDBymT6qPzjhTYglnZlI%2FGRL1VNxA1J9EYGAiAlQBWlraJLCzHLhGnfgMPu%2FebG58tnJutgN9r1HhFz5iqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNs9trmSWmv8syCthKtwDHdWAgdgZpjXYU905h75x9JILlTWmcAsXljxp8wK4ZT2GMHjazRyrCg5mTfkbTU7vvlBwYZaWWlfoBuluTNva11qQKsHE6S9gKEUufaufUu7R9RaFonZySEIgTwJHtN%2BkOzHvTf4LdXXuBg5WjfyqECdrAK2njxIZrrlzwYMmcycbo9c%2BZj3y6VP2N8dM%2FK8tZttmK84fWDBh3DAMnsm1Fki%2FmIEkwH1Gm2swYQnRB1IEH4Ou7JLT%2B%2FL8%2F9ku%2BOd8JuGjpjrH5tGgXQjimqeKCervycl%2FJWE2ZutJdy4Le4K8Ntd1Ahn7V0gVokQLT8ct3aLOitGdmMPfMhi1%2FT5hb2oFHVPzlYPIqy6FLT6vD85l3TeepFQfEhgTU%2BV3cNXt4VDPtm3%2BEc3%2BNlsfNp%2B0%2FeYWlsarKTN7oTVhFJ2nA4awRzvlYvs6T20Nwkg0JcmOCObyqL3gR1tqyG0vondBz9OtQ5T%2F5wDcW8a5tL8QaGbuY7mfH3sSkN4g7zbeaek%2BBZJeQB5LYFAc0yVbXnAhoO3p%2F5x6o4Bt%2BG1audai7BjwatTD8qm29Ixs8WTQ3gKw8jzzJoAO9%2B437fVKYsFarRnpCBX2rgfCT62N5Ke5thKkxfnL0mNsX42dygAw7eqt0wY6pgFQzZi9dhoOAMu5LCohBlOD%2BBQCExT9YgEZMRclaecP4qk%2F%2F5xbrYkmFRKNeuCTV4qtEO5zlzam%2FAXQunZp1jBB9TqVzM9XfBDxSS%2FcPoUZ3zHNIVIlEyu24yagCV8v2Ijki22OsZBR%2FVGOw21m4M%2BH4vvCEGOKxMSHV%2FDQ8asjALXbpVPb3gzaVvZWbqad0yaenuypk4VYFV9O3VLgEYpUnRBBDuVW&X-Amz-Signature=1387159e2f80eb0d68491facb7ed762c3e41369fd1371e11b9a365f9450b80df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
