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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZW4IGN5%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T014535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPjb4y1t9QzG6O06FCg5sWXW5JumQyvhK6XivOyot%2BpAiEA7pjY5zA91AeiE6FGAWgQpN2mcFhMbgtSVIMu2Ugl01Mq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDHrkdVz7gJOZMZuBICrcA5v455bbFP6W3WXnJuapytmaJ6jOKGjKwhsLMs3sgkL6M4500y%2FBl9sGOg%2FdmIs6VvmiTd2Ai97HR15UKda505qv4CktuUpEuxKnQYXUU%2FjGCpSI8IfkRzQnjLx%2BOJmsCLhftWjaXKhA6nKKU10iGuJ4kmX%2BcYrOXdrQPUgpAQh17x%2FERHbT54aR8f9A0XtosVdd4XudG1ZntgxFSwAlOMetocJ1bHh4TIli61%2Ft5UOV4jlfROIBTX953f45Xn0jQ%2B5bqSjX8Fc7FNwdA%2F4rzzC7ID5%2BUkIZ11MZ5MtFR4wSUr9wqDGTZJfYAMNdQ1gyGf%2FfNrhWY7G3JZmjFp9XYzJSW1TXXsQZSf%2B13sEXkwKri9w32vFvDLLpmmvUlx%2FJhBwzitiCqCTI7I99NpjR2ocI%2BlXia1x1EPavOe4r7BC1C%2B5XnSYD2cIs2QmAjquXt3XDzvIAuq8EamLlKX6Obrx91hkzIBxr3nYs92at1%2B1ECzVF%2F1ndb5AyUL70kJyEVksbH20K2V6cvBI51VTfnOLqx%2B35Vsd%2B6apGAI5KmAZV7TTyjC5w%2FR26qNrtD1wfV1MUgHtVORTk5jpQQ1CWIHeUnvdWWuJD9FuaI3Xwhv2hpCtTyZW%2FyCnBIefdMIGo%2FdQGOqUBbduoieAMCOL6WBc111%2BTROaOWAdtdhcqdxLlhli%2BaeChTvAzuhYwEcKC%2BB7vzrA%2FQtVTqPNWiTYoDuCP73q9FT8Zpnk31uj1%2FEA5CeSPsvd%2Fb8uGd%2Bt0ovVU7lQFT6hM5U22oJTMvpMR0O3SDzorEcJuKxqThqmjrsEwWSsldqJB0DQ5qtcW5Bx8lEVsmay93Fy4ht1od6QAhZ2gq4PMMpeIi%2FBA&X-Amz-Signature=8caa64c4bfae7511a840ca7ffadf9cb70627b800a0ec43782f6d6d1f39960990&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZW4IGN5%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T014535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPjb4y1t9QzG6O06FCg5sWXW5JumQyvhK6XivOyot%2BpAiEA7pjY5zA91AeiE6FGAWgQpN2mcFhMbgtSVIMu2Ugl01Mq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDHrkdVz7gJOZMZuBICrcA5v455bbFP6W3WXnJuapytmaJ6jOKGjKwhsLMs3sgkL6M4500y%2FBl9sGOg%2FdmIs6VvmiTd2Ai97HR15UKda505qv4CktuUpEuxKnQYXUU%2FjGCpSI8IfkRzQnjLx%2BOJmsCLhftWjaXKhA6nKKU10iGuJ4kmX%2BcYrOXdrQPUgpAQh17x%2FERHbT54aR8f9A0XtosVdd4XudG1ZntgxFSwAlOMetocJ1bHh4TIli61%2Ft5UOV4jlfROIBTX953f45Xn0jQ%2B5bqSjX8Fc7FNwdA%2F4rzzC7ID5%2BUkIZ11MZ5MtFR4wSUr9wqDGTZJfYAMNdQ1gyGf%2FfNrhWY7G3JZmjFp9XYzJSW1TXXsQZSf%2B13sEXkwKri9w32vFvDLLpmmvUlx%2FJhBwzitiCqCTI7I99NpjR2ocI%2BlXia1x1EPavOe4r7BC1C%2B5XnSYD2cIs2QmAjquXt3XDzvIAuq8EamLlKX6Obrx91hkzIBxr3nYs92at1%2B1ECzVF%2F1ndb5AyUL70kJyEVksbH20K2V6cvBI51VTfnOLqx%2B35Vsd%2B6apGAI5KmAZV7TTyjC5w%2FR26qNrtD1wfV1MUgHtVORTk5jpQQ1CWIHeUnvdWWuJD9FuaI3Xwhv2hpCtTyZW%2FyCnBIefdMIGo%2FdQGOqUBbduoieAMCOL6WBc111%2BTROaOWAdtdhcqdxLlhli%2BaeChTvAzuhYwEcKC%2BB7vzrA%2FQtVTqPNWiTYoDuCP73q9FT8Zpnk31uj1%2FEA5CeSPsvd%2Fb8uGd%2Bt0ovVU7lQFT6hM5U22oJTMvpMR0O3SDzorEcJuKxqThqmjrsEwWSsldqJB0DQ5qtcW5Bx8lEVsmay93Fy4ht1od6QAhZ2gq4PMMpeIi%2FBA&X-Amz-Signature=8073cd36ecf78e88986866922b0176304c2e2a3c36c90c96813dfee2200e6f89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
