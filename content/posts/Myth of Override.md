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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNDUCXBK%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T192722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8fpVG%2BaMPx7%2B6Gdj9LGJpBeN6xTf1isvql0Ytl8LoLAiBVFrCNMqAr4p0AfnnQlGVC7CZ1JEozmSlDEGeTPon8gyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMcd0F%2FYQUNUGe7FCcKtwDeXq3g5CRHn%2F7Bomc64AgvFGyJkjn504XGVE7gGXYK8OWTzjLbLBy%2BvbvJ1ZH%2FtEmnB0m%2FP22W9oet3tpHr04rgMQ5C8bB3dXhJmkHWH7VqtnuPub%2BUEjiqSCNyz%2BnWqX9Io1Cc8QNGS%2ByEi%2FZmDU8zavBlesXY4bECkdaJwrnXleS%2FP7PCBRV%2FFlv8jscmPIpV%2F6muyzakHMdDM0EuYTt8mKOGTex2cELsdZ3xfJXnfJ%2BdhsOlV5kgiCm16INdDwT1u4LeoYSw6MHmbVJV2YK2KnitQ82CQjMSedhclm8vpqFfCoGxW1bY3mQUk8%2FoidED2s1njByOye8wgENmEKqqnrByjRoFNw2uU6OPMdtfHcDvdc3fM851EoZd2Yz635QfJAu5zaPgt8rncnZBU6pwXBhYjIyrr0wx%2Bx9%2Bpc91RXva9b9wtQ5Ok1yAmFEUyeenSb9rY5kbl7ppGFvf%2F11Smi%2B0enazWZwBheO3oAm28PQbJ4Zni%2Fyrd5oQj8JurIAwO4eM6uAzOtmNaxU3qGZIJLldm2R5lzpKJBzVy6OtGpxV%2BkVEPmky%2B0oHsbGKLU9htionO4dZ4OAoie05Y%2FffwxdXkE4jLzbYyNB1sDeJ0mecN1LZv4kWXeL%2BYw2qbG0QY6pgHJ7BuapTwodMpWrAAKI5NfZqyI5U6VF3j7uW3UMcHS6rFnRuvdUrX82VTeywqv%2Bw9t3eS1a2iLHVPtym2Jo0tUOmAD%2FRrUoQVV6ThSZPTCtcCPiwnmkY77bJs4EZCaIWbriJ3SJbzcNxCfb4E3dzvKKLi%2FLqyCa33bXbAc3gmhhjPMw1aF%2BOgrkl85KTl%2BkOMAA7PCU0COFzn%2BVSEtapPTDbEPxz6X&X-Amz-Signature=403f05cfc6645ad87ee4af08a96075899d61783453ab9daf4dff65c0705a3187&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNDUCXBK%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T192722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8fpVG%2BaMPx7%2B6Gdj9LGJpBeN6xTf1isvql0Ytl8LoLAiBVFrCNMqAr4p0AfnnQlGVC7CZ1JEozmSlDEGeTPon8gyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMcd0F%2FYQUNUGe7FCcKtwDeXq3g5CRHn%2F7Bomc64AgvFGyJkjn504XGVE7gGXYK8OWTzjLbLBy%2BvbvJ1ZH%2FtEmnB0m%2FP22W9oet3tpHr04rgMQ5C8bB3dXhJmkHWH7VqtnuPub%2BUEjiqSCNyz%2BnWqX9Io1Cc8QNGS%2ByEi%2FZmDU8zavBlesXY4bECkdaJwrnXleS%2FP7PCBRV%2FFlv8jscmPIpV%2F6muyzakHMdDM0EuYTt8mKOGTex2cELsdZ3xfJXnfJ%2BdhsOlV5kgiCm16INdDwT1u4LeoYSw6MHmbVJV2YK2KnitQ82CQjMSedhclm8vpqFfCoGxW1bY3mQUk8%2FoidED2s1njByOye8wgENmEKqqnrByjRoFNw2uU6OPMdtfHcDvdc3fM851EoZd2Yz635QfJAu5zaPgt8rncnZBU6pwXBhYjIyrr0wx%2Bx9%2Bpc91RXva9b9wtQ5Ok1yAmFEUyeenSb9rY5kbl7ppGFvf%2F11Smi%2B0enazWZwBheO3oAm28PQbJ4Zni%2Fyrd5oQj8JurIAwO4eM6uAzOtmNaxU3qGZIJLldm2R5lzpKJBzVy6OtGpxV%2BkVEPmky%2B0oHsbGKLU9htionO4dZ4OAoie05Y%2FffwxdXkE4jLzbYyNB1sDeJ0mecN1LZv4kWXeL%2BYw2qbG0QY6pgHJ7BuapTwodMpWrAAKI5NfZqyI5U6VF3j7uW3UMcHS6rFnRuvdUrX82VTeywqv%2Bw9t3eS1a2iLHVPtym2Jo0tUOmAD%2FRrUoQVV6ThSZPTCtcCPiwnmkY77bJs4EZCaIWbriJ3SJbzcNxCfb4E3dzvKKLi%2FLqyCa33bXbAc3gmhhjPMw1aF%2BOgrkl85KTl%2BkOMAA7PCU0COFzn%2BVSEtapPTDbEPxz6X&X-Amz-Signature=8e35f05c72c516b1a1d7be86ed480522f7d2da00cb2ae3e8c96b39d3dc22869b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
