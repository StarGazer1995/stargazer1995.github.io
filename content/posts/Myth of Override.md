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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOMVIDLR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T045734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGZ1BDXfhgwwtGV3N7VfR5xXMn5bxJx8YsqI%2FfWmOUm2AiALiKkNhthdhUFnRpycmbsbssBwMnKOMZHPumn8oGcs%2BiqIBAi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6FgUdP2kEN742GUvKtwDstCAZJ7RpA5SZnl3f4pDR442GCOY3JxhAdF%2BbGcDbXjiPK00i6Yu0YsWHYlXFD19XbhOYjcZrtC124KG1bJsfEt7OVsCMQEWjnudvpGn%2BgvTkKqy4z%2FTEcs5QEyfZwRmqDuPFP9rioWmu3d3ws19bBZWpNTItAExzOI3OOyMu9lMC5TLNqYRhOOQnzaSTXDFTEdMVSSgBD1UB35%2Bwd1MWPL4N5pdh141gTT6wqwb8G6DD3GYcuK0VlOfdPEJ3xkRU2YgN45Pu9mvGvkEd%2F%2F2hlqTgDP7ux4GWOqwd1uXZ73TaDxHKOaZ6C%2FynTvcauR7uriZKlZMt%2F7ESvGhwHT7fUEcH%2F2Zo9rpfwOcBaCdXEDIoA9SDw7ik8yucagJz7V6l%2BKALzfWNMXhqUlim6%2BbPMoM5%2Fh%2BIw9MKvUHRd9owZoqDD33PTm0S77M99wXiZ5ZZtD9lPMXTWFzN%2F1MSziFNyJRcUUO9DLZkvQMd%2B9KRQOHGKNluKp7aZ0VAOwZYyzxkr9phgbNOhMAas6ouG4wUtXlTPzRM0d4ezvBAQmFgCDA6LHcwao%2FTOFusMci%2FBppHqaTFhOJUYBofaoDVzJyqM7N9ZuA3CLhB1FZXCG8XVaQ9gp9gnP9bEdp0qEwxvL70gY6pgF76Bkq2TLYEAlRrFOi1LcUWP%2FSuOgtzr4%2FRedY9gmoOYdWpKKV7I0xlRC%2BpJtvgojsCHCm0JuaqNO%2BDJd1bGRf9gNxsgrWe8Uk2wTV%2FIlp0T3sPmMVwj8JRk5EFyV2mw7si38sAd2WDyyTW0gteNei6DoEeycfbYfwVXa18RUW8ARAOiDQ23d38s%2BKn%2BzooYL1hx3txZ12JBqNt6b7kQuIwBi%2B9D7U&X-Amz-Signature=a3cf9908cde38b81c811fa4a06d627985672b5a7ab7c498a2d5afbba7a4ef22a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOMVIDLR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T045734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGZ1BDXfhgwwtGV3N7VfR5xXMn5bxJx8YsqI%2FfWmOUm2AiALiKkNhthdhUFnRpycmbsbssBwMnKOMZHPumn8oGcs%2BiqIBAi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6FgUdP2kEN742GUvKtwDstCAZJ7RpA5SZnl3f4pDR442GCOY3JxhAdF%2BbGcDbXjiPK00i6Yu0YsWHYlXFD19XbhOYjcZrtC124KG1bJsfEt7OVsCMQEWjnudvpGn%2BgvTkKqy4z%2FTEcs5QEyfZwRmqDuPFP9rioWmu3d3ws19bBZWpNTItAExzOI3OOyMu9lMC5TLNqYRhOOQnzaSTXDFTEdMVSSgBD1UB35%2Bwd1MWPL4N5pdh141gTT6wqwb8G6DD3GYcuK0VlOfdPEJ3xkRU2YgN45Pu9mvGvkEd%2F%2F2hlqTgDP7ux4GWOqwd1uXZ73TaDxHKOaZ6C%2FynTvcauR7uriZKlZMt%2F7ESvGhwHT7fUEcH%2F2Zo9rpfwOcBaCdXEDIoA9SDw7ik8yucagJz7V6l%2BKALzfWNMXhqUlim6%2BbPMoM5%2Fh%2BIw9MKvUHRd9owZoqDD33PTm0S77M99wXiZ5ZZtD9lPMXTWFzN%2F1MSziFNyJRcUUO9DLZkvQMd%2B9KRQOHGKNluKp7aZ0VAOwZYyzxkr9phgbNOhMAas6ouG4wUtXlTPzRM0d4ezvBAQmFgCDA6LHcwao%2FTOFusMci%2FBppHqaTFhOJUYBofaoDVzJyqM7N9ZuA3CLhB1FZXCG8XVaQ9gp9gnP9bEdp0qEwxvL70gY6pgF76Bkq2TLYEAlRrFOi1LcUWP%2FSuOgtzr4%2FRedY9gmoOYdWpKKV7I0xlRC%2BpJtvgojsCHCm0JuaqNO%2BDJd1bGRf9gNxsgrWe8Uk2wTV%2FIlp0T3sPmMVwj8JRk5EFyV2mw7si38sAd2WDyyTW0gteNei6DoEeycfbYfwVXa18RUW8ARAOiDQ23d38s%2BKn%2BzooYL1hx3txZ12JBqNt6b7kQuIwBi%2B9D7U&X-Amz-Signature=997cceeeb33890b1bd49d47ddcabfd3a38f032a18dc6b205e35d265f0826363e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
