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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCVUOF2P%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T015038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICY3Ja%2FxCbzB18yvDPirX35qIINPby2c%2BBQM72bowLuEAiA8JpqB0Nr7vkW72bFdRJF%2FT5dJQCdYc%2Fk5Tu6LiOd8rCqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrqfua5chem7jrpSKtwDl05n3%2B2LbFIuFh4XhnvmDcjh1VwCENe5kL8vKXgSJLtTO6F4RVLTYWm%2FCB2aQlWaBrTaJ8DRQviowqk3kj6luTVQdTuCMv7%2B3nQ6g8gYq34eJzoLfcHBxaLK%2FXuRTtXZlleuxNfUeJVLoSkGBafZyDXBhfZfaOXSYOUw2Sv5uaCnwOykW7sQyu7fT3Jj0Bpc44wWMYMrSGRz%2Fyfv%2BcatSW6bOD9vk00uheAwph4ysUejImlLtDi0hP%2BT9ryZ2dvDAKC1NCdxbTFwyzUt%2BvdBOvwu3IkwIOL4UnhPk2WvtJjCkMHgRF4n50MvRuAAtES3ktOqsooMB%2Fu82DfKmMg0wLHwwNbTIlHnBOV0sHY3Znnkxuor%2BC7KW%2BscAgf2ujN17sSTCqIep9NC2Y4AOUGAmwpoRBqqGwvp7Wz6uJsGpD%2BfsLxf8Hswo4UAeQdw8psR5NGqdxS2t8mMD36IvvK7wGtL7aEufCegceF52aqKH5JtAT7vDJBsQ5POCQL%2B32PC6NCQb7I8QAaDMjPFB4xBeQLf1SahQqUAc4I9VCHVnmzYFcnW%2FUU%2BypMhr2iZhiu%2BJpg1cj%2BTJn6VNgoSV1jDSL8P51mSyRxKHnC6752%2BukyGjG71geh6IFSytuMw%2BObd0AY6pgGBWlXOXnPKRu0nY00onuBZ9W9x%2FMVV4mNHxqncpsZTLl2Mr2O3o5rRso%2BxcYVAOex4vGxHVwwnJKTH%2Byc6YilpZM5VehHA16iC9ELCRLoyUXwIEZPz%2BT13wrdAaJPPL8EzAAssQCThyCF7Xr7dPEDjDdE%2B87ZhnyC9foAxaqS74DPynk%2BsISlqQM10v1NGx%2B58l%2F5DXqDEQaK3yLzg9CFN0chScZDE&X-Amz-Signature=6b8d89476a98ce776df9a23015ff7300d0d44a759dafa2e3f26c1383be577e02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCVUOF2P%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T015038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICY3Ja%2FxCbzB18yvDPirX35qIINPby2c%2BBQM72bowLuEAiA8JpqB0Nr7vkW72bFdRJF%2FT5dJQCdYc%2Fk5Tu6LiOd8rCqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrqfua5chem7jrpSKtwDl05n3%2B2LbFIuFh4XhnvmDcjh1VwCENe5kL8vKXgSJLtTO6F4RVLTYWm%2FCB2aQlWaBrTaJ8DRQviowqk3kj6luTVQdTuCMv7%2B3nQ6g8gYq34eJzoLfcHBxaLK%2FXuRTtXZlleuxNfUeJVLoSkGBafZyDXBhfZfaOXSYOUw2Sv5uaCnwOykW7sQyu7fT3Jj0Bpc44wWMYMrSGRz%2Fyfv%2BcatSW6bOD9vk00uheAwph4ysUejImlLtDi0hP%2BT9ryZ2dvDAKC1NCdxbTFwyzUt%2BvdBOvwu3IkwIOL4UnhPk2WvtJjCkMHgRF4n50MvRuAAtES3ktOqsooMB%2Fu82DfKmMg0wLHwwNbTIlHnBOV0sHY3Znnkxuor%2BC7KW%2BscAgf2ujN17sSTCqIep9NC2Y4AOUGAmwpoRBqqGwvp7Wz6uJsGpD%2BfsLxf8Hswo4UAeQdw8psR5NGqdxS2t8mMD36IvvK7wGtL7aEufCegceF52aqKH5JtAT7vDJBsQ5POCQL%2B32PC6NCQb7I8QAaDMjPFB4xBeQLf1SahQqUAc4I9VCHVnmzYFcnW%2FUU%2BypMhr2iZhiu%2BJpg1cj%2BTJn6VNgoSV1jDSL8P51mSyRxKHnC6752%2BukyGjG71geh6IFSytuMw%2BObd0AY6pgGBWlXOXnPKRu0nY00onuBZ9W9x%2FMVV4mNHxqncpsZTLl2Mr2O3o5rRso%2BxcYVAOex4vGxHVwwnJKTH%2Byc6YilpZM5VehHA16iC9ELCRLoyUXwIEZPz%2BT13wrdAaJPPL8EzAAssQCThyCF7Xr7dPEDjDdE%2B87ZhnyC9foAxaqS74DPynk%2BsISlqQM10v1NGx%2B58l%2F5DXqDEQaK3yLzg9CFN0chScZDE&X-Amz-Signature=2d191a4cae369e4928695029920df084ff6265d83076158c626029277b3a68db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
