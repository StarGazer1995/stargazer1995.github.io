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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YSDBNQH%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T135812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIHrKYX%2FPgsmO8Bml%2Bq1HF%2Fk5plTcnzfn%2Fq1koiblx99vAiEA1qNTVis0scVa1t%2FU%2BdFIZfchZcJy1xOiurGaEtQYCYkq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDLJrxr5FJeSst7NLxyrcA8adV4BET83Oox4ZF%2F9Ish2FbgvFIjcpr3qUWt7xS7rcMOE2u3t2N2BkuJq%2FO0e2UJal%2FBm%2BNCQGMdW4n8nO4pKQ00eA4kHrhXtOYPnnfcZx0omjewpZBKmmhNlztkdupu6Fo84XqWSovL3f58drUoQiARykUhKxHOieQzY80fk2%2FjqfZZhG1FER8oQei48ZBre%2Bp2VCqMaUXphw7jGtmeIzOdyw7XrYlS76Al4t9BNssaXicfb0dGuaYPUdrPigGrcFI8fOik55%2Fj8wrR6VwTxdk7F%2FKZ%2BpYOTjgW6M%2FbkAAadVvYAnRreGvHNwNCua7fKbngSIGGlloQip4caDY%2BGz%2BElYXvx0LZtie20ydJkIjzU8KUFdlEmXIY7rAKVu2rcHWM4kyKmjhCutdITKI55LbBsQ4Kml%2F%2B0A%2FLKsyear4WVIH6fC%2F5EWuR5kgh8NJO6Nx%2FVlSlteV4Md%2BRlfE%2FIebCQPvHK1dIR1ktI0bXHWJK%2FR0jD9jdCtPuO43jB3WUBqS6kNh46THqGzK2KmPr8iF0E2nys5Nwgbki07ACSw15W3BA8AmHtyDR5z1GvAz5C8aYWzkyTjCP2OWHazzWc4LTCRbgitE42cf9S%2Bewt546oIv8NYdKQRVcJHMOfUntIGOqUB3DcqKnwVsMUoYPy3UbCIkgBByA2u21YusD8mFV4fsBvk3pQOfKAvQ1pfvmVVRJL%2B5rirdmQK4%2Ffod%2FI4cHbiUdBdMPf1BZTr7iLBcDRcsetWKbMoW62xh%2BjIWeccvwmfTWOBQwsgzhazk2wIybggaeUPbcVePdWH6du0QFd7yjGi2kkFhH4iQmnwgs9th77tQDC6bg4xNix8SY3wgIPcNHAi86WP&X-Amz-Signature=23e5b599f9c09748d0f0f151a4ace07b8cf454eb14af4e1926420caa899ca359&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YSDBNQH%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T135812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIHrKYX%2FPgsmO8Bml%2Bq1HF%2Fk5plTcnzfn%2Fq1koiblx99vAiEA1qNTVis0scVa1t%2FU%2BdFIZfchZcJy1xOiurGaEtQYCYkq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDLJrxr5FJeSst7NLxyrcA8adV4BET83Oox4ZF%2F9Ish2FbgvFIjcpr3qUWt7xS7rcMOE2u3t2N2BkuJq%2FO0e2UJal%2FBm%2BNCQGMdW4n8nO4pKQ00eA4kHrhXtOYPnnfcZx0omjewpZBKmmhNlztkdupu6Fo84XqWSovL3f58drUoQiARykUhKxHOieQzY80fk2%2FjqfZZhG1FER8oQei48ZBre%2Bp2VCqMaUXphw7jGtmeIzOdyw7XrYlS76Al4t9BNssaXicfb0dGuaYPUdrPigGrcFI8fOik55%2Fj8wrR6VwTxdk7F%2FKZ%2BpYOTjgW6M%2FbkAAadVvYAnRreGvHNwNCua7fKbngSIGGlloQip4caDY%2BGz%2BElYXvx0LZtie20ydJkIjzU8KUFdlEmXIY7rAKVu2rcHWM4kyKmjhCutdITKI55LbBsQ4Kml%2F%2B0A%2FLKsyear4WVIH6fC%2F5EWuR5kgh8NJO6Nx%2FVlSlteV4Md%2BRlfE%2FIebCQPvHK1dIR1ktI0bXHWJK%2FR0jD9jdCtPuO43jB3WUBqS6kNh46THqGzK2KmPr8iF0E2nys5Nwgbki07ACSw15W3BA8AmHtyDR5z1GvAz5C8aYWzkyTjCP2OWHazzWc4LTCRbgitE42cf9S%2Bewt546oIv8NYdKQRVcJHMOfUntIGOqUB3DcqKnwVsMUoYPy3UbCIkgBByA2u21YusD8mFV4fsBvk3pQOfKAvQ1pfvmVVRJL%2B5rirdmQK4%2Ffod%2FI4cHbiUdBdMPf1BZTr7iLBcDRcsetWKbMoW62xh%2BjIWeccvwmfTWOBQwsgzhazk2wIybggaeUPbcVePdWH6du0QFd7yjGi2kkFhH4iQmnwgs9th77tQDC6bg4xNix8SY3wgIPcNHAi86WP&X-Amz-Signature=95e35daebb72113daf54319f301de6a40710444309f4511c7e35efc6f215b980&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
