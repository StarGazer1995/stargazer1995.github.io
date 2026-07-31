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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD7QKCIB%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T012929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3Vl%2FLanxh3utYtdPN3mX4oQmDJRJ1ikIkKOzCD6kavAiEA7GYEpw29aHmgKO%2BJUzZqIjvMfLUX5jDdO6QCowDmbNAqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7U%2B0zcaxbrJ9u3NyrcA2Ls%2FbjRMjvE5Z8e0EP6w4KuyjnVZVvJeEa8sv7nMV3KtuU3fvqrVt3XNpef9XyVotY6y9K791iXYTVl1vwYtyVsuV6YQpCAIMyUzln21BE3KzxnFAuY1Nu1xxOvPt4DPmncfaNu%2BX3dqT3Cie9hX%2BZk%2FCMEDg2aDDafBqQ37LsXsm326MmHLOsimko2A6x1AFJ30zoUE7a73ZY0ZTq1ureC3dIiZHZUzpQPwzYrrhiuQqRLfIsVm3TGP9W5CYR8b3h5mlg0Ugnk8usp09PBLo5tR%2FDv2qn%2FJZ5V2zMhhz8fJb0I0HNaNReM2D2Jf0AIwcGjt3Uo5owsfZEDXFZ6a5JINVbjUUWtevWNSnQPVgZVDvGvIPtgPmt2Lb2SbKDQAI4UKu9C0lKChJCqR1T6Gr1tJouyu08Z4HlBrU%2FUcvMf5XsI9BRh%2B5vcEZaKHGeots2vZ9og95CyMBAuVSVuXw4zfnDI53tW6zI3eqsY2wZFQYLpS%2BbUc1%2BPEylkA0tT7JPN13cJ%2FwZaNsYCe3RUjPHMtv4vfRKzXjVDgwqSndVWd2kX3ngt0kkTct9aTZqZabf5I0rYKKe3mitowywgZM1BvSnH9Li84wIr1pN4vtvFSW8lVygI9%2BwYm2VzMLXvr9MGOqUBOxB1Vq6JSGUdkXm5WPaEFgD6%2B64JwOIZwZ514Mjy0P2RRzR2TIFq0M%2BVA5iUBSrG1dZCmC%2BkWbf1xezR1y3c4StP5Ipd12WYZ4NekBQCUdfGHrVsLCuzrSryHHW1O70Nn3CsVp%2BT4OI1nzp4Zbq1D0KVcuEve%2FfE6HEaqy5GVl5ofhJrCdjDK3vpdRd2tXAQ1RdqHYur0zU2beW%2F%2FL3ZKFDXolqB&X-Amz-Signature=d92c52e1fb53ae0dd0fdb1dff33efb9b7376f218f11cb21ab4ecef6c8b6e460b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD7QKCIB%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T012929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3Vl%2FLanxh3utYtdPN3mX4oQmDJRJ1ikIkKOzCD6kavAiEA7GYEpw29aHmgKO%2BJUzZqIjvMfLUX5jDdO6QCowDmbNAqiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7U%2B0zcaxbrJ9u3NyrcA2Ls%2FbjRMjvE5Z8e0EP6w4KuyjnVZVvJeEa8sv7nMV3KtuU3fvqrVt3XNpef9XyVotY6y9K791iXYTVl1vwYtyVsuV6YQpCAIMyUzln21BE3KzxnFAuY1Nu1xxOvPt4DPmncfaNu%2BX3dqT3Cie9hX%2BZk%2FCMEDg2aDDafBqQ37LsXsm326MmHLOsimko2A6x1AFJ30zoUE7a73ZY0ZTq1ureC3dIiZHZUzpQPwzYrrhiuQqRLfIsVm3TGP9W5CYR8b3h5mlg0Ugnk8usp09PBLo5tR%2FDv2qn%2FJZ5V2zMhhz8fJb0I0HNaNReM2D2Jf0AIwcGjt3Uo5owsfZEDXFZ6a5JINVbjUUWtevWNSnQPVgZVDvGvIPtgPmt2Lb2SbKDQAI4UKu9C0lKChJCqR1T6Gr1tJouyu08Z4HlBrU%2FUcvMf5XsI9BRh%2B5vcEZaKHGeots2vZ9og95CyMBAuVSVuXw4zfnDI53tW6zI3eqsY2wZFQYLpS%2BbUc1%2BPEylkA0tT7JPN13cJ%2FwZaNsYCe3RUjPHMtv4vfRKzXjVDgwqSndVWd2kX3ngt0kkTct9aTZqZabf5I0rYKKe3mitowywgZM1BvSnH9Li84wIr1pN4vtvFSW8lVygI9%2BwYm2VzMLXvr9MGOqUBOxB1Vq6JSGUdkXm5WPaEFgD6%2B64JwOIZwZ514Mjy0P2RRzR2TIFq0M%2BVA5iUBSrG1dZCmC%2BkWbf1xezR1y3c4StP5Ipd12WYZ4NekBQCUdfGHrVsLCuzrSryHHW1O70Nn3CsVp%2BT4OI1nzp4Zbq1D0KVcuEve%2FfE6HEaqy5GVl5ofhJrCdjDK3vpdRd2tXAQ1RdqHYur0zU2beW%2F%2FL3ZKFDXolqB&X-Amz-Signature=25decd16c06f23b8ee5a51c6d69f26c8958a77a04ed0d28e881a5a4750f2f30b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
