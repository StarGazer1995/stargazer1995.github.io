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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RPQYWEH%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJGMEQCIFU7lfTievKfEswxjV%2FMs0BOnkFexnBM6%2FKbaTn%2BH%2FS9AiB84DWFcIlAHbP55X5Hs%2FTWExLI1kd616zgJEkIe3u7aSqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW46cDkF9voUlZbMxKtwDcinqbMGR4EDoMUmuqxCxLGcPQllpPXHkvvL5PcsvC0R%2Bmr0irY2n64zBKrFt%2FxyOcZodWdtrGFOYue3hGDKmIaue5sRD6EPoVl6Ih4LjEx5iqkqmiQCjOjLLDSg%2BG2%2B2eBKCTH%2Fgac85XVkgqsmO19xUVTTkI1sJBQgFoB6XORh8f37Dhi%2BJNf34pi%2BTswXaflPBYpC4nQyAtRHSfvPMPD%2FeGiKD8V%2FbUFsucn4UYMOB1pEY%2FL%2B%2BvEwV%2F%2FwqXmdOodl4Ja3osexxUNm%2BIOUJQODIq2cyVfyrWoDP8ioE0x3F%2B5GqN2dDV9mVF%2F3dOWhUA%2B2dcgAwZStpzxNbXbvWi%2FuJOpjypXD3QcoClehQPMXvYoBbac4AEflodNToKmRZ7LOv%2BDSMFU1d3vJ1RjMy%2FcAXby1Qm7qRPcKpFJRa9Y9LI178A6UXwGnJBwgSiXcg8hJQSh2ArdHTyAz4f7430m2KdzjbLIJYFrnBbVCavNljYQ34FOPCzeVgmU6eJvnCwQcRYibb91Rn%2BmXpjkSV3llypMB%2FQG7gl07aAhF1jlGFoZ8yjjSxnoslW8PX3wBoVp2rpHV%2FN4q5H2ypJc1qaHBBNSQKcgIy7VI7lziEtkUT0YLpAcNhTvLN0Kow2LvN1gY6pgHQ74FXPQdFRIn0tOV4ZcBTnyn1dcn6it5uQV3ckHWLyRB2GjpKqmZDO8ovRF1cAFgEVQfLUi3ZQ4KgeFRj6n2iVczDd8HaEviTFdNp0W%2F7eaVF4C5NXHjbLYR5OXbFonVkUYd0n1oIA%2FtFpzdjodAIY%2BBtunCLFTt06f%2BQ4utmWpG9jOkYAtfDSIMKc9ojmMumzoLtx7WKkOQlXkrOo%2F5CwF0eYGPQ&X-Amz-Signature=66f2ef403e387d8e7e5e440f2c80b4a7fbfc467cc10e2144cfa7bffec91f7cd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RPQYWEH%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJGMEQCIFU7lfTievKfEswxjV%2FMs0BOnkFexnBM6%2FKbaTn%2BH%2FS9AiB84DWFcIlAHbP55X5Hs%2FTWExLI1kd616zgJEkIe3u7aSqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW46cDkF9voUlZbMxKtwDcinqbMGR4EDoMUmuqxCxLGcPQllpPXHkvvL5PcsvC0R%2Bmr0irY2n64zBKrFt%2FxyOcZodWdtrGFOYue3hGDKmIaue5sRD6EPoVl6Ih4LjEx5iqkqmiQCjOjLLDSg%2BG2%2B2eBKCTH%2Fgac85XVkgqsmO19xUVTTkI1sJBQgFoB6XORh8f37Dhi%2BJNf34pi%2BTswXaflPBYpC4nQyAtRHSfvPMPD%2FeGiKD8V%2FbUFsucn4UYMOB1pEY%2FL%2B%2BvEwV%2F%2FwqXmdOodl4Ja3osexxUNm%2BIOUJQODIq2cyVfyrWoDP8ioE0x3F%2B5GqN2dDV9mVF%2F3dOWhUA%2B2dcgAwZStpzxNbXbvWi%2FuJOpjypXD3QcoClehQPMXvYoBbac4AEflodNToKmRZ7LOv%2BDSMFU1d3vJ1RjMy%2FcAXby1Qm7qRPcKpFJRa9Y9LI178A6UXwGnJBwgSiXcg8hJQSh2ArdHTyAz4f7430m2KdzjbLIJYFrnBbVCavNljYQ34FOPCzeVgmU6eJvnCwQcRYibb91Rn%2BmXpjkSV3llypMB%2FQG7gl07aAhF1jlGFoZ8yjjSxnoslW8PX3wBoVp2rpHV%2FN4q5H2ypJc1qaHBBNSQKcgIy7VI7lziEtkUT0YLpAcNhTvLN0Kow2LvN1gY6pgHQ74FXPQdFRIn0tOV4ZcBTnyn1dcn6it5uQV3ckHWLyRB2GjpKqmZDO8ovRF1cAFgEVQfLUi3ZQ4KgeFRj6n2iVczDd8HaEviTFdNp0W%2F7eaVF4C5NXHjbLYR5OXbFonVkUYd0n1oIA%2FtFpzdjodAIY%2BBtunCLFTt06f%2BQ4utmWpG9jOkYAtfDSIMKc9ojmMumzoLtx7WKkOQlXkrOo%2F5CwF0eYGPQ&X-Amz-Signature=e5452a456feb94f133fc8436a95718d4c18cbb9ff28386fe2daa215cad89e7dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
