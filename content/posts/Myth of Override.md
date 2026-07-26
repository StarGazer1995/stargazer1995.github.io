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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOYKNUOQ%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T224824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIHho0co2JbdHRCv5AxF9Qm%2FeffHgaTPpO3Q02W2JsNDsAiEA3RU8BJDpeLzbjvVqE%2FojXSGn5ebi5EVJNlZJLR%2BNNcsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDOeDuVr4s%2F%2FLTno1IircA9h1j9mDcQjpNXUEiaADC6qfv4R%2FQnbSS7qj3UqRnjC2t5gkKF2mAY4j6zwEdjcQTRuL%2FQbwASwJ3QnlyJcRjFi%2F0hACJvfuHnZhE8wvSqalFY4sbrOGNJ3EpgZst8v0DUeVKmwbAbWDnlwX0HVllIAN8l97Bln08LmUqUxztLh7Pmf4qnMOn0NN9o4frBX%2BfTE3MYiKTadnsSe2JNEr4rYS3LfYWq1Uc2WcGKZvfZMc1u3t16JXkilmfvrhx8GY%2BT0TpexM2DTnKl%2FgSC%2B6LR6s0K%2F1D0WDLWcPuRddq9i%2BF4Qtsnu1RQ4xAx3ZarQPimINbtZv%2BNGDwnadIZNfEp5IzjD%2FzJHsEigLIvISBFMeGeFcuc9pxt5XMbbqxIqufgVrM%2Bls4kDgvfPVd1xXL2Zz1VctNKYUOms1Re8le5ArDuDXNs31aepESiYMMhEEN0KFlr0x%2FHtF6Hhk3y9jj3iokcH0mpt1hfIYyvCx1WzTSm6LnQwqsFpUWpko2XO6%2BvlFG33ctuwMAhV0vVRZForBex2fF5wERRQXQXthVUJ4cQUSJxbuiMcocrjG72l93d%2BLDlG8r8h6PZpdCJ%2FMYvtfxL9hSeMoDpDIWTpsrSl6QzHBK3dCP1YctiYnMMaImtMGOqUBewuVY76Bh1Wp708Ev%2B7geFMyMeaFPIQxFtV9Fy7QCLmnGpZsgNgaMUJ7RCDNFROCbtgeZvQaEhjGEv04XFu2rS2EiYo5%2BpzuJePUcaT67AIklJewBs9ShetJQin2EqSxdldvwzS3riUEo1BCdc%2FtI0yM3SR4FBHAJ7RIxnnXObEECwhA7NuSmTk%2B5tPxxN%2FZX9XYE%2FlXHwvo6urBTZSWCYdhmmRm&X-Amz-Signature=215791469d71a8affecb4544b6823da6d8e9abd45dac7443cb95f52cc593f4da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOYKNUOQ%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T224824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIHho0co2JbdHRCv5AxF9Qm%2FeffHgaTPpO3Q02W2JsNDsAiEA3RU8BJDpeLzbjvVqE%2FojXSGn5ebi5EVJNlZJLR%2BNNcsq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDOeDuVr4s%2F%2FLTno1IircA9h1j9mDcQjpNXUEiaADC6qfv4R%2FQnbSS7qj3UqRnjC2t5gkKF2mAY4j6zwEdjcQTRuL%2FQbwASwJ3QnlyJcRjFi%2F0hACJvfuHnZhE8wvSqalFY4sbrOGNJ3EpgZst8v0DUeVKmwbAbWDnlwX0HVllIAN8l97Bln08LmUqUxztLh7Pmf4qnMOn0NN9o4frBX%2BfTE3MYiKTadnsSe2JNEr4rYS3LfYWq1Uc2WcGKZvfZMc1u3t16JXkilmfvrhx8GY%2BT0TpexM2DTnKl%2FgSC%2B6LR6s0K%2F1D0WDLWcPuRddq9i%2BF4Qtsnu1RQ4xAx3ZarQPimINbtZv%2BNGDwnadIZNfEp5IzjD%2FzJHsEigLIvISBFMeGeFcuc9pxt5XMbbqxIqufgVrM%2Bls4kDgvfPVd1xXL2Zz1VctNKYUOms1Re8le5ArDuDXNs31aepESiYMMhEEN0KFlr0x%2FHtF6Hhk3y9jj3iokcH0mpt1hfIYyvCx1WzTSm6LnQwqsFpUWpko2XO6%2BvlFG33ctuwMAhV0vVRZForBex2fF5wERRQXQXthVUJ4cQUSJxbuiMcocrjG72l93d%2BLDlG8r8h6PZpdCJ%2FMYvtfxL9hSeMoDpDIWTpsrSl6QzHBK3dCP1YctiYnMMaImtMGOqUBewuVY76Bh1Wp708Ev%2B7geFMyMeaFPIQxFtV9Fy7QCLmnGpZsgNgaMUJ7RCDNFROCbtgeZvQaEhjGEv04XFu2rS2EiYo5%2BpzuJePUcaT67AIklJewBs9ShetJQin2EqSxdldvwzS3riUEo1BCdc%2FtI0yM3SR4FBHAJ7RIxnnXObEECwhA7NuSmTk%2B5tPxxN%2FZX9XYE%2FlXHwvo6urBTZSWCYdhmmRm&X-Amz-Signature=8d2df0dee09ea08b81adb992c3137162c70c64774a08f31e08bd98c0cd2a6e21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
