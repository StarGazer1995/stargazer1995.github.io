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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZSFDN3W%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T094458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDAywNVXiy4t33SNli0fbEAKJsutE1lFjekbZKscrFKXQIhAMyRkSp2Xan8zawcs7HcuYgZhYu1SASo4G9ibnrj7HAcKv8DCBAQABoMNjM3NDIzMTgzODA1IgzEfN69JOcYPN1qZMgq3ANbOLLWZA5ODcnr4xqnV66I8nuJR72N5qVVkrVshxAiMSaNkDPPKFgsmf4ZKacdRWE8hmDcJpIZnQLyG5UHeM5%2BKb9%2FhZ2U%2B3OFYLFxdkYXmfgIm7u9U%2BY1BIrL6XdwpTrYMoaKncfGIr4qjLAkNnIDsuT%2FStDHnVhLbTPUjE6jvq1nzvKNRo3JQ3LGVLgmymBK938YOdC4LgzmiE2Hi9j3QCyapbdjI0frZQKHaigX1Fxf09KrlUAhox4IiUZU%2FNX4NR7YEFZ7klSHUZ46BQSsgadlR9sRdZu2u3TrYdKBgUBsOScqcxJmIevBX8PWiFIqVPV6nnl1Qe1%2BZFFCpxeq1FsEgENUhLIa%2F4PQ48B7CRiR%2BEDoE9uv76BEX7Nn817fk6WGcxPR0YnQ2%2FHbzJwEgD%2Fcd%2FJglwt46tgT1lRvDoZ2nwglS54CsdK0uuQ9qToyslGyxgWsWcml0797sE9JLOPD1lSs%2BksE2d9RjiSb%2FVseyP6dnCH76iDzYgIOJJ3l7hjd3fQ%2FFLtJroAIMpZpQC5p7sVoOPg4hXx3KTlz%2FQDKGf1GxPLOcGWbhfLgQ7ZEL132LwaQS3AhWt%2Fc4BtileXiBdsWMMgqB1nkaLEOaxuFUk5wma9ffObtlTDSydfSBjqkAflwsooSL%2B8Gm7q%2Fq86pnrtX9CilVQKWPXqGEZQkOe7ISl5tfXe5J3ODU%2FZoRMm30CnO9%2BPcGhg9a%2FTwgRLs5T%2Bt5XXmXB2J%2FJFefTF56M2KvWhXaSTBfTGYo4e2YljaYZaG%2BrCNFx2zRkB5%2B3GUoMPRvZmrksnCCpkQj853UmqF2NimBxnwgqqrWuGMz3onqPknoXR9z%2FrRS8CFIQc%2FzH4SJveY&X-Amz-Signature=d6ab04afa836ada890893839bb0636da8f9da6fb2d884c5d5fcd840183982f38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZSFDN3W%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T094458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDAywNVXiy4t33SNli0fbEAKJsutE1lFjekbZKscrFKXQIhAMyRkSp2Xan8zawcs7HcuYgZhYu1SASo4G9ibnrj7HAcKv8DCBAQABoMNjM3NDIzMTgzODA1IgzEfN69JOcYPN1qZMgq3ANbOLLWZA5ODcnr4xqnV66I8nuJR72N5qVVkrVshxAiMSaNkDPPKFgsmf4ZKacdRWE8hmDcJpIZnQLyG5UHeM5%2BKb9%2FhZ2U%2B3OFYLFxdkYXmfgIm7u9U%2BY1BIrL6XdwpTrYMoaKncfGIr4qjLAkNnIDsuT%2FStDHnVhLbTPUjE6jvq1nzvKNRo3JQ3LGVLgmymBK938YOdC4LgzmiE2Hi9j3QCyapbdjI0frZQKHaigX1Fxf09KrlUAhox4IiUZU%2FNX4NR7YEFZ7klSHUZ46BQSsgadlR9sRdZu2u3TrYdKBgUBsOScqcxJmIevBX8PWiFIqVPV6nnl1Qe1%2BZFFCpxeq1FsEgENUhLIa%2F4PQ48B7CRiR%2BEDoE9uv76BEX7Nn817fk6WGcxPR0YnQ2%2FHbzJwEgD%2Fcd%2FJglwt46tgT1lRvDoZ2nwglS54CsdK0uuQ9qToyslGyxgWsWcml0797sE9JLOPD1lSs%2BksE2d9RjiSb%2FVseyP6dnCH76iDzYgIOJJ3l7hjd3fQ%2FFLtJroAIMpZpQC5p7sVoOPg4hXx3KTlz%2FQDKGf1GxPLOcGWbhfLgQ7ZEL132LwaQS3AhWt%2Fc4BtileXiBdsWMMgqB1nkaLEOaxuFUk5wma9ffObtlTDSydfSBjqkAflwsooSL%2B8Gm7q%2Fq86pnrtX9CilVQKWPXqGEZQkOe7ISl5tfXe5J3ODU%2FZoRMm30CnO9%2BPcGhg9a%2FTwgRLs5T%2Bt5XXmXB2J%2FJFefTF56M2KvWhXaSTBfTGYo4e2YljaYZaG%2BrCNFx2zRkB5%2B3GUoMPRvZmrksnCCpkQj853UmqF2NimBxnwgqqrWuGMz3onqPknoXR9z%2FrRS8CFIQc%2FzH4SJveY&X-Amz-Signature=6b6d68a20db7fcb55c2b69cd68c439f5a409423d578efc02d44fc27bec1f9dc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
