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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMLUOP3X%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T190947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIDBhaTkLRFtYmkywnEu9sowhgfYQ5O%2FGa5JThDn23WblAiAIpMOT6l6M%2FKqa4nJRUHn8TuvLKmdhPtbEHJ7Hey4pCyr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIM5ZPQaePIkCrzoVGHKtwDv4Fr5lXMR%2FVXGXE1Z21%2FOKRSP%2FNoIQoVWBHQNoLCvaaaDLKOXCviEewyrPNXwUkzJGTG9EYZa66HWDKBog8cZ4LwItI%2B4AY1rH7wGNDIiMkSckhD6z%2FXT7zAo77Rk%2F7FE4cmwWa9QFYGGpd9hP%2FQ5owhVR0B3dqVco9H8gidZqvq35jSwM8uFFHT8Aemhavh74Ri9nkfWZrNPihPQ05eSiCfCyfIgXkw9JXiZTZlx52BP3CvGKtfML9aTw9842y4B%2Bj8f5KeciKaFzziAbXHkgEjzYFsADd11U3wABrln6t5GjNfLPiI%2BNIy5FVfIOU4Xn3Hnkf7OcCGAY9EIBut6nRtjQlqPGlMVunHB%2BZVtsZYtbnNRpve4f4s0%2F26svPmN8ayJFwcWzFkb%2Ba1Gn%2FYOb0j7Gr9LB4ulQ%2BYeXjpD1m%2BBhUI3yr93pcSiaeucAi6V6yBv0r39RD%2FBhqKqgRCj%2FGY0gJiUB4bhaXN0Kk1urFh%2B53YyHpXsxIrzJJyTFh8t2DN4%2BSNdMQmeHgJ3zvJ1u3YkG%2FfLr754QGFPAvSWIVdhVCkscxNDt5BUAMlAXlUQMyMfK9%2FuORx6LMc%2FFBwyllc2RzVuwxHl29CwTjpiHNnLS%2BG6fNwakIGmLQwv9uO0wY6pgFSO4sJdo1s%2FQeDHgqZFvA4naPZj2%2FN9qinDEqVmxYkLEf0ddhoq1s%2BmXFc0D7%2F5LN7SjZhuINwhi2nlm0JBtq4quSi8JswfLctxwoGd4HiVONqSOrj2cK0G5oM4%2BMA2l94pIEfXbworkn6xyipfKhjNwlMr8n5Q3hmeIN1%2FblGxRZCYLgh1BnzJVf0Ny6tzpsmuZxn8M%2FsCjkPUwCY7C5ltczRu0zb&X-Amz-Signature=5d705cecddff7890dc31a6023bf49fb3bb1cd4bfd345e56e3791585b003d80e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMLUOP3X%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T190947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIDBhaTkLRFtYmkywnEu9sowhgfYQ5O%2FGa5JThDn23WblAiAIpMOT6l6M%2FKqa4nJRUHn8TuvLKmdhPtbEHJ7Hey4pCyr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIM5ZPQaePIkCrzoVGHKtwDv4Fr5lXMR%2FVXGXE1Z21%2FOKRSP%2FNoIQoVWBHQNoLCvaaaDLKOXCviEewyrPNXwUkzJGTG9EYZa66HWDKBog8cZ4LwItI%2B4AY1rH7wGNDIiMkSckhD6z%2FXT7zAo77Rk%2F7FE4cmwWa9QFYGGpd9hP%2FQ5owhVR0B3dqVco9H8gidZqvq35jSwM8uFFHT8Aemhavh74Ri9nkfWZrNPihPQ05eSiCfCyfIgXkw9JXiZTZlx52BP3CvGKtfML9aTw9842y4B%2Bj8f5KeciKaFzziAbXHkgEjzYFsADd11U3wABrln6t5GjNfLPiI%2BNIy5FVfIOU4Xn3Hnkf7OcCGAY9EIBut6nRtjQlqPGlMVunHB%2BZVtsZYtbnNRpve4f4s0%2F26svPmN8ayJFwcWzFkb%2Ba1Gn%2FYOb0j7Gr9LB4ulQ%2BYeXjpD1m%2BBhUI3yr93pcSiaeucAi6V6yBv0r39RD%2FBhqKqgRCj%2FGY0gJiUB4bhaXN0Kk1urFh%2B53YyHpXsxIrzJJyTFh8t2DN4%2BSNdMQmeHgJ3zvJ1u3YkG%2FfLr754QGFPAvSWIVdhVCkscxNDt5BUAMlAXlUQMyMfK9%2FuORx6LMc%2FFBwyllc2RzVuwxHl29CwTjpiHNnLS%2BG6fNwakIGmLQwv9uO0wY6pgFSO4sJdo1s%2FQeDHgqZFvA4naPZj2%2FN9qinDEqVmxYkLEf0ddhoq1s%2BmXFc0D7%2F5LN7SjZhuINwhi2nlm0JBtq4quSi8JswfLctxwoGd4HiVONqSOrj2cK0G5oM4%2BMA2l94pIEfXbworkn6xyipfKhjNwlMr8n5Q3hmeIN1%2FblGxRZCYLgh1BnzJVf0Ny6tzpsmuZxn8M%2FsCjkPUwCY7C5ltczRu0zb&X-Amz-Signature=5548ce8def5e0c53d70ecbc747dad1cbb7886155c62aa35ea5ba84913a8d4694&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
