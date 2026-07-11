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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBKHHLFH%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T012321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfguqdEa5SlPNbdYa%2Fd6EhVAq3Nu7SAbTRNwPLlJ5%2FlAIgSyPFs1k0VebXUqg4Vj4gln5P5cohu7wmldxxb8kPeqUqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjPFM0OY%2B5PqIG3%2ByrcA2vQaRf8j80%2BUmz1YvIfvf51WuJ%2Brr5noUnIp1KqBfoUCyicYFeziOdzK057Ku0lkiT4M3p2ZIEhQkM0CRJKtM%2FvBN%2FEHRH9iUnFDcz%2B02PTUkFwXnxSyuaQSiP3KB3PAcCvKFEPJCYHc7yI3f%2BWfhvbx33d7ZGuZPsbdLvwwfBKKLLuvQ9rxjm5kzN03x5e9lT8KL6NH2tdnrbEIJt8a4on4ILtdQZGJIHRnG9bmD8Ek0%2Be3ZU2us0JMlLeaHcZwj8cCUxgVtQ995f5TddqRAojTvReeDgNe2Nb4q9rKLnVez5eBMa2XPMntw9kHT%2B7MLzIsU1T%2BEIkvQcXlU%2B2T%2FR6CmPhpeghptWexCWduju%2BexaPm5LLdWB%2BJs9L%2FMMrXpz3ZTRGvxBVID6se44FVOr8XPnHsmakswGHhklLn9%2F0fe6vB8BR2KRkwqkpw%2F0whrxxJpEJa4IvX1wiqUdKdqnIEsgVyr5R7VxvfQ4ErAp9TRNEBH4V%2FeZLnri3jiwVpuHqP3Ep7KN6FS49QtH8J7Ia4o9tCpa9ryExU61SYTQUkTAFswrYWTcYfWhcfkk9t7MB2v4UeAzLDNzTQ2MBsPs%2Bedkicjizl6HvvSA7%2BP0Q8nd%2FiYOJSAjRSzITMN3TxdIGOqUBKTgIh0OIQa0zx5ZHxpWpSos2urS4GgPR5DFiIHxjbnhCw1yqDDcmBN0wpmcbe1T%2FlroTrWLaaxxFr0o6tfBOIpN8s3rn5cUkkWJV2%2FGmBuDbmLtuvOvN%2BrEJKEHy3cJfUlII7jkxeASqnkGy70vh%2FwPNCy2v1jQva4LTBTcmi84%2FDDk1JUa8qKjhXysg5KJXE6jacgVlqezMeAIamO57LZYMK9Ex&X-Amz-Signature=84a29bc1ed4c238e812ca760762cf025c75cdf6ed73776b2957fc8b2fb00bc5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBKHHLFH%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T012321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfguqdEa5SlPNbdYa%2Fd6EhVAq3Nu7SAbTRNwPLlJ5%2FlAIgSyPFs1k0VebXUqg4Vj4gln5P5cohu7wmldxxb8kPeqUqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjPFM0OY%2B5PqIG3%2ByrcA2vQaRf8j80%2BUmz1YvIfvf51WuJ%2Brr5noUnIp1KqBfoUCyicYFeziOdzK057Ku0lkiT4M3p2ZIEhQkM0CRJKtM%2FvBN%2FEHRH9iUnFDcz%2B02PTUkFwXnxSyuaQSiP3KB3PAcCvKFEPJCYHc7yI3f%2BWfhvbx33d7ZGuZPsbdLvwwfBKKLLuvQ9rxjm5kzN03x5e9lT8KL6NH2tdnrbEIJt8a4on4ILtdQZGJIHRnG9bmD8Ek0%2Be3ZU2us0JMlLeaHcZwj8cCUxgVtQ995f5TddqRAojTvReeDgNe2Nb4q9rKLnVez5eBMa2XPMntw9kHT%2B7MLzIsU1T%2BEIkvQcXlU%2B2T%2FR6CmPhpeghptWexCWduju%2BexaPm5LLdWB%2BJs9L%2FMMrXpz3ZTRGvxBVID6se44FVOr8XPnHsmakswGHhklLn9%2F0fe6vB8BR2KRkwqkpw%2F0whrxxJpEJa4IvX1wiqUdKdqnIEsgVyr5R7VxvfQ4ErAp9TRNEBH4V%2FeZLnri3jiwVpuHqP3Ep7KN6FS49QtH8J7Ia4o9tCpa9ryExU61SYTQUkTAFswrYWTcYfWhcfkk9t7MB2v4UeAzLDNzTQ2MBsPs%2Bedkicjizl6HvvSA7%2BP0Q8nd%2FiYOJSAjRSzITMN3TxdIGOqUBKTgIh0OIQa0zx5ZHxpWpSos2urS4GgPR5DFiIHxjbnhCw1yqDDcmBN0wpmcbe1T%2FlroTrWLaaxxFr0o6tfBOIpN8s3rn5cUkkWJV2%2FGmBuDbmLtuvOvN%2BrEJKEHy3cJfUlII7jkxeASqnkGy70vh%2FwPNCy2v1jQva4LTBTcmi84%2FDDk1JUa8qKjhXysg5KJXE6jacgVlqezMeAIamO57LZYMK9Ex&X-Amz-Signature=7b1818b6c26b686ee64c40f94a66cc0b2d0ab231392599dfbaa1cea7d5d68946&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
