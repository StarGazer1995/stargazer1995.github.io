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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C5SEXLG%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T161854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5asrQpzVEeW4ParHsRi6A49y9f8KNZj9WvSk%2BmhQlOAiEAu5nN%2FmoLH4ds8oeuvMTP8d8m2I1UX7VBpSKmkslaVP8qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCp4IoDx0n5HyrBgCrcA%2BAUXblhVft%2Fp7lcChSLxzEKTrR0ztoR%2BJjfjRFrTz8UWqC0QXABzVvsLVjr4CTVfLnlEQ%2BfZdeL1YB0H6O2%2BFywMas3Q6ysAo2nVMXktJnaZ4UO9PUX8vDwGz3CtiivfRsAqwcBKf7%2B9dOT117SqmVL174IU8kPP8FYN6OH1M1Uo%2BxjGew9LyCcrX5UtLj6URA%2FleEr4cSelo9XduxP46v9%2FNPWtUwbF4Z%2BNhy%2FWYsrtMnFVFc2n1vKvWYgrQYCd6r9FhF4r6vXmgUftV%2FTbqrd72hilWIBIYcN7Nnlqc3ISXu7mBX%2BNK2LWzrT1JVm6C6Qip4BRgQWodOmkbZVg9UQSibFuWg5oNmG5HwOsxqoEYYurt9prK4TZmFklZ0aOaV1X5TiAQAzl%2F2lrd3Mw0dAErdRcdeP8Ow7bsyd8D9ZQXj1lDj0y7oscr7R3R3Ja%2BW6p5LofNPZ7RawlrXDLNLCtdPMa7lsFzYtNu%2FKT66kviN1BFqingOnfTT0vdpKPuKX6wlRzYr6qURllo4f6sWEvrerBIk0FdiEGi%2FNfqzzzR%2BPpJvfyXglymLgciOpqMUUvDLHZn7kdvp1fF2Z5WxlTL5cJY6c3FVAeVMIpJ3GWzyccaC4W1le8NyAMOXBodQGOqUBzRuepaArd1jN0sb%2BP4hGsEGGk6ZxyGlA9D9H45gZBINjnAqTvzOyiXwWj6WOUtEPU4VGjH8G%2B32DtoR1%2F%2BbDyo78UZybuhSNluaBkOpIrVah2hL%2Ba2Y15aORhA3Ike1EoxfIqIxXVldyg7V7kE%2BiWmo25wSBErEBM1MwvRyY8XSQii70Ony3SjwC6cZkdwBCRabm%2Fer2PVUtiT0QsVQjS45I8sg8&X-Amz-Signature=568a45da9a6b3cd8e77ad0b62ccd5ae93d572d86144a027fc17fdcef513ba93b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C5SEXLG%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T161854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5asrQpzVEeW4ParHsRi6A49y9f8KNZj9WvSk%2BmhQlOAiEAu5nN%2FmoLH4ds8oeuvMTP8d8m2I1UX7VBpSKmkslaVP8qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCp4IoDx0n5HyrBgCrcA%2BAUXblhVft%2Fp7lcChSLxzEKTrR0ztoR%2BJjfjRFrTz8UWqC0QXABzVvsLVjr4CTVfLnlEQ%2BfZdeL1YB0H6O2%2BFywMas3Q6ysAo2nVMXktJnaZ4UO9PUX8vDwGz3CtiivfRsAqwcBKf7%2B9dOT117SqmVL174IU8kPP8FYN6OH1M1Uo%2BxjGew9LyCcrX5UtLj6URA%2FleEr4cSelo9XduxP46v9%2FNPWtUwbF4Z%2BNhy%2FWYsrtMnFVFc2n1vKvWYgrQYCd6r9FhF4r6vXmgUftV%2FTbqrd72hilWIBIYcN7Nnlqc3ISXu7mBX%2BNK2LWzrT1JVm6C6Qip4BRgQWodOmkbZVg9UQSibFuWg5oNmG5HwOsxqoEYYurt9prK4TZmFklZ0aOaV1X5TiAQAzl%2F2lrd3Mw0dAErdRcdeP8Ow7bsyd8D9ZQXj1lDj0y7oscr7R3R3Ja%2BW6p5LofNPZ7RawlrXDLNLCtdPMa7lsFzYtNu%2FKT66kviN1BFqingOnfTT0vdpKPuKX6wlRzYr6qURllo4f6sWEvrerBIk0FdiEGi%2FNfqzzzR%2BPpJvfyXglymLgciOpqMUUvDLHZn7kdvp1fF2Z5WxlTL5cJY6c3FVAeVMIpJ3GWzyccaC4W1le8NyAMOXBodQGOqUBzRuepaArd1jN0sb%2BP4hGsEGGk6ZxyGlA9D9H45gZBINjnAqTvzOyiXwWj6WOUtEPU4VGjH8G%2B32DtoR1%2F%2BbDyo78UZybuhSNluaBkOpIrVah2hL%2Ba2Y15aORhA3Ike1EoxfIqIxXVldyg7V7kE%2BiWmo25wSBErEBM1MwvRyY8XSQii70Ony3SjwC6cZkdwBCRabm%2Fer2PVUtiT0QsVQjS45I8sg8&X-Amz-Signature=48a31c304eb2894121cdf355b37bedbcfd5d1abf4595811ba7f1abc613ce11a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
