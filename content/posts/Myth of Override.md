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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ULKZHI4%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T223603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC28kzSLGCwcW1s8Fcy8ecoku%2F6nG1EW4FePZbaETt%2FGAIhALIWqIQ44s4TTfhEP0j%2BG4kKTNVciQzEgPXhosQF9768KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzehGtj%2BC8pt9zN3yEq3APJKNl4YlSIvDpwRSRWU9M5QLXxSAgYhbrdd08hVo78ma2SE%2BMlIsd%2BYQes1YRnigFnHqFZio%2BkH0lRDZM8QcGSveZ4OYOkAhbaFqcHsL8jY7f85VLvJRWYWUMeRBI3HtYr0JJXg1FuiH85golONVknOejW%2BnlWygYRVUsQDU%2F0xD0%2B%2BLix8BdLZ2%2BeOKa4uiO%2FQnmnEXY%2FBwVVOcdtAEFLUVv8LbD5dEIANTGDGnvdL7ogbSFWhYDQcP9S9PX3tBRYbBL4eos5fb7ofhRe%2F5nzYLi9mSLdp9GJBlGa1dst%2FICVmdlaCWDcGVJOYgBbkaI82PCB4R7%2FVLK81lEq7BiErGVtkVmK0FLJAfCeZmKAx6mAO1MADHsoMyvfIzGP4vjlXoN8KLEGb4RUNRAWgZX9xQ1ysEG9i6aZPXnQ5cbCwwokE%2B9%2B0QSsMMZROyo1nErLLuXWxCesfcCUb0%2BjObYNoCdLKOWK%2B9kcUk5g1fPuNkP3q2Ls4QA0KgIu0SetJT6RcBsdiwFZRju02Ls5br%2FuoZCwnB90IC47fMJFKMT%2FmpsRLkm%2BwmmVIHbCeu1p56%2BIFBTOo9K5%2BBGRBTEdCI9%2FHlisUBL78SH%2FnB19E5yqBYJDGp9r0jTZFnXGGjC3yaPQBjqkASuZLWqTcz0hbn5Fma9FX0YI%2BNVvelu3lgXVALm3EtyznwhKo4Y9Iybp20xKZ69sInSVkyNUBZf5mP96D61nSic7A6zFdKi9QCUnLONWASW1ztRQKjiTRMLylR8brihYYvlAKzXQ8feAiRT%2FlnDu8Qy9atezUWGjNqCe07Isdqp1I7w%2FQf7WlsnKjUkvfugZGp761sadCo9gx1N0co48J3nMuJU7&X-Amz-Signature=622920e695ac9e62cb9d4737e99435f93781fa0f37ea1259bf91321373585d2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ULKZHI4%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T223603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC28kzSLGCwcW1s8Fcy8ecoku%2F6nG1EW4FePZbaETt%2FGAIhALIWqIQ44s4TTfhEP0j%2BG4kKTNVciQzEgPXhosQF9768KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzehGtj%2BC8pt9zN3yEq3APJKNl4YlSIvDpwRSRWU9M5QLXxSAgYhbrdd08hVo78ma2SE%2BMlIsd%2BYQes1YRnigFnHqFZio%2BkH0lRDZM8QcGSveZ4OYOkAhbaFqcHsL8jY7f85VLvJRWYWUMeRBI3HtYr0JJXg1FuiH85golONVknOejW%2BnlWygYRVUsQDU%2F0xD0%2B%2BLix8BdLZ2%2BeOKa4uiO%2FQnmnEXY%2FBwVVOcdtAEFLUVv8LbD5dEIANTGDGnvdL7ogbSFWhYDQcP9S9PX3tBRYbBL4eos5fb7ofhRe%2F5nzYLi9mSLdp9GJBlGa1dst%2FICVmdlaCWDcGVJOYgBbkaI82PCB4R7%2FVLK81lEq7BiErGVtkVmK0FLJAfCeZmKAx6mAO1MADHsoMyvfIzGP4vjlXoN8KLEGb4RUNRAWgZX9xQ1ysEG9i6aZPXnQ5cbCwwokE%2B9%2B0QSsMMZROyo1nErLLuXWxCesfcCUb0%2BjObYNoCdLKOWK%2B9kcUk5g1fPuNkP3q2Ls4QA0KgIu0SetJT6RcBsdiwFZRju02Ls5br%2FuoZCwnB90IC47fMJFKMT%2FmpsRLkm%2BwmmVIHbCeu1p56%2BIFBTOo9K5%2BBGRBTEdCI9%2FHlisUBL78SH%2FnB19E5yqBYJDGp9r0jTZFnXGGjC3yaPQBjqkASuZLWqTcz0hbn5Fma9FX0YI%2BNVvelu3lgXVALm3EtyznwhKo4Y9Iybp20xKZ69sInSVkyNUBZf5mP96D61nSic7A6zFdKi9QCUnLONWASW1ztRQKjiTRMLylR8brihYYvlAKzXQ8feAiRT%2FlnDu8Qy9atezUWGjNqCe07Isdqp1I7w%2FQf7WlsnKjUkvfugZGp761sadCo9gx1N0co48J3nMuJU7&X-Amz-Signature=42c418c65e30e53279fdc103d6cf97540f74fe085c446675fc754fab031afb2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
