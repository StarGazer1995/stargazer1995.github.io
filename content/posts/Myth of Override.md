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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIHNDCJ2%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T210318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu%2F5Hbb3MXQHTrlaD7hioUQme%2BdDiEwMNEpBRZdbxJYwIhALR73FVh60ZP2%2FUmcBKfPCn7Q5CIdFeqjC8RKDNezqYeKv8DCGUQABoMNjM3NDIzMTgzODA1IgwxlCAHqnG%2F43g1gZQq3APWLnrq1kFblx6%2BeBYXUlXR%2B9Ss1gGIUhXXCejSgS3HazyOT04LKZvNB32Yc7rPSjoM5pZTQyjTjGQg1Eohm3vQO%2BzoVx5MMSwOx%2Fj5cuoIJZMzhjJy2lFnkN6%2BIF4TrSspwV4f39dWnWRsBT5fFTmN7q1GqEKWOGt6g7%2FugQOVcASBij8zplKt%2Fvk5bLv8pfz8RhEz3St%2FfoqJcCoCEyhYyM0QtUP1IOSaAQ4y%2BvzIqUydpcU8lhIIH9XqGq6YIAIYpYBy7Vl1%2BIqHlSvNzZhf%2F819By%2BIztSr%2Bi3fanbAD1NgiavHKvQzADrTokCmYYRqBVgoEgFXltc6Kar3SDvwjPfIJxPnntDkzDNQdiRsQLO2gFMOHAvEbm974FZuR4TcnYUVKVHWr67Ghxg6kYVJ%2FQm5%2FpBf3OCS6yRcsyNC52lXjng6c1s3n%2B6qESkXe4NOosdtOlQ%2FWj6jK6XlEB4MQ%2Bn88hOig63YcuNeQ%2FLF2jlKEwEfMTelGeyHx5QuoosT8s9H5msLft4asCsqtTbQvjmWyCc18MH7UfQ24KupIig4guEr%2Fh495R50NJ%2BePcgJqb2FYCaVMCmpSefcdbE7faQ649dJq0OPuIk%2FmI%2B9wEJ9CUSa5CKa8ri34zDaxJjQBjqkAYvcT0CCP8Kxt%2FbpDXw75MYjMVceGg7KDVDZTI5IXtgyU1tsxq62%2FsLwPW06FoeS%2F%2FwjK5KgLO%2FYaJEiTpMUMkw5BEHJTIcAxeeHZIEJHkAuYY5eWDRG%2FamNf%2FwMWk6n9Qw3bfGMnU0FvzaAJDtEQAfMxJrObya7tdEDDWZ2cr1rJj2fsJK3w4tB8LoeHv2BbbxOjBmTr0y4XjmCcPD%2Fueno3Yik&X-Amz-Signature=94f13250d0ce9e65d6220df7ba0ca6280335589a7cea17a548cbe238e76cfc82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIHNDCJ2%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T210318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu%2F5Hbb3MXQHTrlaD7hioUQme%2BdDiEwMNEpBRZdbxJYwIhALR73FVh60ZP2%2FUmcBKfPCn7Q5CIdFeqjC8RKDNezqYeKv8DCGUQABoMNjM3NDIzMTgzODA1IgwxlCAHqnG%2F43g1gZQq3APWLnrq1kFblx6%2BeBYXUlXR%2B9Ss1gGIUhXXCejSgS3HazyOT04LKZvNB32Yc7rPSjoM5pZTQyjTjGQg1Eohm3vQO%2BzoVx5MMSwOx%2Fj5cuoIJZMzhjJy2lFnkN6%2BIF4TrSspwV4f39dWnWRsBT5fFTmN7q1GqEKWOGt6g7%2FugQOVcASBij8zplKt%2Fvk5bLv8pfz8RhEz3St%2FfoqJcCoCEyhYyM0QtUP1IOSaAQ4y%2BvzIqUydpcU8lhIIH9XqGq6YIAIYpYBy7Vl1%2BIqHlSvNzZhf%2F819By%2BIztSr%2Bi3fanbAD1NgiavHKvQzADrTokCmYYRqBVgoEgFXltc6Kar3SDvwjPfIJxPnntDkzDNQdiRsQLO2gFMOHAvEbm974FZuR4TcnYUVKVHWr67Ghxg6kYVJ%2FQm5%2FpBf3OCS6yRcsyNC52lXjng6c1s3n%2B6qESkXe4NOosdtOlQ%2FWj6jK6XlEB4MQ%2Bn88hOig63YcuNeQ%2FLF2jlKEwEfMTelGeyHx5QuoosT8s9H5msLft4asCsqtTbQvjmWyCc18MH7UfQ24KupIig4guEr%2Fh495R50NJ%2BePcgJqb2FYCaVMCmpSefcdbE7faQ649dJq0OPuIk%2FmI%2B9wEJ9CUSa5CKa8ri34zDaxJjQBjqkAYvcT0CCP8Kxt%2FbpDXw75MYjMVceGg7KDVDZTI5IXtgyU1tsxq62%2FsLwPW06FoeS%2F%2FwjK5KgLO%2FYaJEiTpMUMkw5BEHJTIcAxeeHZIEJHkAuYY5eWDRG%2FamNf%2FwMWk6n9Qw3bfGMnU0FvzaAJDtEQAfMxJrObya7tdEDDWZ2cr1rJj2fsJK3w4tB8LoeHv2BbbxOjBmTr0y4XjmCcPD%2Fueno3Yik&X-Amz-Signature=b5685586c21a4fdf188038d49f86d0b72212741b1003f0b380a7989eff1b64ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
