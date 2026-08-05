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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMVINJNS%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T012158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJIMEYCIQDAOYPp0qgJFoXjoS%2Bxl18wRz6IKLiUFrGY9hCW9F61CQIhAOkwuqlViCanoOS7be2%2BAk%2FAeeI4V0VJzYEjYgzF0ctuKv8DCBoQABoMNjM3NDIzMTgzODA1Igxe4qPM6LcBHpFxIEwq3AOwFK3YFPyGxvVq08HaPkX4wTPOFzW8IS56ZGE7bUqT%2BWPkwvBQAE%2BF3sATBldGv3xe3l4U5Bo%2FlDbzgmFOOENyhCa8DIoJADshbmr%2BsZDTqWqpWh2mpEJyJFNRxRenr%2FGRk4rvGVHufComBAcw5cFZDwDTNnH6J9etUdLEg9fmNKAqXTdv%2FytJP0RPK0YmeOAQ6s3Iqcmu7NQjlKHoj8dPhzLMwRn20ep28YMSuQqnpPdP59HCtLZ9EKVTjFjprCukyCDmaYrJ4TpuBO8qCgIB%2FvLA3tkZbRcP%2BFpX%2FhaIKrinzh7n3nPOyrkwp7wN6i%2BYCbVswxiOi3AdckFTmesKLy34w1IPzQ5Y7WcECjBfcguCISVo27RsrCTz4VH1tze%2BLLe5GjUfyZfIUnWDirB2Pe1XYsfNtzkUeP9rjtkLCD3GJuKeVM8SSbyD8nItT75Rz72YB%2FVLG3Uwt%2B14bwV3ZZohQ8tbpfMI%2FX0ADCYZort3ed0dqMNfmRFNctYBqMPai6rZN8M3zxlW%2Fj6VKNVDX8P2UG0BWlo1zSiLkh43NI%2BDcCz6VIksfRItUJjBQFtu%2BA6m7UCQBXeoiCSB%2FO0bGo5DLbWPH2WLnCnzZIAjCdh5VlPgBwMgf0hLezCalMrTBjqkAQjL4wd9lSbirvHFunCcc9PqSub28EzrEwgC9YA1GT7ZRZcdrROgYtcaNz%2FLdxgeWt1VcO1VIL0InvGZEZLa%2BTO9ONS5xFflE82PzIcYsve3K0UK5jaKlIZNrfmGE9KmbJOvGqfda0pC%2FPsZpud3nAqySVj0TsixQWWa7xR6%2FwkMxKd11uIsGVQI42OhD3hVqCPoCP21Lu7DKkNwwIb1nXhVUqlz&X-Amz-Signature=6ac51bf3bf96b7eaa420306201d982e34a4bd8021d0e538d71166a7b9acaaff6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMVINJNS%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T012158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJIMEYCIQDAOYPp0qgJFoXjoS%2Bxl18wRz6IKLiUFrGY9hCW9F61CQIhAOkwuqlViCanoOS7be2%2BAk%2FAeeI4V0VJzYEjYgzF0ctuKv8DCBoQABoMNjM3NDIzMTgzODA1Igxe4qPM6LcBHpFxIEwq3AOwFK3YFPyGxvVq08HaPkX4wTPOFzW8IS56ZGE7bUqT%2BWPkwvBQAE%2BF3sATBldGv3xe3l4U5Bo%2FlDbzgmFOOENyhCa8DIoJADshbmr%2BsZDTqWqpWh2mpEJyJFNRxRenr%2FGRk4rvGVHufComBAcw5cFZDwDTNnH6J9etUdLEg9fmNKAqXTdv%2FytJP0RPK0YmeOAQ6s3Iqcmu7NQjlKHoj8dPhzLMwRn20ep28YMSuQqnpPdP59HCtLZ9EKVTjFjprCukyCDmaYrJ4TpuBO8qCgIB%2FvLA3tkZbRcP%2BFpX%2FhaIKrinzh7n3nPOyrkwp7wN6i%2BYCbVswxiOi3AdckFTmesKLy34w1IPzQ5Y7WcECjBfcguCISVo27RsrCTz4VH1tze%2BLLe5GjUfyZfIUnWDirB2Pe1XYsfNtzkUeP9rjtkLCD3GJuKeVM8SSbyD8nItT75Rz72YB%2FVLG3Uwt%2B14bwV3ZZohQ8tbpfMI%2FX0ADCYZort3ed0dqMNfmRFNctYBqMPai6rZN8M3zxlW%2Fj6VKNVDX8P2UG0BWlo1zSiLkh43NI%2BDcCz6VIksfRItUJjBQFtu%2BA6m7UCQBXeoiCSB%2FO0bGo5DLbWPH2WLnCnzZIAjCdh5VlPgBwMgf0hLezCalMrTBjqkAQjL4wd9lSbirvHFunCcc9PqSub28EzrEwgC9YA1GT7ZRZcdrROgYtcaNz%2FLdxgeWt1VcO1VIL0InvGZEZLa%2BTO9ONS5xFflE82PzIcYsve3K0UK5jaKlIZNrfmGE9KmbJOvGqfda0pC%2FPsZpud3nAqySVj0TsixQWWa7xR6%2FwkMxKd11uIsGVQI42OhD3hVqCPoCP21Lu7DKkNwwIb1nXhVUqlz&X-Amz-Signature=bd6c057f6a22a892c5e2b10879ed4e111e25e50c42efc63b413bbec1ad62cb0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
