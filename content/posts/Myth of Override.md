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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCWMUNMJ%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T060014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFXuRKgJAdnKYfX%2FoQO81zwb3TB2Pcr0N9D9E2Az21bAiEAhZ4XX4PXScqn7xR7iEU%2Bgr7xx8L%2FtV1%2BmVQ1vGlZHv4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoOMHWOpzu0GZjFICrcA5MtN5QPDYgv7azvCox4AnLiNh30yaLLDKXLcAdBShXHPT18uWc0lSVjk2z5PoPCtGIqfbmVdN6gVrSJ7640g7gEbIGJP1Kz8nSj4SFwVnvw7rQz2dwmq5%2BoHzx3WmOjt%2Flq49Ti8BcTtizuXNmNb8mm3AVPL5ZIikeH1XJ0vinV8V02xv15P3YlyOC2bLXsebu2Vlprimdw0q4h6yP1MGrVgljED95Et%2FhXFqqjf4ExezA7BDj6Rymn%2F%2FfdVwOyxSjLw6XlsT5y1y%2BXi6wOAVuMd2Y6iwkYhE6A%2FtY9iVDUn9%2BRZWj%2FEGpXhGDyL9s2HspkFi91zPJBh4Hcj2GiWtKmcMtTG07AuC6QcP9mZI3ukAbO4Y5KxdpX2ib7I5Ek0y82ferG2HoDGbsnzbvDjda%2BTIIUrcL2%2Bs85oaYmUS5jqq6qnGukN%2Fl7%2Fft%2BsKNlsFWpsYRwnsx1UFZ71o%2FwyGeCHLNVJwrazPLKI8J5hmfILpqunmU5tDQvQaMgUVbzlfzULBjj1HNMcoq3fTCftG3tVcRBUH2UeR9ehc2jmaN2K5fTS%2Bgy0JTA4NElfQXyQBLh7%2BIzCrrDgYbFOpXt%2BAhDGC3EZWS877pi%2Bp1vW%2BBXOmEMC4XCQXjKWRZqMJK1ntEGOqUBIIML4ImG181KXUmp0t1%2FDn02%2B4le44e5dAbK9wAJWcQ9ZVf0oqxP7NDH9sJdF9iL7Q5VM00OlKK5CxYh1wOmyotRn6%2F52XX9hXM%2F373Fs7XFm8qgi23sMLbCBwWFYcsIeCdD4Y8fJBRllEgG3GP0WfhKWJE8%2B1lnQBVPYwvyJTW%2FfG3ygitslDFgyY7eRptCxltByLAk73%2FTheslhOk0E6CZgsMn&X-Amz-Signature=72b1d5e17d38c2daeaa635e24e7fed6fb1d68ff7f0aff1dad21c70448d602a00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCWMUNMJ%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T060014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFXuRKgJAdnKYfX%2FoQO81zwb3TB2Pcr0N9D9E2Az21bAiEAhZ4XX4PXScqn7xR7iEU%2Bgr7xx8L%2FtV1%2BmVQ1vGlZHv4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoOMHWOpzu0GZjFICrcA5MtN5QPDYgv7azvCox4AnLiNh30yaLLDKXLcAdBShXHPT18uWc0lSVjk2z5PoPCtGIqfbmVdN6gVrSJ7640g7gEbIGJP1Kz8nSj4SFwVnvw7rQz2dwmq5%2BoHzx3WmOjt%2Flq49Ti8BcTtizuXNmNb8mm3AVPL5ZIikeH1XJ0vinV8V02xv15P3YlyOC2bLXsebu2Vlprimdw0q4h6yP1MGrVgljED95Et%2FhXFqqjf4ExezA7BDj6Rymn%2F%2FfdVwOyxSjLw6XlsT5y1y%2BXi6wOAVuMd2Y6iwkYhE6A%2FtY9iVDUn9%2BRZWj%2FEGpXhGDyL9s2HspkFi91zPJBh4Hcj2GiWtKmcMtTG07AuC6QcP9mZI3ukAbO4Y5KxdpX2ib7I5Ek0y82ferG2HoDGbsnzbvDjda%2BTIIUrcL2%2Bs85oaYmUS5jqq6qnGukN%2Fl7%2Fft%2BsKNlsFWpsYRwnsx1UFZ71o%2FwyGeCHLNVJwrazPLKI8J5hmfILpqunmU5tDQvQaMgUVbzlfzULBjj1HNMcoq3fTCftG3tVcRBUH2UeR9ehc2jmaN2K5fTS%2Bgy0JTA4NElfQXyQBLh7%2BIzCrrDgYbFOpXt%2BAhDGC3EZWS877pi%2Bp1vW%2BBXOmEMC4XCQXjKWRZqMJK1ntEGOqUBIIML4ImG181KXUmp0t1%2FDn02%2B4le44e5dAbK9wAJWcQ9ZVf0oqxP7NDH9sJdF9iL7Q5VM00OlKK5CxYh1wOmyotRn6%2F52XX9hXM%2F373Fs7XFm8qgi23sMLbCBwWFYcsIeCdD4Y8fJBRllEgG3GP0WfhKWJE8%2B1lnQBVPYwvyJTW%2FfG3ygitslDFgyY7eRptCxltByLAk73%2FTheslhOk0E6CZgsMn&X-Amz-Signature=80dda4244e71c6ac3f93e0e35f6ad7e1ad08a75ff0662d997d7286af95560366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
