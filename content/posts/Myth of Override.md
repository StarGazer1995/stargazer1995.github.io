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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3Z6IAY3%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T230305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDraaDs9M%2FDHQnyewHpkWBKvZqeG1V8sPmPkfE9Y65wqwIgPDa%2BkFsnMumFBVMmY3GVn1jHO2p02LAFPCjQMjVEsGkqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6hbDtqi4Ns67Jx%2BSrcA6JQ7bui44RaRcjR93ZUCoLCn3MxMVzNQqChZ2H9qINbgwI4pwW9qCUv6s%2Fya2KBgbWENhKhPJ3753NRrRVJl%2BiKjGEgkog5BAkG32CZ%2FANEhmwsp%2FY70TPbEMOshK8Tz7MlTUOAqLkaC46rHJ%2BDMikAZMQUNbVb87rhmo8qZqn0TZL60FYNt3im1fhAAGHQEBsGlJo0RHBggLhDCDdoHL2PU58V73Pz5sM0wXTi48gNHBUU%2BPKCBxIyM8WZ2r8%2BbQEgbfDDDORe%2FKM7fFnYvcnU0JmFv6wv0QNWngkytnBGFUuALfyDskseo6A2PtuX%2F6hiAEa1Cn4LstzhUxbcJ3GFQwAnZN738M3xinC8S7D5mQj%2BkgRM8mAC3iQ6ASCb%2F95O871F14y92d3t84qQZIdepraMZSX7hVtf9CKuQOG3NoKTygE4rclx6BSnAKCQQUs7%2FSPY%2BVE%2BNYRoy1EUEaavXukT080NlLsCHeeLr9kNX5loUsszhqDyo2ByTiuUYxmEHuJTNqxfxSv2tIyiVOavZ03%2FA6%2BKTxxpoO1%2BoOfy%2FazWZTnAluiuWeo%2BZ5BAhO90O8k95F2z3ewpMNZZBA7zk8ZGJMKHHySp9y2pSZ4CTUzTUDr65%2BphkiUsMPnnkNIGOqUBLwLzIbjT68C9n%2BwvGLI%2BdSCIN%2FoskASuybV%2FIf00IINZUfWKLr%2B5uKo4cBJFKy5bLj9JQfTsw%2BKqeD010Hk3wzhWBVls0wjKfeqLZTFX0Y9mRUsmJQfS3I7DqonS9kWrEz1BvcCe5KMtz%2BqNdFBjJrUtZVAtmtY%2Bu%2Bt%2B%2FzsqkLe4iMWu4%2FL6aZUnq60a0Of0mXhXNRBPN4J%2B1VKRI9AL36Hz%2FPKA&X-Amz-Signature=774ffab5a5c0a4e7857f70336bc4fcbf002f632f43e476c4f8550210d4d218b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3Z6IAY3%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T230305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDraaDs9M%2FDHQnyewHpkWBKvZqeG1V8sPmPkfE9Y65wqwIgPDa%2BkFsnMumFBVMmY3GVn1jHO2p02LAFPCjQMjVEsGkqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6hbDtqi4Ns67Jx%2BSrcA6JQ7bui44RaRcjR93ZUCoLCn3MxMVzNQqChZ2H9qINbgwI4pwW9qCUv6s%2Fya2KBgbWENhKhPJ3753NRrRVJl%2BiKjGEgkog5BAkG32CZ%2FANEhmwsp%2FY70TPbEMOshK8Tz7MlTUOAqLkaC46rHJ%2BDMikAZMQUNbVb87rhmo8qZqn0TZL60FYNt3im1fhAAGHQEBsGlJo0RHBggLhDCDdoHL2PU58V73Pz5sM0wXTi48gNHBUU%2BPKCBxIyM8WZ2r8%2BbQEgbfDDDORe%2FKM7fFnYvcnU0JmFv6wv0QNWngkytnBGFUuALfyDskseo6A2PtuX%2F6hiAEa1Cn4LstzhUxbcJ3GFQwAnZN738M3xinC8S7D5mQj%2BkgRM8mAC3iQ6ASCb%2F95O871F14y92d3t84qQZIdepraMZSX7hVtf9CKuQOG3NoKTygE4rclx6BSnAKCQQUs7%2FSPY%2BVE%2BNYRoy1EUEaavXukT080NlLsCHeeLr9kNX5loUsszhqDyo2ByTiuUYxmEHuJTNqxfxSv2tIyiVOavZ03%2FA6%2BKTxxpoO1%2BoOfy%2FazWZTnAluiuWeo%2BZ5BAhO90O8k95F2z3ewpMNZZBA7zk8ZGJMKHHySp9y2pSZ4CTUzTUDr65%2BphkiUsMPnnkNIGOqUBLwLzIbjT68C9n%2BwvGLI%2BdSCIN%2FoskASuybV%2FIf00IINZUfWKLr%2B5uKo4cBJFKy5bLj9JQfTsw%2BKqeD010Hk3wzhWBVls0wjKfeqLZTFX0Y9mRUsmJQfS3I7DqonS9kWrEz1BvcCe5KMtz%2BqNdFBjJrUtZVAtmtY%2Bu%2Bt%2B%2FzsqkLe4iMWu4%2FL6aZUnq60a0Of0mXhXNRBPN4J%2B1VKRI9AL36Hz%2FPKA&X-Amz-Signature=f7071fd74d581ce724b622fcf790ee2d772d0807df6e195a040751e3eb8f1884&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
