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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625LBZQKZ%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T164459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQC%2FhXi2YNMRkRMBMAvc9z5WTTbhOLZHCL5sG6R54aVVhgIhAJWutPQawQtRcjRe4ED7wC8193UfeH8QJ26JJGedJRZiKv8DCDkQABoMNjM3NDIzMTgzODA1IgyIgWdQyoZRg4bfgcEq3AMCBnRd6dRUHjMODc3TKDpHaSsRdcyXCgmlp%2FGF346KCTy2gyUJINknvGXybtukf7%2BYO%2FKqpxCkoUi70Jv8OWOTT0S8eWBxxEMPnO3mNxNpwEIouYljlw1DBrtMsskhF1pVDWrD49QWVNv31u%2FITPSWSnpKRkVZRCsLFkIqGpfcjqFP%2BLNdACuoKqsYbU8SwuZSUqZObP8pQoikPg7%2F%2FYwWzaBSF%2FPBGRAHOmjeRo7VcaKNLIch7Vw8ocBNSUIR4qZNezT4CsK8Hu5s0rBxSrKjhkjBKlN7BHENSDJIxziIYWSjmWElKqhX8vL7n6H0cLxAZCJ3Ks5iS196lNBOup10LE%2BgZG1ZPGUCkcuC0NAow0PvXVieBS514WKzxrEDV6Y%2BUIHziU3Iom3iViD9%2BynKqUH6sUcKD5DIE8a6g%2B5nOB648HIRVHgiiB0%2FeUsX45bO1lFZmBPm3tt7armNVTqxR3QW0JmZes6oUSH8KL1XfTmOHtKXpWgFpYWtTPE7ZmOCMr3LN0cCY7BFUvZnINjr5fppEINA7Y4xZs2HnAgSCLUVwPN2ItnMoW4BvOCiHYPUDAUH6jheGM6mosgBWOosrwhAISYnpt%2BAbNH892x3Yt%2BMcXiJzkHCWjEMrTDh6ZjTBjqkAcCC%2FsDrlIUT4%2BryS4eAKZi58IUvlQ4WUxckB29Km6xuhB0azFcC%2FCkXSLfz0AHmHqM974I2VrYQnnKplH%2FLVwEHwHTThdZ824%2BIX%2BVvGi5xhRsGS5W6m81jELc2KAY9eP5L%2BHIF5Q8y6SmzS%2F8grgQVi%2F8dNnWRHzQMYvw1T8XXVjcn%2FOu%2FLbcdS31xjs5eGcFA8Zrowv3zXV7f2Skx20%2BOEq7x&X-Amz-Signature=889ec304bc7a1328edeb90f2e777570a49a15d53992f977d5182e5657d355934&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625LBZQKZ%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T164459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQC%2FhXi2YNMRkRMBMAvc9z5WTTbhOLZHCL5sG6R54aVVhgIhAJWutPQawQtRcjRe4ED7wC8193UfeH8QJ26JJGedJRZiKv8DCDkQABoMNjM3NDIzMTgzODA1IgyIgWdQyoZRg4bfgcEq3AMCBnRd6dRUHjMODc3TKDpHaSsRdcyXCgmlp%2FGF346KCTy2gyUJINknvGXybtukf7%2BYO%2FKqpxCkoUi70Jv8OWOTT0S8eWBxxEMPnO3mNxNpwEIouYljlw1DBrtMsskhF1pVDWrD49QWVNv31u%2FITPSWSnpKRkVZRCsLFkIqGpfcjqFP%2BLNdACuoKqsYbU8SwuZSUqZObP8pQoikPg7%2F%2FYwWzaBSF%2FPBGRAHOmjeRo7VcaKNLIch7Vw8ocBNSUIR4qZNezT4CsK8Hu5s0rBxSrKjhkjBKlN7BHENSDJIxziIYWSjmWElKqhX8vL7n6H0cLxAZCJ3Ks5iS196lNBOup10LE%2BgZG1ZPGUCkcuC0NAow0PvXVieBS514WKzxrEDV6Y%2BUIHziU3Iom3iViD9%2BynKqUH6sUcKD5DIE8a6g%2B5nOB648HIRVHgiiB0%2FeUsX45bO1lFZmBPm3tt7armNVTqxR3QW0JmZes6oUSH8KL1XfTmOHtKXpWgFpYWtTPE7ZmOCMr3LN0cCY7BFUvZnINjr5fppEINA7Y4xZs2HnAgSCLUVwPN2ItnMoW4BvOCiHYPUDAUH6jheGM6mosgBWOosrwhAISYnpt%2BAbNH892x3Yt%2BMcXiJzkHCWjEMrTDh6ZjTBjqkAcCC%2FsDrlIUT4%2BryS4eAKZi58IUvlQ4WUxckB29Km6xuhB0azFcC%2FCkXSLfz0AHmHqM974I2VrYQnnKplH%2FLVwEHwHTThdZ824%2BIX%2BVvGi5xhRsGS5W6m81jELc2KAY9eP5L%2BHIF5Q8y6SmzS%2F8grgQVi%2F8dNnWRHzQMYvw1T8XXVjcn%2FOu%2FLbcdS31xjs5eGcFA8Zrowv3zXV7f2Skx20%2BOEq7x&X-Amz-Signature=017a3342b69120510098e0c16d3e0a7b5e8f6add61c5770628276d5352184e56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
