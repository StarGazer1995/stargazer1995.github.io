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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGLZ4L67%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T104724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDxtSajHcllTwCmvLbeHLwIu8uqXqSomRdcQ1TdYmgWuwIhAKA1HiPv%2FrpZiIwhEK3tgt0mXCrWb%2FiBlqr%2F3hDMPkkrKogECPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzyp364J%2Bqo7T7QVCYq3ANoUvdhUXp%2FNpZEcZIrHSjiKsvi%2Bt5vxjA174SjBePIXJJLxzkuA0F6l382Yn4bx3qvIW1WLrxvssTDi50Jbhfp82l6dBB1LW6MPCN2WWxFBUzzHPycDUmr6Qdutswu2qh9DInZXzmhvRLRFAkgJ3JKm%2FNX3Bsm%2FTvH8pPXV7WsFP5WMhqqzfiG%2FwyReCW71cB4xD%2Fx8Vs2uYSf9RaiDLN8qWWPPkxUQCF3wQxycyXNNcybXf2RQoSR9HKk14yHvKq89yb8ikprwX20VGwcdvQJYd%2FqqjZ2cwB7hBsmEdMn%2BVRCrLSLgVPNcnVeW%2FngJSGhBRNPvTJQZ8ODgiQ0yntmej7e9a%2BI0N%2BbthnoJ2KtcE8yBHih1v4kHZYyySRMxNgnWZkacSx0%2FbwWDFj3Uii%2BV87gxOtxtWDU9QyerDGwmrZtyEHLAZ%2BfEVwcZMFRlpK1f8%2FBqWFdynQl%2BcRonIRNLr7H28P9D1sAZWIZzAazDVCCA6CNvze0v8hFacruerleo%2FsMMAsCV1BrnOCu%2BC0pliPNITGfyPgIXMg3FoeB3JPal0rSJyxcagvLzJcuAM%2F8WKUfu5EQfTTR%2BJw0CD9QOB%2FtGWnK0jVgFIGx%2BAsUz7hWxVrjWi8LAJsv4jCGnvvTBjqkASyGbH2C%2BEx%2B11W%2Btj1gpTaBcVgyd%2F7AWbLk4Zw0tcVOTC9odM3vDnWO7qQFiDtpd9DYzFM8vJGvfiYHgwN24GeNsZDlaANTn3kvYkGseyOyTdGkXZIOuuXASsXVbw%2FgZNmRO7TgJZtcw4cpm7i8yOs1LVcmvqpiU5rz1RL%2BIv6KiVkBfIaNmgLDRaYWDPQtqsn%2BvpX2rqLBsPyDd%2FBMHYIidIFo&X-Amz-Signature=67797333a6cdee3f75e398ce899b9c02e5747d039dd116e944037b120ae6dd76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGLZ4L67%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T104724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDxtSajHcllTwCmvLbeHLwIu8uqXqSomRdcQ1TdYmgWuwIhAKA1HiPv%2FrpZiIwhEK3tgt0mXCrWb%2FiBlqr%2F3hDMPkkrKogECPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzyp364J%2Bqo7T7QVCYq3ANoUvdhUXp%2FNpZEcZIrHSjiKsvi%2Bt5vxjA174SjBePIXJJLxzkuA0F6l382Yn4bx3qvIW1WLrxvssTDi50Jbhfp82l6dBB1LW6MPCN2WWxFBUzzHPycDUmr6Qdutswu2qh9DInZXzmhvRLRFAkgJ3JKm%2FNX3Bsm%2FTvH8pPXV7WsFP5WMhqqzfiG%2FwyReCW71cB4xD%2Fx8Vs2uYSf9RaiDLN8qWWPPkxUQCF3wQxycyXNNcybXf2RQoSR9HKk14yHvKq89yb8ikprwX20VGwcdvQJYd%2FqqjZ2cwB7hBsmEdMn%2BVRCrLSLgVPNcnVeW%2FngJSGhBRNPvTJQZ8ODgiQ0yntmej7e9a%2BI0N%2BbthnoJ2KtcE8yBHih1v4kHZYyySRMxNgnWZkacSx0%2FbwWDFj3Uii%2BV87gxOtxtWDU9QyerDGwmrZtyEHLAZ%2BfEVwcZMFRlpK1f8%2FBqWFdynQl%2BcRonIRNLr7H28P9D1sAZWIZzAazDVCCA6CNvze0v8hFacruerleo%2FsMMAsCV1BrnOCu%2BC0pliPNITGfyPgIXMg3FoeB3JPal0rSJyxcagvLzJcuAM%2F8WKUfu5EQfTTR%2BJw0CD9QOB%2FtGWnK0jVgFIGx%2BAsUz7hWxVrjWi8LAJsv4jCGnvvTBjqkASyGbH2C%2BEx%2B11W%2Btj1gpTaBcVgyd%2F7AWbLk4Zw0tcVOTC9odM3vDnWO7qQFiDtpd9DYzFM8vJGvfiYHgwN24GeNsZDlaANTn3kvYkGseyOyTdGkXZIOuuXASsXVbw%2FgZNmRO7TgJZtcw4cpm7i8yOs1LVcmvqpiU5rz1RL%2BIv6KiVkBfIaNmgLDRaYWDPQtqsn%2BvpX2rqLBsPyDd%2FBMHYIidIFo&X-Amz-Signature=ae39ba279f2258b6782fd667471245b94fec688bddf3ab82467183e58a06df41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
