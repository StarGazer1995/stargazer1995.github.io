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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXN3ASGU%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T102105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfnB8VEe%2BZGOjVBP%2FkiYGHCHJ9YMfZsPloAPHIWX7BiwIhAKjg%2BiaQrhytUNvySk9TajZpvSY8CXkc07ILC4SUIQC2KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgywLPL6nXfm6uOhdMIq3AOBxBwAzcnxYfFio7hR2t%2FlwH4tZGIUnFPsUJGCODCzt1YiSGW%2BsRV2sEdZ12JHAKQTHnH%2Bpu8vmLDIXRBKDa69S%2BKqjrBrKpuem7mXav5b7NJp8HNci7qLbXQRiiQfm2jssfFvmnyGtRFLRSCHJXGjTnXnRHEuZTOtGbVrEajGj48uDhGfHTlGAKNJkFRSripuFTszHM7Yj%2BovWBgJx038kt5rpTJMQqbOJC5VMEBSzFzGt9Z%2FNgjGQriUF0jgDMDgmX73N2EFmEHNpa2YCNxRRsb%2B6zzbn9unqdvqg%2BG5FIg0%2FlOXSCx8RhZXDc0iDtYVYlFba2YaY%2BkdAJDZf%2FLrgIDSEiR7MmNwTc0KejG8H3%2BiCb7OuoO1hV2XdSP8GSvvZUbstkhwRBrhh7xxSMjUzqig98b4ayMkJiKCLBAZauw7khN81EJNut%2FcczJZ1Zteld0gukwOvLlbHec4Xr%2ByVz18YGOj41S4zUb62WjpMmL3TpUg%2BWUYf8z6tHW%2BIoiXYoYrdUODoMEFCm44x8TxfgDd4zd8zAwaRjw3dn44h85%2BDN%2BMnFCetG7h4mDCNkIXI9oWeJIjDYQmpbhi7U1GmhBl8L%2FVy96811ViNyR%2FgvVkKmvoC2fUTeX4SjCo%2B5TRBjqkAV%2BHA8R%2Br0C6Mh8cRSHCu5icanh7RMhIhp2V9jNx%2FOK5HMrRqiggGsx45wVU5dc4S8iBgiFClf%2FhuFJtlVnrWPztWRUYUGSQFeHNAfF4xX031aaaVgyQApzOwkiN6jwuXJo3iLGfjzJfZZ2M2LOMusF9JvlhJ4mawdOphjBrzYsuAbMmH%2BuCziYc1Nztl6lbj233ZcQ0M9uXlpFRtdXVxB6tdogi&X-Amz-Signature=6f97f722d2021c7fa119984b12822c334f2453d4280d7ae212a6f124d9206ecc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXN3ASGU%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T102105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfnB8VEe%2BZGOjVBP%2FkiYGHCHJ9YMfZsPloAPHIWX7BiwIhAKjg%2BiaQrhytUNvySk9TajZpvSY8CXkc07ILC4SUIQC2KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgywLPL6nXfm6uOhdMIq3AOBxBwAzcnxYfFio7hR2t%2FlwH4tZGIUnFPsUJGCODCzt1YiSGW%2BsRV2sEdZ12JHAKQTHnH%2Bpu8vmLDIXRBKDa69S%2BKqjrBrKpuem7mXav5b7NJp8HNci7qLbXQRiiQfm2jssfFvmnyGtRFLRSCHJXGjTnXnRHEuZTOtGbVrEajGj48uDhGfHTlGAKNJkFRSripuFTszHM7Yj%2BovWBgJx038kt5rpTJMQqbOJC5VMEBSzFzGt9Z%2FNgjGQriUF0jgDMDgmX73N2EFmEHNpa2YCNxRRsb%2B6zzbn9unqdvqg%2BG5FIg0%2FlOXSCx8RhZXDc0iDtYVYlFba2YaY%2BkdAJDZf%2FLrgIDSEiR7MmNwTc0KejG8H3%2BiCb7OuoO1hV2XdSP8GSvvZUbstkhwRBrhh7xxSMjUzqig98b4ayMkJiKCLBAZauw7khN81EJNut%2FcczJZ1Zteld0gukwOvLlbHec4Xr%2ByVz18YGOj41S4zUb62WjpMmL3TpUg%2BWUYf8z6tHW%2BIoiXYoYrdUODoMEFCm44x8TxfgDd4zd8zAwaRjw3dn44h85%2BDN%2BMnFCetG7h4mDCNkIXI9oWeJIjDYQmpbhi7U1GmhBl8L%2FVy96811ViNyR%2FgvVkKmvoC2fUTeX4SjCo%2B5TRBjqkAV%2BHA8R%2Br0C6Mh8cRSHCu5icanh7RMhIhp2V9jNx%2FOK5HMrRqiggGsx45wVU5dc4S8iBgiFClf%2FhuFJtlVnrWPztWRUYUGSQFeHNAfF4xX031aaaVgyQApzOwkiN6jwuXJo3iLGfjzJfZZ2M2LOMusF9JvlhJ4mawdOphjBrzYsuAbMmH%2BuCziYc1Nztl6lbj233ZcQ0M9uXlpFRtdXVxB6tdogi&X-Amz-Signature=38d274c71548d5d71f06bbe23a2f1a984e5c6a5cbab58ad11cbfd5fe726f5210&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
