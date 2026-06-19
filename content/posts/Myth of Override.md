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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TVJOL72%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T192350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9MlIcfTRTHa4mPMytuEBANYxKS6QlO6%2FqyZT0t2AmEQIgUoaYDU2%2B5FyBCFp%2FSYYGh4k5GeiBh%2B4Zj%2B6oW5cz3WAqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLYtu8%2B0neLZiikLsSrcA0oTScDvm%2BdHwYeKX1ratxxR3Gzf8SabEFHSopBeiC8cRHhjX7zc3wPnDvO64Nry%2B3wc5DShNdgKQmKMcFpX7LmL1gD7Hgv%2BgKaH1of4O3EK56Ga7wgP2OGwQUOc0jjjsj8kMmdk6Ba%2FMO35wAxi3RKaPpDEVvfCPy0U%2Flz%2F%2FoZp%2BbuuTtUue6xN6xV5Y7VWEDGBukqhWxRX%2BJR98nT0bFJqxH0FHCIQo3ntzV9Dc8ojYtipPML9hTtPTKlCOFSJWaYY3viTUHuVuPOxgrNrO8FwQ%2F9OVRopyVMxcDoR1Uja%2BQj2vvAZFHlSzWKZW2tWJ3%2Bj2BGFqtIPM7NFFNM9lUUFSisy8Vl5CXago%2FwA%2FLCZVJKQYiUWazDiCR9IW3I3axmGkfPQI1WbDQxUl0E8hULdCybgD%2FCnmnLGtjRNLMoXYre5wjwgnUJ74AHRIPTi%2FouB3yIhgJs5ah6bqTeqfn%2FUpGU6lnMcZzQrK%2FbEDDnkDks1C9vDj9wU3zFNbljYYmlfgndqETE0qTVZ5Bcu1X7%2BbCw2CheLZNNOaxbhM1jefCFSt395qBb4P8z36rh%2BCZKLNjXMwGPD1ZJKNbWs5b%2BFLtsSYvIDXGIhq%2Fjmfk0uWdb3CwyCxQiciWnmMISi1tEGOqUB4Tmu%2F2Ccmw%2B2xWXqiMnHHh%2B%2BGUFiooA3lpPWRd7oYytdbuv%2BQrBQB0TRMJtaUR1I9KMkvDeMG4VaX0gme%2B10s1u3SBCKikK9QMNpoAHc2QV%2FF0zyQGKSo9RRL%2F8BLzvcJogEPYxosvR73VIOA53bsEMO1IImynzLB8lNk23j%2F8x4xf6idZBhqmz1ndToxTkyfOYfmuYdcx%2BfBrwqvvkrnwIkyA6c&X-Amz-Signature=37c3d564a66c4c0e0564364b0e8c452c4de39a872a5c7e99a3f3677dfaa8d75e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TVJOL72%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T192350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9MlIcfTRTHa4mPMytuEBANYxKS6QlO6%2FqyZT0t2AmEQIgUoaYDU2%2B5FyBCFp%2FSYYGh4k5GeiBh%2B4Zj%2B6oW5cz3WAqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLYtu8%2B0neLZiikLsSrcA0oTScDvm%2BdHwYeKX1ratxxR3Gzf8SabEFHSopBeiC8cRHhjX7zc3wPnDvO64Nry%2B3wc5DShNdgKQmKMcFpX7LmL1gD7Hgv%2BgKaH1of4O3EK56Ga7wgP2OGwQUOc0jjjsj8kMmdk6Ba%2FMO35wAxi3RKaPpDEVvfCPy0U%2Flz%2F%2FoZp%2BbuuTtUue6xN6xV5Y7VWEDGBukqhWxRX%2BJR98nT0bFJqxH0FHCIQo3ntzV9Dc8ojYtipPML9hTtPTKlCOFSJWaYY3viTUHuVuPOxgrNrO8FwQ%2F9OVRopyVMxcDoR1Uja%2BQj2vvAZFHlSzWKZW2tWJ3%2Bj2BGFqtIPM7NFFNM9lUUFSisy8Vl5CXago%2FwA%2FLCZVJKQYiUWazDiCR9IW3I3axmGkfPQI1WbDQxUl0E8hULdCybgD%2FCnmnLGtjRNLMoXYre5wjwgnUJ74AHRIPTi%2FouB3yIhgJs5ah6bqTeqfn%2FUpGU6lnMcZzQrK%2FbEDDnkDks1C9vDj9wU3zFNbljYYmlfgndqETE0qTVZ5Bcu1X7%2BbCw2CheLZNNOaxbhM1jefCFSt395qBb4P8z36rh%2BCZKLNjXMwGPD1ZJKNbWs5b%2BFLtsSYvIDXGIhq%2Fjmfk0uWdb3CwyCxQiciWnmMISi1tEGOqUB4Tmu%2F2Ccmw%2B2xWXqiMnHHh%2B%2BGUFiooA3lpPWRd7oYytdbuv%2BQrBQB0TRMJtaUR1I9KMkvDeMG4VaX0gme%2B10s1u3SBCKikK9QMNpoAHc2QV%2FF0zyQGKSo9RRL%2F8BLzvcJogEPYxosvR73VIOA53bsEMO1IImynzLB8lNk23j%2F8x4xf6idZBhqmz1ndToxTkyfOYfmuYdcx%2BfBrwqvvkrnwIkyA6c&X-Amz-Signature=7e553457985d5e632d21108db61283dfb42dcd86fdb485a0a274cd187f439ea3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
