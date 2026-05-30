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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UX2QDFG%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T130007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICBXW1nAvVusZt3VIn52QvI6%2BgDD%2BFbr2SwWc8CtsfZRAiEAkbg%2FdJzunD7K5MiINf%2F%2FpfXrBJ8SND1c0zzyFxZAovQqiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIZzcCT5ef91oPR9SrcA7kvuhQUTlcbCBwk45aq%2BcxQAuw2lf8klj2Edsc2CA%2FeidODGzW5bjPOTRDYH%2B99w8LpuMVPFkSRfVgvczXDEEXj4FxZOSCAJMMLk6ZIjEw5c6UL7PoPo5JAneVFHA5TgdVZumR7T5%2BXJW0%2Bz0cY37Z%2Fwne9lAno%2BaxhA38Zn82Kv%2FQHyz54DYUzkHrh1YovD80xW8rIjTXlh2T80Q5hQxHIq%2FYrI%2FN8T3Rr7HpEnQdrWTKXrnqpXYcdLWtPXwUqG94xnJhOdiyOF8sRl7%2BVVyl71w4dxbG3XdAccAjTHWX8e3qCEKYtN5d6j9ixPyJmk9vUtei%2FxnahPzse7OlFpR0WH6M8hMe5Ufifm6jV2g%2F%2FBB7IXNA0eABBvQrfIfTu3xLrMv3%2BgtJnPTo4xheeaNSQok%2BBKMJzHZHZeSMGShzUhfq7NYFneBe9IBOeE%2FAnC2SjUAKWtdDtGA6fxFf0kicCN5YAZvQ8vUe2Q4pdN7EL3RLnt2RBfKAjQx7NQP15A4RXYZQ%2BnLYAogQdiDCVHRMhQtu2ZvAcVczaeZvQgLwx%2BMl0JCpZ6qCLeM7edwkfo9KQGOrml%2FkuN0uM4G5g%2FzzX1oIx9uYCNSqW3h2dpAQNY9BOZkVzOhAR61O8MLSJ69AGOqUBE5n%2B%2B0Fa8jEcQUN7zLa%2FJMcO8GLee5rfcOGwNraLYb7n%2BYTn3QUFeVZE9vAo%2FtZ6fHqGVRL2nwRV0rw7QOUl%2BjWH%2BCLtBnzAUyz4%2F093O4mK8EHvBcuQxCTKvzDDcyE08ItFFnf4dI6gJxtGkLip%2FeU7PK7NCABNMGOdx1WD8oZAcEovXGD2W2KeCko5fTPADPwQwwlaIKAgJgLhrtBClEWIhAEq&X-Amz-Signature=93d507da944dad1cac48f1a3958a2366bb4b29faaf6460229dce011b89349add&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UX2QDFG%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T130007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICBXW1nAvVusZt3VIn52QvI6%2BgDD%2BFbr2SwWc8CtsfZRAiEAkbg%2FdJzunD7K5MiINf%2F%2FpfXrBJ8SND1c0zzyFxZAovQqiAQI3P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIZzcCT5ef91oPR9SrcA7kvuhQUTlcbCBwk45aq%2BcxQAuw2lf8klj2Edsc2CA%2FeidODGzW5bjPOTRDYH%2B99w8LpuMVPFkSRfVgvczXDEEXj4FxZOSCAJMMLk6ZIjEw5c6UL7PoPo5JAneVFHA5TgdVZumR7T5%2BXJW0%2Bz0cY37Z%2Fwne9lAno%2BaxhA38Zn82Kv%2FQHyz54DYUzkHrh1YovD80xW8rIjTXlh2T80Q5hQxHIq%2FYrI%2FN8T3Rr7HpEnQdrWTKXrnqpXYcdLWtPXwUqG94xnJhOdiyOF8sRl7%2BVVyl71w4dxbG3XdAccAjTHWX8e3qCEKYtN5d6j9ixPyJmk9vUtei%2FxnahPzse7OlFpR0WH6M8hMe5Ufifm6jV2g%2F%2FBB7IXNA0eABBvQrfIfTu3xLrMv3%2BgtJnPTo4xheeaNSQok%2BBKMJzHZHZeSMGShzUhfq7NYFneBe9IBOeE%2FAnC2SjUAKWtdDtGA6fxFf0kicCN5YAZvQ8vUe2Q4pdN7EL3RLnt2RBfKAjQx7NQP15A4RXYZQ%2BnLYAogQdiDCVHRMhQtu2ZvAcVczaeZvQgLwx%2BMl0JCpZ6qCLeM7edwkfo9KQGOrml%2FkuN0uM4G5g%2FzzX1oIx9uYCNSqW3h2dpAQNY9BOZkVzOhAR61O8MLSJ69AGOqUBE5n%2B%2B0Fa8jEcQUN7zLa%2FJMcO8GLee5rfcOGwNraLYb7n%2BYTn3QUFeVZE9vAo%2FtZ6fHqGVRL2nwRV0rw7QOUl%2BjWH%2BCLtBnzAUyz4%2F093O4mK8EHvBcuQxCTKvzDDcyE08ItFFnf4dI6gJxtGkLip%2FeU7PK7NCABNMGOdx1WD8oZAcEovXGD2W2KeCko5fTPADPwQwwlaIKAgJgLhrtBClEWIhAEq&X-Amz-Signature=65b67d54f40707ceff467e334040fb419911967a5aaa04f4ca9c410bcbd46f47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
