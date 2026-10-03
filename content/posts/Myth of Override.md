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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KX2M6IM%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T071254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWnoAOVm58bAHpNElYK5he44XLwawLQNJxEfRws%2BmEyAIhANe36dezNt7LnUnvW9Dn9MpZBSYqtbKRKxufhL4zn%2BZxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FgMQYwM0MUOUFzSwq3APRZqdhYI1nVOqAg9nrx3a9imjZgKrFyl58OhxrvU3d32lrqpOgDpqgPDb5gwLHz7yuIFaP7T0FqlLn4yU7XHK5iVhve8BE1DjINW6XEKZpODA%2FwpA%2FJKP%2BZQ2Kp%2Bdb50Y3Ch3cgupWGOFu16DUaQ4hISOeehZ52KD3rqXEYFxwXyIX8Ylxw09jHbWbFUEHExfJv7z6VYxhME8L4P21MMh6b0XEcqG46F%2Be%2Ftuofw5DKscDr%2B%2FyZiWk8G5EDkGAvT%2BJ70QJ9Crp3w5kaGpSo9uezmXcnzuaHRZqq%2FmSfHXL3zyDgf1%2B3vv5hisefCyyazkl%2BNt6gN1P7tYDcZDgzb7Ueye1kLRBHdaLqGWLGpS5SY0bLaixCxf%2BriQk5eUkOGOPfMHu9q0pQlRHjg%2BUzuqfCqNd8y0vOQ0z7OhtOcyeDRTYmq7VyTWlZMydmDVHjp6qISKyA4y3wpya2QDMvHRxT1z6MnEN3%2FgS8Cp8HjlHqOXcRFPBwapqphwTrsM98SGfer5UaylsLS%2BImJG%2F%2BYvrRyas58ahJfUj6ZhYQ2sSMLZRHbYN%2B%2F9d6p37%2Bp%2FStZBM5HyMLzScoDnYxsdeIsBsNxYtm1%2BG2iI7uBZdQ9nU5QemrX5KXzXIPUPpnDCivoLWBjqkAX5lwzaAHcXD0O4akVVC%2FfhT%2FGwN8W4IbCVOzDPNMShroqZkMTJQPaAXDfh%2BHznur0AoQWIo8l627GgI5Dc%2Baefdu%2Fw1ray3blrtkssfNqmL6NKZ%2FLn6K7pgsYg6eH5Mds59%2B4G%2FzT6wNdpoNCmziBPjjXIABAowZSGaCR8thUK%2BX4B%2B%2FfhSEekHpZ3IGHXbMlx3YY7Su7SM4BHm9J71uxvqJqeS&X-Amz-Signature=dd36fe1c626bf8456d29f67a134e49a40f4b1186f17bb278a810c0c33f24f432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KX2M6IM%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T071254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWnoAOVm58bAHpNElYK5he44XLwawLQNJxEfRws%2BmEyAIhANe36dezNt7LnUnvW9Dn9MpZBSYqtbKRKxufhL4zn%2BZxKogECKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FgMQYwM0MUOUFzSwq3APRZqdhYI1nVOqAg9nrx3a9imjZgKrFyl58OhxrvU3d32lrqpOgDpqgPDb5gwLHz7yuIFaP7T0FqlLn4yU7XHK5iVhve8BE1DjINW6XEKZpODA%2FwpA%2FJKP%2BZQ2Kp%2Bdb50Y3Ch3cgupWGOFu16DUaQ4hISOeehZ52KD3rqXEYFxwXyIX8Ylxw09jHbWbFUEHExfJv7z6VYxhME8L4P21MMh6b0XEcqG46F%2Be%2Ftuofw5DKscDr%2B%2FyZiWk8G5EDkGAvT%2BJ70QJ9Crp3w5kaGpSo9uezmXcnzuaHRZqq%2FmSfHXL3zyDgf1%2B3vv5hisefCyyazkl%2BNt6gN1P7tYDcZDgzb7Ueye1kLRBHdaLqGWLGpS5SY0bLaixCxf%2BriQk5eUkOGOPfMHu9q0pQlRHjg%2BUzuqfCqNd8y0vOQ0z7OhtOcyeDRTYmq7VyTWlZMydmDVHjp6qISKyA4y3wpya2QDMvHRxT1z6MnEN3%2FgS8Cp8HjlHqOXcRFPBwapqphwTrsM98SGfer5UaylsLS%2BImJG%2F%2BYvrRyas58ahJfUj6ZhYQ2sSMLZRHbYN%2B%2F9d6p37%2Bp%2FStZBM5HyMLzScoDnYxsdeIsBsNxYtm1%2BG2iI7uBZdQ9nU5QemrX5KXzXIPUPpnDCivoLWBjqkAX5lwzaAHcXD0O4akVVC%2FfhT%2FGwN8W4IbCVOzDPNMShroqZkMTJQPaAXDfh%2BHznur0AoQWIo8l627GgI5Dc%2Baefdu%2Fw1ray3blrtkssfNqmL6NKZ%2FLn6K7pgsYg6eH5Mds59%2B4G%2FzT6wNdpoNCmziBPjjXIABAowZSGaCR8thUK%2BX4B%2B%2FfhSEekHpZ3IGHXbMlx3YY7Su7SM4BHm9J71uxvqJqeS&X-Amz-Signature=8776a3f8c6aceb5e1f0bc889c83a9058e0ce574d72a9fd5742751c23fa03003a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
