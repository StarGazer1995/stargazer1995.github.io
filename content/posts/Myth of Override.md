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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GRM6DFN%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T235252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOnJPw6Ot7XRKNkKjcotrTdJ6Bl1xTDy4tG61%2F%2BPuODgIgBMiIMvOZ96AUFAJTQtc%2ByB0Tq%2FMO8O%2BohBTFBFPPg4MqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbR4CGIKgaeU%2FWGdCrcAwQ7TK9js96JXZdsz0MdgRqPoROUORMOMB9G0E0AgiSCPM6PVgsMmwr2izhmx6zVh3yr8zbNjJLbr7p5bg7%2B33pkfZbkWz21sR8hHQUmsBjwC0MzpfqpgH1K%2FpCL%2FkdXmTq6uPuI4loB65ckZ7w3FlTMmnnItWWTiDajh4M8tZ8%2BWwFkEbWL%2F4BXF6O8YORdHPR0sUlLZGvRwdEsIagCC3E8TIw1jzNspU4sdoVqRDE2Befxojuv98HtBqVm8zwfmPwQufxZUlr9PYOH8YrfdsEokmXX0MoJow82u8JyMrc0%2BilLdXLuDCYRhVmqi8jwXZfYbCQ6EC2AsmJbS50iKSZeN7GTDDqJFNa6EFehHjKua%2Fwifg2EEbXJDsFLr2MRQLvK8FsNq7j46qoC9ML1JnvO2ToxXK8Kz49ZxeNatKCvk6KfS44inmxsnGGx6Ov6HDyr795sHytsW0Rvp%2BXpg9sFOR4Roix46ofFZoyJPdiMF4cQRGyaM20Y8HEALHnpRKnFMCSL5CnqwhLyq9BLq9BXnqcDGOIcuZMJh0y9sUirRf%2FjAZJmvy%2F5QMHHnP1WsnV4hvRpJKSS8JKElFUQ%2F7YayBRyKkl0kqOqtwpQb%2F%2FyCJhrya%2BS4dDs3z%2FVMPvo6M8GOqUBSob6LEL6dXbaOQywdqdFFU0HMqlolsTu5MfPXpu11SJiCKg9B68Gji72BSTa%2F5Fgfz97AVO2OtmquKjsx5W5ljeI%2FYaJyle319eKO2o23d3D6Pxsuub0G7%2Fk7OrZ8U4%2FViLuXsr7AyAXXOPNHpgoM3QBDSqzLBbu9DiIvNTPksKfbIouKrZSGSL5UvhR56jUEqXzNyUHR53msyr1QFDHKwQglGf4&X-Amz-Signature=05013a86b775ff86c026ccb2cff59fafbcd22d429d016e4b18c203a2feb1ed0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GRM6DFN%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T235252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOnJPw6Ot7XRKNkKjcotrTdJ6Bl1xTDy4tG61%2F%2BPuODgIgBMiIMvOZ96AUFAJTQtc%2ByB0Tq%2FMO8O%2BohBTFBFPPg4MqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIbR4CGIKgaeU%2FWGdCrcAwQ7TK9js96JXZdsz0MdgRqPoROUORMOMB9G0E0AgiSCPM6PVgsMmwr2izhmx6zVh3yr8zbNjJLbr7p5bg7%2B33pkfZbkWz21sR8hHQUmsBjwC0MzpfqpgH1K%2FpCL%2FkdXmTq6uPuI4loB65ckZ7w3FlTMmnnItWWTiDajh4M8tZ8%2BWwFkEbWL%2F4BXF6O8YORdHPR0sUlLZGvRwdEsIagCC3E8TIw1jzNspU4sdoVqRDE2Befxojuv98HtBqVm8zwfmPwQufxZUlr9PYOH8YrfdsEokmXX0MoJow82u8JyMrc0%2BilLdXLuDCYRhVmqi8jwXZfYbCQ6EC2AsmJbS50iKSZeN7GTDDqJFNa6EFehHjKua%2Fwifg2EEbXJDsFLr2MRQLvK8FsNq7j46qoC9ML1JnvO2ToxXK8Kz49ZxeNatKCvk6KfS44inmxsnGGx6Ov6HDyr795sHytsW0Rvp%2BXpg9sFOR4Roix46ofFZoyJPdiMF4cQRGyaM20Y8HEALHnpRKnFMCSL5CnqwhLyq9BLq9BXnqcDGOIcuZMJh0y9sUirRf%2FjAZJmvy%2F5QMHHnP1WsnV4hvRpJKSS8JKElFUQ%2F7YayBRyKkl0kqOqtwpQb%2F%2FyCJhrya%2BS4dDs3z%2FVMPvo6M8GOqUBSob6LEL6dXbaOQywdqdFFU0HMqlolsTu5MfPXpu11SJiCKg9B68Gji72BSTa%2F5Fgfz97AVO2OtmquKjsx5W5ljeI%2FYaJyle319eKO2o23d3D6Pxsuub0G7%2Fk7OrZ8U4%2FViLuXsr7AyAXXOPNHpgoM3QBDSqzLBbu9DiIvNTPksKfbIouKrZSGSL5UvhR56jUEqXzNyUHR53msyr1QFDHKwQglGf4&X-Amz-Signature=b1c268539f3184e887b02f5c529e4cddc1dd3d6ca45725982789dc05cf65a5ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
