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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6OKI5FS%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T142307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTRKEBk9ZnWVbHUkRN0rL73ugVrW1JndBz79f%2FmOv%2BfwIhANoQuV%2FzhJ7a5%2FY7L3lVs3zmU0a7oO3fziAUaUTk8UdPKv8DCF4QABoMNjM3NDIzMTgzODA1IgzcgYolX3rdhxS6%2ByAq3APetrqqi7mH4dhwVNJm%2B1vNWPwcLV6kfHyltNRi3SDalRiQjcWTd5tac5KnuKY68apAx8v4AFz4CSFcFkD%2B2Eg5Fkm%2BJC8c43fAwDVfZJPBzmDccgi50WD3%2FCO74IBu%2F2NKROZzj56WN8lC272%2BlG6IZB%2FitVhdPO1fDQsO6oWoGRHoUSU%2FRy40a4FNnTn1MtJdaKcAg7PNFfMPozkbkKDuEbbhVWKRHZw3MndYefqidzyvhypomWQyv3Y8RWJ53hnQfnj7aeqdLhcxwMXRDaT%2BP%2FooI2d4qDc43tmeqjm6iPyu%2FpGjfhKaZEsX%2BdwTuxeUhoBA5xSZkXzDfTze8srq36DVpZ%2F8bxGcaI7wIjfKXkA0ov7GNGx7bz6g8KAkx0XMopMGk1n%2Fgnl232O1M08ruscMMMiv%2By2Y9G8G57N7GOYSuGOnZf5XninN0QnFleY%2FMMEd8v7TY%2F2RnfxNOi%2FbY8TdUSvQ0a%2F9e%2FPi%2Bfav1%2F12X4dpNJrKR6PNzziuZ6Zi2zdCMKfLY79xoCFgIomyl7ohxrOhGxn2sGBaYHnhXO9t2xjrEUPwjtFzPOy20XAhFwFst4PHFgzKW5gQjwQ3vV1AY7y4bnwIObJXUu9m3I2cjHygRN3nHbctSDDet5HUBjqkAZhgWvAuHgs5r4cttKzMdOddRPW7JOTWWCinjYS4EZW3%2BHQGK2bZHwZlC66II7zaoEPwDzry9z4eHLR4DTkI7B3Qf4XodWIuIn1sYenGMZOVZfUuXX%2FWDbN7WCPeBYTOXgL1SkcK8AEp%2BryVqbSOQZC1mJSGzIJUSsKy1uRrNL4%2B8G%2BfgEQZM1URZLVfhtI3aZ8oDCr1Rrw09QUbg9vpQz8dV8my&X-Amz-Signature=2515bb912c53c708279145eca905b05684d2e648ff5f743a8a80a96abd627559&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6OKI5FS%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T142307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTRKEBk9ZnWVbHUkRN0rL73ugVrW1JndBz79f%2FmOv%2BfwIhANoQuV%2FzhJ7a5%2FY7L3lVs3zmU0a7oO3fziAUaUTk8UdPKv8DCF4QABoMNjM3NDIzMTgzODA1IgzcgYolX3rdhxS6%2ByAq3APetrqqi7mH4dhwVNJm%2B1vNWPwcLV6kfHyltNRi3SDalRiQjcWTd5tac5KnuKY68apAx8v4AFz4CSFcFkD%2B2Eg5Fkm%2BJC8c43fAwDVfZJPBzmDccgi50WD3%2FCO74IBu%2F2NKROZzj56WN8lC272%2BlG6IZB%2FitVhdPO1fDQsO6oWoGRHoUSU%2FRy40a4FNnTn1MtJdaKcAg7PNFfMPozkbkKDuEbbhVWKRHZw3MndYefqidzyvhypomWQyv3Y8RWJ53hnQfnj7aeqdLhcxwMXRDaT%2BP%2FooI2d4qDc43tmeqjm6iPyu%2FpGjfhKaZEsX%2BdwTuxeUhoBA5xSZkXzDfTze8srq36DVpZ%2F8bxGcaI7wIjfKXkA0ov7GNGx7bz6g8KAkx0XMopMGk1n%2Fgnl232O1M08ruscMMMiv%2By2Y9G8G57N7GOYSuGOnZf5XninN0QnFleY%2FMMEd8v7TY%2F2RnfxNOi%2FbY8TdUSvQ0a%2F9e%2FPi%2Bfav1%2F12X4dpNJrKR6PNzziuZ6Zi2zdCMKfLY79xoCFgIomyl7ohxrOhGxn2sGBaYHnhXO9t2xjrEUPwjtFzPOy20XAhFwFst4PHFgzKW5gQjwQ3vV1AY7y4bnwIObJXUu9m3I2cjHygRN3nHbctSDDet5HUBjqkAZhgWvAuHgs5r4cttKzMdOddRPW7JOTWWCinjYS4EZW3%2BHQGK2bZHwZlC66II7zaoEPwDzry9z4eHLR4DTkI7B3Qf4XodWIuIn1sYenGMZOVZfUuXX%2FWDbN7WCPeBYTOXgL1SkcK8AEp%2BryVqbSOQZC1mJSGzIJUSsKy1uRrNL4%2B8G%2BfgEQZM1URZLVfhtI3aZ8oDCr1Rrw09QUbg9vpQz8dV8my&X-Amz-Signature=247fe0bb9ace3bd7af84824e6d89b3b864e899e4c4b7e7bc77cab91c05530c51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
