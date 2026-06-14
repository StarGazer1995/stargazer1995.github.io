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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KVVLDYA%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T114938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIFl6uwKVgCpHgP70aNvl4VIXrabZOR%2BCdOFt2ar9uX5GAiEAwOQxUb5NWO%2B90e0e5bv66wyJ%2FMMfaooHyrbWF5P4baEq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDNCbDFM0YGSHchWfwCrcA%2FP7vB9cGpXWpAcI7ty%2Fb2EhOFbQWDbhmjPBNf9TR6o9aDigs1dwVIXXRw3OueSsisb%2FpaDI2UwQSbwob6JL81pfCgeVCoWpM8Mb4jUYR6L7MU%2F9QvnlpRP6nszuAQIYXRwIByJBt9o6SBy4WP6BCFmM7t8fdEfNP1sMdQFJOqxp%2FiEMCh9QLFXwCoU93zOtub8Ytyxs0%2BUPx8y9PaZGGIhT2tkFhtDZzXOzmrcBkRKpaWyHG51EneOvy2zXxmtECotq1WCs4kcDReOqJBPfSa9cyFpevizShcX6HvC01QPu7bwxhXXyjA%2F1xbDcIzA5wmv78JCorh1HYe83Kusb%2BZMRKWrC%2FhX8zsbgqonpIXAhvP1ZxtPAI32SAt9ZSbH%2BCloYw13ibJP9jaxroC%2FzbAExL8OhUxpAANdoVOcgOJ1W5nYWIoz77SHdJssisjOrc7ALEuaE2SW0xmLAS94xBj%2BK1LfUQkFcOU0QOdYBEwFU4Nb4NlvuRpRxcSMzHKws%2Fl5WwBfjWN4TB57HbRcehXLBgXZIyLhTlscFxP8ZZOpbXCwxb1xZz%2B4bVSlH0jiB8MQv9GTF83hfwKknl0%2F6Z6nxbgvMDszi0d9jaIr8GPiWHemqkVNMNtJ16V92MMnGudEGOqUB1LBffAWrs%2FYZTyDNel4%2BhNgIS0ejU1C4v2lGitSX0h26AUNtrjFexXeIwRv3R2Gk9gBrA55mTrIMZAAsdRPqE9cbNGHFMiYpDibOS4vhoPhuQshhUV5fEreGhvQHwlXmKf%2BAIb%2FUtjRaHnj%2BxZsMf%2FAJZQ0Q9OgjIHf%2BRazJH%2BipM5PpZrNi3Syr85FUrHO7n0TzW%2BL0Ko78k8CDjYx7DRkHiCMr&X-Amz-Signature=4ee0ab6ab73695aa7acdf9a9078a770607b230a2d0497b83e2edbf261026a0aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KVVLDYA%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T114938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIFl6uwKVgCpHgP70aNvl4VIXrabZOR%2BCdOFt2ar9uX5GAiEAwOQxUb5NWO%2B90e0e5bv66wyJ%2FMMfaooHyrbWF5P4baEq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDNCbDFM0YGSHchWfwCrcA%2FP7vB9cGpXWpAcI7ty%2Fb2EhOFbQWDbhmjPBNf9TR6o9aDigs1dwVIXXRw3OueSsisb%2FpaDI2UwQSbwob6JL81pfCgeVCoWpM8Mb4jUYR6L7MU%2F9QvnlpRP6nszuAQIYXRwIByJBt9o6SBy4WP6BCFmM7t8fdEfNP1sMdQFJOqxp%2FiEMCh9QLFXwCoU93zOtub8Ytyxs0%2BUPx8y9PaZGGIhT2tkFhtDZzXOzmrcBkRKpaWyHG51EneOvy2zXxmtECotq1WCs4kcDReOqJBPfSa9cyFpevizShcX6HvC01QPu7bwxhXXyjA%2F1xbDcIzA5wmv78JCorh1HYe83Kusb%2BZMRKWrC%2FhX8zsbgqonpIXAhvP1ZxtPAI32SAt9ZSbH%2BCloYw13ibJP9jaxroC%2FzbAExL8OhUxpAANdoVOcgOJ1W5nYWIoz77SHdJssisjOrc7ALEuaE2SW0xmLAS94xBj%2BK1LfUQkFcOU0QOdYBEwFU4Nb4NlvuRpRxcSMzHKws%2Fl5WwBfjWN4TB57HbRcehXLBgXZIyLhTlscFxP8ZZOpbXCwxb1xZz%2B4bVSlH0jiB8MQv9GTF83hfwKknl0%2F6Z6nxbgvMDszi0d9jaIr8GPiWHemqkVNMNtJ16V92MMnGudEGOqUB1LBffAWrs%2FYZTyDNel4%2BhNgIS0ejU1C4v2lGitSX0h26AUNtrjFexXeIwRv3R2Gk9gBrA55mTrIMZAAsdRPqE9cbNGHFMiYpDibOS4vhoPhuQshhUV5fEreGhvQHwlXmKf%2BAIb%2FUtjRaHnj%2BxZsMf%2FAJZQ0Q9OgjIHf%2BRazJH%2BipM5PpZrNi3Syr85FUrHO7n0TzW%2BL0Ko78k8CDjYx7DRkHiCMr&X-Amz-Signature=580ab964e2d665cb05f1b06a133dc7b4d7b34ca6ddf3bb6f6efdcc3ccb2626c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
