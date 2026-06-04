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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEXQPRRV%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T023145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCp%2F6h%2FZ8ojFDfrtl4ZLynx63i4gSsiJvG6I2k3o%2BgcvgIgSitbW3S6E6%2Fmgbspg96O5t%2BHkcCUKAIKZBL7Jx5siu4q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDMiH5kqC4SuRouMuISrcA76TAIuMKI3mQvh6yd2%2BMrKXLFXeF1awHrnAewNZfmhcQv44R6gJ4kl5lZ4Ydd2ReLUI9lrVivEt7ayFXxlKgqhJQ4ObrTRresvUaz5y3lvs09MJHcoOLTTEO7WecWGbO2%2BALiAOXbgi6lKjZHn3RDUso9cX0UJyX2RGje5lJkUbu844%2Fa5H5fRD36wCgrDl4DRq35pfvzqmiUQUnCCv76HxqR3MTKi8RKLXfAs%2FmjBPQPvQknnew38cMb56xDrTDAieShOdhsrLOTFFOnJdFWat7wqEtuZne5dqZ93J24UGan9prLLT%2Bxkly%2BoGXf72EnEoavpAWRv2R9j2O8nCB00jxlf62%2BI1ZSUfPjlJhUbxKHuUuBs5j5c9FLhBKSZDuHFlEXtAsPBSYCbO%2BCQpA9ifwzRM9zxYP2bOjlfX3AcC2HlyThJBl9XnYi8FqrTA26%2B8HdYlsYEhzcMdVe8HM4yWLOgN1HYnwxGHcNLbxMh09RUF%2FZqrgBJ787OpiVsVQ5doOojSTQmf%2FFbzrmRfXYpWth7GMqmpc4bmdruvEKi0qt5RbI4p%2FrXPwSdD6tVf9uskwrKg%2FNl%2Fy9oy4BUlA0l217WT8SDAK%2F5GCefzU%2BSZLbJEdoyhn5NGix%2FkMK2wg9EGOqUB0LPkxlzZ1nTCXG6Am4QJA57qFYiJ5i5YBzEgUD%2FGxqBW3aEU4SEc6HlL8qTJJukLpvPOp7WcCOEiODczeLRn94AAF3%2FIxHutDHfphm7RZGT%2FdNkVNPsTlU5T36ywLOzHBVavOVoGqDrPtcKq8GOOjpteF2VFbpaeDL%2Fz8MJHdFaUP8fNwwzWkJTpoMnu7Fch1xDh45TUpDO2Mxb%2FANDyUFSPL7lS&X-Amz-Signature=15be74afc3f56ced82b97f68484451a1e7c26110f3d203ad6d18d11e95bef1ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEXQPRRV%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T023145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCp%2F6h%2FZ8ojFDfrtl4ZLynx63i4gSsiJvG6I2k3o%2BgcvgIgSitbW3S6E6%2Fmgbspg96O5t%2BHkcCUKAIKZBL7Jx5siu4q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDMiH5kqC4SuRouMuISrcA76TAIuMKI3mQvh6yd2%2BMrKXLFXeF1awHrnAewNZfmhcQv44R6gJ4kl5lZ4Ydd2ReLUI9lrVivEt7ayFXxlKgqhJQ4ObrTRresvUaz5y3lvs09MJHcoOLTTEO7WecWGbO2%2BALiAOXbgi6lKjZHn3RDUso9cX0UJyX2RGje5lJkUbu844%2Fa5H5fRD36wCgrDl4DRq35pfvzqmiUQUnCCv76HxqR3MTKi8RKLXfAs%2FmjBPQPvQknnew38cMb56xDrTDAieShOdhsrLOTFFOnJdFWat7wqEtuZne5dqZ93J24UGan9prLLT%2Bxkly%2BoGXf72EnEoavpAWRv2R9j2O8nCB00jxlf62%2BI1ZSUfPjlJhUbxKHuUuBs5j5c9FLhBKSZDuHFlEXtAsPBSYCbO%2BCQpA9ifwzRM9zxYP2bOjlfX3AcC2HlyThJBl9XnYi8FqrTA26%2B8HdYlsYEhzcMdVe8HM4yWLOgN1HYnwxGHcNLbxMh09RUF%2FZqrgBJ787OpiVsVQ5doOojSTQmf%2FFbzrmRfXYpWth7GMqmpc4bmdruvEKi0qt5RbI4p%2FrXPwSdD6tVf9uskwrKg%2FNl%2Fy9oy4BUlA0l217WT8SDAK%2F5GCefzU%2BSZLbJEdoyhn5NGix%2FkMK2wg9EGOqUB0LPkxlzZ1nTCXG6Am4QJA57qFYiJ5i5YBzEgUD%2FGxqBW3aEU4SEc6HlL8qTJJukLpvPOp7WcCOEiODczeLRn94AAF3%2FIxHutDHfphm7RZGT%2FdNkVNPsTlU5T36ywLOzHBVavOVoGqDrPtcKq8GOOjpteF2VFbpaeDL%2Fz8MJHdFaUP8fNwwzWkJTpoMnu7Fch1xDh45TUpDO2Mxb%2FANDyUFSPL7lS&X-Amz-Signature=a9c5d0581009ecef8632648b0cf9e7cfcf248cda84c7c5662a25d97298f5a3f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
