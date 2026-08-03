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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVOIGQXV%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T052847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIF3Hzmwy6Fu8jbTP8qL6wQwfFnPM%2BOMyJmuQYUUA%2BSglAiAnv3rgrpnCWbtzZkDju21uTTXc3uIdD19%2FPGQnodzByyqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMgwoLguvJA5bfnpoKtwDGnra3DnCCG4v7EqBj1qaR1BhD1af8A%2Fw2z4llLzSJ7T1Tkvixa6gnFJSNSZwab4pfuc0hkLzqlxzIJWqAibTDlO6mS%2BAP%2FRb5ZQYkhh0SKvXizrWSeps7jDdcfC7qS0RoUMj26xNZ4HRd4sC36fqFM1oW8g1N1TqtwCC2iTNVG7UCp%2FDWxd%2FY7pG0M8zoywbJodK7YGZ%2FU%2FPZ96ZIAZe%2B4VpbvNFzTNlgMbOgb%2FFSbDckOv7LRU8mOPXW%2F1AN8XptkE5mod4hAZEU98x0iztHau8zY2JyXygWGKXjEkKi3Mzx77UWcLGVI2P2mZJNUIIpIbMXFe3YzFWa%2BevoIxR0woM83IOLP4BU9TxQu07KYSTdYpQirh1jNkzO0RvII0Zpn65tH07GLI0pvcY0tV%2BMPTY6qw%2B2UebFQNslO72e50CRZTgu%2FTViwdYBI1oyF1X8eG8JI89fabEJALMMnculauw0EL7S6LCpmREr%2BVoWSX5Py%2FTYRX1%2BRsucT0gaosksYZFMrNeSWZbm%2BolHUu7meDMIg2bdimZZL8AJyQxT4XVugtSp0wcUddG98LrZv4yBCEYMT6UEYETE%2B%2FuvGky%2Bd6Py%2FqrZmCETT9411VhOgvBB2Le9xNqn2fdwywwybzA0wY6pgH4nrb5g8f9tt%2FRbe3n7jMrsPLvgTNu%2FPYfAxJp7GABJQW6JaMwy9YVQBRF6DugYKDgj7M6525EBg2J0sSMUKrwluMSusuY1XeOZcu3JOW9NejBS9Uvp6PWW4woSMNpEP3xfWIx7ul1qJ2N%2BWkkEZmR6DqK3boyVUdTQhxGRf96mmBJvEwRLhF5uDf4rro5hejp%2By%2BIjjoxxErcqMkkpCKdgnA0JRbV&X-Amz-Signature=112965f9f4b465c10f80b2c3ab4632344bd7c5dcf86e0d9a978cc53ada8e6841&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVOIGQXV%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T052847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIF3Hzmwy6Fu8jbTP8qL6wQwfFnPM%2BOMyJmuQYUUA%2BSglAiAnv3rgrpnCWbtzZkDju21uTTXc3uIdD19%2FPGQnodzByyqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMgwoLguvJA5bfnpoKtwDGnra3DnCCG4v7EqBj1qaR1BhD1af8A%2Fw2z4llLzSJ7T1Tkvixa6gnFJSNSZwab4pfuc0hkLzqlxzIJWqAibTDlO6mS%2BAP%2FRb5ZQYkhh0SKvXizrWSeps7jDdcfC7qS0RoUMj26xNZ4HRd4sC36fqFM1oW8g1N1TqtwCC2iTNVG7UCp%2FDWxd%2FY7pG0M8zoywbJodK7YGZ%2FU%2FPZ96ZIAZe%2B4VpbvNFzTNlgMbOgb%2FFSbDckOv7LRU8mOPXW%2F1AN8XptkE5mod4hAZEU98x0iztHau8zY2JyXygWGKXjEkKi3Mzx77UWcLGVI2P2mZJNUIIpIbMXFe3YzFWa%2BevoIxR0woM83IOLP4BU9TxQu07KYSTdYpQirh1jNkzO0RvII0Zpn65tH07GLI0pvcY0tV%2BMPTY6qw%2B2UebFQNslO72e50CRZTgu%2FTViwdYBI1oyF1X8eG8JI89fabEJALMMnculauw0EL7S6LCpmREr%2BVoWSX5Py%2FTYRX1%2BRsucT0gaosksYZFMrNeSWZbm%2BolHUu7meDMIg2bdimZZL8AJyQxT4XVugtSp0wcUddG98LrZv4yBCEYMT6UEYETE%2B%2FuvGky%2Bd6Py%2FqrZmCETT9411VhOgvBB2Le9xNqn2fdwywwybzA0wY6pgH4nrb5g8f9tt%2FRbe3n7jMrsPLvgTNu%2FPYfAxJp7GABJQW6JaMwy9YVQBRF6DugYKDgj7M6525EBg2J0sSMUKrwluMSusuY1XeOZcu3JOW9NejBS9Uvp6PWW4woSMNpEP3xfWIx7ul1qJ2N%2BWkkEZmR6DqK3boyVUdTQhxGRf96mmBJvEwRLhF5uDf4rro5hejp%2By%2BIjjoxxErcqMkkpCKdgnA0JRbV&X-Amz-Signature=e0caceb952e985d56e32d231acd1618595f343bcdee915fbf765870fcd122fa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
