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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S72LNK75%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T121932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCss8xUMRRY1PRKWnd6iF%2FOMQnI2wH0WP7ph5ek255wGwIhAJDI9bGBjacjZmKrCq%2Fh8fmNyPMzCI4NmX05GHi3dVhYKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcA%2BRdOBYsF2wSgD8q3APou5eFSzp%2Bted9i60mWf3c9McBfMLDlebUxkbgDzy19vE5AFuNnJbjr14AbwryPFonjg%2BsNpf%2BKwJsL2MfIAfTXKIC2nzR0uKkoRkObFKT2il1TY6TJajDtmS5%2BPQQc5swNFaorFLAoaGeqTFEPRooM51MwyQ119o8L%2BuUhwZ6bKHsdYxm8CiocNx6qlY2ar7DOO%2FGWwJM3RwsvyWG1Ul%2FUpQbPzBJ%2FOb%2B7X1NbKsW4LkuEFt8UzvQmU5xOziU09csIYPV2PiseX4sheSW5O%2Fyrm9Ci0M%2BNhAb6CyuVQgk%2F4wawt54x4ZWKPUXkVpJoHkDLVS3rnAR5YNfSp6Hi0ed%2F8sAsWatr0U8CnIs0Sc1A8ltLdwmgvwcfufuSgzzk%2FXzl6%2BJfxLKBUycsn%2FjubSRPi5L1q8dG0vTludD5XIO9IfE%2BB1v2gIUJTcqhKN24SC0o3cd1QOOtHyC60NJJtDkgcFKnnFCieDWyLJY2i3mUpvWu2m37to9IRbluoG6BzjmEO8t%2F6lceIpvTl7bgRt2gUcl4EiiIV6MKYRTvhkHiIF4zNCsZGa4H5X9TMsFTCt0mL%2BsU%2BW%2FJurp4UAUs5w2nUPdRxMHg3OqB9xT9wLe2Au0eJ38czu%2B1W80WTD4p%2BXUBjqkAX4JJ545epNbeHDU192AKuqqXFDC9jhbDFY3JgICcS5XA1s9U8ADcevPp7AsSkjyyL5ogHTK%2F3nwAxBUOEa%2BBxRm429TWgBKs2zt4RBgAMVt2MMAkdv9YGci0Q2kkQ1X%2BqtE7tyaAXPIs03tHfqWsyqdIplkAUWJ2RQtwzpwhsTBA7HjDthnfBhmy4WdhxLQf1BtsckCBMjj3RXR2RpS7STdtyEE&X-Amz-Signature=e987e9ce1f1b833982ded6ee249dc43176fd74a83174b58298df3a846be61941&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S72LNK75%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T121932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCss8xUMRRY1PRKWnd6iF%2FOMQnI2wH0WP7ph5ek255wGwIhAJDI9bGBjacjZmKrCq%2Fh8fmNyPMzCI4NmX05GHi3dVhYKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcA%2BRdOBYsF2wSgD8q3APou5eFSzp%2Bted9i60mWf3c9McBfMLDlebUxkbgDzy19vE5AFuNnJbjr14AbwryPFonjg%2BsNpf%2BKwJsL2MfIAfTXKIC2nzR0uKkoRkObFKT2il1TY6TJajDtmS5%2BPQQc5swNFaorFLAoaGeqTFEPRooM51MwyQ119o8L%2BuUhwZ6bKHsdYxm8CiocNx6qlY2ar7DOO%2FGWwJM3RwsvyWG1Ul%2FUpQbPzBJ%2FOb%2B7X1NbKsW4LkuEFt8UzvQmU5xOziU09csIYPV2PiseX4sheSW5O%2Fyrm9Ci0M%2BNhAb6CyuVQgk%2F4wawt54x4ZWKPUXkVpJoHkDLVS3rnAR5YNfSp6Hi0ed%2F8sAsWatr0U8CnIs0Sc1A8ltLdwmgvwcfufuSgzzk%2FXzl6%2BJfxLKBUycsn%2FjubSRPi5L1q8dG0vTludD5XIO9IfE%2BB1v2gIUJTcqhKN24SC0o3cd1QOOtHyC60NJJtDkgcFKnnFCieDWyLJY2i3mUpvWu2m37to9IRbluoG6BzjmEO8t%2F6lceIpvTl7bgRt2gUcl4EiiIV6MKYRTvhkHiIF4zNCsZGa4H5X9TMsFTCt0mL%2BsU%2BW%2FJurp4UAUs5w2nUPdRxMHg3OqB9xT9wLe2Au0eJ38czu%2B1W80WTD4p%2BXUBjqkAX4JJ545epNbeHDU192AKuqqXFDC9jhbDFY3JgICcS5XA1s9U8ADcevPp7AsSkjyyL5ogHTK%2F3nwAxBUOEa%2BBxRm429TWgBKs2zt4RBgAMVt2MMAkdv9YGci0Q2kkQ1X%2BqtE7tyaAXPIs03tHfqWsyqdIplkAUWJ2RQtwzpwhsTBA7HjDthnfBhmy4WdhxLQf1BtsckCBMjj3RXR2RpS7STdtyEE&X-Amz-Signature=93e6935d5f05ad12df8243201d4a3c3701820bf1788a926599f24b0ca5b2f4d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
