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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXJV7EAK%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T161850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIECTwwDRC5Bas7rLP6smSyjQs5xX6urvBRUm%2FFFkhAeAAiEAjc7KO3g4Wr%2FFtp4S%2Bppv%2B84xybJliMS9C5tBxayy56gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDElr%2BMGtp1pq8PCVXircAyXEsusIxVOUAU1WwuPnzU3yMXyoGe%2B5PwjE4QoTzu6RSOI3MwIQSTbD858gzwOV2jJH50FQLgmGJCc9ow983FDuywOXM4FLzSOATSkMgjAdHvbPQdP%2Frvxa2JcChd0yfW6nPTVxnLYh2o2rzcZUnAYykp%2FAKFh9Rbee1aHHtPgqrq5lyUvuSXaqWs8Qufp7qbrCJBdoT7YrGGc8npacz2XhmcSLCupiYrS1EEwAMRhkRWxod1kAUY%2Fw0fPXbqiNxt09tS5rM8Szf%2FqeToQrwANYRU8hj3tETjJ9rlRRpqLb4oRGQplYpwgbjrWrqucsCITOUzn%2FHBQbTlbMrxTCkSqpDf%2BVjdeoD9XRYDLRh3ONtz7GtLhcuN92EGtGLTl9adXN40fvXCmjyUSl9ku8%2FoO9Y8a%2BtuwmpwROgeEydNywpPyvY2ParI2LCh0BCMSV85UVVeSfnVYC5qieJYDxfg2PXKnoJze2z4xpEEsP1gvjvqbK5QObKU8EueaekRUGsea9qsngkEJAeCtQoNyu5Tcf%2Byeq9OD3VJdlwroDLsWYnmCwDoSiCFSYa8xfWmmrbh9Vn3zzYZ%2BMDRU4HiLhjVQG%2Bhx8JwyLAmNqlBzFODt2lmnKGBr8GMQpePVlMPOe3dMGOqUB6fWccbOvN%2BGdl%2FB%2FDPBeDvHnBGy0YuA2SCyLZg5Hin972AzwgGjXa1tOmb9Yb75KBAL%2FZO0TmaADYS31KyNpsSXA8qdZxu3fWazKOTLQEszI1P8YX%2FZCTj5ek%2Bips4KBTYTOLb%2FO%2FiUcovTOzX74gzqZ6xCZzId0OwvoLaTkxyGvyCkdSa%2BfbsnH4641rzhaMIylQwymBpjNafBIl%2Ft4%2By8Z6czX&X-Amz-Signature=1a4cb33f3c17e9d9776a3728d3c17244f6f4952b44a33a5815dd1bee163160cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXJV7EAK%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T161850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIECTwwDRC5Bas7rLP6smSyjQs5xX6urvBRUm%2FFFkhAeAAiEAjc7KO3g4Wr%2FFtp4S%2Bppv%2B84xybJliMS9C5tBxayy56gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDElr%2BMGtp1pq8PCVXircAyXEsusIxVOUAU1WwuPnzU3yMXyoGe%2B5PwjE4QoTzu6RSOI3MwIQSTbD858gzwOV2jJH50FQLgmGJCc9ow983FDuywOXM4FLzSOATSkMgjAdHvbPQdP%2Frvxa2JcChd0yfW6nPTVxnLYh2o2rzcZUnAYykp%2FAKFh9Rbee1aHHtPgqrq5lyUvuSXaqWs8Qufp7qbrCJBdoT7YrGGc8npacz2XhmcSLCupiYrS1EEwAMRhkRWxod1kAUY%2Fw0fPXbqiNxt09tS5rM8Szf%2FqeToQrwANYRU8hj3tETjJ9rlRRpqLb4oRGQplYpwgbjrWrqucsCITOUzn%2FHBQbTlbMrxTCkSqpDf%2BVjdeoD9XRYDLRh3ONtz7GtLhcuN92EGtGLTl9adXN40fvXCmjyUSl9ku8%2FoO9Y8a%2BtuwmpwROgeEydNywpPyvY2ParI2LCh0BCMSV85UVVeSfnVYC5qieJYDxfg2PXKnoJze2z4xpEEsP1gvjvqbK5QObKU8EueaekRUGsea9qsngkEJAeCtQoNyu5Tcf%2Byeq9OD3VJdlwroDLsWYnmCwDoSiCFSYa8xfWmmrbh9Vn3zzYZ%2BMDRU4HiLhjVQG%2Bhx8JwyLAmNqlBzFODt2lmnKGBr8GMQpePVlMPOe3dMGOqUB6fWccbOvN%2BGdl%2FB%2FDPBeDvHnBGy0YuA2SCyLZg5Hin972AzwgGjXa1tOmb9Yb75KBAL%2FZO0TmaADYS31KyNpsSXA8qdZxu3fWazKOTLQEszI1P8YX%2FZCTj5ek%2Bips4KBTYTOLb%2FO%2FiUcovTOzX74gzqZ6xCZzId0OwvoLaTkxyGvyCkdSa%2BfbsnH4641rzhaMIylQwymBpjNafBIl%2Ft4%2By8Z6czX&X-Amz-Signature=5365936b7dac547ccc07b1514acbe4f526db9f2b0fd794470125c83dd71ef0ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
