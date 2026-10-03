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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYC2U2GM%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T174125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAGIUkRTLRr%2BgZIJe%2BHl%2BUSHvHB31YN0ZAwp3vkKrHVSAiEAqz7NMGjWv2iTvb3UJM5pS4BCtex6zK%2B5zRgXPAF9d4IqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnhNS5MC9qfuK7M8yrcA8UMuuN6viqUv5pTwXfX%2BK6Ay7e%2BroPR1gN3Z%2FvOrUoiNIa8Gvhv%2Fco6maR4VTPNPNNwiQqpuQBXqNKV53bNkMFKvp1n12PRXXXifF0QgGSLsWuJzKrGcrVIM9TtYKHIIRdk0RAdySrR2b24GV3qJZq%2BbxDb2fyYZkJ4XZnjObukEHeVRY43lj4fEugKsb3%2FX%2FCIWUpM9%2FYvgMaezTP8fmdhXfEywI1vvX1AJSjC5xKxI%2FfAPPezxIvdSPDiexnVh16oaTbc9k7LfuS1pi%2Bwkt64%2FOZdtBNs0JeAHGr3T7dcSoSIWe2ExcoOKPPwD2vL285oZBiCtKJPp6SPb4xKWR%2FBcGZR8nR9%2FKipJ65LlY73yubXIdufIxiQ6s5UbL%2BH3o9%2BS2VLiq5R6qxyP8qgCe1hUDBPXoxkjX5ipnwtudr9OA4cK6U3nNVhPrLcfqwZHtS5G%2FbmRv8aTg1Md3kX2reucUXz7IfwPyuNuFTgFwVox9pPDOXhu7x0TC%2Bvgx1QnGdlqIl4rBdVvZVzNk3h%2BfoejKevjq8IkSjZWND4ZN8rqbYbyDlzjXsdovE%2BbUiX66TNJJw3YUCXcHLZLkA%2FOB6BlEPeuEekmzlk3QMn9%2BadNVtq32C66C93PiCYMOLzhNYGOqUBT%2FDuDyB2D5YJ5X5NPkVPVL%2BzRrlm3NabXeEcDj6VanVxQY7RMrQ5BSa%2F6E72DzGjS2chp5YWGIL6jj5%2FSwFYkrQy6EqRLQJVsLaLZN7wEwZCCH%2FEfsgMXaaFhdrOgM%2FQciKndBC0a3mzl35BCUn%2BpjGIopQtF5gSgSje0qGKUUTRwnXr7VONF%2B2iCx0WiOcz4GJ%2FDJjJjBmsmYG%2BjTJ9z65YSsqo&X-Amz-Signature=e6c5ba258655103b8dcf46d3eeb71c1ed2cb9e2080cfcb78579a73f3f0731a9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYC2U2GM%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T174125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAGIUkRTLRr%2BgZIJe%2BHl%2BUSHvHB31YN0ZAwp3vkKrHVSAiEAqz7NMGjWv2iTvb3UJM5pS4BCtex6zK%2B5zRgXPAF9d4IqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnhNS5MC9qfuK7M8yrcA8UMuuN6viqUv5pTwXfX%2BK6Ay7e%2BroPR1gN3Z%2FvOrUoiNIa8Gvhv%2Fco6maR4VTPNPNNwiQqpuQBXqNKV53bNkMFKvp1n12PRXXXifF0QgGSLsWuJzKrGcrVIM9TtYKHIIRdk0RAdySrR2b24GV3qJZq%2BbxDb2fyYZkJ4XZnjObukEHeVRY43lj4fEugKsb3%2FX%2FCIWUpM9%2FYvgMaezTP8fmdhXfEywI1vvX1AJSjC5xKxI%2FfAPPezxIvdSPDiexnVh16oaTbc9k7LfuS1pi%2Bwkt64%2FOZdtBNs0JeAHGr3T7dcSoSIWe2ExcoOKPPwD2vL285oZBiCtKJPp6SPb4xKWR%2FBcGZR8nR9%2FKipJ65LlY73yubXIdufIxiQ6s5UbL%2BH3o9%2BS2VLiq5R6qxyP8qgCe1hUDBPXoxkjX5ipnwtudr9OA4cK6U3nNVhPrLcfqwZHtS5G%2FbmRv8aTg1Md3kX2reucUXz7IfwPyuNuFTgFwVox9pPDOXhu7x0TC%2Bvgx1QnGdlqIl4rBdVvZVzNk3h%2BfoejKevjq8IkSjZWND4ZN8rqbYbyDlzjXsdovE%2BbUiX66TNJJw3YUCXcHLZLkA%2FOB6BlEPeuEekmzlk3QMn9%2BadNVtq32C66C93PiCYMOLzhNYGOqUBT%2FDuDyB2D5YJ5X5NPkVPVL%2BzRrlm3NabXeEcDj6VanVxQY7RMrQ5BSa%2F6E72DzGjS2chp5YWGIL6jj5%2FSwFYkrQy6EqRLQJVsLaLZN7wEwZCCH%2FEfsgMXaaFhdrOgM%2FQciKndBC0a3mzl35BCUn%2BpjGIopQtF5gSgSje0qGKUUTRwnXr7VONF%2B2iCx0WiOcz4GJ%2FDJjJjBmsmYG%2BjTJ9z65YSsqo&X-Amz-Signature=ffa004112facb95897c0808e914eec17ec8d5678384918849fac0204eeb2dabf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
