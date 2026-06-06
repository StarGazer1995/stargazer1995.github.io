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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC4S3RXH%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T190300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCq5AkSIdTNGoO8Ek5nWWIVKRjM9m3gEQzmLLoNz3WoKwIhAKgdOBxkQC8Auw0Gj5PcqGzaHEyJNKJJQgbfjRnJZPBjKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzvbb84Z99BVTiiLQ0q3APUXG1CxRWlzR6JNvIVL8jR9JU%2F6giF7fx%2FUouktVdOzo2tmfbxUyYm59GkX%2FLsDC2A10nbaESNqYVL3YNryMmLzdVvbzCAHq7nZlM1wGWtTAzUIOcABNepnU%2Fee3xrh%2BGHmw2rEfKIir0E06V%2FOAmIXZvzmrZw4g%2Fr9eO%2FFRCt%2FbWUq57Pduq2nYKgH7jRGHJFaqGQ6ojn%2BmjN7asFsV82FP6WE0EFpGVdDvwco3%2FqK9xw4tRczu5UttJHOkL0wpMJnozel%2FOxiQQb8akfnLCnmKyYXJxYMufYxcpALbtZaB7upN9zcB4gMCr%2F6B77ps5DsW%2FYZCQW%2FhQtcGNK4NytmGZDpCZhHaL2h7MwwQlDxPgk6Mrdvk1fTAKJdzXfdfYjGZ8yFYsDYWnPpr%2BP8KCPj25JReuRSV44%2BV2DeRNEVzD7%2B%2BSB8MUsrXXaA%2BmPY0N8eVJZhPcJ3snyosrnfFErgM%2BJXwRrqZ6arZSxI%2B5c6unA0D5w0T9z5W5i3k3sctO%2FCznF1U2DRZIIsFEgGDZ4bgWa8%2BnjCjy2JaqYKW8uW8qY%2FdMYAF2RfbvIw5gzPfKTg%2FJ2Z%2FW6nofpGlvnjoi%2FY6hTSXHRflotWdYyrnovOTsQfqjGpYNHjNNH%2BzCqxZHRBjqkAR6GxqT2qP3m2CbFhzB4ENLSW26kj3qqBTY5RewaDi0H5oYwqEMeSC%2B1BXS5LdeRjBtc241Y6I3ulTRFfON9bzV07SSEqbsG%2Fdrko88hPD9oFEx92BzHta89s3rqYlEcbJ%2BrNxrW6L3StSy%2BeokVvyWeyjnQiN2mN9Rj7C0FjXKGG5gLIn3zGZJL1sp8uQGUDLzCsYBndd4bnzp5qKx2URqSsr6d&X-Amz-Signature=b2234d9009dea657cebfa339584f60d02ba85636387d8edf91232a847ddf2e78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RC4S3RXH%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T190300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCq5AkSIdTNGoO8Ek5nWWIVKRjM9m3gEQzmLLoNz3WoKwIhAKgdOBxkQC8Auw0Gj5PcqGzaHEyJNKJJQgbfjRnJZPBjKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzvbb84Z99BVTiiLQ0q3APUXG1CxRWlzR6JNvIVL8jR9JU%2F6giF7fx%2FUouktVdOzo2tmfbxUyYm59GkX%2FLsDC2A10nbaESNqYVL3YNryMmLzdVvbzCAHq7nZlM1wGWtTAzUIOcABNepnU%2Fee3xrh%2BGHmw2rEfKIir0E06V%2FOAmIXZvzmrZw4g%2Fr9eO%2FFRCt%2FbWUq57Pduq2nYKgH7jRGHJFaqGQ6ojn%2BmjN7asFsV82FP6WE0EFpGVdDvwco3%2FqK9xw4tRczu5UttJHOkL0wpMJnozel%2FOxiQQb8akfnLCnmKyYXJxYMufYxcpALbtZaB7upN9zcB4gMCr%2F6B77ps5DsW%2FYZCQW%2FhQtcGNK4NytmGZDpCZhHaL2h7MwwQlDxPgk6Mrdvk1fTAKJdzXfdfYjGZ8yFYsDYWnPpr%2BP8KCPj25JReuRSV44%2BV2DeRNEVzD7%2B%2BSB8MUsrXXaA%2BmPY0N8eVJZhPcJ3snyosrnfFErgM%2BJXwRrqZ6arZSxI%2B5c6unA0D5w0T9z5W5i3k3sctO%2FCznF1U2DRZIIsFEgGDZ4bgWa8%2BnjCjy2JaqYKW8uW8qY%2FdMYAF2RfbvIw5gzPfKTg%2FJ2Z%2FW6nofpGlvnjoi%2FY6hTSXHRflotWdYyrnovOTsQfqjGpYNHjNNH%2BzCqxZHRBjqkAR6GxqT2qP3m2CbFhzB4ENLSW26kj3qqBTY5RewaDi0H5oYwqEMeSC%2B1BXS5LdeRjBtc241Y6I3ulTRFfON9bzV07SSEqbsG%2Fdrko88hPD9oFEx92BzHta89s3rqYlEcbJ%2BrNxrW6L3StSy%2BeokVvyWeyjnQiN2mN9Rj7C0FjXKGG5gLIn3zGZJL1sp8uQGUDLzCsYBndd4bnzp5qKx2URqSsr6d&X-Amz-Signature=4df9a2731f5a0e8a693952768561f525bbc6f62d7bc69dfe83565ecaa34f38fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
