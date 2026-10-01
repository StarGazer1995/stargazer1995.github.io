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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDLGPYMG%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T005452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpkZW%2B5N8mxZwdmqTgx6Wb4%2FjdfXJ8C25QHJHyJxAD2gIgQXMzYE0DVqFStOjHH6m7S4zse9wGmseC4qY27xGf8BMq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDI2FEtWI7Hbad%2FO0tircA1K7Y9%2F7LDm4O87aQvOkF5FtPTQQk08HGh%2BUfSCHikriNrvaLYCWAS089cWkDxmT%2FDdHWpJwzRrgi1luLloCEHud3QVGXLgB6FAG9v88CGbjFLHrHfvSrcYtt0sCr3cuJufPgHtCEmbBPfZ6LCXj6KWXAabU38CjQIFv%2B%2BhB2QSUCyRR09OAU%2FCg2fZtsc6W%2B167Qf3%2FcwB0b9g2AyoVlh%2Fsjv6ek6gfdv1XaChOgm6k5xKYCyZuqx8GjU7LHcG5eh%2Bs1pZ%2Fh3R3SOuOEGcg0%2BB%2FzH74%2Bks%2BDOCqPt9MogXkoGJbzOJKI2JQqOqYg6uzeQTsO9agW5fhpLtdnJKk0FDw2UXBuqkyt2HE5v8fFGvjOG%2FWi1UMfTFT4xrPcdBKxFCVKjklT%2FFR0zzjIVOGb0R0cJ2vl7cVx5qOFFtH3ya2%2FEPzWGpXXC3SXHRgRcBosFNZutPz9B6%2FuH%2FgsAbFS38xhv%2B13BdfZb5ckaeBQ0O55izuwihGkL%2BHWz8CACWRs47999FBtF9Upgr6ory5f33GKP9%2BHA6pI2Lts6ajU3mBxY20DfXVc2VHD9Y4y70WGvc64eU%2FLb4jHG5ns50r%2BjsRHoqX6NTn9E81U1Dk7bjT6NGJ8L1SWWCffFW2MMKg9tUGOqUBEUEkcSHOVA%2B%2BhpXtkPg%2FOhUtN4awQK0PH0jDKOBB%2BGoPslvq4riDgSF4ZmmzMouszL6D4p446ruWo9lZCWga4Fhwik7YhY1bubBKyQ%2BV5%2Fxo5fIfAOa1bJNaUOJdo1DDD%2FpKJtcbzGhMLGDFQbzAudBS8%2FZnk5KZ6pYraqiKb6si2HqvZBrg4JT6TN1v1OMfqxyhSjcv3dsZhW%2FC%2Fqckq3aHCPW9&X-Amz-Signature=c9fdde5c9fcd9bf65858504e3e4884ca5bcdb2d296f106f935bbbc40caf562e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDLGPYMG%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T005452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpkZW%2B5N8mxZwdmqTgx6Wb4%2FjdfXJ8C25QHJHyJxAD2gIgQXMzYE0DVqFStOjHH6m7S4zse9wGmseC4qY27xGf8BMq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDI2FEtWI7Hbad%2FO0tircA1K7Y9%2F7LDm4O87aQvOkF5FtPTQQk08HGh%2BUfSCHikriNrvaLYCWAS089cWkDxmT%2FDdHWpJwzRrgi1luLloCEHud3QVGXLgB6FAG9v88CGbjFLHrHfvSrcYtt0sCr3cuJufPgHtCEmbBPfZ6LCXj6KWXAabU38CjQIFv%2B%2BhB2QSUCyRR09OAU%2FCg2fZtsc6W%2B167Qf3%2FcwB0b9g2AyoVlh%2Fsjv6ek6gfdv1XaChOgm6k5xKYCyZuqx8GjU7LHcG5eh%2Bs1pZ%2Fh3R3SOuOEGcg0%2BB%2FzH74%2Bks%2BDOCqPt9MogXkoGJbzOJKI2JQqOqYg6uzeQTsO9agW5fhpLtdnJKk0FDw2UXBuqkyt2HE5v8fFGvjOG%2FWi1UMfTFT4xrPcdBKxFCVKjklT%2FFR0zzjIVOGb0R0cJ2vl7cVx5qOFFtH3ya2%2FEPzWGpXXC3SXHRgRcBosFNZutPz9B6%2FuH%2FgsAbFS38xhv%2B13BdfZb5ckaeBQ0O55izuwihGkL%2BHWz8CACWRs47999FBtF9Upgr6ory5f33GKP9%2BHA6pI2Lts6ajU3mBxY20DfXVc2VHD9Y4y70WGvc64eU%2FLb4jHG5ns50r%2BjsRHoqX6NTn9E81U1Dk7bjT6NGJ8L1SWWCffFW2MMKg9tUGOqUBEUEkcSHOVA%2B%2BhpXtkPg%2FOhUtN4awQK0PH0jDKOBB%2BGoPslvq4riDgSF4ZmmzMouszL6D4p446ruWo9lZCWga4Fhwik7YhY1bubBKyQ%2BV5%2Fxo5fIfAOa1bJNaUOJdo1DDD%2FpKJtcbzGhMLGDFQbzAudBS8%2FZnk5KZ6pYraqiKb6si2HqvZBrg4JT6TN1v1OMfqxyhSjcv3dsZhW%2FC%2Fqckq3aHCPW9&X-Amz-Signature=7b29a73884d21e27e304b64a9f3756775c4075a15a20f59cb77c46d63e214b28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
