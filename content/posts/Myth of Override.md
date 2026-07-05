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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPWEBNC7%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T055411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIC64oQZ2WaXQfm2y%2FWtTrjm1VdjocS8IMkjzVDMvJ%2BdjAiEA2MthcDB%2FN51UFsTa%2BuWKFQVOJAggW6YF%2FzKyJOmafc4q%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDN85ZsNg%2Bo5aiV1y9SrcA8gNU6bxzQT%2BhE11ofHOVUdBDf01wuV0z%2BMX%2FWxbiR7Yx0zqaJfZvP6euZ0w%2BWVwqz4MtSIZFjceGXvgJ1XcltN8Cq0AqVkwcIiyD%2BeQYtYThFE4BstVeCW%2FOU4hv9HSwceTLaCwa5VPUHRLeia0uDbhWLBb9OKSQAmh3Q0EIAAcBIG%2FC3t6Ybg4Hie9c3OYCWUgjPokoV9IFkICcZjAeTXodJgXUephaVOYiwUcRhlP7eHYtQNnlgSJyFczKdc9lOOLBXU0ClJXLNrlyUDjnKcKrLlG%2F9cC7%2FEDjGCTkeeMyL6Sp5WTT9i5SBB6jno60DiC9EQFGkQAgTylBIy4DsourNaxFjpoPukuXakUisHktBDxXeb9elQpS2oDgOETOm3LcO8m%2FHlivIeqkwzruQHZpGnCbjduwI6NXbGXJnEG4lXDH7OcG6pA3EBtnofgSRrNoEuZdrrIyBWpWPRMDluDGIc66idccov28RJ5bwwgJxKF5M92A%2BogB6u9119FuYtmt0K132W%2BFtsCLud2pSIYl9XDWcZTbwUFebUmWPaV3E6zweWKJGSjfxY6x5YgTGwRtJLYEHS41APG7dU5d6b5lg594FTgIbmVY%2BKYvlJMnRBopMHrDiQcBFTMMODbptIGOqUBVBn1Vxz938w%2Fwe5eqrJEnTNZHJo0oA5HhMqkQz5mKi7uJmR5Xt4n9%2Bv3Z5Ci2CdJeBf3Kd5V0GjgoAII8J7VOsdxM%2BKf52yrMfBedWHwWIklKcq2r5hqB3%2BDdMaePsvOhza18MrJhtMlxQXaUK7jLX5bLST6TO8NTT6WmDSJzdLnftg0%2Fxe0qw7VtwkHmiHWMm95nP8EOI3Gnw0f2njESdBYlCp1&X-Amz-Signature=5860c6e6a5a4f1167d6b83d00308d1f01654d55f4958ffb6f547f57d873ac172&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPWEBNC7%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T055411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIC64oQZ2WaXQfm2y%2FWtTrjm1VdjocS8IMkjzVDMvJ%2BdjAiEA2MthcDB%2FN51UFsTa%2BuWKFQVOJAggW6YF%2FzKyJOmafc4q%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDN85ZsNg%2Bo5aiV1y9SrcA8gNU6bxzQT%2BhE11ofHOVUdBDf01wuV0z%2BMX%2FWxbiR7Yx0zqaJfZvP6euZ0w%2BWVwqz4MtSIZFjceGXvgJ1XcltN8Cq0AqVkwcIiyD%2BeQYtYThFE4BstVeCW%2FOU4hv9HSwceTLaCwa5VPUHRLeia0uDbhWLBb9OKSQAmh3Q0EIAAcBIG%2FC3t6Ybg4Hie9c3OYCWUgjPokoV9IFkICcZjAeTXodJgXUephaVOYiwUcRhlP7eHYtQNnlgSJyFczKdc9lOOLBXU0ClJXLNrlyUDjnKcKrLlG%2F9cC7%2FEDjGCTkeeMyL6Sp5WTT9i5SBB6jno60DiC9EQFGkQAgTylBIy4DsourNaxFjpoPukuXakUisHktBDxXeb9elQpS2oDgOETOm3LcO8m%2FHlivIeqkwzruQHZpGnCbjduwI6NXbGXJnEG4lXDH7OcG6pA3EBtnofgSRrNoEuZdrrIyBWpWPRMDluDGIc66idccov28RJ5bwwgJxKF5M92A%2BogB6u9119FuYtmt0K132W%2BFtsCLud2pSIYl9XDWcZTbwUFebUmWPaV3E6zweWKJGSjfxY6x5YgTGwRtJLYEHS41APG7dU5d6b5lg594FTgIbmVY%2BKYvlJMnRBopMHrDiQcBFTMMODbptIGOqUBVBn1Vxz938w%2Fwe5eqrJEnTNZHJo0oA5HhMqkQz5mKi7uJmR5Xt4n9%2Bv3Z5Ci2CdJeBf3Kd5V0GjgoAII8J7VOsdxM%2BKf52yrMfBedWHwWIklKcq2r5hqB3%2BDdMaePsvOhza18MrJhtMlxQXaUK7jLX5bLST6TO8NTT6WmDSJzdLnftg0%2Fxe0qw7VtwkHmiHWMm95nP8EOI3Gnw0f2njESdBYlCp1&X-Amz-Signature=dedc93accdaab014a90cdc8d023b665d208fc9db1c23727f73192ac24d576d0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
