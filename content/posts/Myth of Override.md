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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCVUD5H2%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T090210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFW2%2F3WJgLTb4qKzaUW%2Fe114v8gXMfWAMH7%2BRZWwI77dAiEA31eg%2B9s%2BxID%2BLN71SG94LowPeACp6ZRgLO%2B5TrkzEMYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwm9ALFu6pUiaIrvyrcA2rOPGsmkgpg4GHjepT1UPJiYnH19WlJ5CZoH9fUPenHp9k5skrXVqfXQa3WEEzbiQ1Moa2iZh1hdAT7m2hO10wHjYqy7dbayTk9dn1D0tAitJnncRpOOKxyOEnrz6bTsWLi5GzyMwYBnxsFqK8xFOJYsnat%2BBxUBunn5uu%2F8sHf7PSAtGwkovl8egD4wKij2YQmchonk6U%2Bm7yRKuyXZadPl4kyaHIfTy6zxRj4%2F1GOFoKNQZ%2BGHvZIN1kSn3JYxRAm8Mr2zBf24terzceYTNlg4WfRL4i0iywCD7Lko1pTc0TuX20S%2FRT6a1BpgGcBQSp9FV55ls8MoamX7G1phw7FXwMZy7u25iKj%2FVbO3T9WQJFYkwAg021AvjtO1v5rC3OLBZlcvsv63isYzBMHwvxWBhis7uA3Fj%2BbjAhiOZWM0N36Bg%2FdNMZ51P2YW%2BLWn6g3JHd%2B8LLcZnfr4XWbyQ%2FRySTHVtvWy5U2m%2BujOh8F%2FMKR%2BvLC3sH3KKpsSyOZ%2BoxRsg8WOR3TZGaZzZFBmvHJgOqEy7lBbK4dB3zXT7xxtp%2FDnmgei33wWaRtjiJcHQDthJUE%2BcONXRBzxMCgHPLQePwWqLUNSO6WsnTR2dhnIQjcGntffVd1cX3mMNegvdIGOqUBSLMrVAujv4e6159%2FkYD7YklYk3ZWc1ypxE%2BYYYQ%2FtI0yG34HfJa8DNqyCTnpmiWNxEx2UG86wzYbImYZd5bBg9KbHO44qukl%2FjxPBkY3fbVaBP5AWmKr%2FCtuq6kEW2Nt5HijcdcD4CfwjXfp6yjbXXX5BVx4n%2BECJzQFVgw6qlbSHhCAsYyXp1LGNaPiO3hIzhTywhVCJ%2FGJ%2FiFlx9bslXKq%2B%2FPV&X-Amz-Signature=2aecdd6bd9f0502be9ea0118cd4d428a08e04ac3fec648c7ef55635a008a7fb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCVUD5H2%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T090210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFW2%2F3WJgLTb4qKzaUW%2Fe114v8gXMfWAMH7%2BRZWwI77dAiEA31eg%2B9s%2BxID%2BLN71SG94LowPeACp6ZRgLO%2B5TrkzEMYqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwm9ALFu6pUiaIrvyrcA2rOPGsmkgpg4GHjepT1UPJiYnH19WlJ5CZoH9fUPenHp9k5skrXVqfXQa3WEEzbiQ1Moa2iZh1hdAT7m2hO10wHjYqy7dbayTk9dn1D0tAitJnncRpOOKxyOEnrz6bTsWLi5GzyMwYBnxsFqK8xFOJYsnat%2BBxUBunn5uu%2F8sHf7PSAtGwkovl8egD4wKij2YQmchonk6U%2Bm7yRKuyXZadPl4kyaHIfTy6zxRj4%2F1GOFoKNQZ%2BGHvZIN1kSn3JYxRAm8Mr2zBf24terzceYTNlg4WfRL4i0iywCD7Lko1pTc0TuX20S%2FRT6a1BpgGcBQSp9FV55ls8MoamX7G1phw7FXwMZy7u25iKj%2FVbO3T9WQJFYkwAg021AvjtO1v5rC3OLBZlcvsv63isYzBMHwvxWBhis7uA3Fj%2BbjAhiOZWM0N36Bg%2FdNMZ51P2YW%2BLWn6g3JHd%2B8LLcZnfr4XWbyQ%2FRySTHVtvWy5U2m%2BujOh8F%2FMKR%2BvLC3sH3KKpsSyOZ%2BoxRsg8WOR3TZGaZzZFBmvHJgOqEy7lBbK4dB3zXT7xxtp%2FDnmgei33wWaRtjiJcHQDthJUE%2BcONXRBzxMCgHPLQePwWqLUNSO6WsnTR2dhnIQjcGntffVd1cX3mMNegvdIGOqUBSLMrVAujv4e6159%2FkYD7YklYk3ZWc1ypxE%2BYYYQ%2FtI0yG34HfJa8DNqyCTnpmiWNxEx2UG86wzYbImYZd5bBg9KbHO44qukl%2FjxPBkY3fbVaBP5AWmKr%2FCtuq6kEW2Nt5HijcdcD4CfwjXfp6yjbXXX5BVx4n%2BECJzQFVgw6qlbSHhCAsYyXp1LGNaPiO3hIzhTywhVCJ%2FGJ%2FiFlx9bslXKq%2B%2FPV&X-Amz-Signature=a3a3e2374d424434367c8d66c19af667863e3d95d9061d369a960bb7a07eb710&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
