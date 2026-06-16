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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFGWR7EL%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T145225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLLibNtN5r93pL57VKqnWYs%2Bon8Dx0q4uqAY941AA9SgIhAKb16k5wPSDpp0BkxGPiB%2BDbNoVW2SYroFYBRPcB83rnKv8DCHcQABoMNjM3NDIzMTgzODA1IgxrkibPxnHe6hgTEnsq3AMtfka1CrhPcloD%2BbFV5%2BHNlzRjJpBd8k6txGkuLfHgojPC4QqP8umg6bHyXYe53b1tHZ%2FGqGMvJar4cHy8T1d44%2BoN52ggS0nNMLzzEXp6hdsfju9lKyiiJwnU613leNHo6bbGcjP3s%2BevkedxZC%2BKDjUBAYx3h9GKtM%2FL81p3YEKLiohBg3iRwFXjMOPMf5DYtpBGVe2KCcz%2B7CDW%2FPktemoJ4hSXQmoYxvi%2FxTWGZyioYEtgcx92aahuwtNuSsUy4IyEAZzS%2BTgqhTvoiK63OLPk5ge3YO4MdSp0N3%2BtIDioISUsxiCjpSalq2kuOa3pr1Lng9jtgXenin5Da6In9RXcPZZA%2FhB%2BhqGSJm0Y%2B5AqZPT1HFTLfho%2B0l8JujCIir%2BlAuRBRWxD3ppgX1mS%2F6qjHOOWuB4eQZ4dDrhlkMC7M3iuXOLXqyJP5YLHF5JP8kRzMs6tYtP9zNNwHTZwwtb85vUrrYq1%2BJVesiy5dVbox1YsiseLiYB9gIOi3YZ5VolOYDhSNgweHnABu7oaTQ%2FjzfMahIzDOyMSNgvSSMkqW8lmho4twZarWkmOjpVz4vzFi9g1OVoJ6v2zPDVKQA1e9P%2B5EBn3f%2BRQktZTuD%2Buf2ddL2GJyz57DDCoq8XRBjqkAU0bMve%2BHlg88UyQM6LLqi0bNmYa3whmxWW7fidXsx27cf7VBfsWqOS%2FzdjGCuWJ2REx%2B0Ts3UoaWtgVfRSlAp5QQD8ip7%2FZHxkMygNLPtS07g42RjH7Y84X4RWLL81ejuufCb3kNyUKwB%2FEEPx%2BS5uUHbrgS7SBMlAAWEXJvh9PrqENKntVNwerGaYN9qu8%2BAvLnW8nwSIKIC75tB4JO38ZtVux&X-Amz-Signature=05f43b68bf7a04d7f83c8a2d378ce84f3b5654588d2fdc81f2fa6cd8eb1a2e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFGWR7EL%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T145225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLLibNtN5r93pL57VKqnWYs%2Bon8Dx0q4uqAY941AA9SgIhAKb16k5wPSDpp0BkxGPiB%2BDbNoVW2SYroFYBRPcB83rnKv8DCHcQABoMNjM3NDIzMTgzODA1IgxrkibPxnHe6hgTEnsq3AMtfka1CrhPcloD%2BbFV5%2BHNlzRjJpBd8k6txGkuLfHgojPC4QqP8umg6bHyXYe53b1tHZ%2FGqGMvJar4cHy8T1d44%2BoN52ggS0nNMLzzEXp6hdsfju9lKyiiJwnU613leNHo6bbGcjP3s%2BevkedxZC%2BKDjUBAYx3h9GKtM%2FL81p3YEKLiohBg3iRwFXjMOPMf5DYtpBGVe2KCcz%2B7CDW%2FPktemoJ4hSXQmoYxvi%2FxTWGZyioYEtgcx92aahuwtNuSsUy4IyEAZzS%2BTgqhTvoiK63OLPk5ge3YO4MdSp0N3%2BtIDioISUsxiCjpSalq2kuOa3pr1Lng9jtgXenin5Da6In9RXcPZZA%2FhB%2BhqGSJm0Y%2B5AqZPT1HFTLfho%2B0l8JujCIir%2BlAuRBRWxD3ppgX1mS%2F6qjHOOWuB4eQZ4dDrhlkMC7M3iuXOLXqyJP5YLHF5JP8kRzMs6tYtP9zNNwHTZwwtb85vUrrYq1%2BJVesiy5dVbox1YsiseLiYB9gIOi3YZ5VolOYDhSNgweHnABu7oaTQ%2FjzfMahIzDOyMSNgvSSMkqW8lmho4twZarWkmOjpVz4vzFi9g1OVoJ6v2zPDVKQA1e9P%2B5EBn3f%2BRQktZTuD%2Buf2ddL2GJyz57DDCoq8XRBjqkAU0bMve%2BHlg88UyQM6LLqi0bNmYa3whmxWW7fidXsx27cf7VBfsWqOS%2FzdjGCuWJ2REx%2B0Ts3UoaWtgVfRSlAp5QQD8ip7%2FZHxkMygNLPtS07g42RjH7Y84X4RWLL81ejuufCb3kNyUKwB%2FEEPx%2BS5uUHbrgS7SBMlAAWEXJvh9PrqENKntVNwerGaYN9qu8%2BAvLnW8nwSIKIC75tB4JO38ZtVux&X-Amz-Signature=1713749de6cecbcc7fe6997fd7f5185a721f76016440d28ab6d6511522d199e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
