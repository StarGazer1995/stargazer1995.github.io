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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTFQI76Y%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T020049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDoXwdLoyyWEyOzYd8Ngq55VMMaD%2FD%2F8To%2Bri3cmfLvsgIhAJdBA6T7T2RAvIhJnM5A%2BS%2F%2FoHppw7AMmkb1TWLT0KEJKv8DCBMQABoMNjM3NDIzMTgzODA1IgwV38aGEWwTf%2FepDjMq3AOcNGCNhRfVw8atms%2B%2BVTI8gUPDVCw5TupoUl9%2BbfqRUgRT3ljmDMVDCJHIIAwhOlr0iSEbb%2FFDAg8eAr5T34luX443Ky2MjceTpi9QCDK7d%2FErGgTmVfmU%2F72kdDdHyyybE86yMBEjqtZKi0odbS%2F7Ijo0RW2rxYB2R9mHH%2FqRqKmjlKZZq0ek2F4qNlUXFxjOZc3exhsB4F4OYdqwMY3KHllQFTjRVKhsAVK5bYndDIFy278fHYkKgNB5UdqTMvMLKWgDP%2By96h8CEUDJ1qAMc0NaRCgQbifKCFexZ%2BmA3RAUoU7bccGxDZSKYs9gDlfGnDKv2L3pUsd6NiMgC8JbUBcLt4AT6ApURv1268%2BIDQb%2BRxMUw%2FNsS%2BTBenxbEHMGDLroiGG3tLiXMWvM0uOqPXl6k1PBMMw6zYegvTKEbI4TJVyWVGX7kIY%2BFTMXn6FQI%2B6uJ%2BrGzrCsejHXHXAejaFEhBwRpVNNI66JNcxNl0%2B3RoaDY1%2Br3xIaL3BLcVLVHxUGoJgmHbQdGtn%2FC7F7%2BJUA2gVjmaDlc5YvmyCu5EUvInmpRI1SUtKg5r7X%2FthzEL1s1IX5VhOm09tSktERrDhZPF9DDxLYOUOUlnUDRKYYE0Ja5FPxH%2FVXjDCbx%2BfRBjqkAXQGZEYN2BC0LgAC1bLo2kYDwfnpIX0%2FHCBq89CCWkVbJlt7vdrC78Jtz4T%2Fy8k5R%2BRZOyiu8Us4LO9sjGlGTTQC0zQJerH%2Fs6osNuwKA28LBrmhVfyaXmJpTdnA6TihfVJVR5Hx8rY7%2FxWfMwhw7gmTH11KJD9NB%2B%2BG7HrIhC%2BMfhN8%2BN9pIIEF0zmWIZKZiA1HRn10KxwtZC0HJpGzhRiU%2FxiN&X-Amz-Signature=625690fd46f9fed3d9598fdb698ceb8b1915b61c6150676b685436f753b1faf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTFQI76Y%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T020049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDoXwdLoyyWEyOzYd8Ngq55VMMaD%2FD%2F8To%2Bri3cmfLvsgIhAJdBA6T7T2RAvIhJnM5A%2BS%2F%2FoHppw7AMmkb1TWLT0KEJKv8DCBMQABoMNjM3NDIzMTgzODA1IgwV38aGEWwTf%2FepDjMq3AOcNGCNhRfVw8atms%2B%2BVTI8gUPDVCw5TupoUl9%2BbfqRUgRT3ljmDMVDCJHIIAwhOlr0iSEbb%2FFDAg8eAr5T34luX443Ky2MjceTpi9QCDK7d%2FErGgTmVfmU%2F72kdDdHyyybE86yMBEjqtZKi0odbS%2F7Ijo0RW2rxYB2R9mHH%2FqRqKmjlKZZq0ek2F4qNlUXFxjOZc3exhsB4F4OYdqwMY3KHllQFTjRVKhsAVK5bYndDIFy278fHYkKgNB5UdqTMvMLKWgDP%2By96h8CEUDJ1qAMc0NaRCgQbifKCFexZ%2BmA3RAUoU7bccGxDZSKYs9gDlfGnDKv2L3pUsd6NiMgC8JbUBcLt4AT6ApURv1268%2BIDQb%2BRxMUw%2FNsS%2BTBenxbEHMGDLroiGG3tLiXMWvM0uOqPXl6k1PBMMw6zYegvTKEbI4TJVyWVGX7kIY%2BFTMXn6FQI%2B6uJ%2BrGzrCsejHXHXAejaFEhBwRpVNNI66JNcxNl0%2B3RoaDY1%2Br3xIaL3BLcVLVHxUGoJgmHbQdGtn%2FC7F7%2BJUA2gVjmaDlc5YvmyCu5EUvInmpRI1SUtKg5r7X%2FthzEL1s1IX5VhOm09tSktERrDhZPF9DDxLYOUOUlnUDRKYYE0Ja5FPxH%2FVXjDCbx%2BfRBjqkAXQGZEYN2BC0LgAC1bLo2kYDwfnpIX0%2FHCBq89CCWkVbJlt7vdrC78Jtz4T%2Fy8k5R%2BRZOyiu8Us4LO9sjGlGTTQC0zQJerH%2Fs6osNuwKA28LBrmhVfyaXmJpTdnA6TihfVJVR5Hx8rY7%2FxWfMwhw7gmTH11KJD9NB%2B%2BG7HrIhC%2BMfhN8%2BN9pIIEF0zmWIZKZiA1HRn10KxwtZC0HJpGzhRiU%2FxiN&X-Amz-Signature=8ce3bc338dec719abe1f3258ebe48bdb657112805b35876a912e1447a6dc0478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
