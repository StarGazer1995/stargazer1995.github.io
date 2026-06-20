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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN7APIVO%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T171500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIERJbL%2FigSzC2vo77RbG8rnQPaa5%2FVOEayN%2FXC9BN%2BLuAiBcPvbfM%2BOWeGG0isLggTD%2FqnIJANr3L3wCFU%2Bm2qgBwSqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG88reqITL%2BMWIRrgKtwD9vH8Ls7%2BaNIyw1Mzz44WNnP7yg%2FJQ5m%2FgTt6x1cUcW%2FBhEDVx7cHAPZiUhzoQCmDpyHs0gaIVJMZ8mS6P6yOkfjuSJmszru7sfzIlo0Qd9uR8yrtmU%2FNWw6%2BeSJcDiYKvfSa8U32Lxs9KWOr5J6A0VSKkAaXetnEZOTl%2FYcT1XJxs%2FLMeK8DwRPXM%2BM7LJlSirpKmvZkEagZt5T5O6B%2FJZWRNf4JH5yD3LDrH1ec0TElWiRs32EMqmIsmtOUF%2F0wILKrkaITeavuDcH0F%2FTDYSQbNR1ECkrlwh3vemh9bbwI29aKoeA7ExWUD9e2BoMUIJaNLyweY%2FKM5tVPI4I%2FIQSqg%2Bwk2Sa8amufwH9PKCJ4MXGr9SR4DJL4NF4nJJJL%2BoorLyBMInEr6GvAmF2xw1FhpFkFXfv1LgId4K8ErTlRjc17sDDcjm1dC6jRydRFSC00J5g1W22x%2BsZWJhHwAatfOFogeM6t4Tf2%2Fvj9jloZ74vdGEXPZdJUlXX3kSt%2FWczUEr2BIzu45xUceG3VzLynxl0o%2BYsTi0ownyjnHqDSntKVeAGpWF4tjCARomVyD0j80iZVarpRop8n1tLZAmHARYRqR8TSUoMPseEb7tA6uiMiAIh6EadT7v0wz4zb0QY6pgE%2B1lBWfA2AofEijcfU%2B6XuVMX6YZHOwXbhgNkNjVEg9%2BROXRpo2eJBrvBRQexHQjcoGWWm2CC4jsep2KU%2BuV0tzqO%2BB6IRTl8QoVzzrlpWcBh1lvZrLn3gJpMoUMmncIF%2BSAFoSYra%2F%2BV9jBW8o5tS3bTLdnDr%2BaHRD8AQFog3nUZdP14ForhTXbNJfNz%2Bmu24wJPZ0tv0rdMt%2BuuClLgVg%2BZXIQAY&X-Amz-Signature=7f86bc7dbdbbddbaff34b0188b0a3c420635406347d4fc2f8d63f13a2a8b4a9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN7APIVO%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T171500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIERJbL%2FigSzC2vo77RbG8rnQPaa5%2FVOEayN%2FXC9BN%2BLuAiBcPvbfM%2BOWeGG0isLggTD%2FqnIJANr3L3wCFU%2Bm2qgBwSqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG88reqITL%2BMWIRrgKtwD9vH8Ls7%2BaNIyw1Mzz44WNnP7yg%2FJQ5m%2FgTt6x1cUcW%2FBhEDVx7cHAPZiUhzoQCmDpyHs0gaIVJMZ8mS6P6yOkfjuSJmszru7sfzIlo0Qd9uR8yrtmU%2FNWw6%2BeSJcDiYKvfSa8U32Lxs9KWOr5J6A0VSKkAaXetnEZOTl%2FYcT1XJxs%2FLMeK8DwRPXM%2BM7LJlSirpKmvZkEagZt5T5O6B%2FJZWRNf4JH5yD3LDrH1ec0TElWiRs32EMqmIsmtOUF%2F0wILKrkaITeavuDcH0F%2FTDYSQbNR1ECkrlwh3vemh9bbwI29aKoeA7ExWUD9e2BoMUIJaNLyweY%2FKM5tVPI4I%2FIQSqg%2Bwk2Sa8amufwH9PKCJ4MXGr9SR4DJL4NF4nJJJL%2BoorLyBMInEr6GvAmF2xw1FhpFkFXfv1LgId4K8ErTlRjc17sDDcjm1dC6jRydRFSC00J5g1W22x%2BsZWJhHwAatfOFogeM6t4Tf2%2Fvj9jloZ74vdGEXPZdJUlXX3kSt%2FWczUEr2BIzu45xUceG3VzLynxl0o%2BYsTi0ownyjnHqDSntKVeAGpWF4tjCARomVyD0j80iZVarpRop8n1tLZAmHARYRqR8TSUoMPseEb7tA6uiMiAIh6EadT7v0wz4zb0QY6pgE%2B1lBWfA2AofEijcfU%2B6XuVMX6YZHOwXbhgNkNjVEg9%2BROXRpo2eJBrvBRQexHQjcoGWWm2CC4jsep2KU%2BuV0tzqO%2BB6IRTl8QoVzzrlpWcBh1lvZrLn3gJpMoUMmncIF%2BSAFoSYra%2F%2BV9jBW8o5tS3bTLdnDr%2BaHRD8AQFog3nUZdP14ForhTXbNJfNz%2Bmu24wJPZ0tv0rdMt%2BuuClLgVg%2BZXIQAY&X-Amz-Signature=137dcf7d30a779ac422223496f02a300a8ac03fc6c00c94cd8cfa3685e397aa5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
