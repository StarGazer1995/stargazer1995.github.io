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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662D3IKHL5%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T143136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIDNndHJXJI%2FjC%2FWtsqRkPB3q6%2Biuz%2FAG8NtZeJROo%2BkqAiEAr6KxwVlxPLF2yuyJgwcVhUql7T%2B5xWaarHt5CH7Mj%2FcqiAQI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAF7zK5b5tjRGmS2SrcA7bK1Uv6di0DXmnLYo7j0qgdkjX7Wg%2B3xSvE4zKPSQoKm24rT7o%2FF5c6CYqvpEssILWUgBNU8Pw7HvJB3pHBH6yVUO7uzzMU8Ey18mB1VjNZ5S5bQRao7nHdtfInbSQXPAEPuAFeQedpBgzxLN%2FxVr5HpufDhn1UGr7IQuLmt%2FUYSchwQA9QUyXLEAl55nnaZxTx1T5MBC29Ct8tysXkdBlC9uAHz9e7bcEiO1V%2FFyJUQWkp69MZKy%2Fb9V%2BUPRCyQjXrEfMP2I8rByCAiCyrK31MxpAAxJP5aRXPDhTzkjlIUMAos9SG2t4QUkiGRng0x9uRsT7OOGMRVKIR9yb%2BdmIruF3lL4Zyu3vse2a%2F2haK%2FVfgf5iCPxmNWpM6LfQiHHXAcbX%2F3ye%2Bwe5vOrJK6jpbXTMAa2zwlKHqxIPcIhOKHGUQeYvSDVF6lQTSmsRRJ4BKibm9pU81VlKbTGzWNZKNfzue1JjRhYbomvSR8xZJY9FHudIPXVmrlnlrKLykTV7c4h6LHymdY91iHZ%2BzNtrPEumuQPYKR%2FZgQUc4KjXDlu4bG4Ke1RNwQwZMRjMuSwyxF0bPaF%2FvmPAe6oQdcksvI1Mo0b4%2BXK6XSfr7nZc8iRLCvHvd%2B%2BpFkZrwMILpttAGOqUBS5DoMZBCOavN%2BXjz6RNOur6lZnvwjfaxQt9r%2Bv9w6AKgMbz44VQtxrhADGprqkGcDlkTk5MZgg6ZG%2BmADT2OMl709x79lImns6yaq8ZbqZ34ZvrXp7%2BWG1cn%2FmqqQxsOS%2BQNUwel67aPjy7EIk56bSADHIsKdvfxf4Z3bZXGyyYSILaYK9qnWtM%2FwNzCzjvbl6iuR5bywO1TgggQd0lrCb9cGado&X-Amz-Signature=8ad831a4d8e976d2909f3b9323f16c83a227cb7a91b6b0a8b95e7ea4ab836525&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662D3IKHL5%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T143136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIDNndHJXJI%2FjC%2FWtsqRkPB3q6%2Biuz%2FAG8NtZeJROo%2BkqAiEAr6KxwVlxPLF2yuyJgwcVhUql7T%2B5xWaarHt5CH7Mj%2FcqiAQI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAF7zK5b5tjRGmS2SrcA7bK1Uv6di0DXmnLYo7j0qgdkjX7Wg%2B3xSvE4zKPSQoKm24rT7o%2FF5c6CYqvpEssILWUgBNU8Pw7HvJB3pHBH6yVUO7uzzMU8Ey18mB1VjNZ5S5bQRao7nHdtfInbSQXPAEPuAFeQedpBgzxLN%2FxVr5HpufDhn1UGr7IQuLmt%2FUYSchwQA9QUyXLEAl55nnaZxTx1T5MBC29Ct8tysXkdBlC9uAHz9e7bcEiO1V%2FFyJUQWkp69MZKy%2Fb9V%2BUPRCyQjXrEfMP2I8rByCAiCyrK31MxpAAxJP5aRXPDhTzkjlIUMAos9SG2t4QUkiGRng0x9uRsT7OOGMRVKIR9yb%2BdmIruF3lL4Zyu3vse2a%2F2haK%2FVfgf5iCPxmNWpM6LfQiHHXAcbX%2F3ye%2Bwe5vOrJK6jpbXTMAa2zwlKHqxIPcIhOKHGUQeYvSDVF6lQTSmsRRJ4BKibm9pU81VlKbTGzWNZKNfzue1JjRhYbomvSR8xZJY9FHudIPXVmrlnlrKLykTV7c4h6LHymdY91iHZ%2BzNtrPEumuQPYKR%2FZgQUc4KjXDlu4bG4Ke1RNwQwZMRjMuSwyxF0bPaF%2FvmPAe6oQdcksvI1Mo0b4%2BXK6XSfr7nZc8iRLCvHvd%2B%2BpFkZrwMILpttAGOqUBS5DoMZBCOavN%2BXjz6RNOur6lZnvwjfaxQt9r%2Bv9w6AKgMbz44VQtxrhADGprqkGcDlkTk5MZgg6ZG%2BmADT2OMl709x79lImns6yaq8ZbqZ34ZvrXp7%2BWG1cn%2FmqqQxsOS%2BQNUwel67aPjy7EIk56bSADHIsKdvfxf4Z3bZXGyyYSILaYK9qnWtM%2FwNzCzjvbl6iuR5bywO1TgggQd0lrCb9cGado&X-Amz-Signature=d02e4288783aaf53ac8d2693c438cff5c360c040493e33e95abed0596bd25938&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
