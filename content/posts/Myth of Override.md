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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TCWSSI3%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T003329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDgP%2FJcaQnEtV%2BqhS3n%2F5c%2F4hUOcc0oGDfkSyD0MOU1kQIgeomzhFghKw26%2BrD2yZBi%2FPEtYBcVzuu9cICk8dmhBjEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxs%2FaV4obOmjjR78SrcA45Pi6BKhaRp7n9iAje2r1uGlH1F23fe4zlW63w9tV97ZkGDTXATd1THCwgNxl9mso3bYAdlOK3XkgZ8PV%2BCFtHT3HR6Sa0gnFyC1idQkKAnm5yF2NmUgisd31qnDF5SAkwkbpoSE1ljTENwdITlBqgI%2BFJOM2C%2FJBzrJzy5cBK%2FOUW5Az%2BrPAThQkUdPvH7%2BLeeCXQdIQT%2BwkeRTGCrXpBmSp8j%2BiV5i6kHp7W8xUuFQj7aFXJa1A2S67A6FXjRftTxBNbazX4QCKl5EBudotY%2FIkN5oKMLtzzfD0%2Fm2%2ByKmhL67AEbIa4dkkHdNgsW5YnPdqACXXZYPGgnOUDSNlhDeGGv%2BhUZR5RIP3J6BKI6aw%2B%2BA8JoVP9JZWVum7ox2HT2AV3i2oFTqRuAqR0fMlDoUqsRIkg4NQVlW6gYU3EVd3tm%2FkY4TOcFmD526OX1mNdTlv1ILMPo8A4DhqmsqGMeu0X0cqbLL%2B0jFbrueU5oZdRI5KpTQ8eKiXkUQx1En7f%2FvUzvagk53Cu0eKp4PKiNco5RjhFOWBc9xth7L9kbieJ7oivzS7RckpWmjW%2BPBkdKmxH5H5yb7dzzlkCPjAhGLsGgKsy8w7wvSGMdqBfqe8JEkmGjxcCvdYKAMJ2QrtQGOqUBDrdTAAFyNS5y7Iz3hIQunA5kpRllwr0F4KR%2F5Oj2FtB%2Bh8cvnLcUDL9IVVF2hEjdAlV%2B8nPBFyilej7bLw981%2Fa81%2B2qL1zIM8NT43zIsZmEws2tvCTuJfWGJYFxmTpSXvsQwrCWeHBhPU8jkOJ0atnohoL6OA4L1WGGql2vNt9z3grIPRtWVimM9n3FS1uR2wbJvI06k7LyA%2BZvrTLZ2ssRpOJd&X-Amz-Signature=508eb4207526dee27654a6845cf85d8641c9feb91c14d800fae32217b95c2e43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TCWSSI3%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T003329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDgP%2FJcaQnEtV%2BqhS3n%2F5c%2F4hUOcc0oGDfkSyD0MOU1kQIgeomzhFghKw26%2BrD2yZBi%2FPEtYBcVzuu9cICk8dmhBjEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDxs%2FaV4obOmjjR78SrcA45Pi6BKhaRp7n9iAje2r1uGlH1F23fe4zlW63w9tV97ZkGDTXATd1THCwgNxl9mso3bYAdlOK3XkgZ8PV%2BCFtHT3HR6Sa0gnFyC1idQkKAnm5yF2NmUgisd31qnDF5SAkwkbpoSE1ljTENwdITlBqgI%2BFJOM2C%2FJBzrJzy5cBK%2FOUW5Az%2BrPAThQkUdPvH7%2BLeeCXQdIQT%2BwkeRTGCrXpBmSp8j%2BiV5i6kHp7W8xUuFQj7aFXJa1A2S67A6FXjRftTxBNbazX4QCKl5EBudotY%2FIkN5oKMLtzzfD0%2Fm2%2ByKmhL67AEbIa4dkkHdNgsW5YnPdqACXXZYPGgnOUDSNlhDeGGv%2BhUZR5RIP3J6BKI6aw%2B%2BA8JoVP9JZWVum7ox2HT2AV3i2oFTqRuAqR0fMlDoUqsRIkg4NQVlW6gYU3EVd3tm%2FkY4TOcFmD526OX1mNdTlv1ILMPo8A4DhqmsqGMeu0X0cqbLL%2B0jFbrueU5oZdRI5KpTQ8eKiXkUQx1En7f%2FvUzvagk53Cu0eKp4PKiNco5RjhFOWBc9xth7L9kbieJ7oivzS7RckpWmjW%2BPBkdKmxH5H5yb7dzzlkCPjAhGLsGgKsy8w7wvSGMdqBfqe8JEkmGjxcCvdYKAMJ2QrtQGOqUBDrdTAAFyNS5y7Iz3hIQunA5kpRllwr0F4KR%2F5Oj2FtB%2Bh8cvnLcUDL9IVVF2hEjdAlV%2B8nPBFyilej7bLw981%2Fa81%2B2qL1zIM8NT43zIsZmEws2tvCTuJfWGJYFxmTpSXvsQwrCWeHBhPU8jkOJ0atnohoL6OA4L1WGGql2vNt9z3grIPRtWVimM9n3FS1uR2wbJvI06k7LyA%2BZvrTLZ2ssRpOJd&X-Amz-Signature=b0fb16a401699c75ed5dd36e32a6d4971f82cdbd36c5512ab80d4ffdc0462232&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
