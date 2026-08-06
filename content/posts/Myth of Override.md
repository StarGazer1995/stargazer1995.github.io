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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCJKUUWT%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T115622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQD57%2Fb9d8JvxvtJlk0X8c%2F%2BL2iV9eiZLNGN7l4u3rtltwIgHCbh3BGEusu4N%2BcVlH5pL59jmnkZ5a1pBOU8kz%2Bl%2FFYq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDIdcRJZcNQMD44qt%2FCrcAzeQJCej3MKhb0OYjFHdqUScmhmW77dME3HBdb%2FQ71qVFoRZW1ED6iSyHEss%2FUGdskVyk9uCmntgZ6AvKRrSt1DS4WnPZJwnUeijrWXR7YoyafKoerK9WQT6iYWK2uDpP9cfILtRz2n0puLQFu4yfzMIHcyAV%2FKj342a0zwvw4uIC4dcE3HSUsjfJhwjrlyRHuqNDsz3XuvgNrHDKL218wzm%2FPQlL7GFmz6dpOTYy9ewTTwh42kaJsfMJdROMFgUiUAk05%2BE%2Bvfn1S3wEvX%2FbQdLZ5%2BTY6ZC%2Bd62Mucri5Y73GNHhH7LwVfcfKPE%2FoQTLUGuvflrg%2BQclydFdILE1ijsP0WcdGuvq3h087ur0DMp%2FvWdnIlNNkgYUDn03pqD%2FeTeOORXcS%2FjrT2oUkuw3HcrxIsp1J%2Ft%2FFUNT%2BfiYrldY2eHh0VigxZnElPArCHOeyDOfVo5Gw8jQn0a2MR6rMGt4QJumVLE5udFGh3OtP82giSdHh1%2BBJZKjSEsmyqEuFkumd31qZT63mpNZjHB2sAf8O2Usz1FYI%2BUPQ5v%2FLn3ltO8x%2B3pj%2F0TV1a4CJtkd0p0wgheLHJTvXpvJS6XAIy25LyhLwgV9BxUXr%2BCWt3BgIs6T9oSyBrNd%2BrWMKPF0dMGOqUB2i9%2BDwoBso8kU3kbweH6YCqVUTaAmvzPZa7xYwfltAng8f%2FZs1Fgzx6NsKPCNZFsR7%2BeGr21QycGjU3CsdRo5rXhDw2JamtJLOYa44KP8N1TXTsW4Gdd7oheokaUtbfMV0Ob6nTv6EPYn3JPvB6%2Bp%2FJQsDwc9dwRObbzDJZqk%2FYy30%2BCfrXloH874DMD33Tsp6HRZ0pKwZWeIRWTxGORG3yqYJnl&X-Amz-Signature=34ca78c2e8229f7685a9c586da9ab786273457c6ab6bdcc544ae83c6adef3fba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCJKUUWT%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T115622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQD57%2Fb9d8JvxvtJlk0X8c%2F%2BL2iV9eiZLNGN7l4u3rtltwIgHCbh3BGEusu4N%2BcVlH5pL59jmnkZ5a1pBOU8kz%2Bl%2FFYq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDIdcRJZcNQMD44qt%2FCrcAzeQJCej3MKhb0OYjFHdqUScmhmW77dME3HBdb%2FQ71qVFoRZW1ED6iSyHEss%2FUGdskVyk9uCmntgZ6AvKRrSt1DS4WnPZJwnUeijrWXR7YoyafKoerK9WQT6iYWK2uDpP9cfILtRz2n0puLQFu4yfzMIHcyAV%2FKj342a0zwvw4uIC4dcE3HSUsjfJhwjrlyRHuqNDsz3XuvgNrHDKL218wzm%2FPQlL7GFmz6dpOTYy9ewTTwh42kaJsfMJdROMFgUiUAk05%2BE%2Bvfn1S3wEvX%2FbQdLZ5%2BTY6ZC%2Bd62Mucri5Y73GNHhH7LwVfcfKPE%2FoQTLUGuvflrg%2BQclydFdILE1ijsP0WcdGuvq3h087ur0DMp%2FvWdnIlNNkgYUDn03pqD%2FeTeOORXcS%2FjrT2oUkuw3HcrxIsp1J%2Ft%2FFUNT%2BfiYrldY2eHh0VigxZnElPArCHOeyDOfVo5Gw8jQn0a2MR6rMGt4QJumVLE5udFGh3OtP82giSdHh1%2BBJZKjSEsmyqEuFkumd31qZT63mpNZjHB2sAf8O2Usz1FYI%2BUPQ5v%2FLn3ltO8x%2B3pj%2F0TV1a4CJtkd0p0wgheLHJTvXpvJS6XAIy25LyhLwgV9BxUXr%2BCWt3BgIs6T9oSyBrNd%2BrWMKPF0dMGOqUB2i9%2BDwoBso8kU3kbweH6YCqVUTaAmvzPZa7xYwfltAng8f%2FZs1Fgzx6NsKPCNZFsR7%2BeGr21QycGjU3CsdRo5rXhDw2JamtJLOYa44KP8N1TXTsW4Gdd7oheokaUtbfMV0Ob6nTv6EPYn3JPvB6%2Bp%2FJQsDwc9dwRObbzDJZqk%2FYy30%2BCfrXloH874DMD33Tsp6HRZ0pKwZWeIRWTxGORG3yqYJnl&X-Amz-Signature=c08d194c5b678822895a5a5b70d83a407647b5e0de7c73be32bf8254c94b3cae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
