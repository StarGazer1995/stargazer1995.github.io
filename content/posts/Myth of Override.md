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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644N5J4LF%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T224521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIA9Wo1UimtM8Sswi1qkYZp%2BqxQOpHLwjxQAmR8gIgO1dAiAGAhzCn%2BXB49wTHwwk%2Fk9czcrmfDj4KBCwokcXlCNJ%2BSr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMCe8W%2B8vEEUzuImnRKtwDCrKLwx2CHZo1fjjOdgFwnnb5bAQpQiauutuvRUnm8%2FcXxhdfb8tm1gHT3sztavcG45tIfkQUwUIb11AplghIkjQqmqgXn046qnEY7%2BrYpn1IMbIWpGhsdHqOTSzJeQR31BfYZ%2Bv4%2F8eh2Djscf%2FCNkuM6VWnM7uELsAnhpnM0tfN1342EXPX3Tjh70BGqRHtkba9%2FhU5N0qsIh8ZlPGQPFamVIITPcHlJEyLp4v%2FS5innskF7P7iEwFJsCx%2F5wk7HaFBfYTyhcX8Lo7xh47ZiKBFlgeQFvP0iQuboO%2FAF2jjxd%2FEP5NHvN4ECBT5sWj%2Bddti8c%2FcfED5X2%2BIpzsV9yLA6I%2Bw5SgyY40TZjYa%2BF539KDk1ZGML0NXfy0oJ5jDUnPec2%2FPOLlh%2F5kfBwE9PgpemEAdv%2Fgy2lj1oWYjeCOpKSp13o%2BoqpZEn0aItNXnKbxd0SYjKOTWTqAi%2FS%2Bx1gnrywOqNyYTrDZ6ut8lKABQrbFMH0e7vWqjYRA%2BHs1g8%2Fwamg1Dk%2FTDwJoiDuutomkSxM06TZoyWZFEKES6dVHC5qf6jluHjIsbONNRvcr5%2BjSxG0CDITl500bNIT18wYjeH%2BxwwIF97CX%2FQ7il5eEBhAtICLqz396oRNUwndLa0gY6pgHYY4YkSmg2VB7kS%2FknyZt8UPPBIZ%2F267znlKI6nh%2FYPhJG%2BlAgB1PV4%2Fv7X2fVWwjm4WMKNDfl9kMQcxMSMM1zt3%2BYrL3sLY5p2cztIw7IVW4SZVfkiXO5DlxkbW59DnPZEPAEkCge1y0uyeQLu7DL%2FsiWv3fvx4A1y0t8XGOqDc%2BpqJbWGnoafpKIsZUwGTNTDNajblKnTRj2EqjGJDKmJBcM4Dtg&X-Amz-Signature=9969ec6f66cc00a7f0ba74c0d92e647168201f71cc766cd7be0740391ad76131&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644N5J4LF%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T224521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIA9Wo1UimtM8Sswi1qkYZp%2BqxQOpHLwjxQAmR8gIgO1dAiAGAhzCn%2BXB49wTHwwk%2Fk9czcrmfDj4KBCwokcXlCNJ%2BSr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMCe8W%2B8vEEUzuImnRKtwDCrKLwx2CHZo1fjjOdgFwnnb5bAQpQiauutuvRUnm8%2FcXxhdfb8tm1gHT3sztavcG45tIfkQUwUIb11AplghIkjQqmqgXn046qnEY7%2BrYpn1IMbIWpGhsdHqOTSzJeQR31BfYZ%2Bv4%2F8eh2Djscf%2FCNkuM6VWnM7uELsAnhpnM0tfN1342EXPX3Tjh70BGqRHtkba9%2FhU5N0qsIh8ZlPGQPFamVIITPcHlJEyLp4v%2FS5innskF7P7iEwFJsCx%2F5wk7HaFBfYTyhcX8Lo7xh47ZiKBFlgeQFvP0iQuboO%2FAF2jjxd%2FEP5NHvN4ECBT5sWj%2Bddti8c%2FcfED5X2%2BIpzsV9yLA6I%2Bw5SgyY40TZjYa%2BF539KDk1ZGML0NXfy0oJ5jDUnPec2%2FPOLlh%2F5kfBwE9PgpemEAdv%2Fgy2lj1oWYjeCOpKSp13o%2BoqpZEn0aItNXnKbxd0SYjKOTWTqAi%2FS%2Bx1gnrywOqNyYTrDZ6ut8lKABQrbFMH0e7vWqjYRA%2BHs1g8%2Fwamg1Dk%2FTDwJoiDuutomkSxM06TZoyWZFEKES6dVHC5qf6jluHjIsbONNRvcr5%2BjSxG0CDITl500bNIT18wYjeH%2BxwwIF97CX%2FQ7il5eEBhAtICLqz396oRNUwndLa0gY6pgHYY4YkSmg2VB7kS%2FknyZt8UPPBIZ%2F267znlKI6nh%2FYPhJG%2BlAgB1PV4%2Fv7X2fVWwjm4WMKNDfl9kMQcxMSMM1zt3%2BYrL3sLY5p2cztIw7IVW4SZVfkiXO5DlxkbW59DnPZEPAEkCge1y0uyeQLu7DL%2FsiWv3fvx4A1y0t8XGOqDc%2BpqJbWGnoafpKIsZUwGTNTDNajblKnTRj2EqjGJDKmJBcM4Dtg&X-Amz-Signature=94f8845be098c976c2d2f0e823c6e3f8894290a4fd1cd8f8d1c835cda5607aa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
