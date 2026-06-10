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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCOYMIAT%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T080000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIA2O77gC7S1L9XyZeZdseGlKkivd%2B3pCZqov%2FYCKp5IdAiEA064Mg6JNCql5e1ddlsWXAcdvpGzBJtlvbulIeUjieSMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvGM8avLpAN3JFFwSrcA75s%2Bp9oVrYO%2FyThFwf0yZnmggGBKwzfx6EYEaa2Jx0ZQyBmp64U9uO%2Fo0hXib%2B3HXviskm4ue%2FMwgU7ovR0OiUivOzKNEWzfYygU1dAscXOmXib0R6jSATjM2a0sioGHEN%2F%2ByUQJOSAUIMMPRjFS4pNXGCIbQlNsMt6U2%2B%2BiG0Jor0ZKokAC34ZvNmKC5UXbRCs%2F8bUlVA1Iz0LIgik5x363q%2Bzo%2Fk7VtZ1YLU8bWT3EU8p4Gsw4sizDZ%2F1ea0jyFp0dKaEKFHr92wBvhjPKaXyWWytSTwGpR5y6p1sotMOS14S%2Bl%2F4fmwM1of%2FZndauxr6Prk%2BgZa6Ch4L8H7JwuY7lZjDIbhIf0A5oiz8j90bf8xwmHqiohjES5UgsgYYm4r%2BN76dO5b8sg0r%2BpnLom9azzKhhYuaurYpv8WqZZEHIBXQSP%2B8j4DRMW4ji4zBmd1h194B9vYbRKgHbllVSN5D0XIcIg%2BBoitFweV2FBsji65r129s7NRM1KLfJue%2BvOFtyxqMjaBWDtte5ZaPkmyhvA%2Fw4AOrM37E3Nm2%2FQA9yefEncT5UVYlBxWdoh%2BjXAZpsHch0kdtYmFddfFulo9boMoNQjhDgYn2lG9x9sg1S8KFbPfMfkvBXQbDMNSrpNEGOqUBZJfDSymC%2BixLyXsEPA4OwMrLn9s2AnnlRrt0NcKkM4xbWrF6DbH2DZRlue47sqb1xtx8%2FTvIPBdiqJauiDyy6bFKKIZy0XBdq3eHix%2FmL%2FGgwLYOLcj7d0Eq4yFAtRJSYK8QuwWvApVjIHovD%2BOniWADP3MPt26Cs%2FeFP8lguy8JBOAt8xIMto6oPQyy6%2Bb9ZYhQw%2FAJee6SjoGKVQbTUv9cGMRI&X-Amz-Signature=31d657c2778b8574311ae0ae8917083dff2ed265127a468dd2cd56300b98bdff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCOYMIAT%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T080000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIA2O77gC7S1L9XyZeZdseGlKkivd%2B3pCZqov%2FYCKp5IdAiEA064Mg6JNCql5e1ddlsWXAcdvpGzBJtlvbulIeUjieSMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvGM8avLpAN3JFFwSrcA75s%2Bp9oVrYO%2FyThFwf0yZnmggGBKwzfx6EYEaa2Jx0ZQyBmp64U9uO%2Fo0hXib%2B3HXviskm4ue%2FMwgU7ovR0OiUivOzKNEWzfYygU1dAscXOmXib0R6jSATjM2a0sioGHEN%2F%2ByUQJOSAUIMMPRjFS4pNXGCIbQlNsMt6U2%2B%2BiG0Jor0ZKokAC34ZvNmKC5UXbRCs%2F8bUlVA1Iz0LIgik5x363q%2Bzo%2Fk7VtZ1YLU8bWT3EU8p4Gsw4sizDZ%2F1ea0jyFp0dKaEKFHr92wBvhjPKaXyWWytSTwGpR5y6p1sotMOS14S%2Bl%2F4fmwM1of%2FZndauxr6Prk%2BgZa6Ch4L8H7JwuY7lZjDIbhIf0A5oiz8j90bf8xwmHqiohjES5UgsgYYm4r%2BN76dO5b8sg0r%2BpnLom9azzKhhYuaurYpv8WqZZEHIBXQSP%2B8j4DRMW4ji4zBmd1h194B9vYbRKgHbllVSN5D0XIcIg%2BBoitFweV2FBsji65r129s7NRM1KLfJue%2BvOFtyxqMjaBWDtte5ZaPkmyhvA%2Fw4AOrM37E3Nm2%2FQA9yefEncT5UVYlBxWdoh%2BjXAZpsHch0kdtYmFddfFulo9boMoNQjhDgYn2lG9x9sg1S8KFbPfMfkvBXQbDMNSrpNEGOqUBZJfDSymC%2BixLyXsEPA4OwMrLn9s2AnnlRrt0NcKkM4xbWrF6DbH2DZRlue47sqb1xtx8%2FTvIPBdiqJauiDyy6bFKKIZy0XBdq3eHix%2FmL%2FGgwLYOLcj7d0Eq4yFAtRJSYK8QuwWvApVjIHovD%2BOniWADP3MPt26Cs%2FeFP8lguy8JBOAt8xIMto6oPQyy6%2Bb9ZYhQw%2FAJee6SjoGKVQbTUv9cGMRI&X-Amz-Signature=e831781c3d5d0dde70de24e954c06d22e0534d5c0da3891ec232c65f4a5ff620&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
