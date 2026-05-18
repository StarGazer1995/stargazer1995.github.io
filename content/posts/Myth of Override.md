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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMDJNA4C%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T145202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXiP4E%2BBpdbHmHwg9Gqzv4qHvnA8BV5%2BUWxVtw2OnraAiEAhsJrgB6WP7o3JOuEZzLpcUupD4t6L72SBnoxRnV7a1EqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRCB8O4eLmpZ%2FOkoyrcAzv%2BRugi53cC5VHOJcmKo3O0T2Pog2RaiK0DeKEDcYBKqrBHULHDO5jVgVhFWQ%2FVP78t3gAtqBNZWRPC%2BT8UYd6823Vp6W6trdDLfgHV%2Bxb8PuX2pdPnGkvfKI9TdgqFTRuuEGIWqDvX4qW4sHzPEkybhoCf9FXsk7CU76PI2afxur4t2M4jFHM168qQmIwRFe7SVLEstoKkHY%2Fn1iyfd%2Fu%2FNIoRHYb7Gpbd1sIeWYdChc5xfitciVxmL30op5j3xxhYyPvyf3Wz4YL1I5p4lh9lMQmW4cFMtDG%2BoHhKsSx3E5R5TqkguRm2A7VlHnBS3FlCcxKzB6fijaj%2FUd97488Iia%2Fm9ULoFGbFjw05J1e3NbXktKX4n3bUlbW6g%2FLMvsf0FSU8E4FdCueQtfFVFCaMtiuD50z7e7goFEXHgymYrW716dA5bolBbNAjMaswOROyYEmHdkud6QDe0YKgstUitibo91CxIbCpM5T%2BLQ8fGnfXM82f990bxbcIGONi12b%2Bni1dr9ocerHP9Wi%2BOasm8nLBISEYNaGQfPlJWxsOrKNkziaCn1R%2BPJF7dMM9npi54ggWPqPIIafM7lnn%2B96DhmCztqGcdywuk389tGRsCWsn6ULSCsN0yVzpMPCrrNAGOqUBy0g2T7s7ekA5Xa4Ntf72mE2TPI7Vdz2RBYvEcsjtAZogGWSvZ6ov%2FwSmwNqpOZCx2rj60VaZ3V823UXfDZdamV40BfCY8vfjGMdJhP6MPx35H2LaAi4kYnWj%2FzdIUp%2BGlm92XNmEJVvZ4uOilvkoJxxZ%2FcPj2KTWl7Vc4zvUxP9qarlTdDpgGEonTINPNLUeExEuQCIc3bAMSTLDrf%2F0YJfvZI3V&X-Amz-Signature=c7bd58291d2e0fbb49640622b5644609b22190103d8207bf14ff4c051f5bc263&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMDJNA4C%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T145202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXiP4E%2BBpdbHmHwg9Gqzv4qHvnA8BV5%2BUWxVtw2OnraAiEAhsJrgB6WP7o3JOuEZzLpcUupD4t6L72SBnoxRnV7a1EqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRCB8O4eLmpZ%2FOkoyrcAzv%2BRugi53cC5VHOJcmKo3O0T2Pog2RaiK0DeKEDcYBKqrBHULHDO5jVgVhFWQ%2FVP78t3gAtqBNZWRPC%2BT8UYd6823Vp6W6trdDLfgHV%2Bxb8PuX2pdPnGkvfKI9TdgqFTRuuEGIWqDvX4qW4sHzPEkybhoCf9FXsk7CU76PI2afxur4t2M4jFHM168qQmIwRFe7SVLEstoKkHY%2Fn1iyfd%2Fu%2FNIoRHYb7Gpbd1sIeWYdChc5xfitciVxmL30op5j3xxhYyPvyf3Wz4YL1I5p4lh9lMQmW4cFMtDG%2BoHhKsSx3E5R5TqkguRm2A7VlHnBS3FlCcxKzB6fijaj%2FUd97488Iia%2Fm9ULoFGbFjw05J1e3NbXktKX4n3bUlbW6g%2FLMvsf0FSU8E4FdCueQtfFVFCaMtiuD50z7e7goFEXHgymYrW716dA5bolBbNAjMaswOROyYEmHdkud6QDe0YKgstUitibo91CxIbCpM5T%2BLQ8fGnfXM82f990bxbcIGONi12b%2Bni1dr9ocerHP9Wi%2BOasm8nLBISEYNaGQfPlJWxsOrKNkziaCn1R%2BPJF7dMM9npi54ggWPqPIIafM7lnn%2B96DhmCztqGcdywuk389tGRsCWsn6ULSCsN0yVzpMPCrrNAGOqUBy0g2T7s7ekA5Xa4Ntf72mE2TPI7Vdz2RBYvEcsjtAZogGWSvZ6ov%2FwSmwNqpOZCx2rj60VaZ3V823UXfDZdamV40BfCY8vfjGMdJhP6MPx35H2LaAi4kYnWj%2FzdIUp%2BGlm92XNmEJVvZ4uOilvkoJxxZ%2FcPj2KTWl7Vc4zvUxP9qarlTdDpgGEonTINPNLUeExEuQCIc3bAMSTLDrf%2F0YJfvZI3V&X-Amz-Signature=279987692bcebeb454ed5f3375f87ddff6cc4182359661705f93fc325d01e680&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
