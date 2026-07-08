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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEZG4QGN%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T205446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVnX867PrgJhed3R8QqNr%2Br2Uxnas5utmpzMmJkIPFFAIhAN4bEYaSfhBlJWHeT7QuBZcBFiMTgmwxMJ3DlAAg4%2F0ZKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR6iU3DD3olPPd37gq3AM%2FXXA3rtp4IfmTL%2BskKaQaylwIBJRIZSdTD%2F9iOxlHfhNBj0Lcb%2Fz0EhPve5aj9zl0O6y0MhOvvoa%2FOKhyEVSQTnki8WPO1spqZNQ6l%2FEVTuj%2FSPmM%2FT1sZPWJqzvyxfZjSw3z67IK8azPb0eMwYY6jdDgosvYWmfT%2BqwYMnJLX8JRlodYsFwzWrsb47ixn%2FnhE7f3i9yyC%2FSqNB8GwRSJ9IBngfFweUfz6Txxapn6oob%2BSBnH2alhaTFbRqRQUmNXBiWB61WbYr0JHfT8w%2BugvHcmIxeO86CDAwhnNToAK%2B8scyjv7MfHsE7zA3ascnMB5GxYqnjFTMEhS4Ye9v4A105rMs9SO6SiAbfmkIqOiC1WsBbU8JfVQtrhu8YZDEZOzqOg7auWagSSPNi%2FFaI%2FJjDOxwKsqdsptNq62ojhSDKq5b6hHGtR%2FCo4EOfiVRf0C%2BtsfERB5Sg3KLMlwripCz%2Fdmxd2EYrbSxCWgKF3l6gKyOqnerlr73q%2BT5CYTMR0%2BXDPyoiF9dYrol8P5v8uO2N6P%2FenMitNBG0W8r7s3FZjNX5gcU7GgAz0aUIdxIHlgMdk4loZxAmLqUxT7gAg20v790MPbQgESY7AMnbFrp1Xxei4U2Z0r0i9qjDCybrSBjqkAWxjbmQGR0g9TdIihNWiQmWFhFUFFvlv1QUM3opblzpj24nG2WYgez5NTg3W2cnvOChkRkeOIzHv7zHhSikuPrjc7iEykvDE4%2Fe%2Bs6VJND%2FkKdf%2FmRd5BDPOXWiEPaOWS2sW9acsjq8%2BXXkvvac7%2BwW0qNi1Egy6YI5De2xfEk6qQvGj73kWSlhlBP%2BZJS9Zwm53kxVjSXKl4QSiuwYmvF%2BO6IFX&X-Amz-Signature=fa9231a0b038a66b49f4be0b98cefa9be1936408d35d441effef8c8f2bfa3a5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEZG4QGN%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T205446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVnX867PrgJhed3R8QqNr%2Br2Uxnas5utmpzMmJkIPFFAIhAN4bEYaSfhBlJWHeT7QuBZcBFiMTgmwxMJ3DlAAg4%2F0ZKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR6iU3DD3olPPd37gq3AM%2FXXA3rtp4IfmTL%2BskKaQaylwIBJRIZSdTD%2F9iOxlHfhNBj0Lcb%2Fz0EhPve5aj9zl0O6y0MhOvvoa%2FOKhyEVSQTnki8WPO1spqZNQ6l%2FEVTuj%2FSPmM%2FT1sZPWJqzvyxfZjSw3z67IK8azPb0eMwYY6jdDgosvYWmfT%2BqwYMnJLX8JRlodYsFwzWrsb47ixn%2FnhE7f3i9yyC%2FSqNB8GwRSJ9IBngfFweUfz6Txxapn6oob%2BSBnH2alhaTFbRqRQUmNXBiWB61WbYr0JHfT8w%2BugvHcmIxeO86CDAwhnNToAK%2B8scyjv7MfHsE7zA3ascnMB5GxYqnjFTMEhS4Ye9v4A105rMs9SO6SiAbfmkIqOiC1WsBbU8JfVQtrhu8YZDEZOzqOg7auWagSSPNi%2FFaI%2FJjDOxwKsqdsptNq62ojhSDKq5b6hHGtR%2FCo4EOfiVRf0C%2BtsfERB5Sg3KLMlwripCz%2Fdmxd2EYrbSxCWgKF3l6gKyOqnerlr73q%2BT5CYTMR0%2BXDPyoiF9dYrol8P5v8uO2N6P%2FenMitNBG0W8r7s3FZjNX5gcU7GgAz0aUIdxIHlgMdk4loZxAmLqUxT7gAg20v790MPbQgESY7AMnbFrp1Xxei4U2Z0r0i9qjDCybrSBjqkAWxjbmQGR0g9TdIihNWiQmWFhFUFFvlv1QUM3opblzpj24nG2WYgez5NTg3W2cnvOChkRkeOIzHv7zHhSikuPrjc7iEykvDE4%2Fe%2Bs6VJND%2FkKdf%2FmRd5BDPOXWiEPaOWS2sW9acsjq8%2BXXkvvac7%2BwW0qNi1Egy6YI5De2xfEk6qQvGj73kWSlhlBP%2BZJS9Zwm53kxVjSXKl4QSiuwYmvF%2BO6IFX&X-Amz-Signature=5cba2116286e85dc350da24c043a76540e8205cdc523a4b2017915fe1f973e5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
