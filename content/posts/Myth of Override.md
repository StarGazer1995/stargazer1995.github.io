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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPZW64XY%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T164332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHG5sxj7k%2BPYMs8t1fKPXLYCM3UpQANDApSJPpBkSrx9AiEA0mIh0erL3ww0MJvZXlS%2B4BfOS9lkX7AYYdb9zEKRaqAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDBGqU4CixlGWIRnzTCrcA7S%2Fd8xXpZRnutKS6gfrIF6UR0eA4w%2F1oUkEQ9Lo%2FjMPzU6H4amGE0fFwshm9ctHtvFblMgkKK81f5%2BG3x8JCmDUMzGjjbyHu%2Fc5Ao5xNVt%2FjPJEHyXc1NgGsWhyNCqpBZDNvi6O96HldDlRbSKh0UAyCOzENtk%2FWzMut3VXxWtQW3sNELDOyblTCI4vTNZMtk9Wze2DnGc6YymHdRj%2FWsyzpzkE1P%2BJB7ph6hxLSW2k%2Fn1Y9ISGSBn%2BQD3WMBdC8hReDYPHViy0bw%2B4OKCTIqpOZ2tADI7B2%2BGYaCj2DdkQkx9tJEMXbllmJyv3VH9ktUtWFiYhAYlTnCUVXKoCcWWf0dN9QbeEOfBInaudwsOoiqb1GYdv9O4MRhP6lrQhnD49T1fRUnNyrJTou6Xe2NHmUnghAA9ERIiBUSl6V9wmzD0biPIKt%2Fe%2F784DL4qdlkPB2nsSO24MjJfwCrFNHZMXeH0kdWtk0GSeFO6i2nN%2BZOA2WJVt%2BsvR6BRIJczAxXwJYeNVxywKt6%2BC%2Fo%2FesHj4rhqsqoOx32HzUiZyS06oWwDUk6K78aVQger1yfU43BOv6UBv87y6ursA9ywIbq4jBBpkTSdK0nwgBzC3ljzH0nKkk6KGQaMb0ZvXMIyqhtEGOqUBuelyK%2BWRWvmfuAjKyeX4ztcPSf4lF583qA8lDkth%2Bz0t3fCrfSk52A9jPbsolq41Vegg0IddFrJiCRhCqmFIQjeie5wFwUEV96nU8cMkPW8SNDtdA9T3sSR5TOo8vsMq%2FL6R7xXbdWbDVhaYL2lKjOv4l4xZo2%2F7Xyf4YEB5iE5NIGwMAhEG0sqIsbOL7%2BvFjsJBoqmKFP0FxJ3p0HbR3KDrFZ2V&X-Amz-Signature=be9bbebe03a8d6b5217505e59b3c753ef16b78bf728924759e7108eb98703100&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPZW64XY%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T164332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHG5sxj7k%2BPYMs8t1fKPXLYCM3UpQANDApSJPpBkSrx9AiEA0mIh0erL3ww0MJvZXlS%2B4BfOS9lkX7AYYdb9zEKRaqAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDBGqU4CixlGWIRnzTCrcA7S%2Fd8xXpZRnutKS6gfrIF6UR0eA4w%2F1oUkEQ9Lo%2FjMPzU6H4amGE0fFwshm9ctHtvFblMgkKK81f5%2BG3x8JCmDUMzGjjbyHu%2Fc5Ao5xNVt%2FjPJEHyXc1NgGsWhyNCqpBZDNvi6O96HldDlRbSKh0UAyCOzENtk%2FWzMut3VXxWtQW3sNELDOyblTCI4vTNZMtk9Wze2DnGc6YymHdRj%2FWsyzpzkE1P%2BJB7ph6hxLSW2k%2Fn1Y9ISGSBn%2BQD3WMBdC8hReDYPHViy0bw%2B4OKCTIqpOZ2tADI7B2%2BGYaCj2DdkQkx9tJEMXbllmJyv3VH9ktUtWFiYhAYlTnCUVXKoCcWWf0dN9QbeEOfBInaudwsOoiqb1GYdv9O4MRhP6lrQhnD49T1fRUnNyrJTou6Xe2NHmUnghAA9ERIiBUSl6V9wmzD0biPIKt%2Fe%2F784DL4qdlkPB2nsSO24MjJfwCrFNHZMXeH0kdWtk0GSeFO6i2nN%2BZOA2WJVt%2BsvR6BRIJczAxXwJYeNVxywKt6%2BC%2Fo%2FesHj4rhqsqoOx32HzUiZyS06oWwDUk6K78aVQger1yfU43BOv6UBv87y6ursA9ywIbq4jBBpkTSdK0nwgBzC3ljzH0nKkk6KGQaMb0ZvXMIyqhtEGOqUBuelyK%2BWRWvmfuAjKyeX4ztcPSf4lF583qA8lDkth%2Bz0t3fCrfSk52A9jPbsolq41Vegg0IddFrJiCRhCqmFIQjeie5wFwUEV96nU8cMkPW8SNDtdA9T3sSR5TOo8vsMq%2FL6R7xXbdWbDVhaYL2lKjOv4l4xZo2%2F7Xyf4YEB5iE5NIGwMAhEG0sqIsbOL7%2BvFjsJBoqmKFP0FxJ3p0HbR3KDrFZ2V&X-Amz-Signature=846cb7708c8af644b5f7f83ce2001d872cf0ea1b82e3fe9ee6edf85a0696cb00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
