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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCOXTIYU%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T003319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQD3w8vy%2Fe1hf9j3UmORFMz4Q%2Biv8EDWaUmHkWGm2GXn4gIgFV87AURf3zTzoVnHqhaWExfWJa3NP3CMnYJKBbCE3pgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDmdvEVTZmGD0RM9wyrcA%2BPqIBi%2BgDYqbWb5ESl1sM2%2FZ7PHNmkRQZ8j%2BMkgwSAt4LNUZ25NyIM%2B4oyX0m9fVcIrfaAGWF59WNVt4TjGfZ6iV2nsgxqBbVlMHWvmOnfdQ8CZ3jz%2F9oCWqBvaS2sVjNm%2Bxbqu1kAHlSM6Gr8ccUh8YIZPo2Ux5hxSMQDJOeYrlcQOEDEDDMjgIh5hpufODRJa9ez8kYy4QL%2F%2BJk80NnS%2BFx804wVMehZsqwlj7oo%2Fu7Za9x7AYl5dVP7D0OIA518u%2BzOS1ElVjKWFGeTBVG2X%2FnGWTCH5zE%2BLv6tqUgojlghd9NtdJvO69%2FsyTb4KuZvj5BLqLPVKowcNREo5JSrPEQAHm5d1ba7%2Fy5hYcqvrjSqeDurl3cigGGSxWElS3EWw1CTpaGMhTyMGsRjTzIxRyKDJCHl92GJsxyc5OoQmCYpQjeUlb%2BN6d6q4BqE%2FGR6mhl7q0QoXyDFLMlvD8sPTr%2Fl1OB2KxCfUDQC5uQQOh%2FjghVACPxdpiwRA5rX92Ym7%2BwjxRUA0d0zWYuYFdkXqatE3QEaMPVxxd%2BcfmFjuNyzELAvEyK2%2BArLKGOuBGTh5B2Lm0464WlbaoWdW6PLZWtkad5KF0bXRd5tKmDwGW4rI7HXotsdG%2BRjoMJiQs9QGOqUBDFVHfngdlh8brSLQoo%2BUWtak4R03NVwhPC0gASCtyn0WtoVkT9GiSzec3osqMY4hH4Z%2FFNLysRpvx1wg86RAb8lISySvOamErW4fbBaoHHkwbUFvoilMBbH%2B0lk3enes60uGQRTDJv%2BSHaNmK5hpzp61lYpoWIZaqnTBqkoRcwoZBxBsdVfDXV7KU5CknqJbwEqF9g6h3ZzOrkE5xxGucK06vS2F&X-Amz-Signature=5965468afd94d9bd0b589450e446945804cd1fa3f00ae756120c29f0df017cf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCOXTIYU%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T003319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQD3w8vy%2Fe1hf9j3UmORFMz4Q%2Biv8EDWaUmHkWGm2GXn4gIgFV87AURf3zTzoVnHqhaWExfWJa3NP3CMnYJKBbCE3pgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDmdvEVTZmGD0RM9wyrcA%2BPqIBi%2BgDYqbWb5ESl1sM2%2FZ7PHNmkRQZ8j%2BMkgwSAt4LNUZ25NyIM%2B4oyX0m9fVcIrfaAGWF59WNVt4TjGfZ6iV2nsgxqBbVlMHWvmOnfdQ8CZ3jz%2F9oCWqBvaS2sVjNm%2Bxbqu1kAHlSM6Gr8ccUh8YIZPo2Ux5hxSMQDJOeYrlcQOEDEDDMjgIh5hpufODRJa9ez8kYy4QL%2F%2BJk80NnS%2BFx804wVMehZsqwlj7oo%2Fu7Za9x7AYl5dVP7D0OIA518u%2BzOS1ElVjKWFGeTBVG2X%2FnGWTCH5zE%2BLv6tqUgojlghd9NtdJvO69%2FsyTb4KuZvj5BLqLPVKowcNREo5JSrPEQAHm5d1ba7%2Fy5hYcqvrjSqeDurl3cigGGSxWElS3EWw1CTpaGMhTyMGsRjTzIxRyKDJCHl92GJsxyc5OoQmCYpQjeUlb%2BN6d6q4BqE%2FGR6mhl7q0QoXyDFLMlvD8sPTr%2Fl1OB2KxCfUDQC5uQQOh%2FjghVACPxdpiwRA5rX92Ym7%2BwjxRUA0d0zWYuYFdkXqatE3QEaMPVxxd%2BcfmFjuNyzELAvEyK2%2BArLKGOuBGTh5B2Lm0464WlbaoWdW6PLZWtkad5KF0bXRd5tKmDwGW4rI7HXotsdG%2BRjoMJiQs9QGOqUBDFVHfngdlh8brSLQoo%2BUWtak4R03NVwhPC0gASCtyn0WtoVkT9GiSzec3osqMY4hH4Z%2FFNLysRpvx1wg86RAb8lISySvOamErW4fbBaoHHkwbUFvoilMBbH%2B0lk3enes60uGQRTDJv%2BSHaNmK5hpzp61lYpoWIZaqnTBqkoRcwoZBxBsdVfDXV7KU5CknqJbwEqF9g6h3ZzOrkE5xxGucK06vS2F&X-Amz-Signature=9f2cb16b78646f58e541eccdab052f01db19aded1f6e2b93bbf318d78327c0a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
