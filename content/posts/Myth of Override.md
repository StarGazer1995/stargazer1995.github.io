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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X3IGGLT%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T104309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb6UxvKv4bUilP%2BEr6D6wWz8QsSRg1MpbZNHHctpjK7wIgASuBg%2B5dDlcTuVICC0zzT2g3zvDuINt1llNUwx%2Bncmkq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDHatHjfMtTS4rHlXUyrcAyrYdSNE9SIHeCfQoTv1J%2BytkUECW0kiTuTEcwV6YIHyuuAQk8mMSnZL%2B0G9LljF3eX96faZybt6qxtHRBJdzWB6nC959ps71%2B4N428Ryd7Lc1HFGrwcJJDuzzcBDI%2BTzdIrO9Ai3NEHHWAtKJ4HsayMmAMyOqkpksM0Xvg8i%2FA%2BJNv%2FlLY%2FNzBnfK%2Fl%2FYCBmhP501c8h92DLxfSELznfjRjn1vMG1lHg4axGaZS1snNzi7MR%2FZdkbDCsPVSRkp49HS0ygr8bngJRlzwZOVsCI2dPJCbIUmNCpYcwgmgLoHFtJ58yufmrZinO2QZRpiykqt0z1uQug6gp2z4dcZfJd3zAu%2BrgXAb67PxmvJwf1hYgzE8%2BWqTdeM1nV6jEA4RNG5JNgtBvpU8mns%2FK%2BQqrq3BxTmJc8OD2Ly22tqEubjhmYx63V8%2FvFsvjiokjOUIQXLl14qCDMeP6Px7w%2BN8NAtlTbRXzDjKlUeIMhmSq099RF%2BFGRNR2Ik4%2BHiV1Z15UPn1CbHGF69faLefE%2B%2Fi1nINuax%2FXCxVGN0o1jObjVX%2BiJG6eYKEi9BeV4SnL1mAshdfC0ZKRyXI0qmqBiYN2Es9Sxh7ZCh3OteGMwR%2B84%2BPEFkP902CUcIMr1YVMN2f%2BdEGOqUBzVaZGwC29J5xREQtXctT6qhaKCCbBxi9aGH%2FPmMBPj3uUvzHCkiFRo%2BBLzDTW5OefjouMkTWl%2BxcdsvaHGjel0Yz3MBUcQZn3YpnR4l7brfgFsBeDW3Zc%2FWdmpCBaMsV3TNtWKKcHbqZXcDLMj41riznzxsikjgAH7tSDTJkBwZNlio45L7JyIbJk%2BIqHN%2FffpFC1K4SXo3CqzYjO0g6c8aX0VZr&X-Amz-Signature=9740e005a1c2218e92e3efa0c7b36fc48876ecf16b21d25166d7501049cafb9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X3IGGLT%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T104309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb6UxvKv4bUilP%2BEr6D6wWz8QsSRg1MpbZNHHctpjK7wIgASuBg%2B5dDlcTuVICC0zzT2g3zvDuINt1llNUwx%2Bncmkq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDHatHjfMtTS4rHlXUyrcAyrYdSNE9SIHeCfQoTv1J%2BytkUECW0kiTuTEcwV6YIHyuuAQk8mMSnZL%2B0G9LljF3eX96faZybt6qxtHRBJdzWB6nC959ps71%2B4N428Ryd7Lc1HFGrwcJJDuzzcBDI%2BTzdIrO9Ai3NEHHWAtKJ4HsayMmAMyOqkpksM0Xvg8i%2FA%2BJNv%2FlLY%2FNzBnfK%2Fl%2FYCBmhP501c8h92DLxfSELznfjRjn1vMG1lHg4axGaZS1snNzi7MR%2FZdkbDCsPVSRkp49HS0ygr8bngJRlzwZOVsCI2dPJCbIUmNCpYcwgmgLoHFtJ58yufmrZinO2QZRpiykqt0z1uQug6gp2z4dcZfJd3zAu%2BrgXAb67PxmvJwf1hYgzE8%2BWqTdeM1nV6jEA4RNG5JNgtBvpU8mns%2FK%2BQqrq3BxTmJc8OD2Ly22tqEubjhmYx63V8%2FvFsvjiokjOUIQXLl14qCDMeP6Px7w%2BN8NAtlTbRXzDjKlUeIMhmSq099RF%2BFGRNR2Ik4%2BHiV1Z15UPn1CbHGF69faLefE%2B%2Fi1nINuax%2FXCxVGN0o1jObjVX%2BiJG6eYKEi9BeV4SnL1mAshdfC0ZKRyXI0qmqBiYN2Es9Sxh7ZCh3OteGMwR%2B84%2BPEFkP902CUcIMr1YVMN2f%2BdEGOqUBzVaZGwC29J5xREQtXctT6qhaKCCbBxi9aGH%2FPmMBPj3uUvzHCkiFRo%2BBLzDTW5OefjouMkTWl%2BxcdsvaHGjel0Yz3MBUcQZn3YpnR4l7brfgFsBeDW3Zc%2FWdmpCBaMsV3TNtWKKcHbqZXcDLMj41riznzxsikjgAH7tSDTJkBwZNlio45L7JyIbJk%2BIqHN%2FffpFC1K4SXo3CqzYjO0g6c8aX0VZr&X-Amz-Signature=5aabc9b780167d393cca8d323df2a5629afaa05084ed5bad6e97a06eb84bf031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
