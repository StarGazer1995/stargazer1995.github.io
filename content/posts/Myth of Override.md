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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TCJRLHU%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T134143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHA9fkYU7HtWcgLBOv0Y2jQvlnhW8t%2FScwqybW2TxN9IAiEAzdIMowv7lwtAoLqPgwL0VOCrqChc9Az0GktykayZr2gq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDDY2ohOLwPRsH4%2FjdSrcAypV584IDbVthOTnj%2Bmnso2x%2BrfQWYBWO4MjOlixW4Yy7IaTTYpBnH5EvD3Lzxph3RCsNCmk8UiE9g3XtCs0fOnEkLpj%2FSNHt6MFvNLcJnuJOXBDwv5uydeATGJ9HHbRf8nfSfvnIhLnAypCpCT32LZuQbfQk9Xk6aKL7dXgI1uT8H6mOAoYWrxudJmMWaueQCPq60fHaI2xyvECysS8oAAXxoZ8Wj58ulWi%2BFmiegGmtLF%2FcoGH3LzTNNVFUjAg5lyWWloe99BHhBgANdlXPbYFWCvB1mD63QN3uTB31fIuY9UEcX8mbmyA3TC8Op%2FxMuUGBt750cdklwmiCV9WZ7%2FLWN0DMXUcLR12XXDJ3V1poXroH7fcdMR2CbtYVvCv%2B2RFwffFD8OEhzMe5l%2F66msXbcG%2B7rrPikUg%2FmWM6zBZIcMqtPumXBjgoO8o20xsxf5zeU%2BM8m3zNQTRY1E%2B8C%2Bcvy9Dtd11k3b2LKmTvc9pryc0AI4eR0pWbnvIqbC9MZD4jz%2BQJhw4CzyxYd5zF7TXKL%2FSbOWGJqQgvKrxf0o6jssavgTEriCfASBSJ2AqzOdLMpVDiGZzm%2BVHIHRmcbX%2FK%2BQD3%2B4Gi%2FBMZTQteVRJ7KdfJtA%2B%2F29ml2gyMOn%2Fp9MGOqUBTacRMMqO10pHWenVQw8bMGyPKuKnXlyxV27S4qdaoARIl3jzEH4IuCbu0axsihMyh22dWRG4nJ336v%2BhtNrAQwpOOFS28ng5gdEpWPqy3TENC4DR68yVzLb7oKDjKcH0J%2Bp%2B1y4wtcHMV3vm2RFmCRlY7IwC%2BM3okp6pt3Zdml5%2F7SgLY5sdmJbqagIUCfl8MnEmn5pjwrIoMgWoscA4qEFlHUNP&X-Amz-Signature=f2d2a143ff8846f04196b70b66b28ef66a4dc6266dc2c58e73bc3af815e70c94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TCJRLHU%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T134143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHA9fkYU7HtWcgLBOv0Y2jQvlnhW8t%2FScwqybW2TxN9IAiEAzdIMowv7lwtAoLqPgwL0VOCrqChc9Az0GktykayZr2gq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDDY2ohOLwPRsH4%2FjdSrcAypV584IDbVthOTnj%2Bmnso2x%2BrfQWYBWO4MjOlixW4Yy7IaTTYpBnH5EvD3Lzxph3RCsNCmk8UiE9g3XtCs0fOnEkLpj%2FSNHt6MFvNLcJnuJOXBDwv5uydeATGJ9HHbRf8nfSfvnIhLnAypCpCT32LZuQbfQk9Xk6aKL7dXgI1uT8H6mOAoYWrxudJmMWaueQCPq60fHaI2xyvECysS8oAAXxoZ8Wj58ulWi%2BFmiegGmtLF%2FcoGH3LzTNNVFUjAg5lyWWloe99BHhBgANdlXPbYFWCvB1mD63QN3uTB31fIuY9UEcX8mbmyA3TC8Op%2FxMuUGBt750cdklwmiCV9WZ7%2FLWN0DMXUcLR12XXDJ3V1poXroH7fcdMR2CbtYVvCv%2B2RFwffFD8OEhzMe5l%2F66msXbcG%2B7rrPikUg%2FmWM6zBZIcMqtPumXBjgoO8o20xsxf5zeU%2BM8m3zNQTRY1E%2B8C%2Bcvy9Dtd11k3b2LKmTvc9pryc0AI4eR0pWbnvIqbC9MZD4jz%2BQJhw4CzyxYd5zF7TXKL%2FSbOWGJqQgvKrxf0o6jssavgTEriCfASBSJ2AqzOdLMpVDiGZzm%2BVHIHRmcbX%2FK%2BQD3%2B4Gi%2FBMZTQteVRJ7KdfJtA%2B%2F29ml2gyMOn%2Fp9MGOqUBTacRMMqO10pHWenVQw8bMGyPKuKnXlyxV27S4qdaoARIl3jzEH4IuCbu0axsihMyh22dWRG4nJ336v%2BhtNrAQwpOOFS28ng5gdEpWPqy3TENC4DR68yVzLb7oKDjKcH0J%2Bp%2B1y4wtcHMV3vm2RFmCRlY7IwC%2BM3okp6pt3Zdml5%2F7SgLY5sdmJbqagIUCfl8MnEmn5pjwrIoMgWoscA4qEFlHUNP&X-Amz-Signature=c70332e38c2114f80f1d51d91f238b7ef91b8d9be866dec48ca391cd1b208a1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
