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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR3RLEGO%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T190322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDf1MgKNPDSPG%2Fr8kIFshpbtJArTiMmsYEkzAnlsfuN%2FwIhAOgn2K1erF832zE55%2FM%2BFkqd3O%2B1xU26B%2FH%2Fpy1t2YWcKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbYiwpvN5f34SFmHgq3AMOnwgVDAxKw8C5IrOCLBEZ5ijD7GSW3rtZsoyDfflk0mix%2FDbQGv82RcWO9Qw666A5JYN4XpurA0xSQYaHgmxw12ukR5EXISlrRixGJ%2FJsQqjyQBt37uVghxmpvB0fQBOen9ALvXrC%2F0f5F0RQoJRAg3ZR8XFWeISPleF6TjQW8afJZA58vFiTUuzcCPzrv4v3tc1pwH9bKqXCOY0jtB%2FcdwxfemDoZKRW9a2aSLnAISbhS0lENu4z1e%2BzPTDE88gFxrbI5FJKf8jTnwMVmAFRliszstdoLMWZ0LMgmQQsJraTEAJsv4eKyoiFsXLlTh1d1gbm37XDBx3x13BsHJ35FUa22O7%2BfZIY8bU%2FIsO5ZiflJgFKzNJpEQ77ARhz2VmO4g0ebjdQ4etnyQY01Q1ZqKJzgZozT0CRrzVQXz3YuenpEctvTuyXfMz1rUF3S6tYUXPqaIFQJptGn7SvfikKoBUQ%2FWORdZ8SSzlduw0%2B7srDiF%2FxrE1EZDboa50hwJeDTDaCHIsIvgw827XCOrabu4tLQ5tmOUOay953YnSVB8lV%2Fk%2FhEs69GPeB0R57zP9jjBcBNEfz8s2FBMGQZtu%2FRoI1gUL5tqkh9Jfu7G7YdIBkoHjACNB42vjRtzD4wPjPBjqkATbSuH4Z5x1q6%2FuL3YkPBUXA%2F8PlxSedB0P0oyvplpSd%2Bd3RHlRRJ0AgzarqdLUWwNwsXtWM9%2B3XcDc9yhGfl3zN5KavCVL5MsEazoNRSeC3Fh7aMpQ0EI%2FhEQaJ9VNieV%2FXWG25HXRsMkbPCFi%2BmuFkP9P3MbP7V0dQap87e4duX4TUy9xzsRVVWqo%2FIdNGanovtC1eeqqqyL2B5bioVnQ962Ue&X-Amz-Signature=c1563804b2b5e3d93f5a456d9b41d07ec455861e28cdaaeda2349f6258c1e76b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR3RLEGO%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T190322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDf1MgKNPDSPG%2Fr8kIFshpbtJArTiMmsYEkzAnlsfuN%2FwIhAOgn2K1erF832zE55%2FM%2BFkqd3O%2B1xU26B%2FH%2Fpy1t2YWcKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzbYiwpvN5f34SFmHgq3AMOnwgVDAxKw8C5IrOCLBEZ5ijD7GSW3rtZsoyDfflk0mix%2FDbQGv82RcWO9Qw666A5JYN4XpurA0xSQYaHgmxw12ukR5EXISlrRixGJ%2FJsQqjyQBt37uVghxmpvB0fQBOen9ALvXrC%2F0f5F0RQoJRAg3ZR8XFWeISPleF6TjQW8afJZA58vFiTUuzcCPzrv4v3tc1pwH9bKqXCOY0jtB%2FcdwxfemDoZKRW9a2aSLnAISbhS0lENu4z1e%2BzPTDE88gFxrbI5FJKf8jTnwMVmAFRliszstdoLMWZ0LMgmQQsJraTEAJsv4eKyoiFsXLlTh1d1gbm37XDBx3x13BsHJ35FUa22O7%2BfZIY8bU%2FIsO5ZiflJgFKzNJpEQ77ARhz2VmO4g0ebjdQ4etnyQY01Q1ZqKJzgZozT0CRrzVQXz3YuenpEctvTuyXfMz1rUF3S6tYUXPqaIFQJptGn7SvfikKoBUQ%2FWORdZ8SSzlduw0%2B7srDiF%2FxrE1EZDboa50hwJeDTDaCHIsIvgw827XCOrabu4tLQ5tmOUOay953YnSVB8lV%2Fk%2FhEs69GPeB0R57zP9jjBcBNEfz8s2FBMGQZtu%2FRoI1gUL5tqkh9Jfu7G7YdIBkoHjACNB42vjRtzD4wPjPBjqkATbSuH4Z5x1q6%2FuL3YkPBUXA%2F8PlxSedB0P0oyvplpSd%2Bd3RHlRRJ0AgzarqdLUWwNwsXtWM9%2B3XcDc9yhGfl3zN5KavCVL5MsEazoNRSeC3Fh7aMpQ0EI%2FhEQaJ9VNieV%2FXWG25HXRsMkbPCFi%2BmuFkP9P3MbP7V0dQap87e4duX4TUy9xzsRVVWqo%2FIdNGanovtC1eeqqqyL2B5bioVnQ962Ue&X-Amz-Signature=775175d2e317f82caed9ff17887cb9f5be1e3f279d6264e6c617382bd6210eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
