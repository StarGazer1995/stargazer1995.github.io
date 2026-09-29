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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646I74HVW%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T142529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj3ZX0JVDC3XxDCf5WI3inj%2FbBGf1ntlWn5xnK%2BKwUZwIgetogLIK811IxTlJcmdZEbISzBQDKwRJXuJrvwjHsTuQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDGNWvbU8M2vZAeWiQircAwlc%2FZZQ8%2Fk%2BCSqSoBZNAUCIZNheMab8my543Yj2TcOuhMXfnrFjaqkbklH74sYR4%2FYBCKoe7lfik9uZy0eaPLXRTZM%2FkDmvtV5UecBUCK8CoCGJMWtFOCvNJfFloyLtNA1AUiyawrffNpHqxrkMsMacOzI1nQDHopn3mvsekfro8ckbiLgVrSZWxG3ADRvNM6Ci4s6Hjc%2FCLvkANyNqzgp%2FwK3%2Bod0RhWD%2BUdQdwfScl5bpND%2FuOnrsk44Ye6oK60mEd0rV483yav0QiSquLM%2B105ejxA%2B3WKh0AHQrnhJ%2F6JQ9eFA%2FFUC0lIKKixrZJ2N1lMvTFkWy6XVQUVsxMnJysEgfR28Zof%2FWs9u5npt7XO92dNry%2BBcGDsOjHqIpSRkTKaoMNkw0dPTxvNiiF6Ed7Lkf%2BjXjkaYPh2ayJs3h4vQnLZ38k5JR4p9RCaMTPCBSUVRK2trwxUEKrFNyxc9ekTUMPdsW3WySKL%2FuJDOyiv8aaV81esFwckrgltTiuQbTY8Ie2wMlEiZ9ZL8u2VLj6dL7MxMNxUN2Gw6vB2RiE2kKI1CyCvZI1YdU55KyCxnNb65jNI5Uew7Mn6LawhkHG4Z1LRyj7%2BBa0XWR1Kdhr%2BEHx3R87t8k5vOdMJ%2BI79UGOqUBieq9SGK6BiaAYeCRIsT0YBvFmpJsbSfycWI7LZZUIJEYX6yLNfur2pqd55iDQb1FTfuFjYgFlz8qfK3fB1O4hi1jgrHIAZ1ZlZKWa3ZcaUsR4%2B1D5qYsEZavnUp7vU5TypGOd6FhNnPuB1zE7F1NyaQCTjXO7CHm%2FcvAAvoyLFFjLVRp1Dfg29vEMuIPcrvzFlJN1Ol0SGN9ER%2BDBXwgDbd9NZZ0&X-Amz-Signature=477c40f0b51ea41ecd7072271db2812b82095e95481e4d90b7bc1dbee77f98c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646I74HVW%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T142529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj3ZX0JVDC3XxDCf5WI3inj%2FbBGf1ntlWn5xnK%2BKwUZwIgetogLIK811IxTlJcmdZEbISzBQDKwRJXuJrvwjHsTuQq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDGNWvbU8M2vZAeWiQircAwlc%2FZZQ8%2Fk%2BCSqSoBZNAUCIZNheMab8my543Yj2TcOuhMXfnrFjaqkbklH74sYR4%2FYBCKoe7lfik9uZy0eaPLXRTZM%2FkDmvtV5UecBUCK8CoCGJMWtFOCvNJfFloyLtNA1AUiyawrffNpHqxrkMsMacOzI1nQDHopn3mvsekfro8ckbiLgVrSZWxG3ADRvNM6Ci4s6Hjc%2FCLvkANyNqzgp%2FwK3%2Bod0RhWD%2BUdQdwfScl5bpND%2FuOnrsk44Ye6oK60mEd0rV483yav0QiSquLM%2B105ejxA%2B3WKh0AHQrnhJ%2F6JQ9eFA%2FFUC0lIKKixrZJ2N1lMvTFkWy6XVQUVsxMnJysEgfR28Zof%2FWs9u5npt7XO92dNry%2BBcGDsOjHqIpSRkTKaoMNkw0dPTxvNiiF6Ed7Lkf%2BjXjkaYPh2ayJs3h4vQnLZ38k5JR4p9RCaMTPCBSUVRK2trwxUEKrFNyxc9ekTUMPdsW3WySKL%2FuJDOyiv8aaV81esFwckrgltTiuQbTY8Ie2wMlEiZ9ZL8u2VLj6dL7MxMNxUN2Gw6vB2RiE2kKI1CyCvZI1YdU55KyCxnNb65jNI5Uew7Mn6LawhkHG4Z1LRyj7%2BBa0XWR1Kdhr%2BEHx3R87t8k5vOdMJ%2BI79UGOqUBieq9SGK6BiaAYeCRIsT0YBvFmpJsbSfycWI7LZZUIJEYX6yLNfur2pqd55iDQb1FTfuFjYgFlz8qfK3fB1O4hi1jgrHIAZ1ZlZKWa3ZcaUsR4%2B1D5qYsEZavnUp7vU5TypGOd6FhNnPuB1zE7F1NyaQCTjXO7CHm%2FcvAAvoyLFFjLVRp1Dfg29vEMuIPcrvzFlJN1Ol0SGN9ER%2BDBXwgDbd9NZZ0&X-Amz-Signature=83dbc538fea3afca6620df98012abada1774b55ae40af8da929f251d2516d988&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
