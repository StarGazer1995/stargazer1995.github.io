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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK35H7DJ%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T212113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHe1SS%2BKQGG7sqFxwKTLaZzsG2KoEi9MRlioWz50kOVgIgSKatmBT8rESWBZtDK1DeqRHDC7jzLPs5D6hs3ojPGbAq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDFjJrJKmfMZnrQeYzircA1RexyI30cLM49zfJiDmxWB60u6cOxMrnT7GPm3etB9tJHjbBaEl%2Bw41vVd2Zl6%2F6gYc2Bm3SQ5Ml0lJ%2F%2F%2BbtrXEGy53jzdRPa4e%2FHHjrZMHSkQbz0O%2F6b%2Fi81enxTc5Ua3bgz5BRjMBHeKtn0SITSrX1aVY72RdUUjxMbED45w%2FtIe%2BNGMYSYNG4kATL%2Famvu3TYjhWOqSpqjYggo4FoJrbe1fSrDmAZyrxEFOaLn1kjFiz9n2Fi26V5iWGWTImnVC21TcPUe7R0HQCzmlGMy22r9QxU2hsEX9LIttK350yvHt5XXAjTxA6s%2BgF0CK4NAq1gbRaJGJRbOvepHVfy%2FJDf6O6YWeerr42fgrYItiZl4DJBWlvzMb2u5qYrAJ%2FuDfxS3XjUCFrdzkYE%2FdWIZe8Zq%2B1DVRH1UwUQErARd7mSO%2FG1AsuqD%2FBxewOYak0P52r16VL30hb0iEpu4IRE79qDfn1dqeoa8Bo5m2%2B7OnHH%2FvqtV56%2BJ%2BrlpRtuKiOQjKaLTEPx%2BiVN%2BUNIwpB8dvR6ikQPeknl6JETh2fQnloOZ%2B8HjMgvOSwDAQde1vM6npQTVsWEOxi3Q5coj1fFP3KB51J1wBvtN%2Bxs0QN8FcD%2Bys3dClyJYAiBbBFMLCP9tEGOqUB5SZIFT%2FvjKucTMqtWY6Gbuj%2BSfAvHGHVbFAUtGQkVNXM0dEKcDyt1HoV2Mcl5Cm5rPuv1ph80ytOSa8U1ytWhGW7FpnDGqnsPGRWmHDWcniTP7dG9gIjapW12Lwq3XT2UnqdFHAZna8p4lZFO2qMeFXOHEgFjUPy4cLMuQYDf9e60JSpe2V9tVuQFzj86C4wWdW%2FXr%2FYofDd9plgU9X7FRv%2Bcz6O&X-Amz-Signature=34a1fe9b763f7b60f292bdcac2a460610cc804f398c4dfa1e1f66690cfa93b8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK35H7DJ%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T212113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHe1SS%2BKQGG7sqFxwKTLaZzsG2KoEi9MRlioWz50kOVgIgSKatmBT8rESWBZtDK1DeqRHDC7jzLPs5D6hs3ojPGbAq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDFjJrJKmfMZnrQeYzircA1RexyI30cLM49zfJiDmxWB60u6cOxMrnT7GPm3etB9tJHjbBaEl%2Bw41vVd2Zl6%2F6gYc2Bm3SQ5Ml0lJ%2F%2F%2BbtrXEGy53jzdRPa4e%2FHHjrZMHSkQbz0O%2F6b%2Fi81enxTc5Ua3bgz5BRjMBHeKtn0SITSrX1aVY72RdUUjxMbED45w%2FtIe%2BNGMYSYNG4kATL%2Famvu3TYjhWOqSpqjYggo4FoJrbe1fSrDmAZyrxEFOaLn1kjFiz9n2Fi26V5iWGWTImnVC21TcPUe7R0HQCzmlGMy22r9QxU2hsEX9LIttK350yvHt5XXAjTxA6s%2BgF0CK4NAq1gbRaJGJRbOvepHVfy%2FJDf6O6YWeerr42fgrYItiZl4DJBWlvzMb2u5qYrAJ%2FuDfxS3XjUCFrdzkYE%2FdWIZe8Zq%2B1DVRH1UwUQErARd7mSO%2FG1AsuqD%2FBxewOYak0P52r16VL30hb0iEpu4IRE79qDfn1dqeoa8Bo5m2%2B7OnHH%2FvqtV56%2BJ%2BrlpRtuKiOQjKaLTEPx%2BiVN%2BUNIwpB8dvR6ikQPeknl6JETh2fQnloOZ%2B8HjMgvOSwDAQde1vM6npQTVsWEOxi3Q5coj1fFP3KB51J1wBvtN%2Bxs0QN8FcD%2Bys3dClyJYAiBbBFMLCP9tEGOqUB5SZIFT%2FvjKucTMqtWY6Gbuj%2BSfAvHGHVbFAUtGQkVNXM0dEKcDyt1HoV2Mcl5Cm5rPuv1ph80ytOSa8U1ytWhGW7FpnDGqnsPGRWmHDWcniTP7dG9gIjapW12Lwq3XT2UnqdFHAZna8p4lZFO2qMeFXOHEgFjUPy4cLMuQYDf9e60JSpe2V9tVuQFzj86C4wWdW%2FXr%2FYofDd9plgU9X7FRv%2Bcz6O&X-Amz-Signature=7bf1b680fbd213d1409fef9272c9e44749e950134621b362875dd9072a3abf94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
