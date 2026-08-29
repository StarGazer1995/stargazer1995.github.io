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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGMZM4S2%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T185850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWN1jTCEyWXDD%2Bzd%2BbQrluuK%2Fb%2BH33Zv4VxdGhdBf2CwIgKax64B21Y4evqv7GneAQPUHovcRInlZAQxby16VZUnIq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDKqJ4AhFvgzbCMMrmircA0uXmIzR39w5lE3U0KId4UBP1y%2FQsnWnM%2BdWcmgmeV7MzDirzgi1flrzmnsr7WVQcnJ4Zwx6kUlwoKOmDirCOsmbDvG%2FKaY9hBsxeaZlQLO56QhNjcLlBXmkF4hBbp6tIvUg2WhopXOkStRnMxjJ%2BKMJOk4NqCEXEOVFJD61nw223NYcMfsj5vhLQM9vPRWCSe62iJJzW4XdSC2TXr2vhdR20SoI6ARr2eFAnLVz4SVfqXln7fk1nDlusYCK4TYOiTSpJ0wClIh3K8hJACPQhTY2cma7xwwCo%2B3xGj3ybyh62ty4IG9oIqmAXX8cGDXA0NcGX1guHjVw90SXe7s%2BqzFe3XcvBqLhvPEq0TWQnDcMkFLXPKH7JZVls%2BtNSGPdt2S6SCLhUehO%2BBawAkArTRRqDNmWhBBA5JLIQjo1syrEEsqmVM%2B%2FXHAvNh3aHdH%2BhbZk%2FdYnMTkEd61Inf%2FsAu9411bJaMQvOWxMYkALp93zqRUOEKX%2B2HAp1xoO4okuGVLACJDnXo%2BvIDcTScplS1JaJERBqYXbbti%2BfPKYL1sAsgWzz8zr4SCtfjS4BMnlmHYLm%2F34Wx%2FJTqFsX9lPbSUXw5swf5a7nmBjJpO9wE8oIbh%2FlwHKx6hG7VZSML%2FHzNQGOqUBZ5vdw%2F4vLUURVolMrQtUVXzLUnNjdkC7%2FRoKICbnyl%2FGvRtYdQ1xtzFkgJa2TtgJ2Jjgi1V08hG0hUXfZLhN0qbKqBt%2FSoN5Em%2BWOnIKw%2B21Yg8eMJvgTcaPrB3RuPs0KqQiOUj670dQjKO6SMoIB5nKQvg8U6ymGyBKvmNrsm152LnCL0hiiislSPkh4QDLysLk1J8zuULm6cq21XjF91I%2FGbj4&X-Amz-Signature=e4df416378526c14c4e5a0e239a76c84ee68eeca0a9b9aa77659e17447f29174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGMZM4S2%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T185850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWN1jTCEyWXDD%2Bzd%2BbQrluuK%2Fb%2BH33Zv4VxdGhdBf2CwIgKax64B21Y4evqv7GneAQPUHovcRInlZAQxby16VZUnIq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDKqJ4AhFvgzbCMMrmircA0uXmIzR39w5lE3U0KId4UBP1y%2FQsnWnM%2BdWcmgmeV7MzDirzgi1flrzmnsr7WVQcnJ4Zwx6kUlwoKOmDirCOsmbDvG%2FKaY9hBsxeaZlQLO56QhNjcLlBXmkF4hBbp6tIvUg2WhopXOkStRnMxjJ%2BKMJOk4NqCEXEOVFJD61nw223NYcMfsj5vhLQM9vPRWCSe62iJJzW4XdSC2TXr2vhdR20SoI6ARr2eFAnLVz4SVfqXln7fk1nDlusYCK4TYOiTSpJ0wClIh3K8hJACPQhTY2cma7xwwCo%2B3xGj3ybyh62ty4IG9oIqmAXX8cGDXA0NcGX1guHjVw90SXe7s%2BqzFe3XcvBqLhvPEq0TWQnDcMkFLXPKH7JZVls%2BtNSGPdt2S6SCLhUehO%2BBawAkArTRRqDNmWhBBA5JLIQjo1syrEEsqmVM%2B%2FXHAvNh3aHdH%2BhbZk%2FdYnMTkEd61Inf%2FsAu9411bJaMQvOWxMYkALp93zqRUOEKX%2B2HAp1xoO4okuGVLACJDnXo%2BvIDcTScplS1JaJERBqYXbbti%2BfPKYL1sAsgWzz8zr4SCtfjS4BMnlmHYLm%2F34Wx%2FJTqFsX9lPbSUXw5swf5a7nmBjJpO9wE8oIbh%2FlwHKx6hG7VZSML%2FHzNQGOqUBZ5vdw%2F4vLUURVolMrQtUVXzLUnNjdkC7%2FRoKICbnyl%2FGvRtYdQ1xtzFkgJa2TtgJ2Jjgi1V08hG0hUXfZLhN0qbKqBt%2FSoN5Em%2BWOnIKw%2B21Yg8eMJvgTcaPrB3RuPs0KqQiOUj670dQjKO6SMoIB5nKQvg8U6ymGyBKvmNrsm152LnCL0hiiislSPkh4QDLysLk1J8zuULm6cq21XjF91I%2FGbj4&X-Amz-Signature=9d71ce65a9444232c60ff918044bbab9a90b57d00865fbcc3981fc3a72b52545&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
