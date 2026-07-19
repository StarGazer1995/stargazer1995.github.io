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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NHS4JVA%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T045946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZj6k5QCIYi28La%2BaFG4cz%2B9gFWJz%2B%2BYQauIq%2FhGPJeAiBZ%2BDL%2FacIOAoKdxU%2FnQTBpyNvro%2FqCodNBIz%2BzPrHvmyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BHf6HzEglZ6SxcMPKtwDBKV%2B%2B0eSqqO%2F6FuuDl3mxuzUo4ZaMnXWDHmmEy1INecHMuctqUp%2B4dQPVnbFf8uk%2BzTZY0%2B8%2Bv%2FodVc3RUWZMrChbEk4wblqu2C4%2FObvTyws%2BrvbkC6U%2Bf35Xgt%2Byh4WY4dTh4mADW7EA%2Bnv64VtVB1JuNtl9VqjkKZbNzm2k9M0qtaqlTiTX5a72BkWuO7oLLHJaJ7tCAysMcAY%2F5Iq7iJr5KhKg3TIbBxcX8uySAVXAz8yeXjXXy%2B2%2BF7DTiHEYN889pbCpiRUlgME8fIWRJLyh7YVHTH7az6oXQ6MviL5P%2BOUR5bScm7vUoRSjB%2FH6VFqye%2F7izQUFzYJAdxbN54ZTz9M9MyWwvPMkcT20Gnc6eyARzbaTq6Om1OPklUSHvHMj9ETwWrCUS5Le%2FsM9wSp350BX3zK3KvZoh1fRwjeber22f5H7H8Ic6ReT4nUeJWaXrZu2Xb%2BbTr9fdMOyErT%2B1NaHNV3wXcU%2BFgIbgkc5YAvsrcYSFSY8gmsQ3bcvmI8BCiGZXFWxuStxji7nPulxmT5ISjK3xT0vh97GB%2FmSHcB2l4WL9C2zduopdic7XOGp8pRJSil9kyYwsWozywbyjKwA1ADu1gB0eWLDNxeR63EnMIq9xmjDQYwx4fx0gY6pgE%2BY5%2B3IPFXSfMPKaM7d5ra1DVer0co0J9qqPm89C%2FpjXDBC85jacOK3i4EEdDvnZ3Iz5VFwU%2BJ%2BhWVmihAtKCJEiovYAImAW7PRKymFia9sY7p6Hr5VJCbhTkmE%2FNBfyKD14ZR77%2FtO62qrk3EIz8cN2ssRyTJebt1ehIUessJoPJF50XZg8vBJMgzGqKoLhG3lRowKsqCGkmNh4rUfrsEWgbOyj27&X-Amz-Signature=113a128b6c56339d93a64c21c27717bac65660991b49637a60b9eaf7e7e3f0b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NHS4JVA%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T045946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZj6k5QCIYi28La%2BaFG4cz%2B9gFWJz%2B%2BYQauIq%2FhGPJeAiBZ%2BDL%2FacIOAoKdxU%2FnQTBpyNvro%2FqCodNBIz%2BzPrHvmyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BHf6HzEglZ6SxcMPKtwDBKV%2B%2B0eSqqO%2F6FuuDl3mxuzUo4ZaMnXWDHmmEy1INecHMuctqUp%2B4dQPVnbFf8uk%2BzTZY0%2B8%2Bv%2FodVc3RUWZMrChbEk4wblqu2C4%2FObvTyws%2BrvbkC6U%2Bf35Xgt%2Byh4WY4dTh4mADW7EA%2Bnv64VtVB1JuNtl9VqjkKZbNzm2k9M0qtaqlTiTX5a72BkWuO7oLLHJaJ7tCAysMcAY%2F5Iq7iJr5KhKg3TIbBxcX8uySAVXAz8yeXjXXy%2B2%2BF7DTiHEYN889pbCpiRUlgME8fIWRJLyh7YVHTH7az6oXQ6MviL5P%2BOUR5bScm7vUoRSjB%2FH6VFqye%2F7izQUFzYJAdxbN54ZTz9M9MyWwvPMkcT20Gnc6eyARzbaTq6Om1OPklUSHvHMj9ETwWrCUS5Le%2FsM9wSp350BX3zK3KvZoh1fRwjeber22f5H7H8Ic6ReT4nUeJWaXrZu2Xb%2BbTr9fdMOyErT%2B1NaHNV3wXcU%2BFgIbgkc5YAvsrcYSFSY8gmsQ3bcvmI8BCiGZXFWxuStxji7nPulxmT5ISjK3xT0vh97GB%2FmSHcB2l4WL9C2zduopdic7XOGp8pRJSil9kyYwsWozywbyjKwA1ADu1gB0eWLDNxeR63EnMIq9xmjDQYwx4fx0gY6pgE%2BY5%2B3IPFXSfMPKaM7d5ra1DVer0co0J9qqPm89C%2FpjXDBC85jacOK3i4EEdDvnZ3Iz5VFwU%2BJ%2BhWVmihAtKCJEiovYAImAW7PRKymFia9sY7p6Hr5VJCbhTkmE%2FNBfyKD14ZR77%2FtO62qrk3EIz8cN2ssRyTJebt1ehIUessJoPJF50XZg8vBJMgzGqKoLhG3lRowKsqCGkmNh4rUfrsEWgbOyj27&X-Amz-Signature=664260a55d2a6a9ce650054b5661646d4e5e1d079819f4b75bd2e3bd753b2ec8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
