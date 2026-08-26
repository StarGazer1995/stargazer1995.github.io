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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHNOCOG6%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T164146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCICN9UouJ0dPgr92ql0bw6LaXBChGak00QAx%2BAvTWQI4OAiBi2%2BGqlWKK%2BhGZbOMCYaTi77ZjwXEPQOhuP%2BpXsIuBFCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMaOHHFMR7qHWdkzhyKtwDlB9ROGlXh7qV61s9CC67aG5eMqQm4aVIYv78xD4ZEY5XJnSv8ahF1CSK%2B7VEXxzvtSVS8WB0aNdHS4PvNGPLRvRs%2BZX3oSiNuAbUWtI0mHlvQCVviw5rGeMmBMv5Ku1AVLVBhUHEXYcbJjz87g32u1Ovh5F3LdNvxCdLOCts6BbxmTvJg%2B6%2BjJXqDI%2FWDsOb4iBPG%2FIA8UEK7HKn5XQn0zjghVSfgXCT42CWoKK2knwhfTnJkFHSLqWl3qKKqYUkeVuwUTU47BkNrYtN1n%2BMn40nOIATos8Bxl4%2Bi%2BAeQfEcdQmlV05ortvmQrUM3kyi%2F83Ug8QdA06gmCI9ozZEU%2BjkXNiZ4MH68ybgDAQpTKTKLg%2B15Yt4NtYPQjkBl4VjcHwuB7bDcphwRTF3T4tS%2Fh0d91PC8fKcA42xS4tMKsiS5ErCGMrNJ73cc8t1pt7Z24W59Hgb%2FZ0J9jZvWnqxb%2FFYcOE2VAGsNzmIhUzYqmQnkk7%2BYkrhVozXP%2BlSXj4V%2FIQXYCfx76jJEmM9AmASfJRnpG8UtFW2Ptlvw2MsYwP%2BxZAMlw6SFh4TKognQWRRTEsZa5P0ev6j7XL14mHJKLXazXeNWB6qBpgWY3IoKX66WoJORUsRGKoEmjgwnOK71AY6pgFvGHHBhwYcN5Xd4h7uh%2BAiZTtwBEo6YGqhN0TPazrmGiWnvIUdHBabRdelpMOug%2BkcLFB5K7vNjZev5a3%2BzANxYSeXfTuy4XBvl98uagAWhFbHChKsR5GznGn15zULZ7n5G8NY2hZq9Go%2BYdTkBjvZ%2FLP6Xp8fJHHLaE%2FqzFcFBZ54tzkYdNxJcAU%2B7AID%2FHjEjI4Wi6Z71DrwVgRP7YH8Gu5MJu%2BD&X-Amz-Signature=dbf79abf2482beffb8347b73854584eebf77bb134e26b3be58f9eff13a13b444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHNOCOG6%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T164145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCICN9UouJ0dPgr92ql0bw6LaXBChGak00QAx%2BAvTWQI4OAiBi2%2BGqlWKK%2BhGZbOMCYaTi77ZjwXEPQOhuP%2BpXsIuBFCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMaOHHFMR7qHWdkzhyKtwDlB9ROGlXh7qV61s9CC67aG5eMqQm4aVIYv78xD4ZEY5XJnSv8ahF1CSK%2B7VEXxzvtSVS8WB0aNdHS4PvNGPLRvRs%2BZX3oSiNuAbUWtI0mHlvQCVviw5rGeMmBMv5Ku1AVLVBhUHEXYcbJjz87g32u1Ovh5F3LdNvxCdLOCts6BbxmTvJg%2B6%2BjJXqDI%2FWDsOb4iBPG%2FIA8UEK7HKn5XQn0zjghVSfgXCT42CWoKK2knwhfTnJkFHSLqWl3qKKqYUkeVuwUTU47BkNrYtN1n%2BMn40nOIATos8Bxl4%2Bi%2BAeQfEcdQmlV05ortvmQrUM3kyi%2F83Ug8QdA06gmCI9ozZEU%2BjkXNiZ4MH68ybgDAQpTKTKLg%2B15Yt4NtYPQjkBl4VjcHwuB7bDcphwRTF3T4tS%2Fh0d91PC8fKcA42xS4tMKsiS5ErCGMrNJ73cc8t1pt7Z24W59Hgb%2FZ0J9jZvWnqxb%2FFYcOE2VAGsNzmIhUzYqmQnkk7%2BYkrhVozXP%2BlSXj4V%2FIQXYCfx76jJEmM9AmASfJRnpG8UtFW2Ptlvw2MsYwP%2BxZAMlw6SFh4TKognQWRRTEsZa5P0ev6j7XL14mHJKLXazXeNWB6qBpgWY3IoKX66WoJORUsRGKoEmjgwnOK71AY6pgFvGHHBhwYcN5Xd4h7uh%2BAiZTtwBEo6YGqhN0TPazrmGiWnvIUdHBabRdelpMOug%2BkcLFB5K7vNjZev5a3%2BzANxYSeXfTuy4XBvl98uagAWhFbHChKsR5GznGn15zULZ7n5G8NY2hZq9Go%2BYdTkBjvZ%2FLP6Xp8fJHHLaE%2FqzFcFBZ54tzkYdNxJcAU%2B7AID%2FHjEjI4Wi6Z71DrwVgRP7YH8Gu5MJu%2BD&X-Amz-Signature=b802ca4e724c83b3a304393bd7550152c1d23c814f018386d18ed46a4146c9a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
