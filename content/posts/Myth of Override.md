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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6U22HOW%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T105452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVmA7YaQ6GdP1rmYmKhKUWojIJ1AZlGjEg3KH48vXWqgIgVtlcKUjsoMkdQ6xBnZAe3K9OcXQdhU31m3GPC3MgJBMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPV1zsZt49HFw6UwYSrcA9t69rU3vktE2rw%2FuKvwgYcfdWRZjVQ%2B8z49o7jqSO5jHDWUBZHosYvzAyYaN%2BaQYuf9bqXjVA3lemNnuO69NcOoBFYsU1uDl2yNaxiHoQ0Ru%2BY4XZwlCrT9CNppw3SRIHDiWfNe8b0O%2B7gMXgu0QvxaQNkCXkf%2FGoZbaZAwHM3YSd1whEGHKEuNxu4TBs5pO%2BmykAxdtd9x2Vx4rZHQNipIJePslfav1axBF%2Bwx4dciMO1t%2FtWS4cxXnnX3bKW%2FjrQMkakKkbwR8jawKy6g2416JJuHAMqi2IHcuwDwUb6d%2F042K1InW59C6OkfXD%2FWfz8FBFBSbqc0GpfXWuLGSIp7DIdhpkdMhNVRavErF153FVWR5D4zlpt1QnFhHIASKNZC5ASzKzio29F1t5%2F7Uo2u3CeUZQ1a56m1Y%2BrLgZCzhoCeZtHqmd3K%2F%2FMCPoz0CcUf0FP1d2FQJOArPBLJVrkw0d1N3lReaudfliKTN6uODzYSuwtiJfIFYrAo8kvzEHNZrchuTNY6I9%2FUG5Fm2a7yf0NPpw04QLteNelUdyfZoXv6Zy8v84XXfm5rS3zc0agDfaUZf9RS07mAQ2d2JLwHXpqs6KhFZrWz0sXve4Ski7vuPq9Y%2Fok%2F%2BcUNMNTpoNAGOqUB7L4O6RHjgikooknQPkz8EyPHvYXoK3BkoWq%2F4de6y0WWi7qwRiJlGH4OZjhyO%2B9EOKrjVDkADfPA5kwqzqUn3TRoBlQWsAHXOIE2ioa8syr%2FK5h7rqlgC%2BKUcZPgoj%2FjoQmEHX6JYI3o6HQ3ySlaDbPU%2BQfMidw5oTLQm9mnGpQz2vXl83RVLk8mIj2H91La9yBvteglJl%2FETwHgHjjNbDUD8dSZ&X-Amz-Signature=96dca3513cdd0f9e21473494919f8612d93265f0dcb7043c643e97c73e09e5cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6U22HOW%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T105452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVmA7YaQ6GdP1rmYmKhKUWojIJ1AZlGjEg3KH48vXWqgIgVtlcKUjsoMkdQ6xBnZAe3K9OcXQdhU31m3GPC3MgJBMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPV1zsZt49HFw6UwYSrcA9t69rU3vktE2rw%2FuKvwgYcfdWRZjVQ%2B8z49o7jqSO5jHDWUBZHosYvzAyYaN%2BaQYuf9bqXjVA3lemNnuO69NcOoBFYsU1uDl2yNaxiHoQ0Ru%2BY4XZwlCrT9CNppw3SRIHDiWfNe8b0O%2B7gMXgu0QvxaQNkCXkf%2FGoZbaZAwHM3YSd1whEGHKEuNxu4TBs5pO%2BmykAxdtd9x2Vx4rZHQNipIJePslfav1axBF%2Bwx4dciMO1t%2FtWS4cxXnnX3bKW%2FjrQMkakKkbwR8jawKy6g2416JJuHAMqi2IHcuwDwUb6d%2F042K1InW59C6OkfXD%2FWfz8FBFBSbqc0GpfXWuLGSIp7DIdhpkdMhNVRavErF153FVWR5D4zlpt1QnFhHIASKNZC5ASzKzio29F1t5%2F7Uo2u3CeUZQ1a56m1Y%2BrLgZCzhoCeZtHqmd3K%2F%2FMCPoz0CcUf0FP1d2FQJOArPBLJVrkw0d1N3lReaudfliKTN6uODzYSuwtiJfIFYrAo8kvzEHNZrchuTNY6I9%2FUG5Fm2a7yf0NPpw04QLteNelUdyfZoXv6Zy8v84XXfm5rS3zc0agDfaUZf9RS07mAQ2d2JLwHXpqs6KhFZrWz0sXve4Ski7vuPq9Y%2Fok%2F%2BcUNMNTpoNAGOqUB7L4O6RHjgikooknQPkz8EyPHvYXoK3BkoWq%2F4de6y0WWi7qwRiJlGH4OZjhyO%2B9EOKrjVDkADfPA5kwqzqUn3TRoBlQWsAHXOIE2ioa8syr%2FK5h7rqlgC%2BKUcZPgoj%2FjoQmEHX6JYI3o6HQ3ySlaDbPU%2BQfMidw5oTLQm9mnGpQz2vXl83RVLk8mIj2H91La9yBvteglJl%2FETwHgHjjNbDUD8dSZ&X-Amz-Signature=6e1f67d23eca1b2bb6b92843ab7dc5b6557968a5dc413105ffcd2a46f2be76f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
