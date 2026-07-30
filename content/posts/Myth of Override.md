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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVOR5OX%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T114541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4gJIskcy3F9S5XJo3KDQG1EyVoUIPS2pNACp2E8ZJJwIgMPoWQtlqifofnQYXTxVfeLiUJjkldKZ3DQb1SWHLZ20qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDJZa1cF%2F1qJUKOKSrcA8u2CSDw0OFfW%2Fr5qlRnpe4gVg%2F0gcJ1s4jq7zD%2BozMMrzc0RFu5v5NjXZ8A5T6k1BbTgGMFGQ7ZKAjrFniT%2FJfLfxpOJzzsCk3xfgTTyVoWzU0Bg8Nw%2BhMgz8hLEbo%2Fl0L3H0ynXkhUIBebltguBnC1u3DgMlyKgMcd%2F0a2%2FPH4ldOiQ8rO57jgq%2BV%2BFcZ94DlakPY4Ue%2FLKDYC5i6EfQaqNxLLFD0a6zkJhbJYXfQZuNWNhV1CDdd7Fg2jbPfjzTPyXY5k7SMvONeuI932lU%2Bsovm%2FHXCvyez7T8Y3dr0rFraOaU7XQqFjlmuKtVd0JxZb64CR7wVqacJQ%2B%2FJfYga%2FSvaP8hMVwyQce6bdq70xwxp0oakTacAS38Ok9ZbiztdC3iP6Hmeyo6QZcbmzKC5VYFEDvuI72807mjsUBAKbu39lRL%2BhBQA7UbEqKZJffsa1WnK%2F1R50bJkWIqbq2L5qMyupzVtKd3yBgm51pw8ST%2B6W4U7MBaHvYYPRHPYxuK%2Be9saBOJXo7k2tz0UV%2F85iYQGdaauuv1IKfi2296qw9a97AfY18fI0HMWR00ynYKVQA4hAsaVfPdeGxYgxOTNpm5fzGefqcJV%2FUG67Cmpd%2F63or2Ebdazi7s9WMJXXrNMGOqUBZbk8lhb6qAfO4wNMHYvFWnk0w1iw0JRjBWH0JdGAV75Ww0AfvTRCBvxbgViTBZ861JR8%2F3tK4RYZcPRiWqvUsZX7isJ7NHYwHXdo%2BEkcC%2Bw0L5Dha8%2FvpQQc4V%2Bg7bpVqVwIHxzr%2FrB2FS6LM2U9k1cny3be7Xq6OivPX4qyxfNoq6NlJbGXbhVKecz2yPBHCK%2BNWq4zI3khWC5tX5knbzKp9ErL&X-Amz-Signature=2fcf2e9c1ae675cee48661b4142251c87e17dcc2017f0be9da54f96c2ab70575&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVOR5OX%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T114541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4gJIskcy3F9S5XJo3KDQG1EyVoUIPS2pNACp2E8ZJJwIgMPoWQtlqifofnQYXTxVfeLiUJjkldKZ3DQb1SWHLZ20qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMDJZa1cF%2F1qJUKOKSrcA8u2CSDw0OFfW%2Fr5qlRnpe4gVg%2F0gcJ1s4jq7zD%2BozMMrzc0RFu5v5NjXZ8A5T6k1BbTgGMFGQ7ZKAjrFniT%2FJfLfxpOJzzsCk3xfgTTyVoWzU0Bg8Nw%2BhMgz8hLEbo%2Fl0L3H0ynXkhUIBebltguBnC1u3DgMlyKgMcd%2F0a2%2FPH4ldOiQ8rO57jgq%2BV%2BFcZ94DlakPY4Ue%2FLKDYC5i6EfQaqNxLLFD0a6zkJhbJYXfQZuNWNhV1CDdd7Fg2jbPfjzTPyXY5k7SMvONeuI932lU%2Bsovm%2FHXCvyez7T8Y3dr0rFraOaU7XQqFjlmuKtVd0JxZb64CR7wVqacJQ%2B%2FJfYga%2FSvaP8hMVwyQce6bdq70xwxp0oakTacAS38Ok9ZbiztdC3iP6Hmeyo6QZcbmzKC5VYFEDvuI72807mjsUBAKbu39lRL%2BhBQA7UbEqKZJffsa1WnK%2F1R50bJkWIqbq2L5qMyupzVtKd3yBgm51pw8ST%2B6W4U7MBaHvYYPRHPYxuK%2Be9saBOJXo7k2tz0UV%2F85iYQGdaauuv1IKfi2296qw9a97AfY18fI0HMWR00ynYKVQA4hAsaVfPdeGxYgxOTNpm5fzGefqcJV%2FUG67Cmpd%2F63or2Ebdazi7s9WMJXXrNMGOqUBZbk8lhb6qAfO4wNMHYvFWnk0w1iw0JRjBWH0JdGAV75Ww0AfvTRCBvxbgViTBZ861JR8%2F3tK4RYZcPRiWqvUsZX7isJ7NHYwHXdo%2BEkcC%2Bw0L5Dha8%2FvpQQc4V%2Bg7bpVqVwIHxzr%2FrB2FS6LM2U9k1cny3be7Xq6OivPX4qyxfNoq6NlJbGXbhVKecz2yPBHCK%2BNWq4zI3khWC5tX5knbzKp9ErL&X-Amz-Signature=23ad644985009b8011f11b730757621dbf6d2e611be4eb056b54cf087fd27c2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
