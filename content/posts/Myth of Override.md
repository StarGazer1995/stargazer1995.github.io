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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT56WDF4%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T012105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID21RtgLXt4Ihae1NzWX1Uwa4uNv1fORp%2BOSrdkDwg78AiEAhsP%2BHNGO7fGo0OjA3kiSBKt%2BvaMpQqBKZZu5kQlirkIq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDPJlBKoQMfdDMn4zoyrcA79YACcNlaEfNEMCPGgNa5BZ%2FTFFDj%2Fw9qrKj8OA%2B9E2EGQYCFBTzcne7Z76%2B1bYigX1IC1l%2FbgRQcN1HS6bmtUW7r2rY5GVxloRqBSV3nVsvJ8xB0CEILoFbXdaqmxl4bv89tdl4Thzg%2BaOfh%2Ft5OyL8cjdHHN46yGfOTrZ5IzTRw4mPKZh1dNxc%2BM94fBwOBTZWJKlwnr4I2C1MLbBqJS%2FJMcglJ8t48UANghHQKZLTqABPrgUqiGZcIas3qKL6eeLkuJ7X%2FzTuvf8lT9j3DkBa3Fll6w8yXfIW1Ivlu1vcLP7JxigekLyoWcFvCavUibEFC9vEFcNmIimuDAe6ce6Y4N6SLD5kQWuyxw0yp7DVLD%2Bp%2Bub8skJAxHcO1C%2BuQzkFUrsbOczXHvgsXV1qZ7dhlcviHQXZrm416VCfBjsZWcs0%2FWbFY6FcIzFoaYqrTwmSvZsUMUZ%2B0avzWoZEtE9ISoabftCaSYk9LqBwRysLkjOJMvw99I1MuwpNCaHUIsDPxXhCy%2F4W07e9WJ3GV2PMaHLMcKXnbnj2wEcfw%2BwLNVbNVqhArov3TNVXrK4jLfTMw4%2BDKqhhNvtQZPFdaMW%2BEu%2B29Y%2BRAePd1QDRPcvKCKEBytf7qI4Mx%2BtMMjEn9MGOqUByB%2FsP9qmsMhJvd6ypkT%2Bald971kIjF%2Bf29cn%2BZFSlvFhFqWxWY2GSRNyF%2BIcHPFCWwxIxrTk1b1a5ICWF9q5xq8rVSIvtmDMaQvK9NYnJq4oXOTjfAXw6OtIN1nWS2ntVqNywT0wCQBcG%2Fky4FuAyPKviNtGqlSB%2Fsq8jE3m7NkDUaBEPxm68CHtYEy8bpwlUJppo8SEB8cRSGNb5C6yw%2BnS2emS&X-Amz-Signature=9f59c1341e6c1b7c9b5d1d511ecd695da354f9931d72a30d0bd3208dbad41c81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT56WDF4%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T012105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID21RtgLXt4Ihae1NzWX1Uwa4uNv1fORp%2BOSrdkDwg78AiEAhsP%2BHNGO7fGo0OjA3kiSBKt%2BvaMpQqBKZZu5kQlirkIq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDPJlBKoQMfdDMn4zoyrcA79YACcNlaEfNEMCPGgNa5BZ%2FTFFDj%2Fw9qrKj8OA%2B9E2EGQYCFBTzcne7Z76%2B1bYigX1IC1l%2FbgRQcN1HS6bmtUW7r2rY5GVxloRqBSV3nVsvJ8xB0CEILoFbXdaqmxl4bv89tdl4Thzg%2BaOfh%2Ft5OyL8cjdHHN46yGfOTrZ5IzTRw4mPKZh1dNxc%2BM94fBwOBTZWJKlwnr4I2C1MLbBqJS%2FJMcglJ8t48UANghHQKZLTqABPrgUqiGZcIas3qKL6eeLkuJ7X%2FzTuvf8lT9j3DkBa3Fll6w8yXfIW1Ivlu1vcLP7JxigekLyoWcFvCavUibEFC9vEFcNmIimuDAe6ce6Y4N6SLD5kQWuyxw0yp7DVLD%2Bp%2Bub8skJAxHcO1C%2BuQzkFUrsbOczXHvgsXV1qZ7dhlcviHQXZrm416VCfBjsZWcs0%2FWbFY6FcIzFoaYqrTwmSvZsUMUZ%2B0avzWoZEtE9ISoabftCaSYk9LqBwRysLkjOJMvw99I1MuwpNCaHUIsDPxXhCy%2F4W07e9WJ3GV2PMaHLMcKXnbnj2wEcfw%2BwLNVbNVqhArov3TNVXrK4jLfTMw4%2BDKqhhNvtQZPFdaMW%2BEu%2B29Y%2BRAePd1QDRPcvKCKEBytf7qI4Mx%2BtMMjEn9MGOqUByB%2FsP9qmsMhJvd6ypkT%2Bald971kIjF%2Bf29cn%2BZFSlvFhFqWxWY2GSRNyF%2BIcHPFCWwxIxrTk1b1a5ICWF9q5xq8rVSIvtmDMaQvK9NYnJq4oXOTjfAXw6OtIN1nWS2ntVqNywT0wCQBcG%2Fky4FuAyPKviNtGqlSB%2Fsq8jE3m7NkDUaBEPxm68CHtYEy8bpwlUJppo8SEB8cRSGNb5C6yw%2BnS2emS&X-Amz-Signature=58c5e12550d9d2d60a73004cc2dd84edfa37a0a8e0c8a99b0dc7d583e7635bb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
