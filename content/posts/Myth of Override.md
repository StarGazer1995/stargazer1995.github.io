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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AALUJH6%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T225430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnrOrSC1t0VPRZs41wuwl1O2gpgPuZpFEkY6cWC0ElagIgeRZIbwCTRE2H3JJYuB6dwxk1Te6I8Wv3wUiRMkiwukYqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVu5gVMZps3QqjOEircAwsEJhZVRCA6cJPlikfFnINQ%2BdouVyiSuVgam6O%2B9IM%2FBazTdvDDDkjMvAFDaZtncaOOkP%2B6852j3RxZWmGNSSGR4364m8c0g3pxVmedt4H%2BFIUGs3Grk%2B6Vrl8nJUjpBCRVofGkiWEMJUWDlTtTNrZt%2BibZsCwODI7IV63jiQsq7MeGxonVRPdiuY1ighruwrCE5ThKXzYFg%2Bx57%2BLroO6QiGuKre%2F9hr3l7Jm6IsEg27sp17YQRMLbaU5opCrEjzsM%2BM4m4j00QvxpMxnLLWNaW5S%2BtWWh7F6uLbWdZdEICqwwkns%2FAlm0Pn4%2FJWmfhffcZnA%2BSdtM%2Bz6V5ZIJu5r3QH%2BsMmw2VoVt8yGFgbygXjgiOiZc%2Bh7V%2FnJGSEDEbzBkihrtZLD4U2ry1MJ3eG1RK5uiycqq1lWd1Zpg%2BBTwAuSQYSsYDr%2FMHTotZsk6%2FLgfy4fDI%2BD2pmNE7F%2BK8kR0PbVQk72ZCiq%2BQg9QpPsceJNG%2BLY9Kphf4ph0HznIwBoRSTBT1KbxxEkiVpPUJFzaym3Qcb2q5txV18FLIG9v%2BwBRLzI6%2BqF50icbOsGYqAmS1b505Wzw0HThOkUyYF6nPEkRxbHBl4Ce3sN%2FMX%2FlIVCNeFN3kjoObT44MPzNl9EGOqUBKjEcW1tFG0ZU6X8YxV1Xv%2F2CONDj%2BvysgCloquMQluI9EvUQIJrnUxnEZgeow7xAabyvOgTvETDCuxfUUGUPUzwXk1z2V2RFvYW5jBPQ6dTciZ9ixuKoS36Zy1X2fGZLoU76whflGusn%2BYSbyZa6RXsjWp3nssxUo8WspqKsSVUxW0XJGpWCQqkkFXFrgr6Tzs1NSxe8%2FCCs4ipBLXJVjHP%2BThWr&X-Amz-Signature=6e5d1a7308d369d0ff80d18b7290592583a9f36992ed1f6803d1a1bed32c39a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AALUJH6%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T225430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnrOrSC1t0VPRZs41wuwl1O2gpgPuZpFEkY6cWC0ElagIgeRZIbwCTRE2H3JJYuB6dwxk1Te6I8Wv3wUiRMkiwukYqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVu5gVMZps3QqjOEircAwsEJhZVRCA6cJPlikfFnINQ%2BdouVyiSuVgam6O%2B9IM%2FBazTdvDDDkjMvAFDaZtncaOOkP%2B6852j3RxZWmGNSSGR4364m8c0g3pxVmedt4H%2BFIUGs3Grk%2B6Vrl8nJUjpBCRVofGkiWEMJUWDlTtTNrZt%2BibZsCwODI7IV63jiQsq7MeGxonVRPdiuY1ighruwrCE5ThKXzYFg%2Bx57%2BLroO6QiGuKre%2F9hr3l7Jm6IsEg27sp17YQRMLbaU5opCrEjzsM%2BM4m4j00QvxpMxnLLWNaW5S%2BtWWh7F6uLbWdZdEICqwwkns%2FAlm0Pn4%2FJWmfhffcZnA%2BSdtM%2Bz6V5ZIJu5r3QH%2BsMmw2VoVt8yGFgbygXjgiOiZc%2Bh7V%2FnJGSEDEbzBkihrtZLD4U2ry1MJ3eG1RK5uiycqq1lWd1Zpg%2BBTwAuSQYSsYDr%2FMHTotZsk6%2FLgfy4fDI%2BD2pmNE7F%2BK8kR0PbVQk72ZCiq%2BQg9QpPsceJNG%2BLY9Kphf4ph0HznIwBoRSTBT1KbxxEkiVpPUJFzaym3Qcb2q5txV18FLIG9v%2BwBRLzI6%2BqF50icbOsGYqAmS1b505Wzw0HThOkUyYF6nPEkRxbHBl4Ce3sN%2FMX%2FlIVCNeFN3kjoObT44MPzNl9EGOqUBKjEcW1tFG0ZU6X8YxV1Xv%2F2CONDj%2BvysgCloquMQluI9EvUQIJrnUxnEZgeow7xAabyvOgTvETDCuxfUUGUPUzwXk1z2V2RFvYW5jBPQ6dTciZ9ixuKoS36Zy1X2fGZLoU76whflGusn%2BYSbyZa6RXsjWp3nssxUo8WspqKsSVUxW0XJGpWCQqkkFXFrgr6Tzs1NSxe8%2FCCs4ipBLXJVjHP%2BThWr&X-Amz-Signature=8e2e7811d57ace7fe55b8a6fa7799fa5b42a3ecb9681e85aaadcb9d4e950502e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
