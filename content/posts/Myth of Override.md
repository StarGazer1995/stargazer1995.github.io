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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQCAI7B%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T225235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIQCP0rAiKyCcqZgKlqFWz3mrEcc%2BWOt57HWgGUQi%2FlU3NgIgLQMP%2F4OOyejmUukaqFEBdGksHLWjK4NvarqwmaSfBCYq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDC1pLDiRbPWMk3IKdircAz3dxIDGUYSbpP2QwfpC9NyByDtDNJF5pa5nvP8BVVXwVTmKixDgCZwt8%2FvNAvIgwAhiLUdM15nSGYcdf%2FN25g%2BPaXXqDn1dA1i2%2FnUB%2B7pzDUpiYyUjGbG7UB46UOmiE00TjZEyViD%2BZ4dStvHcz%2FtCwcZA9bxGdy8ddn19efXffi%2BXPZ9TpM%2F5NmBW%2FWFRA%2F7F0RL6xLIKWrrZL3uT43kcCb%2FnKwETgyX5i04B55gl9fWN4U%2B32lCITJLoRuq7iTbUZ0VvIURgIhIa5EZC2OXrcYDFbz8TNjz1x7YOLHF5I3H2ebP%2B%2BrIcfIcE%2B4wEwr%2BebA1ZgScwdWh6gkp0g3zQOXkKY0%2FTumueeoqKspp6J0yJ5qfE8zjTG5Ms6mfQiQR7LiHYKwHV9yguUlyXyx99ROe1fC8UEJ9ZgGp68wsUSyBGICMPPVmFZGF2wD%2FsbyJOwzbNYFD8flUSDL8zDH7MYWWCJt%2Fx3aWDjr%2FcN9e5%2BypGQTBTaDNxGhxgxU5ktNJDWsP05ar3f8Hgln2KuGPZkn5A5xNkCrO%2BQP857YiDyJej%2FuFQu7iOwxrRNvm1zbAD2oDmfVWleeuZa2bm7T9nQxuqv%2Fz0P51NUVzzQIuKF5D6Ur1Z24fJQGn%2BMOe4ydMGOqUBfWVnkLRznTgKFY6SIzvsK2aeqk428DYsXUGEHfO7dMKkkjchaSk8HbHB2HvuhfCeVOrQh1ASraZruncc9YW5%2BQUmxxIUd%2B%2Bun6n4Z04UOmslwy%2FGUtURJwZ8uBNQrGjNWNjqsxK7%2F2Wj1%2B0NrMTH%2F%2F9y7EFnQ7nj5aCi8PcPKfn7Ub0ZtpG6gbFxz%2F9AJ9W5ngShcjKBM23jSpGE6d2Vt%2BkzMbNO&X-Amz-Signature=a439e1879e206eae590b2041d4f4d77c6de18a4dd0f946eee384a11b90b642f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JQCAI7B%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T225235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIQCP0rAiKyCcqZgKlqFWz3mrEcc%2BWOt57HWgGUQi%2FlU3NgIgLQMP%2F4OOyejmUukaqFEBdGksHLWjK4NvarqwmaSfBCYq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDC1pLDiRbPWMk3IKdircAz3dxIDGUYSbpP2QwfpC9NyByDtDNJF5pa5nvP8BVVXwVTmKixDgCZwt8%2FvNAvIgwAhiLUdM15nSGYcdf%2FN25g%2BPaXXqDn1dA1i2%2FnUB%2B7pzDUpiYyUjGbG7UB46UOmiE00TjZEyViD%2BZ4dStvHcz%2FtCwcZA9bxGdy8ddn19efXffi%2BXPZ9TpM%2F5NmBW%2FWFRA%2F7F0RL6xLIKWrrZL3uT43kcCb%2FnKwETgyX5i04B55gl9fWN4U%2B32lCITJLoRuq7iTbUZ0VvIURgIhIa5EZC2OXrcYDFbz8TNjz1x7YOLHF5I3H2ebP%2B%2BrIcfIcE%2B4wEwr%2BebA1ZgScwdWh6gkp0g3zQOXkKY0%2FTumueeoqKspp6J0yJ5qfE8zjTG5Ms6mfQiQR7LiHYKwHV9yguUlyXyx99ROe1fC8UEJ9ZgGp68wsUSyBGICMPPVmFZGF2wD%2FsbyJOwzbNYFD8flUSDL8zDH7MYWWCJt%2Fx3aWDjr%2FcN9e5%2BypGQTBTaDNxGhxgxU5ktNJDWsP05ar3f8Hgln2KuGPZkn5A5xNkCrO%2BQP857YiDyJej%2FuFQu7iOwxrRNvm1zbAD2oDmfVWleeuZa2bm7T9nQxuqv%2Fz0P51NUVzzQIuKF5D6Ur1Z24fJQGn%2BMOe4ydMGOqUBfWVnkLRznTgKFY6SIzvsK2aeqk428DYsXUGEHfO7dMKkkjchaSk8HbHB2HvuhfCeVOrQh1ASraZruncc9YW5%2BQUmxxIUd%2B%2Bun6n4Z04UOmslwy%2FGUtURJwZ8uBNQrGjNWNjqsxK7%2F2Wj1%2B0NrMTH%2F%2F9y7EFnQ7nj5aCi8PcPKfn7Ub0ZtpG6gbFxz%2F9AJ9W5ngShcjKBM23jSpGE6d2Vt%2BkzMbNO&X-Amz-Signature=959c3add60a297f04d8f972a520c332b1ec2af79828395a3871beea271a470fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
