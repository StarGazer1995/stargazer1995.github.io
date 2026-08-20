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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUEDQ2J6%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T221515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2uBBCG5hmZb27fOoZ%2FFSs84l1zk5%2B55Kj%2B%2B8Zb1ZBLgIgWG6EDypiiZl7IcD7UEozimxQFXwFxi4I%2BXDnLqMBYFMqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCtDlJV3IKu0gyQICrcA7vHq46cEPR86lEPuWWVKZJvqkJZXJWO2bAc1EehYMrTsKH%2Big62y0o4V6sHONPrAuNz%2BJvmOlrfRyjy2h%2BFYYUaMQlrdxjw5PwaB7vx23fGHtHp1ZktnhWDczj1w8gNikid0yb5VQY8Np8r6PXdEYSHHMxgvCOpp2nowlKpzGmoHRYu%2FOlWtgNpaBPuMybq6CM9vU3ncWtD78ELW6pcZmWYsuHvNxOPs61%2BMDlXmdlhccWgz0GOmfZVVLkZu6YAW4jouK5k1h6H7AoXtQC7KGl8XobmcWGli%2FLvMZPPplwekXCeA0JdXIbeRlGGvQ32FD8VGJd5Zwez6Y0F%2FJcLRMaRzyd7bxX3agtxGhYgbUjiVT9lPMp8mJhwwQkFs7IIp2dzrJxjk%2Fmi3h2SmqGW6Inuo5bTpKGMBmjFGTuW9l3VOQp0NRrjbO5EUuWg%2F1OWhot%2FHDASFOb%2BDYrKW6nV3lCi5l3yPSp0nGM8UiUJ5s9ZMgWfQ44uwovsMdOpq6EXYe3hnpRxbkWu%2FIovU2vD2WzA9XAI7zrxWCfEs9H7TgN%2FtvGddVBTiNrPXebm%2BRGTu7nq2L5zNJdY0uX96BqW1xP7QKcMjDup0helQXnQWuMB9%2BWr4fAvzO2i3aG%2BMLj1ndQGOqUBOQZDAIhVNsl8geBys5TGPcU2WA7TsQ8qeaf36o%2F3FzqV%2BMCNqfWGaB7ZiZbxSlgje7ZGYEUpIyhOQa%2BncwYnlUji%2FgFiLKqOJL6Q2jhjdw4eEg9ZJBTypekS17gCSMdQw7MBLIw2DzRDSuZlrNOVhZIxpEfE5Dx2tBDpvS%2F9D173m5CfXLRYdfy%2B9anRtelAklAgXmxcLTStavCfqrLVgoiUGNV%2F&X-Amz-Signature=1a26b283826c0cd628535dfa9bd16bb1196d09be0be959c146a197b6a243dc06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUEDQ2J6%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T221515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2uBBCG5hmZb27fOoZ%2FFSs84l1zk5%2B55Kj%2B%2B8Zb1ZBLgIgWG6EDypiiZl7IcD7UEozimxQFXwFxi4I%2BXDnLqMBYFMqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCtDlJV3IKu0gyQICrcA7vHq46cEPR86lEPuWWVKZJvqkJZXJWO2bAc1EehYMrTsKH%2Big62y0o4V6sHONPrAuNz%2BJvmOlrfRyjy2h%2BFYYUaMQlrdxjw5PwaB7vx23fGHtHp1ZktnhWDczj1w8gNikid0yb5VQY8Np8r6PXdEYSHHMxgvCOpp2nowlKpzGmoHRYu%2FOlWtgNpaBPuMybq6CM9vU3ncWtD78ELW6pcZmWYsuHvNxOPs61%2BMDlXmdlhccWgz0GOmfZVVLkZu6YAW4jouK5k1h6H7AoXtQC7KGl8XobmcWGli%2FLvMZPPplwekXCeA0JdXIbeRlGGvQ32FD8VGJd5Zwez6Y0F%2FJcLRMaRzyd7bxX3agtxGhYgbUjiVT9lPMp8mJhwwQkFs7IIp2dzrJxjk%2Fmi3h2SmqGW6Inuo5bTpKGMBmjFGTuW9l3VOQp0NRrjbO5EUuWg%2F1OWhot%2FHDASFOb%2BDYrKW6nV3lCi5l3yPSp0nGM8UiUJ5s9ZMgWfQ44uwovsMdOpq6EXYe3hnpRxbkWu%2FIovU2vD2WzA9XAI7zrxWCfEs9H7TgN%2FtvGddVBTiNrPXebm%2BRGTu7nq2L5zNJdY0uX96BqW1xP7QKcMjDup0helQXnQWuMB9%2BWr4fAvzO2i3aG%2BMLj1ndQGOqUBOQZDAIhVNsl8geBys5TGPcU2WA7TsQ8qeaf36o%2F3FzqV%2BMCNqfWGaB7ZiZbxSlgje7ZGYEUpIyhOQa%2BncwYnlUji%2FgFiLKqOJL6Q2jhjdw4eEg9ZJBTypekS17gCSMdQw7MBLIw2DzRDSuZlrNOVhZIxpEfE5Dx2tBDpvS%2F9D173m5CfXLRYdfy%2B9anRtelAklAgXmxcLTStavCfqrLVgoiUGNV%2F&X-Amz-Signature=5afccc26409ffea97537e439a4a6a92bb22407a0891b5a21adb1234a43e41e08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
