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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG62DR4T%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T130242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIDJ4UXhCgR46Pl1Mw5sb9kMBVSHJHwGwDDfVWzwtHrORAiBaN%2B%2Bh1R7EKRDvmWtQ556NlG5PTwl2U66jHUmIJWi5myr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMz37obrT2NtXntYWdKtwDXW1Shw%2Bubx%2FnAezFG9vS801shYsROZUKghD194QKQGRCKZtsZXgF%2FNoL%2FiUVmGEKDPeIPRphvvA7ShkUzzbvcJIDPf7bCZXLnCevfSzkHaMVcYBNC0%2BqmqhdOVf7dzw%2B2X59cLWOWAx2mjdo5ASGV6jBhj304jBQBj96PKRmuJitdCO5SsXNOeIXjGNAaIRbIQ6Q%2BYRNXXvHT5gABiItMjnagT9JKflagtR6rQHswZyz6kttNh4g71l%2FPlniCesE4j4sgB1Ma7e6da8bEE0oHMmFSn%2BIikCsmCA7eAMbLTc12bVKWsI862TRm%2FHYa88yaILNjs%2FA99mtVJnzZH%2Bw9Kcluvw%2FlMExuPKH6hGAshAg4nR8bTOjduZ5ycBChBRZYXqjC%2BIdRG9m4%2BIx9jcx2Adm34hFU6djs9Zx8ehfeXiYIYmREJfZHMiatH528UPwXHwhy06hMnMauDsFNKqq6BUooWLAxuj%2BHjFyjEeVqzFxISqjSeTafUYOu5kGv77gIZCWZc8I%2F6bDBD8y8CiWay9pVGsHf5CQrt5ROpE2VvOFUPHs3Ed%2BylmXXEPBubtkSBnRtAdeSk7y2LV1pPq2tA6IiPmajz9xsHPPJfmPjDLAz7eEVN3YHd176nEw6czX0gY6pgFdU%2FOFlPcJ%2BjnONCv5tkzTVuM%2F2CLago3E3rfjfnOGeaIU3bg5l63zwubHDPgnvJO3FB4mCCEI2jnnLpx0yOqhoKRWfgkVtpJUeHEVDpULi1bfm%2F4TEDy58PCcil9wJcUR4s4%2FIaRqBBfWbmnOjVYVyJy7ICXF2vrIWx6O%2Bo%2Bc1b5z37iZN9KbHNTfEemAxnhjBwW129r95AbA79jYzj6brEw%2FMKn%2B&X-Amz-Signature=35d35f6abc8b6365af1c403c6d65027474e261c6fe28f45bf5a3c035cbff5746&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG62DR4T%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T130242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIDJ4UXhCgR46Pl1Mw5sb9kMBVSHJHwGwDDfVWzwtHrORAiBaN%2B%2Bh1R7EKRDvmWtQ556NlG5PTwl2U66jHUmIJWi5myr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMz37obrT2NtXntYWdKtwDXW1Shw%2Bubx%2FnAezFG9vS801shYsROZUKghD194QKQGRCKZtsZXgF%2FNoL%2FiUVmGEKDPeIPRphvvA7ShkUzzbvcJIDPf7bCZXLnCevfSzkHaMVcYBNC0%2BqmqhdOVf7dzw%2B2X59cLWOWAx2mjdo5ASGV6jBhj304jBQBj96PKRmuJitdCO5SsXNOeIXjGNAaIRbIQ6Q%2BYRNXXvHT5gABiItMjnagT9JKflagtR6rQHswZyz6kttNh4g71l%2FPlniCesE4j4sgB1Ma7e6da8bEE0oHMmFSn%2BIikCsmCA7eAMbLTc12bVKWsI862TRm%2FHYa88yaILNjs%2FA99mtVJnzZH%2Bw9Kcluvw%2FlMExuPKH6hGAshAg4nR8bTOjduZ5ycBChBRZYXqjC%2BIdRG9m4%2BIx9jcx2Adm34hFU6djs9Zx8ehfeXiYIYmREJfZHMiatH528UPwXHwhy06hMnMauDsFNKqq6BUooWLAxuj%2BHjFyjEeVqzFxISqjSeTafUYOu5kGv77gIZCWZc8I%2F6bDBD8y8CiWay9pVGsHf5CQrt5ROpE2VvOFUPHs3Ed%2BylmXXEPBubtkSBnRtAdeSk7y2LV1pPq2tA6IiPmajz9xsHPPJfmPjDLAz7eEVN3YHd176nEw6czX0gY6pgFdU%2FOFlPcJ%2BjnONCv5tkzTVuM%2F2CLago3E3rfjfnOGeaIU3bg5l63zwubHDPgnvJO3FB4mCCEI2jnnLpx0yOqhoKRWfgkVtpJUeHEVDpULi1bfm%2F4TEDy58PCcil9wJcUR4s4%2FIaRqBBfWbmnOjVYVyJy7ICXF2vrIWx6O%2Bo%2Bc1b5z37iZN9KbHNTfEemAxnhjBwW129r95AbA79jYzj6brEw%2FMKn%2B&X-Amz-Signature=8d5c28885e8ce4552ab96a5a267bd82d6884f065df21ed6e5fd81c8b60c4ec80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
