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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XX6E6TUA%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T073802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFfcxRFZnF8QzLTvJICVWDlteYoc0jiDrdh4zPzRsO7QIhAImfiack3i9tlIe390b1J0RaTS3m4lja4UweV8gLevZHKv8DCF4QABoMNjM3NDIzMTgzODA1IgzzrY16z0amrNW%2Fx6kq3ANx4OT65bTq%2FkeZ%2B5hDdzuqnHodWifl%2FJDVF7vOKpHAMfT5rXHsaf%2BAYDgRajcTFV%2FXuCKPYRgYpR8NqVwYVR2v%2Fp7n7JIOoXdJxT2AAzVNf2RdJJSCmNRhUiqTRjTRZuPZ7vjOwdgyxW16zoYnkrQGbgqzvdVgulEYYvYj6SW1RUA5rLC6XFTzpHeuDDopfg0OH0Sn3a4iQAFLoB%2BUeLnq%2B4dO9zETNFBMGs55XeYV6Sdk0sE82lvu50%2FGUmXCYs%2BWdTjSjyD0tWjfrNtyN32YnKi2GmMR63HXfbVIRvv8%2B36R2kHXDQBWa4wGw5MYuaBwA%2Fg98LGBVKlLgMepkcXJw%2B3D3o14JuF%2Bwm4COmF%2F9Xl6j5I1ygyja8N%2FPMwgivDxSsuFvXQzSRKjemkRfP%2BwF30PJnSY9ZmlIYj9%2B8rP%2F6%2BwKhJinleuT0ROi%2B2c3hsgHJeHqi5y5BFABU7m0CKF0mKLcxN%2BqKapIN2DY2agl%2Fq00aQ4Sw8ljdhvR8ODmnhaaN9oltXy7WFnwBQ3q4W8I5A5aR5V2pmBMtx9ivcZJRJqdjwNlBWM4jVMy4C8ggu%2Fd58oIhh0XTZYKhhtNQBeqhX68PjxG2%2BpTC4jrEM%2FSvWxE6GPXxR7QZ8qjTDruvLVBjqkAUyDLvHJwlaC0Qylw5shZ%2BO1shEOZJzt8QYBqbabjgGbhZglB3bSpQdbNPw35%2F8ziBMoyLiSXBWuEKTRGtmO%2B%2BL7CUtD2BgR9XeW%2B1s3PSKIr1gv3EzsmtrmySnoSz%2Fp7xdC28GgNQ3ldEpw%2Fd5RxY5AT63nEtnrBQ%2By1ZJShjhv5%2FGsbWhZppG6jliQTZKCv6ds26KvvEJUUWP7d6EZMrU1F86k&X-Amz-Signature=2b184348587c7c3e787c9a50268de0d210e52e7b0a6c66f4dad71673317063f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XX6E6TUA%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T073802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFfcxRFZnF8QzLTvJICVWDlteYoc0jiDrdh4zPzRsO7QIhAImfiack3i9tlIe390b1J0RaTS3m4lja4UweV8gLevZHKv8DCF4QABoMNjM3NDIzMTgzODA1IgzzrY16z0amrNW%2Fx6kq3ANx4OT65bTq%2FkeZ%2B5hDdzuqnHodWifl%2FJDVF7vOKpHAMfT5rXHsaf%2BAYDgRajcTFV%2FXuCKPYRgYpR8NqVwYVR2v%2Fp7n7JIOoXdJxT2AAzVNf2RdJJSCmNRhUiqTRjTRZuPZ7vjOwdgyxW16zoYnkrQGbgqzvdVgulEYYvYj6SW1RUA5rLC6XFTzpHeuDDopfg0OH0Sn3a4iQAFLoB%2BUeLnq%2B4dO9zETNFBMGs55XeYV6Sdk0sE82lvu50%2FGUmXCYs%2BWdTjSjyD0tWjfrNtyN32YnKi2GmMR63HXfbVIRvv8%2B36R2kHXDQBWa4wGw5MYuaBwA%2Fg98LGBVKlLgMepkcXJw%2B3D3o14JuF%2Bwm4COmF%2F9Xl6j5I1ygyja8N%2FPMwgivDxSsuFvXQzSRKjemkRfP%2BwF30PJnSY9ZmlIYj9%2B8rP%2F6%2BwKhJinleuT0ROi%2B2c3hsgHJeHqi5y5BFABU7m0CKF0mKLcxN%2BqKapIN2DY2agl%2Fq00aQ4Sw8ljdhvR8ODmnhaaN9oltXy7WFnwBQ3q4W8I5A5aR5V2pmBMtx9ivcZJRJqdjwNlBWM4jVMy4C8ggu%2Fd58oIhh0XTZYKhhtNQBeqhX68PjxG2%2BpTC4jrEM%2FSvWxE6GPXxR7QZ8qjTDruvLVBjqkAUyDLvHJwlaC0Qylw5shZ%2BO1shEOZJzt8QYBqbabjgGbhZglB3bSpQdbNPw35%2F8ziBMoyLiSXBWuEKTRGtmO%2B%2BL7CUtD2BgR9XeW%2B1s3PSKIr1gv3EzsmtrmySnoSz%2Fp7xdC28GgNQ3ldEpw%2Fd5RxY5AT63nEtnrBQ%2By1ZJShjhv5%2FGsbWhZppG6jliQTZKCv6ds26KvvEJUUWP7d6EZMrU1F86k&X-Amz-Signature=cf034afc8ba75fe655020bb37d7a4c678410e12e07628cbe33257cabf2331233&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
