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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MBRQTZA%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T075031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQDA1X%2B11sZ2UDeAiKW%2B0j%2FP6E1AomzymJIIEzfDIHn2uwIfd%2FpDZTq4DJI1L8wUqPx33ssvjVlK%2BLQq27%2Fy58zjhyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMjTCz8oUYZPKTeJyeKtwD6aLPvSfBLFsIY%2Bu5IAGqz7rmUwPS%2FphEOINcoTAYzMNGefwFS9mz1VChIxzuyHA8Sth4UW2kczOSPOry0CpZHIAZh6B2cdtJgD2eoZPndZiCZUXPatba2UP6jltKxbf79xpiuueBodaIjibyVm0t%2BHw4QfOxoL9PvknSdwKr%2FhyLZ1ABZHAwrHLWfgjI0BP7kwFs05aYI2ktpg0HMAYH2nV88eBIxuuscB46e%2BNqCRXbhkeOWzRyz4ItcKIL5M9XlOA9hKwNB4nX8puEqEH9KET6sovaE%2F2S2CBLapMX%2Ff37j6wdIMuyw9WwIjZ3u65HQyDCzv%2BlWBAkx6h9%2FePC0%2Bn2QqFYtSg0mAQLgLyR%2F9KARlvM1iTr4o7F4XRZk5Od6Wkxg9ZOwvKtukj4Ao2BSfmapQ3cCeMteV0beIaba5LcKJMlA6R3Qh3BwxNzyu0Rs5YdL3hNy4FlyObzn%2F1aWEKXahYHSbINsc1nx2PfY2d99YOu671S%2BwZ9jRFffKF%2BY9%2BQ1eGq%2BOcScR3w7%2FN8tYcM%2ByOfVqAezuzE4RjgmmxLf67y16unXJnRfSN7gevJfEvCHFQ2hJymOxFEbIj2ed5mzYS6Zg8TKezYvYGTsS56Md6EpdgAA%2BIjJVwwza3n0gY6pgE31AHLGaDpcUzQLyZ6kLZIbrxOe2kjFihoGL5NyvVQR0Ra%2FnPcy77Eqn2UjEl4Y1OdBWcTaGFZr3X61%2Bw7dR5OjMuuWS%2Bimuj%2FaX14%2Bny%2BKJffUT2pTIuFGc3aZNCZR8u1rgZC3PvXNj7h1goDHYYJB3pVMwCZK7B7PgVrnYn8%2FNaAH7P0cHIpopfa%2BFfxI5SfEXotj5AzucA3HdLE1Y04xxqNz35n&X-Amz-Signature=edf327b07397c6d18a0cd3d32f168543931b97272acde8fa44c474ed3d466b21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MBRQTZA%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T075031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQDA1X%2B11sZ2UDeAiKW%2B0j%2FP6E1AomzymJIIEzfDIHn2uwIfd%2FpDZTq4DJI1L8wUqPx33ssvjVlK%2BLQq27%2Fy58zjhyr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMjTCz8oUYZPKTeJyeKtwD6aLPvSfBLFsIY%2Bu5IAGqz7rmUwPS%2FphEOINcoTAYzMNGefwFS9mz1VChIxzuyHA8Sth4UW2kczOSPOry0CpZHIAZh6B2cdtJgD2eoZPndZiCZUXPatba2UP6jltKxbf79xpiuueBodaIjibyVm0t%2BHw4QfOxoL9PvknSdwKr%2FhyLZ1ABZHAwrHLWfgjI0BP7kwFs05aYI2ktpg0HMAYH2nV88eBIxuuscB46e%2BNqCRXbhkeOWzRyz4ItcKIL5M9XlOA9hKwNB4nX8puEqEH9KET6sovaE%2F2S2CBLapMX%2Ff37j6wdIMuyw9WwIjZ3u65HQyDCzv%2BlWBAkx6h9%2FePC0%2Bn2QqFYtSg0mAQLgLyR%2F9KARlvM1iTr4o7F4XRZk5Od6Wkxg9ZOwvKtukj4Ao2BSfmapQ3cCeMteV0beIaba5LcKJMlA6R3Qh3BwxNzyu0Rs5YdL3hNy4FlyObzn%2F1aWEKXahYHSbINsc1nx2PfY2d99YOu671S%2BwZ9jRFffKF%2BY9%2BQ1eGq%2BOcScR3w7%2FN8tYcM%2ByOfVqAezuzE4RjgmmxLf67y16unXJnRfSN7gevJfEvCHFQ2hJymOxFEbIj2ed5mzYS6Zg8TKezYvYGTsS56Md6EpdgAA%2BIjJVwwza3n0gY6pgE31AHLGaDpcUzQLyZ6kLZIbrxOe2kjFihoGL5NyvVQR0Ra%2FnPcy77Eqn2UjEl4Y1OdBWcTaGFZr3X61%2Bw7dR5OjMuuWS%2Bimuj%2FaX14%2Bny%2BKJffUT2pTIuFGc3aZNCZR8u1rgZC3PvXNj7h1goDHYYJB3pVMwCZK7B7PgVrnYn8%2FNaAH7P0cHIpopfa%2BFfxI5SfEXotj5AzucA3HdLE1Y04xxqNz35n&X-Amz-Signature=7b2c69fe1fa9c2076f4874477a27836f53a8a22627317935a03a6b119eb5395d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
