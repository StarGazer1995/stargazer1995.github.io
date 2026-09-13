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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJV4N4QH%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T014352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETvBVxwFdNUn0kS6S3v7w5E%2FHmr1mSUOs8cfhjbf%2BOaAiBngtBkvpjuHuDbjC1YPq4BUHlKy7yrM8ejGIuwSJZI1yqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfH71XuaC97okAn%2BiKtwDbQ6%2Bx5vp9iNcg9bs3g52M4PXENI8YiH79RIwr20sYKGB3KpdY7ah%2BkidqEY53M7VKP8ShwPfSsMCJLnF35%2BvRQTroL44if%2FoMivE2HQAf9m9Sfse79NcJSAh0vsKnCMrs4abvBA4Wwli914dCxSX609Mu%2FtnuoblIKbAy%2FyIWbbKsZI2ypEeU4ryAlGbY66yuq%2Bg7xIIJeeaL7eored7CTD9167CxL6ox0qvpQVom4vEVISyhPqwffdICxczDgY5k8W%2BQoRmlPQei7SlC%2Fr9irDCNyNjbg5Kuwx0eggtQqD0cIJK%2BAVT%2Fkb9VJGkYBIY5rqnGtFNqnvFsP6D4OeLrAZLfJRaitNMhCyGnD8UWAO1XSdCLNDGEBB58oQu3E34qsjTX5WI%2FbsoMmDVyw1SJQBrLgwrhN9I3OQNku%2Ffxc7NPgMsoatbAkS2RUXinME6gAUBYMW2Bat9SbjP2r9bjyshhYXAhH7%2BsOKmoI2dsRjDazp1r77SvcCpHJ4YN87LZeWogQBD8txhGd%2B5zLsx9CezlljSQNYXKG2lZAtnhvPz4XHUK3jWTT8wf7zkjBcMlA2F3zu9VhVSjQGv2d4qFyHGkNCbknhcALujdAWuwHzFQuPdZXHe8zQO34sw8%2BKX1QY6pgGxiCK6jtq%2BPt4OqG%2BJHPeaZ8trJc6oFASuVWQCo1VGpCsRf209gurZhNAWbLoig%2FbOGCFVajL3sWyzhLyAk0tp%2FEP9AkoOet1FnDL4kSladpVajN4uE4qjY8oEkLcntHUdG6aFaJIL93izN8D4%2Bnc0Cyw9o0yATYHMR%2FzyqBX2mOfhm5OO5mGDSCbYN8rvR1bntnm6CZY34Cjr8NP%2F1cvAa9PbwDv%2F&X-Amz-Signature=67c3f89b610e369d23710a4e4c550d8dd78f4fdc05b635be6106105440eca513&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJV4N4QH%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T014352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETvBVxwFdNUn0kS6S3v7w5E%2FHmr1mSUOs8cfhjbf%2BOaAiBngtBkvpjuHuDbjC1YPq4BUHlKy7yrM8ejGIuwSJZI1yqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfH71XuaC97okAn%2BiKtwDbQ6%2Bx5vp9iNcg9bs3g52M4PXENI8YiH79RIwr20sYKGB3KpdY7ah%2BkidqEY53M7VKP8ShwPfSsMCJLnF35%2BvRQTroL44if%2FoMivE2HQAf9m9Sfse79NcJSAh0vsKnCMrs4abvBA4Wwli914dCxSX609Mu%2FtnuoblIKbAy%2FyIWbbKsZI2ypEeU4ryAlGbY66yuq%2Bg7xIIJeeaL7eored7CTD9167CxL6ox0qvpQVom4vEVISyhPqwffdICxczDgY5k8W%2BQoRmlPQei7SlC%2Fr9irDCNyNjbg5Kuwx0eggtQqD0cIJK%2BAVT%2Fkb9VJGkYBIY5rqnGtFNqnvFsP6D4OeLrAZLfJRaitNMhCyGnD8UWAO1XSdCLNDGEBB58oQu3E34qsjTX5WI%2FbsoMmDVyw1SJQBrLgwrhN9I3OQNku%2Ffxc7NPgMsoatbAkS2RUXinME6gAUBYMW2Bat9SbjP2r9bjyshhYXAhH7%2BsOKmoI2dsRjDazp1r77SvcCpHJ4YN87LZeWogQBD8txhGd%2B5zLsx9CezlljSQNYXKG2lZAtnhvPz4XHUK3jWTT8wf7zkjBcMlA2F3zu9VhVSjQGv2d4qFyHGkNCbknhcALujdAWuwHzFQuPdZXHe8zQO34sw8%2BKX1QY6pgGxiCK6jtq%2BPt4OqG%2BJHPeaZ8trJc6oFASuVWQCo1VGpCsRf209gurZhNAWbLoig%2FbOGCFVajL3sWyzhLyAk0tp%2FEP9AkoOet1FnDL4kSladpVajN4uE4qjY8oEkLcntHUdG6aFaJIL93izN8D4%2Bnc0Cyw9o0yATYHMR%2FzyqBX2mOfhm5OO5mGDSCbYN8rvR1bntnm6CZY34Cjr8NP%2F1cvAa9PbwDv%2F&X-Amz-Signature=3f582a30bd6a2dffccb828173a8e56e42bdb5466a818fedf660cbe5850a79db1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
