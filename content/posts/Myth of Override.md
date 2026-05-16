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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FLZ5EJ4%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T092024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUj5uCaprruyVSj%2FY05depfdfsARl5YKHYWwaZT6FhtAiAbVa5Ao1pWAIHq0a%2FEAVHG%2FK1D1b%2BmC0kdyP4b3vsvgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVN991L6QV550O8%2F4KtwDtDMnZ36xzfCci73%2BWOrbLhTzwrWi0kkJBJHXxwO4JLWOI%2BPvt6wEQKxVLOqkoKc7vFY%2B9ij4bpSAxE3mywynSxU1C7dN56j5Ar1Uku0%2FO5cN%2BPo0rvCYDXWtLFMz51XSy1FNAPbSpr4EMZmY9urURNA%2B7nrH60bozjQDtVBRzYzYGOnf6Ef%2FCBbA6MqSswNJuyYYD%2BhazDaNgKXDAK7a%2FNYyaxioKNgvKJtd6JVhJ0cGbCeYWJ3Q71Tmv%2F5QKSg5MYY3q1pd5ZLvxEGdeMVx%2BWtb0DEDEiPLBf0dhBuOl8aPJ5KoQMnifU%2FzN8CDTVPwnSROKc8iVMvey5765v5YGcedr5ockzj1PdpR8idRPxMD8jk0SP0JaEDZAh0pSHg%2FSF4keBQTcfV51BYLtiOzZNRv0RkdWu5agc4pYcdpx97S39ot9Ml9C3cWSkiuOzYCiGGL4DK%2FE9fkiwaOJzUS1oGA6fkbCADKv95MlXIGSqscZVAK8LS4r%2BbdFOyQMBrtKrsahghxlvXlIXseTUvpNzyXtiehwuSh8StfHvpDrhCfIh4FAZPj%2FDZJcHd6ZJljqwrXnxY7jjhk0C1FsTNAjexUVuGwBGXeAy7I7H3R%2BMhED2YVXeB4%2BSmnvV0w9Omg0AY6pgFvkZxlhh1Im4CleGU7UOSbdrhPcbk6G8TxgH7IA6jWU0KZOURoE25dVCWBl2cyZSuHb0RxxGoxKl3TnGAqp6shqfXri3NtCUM765XhwlSrZIhysHYgobE7TvOgEdbNWfR8gSNqy0L1Avb0ODnNSM3Q81aB42iskKsu85%2BLq1ygX8kIKfdZBVvPV5nGxKTWn4Jdfnj1kmWF5F0PcuBxmROLVjLmms%2FC&X-Amz-Signature=b21b7f9bc654ca9d51969443aec07b49a461d2333311f54e57779970f4bea66f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FLZ5EJ4%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T092025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUj5uCaprruyVSj%2FY05depfdfsARl5YKHYWwaZT6FhtAiAbVa5Ao1pWAIHq0a%2FEAVHG%2FK1D1b%2BmC0kdyP4b3vsvgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVN991L6QV550O8%2F4KtwDtDMnZ36xzfCci73%2BWOrbLhTzwrWi0kkJBJHXxwO4JLWOI%2BPvt6wEQKxVLOqkoKc7vFY%2B9ij4bpSAxE3mywynSxU1C7dN56j5Ar1Uku0%2FO5cN%2BPo0rvCYDXWtLFMz51XSy1FNAPbSpr4EMZmY9urURNA%2B7nrH60bozjQDtVBRzYzYGOnf6Ef%2FCBbA6MqSswNJuyYYD%2BhazDaNgKXDAK7a%2FNYyaxioKNgvKJtd6JVhJ0cGbCeYWJ3Q71Tmv%2F5QKSg5MYY3q1pd5ZLvxEGdeMVx%2BWtb0DEDEiPLBf0dhBuOl8aPJ5KoQMnifU%2FzN8CDTVPwnSROKc8iVMvey5765v5YGcedr5ockzj1PdpR8idRPxMD8jk0SP0JaEDZAh0pSHg%2FSF4keBQTcfV51BYLtiOzZNRv0RkdWu5agc4pYcdpx97S39ot9Ml9C3cWSkiuOzYCiGGL4DK%2FE9fkiwaOJzUS1oGA6fkbCADKv95MlXIGSqscZVAK8LS4r%2BbdFOyQMBrtKrsahghxlvXlIXseTUvpNzyXtiehwuSh8StfHvpDrhCfIh4FAZPj%2FDZJcHd6ZJljqwrXnxY7jjhk0C1FsTNAjexUVuGwBGXeAy7I7H3R%2BMhED2YVXeB4%2BSmnvV0w9Omg0AY6pgFvkZxlhh1Im4CleGU7UOSbdrhPcbk6G8TxgH7IA6jWU0KZOURoE25dVCWBl2cyZSuHb0RxxGoxKl3TnGAqp6shqfXri3NtCUM765XhwlSrZIhysHYgobE7TvOgEdbNWfR8gSNqy0L1Avb0ODnNSM3Q81aB42iskKsu85%2BLq1ygX8kIKfdZBVvPV5nGxKTWn4Jdfnj1kmWF5F0PcuBxmROLVjLmms%2FC&X-Amz-Signature=f4b569d86906ea73b81c636ba02f2d75177aa4fc68301dc40f7d8fe9d4ff3c77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
