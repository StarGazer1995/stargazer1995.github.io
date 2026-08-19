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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7QJAPNJ%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T082233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfRB5KVb65fe9pDl1%2Bhqe%2FaPvo5x1X8OP28gfGI06KdQIhAMCu0bfmT9A%2BWJGWzZTXuh6MqHg%2FQ7rKCLejKbycTKdDKv8DCHAQABoMNjM3NDIzMTgzODA1IgzAvrjN1ErdaqhbT2Uq3APJqAzo%2BNNnDs19SGdpzrqOZob%2FVEsuPUq5jNBqQYcuW5fybB%2BQqlKvq9znFdrsT4Krp%2Bw%2BGhMMOWBUTve0VOanU1Jgv1p%2BX8kjezV7V3lz0qaEhf0jV6vWX2MzTvpbTOhe7tMZTZQUP2feHZHsbjiLChmW%2BUB0fPBYarSvPMYBssNqKCB%2BwAJfyGza%2FPkcolmbeYIZcX9q9lL4iMc4SF3tBdwj%2FvWX8rQhkAcVf8aqXJn8Jv1D9jJe3UpQuQV9Ag%2BrNsa2x2AtaMLNg%2Fl3EsG0iZcN40zdTnBictL4ExjCq9a8GBaDG1ltYHxM1e4NhWWZoANumt3JxJUhEGu3lLCM%2FtyKTnUMgRT5VQqNY8Iypz2px04ruj8PtJbpBYPHxsIayVAmqC6UkDe%2BFSrBgANn5bt1%2BV%2Bd4%2B%2Bt8ujqC7ThKGdAF8QXdit3iGP7nsS5XTZ0LlyBn9kK74Vj7RaUfztWVvWb7Ta3YE3JmuLVjAgK53py%2BSBoUQNdHYtCejdris3FSQX46Kf2T0gzQn9uf4tcFdZ2EnpNV0lRICyGWjVQsjnSjUjthhHBfWkpiNMvJi3K3vQ%2FowHU6OCjL7QQcsKGSF8NkeXGhmE3VR%2F3lP78ovA6%2BoteXDBxw1SjIzDXn5XUBjqkAeF2FvbLr6N9ZmoeBWk%2Bo9BCdk84ck3EYkdJ3aneJTdyYqa0IwVuQQl8uvCgxI8LKIQ8OK6LNTyYxsjQSAqwvgeNLXO8wUdBhaGsrX72SnoSuylO%2B1jWFXAuZNupMEPO9J2OOucGOMSgpkD67mQL9de90buuR2I71NKpGGoyyQ4wmOn8t1unWLPjcv6UYiHrppd3rJuuUnOx%2FV%2B76iS%2BsHSosTZT&X-Amz-Signature=87100f082c5a7b07cd2d5ba748c44686511d929ed80f432b5b0f98f43f4bc828&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7QJAPNJ%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T082233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfRB5KVb65fe9pDl1%2Bhqe%2FaPvo5x1X8OP28gfGI06KdQIhAMCu0bfmT9A%2BWJGWzZTXuh6MqHg%2FQ7rKCLejKbycTKdDKv8DCHAQABoMNjM3NDIzMTgzODA1IgzAvrjN1ErdaqhbT2Uq3APJqAzo%2BNNnDs19SGdpzrqOZob%2FVEsuPUq5jNBqQYcuW5fybB%2BQqlKvq9znFdrsT4Krp%2Bw%2BGhMMOWBUTve0VOanU1Jgv1p%2BX8kjezV7V3lz0qaEhf0jV6vWX2MzTvpbTOhe7tMZTZQUP2feHZHsbjiLChmW%2BUB0fPBYarSvPMYBssNqKCB%2BwAJfyGza%2FPkcolmbeYIZcX9q9lL4iMc4SF3tBdwj%2FvWX8rQhkAcVf8aqXJn8Jv1D9jJe3UpQuQV9Ag%2BrNsa2x2AtaMLNg%2Fl3EsG0iZcN40zdTnBictL4ExjCq9a8GBaDG1ltYHxM1e4NhWWZoANumt3JxJUhEGu3lLCM%2FtyKTnUMgRT5VQqNY8Iypz2px04ruj8PtJbpBYPHxsIayVAmqC6UkDe%2BFSrBgANn5bt1%2BV%2Bd4%2B%2Bt8ujqC7ThKGdAF8QXdit3iGP7nsS5XTZ0LlyBn9kK74Vj7RaUfztWVvWb7Ta3YE3JmuLVjAgK53py%2BSBoUQNdHYtCejdris3FSQX46Kf2T0gzQn9uf4tcFdZ2EnpNV0lRICyGWjVQsjnSjUjthhHBfWkpiNMvJi3K3vQ%2FowHU6OCjL7QQcsKGSF8NkeXGhmE3VR%2F3lP78ovA6%2BoteXDBxw1SjIzDXn5XUBjqkAeF2FvbLr6N9ZmoeBWk%2Bo9BCdk84ck3EYkdJ3aneJTdyYqa0IwVuQQl8uvCgxI8LKIQ8OK6LNTyYxsjQSAqwvgeNLXO8wUdBhaGsrX72SnoSuylO%2B1jWFXAuZNupMEPO9J2OOucGOMSgpkD67mQL9de90buuR2I71NKpGGoyyQ4wmOn8t1unWLPjcv6UYiHrppd3rJuuUnOx%2FV%2B76iS%2BsHSosTZT&X-Amz-Signature=f3d0a54562140c2df73d95b4e7df87fee9391d3a9ab264691204c270a50ad4c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
