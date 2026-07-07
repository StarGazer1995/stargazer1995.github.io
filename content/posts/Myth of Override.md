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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOII3HFB%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T193136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvXtIUdzzvJF0hjgIFbDT%2BHgG0cGGt%2FxclK5YX1Mg40AiEA0yoDOEEKFEmSAnRpGrNWpEQA2CYl%2FyFRizMCLUpM3hoq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJ3gEhRbfO0Vz3daNircA5TKui7FLH8de0x%2FDm8ZDOq48l9%2BrYQKNIF8wp0F4B5vi2mGIPTMOvNgEj9VhuGAM9A6v%2BbymLkqDSqd0a9wBoEWaJsfNMzdOspIJ0XykWLOCnKuK0qaLzXu6u6ahty7hWtl7KnzqLldbftTsqkZdr7n7PNMIm42kGwiIDq7EtLO7k9RyvDY1yjoA9esjGyiRkRbJxe7clPhwJyMGT99ocqpGVUT7YJxPLdI7181sStcK6aWyne7U3amF65MjFP46uRR8mPn9XcpRM18q%2FNTIuBfArs%2BzndcCes1P%2BOrVJrfREwKHzbInQW4QhE%2BhZQ67QeSIqHXjUBhHOBqPrB8aAT8qXRDQ8rkVMNjk3vX%2ByUc2%2BxHnjZ490mm18eobgQ1YCsWkiy75mkkMgpdkDo6vzGmVuhNr2CVV%2FWYfGlonH9g1uTaAjFfrbRE34MQOzHNkTwpd1GD3UQn%2BLGphrywRRpt6jXM7gQPnQGLhRH599HNzGn63Y%2BYvf4bzGtKlbSGBdCj%2BwLnwgxzR3zyBOssTdZs6RnVLtIfBXwHnlPRef2vy8GPN28rRyojQUFMkloeHsEvrEVNV0gPurP9gWg1DVtUUPZLxEarJC2XBuAUxLcJOXOKrY54bDL78MPmMI%2BZtdIGOqUBuQTcrPmWfV7PRbA%2BWhyKYP8kfsrHrjsa46srjirGvR63yZUzFuOTNwGMUuAxTpY7lLDVrIe%2FTVy1llMj%2Fb5Z2nmPAq4gzKWszihGI2inXYvP7%2FrwGj%2Bi7AtLip3AziYx2SXUOCV1uguvixZUtUZctz%2BNoQ7MM2wy2OIB1bmWso%2BkPOSWkoiydZGK94uRM1p66pWtGRl%2B%2BvpWcM74iV9JR9cGvDhn&X-Amz-Signature=54a97a1c9df2f254a8b821fe1c61c09ffef0263856faf14d3a18d8bd13102aa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOII3HFB%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T193136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvXtIUdzzvJF0hjgIFbDT%2BHgG0cGGt%2FxclK5YX1Mg40AiEA0yoDOEEKFEmSAnRpGrNWpEQA2CYl%2FyFRizMCLUpM3hoq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJ3gEhRbfO0Vz3daNircA5TKui7FLH8de0x%2FDm8ZDOq48l9%2BrYQKNIF8wp0F4B5vi2mGIPTMOvNgEj9VhuGAM9A6v%2BbymLkqDSqd0a9wBoEWaJsfNMzdOspIJ0XykWLOCnKuK0qaLzXu6u6ahty7hWtl7KnzqLldbftTsqkZdr7n7PNMIm42kGwiIDq7EtLO7k9RyvDY1yjoA9esjGyiRkRbJxe7clPhwJyMGT99ocqpGVUT7YJxPLdI7181sStcK6aWyne7U3amF65MjFP46uRR8mPn9XcpRM18q%2FNTIuBfArs%2BzndcCes1P%2BOrVJrfREwKHzbInQW4QhE%2BhZQ67QeSIqHXjUBhHOBqPrB8aAT8qXRDQ8rkVMNjk3vX%2ByUc2%2BxHnjZ490mm18eobgQ1YCsWkiy75mkkMgpdkDo6vzGmVuhNr2CVV%2FWYfGlonH9g1uTaAjFfrbRE34MQOzHNkTwpd1GD3UQn%2BLGphrywRRpt6jXM7gQPnQGLhRH599HNzGn63Y%2BYvf4bzGtKlbSGBdCj%2BwLnwgxzR3zyBOssTdZs6RnVLtIfBXwHnlPRef2vy8GPN28rRyojQUFMkloeHsEvrEVNV0gPurP9gWg1DVtUUPZLxEarJC2XBuAUxLcJOXOKrY54bDL78MPmMI%2BZtdIGOqUBuQTcrPmWfV7PRbA%2BWhyKYP8kfsrHrjsa46srjirGvR63yZUzFuOTNwGMUuAxTpY7lLDVrIe%2FTVy1llMj%2Fb5Z2nmPAq4gzKWszihGI2inXYvP7%2FrwGj%2Bi7AtLip3AziYx2SXUOCV1uguvixZUtUZctz%2BNoQ7MM2wy2OIB1bmWso%2BkPOSWkoiydZGK94uRM1p66pWtGRl%2B%2BvpWcM74iV9JR9cGvDhn&X-Amz-Signature=e93d956a36897d13bd98bb2c740a2770186a4f7daaff7f35b1a2cfabb1e611a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
