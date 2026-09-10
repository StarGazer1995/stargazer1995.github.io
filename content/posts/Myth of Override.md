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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTVG7CPS%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T122658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdOJfUF6%2FAeKtKs%2BgtVBjEShTGGzgMyldUpoz0YnLB6AiBY3p8OK%2FdMjeu83KjmWaOoA2pJRWEuAZ7VNz3pKxTx3CqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdKNb1biT2ucU0z1tKtwDpNWFLY8YfZzPqW8%2FkTK4iwQvBFIO7asWpJSaOI%2FQX6%2FR5DrcykDooX9MfV9C9Pzzo%2FtPp9Y6f9zxiUQ9Wsid5gt%2BaSdPoxM%2F7MpLZ62ZpCUac9j2%2B9plfH2Y%2BUn%2F2f5oh4ebR2Grzn0JqYf%2BuFXbk%2BNQAkc9C7G%2BX3YyxBuQHgEbUtYz0nsn7sc%2BAfuXRiYrTJ6%2F96NckGnICptTlZzSpFQ0GJtjq4Uqw76y2oxTrIcYzxKOJCOZPhjSoRc8qzx%2FCCv5gHgcFfTU2mSIaY7sfM3kehOfw2uIUVKN57EnX4t2dcmuVpPBX0Kp0c0HeMxpycMK1NWyHqDHNu33BafoSSghnUSxyJ6%2FnF50OoUHzsuEmqG0hJHgdwyX7uweENg9ou3M1jSsLDoy%2BowsFAuy19lpWfmXReUFx0cD6FpEetlTnh9l3WFyOgtXH9jX1uWVUHsklB%2FAQJdbpS9NPTuTrqaHvX5GiF36v%2BNyiFAWc2%2BIX7erm8fRvUo8kL6uG76lph9q4caolkxJJukIYKUR8ktsHso2KtXr2emyYdxf%2FZIV5CluCJUpnx5C%2FwkCVQwX5rJS5YskS3ZnCVOmxVXpr7cP%2Fks%2FCkdkFObREsLvIYswj28UchURFtd%2Bz6YwsaCK1QY6pgFZwq%2BoubsOnD1lne3rtE8U4QtoF55UpOaHzmCLPOzIsRzXnUHQmudE0%2FEz4clKqlrXd0gbnoRL5W2JGI9Fnr4bYi%2Bib1B7j%2FDGO%2F7uaUCwIP%2F7%2BLR5W0E7QN%2B29hgRWrWoNslr%2Fxu4OArXz8abXIir%2F7QXyZTa0cIPkz3F5yBdz3WdWCtC%2FRQidJrUpjshnRiSaxTydVWckXo%2BRY2p60q7l08pFQAu&X-Amz-Signature=514664b9ce9129487cb493e620b79c1efa72edbe448c68602bcf2550e1dc6c5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTVG7CPS%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T122658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdOJfUF6%2FAeKtKs%2BgtVBjEShTGGzgMyldUpoz0YnLB6AiBY3p8OK%2FdMjeu83KjmWaOoA2pJRWEuAZ7VNz3pKxTx3CqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdKNb1biT2ucU0z1tKtwDpNWFLY8YfZzPqW8%2FkTK4iwQvBFIO7asWpJSaOI%2FQX6%2FR5DrcykDooX9MfV9C9Pzzo%2FtPp9Y6f9zxiUQ9Wsid5gt%2BaSdPoxM%2F7MpLZ62ZpCUac9j2%2B9plfH2Y%2BUn%2F2f5oh4ebR2Grzn0JqYf%2BuFXbk%2BNQAkc9C7G%2BX3YyxBuQHgEbUtYz0nsn7sc%2BAfuXRiYrTJ6%2F96NckGnICptTlZzSpFQ0GJtjq4Uqw76y2oxTrIcYzxKOJCOZPhjSoRc8qzx%2FCCv5gHgcFfTU2mSIaY7sfM3kehOfw2uIUVKN57EnX4t2dcmuVpPBX0Kp0c0HeMxpycMK1NWyHqDHNu33BafoSSghnUSxyJ6%2FnF50OoUHzsuEmqG0hJHgdwyX7uweENg9ou3M1jSsLDoy%2BowsFAuy19lpWfmXReUFx0cD6FpEetlTnh9l3WFyOgtXH9jX1uWVUHsklB%2FAQJdbpS9NPTuTrqaHvX5GiF36v%2BNyiFAWc2%2BIX7erm8fRvUo8kL6uG76lph9q4caolkxJJukIYKUR8ktsHso2KtXr2emyYdxf%2FZIV5CluCJUpnx5C%2FwkCVQwX5rJS5YskS3ZnCVOmxVXpr7cP%2Fks%2FCkdkFObREsLvIYswj28UchURFtd%2Bz6YwsaCK1QY6pgFZwq%2BoubsOnD1lne3rtE8U4QtoF55UpOaHzmCLPOzIsRzXnUHQmudE0%2FEz4clKqlrXd0gbnoRL5W2JGI9Fnr4bYi%2Bib1B7j%2FDGO%2F7uaUCwIP%2F7%2BLR5W0E7QN%2B29hgRWrWoNslr%2Fxu4OArXz8abXIir%2F7QXyZTa0cIPkz3F5yBdz3WdWCtC%2FRQidJrUpjshnRiSaxTydVWckXo%2BRY2p60q7l08pFQAu&X-Amz-Signature=2bf608186520eb7a226bb65525df9c369890785277f8de4b590fe313592aa18a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
