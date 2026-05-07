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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ALZ3UJZ%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T052219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvbV388cQciDm7Pz0EbI7%2BKr3k7bepo%2F5IZT7b%2BH%2BCiAiEAlNQq16ol6NFStkeu6xQWn6wD%2B4P6%2FU%2F%2FE1IJvjs6hXwqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIH%2BDbgvXz%2F6oIn%2FLCrcA2cLmjpgkaQD2MVVUG6nnYanUp%2Bb2ftZiHIG%2Fq%2FZcy3QNukJlx2ePRGduUNNVVmE61thz52dkaf6IaU%2B9XQbLXnUBJAhoKvcIbwondwdK6tekc5whp1xT31V1LgwJKgRaFIhBZcBApEpfvw7dT4F46LRAGskiawo4PUPEpuILQsfR9Nde8kpHN4WJ0LRmhVSb3kSZzS%2FEbRu6T2v8lDcJJBBA7VXU7618GhNVS4y%2F9vm8zQ8WilV%2Bg9s8GppBbiw4Mq%2Frd5TX%2BNC2pivjeErfHi56RXoD40iYwt3x7S%2BctfuqCzuCRGmTNdc4cs%2BOMJd%2FJY9mogUQYCrhPWQGYSYwYQLbFhTNclfgBFJMXJM%2FM4XpMf7dPI6F3yNMjYk9CUypo0t9ltVbXGV1zCWfnDwwUzJSIYNZSikxuUym5MuTJCwv10zCGnUkTv2cOolok2STwYDcy7VsNvIkUWYmixiKJdJRwKegpq4r5DNTYkL%2FfMLt5ZxB8okzvRmLcNE6HboSb9oq2PJCC3rHN9zLH9zUv2nbmG%2FpknF%2BDjGNsfwb06PUxiklw00LSneoR%2F6DpRNoRJeaCXBiqqwTan8hAfOduLkflXAghPaMHYkUlH4pfSDNHB%2Be%2F6mEQ2YQYLKMOCx8M8GOqUBJk8mourmFZHehMUnhUld2VD%2FYqTFMx1FGcMuXiniSMt2LMXpAIOI3rXm6p0VP%2FtM4aJ8FIpDfy5AMFbuEk3d3cjt1Patehq5JEO2rPfdLDq4EsHQkSKefGu6HY%2B8LOpcQ%2Bw5elIPi1kImOlAZKcjybj7D%2F%2Bwdq%2FEgV6a1hCKdsZ9IDQex0n86xDToOlHlFSGd8KuS%2BS734s08fD03nfzNV1Jo42m&X-Amz-Signature=d044a28900184c1b1f064d64291dcdf23c5b45d58361b51a470f29d1fdc5a3d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ALZ3UJZ%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T052219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvbV388cQciDm7Pz0EbI7%2BKr3k7bepo%2F5IZT7b%2BH%2BCiAiEAlNQq16ol6NFStkeu6xQWn6wD%2B4P6%2FU%2F%2FE1IJvjs6hXwqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIH%2BDbgvXz%2F6oIn%2FLCrcA2cLmjpgkaQD2MVVUG6nnYanUp%2Bb2ftZiHIG%2Fq%2FZcy3QNukJlx2ePRGduUNNVVmE61thz52dkaf6IaU%2B9XQbLXnUBJAhoKvcIbwondwdK6tekc5whp1xT31V1LgwJKgRaFIhBZcBApEpfvw7dT4F46LRAGskiawo4PUPEpuILQsfR9Nde8kpHN4WJ0LRmhVSb3kSZzS%2FEbRu6T2v8lDcJJBBA7VXU7618GhNVS4y%2F9vm8zQ8WilV%2Bg9s8GppBbiw4Mq%2Frd5TX%2BNC2pivjeErfHi56RXoD40iYwt3x7S%2BctfuqCzuCRGmTNdc4cs%2BOMJd%2FJY9mogUQYCrhPWQGYSYwYQLbFhTNclfgBFJMXJM%2FM4XpMf7dPI6F3yNMjYk9CUypo0t9ltVbXGV1zCWfnDwwUzJSIYNZSikxuUym5MuTJCwv10zCGnUkTv2cOolok2STwYDcy7VsNvIkUWYmixiKJdJRwKegpq4r5DNTYkL%2FfMLt5ZxB8okzvRmLcNE6HboSb9oq2PJCC3rHN9zLH9zUv2nbmG%2FpknF%2BDjGNsfwb06PUxiklw00LSneoR%2F6DpRNoRJeaCXBiqqwTan8hAfOduLkflXAghPaMHYkUlH4pfSDNHB%2Be%2F6mEQ2YQYLKMOCx8M8GOqUBJk8mourmFZHehMUnhUld2VD%2FYqTFMx1FGcMuXiniSMt2LMXpAIOI3rXm6p0VP%2FtM4aJ8FIpDfy5AMFbuEk3d3cjt1Patehq5JEO2rPfdLDq4EsHQkSKefGu6HY%2B8LOpcQ%2Bw5elIPi1kImOlAZKcjybj7D%2F%2Bwdq%2FEgV6a1hCKdsZ9IDQex0n86xDToOlHlFSGd8KuS%2BS734s08fD03nfzNV1Jo42m&X-Amz-Signature=40bfc15e6cde3fb08964b4f7c67d418b53770271f346516c0808ee5055ad304a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
