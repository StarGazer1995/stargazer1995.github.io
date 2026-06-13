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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC5ETX7N%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T020610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIAz3Ftf%2Fh7Zdcjx9iLOgHy75d%2FGg3dQAahNx9UaheKm0AiEAy%2BD2ry84ocWdRi%2FWwBEgyD3W%2FLmIvxPF69bf47Sxopwq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPP%2FeXeBB6k5nqe%2FOircAwW5%2FxtRAWqmr%2FXnK7lgvhzroBOvuwsOB3g2LqVn%2F9P65%2F3ygWngGjpRzB1AF5DvqqviPy0NnZ%2F%2BMnQimiquig8ichMW4ZfUPidZUEuguKI1kXY47ocpHo%2BwIno%2FJHbWnw9dkSCrOPtQcQAlV48ax0JDHy1NLoHpiflW57Aciq6GT%2BMNlg0LrgdWk9cW1URRm8rUnhNu4IOkd96x5mnFo8snf2Bv6bcOVmmp2Hlpc4squLfDMu6aGk%2BsRj7asvZxPcazijGjw4t4tvm%2F5kJfcrpz4vnsZisVXsMSweW%2BAeoQ6rjMOblnjLkU%2BxY76OnxlHOv9IO06qMfmPZBCTg1ZmM1YWb3xo5ZW6ILWYjTrcGcwO8CVRAojTK48LN8VFjr%2B5MSF2Sozs3jxPotmb%2FV32%2BDn4QlR2nLPGk2dmGu7lgTvdnKccxnhwvflRpsd5Y0ZjKwFh57m0ROS0UXYLR3BGjAebxcNHDLw96vJ9llIQx7Hxg5D8Gm0L1PBWWczK0Z1E1LyqiNv7apY8MkuVUdJsM%2FZjRLALCMr8n2Jg%2BaR%2BSZ9TU%2B%2BCGFnX1OFV2uAVfVyP8Ypgdkhbt4CjPJa%2FjU%2FEeGoKCB5Gsz25bxNHbZOvZcdaHj9ItToUDDWoi6MJLRstEGOqUBHkF4E%2B%2Bs6lzCaSq801AeLpMDZU9sHWFA9iXvA%2Bqyq8ZCKaGxSg5SAO3mMYpEzFxrg7wRPoeSPgqmGXDD1ctblxzr1gjQXAUKDP7zVxrHDNQBx%2B%2BAiFyk9yEGDJ9hEXu5Yj3A45p9TzgwDKVY5IfPXvRA9CARv7Mf7sKfgNX2Pt6yZqUT95w6xB7MkRWrD%2BMJvcdextRdBYz0kAglXp%2Fc51BWMbYI&X-Amz-Signature=c0e19d94bcfd6250d4a021085868fa23459ec5b31efcda933feac2155a289431&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC5ETX7N%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T020610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIAz3Ftf%2Fh7Zdcjx9iLOgHy75d%2FGg3dQAahNx9UaheKm0AiEAy%2BD2ry84ocWdRi%2FWwBEgyD3W%2FLmIvxPF69bf47Sxopwq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPP%2FeXeBB6k5nqe%2FOircAwW5%2FxtRAWqmr%2FXnK7lgvhzroBOvuwsOB3g2LqVn%2F9P65%2F3ygWngGjpRzB1AF5DvqqviPy0NnZ%2F%2BMnQimiquig8ichMW4ZfUPidZUEuguKI1kXY47ocpHo%2BwIno%2FJHbWnw9dkSCrOPtQcQAlV48ax0JDHy1NLoHpiflW57Aciq6GT%2BMNlg0LrgdWk9cW1URRm8rUnhNu4IOkd96x5mnFo8snf2Bv6bcOVmmp2Hlpc4squLfDMu6aGk%2BsRj7asvZxPcazijGjw4t4tvm%2F5kJfcrpz4vnsZisVXsMSweW%2BAeoQ6rjMOblnjLkU%2BxY76OnxlHOv9IO06qMfmPZBCTg1ZmM1YWb3xo5ZW6ILWYjTrcGcwO8CVRAojTK48LN8VFjr%2B5MSF2Sozs3jxPotmb%2FV32%2BDn4QlR2nLPGk2dmGu7lgTvdnKccxnhwvflRpsd5Y0ZjKwFh57m0ROS0UXYLR3BGjAebxcNHDLw96vJ9llIQx7Hxg5D8Gm0L1PBWWczK0Z1E1LyqiNv7apY8MkuVUdJsM%2FZjRLALCMr8n2Jg%2BaR%2BSZ9TU%2B%2BCGFnX1OFV2uAVfVyP8Ypgdkhbt4CjPJa%2FjU%2FEeGoKCB5Gsz25bxNHbZOvZcdaHj9ItToUDDWoi6MJLRstEGOqUBHkF4E%2B%2Bs6lzCaSq801AeLpMDZU9sHWFA9iXvA%2Bqyq8ZCKaGxSg5SAO3mMYpEzFxrg7wRPoeSPgqmGXDD1ctblxzr1gjQXAUKDP7zVxrHDNQBx%2B%2BAiFyk9yEGDJ9hEXu5Yj3A45p9TzgwDKVY5IfPXvRA9CARv7Mf7sKfgNX2Pt6yZqUT95w6xB7MkRWrD%2BMJvcdextRdBYz0kAglXp%2Fc51BWMbYI&X-Amz-Signature=afc9c2bd35f62c8a1cc9539d7fb280d9ca0866860819c5328dcead3b893c8873&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
