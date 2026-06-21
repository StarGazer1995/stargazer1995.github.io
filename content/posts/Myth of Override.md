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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPLD6X5I%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T154504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIBgFOuT9a0D6g1giEsx5xYJqIosF4Rzv6%2BIvqAJLeIDwAiEApxiTgM2SuiHRcExXjcXoPPhLehrbaD1p4QWkykYHEd8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNErHsHl%2B%2B3fSng9qyrcA%2FYECyL2P%2Bb2bv6%2B10WQgHRqmRNQANPfzkTgVn0gLGswE1E4N2W2Az6j74%2F7iRwPi1s8SZkXtcw3YA9bS%2F%2B3PaHvP0MKzrHzaTYxzgZIGjlVCrHWp7xrPSsii7ac7XuETuEbDLDMDYUiwaVJswGpeE5upmEmViVIAKhhTWNruA8hJi5lqTkvKKBRehW0g%2BbXP%2FhPfR7cZdVXh5ZUgMsTiPJFf%2F%2Fh0EsuLxG8Z9UhOGzO%2BSHP9oPfn4WHXdrWFOO%2F65e93wh1gp28G8ysnRhoaZCuPstROpemlBnMrSqDpFQ4NR3q41hWCGPRhMJarDc0K5x6%2Bwiu%2BfEdTdRf%2FhDL6O1OwD8rXgZGPz%2BGsji7XhKd2%2BQ8brh%2FobSqS%2B8cXe5gGQxyNQvskIJzilFyRp5doLIsFIiEfkANRSYLE%2BFMEeE3BTYpFvRkuvwR%2B0wkwYMSj31ChbixJMQayoH8cm27gWyEjjV2QUNtSpEX1ac%2Flw%2BUKl0n%2BaZgT0Q2%2Bunkjgk2DcNfVwpm26yerKni1S9JW98ficjupjWMByKLIh2pqH2RuIgqEZW5XWkT5CHLUH3Veh%2FxcGzi%2B%2BxJHqx7XlMTdvppmP2Gxl4NmGidGyWChiuCfEcORMMni27QtAkSMPue39EGOqUB%2FOs1tZsc9SxLmr58R4zp5jJh2BSMBtcKE0wxNN9MuxG0FLXkF5cDGSTTFQbRS79LJf7YygNj2P6Fv4Z%2BV02LGe6VXvQ9D0XBwgZ5Ge0T6lj3HSVL7Li4hhGZIPsdoQqZEZJnsFkEwIR%2Br0ll06IaL7m0J8dkHB2qsIN7QGdfd6q%2FE82OyOnLkUVyFualwbMG%2F1C7daRieu9LQMFVKVFwkMu6qFQZ&X-Amz-Signature=d4d9495963d5d7b7e1ab3772fdf6d69b9e85226a13b81c52f6178f28088742d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPLD6X5I%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T154504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIBgFOuT9a0D6g1giEsx5xYJqIosF4Rzv6%2BIvqAJLeIDwAiEApxiTgM2SuiHRcExXjcXoPPhLehrbaD1p4QWkykYHEd8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNErHsHl%2B%2B3fSng9qyrcA%2FYECyL2P%2Bb2bv6%2B10WQgHRqmRNQANPfzkTgVn0gLGswE1E4N2W2Az6j74%2F7iRwPi1s8SZkXtcw3YA9bS%2F%2B3PaHvP0MKzrHzaTYxzgZIGjlVCrHWp7xrPSsii7ac7XuETuEbDLDMDYUiwaVJswGpeE5upmEmViVIAKhhTWNruA8hJi5lqTkvKKBRehW0g%2BbXP%2FhPfR7cZdVXh5ZUgMsTiPJFf%2F%2Fh0EsuLxG8Z9UhOGzO%2BSHP9oPfn4WHXdrWFOO%2F65e93wh1gp28G8ysnRhoaZCuPstROpemlBnMrSqDpFQ4NR3q41hWCGPRhMJarDc0K5x6%2Bwiu%2BfEdTdRf%2FhDL6O1OwD8rXgZGPz%2BGsji7XhKd2%2BQ8brh%2FobSqS%2B8cXe5gGQxyNQvskIJzilFyRp5doLIsFIiEfkANRSYLE%2BFMEeE3BTYpFvRkuvwR%2B0wkwYMSj31ChbixJMQayoH8cm27gWyEjjV2QUNtSpEX1ac%2Flw%2BUKl0n%2BaZgT0Q2%2Bunkjgk2DcNfVwpm26yerKni1S9JW98ficjupjWMByKLIh2pqH2RuIgqEZW5XWkT5CHLUH3Veh%2FxcGzi%2B%2BxJHqx7XlMTdvppmP2Gxl4NmGidGyWChiuCfEcORMMni27QtAkSMPue39EGOqUB%2FOs1tZsc9SxLmr58R4zp5jJh2BSMBtcKE0wxNN9MuxG0FLXkF5cDGSTTFQbRS79LJf7YygNj2P6Fv4Z%2BV02LGe6VXvQ9D0XBwgZ5Ge0T6lj3HSVL7Li4hhGZIPsdoQqZEZJnsFkEwIR%2Br0ll06IaL7m0J8dkHB2qsIN7QGdfd6q%2FE82OyOnLkUVyFualwbMG%2F1C7daRieu9LQMFVKVFwkMu6qFQZ&X-Amz-Signature=b5712ff4871041ec08f31e59fef09ceba66d2bda84daac06d5691046483a14c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
