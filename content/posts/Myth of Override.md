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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CI3GOPD%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T234308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8zeY5f1cBfJXAsViFWJvYQPgxt81M7wgZRkl28L7MlAiB7BFLXyCupyRvLC92jVQ%2BZgI2uezi3x1tS9%2Fv%2BgBvnVSr%2FAwhOEAAaDDYzNzQyMzE4MzgwNSIMKb1gy4Kj0wCmdQlFKtwDipwZ%2BOvC7cmb8D0riNCf8i8%2FZdicXYY0407CkJ4uZqypMzzARQf9ATy%2BU%2Fq48kTkUm3ASQ%2Fsf4TW7729Qj3mh775O0f7HxkiK8SW8aXicMG0DWuvUjO6aUcVLj1VCsdvPi7hcL2tXbXME5xPSRR20G1b8tz4Kogx9pQ9bWZaNG3p6NbeLlH9xq7t1P93tXu6x8sNp4aIZYHr301F7eyRkaDNy7N27RR3yOFigk0TbhFFUJEGUwVgglTZIGo67cwqxne1K4KMTAw15lJwLWV8MgSLtShu75Ybk8xSnADdQzamGPdtQUmI%2F51Td6HUlv6wI0KOr2FCatopErjaaCY9eQMfUZGMK1wCMbPkpEGO4zBnIfzIHsg3cG6fTe56Dg1WfX7Rti7qYBksx5JEFEyerA%2F1SlOEAu9bR4eR0D2LeiHHRGHpFqfv0NF7ESqbUKrCiBgUhmMU7PuMg%2FzJwYDct%2FN8RvALdtcv8BMC1%2BCztYYKWnGHhGNIdZfN980nupQKYeaRtQlErNJPfzkz%2FkBwAX3eBsr8G2gSe0GTyfPa6oLWH%2FicMVCVXBrDdYYOPNqcT8nGA59wHjrK2x4cX9SUPLA3aGT0TBQt22XcnUhOVo4eO3E5aBZvLagfuPowxMa21QY6pgEJXtq1ZiLjKkY7aWuagk0am9NFu8satbJO5z27TDGOglvAXGytgFtp5izs4hEXWHq6M0NKOVILiVWHm9ocKewCATBhx0%2FHaxldMc4OVqXLV6Dud9MPwCAYTjWiIuJN7KZmK0gvwmfcVyTgWkrvtufJ4HVoPcbDScOK%2BffiSGDb6WPsz4O6S70oyvrlNlQHfgpArJUXFXAq5njLq6qEk5qlIjcaRSL8&X-Amz-Signature=5798abf73685ca4a41c6dc783e884515b31345bffde04468693c5dd7e8953eb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CI3GOPD%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T234308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8zeY5f1cBfJXAsViFWJvYQPgxt81M7wgZRkl28L7MlAiB7BFLXyCupyRvLC92jVQ%2BZgI2uezi3x1tS9%2Fv%2BgBvnVSr%2FAwhOEAAaDDYzNzQyMzE4MzgwNSIMKb1gy4Kj0wCmdQlFKtwDipwZ%2BOvC7cmb8D0riNCf8i8%2FZdicXYY0407CkJ4uZqypMzzARQf9ATy%2BU%2Fq48kTkUm3ASQ%2Fsf4TW7729Qj3mh775O0f7HxkiK8SW8aXicMG0DWuvUjO6aUcVLj1VCsdvPi7hcL2tXbXME5xPSRR20G1b8tz4Kogx9pQ9bWZaNG3p6NbeLlH9xq7t1P93tXu6x8sNp4aIZYHr301F7eyRkaDNy7N27RR3yOFigk0TbhFFUJEGUwVgglTZIGo67cwqxne1K4KMTAw15lJwLWV8MgSLtShu75Ybk8xSnADdQzamGPdtQUmI%2F51Td6HUlv6wI0KOr2FCatopErjaaCY9eQMfUZGMK1wCMbPkpEGO4zBnIfzIHsg3cG6fTe56Dg1WfX7Rti7qYBksx5JEFEyerA%2F1SlOEAu9bR4eR0D2LeiHHRGHpFqfv0NF7ESqbUKrCiBgUhmMU7PuMg%2FzJwYDct%2FN8RvALdtcv8BMC1%2BCztYYKWnGHhGNIdZfN980nupQKYeaRtQlErNJPfzkz%2FkBwAX3eBsr8G2gSe0GTyfPa6oLWH%2FicMVCVXBrDdYYOPNqcT8nGA59wHjrK2x4cX9SUPLA3aGT0TBQt22XcnUhOVo4eO3E5aBZvLagfuPowxMa21QY6pgEJXtq1ZiLjKkY7aWuagk0am9NFu8satbJO5z27TDGOglvAXGytgFtp5izs4hEXWHq6M0NKOVILiVWHm9ocKewCATBhx0%2FHaxldMc4OVqXLV6Dud9MPwCAYTjWiIuJN7KZmK0gvwmfcVyTgWkrvtufJ4HVoPcbDScOK%2BffiSGDb6WPsz4O6S70oyvrlNlQHfgpArJUXFXAq5njLq6qEk5qlIjcaRSL8&X-Amz-Signature=6d421a79140259c988103123bf4aff4b2839bf56387083a9718128c78607cadf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
