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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDKSDKHE%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T080658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDG531Uz%2Be%2Bxcd1N9GG%2BCs4rL7UksLLyzhMZx37P8fesAIhAOU385DRPRkyRWRtQ9x8GhrmL3kTibvDt1ZkIWLQA809Kv8DCCAQABoMNjM3NDIzMTgzODA1Igysn%2Fk4qBbANu25I6Eq3AMcnp5HM2rhB%2BhjCVL0TsU0vKsKXdwgK2VvPuSGVYfHjs8qJ7kpsfM56Ltd0vt1smg0ElPeXxO02Yt0MIISuu0s2ZLQOFRgTyWScvweLWsgCLUs%2BM3ADMAXM%2FSrH6Qqa3L6rhzCgJn2zOvnokAH517igJnr9A%2FdWMDww6Wc9vOXTmsiWYO5tjC8InXZR%2FTuCnFGWFWLyklPUwd7KEgixJ5%2FVD7AVxKN6naR%2FJ3Lv1dqcK3ZxdwXmt4DqM%2FVRyCwi2SRwuHPWxzHH04IR8piDgcrQ4VkxNpMaykJTro2uPW2dVxp7c7ZKsrmO2bPz4isyGiY4JGbHC97LN%2FBlhay00Zof7%2BWLtCJVMciKGl1%2B6uZHTytgAUa3HOt7B08E%2BDKpj5w9aKF%2Bm3zz8Bp7GD6XFXbotvF7WQ61Lespf3YA1nZLoWT3XsfL0KbibbokdnlIPfh%2Btr2PnkaTfnvH3WvSMaH0UdqzIqYZ%2Fy56gfnnpHCnVnTvli3mVWj%2Fo%2BF9UXEgvP7vI6fwVEqYppKTzsisjxkPobRv3X3kZF1FMw8ek36xpjHNexChlOcMXM1cq%2FYfgWnNr7czD8rd3gwZiw9B0Onk9hizV3DY%2BTRsSgYpE%2FMtU35VX2KfjPUOWLWZTD7mJ3WBjqkAWM969I8rgZ5AOxEbtT1naoJHYX7FJxMr02ln%2Bjp33Hj0w3ruB7cBGRlZImvADYoIck3GHhGsUx1hQ0t9HBP6urkj2tOEaxPlIZyqe4W7nKJOqvSj92d905TTQuJbW0qDqtZwJXIZG8VWSLOq%2FDz32Wotq46XNuxZX1Uaorh30zYzpF%2Bk7d5X0LU05TXD50H8enKXPn1MmYQUpjFXDvOwEEYQ1Zv&X-Amz-Signature=1bccf67af0025023a567476e6dee59196299d6b64f90ce4d8e1eb780a68fe3fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDKSDKHE%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T080658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDG531Uz%2Be%2Bxcd1N9GG%2BCs4rL7UksLLyzhMZx37P8fesAIhAOU385DRPRkyRWRtQ9x8GhrmL3kTibvDt1ZkIWLQA809Kv8DCCAQABoMNjM3NDIzMTgzODA1Igysn%2Fk4qBbANu25I6Eq3AMcnp5HM2rhB%2BhjCVL0TsU0vKsKXdwgK2VvPuSGVYfHjs8qJ7kpsfM56Ltd0vt1smg0ElPeXxO02Yt0MIISuu0s2ZLQOFRgTyWScvweLWsgCLUs%2BM3ADMAXM%2FSrH6Qqa3L6rhzCgJn2zOvnokAH517igJnr9A%2FdWMDww6Wc9vOXTmsiWYO5tjC8InXZR%2FTuCnFGWFWLyklPUwd7KEgixJ5%2FVD7AVxKN6naR%2FJ3Lv1dqcK3ZxdwXmt4DqM%2FVRyCwi2SRwuHPWxzHH04IR8piDgcrQ4VkxNpMaykJTro2uPW2dVxp7c7ZKsrmO2bPz4isyGiY4JGbHC97LN%2FBlhay00Zof7%2BWLtCJVMciKGl1%2B6uZHTytgAUa3HOt7B08E%2BDKpj5w9aKF%2Bm3zz8Bp7GD6XFXbotvF7WQ61Lespf3YA1nZLoWT3XsfL0KbibbokdnlIPfh%2Btr2PnkaTfnvH3WvSMaH0UdqzIqYZ%2Fy56gfnnpHCnVnTvli3mVWj%2Fo%2BF9UXEgvP7vI6fwVEqYppKTzsisjxkPobRv3X3kZF1FMw8ek36xpjHNexChlOcMXM1cq%2FYfgWnNr7czD8rd3gwZiw9B0Onk9hizV3DY%2BTRsSgYpE%2FMtU35VX2KfjPUOWLWZTD7mJ3WBjqkAWM969I8rgZ5AOxEbtT1naoJHYX7FJxMr02ln%2Bjp33Hj0w3ruB7cBGRlZImvADYoIck3GHhGsUx1hQ0t9HBP6urkj2tOEaxPlIZyqe4W7nKJOqvSj92d905TTQuJbW0qDqtZwJXIZG8VWSLOq%2FDz32Wotq46XNuxZX1Uaorh30zYzpF%2Bk7d5X0LU05TXD50H8enKXPn1MmYQUpjFXDvOwEEYQ1Zv&X-Amz-Signature=b3d0d695b0f80f23ce9556712f317f21646d696164c0969fe343ff950d43aa3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
