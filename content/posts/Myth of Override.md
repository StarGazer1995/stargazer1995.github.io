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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625UWDC23%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T061308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJIMEYCIQC9Ag%2BzTIFjaqIoCe%2FFi3TADj8EePWR2VYs9SpWk1K1BQIhAMKWGnlfbmgizgwpEw3iRbiEYKomGLKSDEeCsWOkrj3RKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweeQph5F4IW2Zv7dYq3ANFxBOOS2J%2Fu2djsi7GI%2BpKIEO9c9Uoaj5h0sBkXdTlLkZApKhLcNEwDPSVj3xOqOUpy%2FQnBu1ZEVXyAUSPmM4ZlXGNSb5QN9qZL4rBwyXbKfb%2F0NQFlh0fAENBMc%2BDM8BOQdAkw1c2Zm%2FrTx8xLdRO6Omd3cM2GcR72cXRKsHuh71BcEo98zQkQaS1iYcKPo5nFYM2WzKKRnV2Gh4dyfRQ%2BdaXS1ifIKmnB42Tbr%2BrDka8LJVLHYh8x3dJJ98ij5mxvjPzgKxJ62CQ3gWwKDBX6sgzfhXexYNgOyzs1xPrnUw%2BZs2MhrdfqLgmfDpdcPo4B02P%2FYvGiJ6stXa75rs653j1TsHp9DyGU7nou3VkO73a1NkeNsUyTrQc6%2FXH0wucSVNwnui%2Frg0CsOW7jVB68s1692MEHkO5bU1PYSi1sQnLiOqMcB%2B%2BlnqwNsCPTOCG9LzBBdMAaOnhFuLB%2F8v7vjX8rbVFAPJPZpbdLiShHRkS1wLP0CZZVd6ISpL1iad9BbACAEe8LQgB%2Fy8F%2B8RIgOhxL6sQlh4lx%2Bh%2FJsV82GyG9w6sG4kpvB42bI4CtiWYOWUBWw1Yun2DP9P4j5o5hiu8Nm7NaRgeJsj5NwgJDA%2FEL%2BBUzgRuA7bfszDfs7rQBjqkAcrA1%2BP2DqMdnW1gjrFV2V64Aadg%2Bh%2FfHpX9efuw4yRUglcHzoONS6%2BOFFweotUFbjmBHzp36xPhGp8mz1l7VYB1HFExZbnJxW2Nx291hyot4eOt4%2B7GSSLhBrHMl4WZWl2vDFG8udwOUQhMFAQi%2F%2BISIFOSk1g9v7kk5nLTzN6pYSJr%2BXYNb5mxawzqsNwLeyPfOzybcYAS7tR78V1%2Fz%2BZ5EWZb&X-Amz-Signature=251d2f4393a784937106d5e66ea7884d10c8d812d8b66d64f00a99bae7d01070&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625UWDC23%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T061308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJIMEYCIQC9Ag%2BzTIFjaqIoCe%2FFi3TADj8EePWR2VYs9SpWk1K1BQIhAMKWGnlfbmgizgwpEw3iRbiEYKomGLKSDEeCsWOkrj3RKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweeQph5F4IW2Zv7dYq3ANFxBOOS2J%2Fu2djsi7GI%2BpKIEO9c9Uoaj5h0sBkXdTlLkZApKhLcNEwDPSVj3xOqOUpy%2FQnBu1ZEVXyAUSPmM4ZlXGNSb5QN9qZL4rBwyXbKfb%2F0NQFlh0fAENBMc%2BDM8BOQdAkw1c2Zm%2FrTx8xLdRO6Omd3cM2GcR72cXRKsHuh71BcEo98zQkQaS1iYcKPo5nFYM2WzKKRnV2Gh4dyfRQ%2BdaXS1ifIKmnB42Tbr%2BrDka8LJVLHYh8x3dJJ98ij5mxvjPzgKxJ62CQ3gWwKDBX6sgzfhXexYNgOyzs1xPrnUw%2BZs2MhrdfqLgmfDpdcPo4B02P%2FYvGiJ6stXa75rs653j1TsHp9DyGU7nou3VkO73a1NkeNsUyTrQc6%2FXH0wucSVNwnui%2Frg0CsOW7jVB68s1692MEHkO5bU1PYSi1sQnLiOqMcB%2B%2BlnqwNsCPTOCG9LzBBdMAaOnhFuLB%2F8v7vjX8rbVFAPJPZpbdLiShHRkS1wLP0CZZVd6ISpL1iad9BbACAEe8LQgB%2Fy8F%2B8RIgOhxL6sQlh4lx%2Bh%2FJsV82GyG9w6sG4kpvB42bI4CtiWYOWUBWw1Yun2DP9P4j5o5hiu8Nm7NaRgeJsj5NwgJDA%2FEL%2BBUzgRuA7bfszDfs7rQBjqkAcrA1%2BP2DqMdnW1gjrFV2V64Aadg%2Bh%2FfHpX9efuw4yRUglcHzoONS6%2BOFFweotUFbjmBHzp36xPhGp8mz1l7VYB1HFExZbnJxW2Nx291hyot4eOt4%2B7GSSLhBrHMl4WZWl2vDFG8udwOUQhMFAQi%2F%2BISIFOSk1g9v7kk5nLTzN6pYSJr%2BXYNb5mxawzqsNwLeyPfOzybcYAS7tR78V1%2Fz%2BZ5EWZb&X-Amz-Signature=74357de23ea71cc2376cc2793d77819e13be1a33e9af94cdd94cedf7cba9b06b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
