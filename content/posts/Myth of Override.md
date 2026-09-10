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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RHJWAJP%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T064623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1mv6N55jrn9INlAMAPVc4wOJg%2FukuPmQqbNkl6mp%2B%2BAiBk4UfGYhzakvd5XpwMZwlKFPs8E1P8YoZkn4vBDoAIEyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMqjoDDahgnKWk7BDvKtwDP7RZL3bhNHO8xeAUu5%2B%2BsVCu1Bzx%2B0i5Vpe3j%2B68wphCT0A8GdaJZnpOQRQVjyQPrgcjATU03dDJGRab5mnNJkCuc%2BdRXX6X5a8U6HFGxmWtq7Dm6A3i6NuIWSvq8psYs1V%2Fi0diQJHl8%2F2VB%2FEOLLL0V7V1Zxfiia5pHFj30yiuYgHKqY17R68ru%2F5TSgdFyXH57qKGw7LhzBwIqkCu9ByMwvfmiwLgdXahvqyk8ID7moxLfbc5pREPK9w21SZhxe5c%2BRx%2BNFc5ugULb47K2fmqYCj8HmfqS4xD2kn3v%2FFtfH21MpdjEEGuREzwhmfz6pIXUX%2B6gERlsBWBRvgXjTug2glgjj%2Fl68OAbRB%2Fk1YBmRt0eSjtL%2Bhzmk6fj63rEinRgGp%2BEqwWL96SlIsc73iH9CVJP%2FJSIcHapiw9k8uvFkDexFdgI7uBLZ0zwERtuFaWwHsTvnTSDtQiUy9sKbzRDdfgLlxOmHG6ltoTkIDX6elbmkw4oy4GFSCUxfbYYaW9aObh6jTUlUGiP9ktwY61O0pzEx1EgOfkuFQDoqBHLfsedvDMZM2RK1W1ohNWCEkZ5FpULNlQaPOZ7ZDz3JFRi7ZkVVDYyxHXcrHUqrkKV7Lb4mlJNsRcC38w8vGI1QY6pgHSbo%2Fj8xDBS9Q0r0gxR8VIOwtkNeWG65FRbuYPASO1R7G8Rn2gAAche%2BXQPAM6sMjatGL7BIkwCo3UaeTY71vM%2BJXiAtwiFzpN%2FZh5RBq2RIMf0YEYeaf1SueRWtdLoJnATnQ%2BfICQLf2Api7F6bW2A44YeFLPLCZqzMzHMeZ8RY%2F2Hl6gja9XC5z2nHMUGkngtUYv05y%2Fk7DHSuFAlktKFkJe1gYw&X-Amz-Signature=1f1ec2ca41f9c54e03276b0adb2376d2161a64b456f3b37bdad6dd459aab06b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RHJWAJP%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T064623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1mv6N55jrn9INlAMAPVc4wOJg%2FukuPmQqbNkl6mp%2B%2BAiBk4UfGYhzakvd5XpwMZwlKFPs8E1P8YoZkn4vBDoAIEyr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMqjoDDahgnKWk7BDvKtwDP7RZL3bhNHO8xeAUu5%2B%2BsVCu1Bzx%2B0i5Vpe3j%2B68wphCT0A8GdaJZnpOQRQVjyQPrgcjATU03dDJGRab5mnNJkCuc%2BdRXX6X5a8U6HFGxmWtq7Dm6A3i6NuIWSvq8psYs1V%2Fi0diQJHl8%2F2VB%2FEOLLL0V7V1Zxfiia5pHFj30yiuYgHKqY17R68ru%2F5TSgdFyXH57qKGw7LhzBwIqkCu9ByMwvfmiwLgdXahvqyk8ID7moxLfbc5pREPK9w21SZhxe5c%2BRx%2BNFc5ugULb47K2fmqYCj8HmfqS4xD2kn3v%2FFtfH21MpdjEEGuREzwhmfz6pIXUX%2B6gERlsBWBRvgXjTug2glgjj%2Fl68OAbRB%2Fk1YBmRt0eSjtL%2Bhzmk6fj63rEinRgGp%2BEqwWL96SlIsc73iH9CVJP%2FJSIcHapiw9k8uvFkDexFdgI7uBLZ0zwERtuFaWwHsTvnTSDtQiUy9sKbzRDdfgLlxOmHG6ltoTkIDX6elbmkw4oy4GFSCUxfbYYaW9aObh6jTUlUGiP9ktwY61O0pzEx1EgOfkuFQDoqBHLfsedvDMZM2RK1W1ohNWCEkZ5FpULNlQaPOZ7ZDz3JFRi7ZkVVDYyxHXcrHUqrkKV7Lb4mlJNsRcC38w8vGI1QY6pgHSbo%2Fj8xDBS9Q0r0gxR8VIOwtkNeWG65FRbuYPASO1R7G8Rn2gAAche%2BXQPAM6sMjatGL7BIkwCo3UaeTY71vM%2BJXiAtwiFzpN%2FZh5RBq2RIMf0YEYeaf1SueRWtdLoJnATnQ%2BfICQLf2Api7F6bW2A44YeFLPLCZqzMzHMeZ8RY%2F2Hl6gja9XC5z2nHMUGkngtUYv05y%2Fk7DHSuFAlktKFkJe1gYw&X-Amz-Signature=3c77e9395993b4ae7b4db213e868ffdecfb89ef27a1a88cbe84a5bc4528e7186&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
