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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WVC6B5O%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T144951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUJI1zStBJnMPm06mW%2FVF%2BbEwttYvarzOuWdhY1chKhAiAfp361OXgs180kxww41tdU8wM%2FbmWWgJ7EK0LiuVs%2FJCqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFrxwXgrWyG5kCw7jKtwDEy7P%2BZKzPav5j%2FrouXcm0snOhc0khoGPQbMRrN20pAPZaCYZQ3seaM1hpArONoZx8ASdHqKt51x4DG3FupfrO3ECd%2BI5FSEcj9c73ai3FDaooHMDZRC04TmAZqZIDjPkoyh4b7xt5Oebk5Zpl%2FzWMR48QOZa92qSaRa%2FL549pA7lxRbos%2FBrj70QK67kLIZv3F6UsyKMjd%2Bh%2B9c%2FTT9Zky0NhE3m%2Fue5bfeUaEfmKYb7TTYmNso5qm66EqGQU9Ka%2BZtt9UaRAEzGN8mUAY2nQcJgJkUNoUYDh2zUPghPSqRRtHC56i0lIGgdX8D6Y3iJRrr06Qa8JhZPjWmtprpU%2BiH4%2BJx%2BaWW%2F30H9357DEpG6FrlJq7bY2pJ7YadDX%2FqRrQH5W6bojn%2F1ODhpF4S0OqjVEQsZjGmsriDgU98CKhoN1EkX4fsiMRKA7AeGHlQkrT3EjbqnBfZ2ofY1H8ENPKvgnBUPvVG4Opl9P9Qc5tddgk%2F3X0rXCWYikEWfpzPXWFsoMF1Y7m%2Bn6tSah8F87iXfj%2FC1qs1rHHK7XOZoOgoKp3SkDMSXO8GiDmhCdSlHFQXR829lNdTGpAqs8pWxXphgQIvKDsQsZG36eRCRuxWk6t7CVDzrPIkeyoYwxLbn0wY6pgFaiBMt8FgCdlea74qkYBoQNYE5%2B2VN%2BUpagJ%2BFVj9uRroKw3ce19QXsBCBksZzqIT0pCzdVRizoP08T6lxhdfqBdyqFiDTCzcyA%2B3fvNzmo%2F4Iys74TIQN2e11FdQKIBIMnJPw5OW%2FZd9NYNjfaq0ti6AeUeyjjE%2FmEdbeJhdqpldUzQ1ifEiD07jeYT7MtzIVgndS%2FYxMHQK6q8IXRu0cpZBx3TBy&X-Amz-Signature=352cb8ba29a0e525a8cd6d5fd9fe2cd40d506ee7b1ea38ed135bccbf91c5ccce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WVC6B5O%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T144951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUJI1zStBJnMPm06mW%2FVF%2BbEwttYvarzOuWdhY1chKhAiAfp361OXgs180kxww41tdU8wM%2FbmWWgJ7EK0LiuVs%2FJCqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFrxwXgrWyG5kCw7jKtwDEy7P%2BZKzPav5j%2FrouXcm0snOhc0khoGPQbMRrN20pAPZaCYZQ3seaM1hpArONoZx8ASdHqKt51x4DG3FupfrO3ECd%2BI5FSEcj9c73ai3FDaooHMDZRC04TmAZqZIDjPkoyh4b7xt5Oebk5Zpl%2FzWMR48QOZa92qSaRa%2FL549pA7lxRbos%2FBrj70QK67kLIZv3F6UsyKMjd%2Bh%2B9c%2FTT9Zky0NhE3m%2Fue5bfeUaEfmKYb7TTYmNso5qm66EqGQU9Ka%2BZtt9UaRAEzGN8mUAY2nQcJgJkUNoUYDh2zUPghPSqRRtHC56i0lIGgdX8D6Y3iJRrr06Qa8JhZPjWmtprpU%2BiH4%2BJx%2BaWW%2F30H9357DEpG6FrlJq7bY2pJ7YadDX%2FqRrQH5W6bojn%2F1ODhpF4S0OqjVEQsZjGmsriDgU98CKhoN1EkX4fsiMRKA7AeGHlQkrT3EjbqnBfZ2ofY1H8ENPKvgnBUPvVG4Opl9P9Qc5tddgk%2F3X0rXCWYikEWfpzPXWFsoMF1Y7m%2Bn6tSah8F87iXfj%2FC1qs1rHHK7XOZoOgoKp3SkDMSXO8GiDmhCdSlHFQXR829lNdTGpAqs8pWxXphgQIvKDsQsZG36eRCRuxWk6t7CVDzrPIkeyoYwxLbn0wY6pgFaiBMt8FgCdlea74qkYBoQNYE5%2B2VN%2BUpagJ%2BFVj9uRroKw3ce19QXsBCBksZzqIT0pCzdVRizoP08T6lxhdfqBdyqFiDTCzcyA%2B3fvNzmo%2F4Iys74TIQN2e11FdQKIBIMnJPw5OW%2FZd9NYNjfaq0ti6AeUeyjjE%2FmEdbeJhdqpldUzQ1ifEiD07jeYT7MtzIVgndS%2FYxMHQK6q8IXRu0cpZBx3TBy&X-Amz-Signature=3913ae7eaec0b6c79d5e631371c7afa269d73e72e0afbb8e4977824b8debe433&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
