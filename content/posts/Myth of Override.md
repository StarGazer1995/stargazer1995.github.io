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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466242RNEZX%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T003321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtuflELTVL4dWl1w9EeTIRDt18%2BKd%2FkO4hJ1Eag2rX5QIhAJ8GUDAEQfOsROCiP0dXIilV8ykDyJCTXIfsR463iC7dKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5XQlBV6RjPJ5DAmIq3AN6nf4i6I3MAvGI63ZABUmkT%2FxV7TzaUv5%2Fh1x7ID%2FKuWoCwtBxFRfYHCFdXDGEHYm0Q1YnAlsnVLyGwBNEYfwXE24luK5CJnkujPMg8O29bYQf8sJ%2B19%2FYis2i75svlpXSfN7YnkSC%2FVlw5xALPF8luABcOAQ2n7JtEM6YEBUqiPlpAaNZ5hLuOUVO%2FqfAF7RgCQPSINxIq7pezPeYTuJ1hmqta3VKApGd8SLjdRvbCBWU9kFfmld5WEbF%2FKd0i%2BxsiJgbX9jLKchIkCNNzgXJVoAbQWJ9IKdtJqNmGXC%2FYuQe5zV2dgFNE7VtuVY4MMbmSKC7fwjt01iRHzmOZXCIkUQFLxoBC4632fZG2sbOCjqAH89ET4U956T0GbVlPIFaWRwoxYUSjZssms4p2MWm7yOxgi%2FrRGEUIcMGgAIoGwfecsgg%2Bqbz%2BtI38caPXDv%2Bv3ULxRPNds%2BKzm0lwRxM6ItiwfDvW6NOUi4tK9vsZnJa2QUR1I%2F%2F6xdiajtRgQjY7BmjAmkC4AXDmWD7JPK0quWUxoJuSUx6UzeFoTFZJ4l33tmZQ0n6kb7e%2F2Tx3qmwq%2F4VHAtIcgSSAFGO0dTZH8TAmxtyqRCt2SllP%2B7kXi%2BmacZfbs3d8LN58zDExKPUBjqkAZI5Q6eJFvwx%2Bp2823ITy8r4lkDKQpmouWfkomyIdG0V2RJUR6T%2FjrlYsiZn0i3RX%2Fh0UjJASkEjCwXsx6MiocrnkFnwk5W0MKRzQ%2BT9md3bs2hMKRrQpjvv%2Bl1rF9B8Tvo7JiHZTj5kFLelYMORbyJUwxO9%2B8V9xwGgwGMObNhaeL6%2Bcb1HaJjp3zy%2FVJ5jeDyQer4nAD%2FxzmaKLWIHfREYXbam&X-Amz-Signature=d180f3da83ab71ba1e4ee72f8fc6d7541047b4bd9cf23c09b7f1ba222a7724c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466242RNEZX%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T003321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtuflELTVL4dWl1w9EeTIRDt18%2BKd%2FkO4hJ1Eag2rX5QIhAJ8GUDAEQfOsROCiP0dXIilV8ykDyJCTXIfsR463iC7dKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5XQlBV6RjPJ5DAmIq3AN6nf4i6I3MAvGI63ZABUmkT%2FxV7TzaUv5%2Fh1x7ID%2FKuWoCwtBxFRfYHCFdXDGEHYm0Q1YnAlsnVLyGwBNEYfwXE24luK5CJnkujPMg8O29bYQf8sJ%2B19%2FYis2i75svlpXSfN7YnkSC%2FVlw5xALPF8luABcOAQ2n7JtEM6YEBUqiPlpAaNZ5hLuOUVO%2FqfAF7RgCQPSINxIq7pezPeYTuJ1hmqta3VKApGd8SLjdRvbCBWU9kFfmld5WEbF%2FKd0i%2BxsiJgbX9jLKchIkCNNzgXJVoAbQWJ9IKdtJqNmGXC%2FYuQe5zV2dgFNE7VtuVY4MMbmSKC7fwjt01iRHzmOZXCIkUQFLxoBC4632fZG2sbOCjqAH89ET4U956T0GbVlPIFaWRwoxYUSjZssms4p2MWm7yOxgi%2FrRGEUIcMGgAIoGwfecsgg%2Bqbz%2BtI38caPXDv%2Bv3ULxRPNds%2BKzm0lwRxM6ItiwfDvW6NOUi4tK9vsZnJa2QUR1I%2F%2F6xdiajtRgQjY7BmjAmkC4AXDmWD7JPK0quWUxoJuSUx6UzeFoTFZJ4l33tmZQ0n6kb7e%2F2Tx3qmwq%2F4VHAtIcgSSAFGO0dTZH8TAmxtyqRCt2SllP%2B7kXi%2BmacZfbs3d8LN58zDExKPUBjqkAZI5Q6eJFvwx%2Bp2823ITy8r4lkDKQpmouWfkomyIdG0V2RJUR6T%2FjrlYsiZn0i3RX%2Fh0UjJASkEjCwXsx6MiocrnkFnwk5W0MKRzQ%2BT9md3bs2hMKRrQpjvv%2Bl1rF9B8Tvo7JiHZTj5kFLelYMORbyJUwxO9%2B8V9xwGgwGMObNhaeL6%2Bcb1HaJjp3zy%2FVJ5jeDyQer4nAD%2FxzmaKLWIHfREYXbam&X-Amz-Signature=99c5f61cb722dc9d37384500fa09f0d9cd22429c94895e9e803ba2c334a0ce43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
