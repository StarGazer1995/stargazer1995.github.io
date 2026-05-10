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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCKFMDG%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T105358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGTgDaW704XxaAx3e2LMsfBUmWjQino4ZQ6G8v2Y1TekAiEAo17Kwpa%2FCwol6jf0KHnhy1Fr0SdWWHQYzStMD3S02qYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCT67%2BCjkEDnpQND9CrcA3HI3SH2G9aeDRknBCAkykeqs9lZEYCBhpq81Lb0tt%2BmLrxI3JFDJjuSeA8FnQ8VP813iX%2Fw9gJ%2FX%2Bttw9cjin1UBugDXJCNqRfcsnPJrctngQ5zcmoiQXQV8WHYO8ZEuxI9oMZXbOcIMRHp8rTFqI%2BRn%2BstGjS5DsjhpvjxDYc2Q9TzJ8vdKrd0u9S9rI6w2Y7I6eGXBe9GKU48tf0Q54ZMEDH38j%2BQ9%2Fe87AjhMmxhe%2Fm%2BpdRABVRnRfSvfXEftWdqGbiSPXvPVstzDrkoSllplr2IceYgozuQiao8G58tB61Xr%2BYLKBELQFkZ%2BVm1938jBqOXCCPO4Rs1eXwkS7DgaYxGnKWKzFzOw8EZ4crZjab0YJiGbX3hM36W32SBBkG1PfhduSMT5aE%2B%2B5Ty3cIaOl62sOXlm1pRMcPZd5Pi5waaDOEl5A9B0cRbmFiY8cm%2BUjeLdhxdRwu%2BvSRvBEQDrcfotKrA3u7ML2UirYbBVHJQ7%2FyVQKzlGqsZmxfQB3LWz9zcPoZeFLafnJRLw1pQg%2Fwo3SboCwdJMP7P9SnwS3IZauBsbS9zw74gi4FvXzxZIrmi2riN%2BjLiX%2BhWseOq4hj6%2FK6Yu004cZSVRpK64bpMZmkoeUuGcwwoMJSxgdAGOqUBuZlXCLyDoz23BP9nxBT23Trc02H7fm5QLE8dVt7IvpoMLrduEa3Hb0AOtDu67LMHkBdwKia%2B0yB0gdIs%2FDp46jJZhRjUqAiVlRfw7had2nUMbOMZoj6MGpHXLktS1MKAuqBkWrgsj6DcUw4%2FTUzP9%2FK0Yrg5bGl2dvM4pi2KuClcPLt40017RKQn1n4szeaRxC8iBzbept9JGTKRkP31LO%2Fe82pj&X-Amz-Signature=037bc01e3321530689286114f7070b4ca93be4bb23b9b69701bf5e5e648c3625&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFCKFMDG%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T105358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIGTgDaW704XxaAx3e2LMsfBUmWjQino4ZQ6G8v2Y1TekAiEAo17Kwpa%2FCwol6jf0KHnhy1Fr0SdWWHQYzStMD3S02qYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCT67%2BCjkEDnpQND9CrcA3HI3SH2G9aeDRknBCAkykeqs9lZEYCBhpq81Lb0tt%2BmLrxI3JFDJjuSeA8FnQ8VP813iX%2Fw9gJ%2FX%2Bttw9cjin1UBugDXJCNqRfcsnPJrctngQ5zcmoiQXQV8WHYO8ZEuxI9oMZXbOcIMRHp8rTFqI%2BRn%2BstGjS5DsjhpvjxDYc2Q9TzJ8vdKrd0u9S9rI6w2Y7I6eGXBe9GKU48tf0Q54ZMEDH38j%2BQ9%2Fe87AjhMmxhe%2Fm%2BpdRABVRnRfSvfXEftWdqGbiSPXvPVstzDrkoSllplr2IceYgozuQiao8G58tB61Xr%2BYLKBELQFkZ%2BVm1938jBqOXCCPO4Rs1eXwkS7DgaYxGnKWKzFzOw8EZ4crZjab0YJiGbX3hM36W32SBBkG1PfhduSMT5aE%2B%2B5Ty3cIaOl62sOXlm1pRMcPZd5Pi5waaDOEl5A9B0cRbmFiY8cm%2BUjeLdhxdRwu%2BvSRvBEQDrcfotKrA3u7ML2UirYbBVHJQ7%2FyVQKzlGqsZmxfQB3LWz9zcPoZeFLafnJRLw1pQg%2Fwo3SboCwdJMP7P9SnwS3IZauBsbS9zw74gi4FvXzxZIrmi2riN%2BjLiX%2BhWseOq4hj6%2FK6Yu004cZSVRpK64bpMZmkoeUuGcwwoMJSxgdAGOqUBuZlXCLyDoz23BP9nxBT23Trc02H7fm5QLE8dVt7IvpoMLrduEa3Hb0AOtDu67LMHkBdwKia%2B0yB0gdIs%2FDp46jJZhRjUqAiVlRfw7had2nUMbOMZoj6MGpHXLktS1MKAuqBkWrgsj6DcUw4%2FTUzP9%2FK0Yrg5bGl2dvM4pi2KuClcPLt40017RKQn1n4szeaRxC8iBzbept9JGTKRkP31LO%2Fe82pj&X-Amz-Signature=7b9c90601dbdb92e851cdfd6bb6a14386149f4969b2b74b8943d7fc52bf232ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
