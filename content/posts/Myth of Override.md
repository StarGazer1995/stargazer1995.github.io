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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OWL3OZL%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T142603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDopI6uIgwK2WLKWOJC9Bc1kuVOMkK0OvSEL5WdRC86YQIgUvt68MPJsbMVDSaDMMNqNxAdxE3qtUqFOeLi2RSWCoYqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC1cgp4carqz8X4lBSrcA1pKRqM%2BBAX8FFaAzsk%2Bua20un%2FzNlx4PLIb6SFFvkqyvdMyZTHVxNoFQcaGfVfMrACje5qy5gCNPgNkWVdfPA5K2iEW7ci2bbf04QjLU0oK13Tdm%2BJ%2BInZidZ3lGBPHO1cd9IiMa9U6TXGjgc0zjJByf5zFAzeVKOG%2FS8jUz9xEt79u4TC3Rn5fiPoK%2FthDiD7BhnMAfdsvFWEbSe4yCV3wuXCFOErmaRrBrRV5ZdFXlOKyuoPliZuyKDB2DkbQ0pddE2dgw0oAf4tM%2F%2B2lTXDnZVnUWYmC2Uo%2FeSQJRhyChnNSCAJAv6MerjM61aNj3i%2FQoc555VzIxhiWFRocKKwiML%2F17nEtLJdXXBKWbszGhschSkbnOOP3GRgOLtTYc5etP1mDrPJ10MJbvNGj8xDi5vLe12V6kbLH3zAlxw1r8LvWasISOstOInVRJYFroILN2g9770QHnQNbKGQO7AAg3a87311kpY8G2DIOTlUTERLQ6S3zJ9CWgO83dZfDMJm1QlwioSQ06fbRrywr3L91aJArMzYBm5FO31H1J9FPu84jRWuKjn%2BO3p0RnYc%2FNR29wjOS1sdZc6EBKj9EFYlEIm7rwPt2v8KmtMiWP60vzqmsJKwQTmR86E%2BfMIXpm9QGOqUBUixJOOMtvbIdtCpk%2FQmRvrp1Yd95LuVSNXeITJ6L9MuOPABa4CR730drqYOp29zscjRDtrPgx2dIVOHfBsKLsrk62dgWQceHvt0I7QmuHyxjVCTm6cpFQpSLBHA6RiSqkTPRctVxUv2r5%2F8MyiHNWTubqDudbJu1OCbxR2LW%2FL5zjGh7CQoGK%2B6IyeMJ1fGBbeeWhr%2BNV1hiIRHGxnyU%2B7NiBBMK&X-Amz-Signature=a304728f6952067bff27acc644b1379d8d10ee0cd08b2bffa7e111e645b33aea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OWL3OZL%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T142603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDopI6uIgwK2WLKWOJC9Bc1kuVOMkK0OvSEL5WdRC86YQIgUvt68MPJsbMVDSaDMMNqNxAdxE3qtUqFOeLi2RSWCoYqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC1cgp4carqz8X4lBSrcA1pKRqM%2BBAX8FFaAzsk%2Bua20un%2FzNlx4PLIb6SFFvkqyvdMyZTHVxNoFQcaGfVfMrACje5qy5gCNPgNkWVdfPA5K2iEW7ci2bbf04QjLU0oK13Tdm%2BJ%2BInZidZ3lGBPHO1cd9IiMa9U6TXGjgc0zjJByf5zFAzeVKOG%2FS8jUz9xEt79u4TC3Rn5fiPoK%2FthDiD7BhnMAfdsvFWEbSe4yCV3wuXCFOErmaRrBrRV5ZdFXlOKyuoPliZuyKDB2DkbQ0pddE2dgw0oAf4tM%2F%2B2lTXDnZVnUWYmC2Uo%2FeSQJRhyChnNSCAJAv6MerjM61aNj3i%2FQoc555VzIxhiWFRocKKwiML%2F17nEtLJdXXBKWbszGhschSkbnOOP3GRgOLtTYc5etP1mDrPJ10MJbvNGj8xDi5vLe12V6kbLH3zAlxw1r8LvWasISOstOInVRJYFroILN2g9770QHnQNbKGQO7AAg3a87311kpY8G2DIOTlUTERLQ6S3zJ9CWgO83dZfDMJm1QlwioSQ06fbRrywr3L91aJArMzYBm5FO31H1J9FPu84jRWuKjn%2BO3p0RnYc%2FNR29wjOS1sdZc6EBKj9EFYlEIm7rwPt2v8KmtMiWP60vzqmsJKwQTmR86E%2BfMIXpm9QGOqUBUixJOOMtvbIdtCpk%2FQmRvrp1Yd95LuVSNXeITJ6L9MuOPABa4CR730drqYOp29zscjRDtrPgx2dIVOHfBsKLsrk62dgWQceHvt0I7QmuHyxjVCTm6cpFQpSLBHA6RiSqkTPRctVxUv2r5%2F8MyiHNWTubqDudbJu1OCbxR2LW%2FL5zjGh7CQoGK%2B6IyeMJ1fGBbeeWhr%2BNV1hiIRHGxnyU%2B7NiBBMK&X-Amz-Signature=79855a08f60fe7f7cc0c2e962b2ac8fc02745ba9f73f8ec6c3467bf31b89524f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
