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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVAMD6AI%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T020325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ4BQA4ffd%2F2Bsw8w0Vf4YLwNzs08AAq2IoUw7bVOqvAiA%2BDQBRFMrksZGzsTYd6F3i9%2FUM3wagyooOPXOX0xWDRyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM43SdxmIV4FsjWLCJKtwDTMH8B75RZ8F853OlQwz8tZqE0mZxMzJoEYF1eK7hQ7gwA1P5GAfoL0gYLNtqBXA6Nwn%2FEa9kmg9qhTRhSKdR%2FxH0jilewvBuldmH7wmXU6TcFycqX%2FcZVtIaBg6f0pb%2FAYgBdTz0zX6tumtE7jtFgsIPfAft2pK8Ui0YNlTcEIXIEMEx3jPOQRb%2FhDgDeayFnsA%2F6x%2BuwsCwMJK7hVB4XFOzMzJYIlL02vJcbmXvy4Pb5hhHGpQpwe42zFRxoW6GfMTDd2d2vtu94uDu3VBkeGe0SjpNQrkOUl%2Fh1ChdhhGAfxitM9eqtduOZG6E92Z4%2FtpgHyotMeRjkpFFFWPq5iU5ZQhJT4aa5M2ShkEq%2Fuy%2BBF%2FP2MQXFDJDZrvReFhSQYGAOvKN8pdDzthsjeGNYO4O2yghmQoqmZQ0kTyNJkB%2BqDbeHQTdQirHlMG%2FFaNZfN8HyKlTCe%2FyFsNPtCKSImtZiJrYgRKyVPn4vPv%2FkrlY1djd2Cbv0s6LvlqGX88YWqflOI5QJHIZKMLifd%2FQcZaj2NrOTjsDtEUYOV2TKdk6fgG%2FQzIGYKUf0%2FbQbn8yEJ8wmmR82vJ95NprGArfDchT96bLeIQJrY6k6b0FvFzV9kl7jJU4kzupccIw1OKp0AY6pgG5uKdcvfuUgRoC4%2BclNFjn2cqT7Uo0KtwFLOaelSQzdxkvgBuIWIyYxVvuorw6I2wgr%2BxEOMMCR%2BMZmyIsPk8bTjGGbJIqPFaYleaVISMKlcqcAiTaDCq7UFH21Uzqh8I4F6V8qsPA%2Bx2jzH7oqGjkUQbeStRmqW%2BW8ImDpe65ReOOQ3wpoCNSPNl8cQKn%2B9%2FsqQ10nvPZfAaPW5ivEHcYd8oBZsTQ&X-Amz-Signature=51df99c18854ab2517e702f3dee9156424d4b8f6d7fc376df4be2b9793702d73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVAMD6AI%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T020324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ4BQA4ffd%2F2Bsw8w0Vf4YLwNzs08AAq2IoUw7bVOqvAiA%2BDQBRFMrksZGzsTYd6F3i9%2FUM3wagyooOPXOX0xWDRyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM43SdxmIV4FsjWLCJKtwDTMH8B75RZ8F853OlQwz8tZqE0mZxMzJoEYF1eK7hQ7gwA1P5GAfoL0gYLNtqBXA6Nwn%2FEa9kmg9qhTRhSKdR%2FxH0jilewvBuldmH7wmXU6TcFycqX%2FcZVtIaBg6f0pb%2FAYgBdTz0zX6tumtE7jtFgsIPfAft2pK8Ui0YNlTcEIXIEMEx3jPOQRb%2FhDgDeayFnsA%2F6x%2BuwsCwMJK7hVB4XFOzMzJYIlL02vJcbmXvy4Pb5hhHGpQpwe42zFRxoW6GfMTDd2d2vtu94uDu3VBkeGe0SjpNQrkOUl%2Fh1ChdhhGAfxitM9eqtduOZG6E92Z4%2FtpgHyotMeRjkpFFFWPq5iU5ZQhJT4aa5M2ShkEq%2Fuy%2BBF%2FP2MQXFDJDZrvReFhSQYGAOvKN8pdDzthsjeGNYO4O2yghmQoqmZQ0kTyNJkB%2BqDbeHQTdQirHlMG%2FFaNZfN8HyKlTCe%2FyFsNPtCKSImtZiJrYgRKyVPn4vPv%2FkrlY1djd2Cbv0s6LvlqGX88YWqflOI5QJHIZKMLifd%2FQcZaj2NrOTjsDtEUYOV2TKdk6fgG%2FQzIGYKUf0%2FbQbn8yEJ8wmmR82vJ95NprGArfDchT96bLeIQJrY6k6b0FvFzV9kl7jJU4kzupccIw1OKp0AY6pgG5uKdcvfuUgRoC4%2BclNFjn2cqT7Uo0KtwFLOaelSQzdxkvgBuIWIyYxVvuorw6I2wgr%2BxEOMMCR%2BMZmyIsPk8bTjGGbJIqPFaYleaVISMKlcqcAiTaDCq7UFH21Uzqh8I4F6V8qsPA%2Bx2jzH7oqGjkUQbeStRmqW%2BW8ImDpe65ReOOQ3wpoCNSPNl8cQKn%2B9%2FsqQ10nvPZfAaPW5ivEHcYd8oBZsTQ&X-Amz-Signature=439c30f8ad0aa71d3afa81c561b89128f90b28c008fbb92632000f500168baa7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
