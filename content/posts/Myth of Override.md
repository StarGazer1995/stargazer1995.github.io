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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662X6JTNTR%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T134148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJIMEYCIQDaBK5WkBvngAIkZhMl8ciAdBhbC1%2Fxpo6g9mQoxIf4LwIhAMWmzGC0B9gexnktzTyTWI3dIypfhcE%2F42quAD2%2FZgqjKv8DCA4QABoMNjM3NDIzMTgzODA1IgzDh0%2BS%2BIq0Cr%2Bfkwwq3APLmqpD4o83iHYjnJ8n4zK%2F9qXMA0zlq41%2Frae3TP5P%2FCzXQAb3pk%2B%2BITpansSld9cH77Zw%2BTUXWzsAKQGAclUYbtII4vBZj7X8N4PtQ3NKz2NfLeG5EI%2F5fxFSZ%2Fo3EBnuMS5%2FLve346Y2x%2FWvjULmTmNNVii%2Bk7OC%2FdUC21bq%2B%2ByW9DjG0lK1boYjM5BzxPMw2qSIJr2utAzZNVT8s6H9TOHP1ZYCVSVswXflUD7usLJZO1JHLZFuzhumZoeIuUuAq0D8U1ld0ljR1ptJNDYdmm8En6zPPCyxByTyZNKzQ7ddn1Dy%2FERYWiVOqO7%2Bapn8%2BYHhGnPNsgbr8IsZBpH6dIttCb9yMN7PE6%2FNOKAuBpAK5o7QieU8nqyzxWBJo%2Bz%2BfB%2FQTYD09kyIgjStNaeIyiweAxfPK6dnvCFztxv8DZ6exEj4KvLKQSSOfgWxaqkYjLpktKmP%2FRDTx%2BS0Km1XkZU6boymqj9ba608%2BmUMPNQge7TM1MMrKUtESAgJfP%2BJp92Ut4dAt0JeZmDOW7ZHnDGI8tr39pgQfw7jbIXela3nJ%2FmIFRcR6EyiXnRg20Z4x6chofeNJl1PqOB%2B71CFvvBpn%2B%2BGCOdADoJPhR24NbIcxxqqx%2FnszEmH8DCJwsfTBjqkAXBu8Kr4Zl%2B5103Kr%2Fn4qBKr%2FiUdd2ORF1sKNRertA0b0GE8X97uB4Kjrt9VBmSITWNY7SffrAmnrmwol%2FP78R62u9N5%2BGimOb7q9zl8V6N0ppD2eulSMfUJeUPVyvkZHosmvIAsIPDUetKOgJwgUhHInoyNzVB%2FBQs2ZntO3qbNTmh3iJLXuqkISRrUUgypaocLYgXkkhFb7r1RKwFUOsbcB%2BVf&X-Amz-Signature=433c8fbac4ac9a41bcd8f8dc96d8220082d5844a2b7d654fabaf37dfa948be48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662X6JTNTR%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T134148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJIMEYCIQDaBK5WkBvngAIkZhMl8ciAdBhbC1%2Fxpo6g9mQoxIf4LwIhAMWmzGC0B9gexnktzTyTWI3dIypfhcE%2F42quAD2%2FZgqjKv8DCA4QABoMNjM3NDIzMTgzODA1IgzDh0%2BS%2BIq0Cr%2Bfkwwq3APLmqpD4o83iHYjnJ8n4zK%2F9qXMA0zlq41%2Frae3TP5P%2FCzXQAb3pk%2B%2BITpansSld9cH77Zw%2BTUXWzsAKQGAclUYbtII4vBZj7X8N4PtQ3NKz2NfLeG5EI%2F5fxFSZ%2Fo3EBnuMS5%2FLve346Y2x%2FWvjULmTmNNVii%2Bk7OC%2FdUC21bq%2B%2ByW9DjG0lK1boYjM5BzxPMw2qSIJr2utAzZNVT8s6H9TOHP1ZYCVSVswXflUD7usLJZO1JHLZFuzhumZoeIuUuAq0D8U1ld0ljR1ptJNDYdmm8En6zPPCyxByTyZNKzQ7ddn1Dy%2FERYWiVOqO7%2Bapn8%2BYHhGnPNsgbr8IsZBpH6dIttCb9yMN7PE6%2FNOKAuBpAK5o7QieU8nqyzxWBJo%2Bz%2BfB%2FQTYD09kyIgjStNaeIyiweAxfPK6dnvCFztxv8DZ6exEj4KvLKQSSOfgWxaqkYjLpktKmP%2FRDTx%2BS0Km1XkZU6boymqj9ba608%2BmUMPNQge7TM1MMrKUtESAgJfP%2BJp92Ut4dAt0JeZmDOW7ZHnDGI8tr39pgQfw7jbIXela3nJ%2FmIFRcR6EyiXnRg20Z4x6chofeNJl1PqOB%2B71CFvvBpn%2B%2BGCOdADoJPhR24NbIcxxqqx%2FnszEmH8DCJwsfTBjqkAXBu8Kr4Zl%2B5103Kr%2Fn4qBKr%2FiUdd2ORF1sKNRertA0b0GE8X97uB4Kjrt9VBmSITWNY7SffrAmnrmwol%2FP78R62u9N5%2BGimOb7q9zl8V6N0ppD2eulSMfUJeUPVyvkZHosmvIAsIPDUetKOgJwgUhHInoyNzVB%2FBQs2ZntO3qbNTmh3iJLXuqkISRrUUgypaocLYgXkkhFb7r1RKwFUOsbcB%2BVf&X-Amz-Signature=f26ee10134f22a457be0b1ec5906b1647db01e91a01be44044483be5e387ac0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
