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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCN6TUKJ%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T185447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3dKQocac%2BEr527iXsZ6Z02HfzYb90HMaUuTWovMGv8wIhAOKNz4BKOWwAFnWfGFvDDFai%2FYTD48MHpi%2BOYRY2ddePKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkJpPTOq%2FN93nLJ9Uq3AMH3YTxL8BgckMB2HKGI9jgFNq6uFmMnsP8dEivd0YaLpEDJ%2BiSTrfzRazQGfuXWxnD9%2BFO9GQl1pfqZo8xoy%2Fb3pcluLhEIl94ytTHSmoj%2BvN4SLkvut529lQJhGYY2GrjL6QngrqW0H1OmsbOnEKAuOwsP0z14JA9bkSqfM3qhFOyZ%2BmPNQkKQ8%2FbKnvUbr%2B0LUK9URiCCYeXMnt%2F%2Bk0MyQY%2FKaSmLMqR7S%2BBR%2FIVloj4%2BY2d3zABIE4Aw5TVAITxG1ul8TtEldeOvwkWF0CP78nZoSnOPMSltdQDvUsn1AZ9Fif1sDeqp59YcAYFn6lAtDizSb5brW3uQIv0dcVFcPC9V2VL3S0xrZs8EhVKTQjRa5sm2PaEcl0yt%2BG65HhIcK5CmWfz2c0SEa6yMtoweBH4w4PJn5ikbEBU06OCBX1rU%2BzHsjAqlHV87FfkYXeC6abEGukpGOC%2F5UfdTWqOGZxxVct9yQhJhDfV5VAez6avW7lFaycy4RXopEK1%2Bn3CffMFCx50vJkA7JsSOfKJE8LXIiQzKKg6j3sROLv4GJ6DZP7AUILuV6LMtjMO8b4TQIRTIivuD0TR5NzsxTZWwItt01aR%2B41wJrnQVi7mq9xe5Sl5xsQdPlEJmzC83tHUBjqkAbJDZtDRloT1fZypqTsyKNNfI8y%2BZjYEhfoGiWEROg2Ul76IK3W46cleCp7HiJEvNVmAPtGTztwbVCbb6a4BKA8D%2Fc6tv%2FNl1JFu3olJdgnRtzMq%2BEeU44yhfkwQHjBfU%2FCSrbQW007BEIV11izqoQ%2FJrXHb1MStHpbtXPHsqQFMf5sqCQEW7AwlCzT%2B40ffmGF9ZkA%2FI5nDkj%2B6S%2BEgGF0ZRTlk&X-Amz-Signature=04044cd04e4e7f59bdb72f0153be5b5a559c4811bcf6d5150e360ad9f6753f64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCN6TUKJ%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T185447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3dKQocac%2BEr527iXsZ6Z02HfzYb90HMaUuTWovMGv8wIhAOKNz4BKOWwAFnWfGFvDDFai%2FYTD48MHpi%2BOYRY2ddePKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkJpPTOq%2FN93nLJ9Uq3AMH3YTxL8BgckMB2HKGI9jgFNq6uFmMnsP8dEivd0YaLpEDJ%2BiSTrfzRazQGfuXWxnD9%2BFO9GQl1pfqZo8xoy%2Fb3pcluLhEIl94ytTHSmoj%2BvN4SLkvut529lQJhGYY2GrjL6QngrqW0H1OmsbOnEKAuOwsP0z14JA9bkSqfM3qhFOyZ%2BmPNQkKQ8%2FbKnvUbr%2B0LUK9URiCCYeXMnt%2F%2Bk0MyQY%2FKaSmLMqR7S%2BBR%2FIVloj4%2BY2d3zABIE4Aw5TVAITxG1ul8TtEldeOvwkWF0CP78nZoSnOPMSltdQDvUsn1AZ9Fif1sDeqp59YcAYFn6lAtDizSb5brW3uQIv0dcVFcPC9V2VL3S0xrZs8EhVKTQjRa5sm2PaEcl0yt%2BG65HhIcK5CmWfz2c0SEa6yMtoweBH4w4PJn5ikbEBU06OCBX1rU%2BzHsjAqlHV87FfkYXeC6abEGukpGOC%2F5UfdTWqOGZxxVct9yQhJhDfV5VAez6avW7lFaycy4RXopEK1%2Bn3CffMFCx50vJkA7JsSOfKJE8LXIiQzKKg6j3sROLv4GJ6DZP7AUILuV6LMtjMO8b4TQIRTIivuD0TR5NzsxTZWwItt01aR%2B41wJrnQVi7mq9xe5Sl5xsQdPlEJmzC83tHUBjqkAbJDZtDRloT1fZypqTsyKNNfI8y%2BZjYEhfoGiWEROg2Ul76IK3W46cleCp7HiJEvNVmAPtGTztwbVCbb6a4BKA8D%2Fc6tv%2FNl1JFu3olJdgnRtzMq%2BEeU44yhfkwQHjBfU%2FCSrbQW007BEIV11izqoQ%2FJrXHb1MStHpbtXPHsqQFMf5sqCQEW7AwlCzT%2B40ffmGF9ZkA%2FI5nDkj%2B6S%2BEgGF0ZRTlk&X-Amz-Signature=02f2b4785dd023ed691a12b7608800b92398de9d3e197dfe02a077fffdad1c19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
