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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AM34T26%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T042931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDFnMvo6xilHUawQ3PKt4EAhjkFZ3VmC5f6ZXlZY8h0AwIgQQWRqGCCgI4U55ZpxSAXO4aV2ILNmRutfUL651gC%2F6cq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDEukH5XM8yF%2B5LLA6yrcA2x%2FXbwaEN0JBZHFR6Wi%2FG7Wwh%2F9qmG5Do8WRP79clBV5L8F5dk8EdBFvojGKVOERLLqTlMmmsTKzxPuJcJRvSkPswvblip8WUi%2F6phfk0oHqKbX2w%2BJqGlZT%2B6z%2F4KDYZF8yUlq8QdVkNH%2BwGt72f92kMp033CD5Ub58ncxnG1ElnpXT1ywB6wSLXQy%2ByhWgbDJODnx4ifjc%2Fzw93ycVK4WLBSd7xtWmw0EBy4l8PucFZjoaCSUjUzbtsdcioHg04IuV%2BAzJh0qLi2brSu0QT8MuBRkVWvS6pEHJbreo6Ew%2FvcUKSe%2FKGovksH%2FzWKyc%2FytVBWgBZcTYdppP44gsxGEi4tm86wxnehBWYQ1MPztRrzS9sEzYEXXjdAEgtYcvmeZcheU0VEkCChgTXJts7ABN26MYY1fujeY2qQ4zLvwAN%2F2bpzGx01TXfgoPWuDhpBkczoEzklpoJu8M8FeQAvTOs26iQgHLB8GNK9q%2B%2FONkrE7aKwMUiYMWQI%2FZlXKXwWN%2F1LF4P2MSfycRDIAn%2FjiLpZB5Ib%2F2IupnR5uJD6SazTOGPxfzU5tlaU3O158bIKUbY84SDA52onaRtnMIV%2BPH4EHWsbGKxyz%2BIsjRRVFMmCQlhVCvp7LfaqBMKDVudQGOqUBha1epBFNtASR7qeTYGyvXjeB2Yh8Ru4NS0RRazm69FFTwQzwqTEMk%2FDtEfHfD5axYGQ1RirOfM0W34S7AtvXl9jp8X1EMEMMUTdg7MMG5uXSZdSgHnTrBoCKPoIDgjEWBHQcRr3oAW%2FwHhZTtNBd5F94A0LARnijrTPIEFqkCaYftMAFwieQw%2Fa89MsYqLyBzOANRwnGm2EkARuShl4E5Xqn4G0Z&X-Amz-Signature=e3fb7003fa4fc8a1d4968591bd6ca934a8ce7f7492b4f6c9cfd77342bfd6c623&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AM34T26%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T042931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDFnMvo6xilHUawQ3PKt4EAhjkFZ3VmC5f6ZXlZY8h0AwIgQQWRqGCCgI4U55ZpxSAXO4aV2ILNmRutfUL651gC%2F6cq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDEukH5XM8yF%2B5LLA6yrcA2x%2FXbwaEN0JBZHFR6Wi%2FG7Wwh%2F9qmG5Do8WRP79clBV5L8F5dk8EdBFvojGKVOERLLqTlMmmsTKzxPuJcJRvSkPswvblip8WUi%2F6phfk0oHqKbX2w%2BJqGlZT%2B6z%2F4KDYZF8yUlq8QdVkNH%2BwGt72f92kMp033CD5Ub58ncxnG1ElnpXT1ywB6wSLXQy%2ByhWgbDJODnx4ifjc%2Fzw93ycVK4WLBSd7xtWmw0EBy4l8PucFZjoaCSUjUzbtsdcioHg04IuV%2BAzJh0qLi2brSu0QT8MuBRkVWvS6pEHJbreo6Ew%2FvcUKSe%2FKGovksH%2FzWKyc%2FytVBWgBZcTYdppP44gsxGEi4tm86wxnehBWYQ1MPztRrzS9sEzYEXXjdAEgtYcvmeZcheU0VEkCChgTXJts7ABN26MYY1fujeY2qQ4zLvwAN%2F2bpzGx01TXfgoPWuDhpBkczoEzklpoJu8M8FeQAvTOs26iQgHLB8GNK9q%2B%2FONkrE7aKwMUiYMWQI%2FZlXKXwWN%2F1LF4P2MSfycRDIAn%2FjiLpZB5Ib%2F2IupnR5uJD6SazTOGPxfzU5tlaU3O158bIKUbY84SDA52onaRtnMIV%2BPH4EHWsbGKxyz%2BIsjRRVFMmCQlhVCvp7LfaqBMKDVudQGOqUBha1epBFNtASR7qeTYGyvXjeB2Yh8Ru4NS0RRazm69FFTwQzwqTEMk%2FDtEfHfD5axYGQ1RirOfM0W34S7AtvXl9jp8X1EMEMMUTdg7MMG5uXSZdSgHnTrBoCKPoIDgjEWBHQcRr3oAW%2FwHhZTtNBd5F94A0LARnijrTPIEFqkCaYftMAFwieQw%2Fa89MsYqLyBzOANRwnGm2EkARuShl4E5Xqn4G0Z&X-Amz-Signature=3ad53d0c285895121fd548f50e80205f4b4b0e370cdf6c3eb3e258844c78ae47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
