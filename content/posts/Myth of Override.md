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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPM27E45%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T164256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCuHVr2Lk9IW3khjWZECHYwroTFufpKSAHZ55oKvT3QgIgDAW1fou7xKWr6WlX3BCau%2FwHvjx4759hLbrizJg1uXQq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDLdSSiHPYS0EZ9RJhCrcA10SfXYgq7Xnd9i35GrKLyA23Jl0mWzTUL6cn6GiHK%2Bd%2BpR1dSfcx959VdfQB1DrDdHsEWwOKBLuNXaLIHm1zDgH6tuC2F2y6paFZvZjYZK1GXNo2fdiLOQ9EABG6MLTl%2BMuVpWle3n%2Bat%2BWk8s2QknsDaMLNjK6PpjncegLyGS3uMmQNrFsqdIqlGIPfnXmLAU1Xn0xxA47CBO5cdpApfTcghNDvYO%2BSRtmOMFItoAS3%2Fo0w%2Fmgu4%2F3cCXVEcJVMi33e4HTmam%2B49h2I%2FOGQmXgkQDSv2n%2BZCfS%2BGsoeja1%2B0k60ymlJQAeregQb1YabSeOz0WjCNIO%2Bkm7W2Z0GWJNnJl0CXCw7R5YZZUu4vdoEqKTruHuGH2Hn167CAi3kkrOVcDCCeN47YJ8vhLkCJ19O%2Fm3IIaWjABCWLg%2BxPjy%2BkaEhWarGRqqwlDBDk8tj9k2sARBqD%2BrA0tiO8ljYvYdS0YqccQwKxSdbHo5ZNORZxTD4oG7rmYgOe7iIZjME6RSHtD1eoZQIF7Wt3V%2FPohjg2NqxrpEcen7RwE0XsOZdWRlpvreOutcyN63Y6ucORL%2BMbhVOPmmq4A78z3CycOvnmwwaW7uE9MYGtT9wErqLPKsOEHqUbZbs3SoMOeu7tIGOqUB%2BF92OZyRS17b2z7M9uDFB2N01hOZS6eO1NXBUBC%2Bwf%2BpdaqunpGg523l%2FPMCxllPBgPBJvK%2Biu8ulpQq5A2VRl0JLnQ24askC6SmGgXAA0XOLkXsbZx4Gy2PRDgGZkCLsUZQ5XETjcOCuwh1n9Hs2MgoN4BWh3nhuz11Ld%2FVzQjRbujez%2Fr2KwkYFyAMw5L9IlGmetx7WWYSPOhv6pACzxBJ%2FRJJ&X-Amz-Signature=ef4cf9f80a058a4e34fc67d758181df8c0665cfcb0dfc2b59acb10b46cd32d7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPM27E45%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T164256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCuHVr2Lk9IW3khjWZECHYwroTFufpKSAHZ55oKvT3QgIgDAW1fou7xKWr6WlX3BCau%2FwHvjx4759hLbrizJg1uXQq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDLdSSiHPYS0EZ9RJhCrcA10SfXYgq7Xnd9i35GrKLyA23Jl0mWzTUL6cn6GiHK%2Bd%2BpR1dSfcx959VdfQB1DrDdHsEWwOKBLuNXaLIHm1zDgH6tuC2F2y6paFZvZjYZK1GXNo2fdiLOQ9EABG6MLTl%2BMuVpWle3n%2Bat%2BWk8s2QknsDaMLNjK6PpjncegLyGS3uMmQNrFsqdIqlGIPfnXmLAU1Xn0xxA47CBO5cdpApfTcghNDvYO%2BSRtmOMFItoAS3%2Fo0w%2Fmgu4%2F3cCXVEcJVMi33e4HTmam%2B49h2I%2FOGQmXgkQDSv2n%2BZCfS%2BGsoeja1%2B0k60ymlJQAeregQb1YabSeOz0WjCNIO%2Bkm7W2Z0GWJNnJl0CXCw7R5YZZUu4vdoEqKTruHuGH2Hn167CAi3kkrOVcDCCeN47YJ8vhLkCJ19O%2Fm3IIaWjABCWLg%2BxPjy%2BkaEhWarGRqqwlDBDk8tj9k2sARBqD%2BrA0tiO8ljYvYdS0YqccQwKxSdbHo5ZNORZxTD4oG7rmYgOe7iIZjME6RSHtD1eoZQIF7Wt3V%2FPohjg2NqxrpEcen7RwE0XsOZdWRlpvreOutcyN63Y6ucORL%2BMbhVOPmmq4A78z3CycOvnmwwaW7uE9MYGtT9wErqLPKsOEHqUbZbs3SoMOeu7tIGOqUB%2BF92OZyRS17b2z7M9uDFB2N01hOZS6eO1NXBUBC%2Bwf%2BpdaqunpGg523l%2FPMCxllPBgPBJvK%2Biu8ulpQq5A2VRl0JLnQ24askC6SmGgXAA0XOLkXsbZx4Gy2PRDgGZkCLsUZQ5XETjcOCuwh1n9Hs2MgoN4BWh3nhuz11Ld%2FVzQjRbujez%2Fr2KwkYFyAMw5L9IlGmetx7WWYSPOhv6pACzxBJ%2FRJJ&X-Amz-Signature=1b23e39e4f3b951f8cd56013bd0df16ce630f160b113709624eb264e8209eba1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
