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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOMIO7MR%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T081623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3GbDsGUjxw0vyBZK9h2RTwtCrwSCfBp8Pe62D%2FiipEgIgRJKz%2BFgfFEYy0lO3L8fNmR5njb2EW7HFRW2Bg4SMaa4q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDJ%2FoXfp9NWCidKAhTSrcA5C%2BM%2BxhLB9v1fqi18vykcUg54WeppIJHHsAnAyl1jcSblgUJd%2BkXb0tbUQ%2F4XYOwns5e25Ubao1DcLcqK2eKaNYnqAL5%2BZVG4Hx4cXZgGS95wWgy29kErmep%2BbMAod0o7hHroqXV70rAqaVU6MuneK27JYS0oQSnJ9ovk6mMZDqOYDZuWnYd8JKuH9lyVT4YJUW1Yvsk3D7ZO2LFI3vXqzSYP6I2N3iD0YExfztQ1JYmEREXq0Cr3BsrGiNDC8HUWaJnrd0FMNaGWvIqfxZH5KMETRrR2WYnABlwBciDzqY8b1r3IPsdCIx3E0LyzL2uhvVwgFjpM2EnUFoJwr5YtWodxtfAh6A%2FZAdgFZGs5Zj%2BMCYI0tZr%2BjnYTQAvvAysHWUxFqzsQLFTLpcZzSe0F6jyhFgGSpM9ZufY%2BWT33jl0m1evwRElOaDQKJbl4wV6nw34Z7P2W6%2FN5qtMKf8ZzctrI6TFhFoz780wq0pSDrn9QhINCQ2Jt9soRV0o1cEVUrpDeqEQXkdMosUe3dyI8lGXFvpBsR69qCApTjZ1szosZcVo3LGk%2FGWUhH7weMQ0y%2Bse8fh8v3pXolQTCJZ%2BMGZt45iiBaRZl%2FcEkGWN8WeqxDSdlLp%2FeUBCrPUMOTlptMGOqUBv1cxk93G9k1AHUZEs6fq3r0k3aWrVemNfe%2FOe5w34pg%2B0CG%2Fa4aCqdJGYJJn0r20YrTiMm2LpaISePaov0y6p8XWN%2BowuNZe4dk7y7%2Br4buGXowBvjBZZ0gNJSjESOXJhjOAghHFxwSPvIJChjh3nC1PL1O8dQhfhxvwlAPXgm3hbsA5NZkzHXztOqbWd8n50nS2E0hkrTORTrz338wWWmQgEl%2Fa&X-Amz-Signature=4acf693cc1abde8afdc27158d2357615dcca3870f2b1b4e2fe0d4ff8b9aaa51c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOMIO7MR%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T081623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3GbDsGUjxw0vyBZK9h2RTwtCrwSCfBp8Pe62D%2FiipEgIgRJKz%2BFgfFEYy0lO3L8fNmR5njb2EW7HFRW2Bg4SMaa4q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDJ%2FoXfp9NWCidKAhTSrcA5C%2BM%2BxhLB9v1fqi18vykcUg54WeppIJHHsAnAyl1jcSblgUJd%2BkXb0tbUQ%2F4XYOwns5e25Ubao1DcLcqK2eKaNYnqAL5%2BZVG4Hx4cXZgGS95wWgy29kErmep%2BbMAod0o7hHroqXV70rAqaVU6MuneK27JYS0oQSnJ9ovk6mMZDqOYDZuWnYd8JKuH9lyVT4YJUW1Yvsk3D7ZO2LFI3vXqzSYP6I2N3iD0YExfztQ1JYmEREXq0Cr3BsrGiNDC8HUWaJnrd0FMNaGWvIqfxZH5KMETRrR2WYnABlwBciDzqY8b1r3IPsdCIx3E0LyzL2uhvVwgFjpM2EnUFoJwr5YtWodxtfAh6A%2FZAdgFZGs5Zj%2BMCYI0tZr%2BjnYTQAvvAysHWUxFqzsQLFTLpcZzSe0F6jyhFgGSpM9ZufY%2BWT33jl0m1evwRElOaDQKJbl4wV6nw34Z7P2W6%2FN5qtMKf8ZzctrI6TFhFoz780wq0pSDrn9QhINCQ2Jt9soRV0o1cEVUrpDeqEQXkdMosUe3dyI8lGXFvpBsR69qCApTjZ1szosZcVo3LGk%2FGWUhH7weMQ0y%2Bse8fh8v3pXolQTCJZ%2BMGZt45iiBaRZl%2FcEkGWN8WeqxDSdlLp%2FeUBCrPUMOTlptMGOqUBv1cxk93G9k1AHUZEs6fq3r0k3aWrVemNfe%2FOe5w34pg%2B0CG%2Fa4aCqdJGYJJn0r20YrTiMm2LpaISePaov0y6p8XWN%2BowuNZe4dk7y7%2Br4buGXowBvjBZZ0gNJSjESOXJhjOAghHFxwSPvIJChjh3nC1PL1O8dQhfhxvwlAPXgm3hbsA5NZkzHXztOqbWd8n50nS2E0hkrTORTrz338wWWmQgEl%2Fa&X-Amz-Signature=c99d6382921e6f35b0baf064279afca38d58073f9a87208540270dc39363837a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
