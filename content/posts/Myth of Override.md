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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRCZ26RU%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T101714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNJ9b5Ksc%2F2APfG%2B1QqTHzZOoy0oNgZeTPznNov%2BZ49gIhAJk%2B%2B1dOUXNQU1BTUg28xFjNQi5u3eFWvUG1ka1kiQCeKv8DCHIQABoMNjM3NDIzMTgzODA1IgwsYI4voL4Ba%2FJbADkq3AOWLgPz7QPpNu1hJ2RlrdlH6sWGf03bmkqfyLFFylHVd60Zgo5g58pkIGRe6F%2BRydcIwshp3dKfHaSrMelhyN7RpiNMS46oWwwom0cpkPExz6hmnRpT31xeFf6mqHwPApgMum0dNPZROqlXGoBQd8BPtrSyvToVMWjKiXbansyaYRbYXlef1fGe%2BCNu2Jg86HjCbrWRTKMH9%2BMb64I2divPoptWZhwsNhbV%2FzZhX%2FBlqlZHAlZCv%2FGudy%2BXm2TbLfHG%2Fw2cpAQ5WM2Qg48I4u5Zf%2B3yl2ikQZIWZR%2FMtDtZJAEfJ6hH4%2F5QMs84YzoEFJmixm0O3znEKpX%2Fw94JkdW%2Fai568GTyZqz67N05niQXwHugC92nu4NuOp6BDArfA%2FqpVOuIgiEWR7BCXiBrroR3SWfxa5KKYSt5YPVjrIDIwrpSMTI7%2BwGjKLo5Ly5ZKz161ngeDjrkKlEiLJX9tkrNPUN5xivbF5IAICbhnaOXDktTOfPY692sYYvgRpNbUzhbJLZjt%2FrkazzOYG0nBxfw7KTXFLO2HoVZdFcIgXnudReoS81SqQ2aI%2BRsVAsGSGkAbu9qoFZK39pQdb9L0QeM6b3yLWdHed%2BDlkFkYdlC70V8GxmkJ58cTIHogjCK55XUBjqkAfqAJKLVJzLW5IP%2FCmS06oyRpikYy%2FATAszQESYq3bv%2FTzkZuDdCm1rRx0fLdwLrg%2Fq5jDOf1vUiPJfee28lp0%2BXWFnFeG4SvS9V6F%2B805VwhbdNrnYsXZiz7S8mzBkIbHXOy2Ee%2BU8IYf5kD5vWJtF0bGcD0H4o%2BLvTzzt2QZdJ%2Bxmh8tiZB%2Bmr4XCOdhKg7Vyy3SxToETsY8WKHHToquCVz%2FS3&X-Amz-Signature=445b107dbcfd7c1a05875bd88f57710ace3902071eefde88fed8cfbe0284e49e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRCZ26RU%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T101714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNJ9b5Ksc%2F2APfG%2B1QqTHzZOoy0oNgZeTPznNov%2BZ49gIhAJk%2B%2B1dOUXNQU1BTUg28xFjNQi5u3eFWvUG1ka1kiQCeKv8DCHIQABoMNjM3NDIzMTgzODA1IgwsYI4voL4Ba%2FJbADkq3AOWLgPz7QPpNu1hJ2RlrdlH6sWGf03bmkqfyLFFylHVd60Zgo5g58pkIGRe6F%2BRydcIwshp3dKfHaSrMelhyN7RpiNMS46oWwwom0cpkPExz6hmnRpT31xeFf6mqHwPApgMum0dNPZROqlXGoBQd8BPtrSyvToVMWjKiXbansyaYRbYXlef1fGe%2BCNu2Jg86HjCbrWRTKMH9%2BMb64I2divPoptWZhwsNhbV%2FzZhX%2FBlqlZHAlZCv%2FGudy%2BXm2TbLfHG%2Fw2cpAQ5WM2Qg48I4u5Zf%2B3yl2ikQZIWZR%2FMtDtZJAEfJ6hH4%2F5QMs84YzoEFJmixm0O3znEKpX%2Fw94JkdW%2Fai568GTyZqz67N05niQXwHugC92nu4NuOp6BDArfA%2FqpVOuIgiEWR7BCXiBrroR3SWfxa5KKYSt5YPVjrIDIwrpSMTI7%2BwGjKLo5Ly5ZKz161ngeDjrkKlEiLJX9tkrNPUN5xivbF5IAICbhnaOXDktTOfPY692sYYvgRpNbUzhbJLZjt%2FrkazzOYG0nBxfw7KTXFLO2HoVZdFcIgXnudReoS81SqQ2aI%2BRsVAsGSGkAbu9qoFZK39pQdb9L0QeM6b3yLWdHed%2BDlkFkYdlC70V8GxmkJ58cTIHogjCK55XUBjqkAfqAJKLVJzLW5IP%2FCmS06oyRpikYy%2FATAszQESYq3bv%2FTzkZuDdCm1rRx0fLdwLrg%2Fq5jDOf1vUiPJfee28lp0%2BXWFnFeG4SvS9V6F%2B805VwhbdNrnYsXZiz7S8mzBkIbHXOy2Ee%2BU8IYf5kD5vWJtF0bGcD0H4o%2BLvTzzt2QZdJ%2Bxmh8tiZB%2Bmr4XCOdhKg7Vyy3SxToETsY8WKHHToquCVz%2FS3&X-Amz-Signature=f5f299b261fa2ba312ca8567404d9ba5dbb8847bc6fde5f7241302604ca4a6a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
