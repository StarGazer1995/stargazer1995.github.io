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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQLZB53S%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T223006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQCzrV%2FjcM33c6ukB5Yoz1W3SSX8K1FO027qJyKkxbGN4AIhAN1HP0GezZEU4XVv0aRFP22OOFUMqVSDofsdDPKx2m7GKogECO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzG7doYOCz%2BKpcczH4q3ANdbhSfXfsPM7hFKzz2l6PZ0m2InfnKDUTyoU7iCL%2F31UUQU4yxLpIpfVfggBpn7Knk13ThIOmEYtMBjSuWwdo4vib3wOvRNooGSFHm%2BXyLUCaaVAir0qb1LO8fGURilaHBuU1dgkVTMckuMVB9UvbObdqHmV2RO5Po8kiGUsnxefY0Lj8chdUB8dQvjjPsx74Go9rLXsnd31qZixNVRp2w9D3FyySwaf1v9oEUp%2Fbl2LKTkD5ZctlyV44WRFswW8DGLkdPxBnl6DSUxvY48zgFBKBxeMl8xJPf1aTD4r5Plfibow9QLiSbavZyneclvL8mw70qHcnwkYKvA5JsSBsCN0Us99UNBBzzZnqY2nUSnJGLEdxOhW%2FqfuDO1al5mpVZTLiThBbHoTfkxSwazAYyCLDG5zEKVkSGM%2BUNx2AiqUQ9JDIGdeH%2B%2FUxop9h4Ff%2FDxXE5df%2Fuwua%2BDcHKLVAaTCWyhrtQxDPcAUltAy3ha6V8uTUVOtKU0k8XeC7bEE9DpBo6ZPVP6upoe4t2yZw7tR4TgLwlCkz%2BH2Y8EiLc9cO87w9RwmX3yzPIDeDcrqR4%2FRrbARy%2Bu0DlRU5IARBWVRAVwEjFhWUaH8DJ2daJjEeXps3A3V%2FZJHFxADC13fjTBjqkAZU2vdHEXlfbOLGVbdkXEv4CW4guV7fIk5QlXvNOusXpsyf3d28SxNGqo83uxG4x3vy8AD%2BDceiubU5Z2Nfktm78kw2a543BjJTeFg%2FRioJLC%2Ff0yjA29WprIR8ni%2FvqiqkBZFyHFBcEsvu3jz2cwDZDGkQHj6iCG44x0uoZf0EO%2F7UZ9wSIu3QggUNZv9o1cIiDLuBEpS1Bxdn%2FvqNcwvYf57oB&X-Amz-Signature=0ab81cf5501ce32e88d75d68898a6d3ac3781221e1d3e799da1c65a3281993d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQLZB53S%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T223006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQCzrV%2FjcM33c6ukB5Yoz1W3SSX8K1FO027qJyKkxbGN4AIhAN1HP0GezZEU4XVv0aRFP22OOFUMqVSDofsdDPKx2m7GKogECO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzG7doYOCz%2BKpcczH4q3ANdbhSfXfsPM7hFKzz2l6PZ0m2InfnKDUTyoU7iCL%2F31UUQU4yxLpIpfVfggBpn7Knk13ThIOmEYtMBjSuWwdo4vib3wOvRNooGSFHm%2BXyLUCaaVAir0qb1LO8fGURilaHBuU1dgkVTMckuMVB9UvbObdqHmV2RO5Po8kiGUsnxefY0Lj8chdUB8dQvjjPsx74Go9rLXsnd31qZixNVRp2w9D3FyySwaf1v9oEUp%2Fbl2LKTkD5ZctlyV44WRFswW8DGLkdPxBnl6DSUxvY48zgFBKBxeMl8xJPf1aTD4r5Plfibow9QLiSbavZyneclvL8mw70qHcnwkYKvA5JsSBsCN0Us99UNBBzzZnqY2nUSnJGLEdxOhW%2FqfuDO1al5mpVZTLiThBbHoTfkxSwazAYyCLDG5zEKVkSGM%2BUNx2AiqUQ9JDIGdeH%2B%2FUxop9h4Ff%2FDxXE5df%2Fuwua%2BDcHKLVAaTCWyhrtQxDPcAUltAy3ha6V8uTUVOtKU0k8XeC7bEE9DpBo6ZPVP6upoe4t2yZw7tR4TgLwlCkz%2BH2Y8EiLc9cO87w9RwmX3yzPIDeDcrqR4%2FRrbARy%2Bu0DlRU5IARBWVRAVwEjFhWUaH8DJ2daJjEeXps3A3V%2FZJHFxADC13fjTBjqkAZU2vdHEXlfbOLGVbdkXEv4CW4guV7fIk5QlXvNOusXpsyf3d28SxNGqo83uxG4x3vy8AD%2BDceiubU5Z2Nfktm78kw2a543BjJTeFg%2FRioJLC%2Ff0yjA29WprIR8ni%2FvqiqkBZFyHFBcEsvu3jz2cwDZDGkQHj6iCG44x0uoZf0EO%2F7UZ9wSIu3QggUNZv9o1cIiDLuBEpS1Bxdn%2FvqNcwvYf57oB&X-Amz-Signature=94e0c082990f37e836f7e5afe77ea23fd7e6c7c13d18db60282aa0eaf35b41c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
