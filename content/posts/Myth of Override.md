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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5IBGS3Q%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T154738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDMxcBL5L%2B1kxj%2BbH%2FNsKu1iLLau50pwAMLVjFhY%2FwP2wIgEh0iQyT91TFGkVCU%2FwvVN%2FAr%2FAdLkmvhJypsxh%2FAyaUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDN46TKPnuneOdmYL7yrcA0kzUV0LKymJjo7pdFrU26LOK2QIZhwSlfKAscnEer5NTd1XnKEKUvT60T0Jo9owjZZ7dMFeSxIB2Tbi55mIRrj%2BIsPIRpnmeMIw1fELa%2B%2FcJ2N8R5ObRAaUE7i3d0CBkWaC0174s0DItIQHVQMEvVgMqJ8laSvVeY15LJV5VC%2BgEYVb0Ei21GkbxFcv3vU5TG5JWV1ImBbgy%2BDFKahBwhOOa2O9ERaV3KbJVZ4bfcK4NsutmEawmdP9%2BrwQS9%2B%2Bdg5pf2iAqtWMM87ycAybaYp4r%2F6vxraUwFn0LQt8L7Cd9p%2B4Dq58WNcsLrAIUi6xoT0l%2BJVoxc4tKA6VJbWNloZ%2BnpU8y4YLLeVobZcwKFYbFkguMD8McJY6SLYo9ExwnmIgGU6ZLbZDyZJnG8A0C6NDpuQRpHZIZvm8PR5wrE%2Bg2eOjPYdY%2B%2BqjZkzCnnnqIH0eLE6MQbCRfwut7Bxd5OMOV9Ha09kyROzYTTINi6HvnUzickmB%2FBxb8QOUOSJgmx1YGUbP%2BGHEwSmVzQtHaHVLnpO%2BdNQu8xBDgQTXYKCRPMBZQhTn44TjFpPZasQxTgitG1Qs3zt2vlfQzjpU8suLMWLYwQ%2BK%2BNqVhu708OU0Z0Ir3HDyGO2%2FU8ZiMKi69tAGOqUBWbpE%2BUNKwfixiFkVx1h%2FdhABf41rt3hjHq7fYNhGCbJQ2oQH4jEpMFUExyVAca8YvGn%2FUviKfFNpqVcu4rOHWrTS0GsRBYjXXkMTLmtKqq56dtf0seBKOPMpvLQ4bezApxZQ85y%2FeDt0TSXBKw24YTzpUA%2Fgf0%2BhF1P6%2BeKmHLm0F3V5Uz9Ol%2Fg%2BDCydLvOYRIJgKn03wFac09Nb9KT4Vgeqv0LU&X-Amz-Signature=8dfd7a8adf3e304d5adb00666c1c9f152399f04c925caaab0adbc21cb7a4a880&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5IBGS3Q%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T154738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDMxcBL5L%2B1kxj%2BbH%2FNsKu1iLLau50pwAMLVjFhY%2FwP2wIgEh0iQyT91TFGkVCU%2FwvVN%2FAr%2FAdLkmvhJypsxh%2FAyaUq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDN46TKPnuneOdmYL7yrcA0kzUV0LKymJjo7pdFrU26LOK2QIZhwSlfKAscnEer5NTd1XnKEKUvT60T0Jo9owjZZ7dMFeSxIB2Tbi55mIRrj%2BIsPIRpnmeMIw1fELa%2B%2FcJ2N8R5ObRAaUE7i3d0CBkWaC0174s0DItIQHVQMEvVgMqJ8laSvVeY15LJV5VC%2BgEYVb0Ei21GkbxFcv3vU5TG5JWV1ImBbgy%2BDFKahBwhOOa2O9ERaV3KbJVZ4bfcK4NsutmEawmdP9%2BrwQS9%2B%2Bdg5pf2iAqtWMM87ycAybaYp4r%2F6vxraUwFn0LQt8L7Cd9p%2B4Dq58WNcsLrAIUi6xoT0l%2BJVoxc4tKA6VJbWNloZ%2BnpU8y4YLLeVobZcwKFYbFkguMD8McJY6SLYo9ExwnmIgGU6ZLbZDyZJnG8A0C6NDpuQRpHZIZvm8PR5wrE%2Bg2eOjPYdY%2B%2BqjZkzCnnnqIH0eLE6MQbCRfwut7Bxd5OMOV9Ha09kyROzYTTINi6HvnUzickmB%2FBxb8QOUOSJgmx1YGUbP%2BGHEwSmVzQtHaHVLnpO%2BdNQu8xBDgQTXYKCRPMBZQhTn44TjFpPZasQxTgitG1Qs3zt2vlfQzjpU8suLMWLYwQ%2BK%2BNqVhu708OU0Z0Ir3HDyGO2%2FU8ZiMKi69tAGOqUBWbpE%2BUNKwfixiFkVx1h%2FdhABf41rt3hjHq7fYNhGCbJQ2oQH4jEpMFUExyVAca8YvGn%2FUviKfFNpqVcu4rOHWrTS0GsRBYjXXkMTLmtKqq56dtf0seBKOPMpvLQ4bezApxZQ85y%2FeDt0TSXBKw24YTzpUA%2Fgf0%2BhF1P6%2BeKmHLm0F3V5Uz9Ol%2Fg%2BDCydLvOYRIJgKn03wFac09Nb9KT4Vgeqv0LU&X-Amz-Signature=5a8829d9eb9dd536a461a0a410e2caa9aac12050b758266e2012c12885a4731f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
