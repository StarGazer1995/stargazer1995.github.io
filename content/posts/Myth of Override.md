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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJDF7H4%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T175518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIFoM%2FZvswE1YGU90qoH9j6CWUMi9ZdK1hI9M2OC4p82XAiBboWna8gCED%2Fo%2FgfXqrO3G%2FBoUKj2IGl1uuat1%2Fu918SqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl16lVxwnVZu1nOilKtwDaCVI6%2FfTxp2dVSeq0697c0SXOe4noIHUOlquHUi21GWBqzUq7ZXGJy2v5Xm%2BYbOCE1hu8O9EvBAWGmELejYTAESuGkJLhrD%2FB9rbc4FMJSfpxlrOT8qQTSXJwaJJFOMV%2B8KE3oD8zzognMrSOiNtQ%2BrbPeZial00LcjAJSVTCOiBuUsOJsSUBmxB77TCoGRFIMJSPFDLUCeOy%2FYMckc1XjEDIaMVHsJxuUMSjsrxorK2b%2Fe9ed9khVfqqvf6h54n15jZreqd4LiJJeXUyd5ents%2BHMaOJ7NwFBqmFJ4PZW4dN9xiM858eKuUdibp%2F8klAQ7uetj0nZK7l7a5FYzmNvp5ckAai3s4wP3z%2FmXnNCJJC4GPo6zD4w6NxK4iVaqE%2B0l5ZcyjBLRC4ZLxXWIJ19AkEeE9gMg126U6NFdY1LwMliLPoDvlFVFrAINYUDtaTY%2FRywon8f9S%2FGsZoult9D5V0d%2FnI7OvT4NJjM%2Bco2h9QL99Y8UKxXl5%2FQvX444pYGr5Xd%2FE1Y4JRAgKzKSjqR38Xzt%2F9stmV%2Fue8O0mqVLLQhYLyba8RPmta9ArSNWzGp8nWWX%2B9%2BAFJVxNPPgP0E4K02dmX0vWrFialnotxEYWQ0WcsVhGd2R2asYws4aK1gY6pgE2KxGIyQeodPbg4D0chRaNrPbyaV2eKHQURjrmmz8RNPXeDCaQ4e8Z95vGRx8j73Fp3ZRJVYSf4MmPOq%2B02Ccl3Pa06F5rge9i9HRWqMG3YpQ1xgUoR54molil37JujPxw3M4%2B5FeWiCV8VAe%2FihQSjrjqZ29MC33OEg5MQoCRqrYPNPQqm9f%2FY94TbvJVbVCKwh9nDBjPrD2cu0mDuIjngqgHpE9C&X-Amz-Signature=beded13c82ef8e7664ed1edf70bfc5c52445ff06379b0b108dcc54fe74906112&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MJDF7H4%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T175518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIFoM%2FZvswE1YGU90qoH9j6CWUMi9ZdK1hI9M2OC4p82XAiBboWna8gCED%2Fo%2FgfXqrO3G%2FBoUKj2IGl1uuat1%2Fu918SqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl16lVxwnVZu1nOilKtwDaCVI6%2FfTxp2dVSeq0697c0SXOe4noIHUOlquHUi21GWBqzUq7ZXGJy2v5Xm%2BYbOCE1hu8O9EvBAWGmELejYTAESuGkJLhrD%2FB9rbc4FMJSfpxlrOT8qQTSXJwaJJFOMV%2B8KE3oD8zzognMrSOiNtQ%2BrbPeZial00LcjAJSVTCOiBuUsOJsSUBmxB77TCoGRFIMJSPFDLUCeOy%2FYMckc1XjEDIaMVHsJxuUMSjsrxorK2b%2Fe9ed9khVfqqvf6h54n15jZreqd4LiJJeXUyd5ents%2BHMaOJ7NwFBqmFJ4PZW4dN9xiM858eKuUdibp%2F8klAQ7uetj0nZK7l7a5FYzmNvp5ckAai3s4wP3z%2FmXnNCJJC4GPo6zD4w6NxK4iVaqE%2B0l5ZcyjBLRC4ZLxXWIJ19AkEeE9gMg126U6NFdY1LwMliLPoDvlFVFrAINYUDtaTY%2FRywon8f9S%2FGsZoult9D5V0d%2FnI7OvT4NJjM%2Bco2h9QL99Y8UKxXl5%2FQvX444pYGr5Xd%2FE1Y4JRAgKzKSjqR38Xzt%2F9stmV%2Fue8O0mqVLLQhYLyba8RPmta9ArSNWzGp8nWWX%2B9%2BAFJVxNPPgP0E4K02dmX0vWrFialnotxEYWQ0WcsVhGd2R2asYws4aK1gY6pgE2KxGIyQeodPbg4D0chRaNrPbyaV2eKHQURjrmmz8RNPXeDCaQ4e8Z95vGRx8j73Fp3ZRJVYSf4MmPOq%2B02Ccl3Pa06F5rge9i9HRWqMG3YpQ1xgUoR54molil37JujPxw3M4%2B5FeWiCV8VAe%2FihQSjrjqZ29MC33OEg5MQoCRqrYPNPQqm9f%2FY94TbvJVbVCKwh9nDBjPrD2cu0mDuIjngqgHpE9C&X-Amz-Signature=374a80890a944e58177397e5e2254a9c9699556bb4766d141d02cf2a4473498c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
