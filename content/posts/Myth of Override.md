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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HXTEIDJ%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T145115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIHygHR2isAEGMSweZ%2FVlRdpFNsS2wHuVb8PYiS8siQa9AiBYnSgf7c%2BhJLzc0Ae9gAbUaypCjq83XVBKZN7sG0r4ZCr%2FAwgOEAAaDDYzNzQyMzE4MzgwNSIMiBpMu6OXRfM7i6DVKtwDuuKxXcPwF5mMAtkfYVlEgJZqxebXvZio6f44KyPQYz7JGE2ppkn8dCUvfI4Cm4dcIU1jZPyvzTPtJZ7D5QHk8g4vwVEv6IZfnXjnxJJuOUdywuIAgGNyUtmvQaEY%2FCqD44GQQ9tQrIpoae%2BqSLsOV%2BJhnL8RaoRkcUizbc9sl7JXgOQjX4PPUnBI5eWNzX4hjTStkOW%2Fp%2FBLEHilyw3J8J5Zbh2YXAnFjCmZuhsyJVadvoCCEp0bIOCskuMH5NS8z4p2DAnC%2FlwCBEbeX8sg9d%2BYX25DqBwq%2B%2FYhg1AwJdlvoSuzE4lXVwZvREzwOuoPjRgXQv64KsjpiVD%2FfX47LZYrEJucIyow1%2FiRRPN%2B42KlElXoPA36OMG%2Fy3R59RjDOu9dqtanm7lvQPtZfCa6RFWuZwnwinCyy%2FDmQFLwvMSv1m8tdYbD5%2F2F9hHCNUQUmPdmijLuJUb5r76VJmXMDVtYNiL4CgvjQk71leclKIQWD7R1Oalv8GCkEBaUXih5gkZD98KHB73QWt3w4rQHMXd8PqoHP%2Bc3JJCnAZXZvJ6klJbyGgKT2iYmrL1MPN4L%2BD70hv32jnzD5w57PgCZAoenjvvjhx9pwEPZSBxqQypmoYQt2sbprWiIrW4wlqKZ1gY6pgEEoY9OJ5Un%2BRY%2BmKVX3fVS%2Be2iog6FXJZw7NmlbN6A0JxCBImv6iiemW8J8SmYza8hfge5Wh1SZZMemEOwDrsIOw6%2BllUnjFCUiPTF%2FXraMf%2FjnxGmzIraZtV6Tzl%2Bh61pRbhyttpByfAXZGXLKj%2Ba8Ks3OvgW1pkWNLIp2PSHs0U0wVykDU3jffuiIlvKmAAEkFYp8sZHBinCgblUq6i8AxMWC%2F9U&X-Amz-Signature=3556c7d70c60cec464ced6ee014fd93e8f91d62449b9a3c7a82f8ea7b1206c8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HXTEIDJ%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T145115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIHygHR2isAEGMSweZ%2FVlRdpFNsS2wHuVb8PYiS8siQa9AiBYnSgf7c%2BhJLzc0Ae9gAbUaypCjq83XVBKZN7sG0r4ZCr%2FAwgOEAAaDDYzNzQyMzE4MzgwNSIMiBpMu6OXRfM7i6DVKtwDuuKxXcPwF5mMAtkfYVlEgJZqxebXvZio6f44KyPQYz7JGE2ppkn8dCUvfI4Cm4dcIU1jZPyvzTPtJZ7D5QHk8g4vwVEv6IZfnXjnxJJuOUdywuIAgGNyUtmvQaEY%2FCqD44GQQ9tQrIpoae%2BqSLsOV%2BJhnL8RaoRkcUizbc9sl7JXgOQjX4PPUnBI5eWNzX4hjTStkOW%2Fp%2FBLEHilyw3J8J5Zbh2YXAnFjCmZuhsyJVadvoCCEp0bIOCskuMH5NS8z4p2DAnC%2FlwCBEbeX8sg9d%2BYX25DqBwq%2B%2FYhg1AwJdlvoSuzE4lXVwZvREzwOuoPjRgXQv64KsjpiVD%2FfX47LZYrEJucIyow1%2FiRRPN%2B42KlElXoPA36OMG%2Fy3R59RjDOu9dqtanm7lvQPtZfCa6RFWuZwnwinCyy%2FDmQFLwvMSv1m8tdYbD5%2F2F9hHCNUQUmPdmijLuJUb5r76VJmXMDVtYNiL4CgvjQk71leclKIQWD7R1Oalv8GCkEBaUXih5gkZD98KHB73QWt3w4rQHMXd8PqoHP%2Bc3JJCnAZXZvJ6klJbyGgKT2iYmrL1MPN4L%2BD70hv32jnzD5w57PgCZAoenjvvjhx9pwEPZSBxqQypmoYQt2sbprWiIrW4wlqKZ1gY6pgEEoY9OJ5Un%2BRY%2BmKVX3fVS%2Be2iog6FXJZw7NmlbN6A0JxCBImv6iiemW8J8SmYza8hfge5Wh1SZZMemEOwDrsIOw6%2BllUnjFCUiPTF%2FXraMf%2FjnxGmzIraZtV6Tzl%2Bh61pRbhyttpByfAXZGXLKj%2Ba8Ks3OvgW1pkWNLIp2PSHs0U0wVykDU3jffuiIlvKmAAEkFYp8sZHBinCgblUq6i8AxMWC%2F9U&X-Amz-Signature=176bd2686382d333f6dbe7c902a2f2df8d7c8eb096743da182dae1ccf7b0964c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
