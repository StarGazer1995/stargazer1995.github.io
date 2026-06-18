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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYCQN6M%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T023000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICq2%2BcyiBzUFe%2FVtrr0RSFZwnvvtxQMuEx8kV6KLD1B8AiEApAzHLS%2FmscVNzsfc3Ze5h5sKNy7sQ%2FXezlMpOTwC9lAqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJYxgVQWNMibTgCKWyrcA4BORyuiqnbmd4NxyH2530FhTjiTQNcVQxLs0lLCbBP62xfzMLQKE7CCUS1pFXABTZf9hy%2FmwtiVsyKzhaSkEQEbrG1zQDtf4LvKuWLXsG5wN%2BeMl5MczBdzzOHHACP7tsPxw0lj6dt3xznx6a0mJ3BTVACSbmIqN4WnCiwI3l8Nhlb3B%2FYm3%2BmeKa%2FCodEwHHLTe%2Fmu9svU%2BK6CkRhftlDEip0fipSkKk5rd6fhhw0VCU7%2FI3lDGc0sOFpizzU33HPi%2B0IzfbGI8xXtwEIcgJSnfLfL38EKBnZ3GR9p1tZUCfvI%2BDveDuM2n3mvzjkipYu4CY%2F06KFoCnsqnNZA01oY6C9Y%2Bb7Hl7UMtf%2FmgHwzCu28YvNvEbUW8DtLySl4MGl2DVK%2BYqstbzhCGnAKXnAkzEhl11xiWHcpH%2BdfpJyxHrM7s%2FISzVNYX1e1p%2BLU%2ByoHkP2CdJVtqJVdwZT8Fbe43CKPRakG31pQE2Cg5mzsozsazRF9doaT6qLp5z6VyKQra7I8uLqpDd50P%2FRCCVPRop%2F0AdVFjW3cgUdMZIyxedIjd9WZXeC6AQ7yEDjSB4vWmFBTDnt51HA9pFRcnzW8zmxd8Vjb1K9MQut6yY62oLadcxRHsjLqpUlQMICGzdEGOqUBsViF8hDOw2vWNv5bgW8ZWk%2BDftfuIpQln%2FfrQmwcp%2BwXMzu%2BNoPYpwuMVhnliX7SuO10jvEej9%2FXPYCBdVn5671%2F1L2ngkwcxVBF%2Bx%2FCo%2FLfX%2B8efvsxnGAXkCIYwpgHzAeF2v8zmDy%2BmQxQjZQ3EpwmXQwPsHT7reXNpP5jk4qfMBwi2CyHcFZ39vqDEdeo7s0TQqOOxl%2FiRMtM153mvUJO13Ci&X-Amz-Signature=f930a02e86cb185bba977c3c0fd0b3c8788a36b3356cab4956eee92dd4cbb908&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYCQN6M%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T023000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICq2%2BcyiBzUFe%2FVtrr0RSFZwnvvtxQMuEx8kV6KLD1B8AiEApAzHLS%2FmscVNzsfc3Ze5h5sKNy7sQ%2FXezlMpOTwC9lAqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJYxgVQWNMibTgCKWyrcA4BORyuiqnbmd4NxyH2530FhTjiTQNcVQxLs0lLCbBP62xfzMLQKE7CCUS1pFXABTZf9hy%2FmwtiVsyKzhaSkEQEbrG1zQDtf4LvKuWLXsG5wN%2BeMl5MczBdzzOHHACP7tsPxw0lj6dt3xznx6a0mJ3BTVACSbmIqN4WnCiwI3l8Nhlb3B%2FYm3%2BmeKa%2FCodEwHHLTe%2Fmu9svU%2BK6CkRhftlDEip0fipSkKk5rd6fhhw0VCU7%2FI3lDGc0sOFpizzU33HPi%2B0IzfbGI8xXtwEIcgJSnfLfL38EKBnZ3GR9p1tZUCfvI%2BDveDuM2n3mvzjkipYu4CY%2F06KFoCnsqnNZA01oY6C9Y%2Bb7Hl7UMtf%2FmgHwzCu28YvNvEbUW8DtLySl4MGl2DVK%2BYqstbzhCGnAKXnAkzEhl11xiWHcpH%2BdfpJyxHrM7s%2FISzVNYX1e1p%2BLU%2ByoHkP2CdJVtqJVdwZT8Fbe43CKPRakG31pQE2Cg5mzsozsazRF9doaT6qLp5z6VyKQra7I8uLqpDd50P%2FRCCVPRop%2F0AdVFjW3cgUdMZIyxedIjd9WZXeC6AQ7yEDjSB4vWmFBTDnt51HA9pFRcnzW8zmxd8Vjb1K9MQut6yY62oLadcxRHsjLqpUlQMICGzdEGOqUBsViF8hDOw2vWNv5bgW8ZWk%2BDftfuIpQln%2FfrQmwcp%2BwXMzu%2BNoPYpwuMVhnliX7SuO10jvEej9%2FXPYCBdVn5671%2F1L2ngkwcxVBF%2Bx%2FCo%2FLfX%2B8efvsxnGAXkCIYwpgHzAeF2v8zmDy%2BmQxQjZQ3EpwmXQwPsHT7reXNpP5jk4qfMBwi2CyHcFZ39vqDEdeo7s0TQqOOxl%2FiRMtM153mvUJO13Ci&X-Amz-Signature=e4f606eabe58effd3592c2aad5837261391226813a4fb9fa708d7338f27a27a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
