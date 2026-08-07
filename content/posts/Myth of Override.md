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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHOUSJRM%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T144451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX8EAfMS%2BxH%2BcJRi5nHWKBImWsvgJq%2F67acrDANwiIywIhAMwuDNQxRdM4mANOfvWRnhEUkO3gXJWO%2BrAtzsdDyjMYKv8DCFYQABoMNjM3NDIzMTgzODA1Igx58J%2FD1l%2ByZ6vKRsAq3AOg5A5aZWm64lqJU6kqZks3sLh7QCAcvvL0N%2FcAjyezuX68V5OCLh92cwcQr%2BWsJkQ0jQn7DEw%2BbvgdEDNG%2FyW6vPVnCPUI72c0YjF36lQ1sFjw9cZZb8lK7xhsuletkMqxR4kjSE3O1zhfYUnnxz1sLVV0e4HLOXJrelj%2FjezMfC8fuemTZ9emxnCPFTgmf3x2ar8Xz3Lizil80cbzLKf1qvctWydnS3xyShgUrzWYKnWBa6Z%2FqngywiFLR69s965GG74czwROhTcbv7%2F986c0laA9EZsASSCcUy2xVOhOas5SAU%2F%2BwJMumBeQIMh%2FCQNZRVKCMV7lv2Vw6CqiYJufPkbDVZgfjzvwQ8wIRQYW93HZMtTc2KVEosgW9ejWPabSxwtIiFM9ZvGVl2%2FlquCH%2Bwc7bsNtE%2BPvHzO7zUKI1VlSncwCzub0A6W4HcfYmOtPiWCemgsfIRGtV2TIJAgirActGccFMx4x%2F0yG4T8CjZhFmrWWiLE9hLrAx58nhBKCrnfznJ36aTi4WpE6BS%2BROE7TMG9uUV9vgTZ39NLztONcRq03%2BLBBXjwkhTW2FPet%2BMXl1L6vueC3YRPnFLp3WXCn9IS6vWyOWeGn5f%2FOuFubE1Tw%2BGasJuuHiDCNrtfTBjqkAVq%2Fpu%2B7ed6YaLC4jbvE2gLrbhnlg3eFmxCR0MvG4aHEhFqH9f2aAAVIGLVluTwsDQs5eQXVBN%2BYywlPo14q231HIbyBmEDDn5S6Zwlh3YjH%2FjXycHLa%2FRe5baTAv1lBujOlf96RmGlK3MgRlMmxvd8otgphLAX1XS2vMT9FBPFmEL8R0ckkP4vimPoOhb0UX9xknVOdDg5ySdD3%2F5Y0byd%2BwvAF&X-Amz-Signature=a9618d94731417ef2ef58e9dcc15f5e526bf6888b9222a43cab7baa68aab24ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHOUSJRM%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T144451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX8EAfMS%2BxH%2BcJRi5nHWKBImWsvgJq%2F67acrDANwiIywIhAMwuDNQxRdM4mANOfvWRnhEUkO3gXJWO%2BrAtzsdDyjMYKv8DCFYQABoMNjM3NDIzMTgzODA1Igx58J%2FD1l%2ByZ6vKRsAq3AOg5A5aZWm64lqJU6kqZks3sLh7QCAcvvL0N%2FcAjyezuX68V5OCLh92cwcQr%2BWsJkQ0jQn7DEw%2BbvgdEDNG%2FyW6vPVnCPUI72c0YjF36lQ1sFjw9cZZb8lK7xhsuletkMqxR4kjSE3O1zhfYUnnxz1sLVV0e4HLOXJrelj%2FjezMfC8fuemTZ9emxnCPFTgmf3x2ar8Xz3Lizil80cbzLKf1qvctWydnS3xyShgUrzWYKnWBa6Z%2FqngywiFLR69s965GG74czwROhTcbv7%2F986c0laA9EZsASSCcUy2xVOhOas5SAU%2F%2BwJMumBeQIMh%2FCQNZRVKCMV7lv2Vw6CqiYJufPkbDVZgfjzvwQ8wIRQYW93HZMtTc2KVEosgW9ejWPabSxwtIiFM9ZvGVl2%2FlquCH%2Bwc7bsNtE%2BPvHzO7zUKI1VlSncwCzub0A6W4HcfYmOtPiWCemgsfIRGtV2TIJAgirActGccFMx4x%2F0yG4T8CjZhFmrWWiLE9hLrAx58nhBKCrnfznJ36aTi4WpE6BS%2BROE7TMG9uUV9vgTZ39NLztONcRq03%2BLBBXjwkhTW2FPet%2BMXl1L6vueC3YRPnFLp3WXCn9IS6vWyOWeGn5f%2FOuFubE1Tw%2BGasJuuHiDCNrtfTBjqkAVq%2Fpu%2B7ed6YaLC4jbvE2gLrbhnlg3eFmxCR0MvG4aHEhFqH9f2aAAVIGLVluTwsDQs5eQXVBN%2BYywlPo14q231HIbyBmEDDn5S6Zwlh3YjH%2FjXycHLa%2FRe5baTAv1lBujOlf96RmGlK3MgRlMmxvd8otgphLAX1XS2vMT9FBPFmEL8R0ckkP4vimPoOhb0UX9xknVOdDg5ySdD3%2F5Y0byd%2BwvAF&X-Amz-Signature=6de58e57a17bb6ee6d062b48b481ce1115e41308ca88c9bbfe83478788184fbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
