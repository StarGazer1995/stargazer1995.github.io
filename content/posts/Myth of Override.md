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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRVI567K%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T164440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCh7dmoWX0Z8abhfjH%2Ba%2Fi9X7Rut6aQ1knwtTaQt3VnUwIgc0ATy4QQrTJfnRitVhMfEH7RAsSTcJ%2F88iBD64Nm%2FxgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNV%2F0%2BnRr4V3%2BapLYyrcA9YR%2FhWJfsZbXJNljki1R0fIffMyJ9AGSh3G5Vkn791glY1BWS%2BuQT6PX1Z9X7TUvuO0IjV9TgQujdA3gWtmaUM3CHkH0d7Fi2Waqzxr3fum4x9oWNqD0Z0FIufOkQ%2BEtCC4Vz7yMmtIU8Tp8IqNj4xc5j69Xd6TOc3qgG7oqRg6yynuJ60RBmWtKrbAMI7vzJgDt58GPy%2Fj7vSzg3RtHiBZwsHWLl9QCjsV0Wz7foZqQD3M%2BPz4wfqWBSRCuaM2F9qECFLnMNBzQl3EGxTMx3rVw%2Fm%2FtcUzsRXwSOEa3xMp24HIVpdX7jHUtXqjFM%2FGndzHjOw8c78qRAqRFWY2yphFAEWH6UsQpq2H%2FEnl4BKUBvLGfmz%2BSKUe0svjATdsfxAu%2FoZhdlv0pxjMuiNO6oLKexMQ1VFvdtUb1AHhoxEJSFASHEjTCAqGw%2BuH5fhPR%2FwgBOoFac7tUUrVu3MlRqZCDE0MuIUFIJGDUy%2B2rZ98RoExAhsQ9KxBHccEyeurhHPGUVl45X%2FlViesCTTHmp8BIRIbpNLKwdJi6%2FBHW0%2Fzp8UmaDl2uB1ZrAC5l%2Bn7sAVm2y1I9Fq%2Bpvv%2Fad5ucSJPEzn8UBhiriVzT4ctxuihE%2Fm0ltdvP%2FZx3Lk9MOW18tMGOqUBI7Wo0vipwkosiHa6P%2FKTzsTxho8CYJ4Prw3QW8xygdlvmw1Z9IKNO%2ByiBEKFJppFvKf29Oaw8K59P4df9krTmzpwGwcxqO6c1hutXFL3GNZzyB%2BdLItsTW%2BS1GEtU6UmpgGCyEwewhNsbJ1nwsoTbWa1ClZWtXJeSFONGe0bR2DVuQVqKr0zUfH6Oj0VXW0OLSLZ2cAuuAGpMj0TlsRcV%2BPHdyvT&X-Amz-Signature=2d3a16eea4aa93bb435cfa2537e5a77bdbc6f1a2f8934d175ee16c5ae7915ec9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRVI567K%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T164440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCh7dmoWX0Z8abhfjH%2Ba%2Fi9X7Rut6aQ1knwtTaQt3VnUwIgc0ATy4QQrTJfnRitVhMfEH7RAsSTcJ%2F88iBD64Nm%2FxgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNV%2F0%2BnRr4V3%2BapLYyrcA9YR%2FhWJfsZbXJNljki1R0fIffMyJ9AGSh3G5Vkn791glY1BWS%2BuQT6PX1Z9X7TUvuO0IjV9TgQujdA3gWtmaUM3CHkH0d7Fi2Waqzxr3fum4x9oWNqD0Z0FIufOkQ%2BEtCC4Vz7yMmtIU8Tp8IqNj4xc5j69Xd6TOc3qgG7oqRg6yynuJ60RBmWtKrbAMI7vzJgDt58GPy%2Fj7vSzg3RtHiBZwsHWLl9QCjsV0Wz7foZqQD3M%2BPz4wfqWBSRCuaM2F9qECFLnMNBzQl3EGxTMx3rVw%2Fm%2FtcUzsRXwSOEa3xMp24HIVpdX7jHUtXqjFM%2FGndzHjOw8c78qRAqRFWY2yphFAEWH6UsQpq2H%2FEnl4BKUBvLGfmz%2BSKUe0svjATdsfxAu%2FoZhdlv0pxjMuiNO6oLKexMQ1VFvdtUb1AHhoxEJSFASHEjTCAqGw%2BuH5fhPR%2FwgBOoFac7tUUrVu3MlRqZCDE0MuIUFIJGDUy%2B2rZ98RoExAhsQ9KxBHccEyeurhHPGUVl45X%2FlViesCTTHmp8BIRIbpNLKwdJi6%2FBHW0%2Fzp8UmaDl2uB1ZrAC5l%2Bn7sAVm2y1I9Fq%2Bpvv%2Fad5ucSJPEzn8UBhiriVzT4ctxuihE%2Fm0ltdvP%2FZx3Lk9MOW18tMGOqUBI7Wo0vipwkosiHa6P%2FKTzsTxho8CYJ4Prw3QW8xygdlvmw1Z9IKNO%2ByiBEKFJppFvKf29Oaw8K59P4df9krTmzpwGwcxqO6c1hutXFL3GNZzyB%2BdLItsTW%2BS1GEtU6UmpgGCyEwewhNsbJ1nwsoTbWa1ClZWtXJeSFONGe0bR2DVuQVqKr0zUfH6Oj0VXW0OLSLZ2cAuuAGpMj0TlsRcV%2BPHdyvT&X-Amz-Signature=eb0966cf26b6d8c5ea0060b1518d7c6fe4a01f754dc35d2341f930b9e93b191c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
