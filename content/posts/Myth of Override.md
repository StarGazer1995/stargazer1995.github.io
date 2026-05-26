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
cover: https://www.notion.so/images/page-cover/webb1.jpg
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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A26DVYP%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T060206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz%2FXbuXvxxV5rR9IQkq3vnU%2BA%2BWLapI7zlMJRh6AC5lQIhALspoH2fmpa42tRNLHd1Tms2EH7HH6Jh5sKSNEb4v1h5Kv8DCHMQABoMNjM3NDIzMTgzODA1IgzJApsTJIXtz1DGoy8q3AMNTXcPr57Jk3lOpewSjXwRCBOeUE1yUbYl%2BQyO9VtkRTABZhpUCNZpmMQHUNMeVpW2Sn4vtwQIN%2BnH6mKcWs6CDyNVtPxryZRbVXe6eIWhMFCuK%2Bkfkh4ZkqLZnuA50dNcKRAY95k%2Fz6jpHimELmsnIJtFdI7W%2BonBetY1B6uYZD0GJAp6pBHJZQAGSKrlSQnxlZngdpzHz3x4N0cfQ3QcOCOugke13UpkQlpxFd5YSNyVFcF2LIceItUWCVADz%2Bti9mzHzKFL3HJHsQDmZQ4iJc8%2FfC3MLjAxtgIX4Hf5m%2B%2FOqfLSeALFRyrw1W28resERE0uIpo1HlnNSqlyZh85NJdY6D80dfK%2FPNWGV0mA%2FR0BhTn0%2B8RPNNl3sDqyyHx02OYAr0YPn0DGVmFZUMH17hqC%2FKt7sh0TRF7aXqpUMBwITxxDxYV7vCF7kk%2BKUiJ1kWM7vxVcU1qhf2zKUlEKYYWU%2Beb%2BBfacySKunb06Eu27CH3hF1h0NaU3FYwuxYCGKABet%2FzYulQ2qO8zU8aVyJv%2B9D%2FGWT4GRlUeeLWAAHrhRoXALb1jGaBM7877TghQQzkitGL7cWTw1B2CMQRw99t5gRdNpmNf%2B18AvtUntqANfdchAuLwKKwqMjCx%2BtPQBjqkAXRRdVU2OCMWg5XuvKN3qqySEu7lNtwOuoC2rTd8nf60MfRsJuaGegHBiaC50GHxrdpOO%2BVJY7ynvdPkYDGqlce1g5SjYT80V%2BYLjoaK5aiHc1l0AoFPrYmGUaI%2FLDHTGfsVqBZf6gc9b5b6N%2BHuZpaceX2TBVd55p7UirL2b323NlONfPErW7AC0iDmRB0MjuSHZvOOBF57Z9csqopi7NqrpB8v&X-Amz-Signature=265c475e42b615412b14aecf41096b51db59096a8af9c73403ba9426ed9f6b73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A26DVYP%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T060206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz%2FXbuXvxxV5rR9IQkq3vnU%2BA%2BWLapI7zlMJRh6AC5lQIhALspoH2fmpa42tRNLHd1Tms2EH7HH6Jh5sKSNEb4v1h5Kv8DCHMQABoMNjM3NDIzMTgzODA1IgzJApsTJIXtz1DGoy8q3AMNTXcPr57Jk3lOpewSjXwRCBOeUE1yUbYl%2BQyO9VtkRTABZhpUCNZpmMQHUNMeVpW2Sn4vtwQIN%2BnH6mKcWs6CDyNVtPxryZRbVXe6eIWhMFCuK%2Bkfkh4ZkqLZnuA50dNcKRAY95k%2Fz6jpHimELmsnIJtFdI7W%2BonBetY1B6uYZD0GJAp6pBHJZQAGSKrlSQnxlZngdpzHz3x4N0cfQ3QcOCOugke13UpkQlpxFd5YSNyVFcF2LIceItUWCVADz%2Bti9mzHzKFL3HJHsQDmZQ4iJc8%2FfC3MLjAxtgIX4Hf5m%2B%2FOqfLSeALFRyrw1W28resERE0uIpo1HlnNSqlyZh85NJdY6D80dfK%2FPNWGV0mA%2FR0BhTn0%2B8RPNNl3sDqyyHx02OYAr0YPn0DGVmFZUMH17hqC%2FKt7sh0TRF7aXqpUMBwITxxDxYV7vCF7kk%2BKUiJ1kWM7vxVcU1qhf2zKUlEKYYWU%2Beb%2BBfacySKunb06Eu27CH3hF1h0NaU3FYwuxYCGKABet%2FzYulQ2qO8zU8aVyJv%2B9D%2FGWT4GRlUeeLWAAHrhRoXALb1jGaBM7877TghQQzkitGL7cWTw1B2CMQRw99t5gRdNpmNf%2B18AvtUntqANfdchAuLwKKwqMjCx%2BtPQBjqkAXRRdVU2OCMWg5XuvKN3qqySEu7lNtwOuoC2rTd8nf60MfRsJuaGegHBiaC50GHxrdpOO%2BVJY7ynvdPkYDGqlce1g5SjYT80V%2BYLjoaK5aiHc1l0AoFPrYmGUaI%2FLDHTGfsVqBZf6gc9b5b6N%2BHuZpaceX2TBVd55p7UirL2b323NlONfPErW7AC0iDmRB0MjuSHZvOOBF57Z9csqopi7NqrpB8v&X-Amz-Signature=c0abdf9a06212f0d2e28473b5dc63cc6af32bff90b08229fe021e76da045a595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
