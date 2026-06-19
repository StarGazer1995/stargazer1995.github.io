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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV4Z46DN%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T085755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBrChSKsrTtfqDBmEfi1gTEKzPQHWdjuJvMXPDGHv4BwIgQbe%2BgLh7mHANsANoFxGYAQ0CB8k7aO9mXbu4EzFSZXMqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFoQ5hYQzKL29rbRCrcA3r0dfkblbl%2B8vOhOhbTWvErI%2Fhv%2FB0dqzj7ZhBKeTJBp8ElJIb61oYlVhQui4pI5L4%2BpWoOlAndmbR3wAM7q0aqZqqlQQrbK%2BIIK73uCSifT8M6xklmhRp7xSH7gpJD9rW8NQR75S6MVBv5MXAP1Z%2Fh7ByTZASdTc68vUgfE9PX4k39ept2Ut4x4t6E4LD0vdpfnMXQzSXxCrLL8hAV3%2BoL8pLZ7J1Bf0bzWVgSjDspS1uP%2F6LuArMbIpRgjAQXp7rNvB2v6Asj69m%2BCHLBFBVdL6DH7TAwS4nLBz4YE6I2uk28SPDZ6WYyaCgqH%2Fx2YqnB4w%2BlB4%2BnIyT6E75BWQEmLVwENNv3PUHVWCJmYGNbAruO98jZKN6g8SgZND2qnlldaQm%2FQ8WvEJv%2FSF0REL6qRUf9GXcRUYkd97bNdRnLthDB46JbTeQkgupL8fzeCh%2F3ZfqLv4j0z4Kh4HRewDS222YOlCdsNT9JpRkimk7Ks3ougcOZhKMGQpMky0RufWoQZZMNFg4%2BJ3IQoed9Q0gzju2i7xmwoSJDCCRPHV43u3iziDXeHIabngNaCoUjRX7lMPUKzTVBtW3tCvTfVzz91Ui5V5KwMson3OOP%2FxZxqT76TkMEG%2FJX8x3gMP%2F409EGOqUBzr3W%2Fqwn3LsBHOOFmpQHUHSaoWT4KUBOJ8yicZ%2BUE6bv1nGF9QJWq0g2Z%2B5QvSZFBMFc7BYlIkOZqxWABMy8GbNLdzGw2lUMvY%2F5oPvPCaEXHmaXWzLL6itNx%2BEIwJWkx8bIJI5OCgi8Zf1X7o9zH24v7B5sguYWQ34mNf16r7eBnYEXKs7dXhOMRzFkRfKlcWuESrh3jHry3DN3L5KcvUHbba5O&X-Amz-Signature=e7652b8f8d13d27c8567de5b71bacbfa40a5c6508ed04ca7058f4ee4f9123124&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV4Z46DN%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T085755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBrChSKsrTtfqDBmEfi1gTEKzPQHWdjuJvMXPDGHv4BwIgQbe%2BgLh7mHANsANoFxGYAQ0CB8k7aO9mXbu4EzFSZXMqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHFoQ5hYQzKL29rbRCrcA3r0dfkblbl%2B8vOhOhbTWvErI%2Fhv%2FB0dqzj7ZhBKeTJBp8ElJIb61oYlVhQui4pI5L4%2BpWoOlAndmbR3wAM7q0aqZqqlQQrbK%2BIIK73uCSifT8M6xklmhRp7xSH7gpJD9rW8NQR75S6MVBv5MXAP1Z%2Fh7ByTZASdTc68vUgfE9PX4k39ept2Ut4x4t6E4LD0vdpfnMXQzSXxCrLL8hAV3%2BoL8pLZ7J1Bf0bzWVgSjDspS1uP%2F6LuArMbIpRgjAQXp7rNvB2v6Asj69m%2BCHLBFBVdL6DH7TAwS4nLBz4YE6I2uk28SPDZ6WYyaCgqH%2Fx2YqnB4w%2BlB4%2BnIyT6E75BWQEmLVwENNv3PUHVWCJmYGNbAruO98jZKN6g8SgZND2qnlldaQm%2FQ8WvEJv%2FSF0REL6qRUf9GXcRUYkd97bNdRnLthDB46JbTeQkgupL8fzeCh%2F3ZfqLv4j0z4Kh4HRewDS222YOlCdsNT9JpRkimk7Ks3ougcOZhKMGQpMky0RufWoQZZMNFg4%2BJ3IQoed9Q0gzju2i7xmwoSJDCCRPHV43u3iziDXeHIabngNaCoUjRX7lMPUKzTVBtW3tCvTfVzz91Ui5V5KwMson3OOP%2FxZxqT76TkMEG%2FJX8x3gMP%2F409EGOqUBzr3W%2Fqwn3LsBHOOFmpQHUHSaoWT4KUBOJ8yicZ%2BUE6bv1nGF9QJWq0g2Z%2B5QvSZFBMFc7BYlIkOZqxWABMy8GbNLdzGw2lUMvY%2F5oPvPCaEXHmaXWzLL6itNx%2BEIwJWkx8bIJI5OCgi8Zf1X7o9zH24v7B5sguYWQ34mNf16r7eBnYEXKs7dXhOMRzFkRfKlcWuESrh3jHry3DN3L5KcvUHbba5O&X-Amz-Signature=adac5f8df68b433d4a34257e845350a5913b3da379d236e0833ac2d4652ee27e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
