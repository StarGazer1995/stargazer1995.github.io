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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUTNNI56%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T182645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDlRBX6FsHieb53MdpP%2BF%2F4N9sC00QcgseTfaI5r7UjGQIgCVb7EaVBaBgMu0ezleFjwZBfUM45jb7u8Q5Q1BCnJ0oqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK16CML4%2Bis7EAgnGircA6JEthqp0xww4f4kUjSBE8osDblsIzv044VcjBcfKwbl1ZL%2FpqwgP44hbS037eBgqVkyas6%2Fet%2Bk7VZsGNeppvorY2%2BOi%2BBEsLgnkiymuJr%2B%2FfmO17jHKyaQOX0SmAZk2iC%2FWIhWgctaaFAFksEF9C6kHDpWzIhXclL2Z%2Fohuf%2B8MzLJkPWyKSuvk2uD%2F9WoreO8p2b1GwXIudql0b5g5SuzCs8fA2UB2HTvHoNlPA4ZaD3OXdczJzHZfN2lCiR%2F53jN3Fc4x5%2FqUi51tislICXCF6nInZfjVMAMO0G7%2FpbWX1pgyDo3qXQqKvG7DjanhVnKWhZe0fNKgvN7rIXPYq0hg4VD%2Fcam8s5k9J7p%2FYKvqSPv7kd4uQsT0eJqfm91D8P98gLq6vAEGNh8ZP3qAUvCf%2B0Qpwr5OIeJHK%2B0Wydy0dHKmDPhYIgYJbAPvaM6GPftnXAjdg5MG46KsyRVdSHc6PH0OY03iLlVMlLUSQcNrWzfFRyP0FREM00%2BmQ25KKf71pnSY8eMDu2BpN9XYX6C6ZMOx2lke9%2F6pAbWl6oU3IMesy3w1tHEIgAe5FdNcWZS7MQpKaROECB%2BhXWrlLjuYKUFK%2BdIT9HXvFkoyb%2F7Y61JWkx7hC34YfULMPis59AGOqUBT46x8zZ6GLnNL1jVJCXhCokMvClvso4x6yS0%2FDwqHjpzV4Nc1cwApq2iElTaLB4K%2B1dMdATVk9V6rpBOMusH7EuF0r6Vp5bTcrw7KU2F3bYlAGY%2F01jPaoDWsTMCUx8oZawzCKTy3Uy2eEfx%2FspGcI0UAS7vx158zUPcZmLnoMDw%2BOHPzj%2FVOHsxEkxmoctOffpTwjGliij6o0K%2FnUODtb3GjBc4&X-Amz-Signature=e48b1fed394a5996fcc3eed17be1b51fea5810a3d92f13347aa0b51997fc37be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUTNNI56%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T182645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDlRBX6FsHieb53MdpP%2BF%2F4N9sC00QcgseTfaI5r7UjGQIgCVb7EaVBaBgMu0ezleFjwZBfUM45jb7u8Q5Q1BCnJ0oqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK16CML4%2Bis7EAgnGircA6JEthqp0xww4f4kUjSBE8osDblsIzv044VcjBcfKwbl1ZL%2FpqwgP44hbS037eBgqVkyas6%2Fet%2Bk7VZsGNeppvorY2%2BOi%2BBEsLgnkiymuJr%2B%2FfmO17jHKyaQOX0SmAZk2iC%2FWIhWgctaaFAFksEF9C6kHDpWzIhXclL2Z%2Fohuf%2B8MzLJkPWyKSuvk2uD%2F9WoreO8p2b1GwXIudql0b5g5SuzCs8fA2UB2HTvHoNlPA4ZaD3OXdczJzHZfN2lCiR%2F53jN3Fc4x5%2FqUi51tislICXCF6nInZfjVMAMO0G7%2FpbWX1pgyDo3qXQqKvG7DjanhVnKWhZe0fNKgvN7rIXPYq0hg4VD%2Fcam8s5k9J7p%2FYKvqSPv7kd4uQsT0eJqfm91D8P98gLq6vAEGNh8ZP3qAUvCf%2B0Qpwr5OIeJHK%2B0Wydy0dHKmDPhYIgYJbAPvaM6GPftnXAjdg5MG46KsyRVdSHc6PH0OY03iLlVMlLUSQcNrWzfFRyP0FREM00%2BmQ25KKf71pnSY8eMDu2BpN9XYX6C6ZMOx2lke9%2F6pAbWl6oU3IMesy3w1tHEIgAe5FdNcWZS7MQpKaROECB%2BhXWrlLjuYKUFK%2BdIT9HXvFkoyb%2F7Y61JWkx7hC34YfULMPis59AGOqUBT46x8zZ6GLnNL1jVJCXhCokMvClvso4x6yS0%2FDwqHjpzV4Nc1cwApq2iElTaLB4K%2B1dMdATVk9V6rpBOMusH7EuF0r6Vp5bTcrw7KU2F3bYlAGY%2F01jPaoDWsTMCUx8oZawzCKTy3Uy2eEfx%2FspGcI0UAS7vx158zUPcZmLnoMDw%2BOHPzj%2FVOHsxEkxmoctOffpTwjGliij6o0K%2FnUODtb3GjBc4&X-Amz-Signature=aacc5a97380511e834e2ec9fc55702de84d01e805fba662b9d6ab680f2013889&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
