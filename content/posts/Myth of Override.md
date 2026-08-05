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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE66E4GC%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T081345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEWVHgJBq0qrRh8zJR83gMJZ0%2F0wuuFSJwVDpmHtEKmjAiEA3tQ96QIyK13I7VdOsnin4CnhhfjK7VsJSlYXxM3PSGgq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDIKNA30lemqS0fyRgCrcA02OK9ThhkFbdYV0z2arbnIrTcQzHvl%2FgMAkMd9IaskYdQy8VLUohIqfEjJi2vGVVJoY%2Fn3ZW6vN%2B5OGhgE3pdiR%2FmOSw3kXOE29iHmT2%2Bb7eMa3mLX3nDRfy0pJgff%2B9nbz5F%2FfyraJccNIIvXWwiW6CIcEYRf8kNhzMU41ZLE9TNWvYS3hDebE0lTannNAuKMOIEec8n%2F9rFeM49g7w%2FwlZZ81QY38k0m3xjTDRd073lcecntex%2FfYNJPYYGIP%2FQZmIIsceojQaUid1UTjKuQ2IJvzcVrFRNjoO%2F7V8GMhHsKtFFmOIw8dLV1i3r9RTa0cMdUyBFPLQJ9TnZgRMjYhEkBI4U4rPggCvVQnvntxeGMpkDevPghs1A67xpZdD686huLY%2FyBSjtcbGtnRSRf1B1Cwij%2BCLqhpFK3IdfKlNUM4izy1HCBUQVoWMO0FDLstVmKe4W4fm6sO%2F%2F5gT6iwZnbxqh3V0%2Bw74LbgQ8HFANRXjmEzLOzjgy2UAAORNNMCP9FZG6btD3Jns1hXxwGb7MvYDJqoicxs%2Bl9mIWZwLpuUBFpTLed31d%2FqUvL%2FptcTeAgS4slAHox%2F3kZ7L%2Fjsy679%2F%2Bk%2FgLu4sdhBUY%2BKQN0SM9jvS0VHabL0MKHdy9MGOqUBiVbW5%2FMBfP1BrFXcpUFbV0po8h3NU9ZZaATvIC%2BlcNTnF5oa%2BkiKqiE9kUyxnitgjpdfS8j3F%2BqYWKJAzuRpaud1xBt96qz6gb1%2BmZAAGWwKFHIECc57rZ0xkBkfpG4QpKc4gtJgxF5gb%2Bo9%2Fa70lAoJG6%2BF3n%2B9dP89GmzB4rBOytZWyBKR9ePpgViXgAnTFbYOvjCFNGvBuyATmnBJQCuOuDTR&X-Amz-Signature=14a2623bd4eea31f2f00bd0f36cb8a6d6ec80dc626438d15afc27e7e46787772&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE66E4GC%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T081345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIEWVHgJBq0qrRh8zJR83gMJZ0%2F0wuuFSJwVDpmHtEKmjAiEA3tQ96QIyK13I7VdOsnin4CnhhfjK7VsJSlYXxM3PSGgq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDIKNA30lemqS0fyRgCrcA02OK9ThhkFbdYV0z2arbnIrTcQzHvl%2FgMAkMd9IaskYdQy8VLUohIqfEjJi2vGVVJoY%2Fn3ZW6vN%2B5OGhgE3pdiR%2FmOSw3kXOE29iHmT2%2Bb7eMa3mLX3nDRfy0pJgff%2B9nbz5F%2FfyraJccNIIvXWwiW6CIcEYRf8kNhzMU41ZLE9TNWvYS3hDebE0lTannNAuKMOIEec8n%2F9rFeM49g7w%2FwlZZ81QY38k0m3xjTDRd073lcecntex%2FfYNJPYYGIP%2FQZmIIsceojQaUid1UTjKuQ2IJvzcVrFRNjoO%2F7V8GMhHsKtFFmOIw8dLV1i3r9RTa0cMdUyBFPLQJ9TnZgRMjYhEkBI4U4rPggCvVQnvntxeGMpkDevPghs1A67xpZdD686huLY%2FyBSjtcbGtnRSRf1B1Cwij%2BCLqhpFK3IdfKlNUM4izy1HCBUQVoWMO0FDLstVmKe4W4fm6sO%2F%2F5gT6iwZnbxqh3V0%2Bw74LbgQ8HFANRXjmEzLOzjgy2UAAORNNMCP9FZG6btD3Jns1hXxwGb7MvYDJqoicxs%2Bl9mIWZwLpuUBFpTLed31d%2FqUvL%2FptcTeAgS4slAHox%2F3kZ7L%2Fjsy679%2F%2Bk%2FgLu4sdhBUY%2BKQN0SM9jvS0VHabL0MKHdy9MGOqUBiVbW5%2FMBfP1BrFXcpUFbV0po8h3NU9ZZaATvIC%2BlcNTnF5oa%2BkiKqiE9kUyxnitgjpdfS8j3F%2BqYWKJAzuRpaud1xBt96qz6gb1%2BmZAAGWwKFHIECc57rZ0xkBkfpG4QpKc4gtJgxF5gb%2Bo9%2Fa70lAoJG6%2BF3n%2B9dP89GmzB4rBOytZWyBKR9ePpgViXgAnTFbYOvjCFNGvBuyATmnBJQCuOuDTR&X-Amz-Signature=b15ebbf344c927b6d67292ea10729af05a5eca034f9fd65d30d3051d517877f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
