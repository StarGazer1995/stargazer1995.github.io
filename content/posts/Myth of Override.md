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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NXSUJBT%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T145022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIHDDniSZuMdu6vpl%2F44Ui%2BegDUAxsdP97frjmahFVAWJAiAprjC1lwfpkzoifwMA2oojRKSHxgzbWLYPwaRFj7VgRCqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgvYC%2FYsl7uKGjxs7KtwDqOX9hkgvFK59Up8nP3rCJ7WC%2B%2B2VIPYNdbsbtWv7WLsSVnDQC7wcYTkJszWK4zYGxksl3R1DGwSfOSK6QUJXEPIKSicjOXwwMvHnZ%2F0prya8RgmAOXnGmnM7OojaUhI%2BzGa45SgzjezaAXs5LtsnOGk4pmz%2Fai0wqPcAehgt2ThsMvkyAHXEiR%2BiGIC5qlFZGYSCVm9zM5RcKAAxz89Y8VXvIt%2Fq%2B8xszvuS%2BLWf9Mi0XwjZzJOiTSPUB%2FcSykTFV5buVDOFmzrvZCmzRHzOsgQN6yjfCRezG0kRIN7N0FGGD0NpHQ5zKlg7KSmcuctaO4Eg7qVNglrlIsBIGkLO%2Boo8lu2XSTngmEBbCPqovh08qu79VCH9ijsVFO%2FQXvS0c2uVGbPaR%2FQF3fV7W0AsuWO2y3X9X5%2FEiOHDYJExcR5qDW87zQPl2OYDqN6a%2Bj5HfupkbaJB1cWGyajhbP3%2BZrqcMrVYLrkEavfbtsaCGx84vyLRzkaz25Bj0Rq9RYmZCW0Bz8p9g%2BtDQFtd7FBfkj3o0cSUVsP%2BqEQ0PMjzxZZKJJ0%2B2ivbOJ62W5WQKJS5i8F9iW8s20oA2v%2FgYofy%2BjA2omvm23ioj8mqxYXh16M2c%2BHi2ytAOR8U2nsw1%2Brx0wY6pgGM%2FhuYls3pwtkGCD4DqYvsXzf67v6rYEmXsMVgphAZYthf6EskKwDOLCPwwcI5fYQ2q2P%2BkFXf6ywsOJ0iMiUUUbZ01XeAjmJX0PKf7X6V7q9ZrDbTyzxjS7kMF5wq1K2job0fsLt%2B6h0wzR6v3UnbIGn%2BKwS5kdAj65dDkRJ5SMo02Wvik1AfzN%2BdLyQwXVyEGY77S8wb5NRPgiBbIuD3dyZlIFBb&X-Amz-Signature=b15ff7b46207514a75e40be2f8e42342dc7f840d682aed0fb594a198f8e5c8e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NXSUJBT%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T145022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIHDDniSZuMdu6vpl%2F44Ui%2BegDUAxsdP97frjmahFVAWJAiAprjC1lwfpkzoifwMA2oojRKSHxgzbWLYPwaRFj7VgRCqIBAjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgvYC%2FYsl7uKGjxs7KtwDqOX9hkgvFK59Up8nP3rCJ7WC%2B%2B2VIPYNdbsbtWv7WLsSVnDQC7wcYTkJszWK4zYGxksl3R1DGwSfOSK6QUJXEPIKSicjOXwwMvHnZ%2F0prya8RgmAOXnGmnM7OojaUhI%2BzGa45SgzjezaAXs5LtsnOGk4pmz%2Fai0wqPcAehgt2ThsMvkyAHXEiR%2BiGIC5qlFZGYSCVm9zM5RcKAAxz89Y8VXvIt%2Fq%2B8xszvuS%2BLWf9Mi0XwjZzJOiTSPUB%2FcSykTFV5buVDOFmzrvZCmzRHzOsgQN6yjfCRezG0kRIN7N0FGGD0NpHQ5zKlg7KSmcuctaO4Eg7qVNglrlIsBIGkLO%2Boo8lu2XSTngmEBbCPqovh08qu79VCH9ijsVFO%2FQXvS0c2uVGbPaR%2FQF3fV7W0AsuWO2y3X9X5%2FEiOHDYJExcR5qDW87zQPl2OYDqN6a%2Bj5HfupkbaJB1cWGyajhbP3%2BZrqcMrVYLrkEavfbtsaCGx84vyLRzkaz25Bj0Rq9RYmZCW0Bz8p9g%2BtDQFtd7FBfkj3o0cSUVsP%2BqEQ0PMjzxZZKJJ0%2B2ivbOJ62W5WQKJS5i8F9iW8s20oA2v%2FgYofy%2BjA2omvm23ioj8mqxYXh16M2c%2BHi2ytAOR8U2nsw1%2Brx0wY6pgGM%2FhuYls3pwtkGCD4DqYvsXzf67v6rYEmXsMVgphAZYthf6EskKwDOLCPwwcI5fYQ2q2P%2BkFXf6ywsOJ0iMiUUUbZ01XeAjmJX0PKf7X6V7q9ZrDbTyzxjS7kMF5wq1K2job0fsLt%2B6h0wzR6v3UnbIGn%2BKwS5kdAj65dDkRJ5SMo02Wvik1AfzN%2BdLyQwXVyEGY77S8wb5NRPgiBbIuD3dyZlIFBb&X-Amz-Signature=d2313376023c966a1aab3079bbd3f77206ef03874efc5b21a0fb29c77951769a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
