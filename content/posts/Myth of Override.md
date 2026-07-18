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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLZN4KD3%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T091507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfWjN%2BnbzkPQ9235YF4zvRIFWmdhizCPlrZz1YGgAmmwIgfFt8o3OZstnIWjJXNozZz%2FeICJIVhWzEaCx8BsWmdVMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDCQfJ6F3oDOj4de6ZircA8tZQ4Dgr11mLc2Tsjw%2BFMJlsCxQMshAROGHBRB64aImgsutlkV%2FR9unGJWVSPA3OWkNZkHdwiqlhJM5V76LewEgUaU1CZSIol6aI8NOA4l4QBRBH%2BjhryOgZk%2Bq1IUZcBF2hipoOYyK7AMhvxm%2Bxlv13VNxG0xC3o8g%2BMKjzYnmdbo5lxU9vCkObcgnM1vKY%2BtaMZKBRc54uTa%2B2Mxl0bKggRzAoRlp93E12byj4S2tH8XZeNHx073POS77NmmMXrzDMy1ByR5ocXTaiHhW2qrWhy0z4QE8zjLNw8mj%2FZ3ElDipgDHm6ADVE2HVMLzBAPgbSPgcxQodov%2B6nlbGz1z0c9sVoRKvQzhog1TqmKJoONQKpR9JZA%2B52%2BAfcnpwmmZjhPHGA39dbVG2kyoYzprEExP8TWpT3DEYzJrlC9VKeQmyEDkdaoFTdAOmY8zDzEPi%2B%2FhXgdQR32hGZ1L1vB6HhebbOViAMdpw2ZIObr6bFeY9015i4oEwQCPy4Tmmwt9iCV5EhtXsSawpfv2gAPU906k%2FCLb2HrP1Ir6if75k1gOl8pioDxGPTDUEVmuJyDGhbm2NhOZAQx7kHkFng%2F9c%2FkEnDF1F2dW7KGekMmxzpqpQZTY7jqEjvP0PMIzx7NIGOqUBW0eqpFRPWFh3E6rnS2jxyq6Kq%2BBqvY%2BFleK9qNE14i8QevloAT9Q145aDgfhZimwI3Y3miifDqMdvk54xTXYqLls4DeWoZym8OAONh0WnWotSu0eY8%2FG2bMXrZE0j23N6hX6rk6XW9CFpkcCtMLBavSC8Qv3wUBf0byKaIQ3NcMIgpU4S%2BboUKdViZfWp%2BbV%2F33R1iLuQEqBEmMsX5zHwY9YI0Rz&X-Amz-Signature=2b787e26ae2fbcb45709d54e370e8674fede27c1218f49e883424d8e662de85d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLZN4KD3%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T091507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfWjN%2BnbzkPQ9235YF4zvRIFWmdhizCPlrZz1YGgAmmwIgfFt8o3OZstnIWjJXNozZz%2FeICJIVhWzEaCx8BsWmdVMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDCQfJ6F3oDOj4de6ZircA8tZQ4Dgr11mLc2Tsjw%2BFMJlsCxQMshAROGHBRB64aImgsutlkV%2FR9unGJWVSPA3OWkNZkHdwiqlhJM5V76LewEgUaU1CZSIol6aI8NOA4l4QBRBH%2BjhryOgZk%2Bq1IUZcBF2hipoOYyK7AMhvxm%2Bxlv13VNxG0xC3o8g%2BMKjzYnmdbo5lxU9vCkObcgnM1vKY%2BtaMZKBRc54uTa%2B2Mxl0bKggRzAoRlp93E12byj4S2tH8XZeNHx073POS77NmmMXrzDMy1ByR5ocXTaiHhW2qrWhy0z4QE8zjLNw8mj%2FZ3ElDipgDHm6ADVE2HVMLzBAPgbSPgcxQodov%2B6nlbGz1z0c9sVoRKvQzhog1TqmKJoONQKpR9JZA%2B52%2BAfcnpwmmZjhPHGA39dbVG2kyoYzprEExP8TWpT3DEYzJrlC9VKeQmyEDkdaoFTdAOmY8zDzEPi%2B%2FhXgdQR32hGZ1L1vB6HhebbOViAMdpw2ZIObr6bFeY9015i4oEwQCPy4Tmmwt9iCV5EhtXsSawpfv2gAPU906k%2FCLb2HrP1Ir6if75k1gOl8pioDxGPTDUEVmuJyDGhbm2NhOZAQx7kHkFng%2F9c%2FkEnDF1F2dW7KGekMmxzpqpQZTY7jqEjvP0PMIzx7NIGOqUBW0eqpFRPWFh3E6rnS2jxyq6Kq%2BBqvY%2BFleK9qNE14i8QevloAT9Q145aDgfhZimwI3Y3miifDqMdvk54xTXYqLls4DeWoZym8OAONh0WnWotSu0eY8%2FG2bMXrZE0j23N6hX6rk6XW9CFpkcCtMLBavSC8Qv3wUBf0byKaIQ3NcMIgpU4S%2BboUKdViZfWp%2BbV%2F33R1iLuQEqBEmMsX5zHwY9YI0Rz&X-Amz-Signature=dc0e68a44f223d38bb541c68bbe7f7ab4455fd17f23aad1477bb6314baee190e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
