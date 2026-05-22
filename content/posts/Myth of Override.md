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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F4TUPQ6%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDpQhpt2gda%2Fdv0sC%2BFa6nbatyW1xMsvKt7Iubn8RMYvQIgKo8fsGcIIGH0%2B7Yogylw4zDQOwq9unn34rRTaYyEMcEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDGA2cvphBoUfairC8ircA%2BcWIZAYCmJflzXJsVbqkMrQOkWUclZDi14aVZQxHeyryof1NCGY60kGI2tQGkAviKJ3ySIIG4IHmB0GG0jFxdcfb8lMLsi0Q1z9LkesGJ%2FEd4KggOK00G4fdr6nYUy3ShNGpQvhtlcdlc%2FkyGZ4XwhdPDUvhiFJDlqf4eYpyhOxo6Fey4vJO3beNvm0DautA2I4hNpwMZr4Ih9SOzcX7ZgM6cQK4t7rs3iwG1877q3cVm6FQJhCbOyLa4n3KXlPsh4PQX%2F1MMxHfikY3YLJ2MupztUvb8VvBgkvw8uxZ4oLlD9uKk%2BA%2Fpcap45bLrGOoB8Xmcqb4yBF3%2BRzoQ0nwV7eXC4WUY92HC9mSGmM%2FC3HyC4qN7tdqdGIbio%2FGlJHSootZLuDDU1CuC3Yx9Rc41sCp8eKWO9hQb%2FE9uB%2FnX04OkYHWY9kykwq7b4EonET8RAAeSO3nIvL6v%2BG87kI7PY35ZjpXC6aLL9iJpVPwlXhetC%2BObnxv7d0n9oNF9mWEU85NBIkx5Ot4aCkFx7cKz5JFtHXP3wdia2ln%2Fiba%2B6wFrewkLXjHyE1FR34EOETCVxLoJXB6czb6UwBXhtIJLDmQT0e7XdTgXMu3WMFVYEumD93NnJXKkbn9WeFMIy9wdAGOqUB4APcqlHm0WdJg1uJSfkJRpEH0IrZdb1GgX2Gw8l%2F8e%2B4Cv1gaFsSFONwA0yskjMLoWWFBvNL8hNSod0EEivOAkdzBWiyp6ImDvb0D65J3tpImFNccpkem%2F5Vms8hXZdUep4DX4NrX6MdanUlewNIL6SmNwJfMthcxQm43Yv%2Bhg%2FUsYKMW2bJERH3FASlQb56cQQttmpitzXmTdctFWK77pYCusfr&X-Amz-Signature=b82f99c43fc3bc1f45421c6265fb5398ce3bf16856449501fa212ae387e28630&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F4TUPQ6%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDpQhpt2gda%2Fdv0sC%2BFa6nbatyW1xMsvKt7Iubn8RMYvQIgKo8fsGcIIGH0%2B7Yogylw4zDQOwq9unn34rRTaYyEMcEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDGA2cvphBoUfairC8ircA%2BcWIZAYCmJflzXJsVbqkMrQOkWUclZDi14aVZQxHeyryof1NCGY60kGI2tQGkAviKJ3ySIIG4IHmB0GG0jFxdcfb8lMLsi0Q1z9LkesGJ%2FEd4KggOK00G4fdr6nYUy3ShNGpQvhtlcdlc%2FkyGZ4XwhdPDUvhiFJDlqf4eYpyhOxo6Fey4vJO3beNvm0DautA2I4hNpwMZr4Ih9SOzcX7ZgM6cQK4t7rs3iwG1877q3cVm6FQJhCbOyLa4n3KXlPsh4PQX%2F1MMxHfikY3YLJ2MupztUvb8VvBgkvw8uxZ4oLlD9uKk%2BA%2Fpcap45bLrGOoB8Xmcqb4yBF3%2BRzoQ0nwV7eXC4WUY92HC9mSGmM%2FC3HyC4qN7tdqdGIbio%2FGlJHSootZLuDDU1CuC3Yx9Rc41sCp8eKWO9hQb%2FE9uB%2FnX04OkYHWY9kykwq7b4EonET8RAAeSO3nIvL6v%2BG87kI7PY35ZjpXC6aLL9iJpVPwlXhetC%2BObnxv7d0n9oNF9mWEU85NBIkx5Ot4aCkFx7cKz5JFtHXP3wdia2ln%2Fiba%2B6wFrewkLXjHyE1FR34EOETCVxLoJXB6czb6UwBXhtIJLDmQT0e7XdTgXMu3WMFVYEumD93NnJXKkbn9WeFMIy9wdAGOqUB4APcqlHm0WdJg1uJSfkJRpEH0IrZdb1GgX2Gw8l%2F8e%2B4Cv1gaFsSFONwA0yskjMLoWWFBvNL8hNSod0EEivOAkdzBWiyp6ImDvb0D65J3tpImFNccpkem%2F5Vms8hXZdUep4DX4NrX6MdanUlewNIL6SmNwJfMthcxQm43Yv%2Bhg%2FUsYKMW2bJERH3FASlQb56cQQttmpitzXmTdctFWK77pYCusfr&X-Amz-Signature=8deae093fbd77afcf3b4cd88d04b8110fa68670303c27d2ea5eb0d0cbffe7bc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
