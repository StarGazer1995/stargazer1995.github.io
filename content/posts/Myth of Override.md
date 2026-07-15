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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF3WJTXB%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T044143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIHeLm%2BO7qfq4wkJSvUdDYmrh8%2Bt5%2FxDzlWCRrT4JEJ%2BSAiABAYlRu6TwWVrgRHQK4Kfjif24h%2F%2FWQfedm65gp9cJ%2FCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMZKKZJoPK4vglwyLeKtwDUJUQNhrmG4mMF6i2huURRS6R234DhRfHbD7gwCrWZIHdiAt1AmfgEoXY2p4XLBeZoXEGnqI9WRFPJ3OxyBLPBn35h3FcWg587Q4axGZmawTcTGlLPTvUv1OzNVBpmvTkHJPIRsJuUBuOmIPCDiVCqSSQ0F2B8XTIQLzKEpaoonlTeHsswC7VnoIx07jq4BWqF%2F7v4Of3n9izLgzM6eqS7dSeHtpzGT%2FLiVX5OpF%2BT5EoyYQLrXpBjiTB%2FJ%2BISCCOVPfSfvgIaMZQ0QELmeMcQZ8H1L%2BAYA%2BrvJjBg%2BH%2BVdXaAYAjgGc7w5h9CjIM%2FRhSkRO8zU566h6b1KbfhtHZI7FIZbr7d75Y5jiOGAFOQsR%2FB3kYsa4oh3UD0GxOOmqoNTNf71EVm7G5rjYzCp7kegtx4v7gElqwMAagWc9SO7tzaOdGmfhXsQsre9x0MXbPfHjZHxQTM6jBU1cUnVfu5%2BidO3fhv4TWRpUlmw32VU3sEg4OAMTTT9NFvbN5Ju6L0kc8osb%2Fb8nxKdoZcEqkspCZ4dIpaGw5zmJXWHGb9KoxQyrbcW%2BRnIIkMpNEiFK3hZtb435uLU1GGdxtYVG0TJodwG7V%2Bvsqg%2F%2ByI8moJlGynuTd%2F%2F6NP7Tp8howp%2Fzb0gY6pgHB7%2FnQxZZ7yU3%2FFni4scsnnpjzIqYUjdlGGZWaqhd90leD3kBCiHkAdJSBX3qyBReaBgFJa1gibLRFNZn2XvD3bKWx1KBcomAKOYW0Xtx%2F%2FlPk85I89CD3drQQYWmYkzLY4z%2FoNYmRmP0poQYkhj%2BtJObUZ8tn8dGw4%2BA5%2FJpMIWdXDq0QafzcDXOsTIWj5v%2BtwqgKYeVEsO5TWjfrkZ2XhvgRVEkO&X-Amz-Signature=f75896673213b5c866946f50adc469e440093ebed1c4a13ea60ddf5b69cf8a93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF3WJTXB%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T044143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIHeLm%2BO7qfq4wkJSvUdDYmrh8%2Bt5%2FxDzlWCRrT4JEJ%2BSAiABAYlRu6TwWVrgRHQK4Kfjif24h%2F%2FWQfedm65gp9cJ%2FCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMZKKZJoPK4vglwyLeKtwDUJUQNhrmG4mMF6i2huURRS6R234DhRfHbD7gwCrWZIHdiAt1AmfgEoXY2p4XLBeZoXEGnqI9WRFPJ3OxyBLPBn35h3FcWg587Q4axGZmawTcTGlLPTvUv1OzNVBpmvTkHJPIRsJuUBuOmIPCDiVCqSSQ0F2B8XTIQLzKEpaoonlTeHsswC7VnoIx07jq4BWqF%2F7v4Of3n9izLgzM6eqS7dSeHtpzGT%2FLiVX5OpF%2BT5EoyYQLrXpBjiTB%2FJ%2BISCCOVPfSfvgIaMZQ0QELmeMcQZ8H1L%2BAYA%2BrvJjBg%2BH%2BVdXaAYAjgGc7w5h9CjIM%2FRhSkRO8zU566h6b1KbfhtHZI7FIZbr7d75Y5jiOGAFOQsR%2FB3kYsa4oh3UD0GxOOmqoNTNf71EVm7G5rjYzCp7kegtx4v7gElqwMAagWc9SO7tzaOdGmfhXsQsre9x0MXbPfHjZHxQTM6jBU1cUnVfu5%2BidO3fhv4TWRpUlmw32VU3sEg4OAMTTT9NFvbN5Ju6L0kc8osb%2Fb8nxKdoZcEqkspCZ4dIpaGw5zmJXWHGb9KoxQyrbcW%2BRnIIkMpNEiFK3hZtb435uLU1GGdxtYVG0TJodwG7V%2Bvsqg%2F%2ByI8moJlGynuTd%2F%2F6NP7Tp8howp%2Fzb0gY6pgHB7%2FnQxZZ7yU3%2FFni4scsnnpjzIqYUjdlGGZWaqhd90leD3kBCiHkAdJSBX3qyBReaBgFJa1gibLRFNZn2XvD3bKWx1KBcomAKOYW0Xtx%2F%2FlPk85I89CD3drQQYWmYkzLY4z%2FoNYmRmP0poQYkhj%2BtJObUZ8tn8dGw4%2BA5%2FJpMIWdXDq0QafzcDXOsTIWj5v%2BtwqgKYeVEsO5TWjfrkZ2XhvgRVEkO&X-Amz-Signature=23f99f835280245255e42b355b8a400fe4d9d3fc4663afa8cc25e8d27740450a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
