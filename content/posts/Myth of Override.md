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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSWEDV4D%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T203503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIE1a1leY0kny6iDs36uSvwZMQcIzx3OtDVOqyPVzfAJCAiEAvnXsLqIkPkfoZospoall8eJMqYz7paKfYTG08Kjr0G8qiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZYWNc1vGb1ZSlKoCrcA5D%2B0I0YEREriSm0hPpWCXfUrJW0T%2BoVGrdLIZuIQX%2BYMrp%2FQEXYDNAbZUAEiwVITFgvs%2BcuU2uGq9%2By1WGydCZmvDVBWGEQXQWJNu42JlQAlIXF0CzHJsyMDkS9xvbHdkgDHDt5XdWI6K3p6%2F6EW7lCT%2BhUxK0%2FJtkjc47ljMXP6pMBAOlepFy%2BSOSVMeBbLmxCGzPS5VuODzdLfXF9jDTOe8P1STpTZ4QaQlMAd7G8XWXCxYWZHej8CIKufZlbnmsy84cVbk9NCDmCJlClDg3zggR%2BaBNNinctd9gSECTWrpjuSte4ml4ArO%2BXxh2fT41vbXok35VbQHxmUzC%2B0p77WaYKx2krrc48kt5woXz7LF5YpNDRM%2BtAyCeA9kfAbH2mg%2FWWwOhtEjJIu8zDXd0Ir7morlSEQUIoQoSr7pK6IDEixp4K8mtWEJKEGyqp4xzFdN6ThAU6%2FOjxCHIBsq%2Bg117Z63FH8n86m0tUMe11xA2BqTF8P0giSgzyPJBGNqqsseF4WCIQsEExMcEm%2F8LcTd5xiWkKs8ATlXVxYX45eEAcopaOwOczukWgD07vB5hnHGZnwF%2BX8r5PhOcPuTItfr75DBYLb52RSGTGwk7cuSW1RE77FzKjeeEWMJTeitYGOqUBGSY8766cMO81T8Vmk%2FOGSrr6LRC6RrwMuGO%2BpxPhW89Y6GzbN1mZrrTWGJl2PccE%2FUcn%2BlIMbUIl2rAbzOwop8FlYuFZvay1mRHSxdw3qC%2BK9YVmt3zU%2B7lAjtZcoWyJsUW%2BuOOOappYtDRO0Dy0upvUswcIMTAuPk%2FR0NED3wAD1Nl6ABW3WzdVuaf2t2GXLKhpitPXyl9odZw1%2F89ABJ5pG9kR&X-Amz-Signature=61532f5b91956c2915ccc2afbf33ac98a60e2a44a5d0deced66a727ab905aa6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSWEDV4D%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T203503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIE1a1leY0kny6iDs36uSvwZMQcIzx3OtDVOqyPVzfAJCAiEAvnXsLqIkPkfoZospoall8eJMqYz7paKfYTG08Kjr0G8qiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZYWNc1vGb1ZSlKoCrcA5D%2B0I0YEREriSm0hPpWCXfUrJW0T%2BoVGrdLIZuIQX%2BYMrp%2FQEXYDNAbZUAEiwVITFgvs%2BcuU2uGq9%2By1WGydCZmvDVBWGEQXQWJNu42JlQAlIXF0CzHJsyMDkS9xvbHdkgDHDt5XdWI6K3p6%2F6EW7lCT%2BhUxK0%2FJtkjc47ljMXP6pMBAOlepFy%2BSOSVMeBbLmxCGzPS5VuODzdLfXF9jDTOe8P1STpTZ4QaQlMAd7G8XWXCxYWZHej8CIKufZlbnmsy84cVbk9NCDmCJlClDg3zggR%2BaBNNinctd9gSECTWrpjuSte4ml4ArO%2BXxh2fT41vbXok35VbQHxmUzC%2B0p77WaYKx2krrc48kt5woXz7LF5YpNDRM%2BtAyCeA9kfAbH2mg%2FWWwOhtEjJIu8zDXd0Ir7morlSEQUIoQoSr7pK6IDEixp4K8mtWEJKEGyqp4xzFdN6ThAU6%2FOjxCHIBsq%2Bg117Z63FH8n86m0tUMe11xA2BqTF8P0giSgzyPJBGNqqsseF4WCIQsEExMcEm%2F8LcTd5xiWkKs8ATlXVxYX45eEAcopaOwOczukWgD07vB5hnHGZnwF%2BX8r5PhOcPuTItfr75DBYLb52RSGTGwk7cuSW1RE77FzKjeeEWMJTeitYGOqUBGSY8766cMO81T8Vmk%2FOGSrr6LRC6RrwMuGO%2BpxPhW89Y6GzbN1mZrrTWGJl2PccE%2FUcn%2BlIMbUIl2rAbzOwop8FlYuFZvay1mRHSxdw3qC%2BK9YVmt3zU%2B7lAjtZcoWyJsUW%2BuOOOappYtDRO0Dy0upvUswcIMTAuPk%2FR0NED3wAD1Nl6ABW3WzdVuaf2t2GXLKhpitPXyl9odZw1%2F89ABJ5pG9kR&X-Amz-Signature=6fb627fbf769cee2826ab7895561a16391e77ec1aab98a614e9bbb4d504e12b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
