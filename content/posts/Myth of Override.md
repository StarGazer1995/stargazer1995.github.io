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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672RKDQ5S%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T164552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FnQdX4NHWFKGlqGLAQ8QZ%2FH7fI1FrXFZOiHTDWv%2BlhgIhAODxJFrHbd0D6zXlmmQnNrn5756604LVKAVP7UdmNiOTKogECMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkyKkbPdaaJg88By0q3AM5nc6ansmPIBjA6kp%2FFTpkLCkdYYMg9QkxoIyRbsUYhAwk02cDmHjPnpyppOHy%2BYSGr2V6mWNgriqv7HbmRywxSx5JTiAzcg6ndxP9lO8gVs3A96G%2FDOM0JVycCJHwzHvHJIVtDzS6hNYu9v823X%2B%2BXd3AUlwnElKmGOGzrjvNX12NeuLWM4NnzfqK0JXC9k3uqIsrGKakmO7xISnc7OuUQa9EBR2DCIlVQFbKiQZrwMzpEA8POb8R5ssyFnUW4XEZf76fKUqIEaHwi%2BDg9VEIUV3Uj3rpnHXrmP3IyxuT%2BvUDrJTP0Dp3OzPT%2FUbZ1nCUqrOa4vVxi5NOyT365%2FDHJ0quhN5ElemrBNtGnLHa6Vw4K0A3%2FrRDHnST7%2B78goetwnsY8op%2FCEHqVWiLx6fbixqzjz%2FSXPnQgp6ZLxMR%2FwPGqYgzXtTDthsCaULZ8AIep%2Bzw%2BRyqIgZRzk1Hhw5i8%2F2dI37xdg743iwSzp9snDI7HMxdAR86RSKt9tfFeccC3Rt4TZcUIydDYwQVRQuVsKyfbmhaWSOr%2FQlNQkLrjKfqmNXjPn5%2FARDhIlR0R9kgAtbfAE3rhu%2BlhMtDMIwJFTpzaq4X7mHPMP8X5UKfsbztdmXDqPpEkv0JojDzkrjTBjqkAZeHpqC9M9ve%2BA%2F7sbC3TjNQQIQzYQvsaC4NCgPN7tLB1bvonGtsHF8Wiubolnjcu6Kt0jrnhJbsPQYu1C61jmQXZiJcCRZuEKaAQpM6%2Bl1Mseo7aHg4zh4S0zC70J8xph0FDp7gW9O5kphMwERLHUmhF%2B7OvLVVqHGLFgTL3dh%2FUa9sZn7c8WkK9RFCMz88T%2B4ERb76R%2FMBHaK%2B%2F0lMz6UKtcAn&X-Amz-Signature=dd18fa43d0ac7e7312393e2c10d3226cb7f69a7362b20a926d20c63ab918a82b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672RKDQ5S%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T164552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FnQdX4NHWFKGlqGLAQ8QZ%2FH7fI1FrXFZOiHTDWv%2BlhgIhAODxJFrHbd0D6zXlmmQnNrn5756604LVKAVP7UdmNiOTKogECMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxkyKkbPdaaJg88By0q3AM5nc6ansmPIBjA6kp%2FFTpkLCkdYYMg9QkxoIyRbsUYhAwk02cDmHjPnpyppOHy%2BYSGr2V6mWNgriqv7HbmRywxSx5JTiAzcg6ndxP9lO8gVs3A96G%2FDOM0JVycCJHwzHvHJIVtDzS6hNYu9v823X%2B%2BXd3AUlwnElKmGOGzrjvNX12NeuLWM4NnzfqK0JXC9k3uqIsrGKakmO7xISnc7OuUQa9EBR2DCIlVQFbKiQZrwMzpEA8POb8R5ssyFnUW4XEZf76fKUqIEaHwi%2BDg9VEIUV3Uj3rpnHXrmP3IyxuT%2BvUDrJTP0Dp3OzPT%2FUbZ1nCUqrOa4vVxi5NOyT365%2FDHJ0quhN5ElemrBNtGnLHa6Vw4K0A3%2FrRDHnST7%2B78goetwnsY8op%2FCEHqVWiLx6fbixqzjz%2FSXPnQgp6ZLxMR%2FwPGqYgzXtTDthsCaULZ8AIep%2Bzw%2BRyqIgZRzk1Hhw5i8%2F2dI37xdg743iwSzp9snDI7HMxdAR86RSKt9tfFeccC3Rt4TZcUIydDYwQVRQuVsKyfbmhaWSOr%2FQlNQkLrjKfqmNXjPn5%2FARDhIlR0R9kgAtbfAE3rhu%2BlhMtDMIwJFTpzaq4X7mHPMP8X5UKfsbztdmXDqPpEkv0JojDzkrjTBjqkAZeHpqC9M9ve%2BA%2F7sbC3TjNQQIQzYQvsaC4NCgPN7tLB1bvonGtsHF8Wiubolnjcu6Kt0jrnhJbsPQYu1C61jmQXZiJcCRZuEKaAQpM6%2Bl1Mseo7aHg4zh4S0zC70J8xph0FDp7gW9O5kphMwERLHUmhF%2B7OvLVVqHGLFgTL3dh%2FUa9sZn7c8WkK9RFCMz88T%2B4ERb76R%2FMBHaK%2B%2F0lMz6UKtcAn&X-Amz-Signature=56a18a79e804b70841afa2bf3b7c0025bd55e6f5eebb5505a855bf27c950d98a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
