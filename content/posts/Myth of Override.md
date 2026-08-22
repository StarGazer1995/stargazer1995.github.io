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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHUZKCBL%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T161034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgH6B2ELET7JpKYIup%2BMIX8yBWJu8x1BH19vFbZTALQwIhANn6RqA7oZCz53m3x%2BuTr6oXRoLQ6oB0ohEGngQkMBo1KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNiI0x%2F8W9woo%2F07cq3APbPEcPO8WzaetMLOQYNlenl5Hg0svpbwc0Gx0wDaWciIWVDvc9ovHX0AXkqDaGGbtWf22MIGpLTR66OsPvCMrQqf59qGiPSVdao90mWeMP0087Ly2gSEcDhQJiC1cyC11%2Fe3fxrNry%2B47%2BnUe6ml%2B408dBzTCD%2BDGDQxqu2rVHQ4cGn%2Fs92fo40KrmIKrpyR3Ycn%2Fl%2FXLHF2OghaMlxaiwPUjodjiLp3bBJkao3%2Fs9IdJ9JjyuPbr45217%2BljK%2F6iT7wtvcfxwhJgwiEbodi%2BAHB9lwlI%2BPwNZ8GNXrUEEONGSDQ0nqOuvnVXwoDC0Kf8h2wkpEZYGzws7ITroD4ffM8rjwDsv3iD4GrSyyheat43yzE%2Fb66BnnjH8tPRD954lKMIbQqvXC0DeLYPRdmGxchlbI0vG%2BRV2r9AcRVNfRaapxxoy1e%2B4kSX7bw5AwTK8XNkVkEbt6ESieQGrnKj3dunfK%2F1rpBAxbIcDclC3p9qY8mz23NIruEnNGmfSmheFqGrKgusfBakKPjy3BPhNjEGda4zyASRD2kLDFd4VSgPLM7v9Zs6P82nCl20nyWtctfoVAos%2FvhE2cVe4x14srN%2F7joScycJcFsZf%2B8%2BIjtX33xN5%2FsurHY2NoDDT9abUBjqkATNFD90AYhy3i5WuJTsfgMfMQvEUCdlof9Zw8bu7boadtdCuzEKaPUMOu8KZJgNSoViKYBvo6qLLpzwBHMxWlPg6QD6llWyBvLeCbcywJdXznbX94UA0d3i2NP7O83Z49AphD0Qp6c4EytYkuln5HSq%2BlifH2Tpn5u6pflftPykTXmCR1VIICkD4UGVilAZR%2BdV751WfGhpa4cX0EyMnJAxD8GAB&X-Amz-Signature=c7d1364a228b0d7e67aee070a2fa6e177dd0a14f2412d110a0297a6db67957c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHUZKCBL%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T161034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgH6B2ELET7JpKYIup%2BMIX8yBWJu8x1BH19vFbZTALQwIhANn6RqA7oZCz53m3x%2BuTr6oXRoLQ6oB0ohEGngQkMBo1KogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNiI0x%2F8W9woo%2F07cq3APbPEcPO8WzaetMLOQYNlenl5Hg0svpbwc0Gx0wDaWciIWVDvc9ovHX0AXkqDaGGbtWf22MIGpLTR66OsPvCMrQqf59qGiPSVdao90mWeMP0087Ly2gSEcDhQJiC1cyC11%2Fe3fxrNry%2B47%2BnUe6ml%2B408dBzTCD%2BDGDQxqu2rVHQ4cGn%2Fs92fo40KrmIKrpyR3Ycn%2Fl%2FXLHF2OghaMlxaiwPUjodjiLp3bBJkao3%2Fs9IdJ9JjyuPbr45217%2BljK%2F6iT7wtvcfxwhJgwiEbodi%2BAHB9lwlI%2BPwNZ8GNXrUEEONGSDQ0nqOuvnVXwoDC0Kf8h2wkpEZYGzws7ITroD4ffM8rjwDsv3iD4GrSyyheat43yzE%2Fb66BnnjH8tPRD954lKMIbQqvXC0DeLYPRdmGxchlbI0vG%2BRV2r9AcRVNfRaapxxoy1e%2B4kSX7bw5AwTK8XNkVkEbt6ESieQGrnKj3dunfK%2F1rpBAxbIcDclC3p9qY8mz23NIruEnNGmfSmheFqGrKgusfBakKPjy3BPhNjEGda4zyASRD2kLDFd4VSgPLM7v9Zs6P82nCl20nyWtctfoVAos%2FvhE2cVe4x14srN%2F7joScycJcFsZf%2B8%2BIjtX33xN5%2FsurHY2NoDDT9abUBjqkATNFD90AYhy3i5WuJTsfgMfMQvEUCdlof9Zw8bu7boadtdCuzEKaPUMOu8KZJgNSoViKYBvo6qLLpzwBHMxWlPg6QD6llWyBvLeCbcywJdXznbX94UA0d3i2NP7O83Z49AphD0Qp6c4EytYkuln5HSq%2BlifH2Tpn5u6pflftPykTXmCR1VIICkD4UGVilAZR%2BdV751WfGhpa4cX0EyMnJAxD8GAB&X-Amz-Signature=073791bfdcd7ac2224a979bd073bb949bde0113a75ca62c84cb08220d459569b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
