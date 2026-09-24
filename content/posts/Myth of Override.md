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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ORBGQLP%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T015515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIEilCGSxaRp%2FTwdNwI1qq2LZrvHcG7gVnua03rnhfF4EAiEA3NubtPp3Lu2YixlBU9LJse0az6G3d5B8ITYF%2B01IG3MqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH84OgtlqdSmaf3eNSrcA4K5JP2KmXYzMXSx5yzL%2FgVdOUz3Lyox81s0EzEEw4uRSOrBqCiwMI8mvu4pRn8ixbjGLNA%2BLn5q%2BhaVgm%2FC05Wc%2BdsQSAU6SAcdUzYDqXoeMwR75%2B%2B%2BBoOvKrOBusdDcb2Hl9WrJGvdL0F8Z%2FE2PdwlYvAyFh60OaHKRSKW45Xm6fuX1uB2Bzm4yjaO7JvSl5uPiAabUE7GyBY20ydbuxXhwM9U%2FoWMlqzjF%2FkUcDE5%2B5KSyAAwQwd3YrjqbFvPuNMEkTqpONro3KG%2F2sWkptyLkLPrQNFYhhV30H0IGNMoAX7ezIBKOTp9M8K1LgiUsM7UH81hNTO7nZ8E2WNIuPuYIjJd8Nx4JEUBnDkiuSCs3RrMZM32EPaquD5Wc%2FElNoKE1gRqTldC3Bbnkr2%2FeNNgXSSubxEMlmCq44eChopRC72IAYsyezLUwNsiPtLTzlyI3uNTHs0LbxPGBqA1Uk7MSy%2FOnMKzmThJO98rnsCqzTeajI4ZhABZ%2B3tr6UMS6sXHI46L%2BCDGxLEXR2PuqNw0Q9b%2FBH6v4EzJOxOkbrUwWg5oV6IlPvG%2F5QAWAleydHcti7ClVPSG4C2TFkPyOM79wJmsb6yVHl4oC2Lj7GbSdyprOCfZsM4r0Yy2MNHt0dUGOqUBXMFx%2B8LR6F03js8stDnw%2Bf02lrXpG8NiywcwV7cniR9Y4X8L6yIwhAp5w9sueNe4UJSPxOarM4yqGYTh7D%2BZJhnxHHk4Qa3XYQEg7d8my%2FgMeIFYDtcPQgUfNmqHsKK%2BuE3lUjNybrBho4leevFM%2FVTYd8FkIrc90fKJuJl7N1qzVCAq5lUYuRQ1FkvhNDS%2FdfxeUiDayJFi%2BdKUpKJZdOygg600&X-Amz-Signature=4a98ca73ced6312dffb17dad647b31744ec8d7157c1497b235e06cff28e6db10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ORBGQLP%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T015515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIEilCGSxaRp%2FTwdNwI1qq2LZrvHcG7gVnua03rnhfF4EAiEA3NubtPp3Lu2YixlBU9LJse0az6G3d5B8ITYF%2B01IG3MqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH84OgtlqdSmaf3eNSrcA4K5JP2KmXYzMXSx5yzL%2FgVdOUz3Lyox81s0EzEEw4uRSOrBqCiwMI8mvu4pRn8ixbjGLNA%2BLn5q%2BhaVgm%2FC05Wc%2BdsQSAU6SAcdUzYDqXoeMwR75%2B%2B%2BBoOvKrOBusdDcb2Hl9WrJGvdL0F8Z%2FE2PdwlYvAyFh60OaHKRSKW45Xm6fuX1uB2Bzm4yjaO7JvSl5uPiAabUE7GyBY20ydbuxXhwM9U%2FoWMlqzjF%2FkUcDE5%2B5KSyAAwQwd3YrjqbFvPuNMEkTqpONro3KG%2F2sWkptyLkLPrQNFYhhV30H0IGNMoAX7ezIBKOTp9M8K1LgiUsM7UH81hNTO7nZ8E2WNIuPuYIjJd8Nx4JEUBnDkiuSCs3RrMZM32EPaquD5Wc%2FElNoKE1gRqTldC3Bbnkr2%2FeNNgXSSubxEMlmCq44eChopRC72IAYsyezLUwNsiPtLTzlyI3uNTHs0LbxPGBqA1Uk7MSy%2FOnMKzmThJO98rnsCqzTeajI4ZhABZ%2B3tr6UMS6sXHI46L%2BCDGxLEXR2PuqNw0Q9b%2FBH6v4EzJOxOkbrUwWg5oV6IlPvG%2F5QAWAleydHcti7ClVPSG4C2TFkPyOM79wJmsb6yVHl4oC2Lj7GbSdyprOCfZsM4r0Yy2MNHt0dUGOqUBXMFx%2B8LR6F03js8stDnw%2Bf02lrXpG8NiywcwV7cniR9Y4X8L6yIwhAp5w9sueNe4UJSPxOarM4yqGYTh7D%2BZJhnxHHk4Qa3XYQEg7d8my%2FgMeIFYDtcPQgUfNmqHsKK%2BuE3lUjNybrBho4leevFM%2FVTYd8FkIrc90fKJuJl7N1qzVCAq5lUYuRQ1FkvhNDS%2FdfxeUiDayJFi%2BdKUpKJZdOygg600&X-Amz-Signature=323c5201cc61099abadc63e99a29a55e1090d7d14ce65924a954da7a13d0dfc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
