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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2FD2QS3%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T054040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEgFWV2vlp%2Bh4die%2BLqNcbIty8kzwDmg4%2F0YGIJJ8MUgIgJJ1uVUjQnETvOLN7SnNziJMDWB%2BdJJwpmeVxQgYkEGAqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLcA5RnFhRz2hsQ3WircAw6GjMbm4T5Sj1bC%2BwDu8rkJtgE3O4kk4UZ1Z77MNOZLDCZA%2FGE6FvUka88wsh1k8nOCDHetV1bHTUzDkTNK7c5cccvH0kqohCT5GhdLnaf%2BhZnYaWoV%2FoWHCej%2Fcjl8VBxKhG6aqivdmYoEbKNezPnXmmNMU2f01ddjAJBWiLu09HtHGIHlds10b%2BExLNrjFXaJrs7Xy5vj87QP39CZfOtPmwhIXJX4pDmyZHugkeT6V7PzvrnkO%2FzS6osehZilhSVVHML0mJa%2FhbtUnUsaoPv2VKqieMSIwXF64J5Zf8Rlb06EMca5QvIrf4Aqfb5aBMT6Vj0AbFOJdIuQAjIllcgpY337OFZOwD7AGkdZVli%2BJwC0utZbi8HUm2%2BCpcvZJaqijuu6iUykR5M4cD5LXTJaE4%2BoE%2FTZgOLflVZedG9ye4lmTVuzgP0SXyUB3N3PksSxju9NKr5pS%2BdKK0ANYqTf07rXKnHlPUEkJz1fdzT%2F4gvrVgIEooVQRQjnNxhO0Lienr67YTNLwC%2BNt19d%2FEZKF92YWBRjpI2koLeYShEEwbIrD2shHVCSmSsr2IVxT2nsuY5eIbOWurW087IGSfy4aX5c2Jgun5R8Rpq8hhmFMhl%2FY9AAC8dgjfn%2BMJzupNAGOqUBQf2CfWfhZMlra9UM0656Fug%2F7EujLv5zhz9lNvrZmwNxv3m2Uu6NG9cyG5HRFaa8lAaR1Wov0%2Fnh2OLNryxwRmK2e8ADPFY4Q37QpJnR09uL3CKYobC0dWMLuIIQ%2B5BpQxLnqK0MYW1M0TIiNmXmKDjU83mysr%2F9cSYdrLYWafq37xlGGNYI2QSpiBjHDSgyoFpMufnVZ4p%2FAdgXIwptSlOl0EHb&X-Amz-Signature=3bf2ca0b0fb480a6c9b40a9d8befcc63e67622d51b2f77dab7c49abea8495978&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2FD2QS3%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T054040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEgFWV2vlp%2Bh4die%2BLqNcbIty8kzwDmg4%2F0YGIJJ8MUgIgJJ1uVUjQnETvOLN7SnNziJMDWB%2BdJJwpmeVxQgYkEGAqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLcA5RnFhRz2hsQ3WircAw6GjMbm4T5Sj1bC%2BwDu8rkJtgE3O4kk4UZ1Z77MNOZLDCZA%2FGE6FvUka88wsh1k8nOCDHetV1bHTUzDkTNK7c5cccvH0kqohCT5GhdLnaf%2BhZnYaWoV%2FoWHCej%2Fcjl8VBxKhG6aqivdmYoEbKNezPnXmmNMU2f01ddjAJBWiLu09HtHGIHlds10b%2BExLNrjFXaJrs7Xy5vj87QP39CZfOtPmwhIXJX4pDmyZHugkeT6V7PzvrnkO%2FzS6osehZilhSVVHML0mJa%2FhbtUnUsaoPv2VKqieMSIwXF64J5Zf8Rlb06EMca5QvIrf4Aqfb5aBMT6Vj0AbFOJdIuQAjIllcgpY337OFZOwD7AGkdZVli%2BJwC0utZbi8HUm2%2BCpcvZJaqijuu6iUykR5M4cD5LXTJaE4%2BoE%2FTZgOLflVZedG9ye4lmTVuzgP0SXyUB3N3PksSxju9NKr5pS%2BdKK0ANYqTf07rXKnHlPUEkJz1fdzT%2F4gvrVgIEooVQRQjnNxhO0Lienr67YTNLwC%2BNt19d%2FEZKF92YWBRjpI2koLeYShEEwbIrD2shHVCSmSsr2IVxT2nsuY5eIbOWurW087IGSfy4aX5c2Jgun5R8Rpq8hhmFMhl%2FY9AAC8dgjfn%2BMJzupNAGOqUBQf2CfWfhZMlra9UM0656Fug%2F7EujLv5zhz9lNvrZmwNxv3m2Uu6NG9cyG5HRFaa8lAaR1Wov0%2Fnh2OLNryxwRmK2e8ADPFY4Q37QpJnR09uL3CKYobC0dWMLuIIQ%2B5BpQxLnqK0MYW1M0TIiNmXmKDjU83mysr%2F9cSYdrLYWafq37xlGGNYI2QSpiBjHDSgyoFpMufnVZ4p%2FAdgXIwptSlOl0EHb&X-Amz-Signature=3bdc2ce259c99a10a351860e47b717ce8e97814bb3711e27283fa16bb489f062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
