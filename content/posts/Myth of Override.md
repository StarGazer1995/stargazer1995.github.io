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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYRE6RBS%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T053054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDkjbMVAXJRcqhfRhLOr1A1Z20QwUWbboWXYozpIRtnxQIhAM8eGyN8rxTAw1w6J%2FcV4U%2B5JSLKF7IuiOP3YbdCk%2BQOKv8DCCQQABoMNjM3NDIzMTgzODA1Igxg8a9NntHSYj3d%2F0Aq3APBWEo%2BBXIBG3Umvu6myWbguwEGYLqh3z7vySC7yvch4siVmDMqnBFeFVL4kov%2BmXHuoIzo3BMmttDxMs5EKPOrUn1DqZadUUtLSUkxZ9P7EZU6zEzDsAo2WAxLmg7ivExvr%2B7A1PmkNDRJ9RWoMeof2VX22mHBhZAh1TyZ%2Bu1gIhZajp%2FCXvbQpY4w0A1v11B5FN3VSxm4gPDsT4vTBgeLkBIfl4mncj%2Fxy2%2FPoXf87fVFMUy5FXBPYYvdw%2B7H3eygXBu7lL8bB4xcUYwEmeSF4GAoDM%2BosKD3%2B8XUqZ5KF%2BC9GtZDwvFR2%2F0TbOXqEOLQN8K3Ce0qgT5ekanm8acJ%2BCXFroWtReWG%2FcC8qo6Eup9zOjlWqf6%2B24KmbIkQf%2BYYSuCpFJ%2FzUvvHR5OdP9JnaFM%2BUVKR4m1XMQrmxhHHc9ILD2NA3VIw5ifglwbpkqAIVwnR632mrToXjolfspWqcc6%2FHInN%2FLa4F8OcC3bNO1VKuBwI56jD%2FswGip2%2F1tITnwIHDE%2BzDdGbV4SdR7g%2Bygeld0CxScDGmp8WfW3VjhhdmBJ1l6T12Rajr%2F%2BoOxe3phnS9ua%2FW%2FTIZUlFSdBS1m%2BwJNBm%2Bb4mPxW0XxoQKIAhmbeiEYpVn3VvfDDCn4rQBjqkAcD%2F0FXcP9Ou3rhB9vOf%2B0EG7dl%2BocP9D4lirx%2FlhBESxtLxVDpRPwgSkcn2lwcPEMoENLzdpEaVczqf3YY6Ei7xNHxmGhLNvMBvqY1FgOGI%2B5gllaxzCokGSDgWi51r7AdcGc6t8iYohtxHXfPy70PouXhTi6t5mj20Y1BZcQU1b%2BF0huPkCUfgs3UhCby8nud%2Fe9LL6hXbRMuup2CLUvQ%2BpsTp&X-Amz-Signature=1848915f098964ec29f516b2802c3fdb0c65b5b005d496f7fed2ee4fddd1d162&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYRE6RBS%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T053054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDkjbMVAXJRcqhfRhLOr1A1Z20QwUWbboWXYozpIRtnxQIhAM8eGyN8rxTAw1w6J%2FcV4U%2B5JSLKF7IuiOP3YbdCk%2BQOKv8DCCQQABoMNjM3NDIzMTgzODA1Igxg8a9NntHSYj3d%2F0Aq3APBWEo%2BBXIBG3Umvu6myWbguwEGYLqh3z7vySC7yvch4siVmDMqnBFeFVL4kov%2BmXHuoIzo3BMmttDxMs5EKPOrUn1DqZadUUtLSUkxZ9P7EZU6zEzDsAo2WAxLmg7ivExvr%2B7A1PmkNDRJ9RWoMeof2VX22mHBhZAh1TyZ%2Bu1gIhZajp%2FCXvbQpY4w0A1v11B5FN3VSxm4gPDsT4vTBgeLkBIfl4mncj%2Fxy2%2FPoXf87fVFMUy5FXBPYYvdw%2B7H3eygXBu7lL8bB4xcUYwEmeSF4GAoDM%2BosKD3%2B8XUqZ5KF%2BC9GtZDwvFR2%2F0TbOXqEOLQN8K3Ce0qgT5ekanm8acJ%2BCXFroWtReWG%2FcC8qo6Eup9zOjlWqf6%2B24KmbIkQf%2BYYSuCpFJ%2FzUvvHR5OdP9JnaFM%2BUVKR4m1XMQrmxhHHc9ILD2NA3VIw5ifglwbpkqAIVwnR632mrToXjolfspWqcc6%2FHInN%2FLa4F8OcC3bNO1VKuBwI56jD%2FswGip2%2F1tITnwIHDE%2BzDdGbV4SdR7g%2Bygeld0CxScDGmp8WfW3VjhhdmBJ1l6T12Rajr%2F%2BoOxe3phnS9ua%2FW%2FTIZUlFSdBS1m%2BwJNBm%2Bb4mPxW0XxoQKIAhmbeiEYpVn3VvfDDCn4rQBjqkAcD%2F0FXcP9Ou3rhB9vOf%2B0EG7dl%2BocP9D4lirx%2FlhBESxtLxVDpRPwgSkcn2lwcPEMoENLzdpEaVczqf3YY6Ei7xNHxmGhLNvMBvqY1FgOGI%2B5gllaxzCokGSDgWi51r7AdcGc6t8iYohtxHXfPy70PouXhTi6t5mj20Y1BZcQU1b%2BF0huPkCUfgs3UhCby8nud%2Fe9LL6hXbRMuup2CLUvQ%2BpsTp&X-Amz-Signature=20d488fb211b1f9b5a8fce68085e14e90b2b9eaf9e05b3be6335830bbd4f5b54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
