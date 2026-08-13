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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQXDB6H%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T202853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCIc2pBhZvKmhQdUGKhrNVx1bDiqm77qoedNuZKbn7OwwIhAOJ%2BS9oK2Fki5k9e0jsHrvwdBXp9R4uZADTqvV7O%2F8OCKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMDE0efUUN1V5eVaMq3AMKxhwXEZmE%2FwwI9lpycKssBeyZNRiZzwemoKQ0H7DUlrOCt6NvsYPMdhM%2Bs6eUf6oibCp6Rp%2FXjaPNReK%2FNK%2FS9eAqctlHURnd9nSJrRiTJofg1icmAFry0hJcx0%2B%2BU8Gh4kiE0hfPmqehkeyu8%2B60ASyCp4K7ZWrrWvRk11WvrklP11i%2B5CcpYv0yg4nitKlxL%2FdhY3RYfBEalN0Eg52yM44EF8IMuhw672SfbCu0rrjhUrrGm3teh9XLQTlXvC16v9VeMyytYKPeIXENBDJZXXbYUlgnqLd%2FkJFN4DYa6RMjhJE9FHmM1k1jc5z71fn4cqisJ464d51quuwNoNqwrh3ID%2BpXeL3caa2nNpx%2F7b1A%2FmiB1hE1TV9leFWhnkkkag3C66fC%2BHMkiNnVJHzIfXj8BaayZfxlew6FcLIoYSClIzDdWQQAcwjdCvLzexEUHkF9UrrFZ6QdT%2FqSccFGhlyUn%2F7ysGGnl8RV%2FZ0XvSKs6CyTsr1%2FbBGZollzy%2BQfGXrJED2C%2FeFcHmE9DvOMFA9GlhVEY9B5bMUuJiATXIIos9qU6u1S1VJoQaXopjC8K5nk3TUHsEZpuHep2KWw8pUWB3G5RQjwON4mYPqwHUF8xADKWDfIE%2FtHlTCoofjTBjqkAXyivatR6%2F7bVF0q45ddD623SW5vbN9cgPS2TvaLsepmn5vc%2F9ROWxIe3BwgtBkt1vxteKMUOdkszLRByAA0tO%2BTfiEHq5TCDtK%2FOCa%2FsExN%2Bjadq5g5HTO9Wwqb6NLjiAGYaCISI12s1hmVJETz9wa5ZFw71GpT3P8f9rUVviUo%2F5ZpQdLyulRSWoflg2b3Pt9WZ00JHdZER%2B0NjD5GhY4pQYmc&X-Amz-Signature=d768d234768fbd2add3ba53268c72fc3c4554b8705c5d9547204f81857978a7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQXDB6H%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T202853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCIc2pBhZvKmhQdUGKhrNVx1bDiqm77qoedNuZKbn7OwwIhAOJ%2BS9oK2Fki5k9e0jsHrvwdBXp9R4uZADTqvV7O%2F8OCKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMDE0efUUN1V5eVaMq3AMKxhwXEZmE%2FwwI9lpycKssBeyZNRiZzwemoKQ0H7DUlrOCt6NvsYPMdhM%2Bs6eUf6oibCp6Rp%2FXjaPNReK%2FNK%2FS9eAqctlHURnd9nSJrRiTJofg1icmAFry0hJcx0%2B%2BU8Gh4kiE0hfPmqehkeyu8%2B60ASyCp4K7ZWrrWvRk11WvrklP11i%2B5CcpYv0yg4nitKlxL%2FdhY3RYfBEalN0Eg52yM44EF8IMuhw672SfbCu0rrjhUrrGm3teh9XLQTlXvC16v9VeMyytYKPeIXENBDJZXXbYUlgnqLd%2FkJFN4DYa6RMjhJE9FHmM1k1jc5z71fn4cqisJ464d51quuwNoNqwrh3ID%2BpXeL3caa2nNpx%2F7b1A%2FmiB1hE1TV9leFWhnkkkag3C66fC%2BHMkiNnVJHzIfXj8BaayZfxlew6FcLIoYSClIzDdWQQAcwjdCvLzexEUHkF9UrrFZ6QdT%2FqSccFGhlyUn%2F7ysGGnl8RV%2FZ0XvSKs6CyTsr1%2FbBGZollzy%2BQfGXrJED2C%2FeFcHmE9DvOMFA9GlhVEY9B5bMUuJiATXIIos9qU6u1S1VJoQaXopjC8K5nk3TUHsEZpuHep2KWw8pUWB3G5RQjwON4mYPqwHUF8xADKWDfIE%2FtHlTCoofjTBjqkAXyivatR6%2F7bVF0q45ddD623SW5vbN9cgPS2TvaLsepmn5vc%2F9ROWxIe3BwgtBkt1vxteKMUOdkszLRByAA0tO%2BTfiEHq5TCDtK%2FOCa%2FsExN%2Bjadq5g5HTO9Wwqb6NLjiAGYaCISI12s1hmVJETz9wa5ZFw71GpT3P8f9rUVviUo%2F5ZpQdLyulRSWoflg2b3Pt9WZ00JHdZER%2B0NjD5GhY4pQYmc&X-Amz-Signature=12985d6786c1e6ec169e6f4249be0ee53a320aa5adfc57f45ccf0257d58df2b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
