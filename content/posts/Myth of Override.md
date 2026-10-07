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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665X5DPRWJ%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T211549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQD%2Fx0okqMVA5atSyGa0SSfTA53Fj%2FbaqUBybavSeclMqQIgEQmW4qX1Kl5ENjKH3X1OU94aEcDOYVG508TiYGeqMuwq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDIgGX0kizbiLrfnfoircA%2BwaeejDm2%2Fh7mJ2iOP47lP8F9NGx1deqwceCGPNfc0qofCjqWwI3pzEfPG%2Bwq%2Bp6451nvoDOAF8qdNYI0gY3hopRj442Wu1niDOXyhlDtgDFuwKRC4egEw%2B7%2FcjP1KDA1mbNxlw4CY0kJdeaAHv0fHULOS7M884qqKElsQoCOBDxhZNFwsmbg%2FPtqlo1Co3%2FWfTlf2dO%2B0aUoyc7MEww%2Fy2Pg14iiO1iHbS%2BmR%2FjQkzfN07WhriBo4N70cybvJyADmw%2FSEnhYFWTPhnDnLJetDjP2TE7ydVrq6FV%2BUf%2BZMnf0IMBeVn3LauPSlUHdLjPk8OESgvmr0fsyDu8E5Gx4gXiC7V6%2FpvzjGyfXuX4SIPtkJGJWeEIDKV1SOyKY8vw%2F%2F5f8SF5HXZC3I7jKbnmkXfr%2FbJpP8n2mygZmMqkTCIkz8oim3eOfixMg5VzaqAgs%2Br1tcc2zuEcKM0y45CWv0y1UmfOvXtQquaFbTSYw6F3YaqgQjRFFktqldxYJryX1we0qw1zz5AJAoKQKlllKkjVCT7N0Ydd%2F31%2Fu6ATJI0zFNzAf0ix%2F%2BXOc73kPlPncL%2BM9lko4OvUkkUyd%2FY30brjwuX2378PyKSAGGTPz5lNfVZN%2BopWtmp1rYoMNTXmtYGOqUB8jPRNkzScpNpZRgd8gBfvoJfrJTXiqWoQ1XRCoxCzNA%2F1srUKARS3zzhs8B6uVKOKfTwec%2FJ%2BKfsxTNs%2F96s5mzGgJTLgHIhVz1wFexEiKgOdM0GI2RCZ%2BlhpXt%2Fvp4mLyvsVJ7n3tishuqsYTY9%2B7Q0VZSJWRiYjGJbMSYj44ZBBXH%2FkJnCWgbhH1u1cqwmjo%2FQcHZK7ZxDbWWLrWd1T%2BINJp1W&X-Amz-Signature=dd22788621e31eaf6b35ab423c90f66784fcc30cb413423bc8043f40de49e486&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665X5DPRWJ%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T211549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQD%2Fx0okqMVA5atSyGa0SSfTA53Fj%2FbaqUBybavSeclMqQIgEQmW4qX1Kl5ENjKH3X1OU94aEcDOYVG508TiYGeqMuwq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDIgGX0kizbiLrfnfoircA%2BwaeejDm2%2Fh7mJ2iOP47lP8F9NGx1deqwceCGPNfc0qofCjqWwI3pzEfPG%2Bwq%2Bp6451nvoDOAF8qdNYI0gY3hopRj442Wu1niDOXyhlDtgDFuwKRC4egEw%2B7%2FcjP1KDA1mbNxlw4CY0kJdeaAHv0fHULOS7M884qqKElsQoCOBDxhZNFwsmbg%2FPtqlo1Co3%2FWfTlf2dO%2B0aUoyc7MEww%2Fy2Pg14iiO1iHbS%2BmR%2FjQkzfN07WhriBo4N70cybvJyADmw%2FSEnhYFWTPhnDnLJetDjP2TE7ydVrq6FV%2BUf%2BZMnf0IMBeVn3LauPSlUHdLjPk8OESgvmr0fsyDu8E5Gx4gXiC7V6%2FpvzjGyfXuX4SIPtkJGJWeEIDKV1SOyKY8vw%2F%2F5f8SF5HXZC3I7jKbnmkXfr%2FbJpP8n2mygZmMqkTCIkz8oim3eOfixMg5VzaqAgs%2Br1tcc2zuEcKM0y45CWv0y1UmfOvXtQquaFbTSYw6F3YaqgQjRFFktqldxYJryX1we0qw1zz5AJAoKQKlllKkjVCT7N0Ydd%2F31%2Fu6ATJI0zFNzAf0ix%2F%2BXOc73kPlPncL%2BM9lko4OvUkkUyd%2FY30brjwuX2378PyKSAGGTPz5lNfVZN%2BopWtmp1rYoMNTXmtYGOqUB8jPRNkzScpNpZRgd8gBfvoJfrJTXiqWoQ1XRCoxCzNA%2F1srUKARS3zzhs8B6uVKOKfTwec%2FJ%2BKfsxTNs%2F96s5mzGgJTLgHIhVz1wFexEiKgOdM0GI2RCZ%2BlhpXt%2Fvp4mLyvsVJ7n3tishuqsYTY9%2B7Q0VZSJWRiYjGJbMSYj44ZBBXH%2FkJnCWgbhH1u1cqwmjo%2FQcHZK7ZxDbWWLrWd1T%2BINJp1W&X-Amz-Signature=c2dc1251043be07509c7e96c20448ec25052edce92dd64335280a1d27f8ff4c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
