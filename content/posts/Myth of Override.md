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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VHXCVAC%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T230445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIAejDCyC98YFprTgnQ2%2Boekmzr7uYi92t83D0A3jtPqBAiEA5lma0NYPd%2FoofZ9pG2noX3Mx74wPH5BBjoOmx5UIDAYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCXl3AoPeYw7zfKY6CrcA%2FrDqmS5ShEeY0LQjHRizDaiAHqYuVfkm1f9kwnWmPdlCnbwKo2Wj9Mmfyk4AOZ5ON39XAhI2Yq0sZh4D1IYbofaxiFK%2FrAWV2Mf28SHQT7ISb8A64Qokrw9aUVPjx%2FczXyiOe1%2BSSB20CS3iblR7CL6EJM7hK%2F9jtHu6zE99s7fONURrozR%2B1hwx6VHo9r8Gkuj3cU7kzUfAaQgJsctXaeCdWc58wjr8dhce5XvfxA01CjjFxVrVPT2WAo1qfy6faRMfbyw9DUDAPUCqUNz5F8MW10DYRhkTZn5DulBWt58oWld42sdtVHS%2BwY7WsRI%2B3%2Fn7Eq3rUiJfvqinv%2BCQ9Zgo%2FbQQf7qziW4POzo%2BeiugmT8vMiLf3OmTfLhb5%2FW3Y6CZJU8sMIFy%2BgQMTuuBHapn6gFeY6bkwqZ69pJMJnoaHeu8p60O2UpocLFd6Mff0eU5rakYOibhCaGURNWl7NDb5VSHRQ0Cm2nUTybXfXaEZqcmD8khYsUj7iWbkdUkuEYJmYq6fwGuYCEdRAOMg10xLicJJlQRfHJIv1%2BEVQu%2BCp7t35D4x9GRglrsRKbyndawMrhjmAOWejEvcULiyJ9o%2BRpIhkhF1bmTS1sWVS1%2BUlTnDWLn%2F2kk0HEMNDtuNAGOqUBwlR2DVdtGGrrt4ve5u6EBF8Bv1ah2hMhUzJhmzVeDf28fl5mEoWWsS%2FzWBlax4%2Fw%2BdXKfmx7B2bfP6fPgMrs7Yw71QXlwqXRxUUHt2LSr5jLh98mWlsV37k13UuWAKzugfOyj7sGx4bE79AGPWzP5xc1e9kfZaKb%2F6jee1KdRGzYVwAbGH%2Bhe6%2FKJOPc8omBfCoqWk846nAfpOAps8TCjq61T%2Bnt&X-Amz-Signature=e87823272aaf159157890b6b8d0275de14a21e3c12c6f4da8d7d9d08c543bff7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VHXCVAC%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T230445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIAejDCyC98YFprTgnQ2%2Boekmzr7uYi92t83D0A3jtPqBAiEA5lma0NYPd%2FoofZ9pG2noX3Mx74wPH5BBjoOmx5UIDAYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCXl3AoPeYw7zfKY6CrcA%2FrDqmS5ShEeY0LQjHRizDaiAHqYuVfkm1f9kwnWmPdlCnbwKo2Wj9Mmfyk4AOZ5ON39XAhI2Yq0sZh4D1IYbofaxiFK%2FrAWV2Mf28SHQT7ISb8A64Qokrw9aUVPjx%2FczXyiOe1%2BSSB20CS3iblR7CL6EJM7hK%2F9jtHu6zE99s7fONURrozR%2B1hwx6VHo9r8Gkuj3cU7kzUfAaQgJsctXaeCdWc58wjr8dhce5XvfxA01CjjFxVrVPT2WAo1qfy6faRMfbyw9DUDAPUCqUNz5F8MW10DYRhkTZn5DulBWt58oWld42sdtVHS%2BwY7WsRI%2B3%2Fn7Eq3rUiJfvqinv%2BCQ9Zgo%2FbQQf7qziW4POzo%2BeiugmT8vMiLf3OmTfLhb5%2FW3Y6CZJU8sMIFy%2BgQMTuuBHapn6gFeY6bkwqZ69pJMJnoaHeu8p60O2UpocLFd6Mff0eU5rakYOibhCaGURNWl7NDb5VSHRQ0Cm2nUTybXfXaEZqcmD8khYsUj7iWbkdUkuEYJmYq6fwGuYCEdRAOMg10xLicJJlQRfHJIv1%2BEVQu%2BCp7t35D4x9GRglrsRKbyndawMrhjmAOWejEvcULiyJ9o%2BRpIhkhF1bmTS1sWVS1%2BUlTnDWLn%2F2kk0HEMNDtuNAGOqUBwlR2DVdtGGrrt4ve5u6EBF8Bv1ah2hMhUzJhmzVeDf28fl5mEoWWsS%2FzWBlax4%2Fw%2BdXKfmx7B2bfP6fPgMrs7Yw71QXlwqXRxUUHt2LSr5jLh98mWlsV37k13UuWAKzugfOyj7sGx4bE79AGPWzP5xc1e9kfZaKb%2F6jee1KdRGzYVwAbGH%2Bhe6%2FKJOPc8omBfCoqWk846nAfpOAps8TCjq61T%2Bnt&X-Amz-Signature=bb0555d4c1ff136b27a2b6b1d95a4187337609878f8d5243f8954bbeb2791fa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
