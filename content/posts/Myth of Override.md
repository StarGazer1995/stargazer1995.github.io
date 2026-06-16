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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665B2ZYRG%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T023544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHGyX6TnNsOk%2B4IopzNWquk8mz%2BbAWMlR4BEMvw8cxvAAiEAreFdEY%2FTUDBvqWnea9A8RcBFUY7Sqs6Ne3PphbMWfLYq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDKqK0964JHMB4bQUJSrcA2CRkqm%2FD0HcLEA%2BkJJfxfawvyYz8NI6GayKSp4N7uMyJ8XLdW%2BOACTdHWafZqX5mSGwN1oEVm5fSjTvVj6SLbkFJTBmvvPhhbD7l5AsWTK34vm3QUaP2ue2dict0M6pWTP18SMOcgijn2nuiI%2Bkc4f70y0%2FDmfjmVmVYC2%2BIUrIWUdQJOZEPZHtiB25JkLj%2B8r3HSA0ABxBTbMwVkYr%2BBe4DGkMAFrrc5O5%2FxwIEJyEEh05H9L%2BRiKugsH9nA5x9TWMsyvtUR5TwVfqckC4xXQYNlevm4lwRXBSFlSu2Rlhw%2FZm9bDofnZIIJ9%2BA3PwQTNbnvY%2Bcf4j7l19nRiU9r15j37dQzsOnUTZ82pFTGRokKwSxK2ohmac3%2B80zqe0ilqGKdZ3okEK0gBHNK4OhoHe9yW2riL7I3evf%2BpG56NgsOHPbTUelIStQ%2FiFOAaupTlxAZQsavMQ%2F0zWnZof1ZrRelWotmK4M7aY0Mwrt96nnj9XAxqI4uVn8zhf22ufmpI78ctvWBHAOwP1y160qLzE%2BiWkDz6ME6CnHs94Nop5tzbwSN32rPPrQM%2BGc1ZisNVQvYLcaPfSF3t3yrGfb33tgazfBqCeEHuJeZNZBtVnHQooTSPZ%2FbXcRn2IMP3dwtEGOqUBdF9%2FnYFfxUfqNui3Ixp9VzV%2Fjhbq0s3gYIbkSrnz%2BUDdp7ilP5Zb0J24JtjJMYfrI6ZFmbOdtdFrtGeYcIzGeAQ9LqEEjq69QnUQmU1isuOWcJNzi702F5jXVP%2BRXQWJZDMo%2B6d15Wc9KaDglhLbXYhJvvcO%2B7Af8r4vD6X7dt6U4CyWiHYKb%2FFjxxSAKl78nHL6%2FHwffQxUKsiES5mm0oB3t9x%2B&X-Amz-Signature=2d546714c413ae5396dea1c721ce79d9c61e34583e332320bf568fa326362a32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665B2ZYRG%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T023544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHGyX6TnNsOk%2B4IopzNWquk8mz%2BbAWMlR4BEMvw8cxvAAiEAreFdEY%2FTUDBvqWnea9A8RcBFUY7Sqs6Ne3PphbMWfLYq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDKqK0964JHMB4bQUJSrcA2CRkqm%2FD0HcLEA%2BkJJfxfawvyYz8NI6GayKSp4N7uMyJ8XLdW%2BOACTdHWafZqX5mSGwN1oEVm5fSjTvVj6SLbkFJTBmvvPhhbD7l5AsWTK34vm3QUaP2ue2dict0M6pWTP18SMOcgijn2nuiI%2Bkc4f70y0%2FDmfjmVmVYC2%2BIUrIWUdQJOZEPZHtiB25JkLj%2B8r3HSA0ABxBTbMwVkYr%2BBe4DGkMAFrrc5O5%2FxwIEJyEEh05H9L%2BRiKugsH9nA5x9TWMsyvtUR5TwVfqckC4xXQYNlevm4lwRXBSFlSu2Rlhw%2FZm9bDofnZIIJ9%2BA3PwQTNbnvY%2Bcf4j7l19nRiU9r15j37dQzsOnUTZ82pFTGRokKwSxK2ohmac3%2B80zqe0ilqGKdZ3okEK0gBHNK4OhoHe9yW2riL7I3evf%2BpG56NgsOHPbTUelIStQ%2FiFOAaupTlxAZQsavMQ%2F0zWnZof1ZrRelWotmK4M7aY0Mwrt96nnj9XAxqI4uVn8zhf22ufmpI78ctvWBHAOwP1y160qLzE%2BiWkDz6ME6CnHs94Nop5tzbwSN32rPPrQM%2BGc1ZisNVQvYLcaPfSF3t3yrGfb33tgazfBqCeEHuJeZNZBtVnHQooTSPZ%2FbXcRn2IMP3dwtEGOqUBdF9%2FnYFfxUfqNui3Ixp9VzV%2Fjhbq0s3gYIbkSrnz%2BUDdp7ilP5Zb0J24JtjJMYfrI6ZFmbOdtdFrtGeYcIzGeAQ9LqEEjq69QnUQmU1isuOWcJNzi702F5jXVP%2BRXQWJZDMo%2B6d15Wc9KaDglhLbXYhJvvcO%2B7Af8r4vD6X7dt6U4CyWiHYKb%2FFjxxSAKl78nHL6%2FHwffQxUKsiES5mm0oB3t9x%2B&X-Amz-Signature=700ad78ae09d1de7a9665f56caffec24bb8fa01b2344afbc17ee075c4cb6c1e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
