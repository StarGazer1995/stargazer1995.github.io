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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QFXU7RL%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T224621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQC7huEv4BlBqqQhsRq4RIzNtszhd1LVHapnIJRdoPuNiAIhAM5FVINhwSKzqROfTmVIHcnLt2OkiyBo4Kj%2Ff%2B8z57T0KogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnxlgFdPIool94AdAq3ANnw%2B4WkEmAXJkKgEK%2FhzMGeF6vk5Dnd75IDSFNHBHjcTh2Jw0Qug0T%2BLKqn5gauRT5IY0n92%2FNC81quO9fnBuCpmfHMGHz%2BucZ3l4wEsEgo5C2gQ2XXaf4gROIpYyfkSCz5wWgiMTPHAzJXvaK2JhzZTF7NAMeCTpbfPZsB9YuQ9KI8O%2BYst7%2B9%2FZ4WV9nHmOTGwVNKw1mhsx2WOyMrL4DGJbERo3bPqg9y5%2FElEa1ivKmu43hsDxbmlhQnrozwl3%2Fb%2FJeA0K6jdoTAIchyV%2BBX%2F4m52en46aZ2nMSyZ%2FccZJ9l3ButpgRCbZp8yXLxPxxBFkfBw56a2iksnVYo5hKNqSgOkizDAFpxAnC1pQ0FAzcoB90vzUpUDvo8bQPnA3GnRuQQz%2B19IJFMi9AKhkDwT8smAfJReHOUhmX7NALkd%2BMehXRBR8uKbAhAkcfilH%2Bi3DX%2F71Xt8tiLIj6KhJFW%2F9N8LWQ02VwY4tA98EueRsLACucyZZPa9axEIKAxcbvYdLsm5zTecZtD4ZsqRh6NnNKECpBpTSPBeIKcwlh9ciaZdG2IJPEH2DBKjShZdujDn%2FXgU7Jm3pS%2Fl%2FfnVwFuSeKUb6stqdxlmuG14x7t2H2TcG6p6pMxrO5PjDS3%2BzQBjqkATayPcWkiw6GLB9X5eA1KKI8HQQH9DnQAKwNtP2i5%2FieeMakLAjGanSZHKK0GNo68Lyo1gIinwy2UmfxEh%2BvYUGfhRdbRoJDGNKRUUlGuZmb8C4Zt9x2s%2BBcbFqG%2Bju0etOSXnQcsSdg7SJ6t9e%2Bkcy42SD14jHs8uV21QvEa2ooZ9BX%2FQbabDDks%2F50T9oCTul0y2cz5X4SBqUOAY1v%2BclVusmg&X-Amz-Signature=2b37641c56501b95f24c7aef81594ff67b186c2e9949ce992110fc25f2017c4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QFXU7RL%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T224621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQC7huEv4BlBqqQhsRq4RIzNtszhd1LVHapnIJRdoPuNiAIhAM5FVINhwSKzqROfTmVIHcnLt2OkiyBo4Kj%2Ff%2B8z57T0KogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxnxlgFdPIool94AdAq3ANnw%2B4WkEmAXJkKgEK%2FhzMGeF6vk5Dnd75IDSFNHBHjcTh2Jw0Qug0T%2BLKqn5gauRT5IY0n92%2FNC81quO9fnBuCpmfHMGHz%2BucZ3l4wEsEgo5C2gQ2XXaf4gROIpYyfkSCz5wWgiMTPHAzJXvaK2JhzZTF7NAMeCTpbfPZsB9YuQ9KI8O%2BYst7%2B9%2FZ4WV9nHmOTGwVNKw1mhsx2WOyMrL4DGJbERo3bPqg9y5%2FElEa1ivKmu43hsDxbmlhQnrozwl3%2Fb%2FJeA0K6jdoTAIchyV%2BBX%2F4m52en46aZ2nMSyZ%2FccZJ9l3ButpgRCbZp8yXLxPxxBFkfBw56a2iksnVYo5hKNqSgOkizDAFpxAnC1pQ0FAzcoB90vzUpUDvo8bQPnA3GnRuQQz%2B19IJFMi9AKhkDwT8smAfJReHOUhmX7NALkd%2BMehXRBR8uKbAhAkcfilH%2Bi3DX%2F71Xt8tiLIj6KhJFW%2F9N8LWQ02VwY4tA98EueRsLACucyZZPa9axEIKAxcbvYdLsm5zTecZtD4ZsqRh6NnNKECpBpTSPBeIKcwlh9ciaZdG2IJPEH2DBKjShZdujDn%2FXgU7Jm3pS%2Fl%2FfnVwFuSeKUb6stqdxlmuG14x7t2H2TcG6p6pMxrO5PjDS3%2BzQBjqkATayPcWkiw6GLB9X5eA1KKI8HQQH9DnQAKwNtP2i5%2FieeMakLAjGanSZHKK0GNo68Lyo1gIinwy2UmfxEh%2BvYUGfhRdbRoJDGNKRUUlGuZmb8C4Zt9x2s%2BBcbFqG%2Bju0etOSXnQcsSdg7SJ6t9e%2Bkcy42SD14jHs8uV21QvEa2ooZ9BX%2FQbabDDks%2F50T9oCTul0y2cz5X4SBqUOAY1v%2BclVusmg&X-Amz-Signature=d7fc04b6eae25095aed30f495a5656047851cf8acc6a42132948ee06b9ded17a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
