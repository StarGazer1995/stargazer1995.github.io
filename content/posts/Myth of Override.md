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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2F27BX%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T225030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIxdSIxPkgEjtdpB6uXM89E5TxeOpQZdbTDxVZNTIFhAiEAlKfuEK0CosNJg0noeVjmUluF7l1ZYmhDKIoZ2%2BwS75wq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDI1CjC9liilNKjntZircA1NrtG3vDo%2FPjuFawTl6cKQPthPhnpnCtJQK%2FeEacbu35QQkrGAe2vwtw7DuS1el7Ryf9igP99ZXgtphRdcieauUE%2F%2BXqMZqc4KPN62bRAo0iiu5fiHS2S5aXCq2j49Tf9AruRabD5JoRKLNRFeoveRTrK579LY%2F0cXp8Pvbanvfqo3SUukZdKPQMrZsrsG%2Btl1mgekh%2FdHIkX%2BYGNz8igtc5n5Vbu0tngS31AnE3X5wJ7wfWAhtaWkTjBJYjKCNs3eXhAvFYiosuWc2Kamild4HFKYTGpipDHxrheEfQzvAZ38YSZomctXPiPFC%2F%2BVJbc6DrqfZVGoIXlV4G7iVpSYr%2FmdJONZTRmj%2BaCkcEkO5TUo1kKkuzG%2Bik0mM5UwTgqR40Dh0%2BPrqAyLWvZKZqrx15olgjB4O%2FYiBofmRhwoTU54BhkRj5ZjSPlf2dsbYy0eK9Za%2BovjEBiyv7cH%2BhGIxw6SUw2CldqeUd82wQGqhZgjoF5t3rijGt%2BgH9d3zSlNQUQxxWkhrr21Ln%2BqmpWmEb6dRzZmDpBo1LpUkr5dBSrCVhz5%2BMCNf0p497X3QCRKTfNDDEjl1cwg9N7EkXHRP5C3%2FCJ0zOP%2FDzY%2FmXQw%2Fa2CPW26un4iC3BzkMLq6pNMGOqUBM3mwEsvYl3SSYzC9wtxZ76Di5ElXmce%2BNfSCis0iJ41TKi3itjjPy%2F9ShnWxvCzTSbVDq%2BzLwXXWTSl1MHkCV%2BOge4Rfospp2oaJvY4qTQOzF7pdBkwP53e4VSsAuao1Mb1sSly6WMHODtMXWCTZr52VKzaOnSukQE8Kw64%2BVlx4TeVGxYTNRYsnlmR7mKxdnw5KFPac8M4impGnPlqBOVPYKOnO&X-Amz-Signature=6bfc39eead2fc00e49af03d8e694d5fa3b08614b99e05a16d4ff3a9ba1c6e031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA2F27BX%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T225030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIxdSIxPkgEjtdpB6uXM89E5TxeOpQZdbTDxVZNTIFhAiEAlKfuEK0CosNJg0noeVjmUluF7l1ZYmhDKIoZ2%2BwS75wq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDI1CjC9liilNKjntZircA1NrtG3vDo%2FPjuFawTl6cKQPthPhnpnCtJQK%2FeEacbu35QQkrGAe2vwtw7DuS1el7Ryf9igP99ZXgtphRdcieauUE%2F%2BXqMZqc4KPN62bRAo0iiu5fiHS2S5aXCq2j49Tf9AruRabD5JoRKLNRFeoveRTrK579LY%2F0cXp8Pvbanvfqo3SUukZdKPQMrZsrsG%2Btl1mgekh%2FdHIkX%2BYGNz8igtc5n5Vbu0tngS31AnE3X5wJ7wfWAhtaWkTjBJYjKCNs3eXhAvFYiosuWc2Kamild4HFKYTGpipDHxrheEfQzvAZ38YSZomctXPiPFC%2F%2BVJbc6DrqfZVGoIXlV4G7iVpSYr%2FmdJONZTRmj%2BaCkcEkO5TUo1kKkuzG%2Bik0mM5UwTgqR40Dh0%2BPrqAyLWvZKZqrx15olgjB4O%2FYiBofmRhwoTU54BhkRj5ZjSPlf2dsbYy0eK9Za%2BovjEBiyv7cH%2BhGIxw6SUw2CldqeUd82wQGqhZgjoF5t3rijGt%2BgH9d3zSlNQUQxxWkhrr21Ln%2BqmpWmEb6dRzZmDpBo1LpUkr5dBSrCVhz5%2BMCNf0p497X3QCRKTfNDDEjl1cwg9N7EkXHRP5C3%2FCJ0zOP%2FDzY%2FmXQw%2Fa2CPW26un4iC3BzkMLq6pNMGOqUBM3mwEsvYl3SSYzC9wtxZ76Di5ElXmce%2BNfSCis0iJ41TKi3itjjPy%2F9ShnWxvCzTSbVDq%2BzLwXXWTSl1MHkCV%2BOge4Rfospp2oaJvY4qTQOzF7pdBkwP53e4VSsAuao1Mb1sSly6WMHODtMXWCTZr52VKzaOnSukQE8Kw64%2BVlx4TeVGxYTNRYsnlmR7mKxdnw5KFPac8M4impGnPlqBOVPYKOnO&X-Amz-Signature=157ff9d117a995f7a5361996491abc45ff7a606c90807a77c897f8463919db9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
