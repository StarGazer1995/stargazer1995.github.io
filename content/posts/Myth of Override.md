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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYGSK2XT%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T143140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIDYZAckc0KF7xuWgNQkfM2IW162urG%2BXXJFFJbm%2BqGhUAiEAq0r2bhXy4fJR%2FLxdP1DIadvsXBajx6mxbCOgdJKsA7gq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDAetZuzYPp1YKSsWySrcA%2B0gxLZvZAv7zr1KYau3HTstIz%2F%2B97y63c%2BsBotv%2FssboxAH6fZNeOMX%2BN6dQaE9Am69E9%2BOcQOHxwR88cEwxVuQ4lZBvt8XDhYf0CH4kpjq3pE4hk7LmXr8iKSjOwqQmErh2PVuj%2BuutX5DAYyDUfcGCuKGV%2Fg8JAzaixoVss0SxxX1HfuljnEWnLxU%2BpXG9b1qh%2B6JPV3yabUXJcxbwUBVTwmv%2FkfQhbqi%2FptGUuWwvdLzJIwTNHWtc8kd1umy0T%2FXhLt%2BXPVsXrD4OgYi5%2BDjTzgXyihfSYC8c6vAGALZat1lxiVeU7HMDtO5ijtxNqWFn8Hc1xh1NLhtboRxxO9rwJlLYdRy0tjpjJCbZYDshRyiAatFFnBWihmuOs6z7gJ2PJ%2FF8%2F0hT3WlEejIg5liE5dfEjBK1bx7JEaNrIFQu1bXRtqt4ifi3mdiurkpYEMDMJMdk4VIgyLv8YWBvpACFcUbMbAnW1nvUWPkymW8Hw7Nn1ofh6eWh1iNF27yTrsb2%2BFyxNKYUGCNLQklkJHZFtwIbNt5HrVhWQyfkD79HObRTuwC02FR1bV6gc6eJgoPbSuuBg7o%2F9WVpZs8DSSC%2BxbN4u4nJ4XxZNls5aFsvZt4V3K%2F%2BEPzTk%2FKMIaq9dQGOqUBx8FiY0tgqGMGvpVTj%2FUTeWozV5HV6R52dmEn%2B3kSOjMnGe3Tk71ZZW8nkS0w9WBPF3GaOAKVlPCoPG0puMe4fo2B3jkhok17JX2%2B%2FsjGEgOP7qmdqHI0NTJ0SJvZUfu8%2Fy%2B335thrwhqq4Eg9JJzlFXR4oY8zhEsr4YQPn1527IbJMPF6uZXh8fvWYLKaiyGDPW17CV4NY%2BdQD%2FfGCPYb%2FN1RgPq&X-Amz-Signature=18705bd0dcaba025d662fdfcf5a46d08f8997690dceb4c9981bd30e08399055f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYGSK2XT%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T143140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIDYZAckc0KF7xuWgNQkfM2IW162urG%2BXXJFFJbm%2BqGhUAiEAq0r2bhXy4fJR%2FLxdP1DIadvsXBajx6mxbCOgdJKsA7gq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDAetZuzYPp1YKSsWySrcA%2B0gxLZvZAv7zr1KYau3HTstIz%2F%2B97y63c%2BsBotv%2FssboxAH6fZNeOMX%2BN6dQaE9Am69E9%2BOcQOHxwR88cEwxVuQ4lZBvt8XDhYf0CH4kpjq3pE4hk7LmXr8iKSjOwqQmErh2PVuj%2BuutX5DAYyDUfcGCuKGV%2Fg8JAzaixoVss0SxxX1HfuljnEWnLxU%2BpXG9b1qh%2B6JPV3yabUXJcxbwUBVTwmv%2FkfQhbqi%2FptGUuWwvdLzJIwTNHWtc8kd1umy0T%2FXhLt%2BXPVsXrD4OgYi5%2BDjTzgXyihfSYC8c6vAGALZat1lxiVeU7HMDtO5ijtxNqWFn8Hc1xh1NLhtboRxxO9rwJlLYdRy0tjpjJCbZYDshRyiAatFFnBWihmuOs6z7gJ2PJ%2FF8%2F0hT3WlEejIg5liE5dfEjBK1bx7JEaNrIFQu1bXRtqt4ifi3mdiurkpYEMDMJMdk4VIgyLv8YWBvpACFcUbMbAnW1nvUWPkymW8Hw7Nn1ofh6eWh1iNF27yTrsb2%2BFyxNKYUGCNLQklkJHZFtwIbNt5HrVhWQyfkD79HObRTuwC02FR1bV6gc6eJgoPbSuuBg7o%2F9WVpZs8DSSC%2BxbN4u4nJ4XxZNls5aFsvZt4V3K%2F%2BEPzTk%2FKMIaq9dQGOqUBx8FiY0tgqGMGvpVTj%2FUTeWozV5HV6R52dmEn%2B3kSOjMnGe3Tk71ZZW8nkS0w9WBPF3GaOAKVlPCoPG0puMe4fo2B3jkhok17JX2%2B%2FsjGEgOP7qmdqHI0NTJ0SJvZUfu8%2Fy%2B335thrwhqq4Eg9JJzlFXR4oY8zhEsr4YQPn1527IbJMPF6uZXh8fvWYLKaiyGDPW17CV4NY%2BdQD%2FfGCPYb%2FN1RgPq&X-Amz-Signature=3a99a35c23a964c6fd33b8a7cafe56c386abc089d397f94fde9b332a061ece01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
