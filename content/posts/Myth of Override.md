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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RECUGL2M%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T165104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6AKfSZIn%2Bp4g80W1Nzmw2tHZozQnq4aDPzMLDsJtcUQIgKasTts%2BPKvpK62%2Fm94nDlYcDlrt8Gy6qt5s9Hu%2BvKOgqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKm%2BXB6x1bpJWnTOvCrcAwV%2FN7KZ2nEBwouQbXmCAJaoyDbLlAa60oXIoTsd0xHbAXeXtWTRN8ZshCJr8YVW8AAWg9mzjR8UI6FZat6%2FARUyOJ9dRcg4bWNFKRjJjboEfYBwH1nqvKr%2FSo2dY7tKCm7Y0RK%2Bz282EWbjwz3frkp0QSfSV1icdTIRQiQdAtmmDVsFyeOfMgsKDhGlBpWCuyyzvP60BYk440vUpV0iGQyi3tnwNmvEkXXBRYOypbTQCQ4Ze6bBES9le6uK5vejW6fFA9FKqQbPdhEjma0GstURBp1XGsOj2r1MyhvtTVkCh%2Fn8rrfrT5L5B5Rc40YKHMGbItMtXtOgH44167MiAsPcd%2BiXq3ZzzmrEovl5EbW%2FSBWSXXwex9tZz0slQs8jAdAaSv5KL%2BPbA2YsqHlqfhYLznAU9aiMlkQeQZenvQGb7zjvZVrgCBiZZgcRBMgXvp%2BNrlGGMb6u30Yd7Gnin3TSMLVxHRw6myTOGYjLzOyUfLV0A0nC1WhKlK05x6dC65LZyY%2BBSCnBgBn1%2F1io675r4Nuu7yDqxFg%2Fr5uDBUh8aK4KPOARjmV5AXtAQTRJaQyfhlTASmWMg7tPCwzlBFHF3wzAH5YVjAeRNIGTDz3cLPn1WpjpRc1EMjEJMM2y0NEGOqUBtAM41J6Q4smdfPN0dhv0ghdw36LnBwqUxbQ1No7015Mq0eF3bAImKWEJXVDwHzuV2iSW%2Byt%2BnWTupDfUYPzTM2KhabvxlVW9XeVCxPMKs6uUxYbhpqS3VyLYzoZ7d%2BC7kbVT%2FiO%2BI%2B1ln%2F%2B%2BzvVDr7D07718rp%2BMTG5%2BU%2B5VDvD%2FzuItXxzCWegF00yrzqStOx%2FsHJNWGgI%2BbYeNVgZpl1oin5V%2F&X-Amz-Signature=1d8f715f0a067e603f2015c9d852558ab4f78cf25f606cc1e00dc3f0085a4eef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RECUGL2M%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T165104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6AKfSZIn%2Bp4g80W1Nzmw2tHZozQnq4aDPzMLDsJtcUQIgKasTts%2BPKvpK62%2Fm94nDlYcDlrt8Gy6qt5s9Hu%2BvKOgqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKm%2BXB6x1bpJWnTOvCrcAwV%2FN7KZ2nEBwouQbXmCAJaoyDbLlAa60oXIoTsd0xHbAXeXtWTRN8ZshCJr8YVW8AAWg9mzjR8UI6FZat6%2FARUyOJ9dRcg4bWNFKRjJjboEfYBwH1nqvKr%2FSo2dY7tKCm7Y0RK%2Bz282EWbjwz3frkp0QSfSV1icdTIRQiQdAtmmDVsFyeOfMgsKDhGlBpWCuyyzvP60BYk440vUpV0iGQyi3tnwNmvEkXXBRYOypbTQCQ4Ze6bBES9le6uK5vejW6fFA9FKqQbPdhEjma0GstURBp1XGsOj2r1MyhvtTVkCh%2Fn8rrfrT5L5B5Rc40YKHMGbItMtXtOgH44167MiAsPcd%2BiXq3ZzzmrEovl5EbW%2FSBWSXXwex9tZz0slQs8jAdAaSv5KL%2BPbA2YsqHlqfhYLznAU9aiMlkQeQZenvQGb7zjvZVrgCBiZZgcRBMgXvp%2BNrlGGMb6u30Yd7Gnin3TSMLVxHRw6myTOGYjLzOyUfLV0A0nC1WhKlK05x6dC65LZyY%2BBSCnBgBn1%2F1io675r4Nuu7yDqxFg%2Fr5uDBUh8aK4KPOARjmV5AXtAQTRJaQyfhlTASmWMg7tPCwzlBFHF3wzAH5YVjAeRNIGTDz3cLPn1WpjpRc1EMjEJMM2y0NEGOqUBtAM41J6Q4smdfPN0dhv0ghdw36LnBwqUxbQ1No7015Mq0eF3bAImKWEJXVDwHzuV2iSW%2Byt%2BnWTupDfUYPzTM2KhabvxlVW9XeVCxPMKs6uUxYbhpqS3VyLYzoZ7d%2BC7kbVT%2FiO%2BI%2B1ln%2F%2B%2BzvVDr7D07718rp%2BMTG5%2BU%2B5VDvD%2FzuItXxzCWegF00yrzqStOx%2FsHJNWGgI%2BbYeNVgZpl1oin5V%2F&X-Amz-Signature=f1cb8c53bfc8013dd3014b35eb42c5d492c13a296117d63e42278cdc2d5b6419&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
