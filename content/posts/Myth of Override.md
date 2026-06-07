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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WXK2UQS%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T131705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE6Opo4vQi9T%2BxTFXar%2BegNSowTs9%2Bs7IgfDi8P0YXq2AiEA%2FmUVuvHcZBaIQv7HgWmJzUVHKVs5fvhftQsyYtpVLHoqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmVGJk2fQtHv6qqIyrcA3%2FZt24N6TSseGNBC6Y43466Eep9SEmVhH99TAmjTZ1dGGZn0xu1Y4dGdF3s4YtdlKlRJ8rqrxmU699O6t5hpU9KQbSCBhdQiH2fInQhzP34MUaTNmqhgqc2cpHTQC4pcPuEMZFtRwb6N2r%2FBbhUrW1s%2Fq4y3F5X1tYnrAuVNPoGKnRb1CB5WTKeyYFvwCxR7PueDGroJiyDuaCGrcbHQob5JkzuYWTyRRF5aOJ0VEfqY%2FI8bvLzNZ5BRMChC%2BGQgmr8R%2Bw1gnOkFCcUit2Eve82WeWq1SDzSaxUEWYn3U4Y40GqCRX%2FUlpPIh930oVq9hbqjYXgha5rgSDxVUgVP8S%2BtfBbIy0aSIUzBNj7TaeOktZUG6SX69xwbd37Y0Mx3bQDBs0zgm%2FSTHBSb4NhBuluXqCuvLxgmRb3%2B3rJv2Ph%2FXwV75Uth8h4ftO4wfKNn%2FFW%2BsN%2FuWUQphmnrFHWNQ4A6y%2BvDW0uc1L0p7c8wGU1PgL1DV8qzvmec43zUBS8d%2BP9jXv%2BXXzRHjGf2m80xi%2FF8adocHG3kp79QRl%2FDgtb6H7HXcIVkvz3eGuAL0fy3YVg9glRAHjd%2FwJUXA9r8QxMoj9LfMez1rtOFfsM%2FpG0FyBaD7jBpgb%2BA2gIMP%2BtldEGOqUB4vfZqwHZF7RdM7s7LymN3pBFkqvqjerz3CKwXauUgZCCCM1wW5auEk9M%2BJ3JvSRm9fG0QX2QjPm9gv1cqjB6mhNuwlLq6MvLBez8ri4ZWLVt%2FIiMUbfnj5CDzKolOYq65Pb6pFGd%2FiMYjFTW7MNJJNxuejK5A%2FYBzi2iZFpINx8ZmilqIa9%2BIk0VGVZ5UX1BS4%2FGgHp%2Bvt9BSUngFS03hI%2FzLUks&X-Amz-Signature=a38a00e364d96397b328c70665bd42729aae144fe34a19d35519bf7f36ecd939&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WXK2UQS%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T131705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE6Opo4vQi9T%2BxTFXar%2BegNSowTs9%2Bs7IgfDi8P0YXq2AiEA%2FmUVuvHcZBaIQv7HgWmJzUVHKVs5fvhftQsyYtpVLHoqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGmVGJk2fQtHv6qqIyrcA3%2FZt24N6TSseGNBC6Y43466Eep9SEmVhH99TAmjTZ1dGGZn0xu1Y4dGdF3s4YtdlKlRJ8rqrxmU699O6t5hpU9KQbSCBhdQiH2fInQhzP34MUaTNmqhgqc2cpHTQC4pcPuEMZFtRwb6N2r%2FBbhUrW1s%2Fq4y3F5X1tYnrAuVNPoGKnRb1CB5WTKeyYFvwCxR7PueDGroJiyDuaCGrcbHQob5JkzuYWTyRRF5aOJ0VEfqY%2FI8bvLzNZ5BRMChC%2BGQgmr8R%2Bw1gnOkFCcUit2Eve82WeWq1SDzSaxUEWYn3U4Y40GqCRX%2FUlpPIh930oVq9hbqjYXgha5rgSDxVUgVP8S%2BtfBbIy0aSIUzBNj7TaeOktZUG6SX69xwbd37Y0Mx3bQDBs0zgm%2FSTHBSb4NhBuluXqCuvLxgmRb3%2B3rJv2Ph%2FXwV75Uth8h4ftO4wfKNn%2FFW%2BsN%2FuWUQphmnrFHWNQ4A6y%2BvDW0uc1L0p7c8wGU1PgL1DV8qzvmec43zUBS8d%2BP9jXv%2BXXzRHjGf2m80xi%2FF8adocHG3kp79QRl%2FDgtb6H7HXcIVkvz3eGuAL0fy3YVg9glRAHjd%2FwJUXA9r8QxMoj9LfMez1rtOFfsM%2FpG0FyBaD7jBpgb%2BA2gIMP%2BtldEGOqUB4vfZqwHZF7RdM7s7LymN3pBFkqvqjerz3CKwXauUgZCCCM1wW5auEk9M%2BJ3JvSRm9fG0QX2QjPm9gv1cqjB6mhNuwlLq6MvLBez8ri4ZWLVt%2FIiMUbfnj5CDzKolOYq65Pb6pFGd%2FiMYjFTW7MNJJNxuejK5A%2FYBzi2iZFpINx8ZmilqIa9%2BIk0VGVZ5UX1BS4%2FGgHp%2Bvt9BSUngFS03hI%2FzLUks&X-Amz-Signature=02a89ee1df4a2f744a4e8ef946c174612f4780c190c1d80861d424ad2b34cdde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
