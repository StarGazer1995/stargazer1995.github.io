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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636TFIROO%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T032405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFe6wLalnLMg3F7wdHVoPkNELEz%2B6g5tU7SUqMmp60WTAiBXc6YLXBPk9Q59vfqMHC8dp0yJe5dwR4rMpUsRItpFlCr%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMJPZnbzKIHGqIlk7QKtwDgGtkVXjQ45loZLRM4uZ%2FD1oDbX%2B%2FCjWZIY9hlVgVzX%2FhM51CqT3rpKg4SUFBwKivaHpgfpp2%2BH5CmkJfFHCC5y286Ykk%2FGDCAj5yRsO0m0c4RZg0pwP6xgIMS%2FgttLxd05t26U6aphbV3l4f8D3sRWmklpkz0Sy5UqHJhdvUncOcAqm0fbeay%2FvuZxZQSzE%2BdfG6g05DwtETOm3QHJYTjXVzoiw6if8GSyY6FqzpoviaGEvcjoKEkMJtbKjtNX6xTBIoth7iafdHj91nUbiOeNPgKE3bIWDXi4p3MZC3iqKUKzEBkIVEAAzwWxnJ2bmf42ejhzJ0Px%2FRUccNcXqNIP0YkcGDZ9Q0XvveOKo0M4ALwhI1ukuWC72s2fhoevodnBUdpZKtt3JNrauDapFy2%2FejqkyQAz0yJseNfl28AngHj8MZVyzyqCxkd%2FHfuLF1yFPCYeCHQLSTLtq5HLgu%2FZ%2BAsjzdAvkz78aGqWt1uaWNxgzUleuKYwfx3Is8%2BzaNdIAQhSWgO8DPnPG0JfagWTYhoJOJqdRri1yiIJv7qHFnhIrVZ9p%2BQILgj8tpU1F6eTAl4uwTnY4QcACVgjtYwMj5pYiDya9mT7Gm8eHyRD8h340JAHkYdp38b8YwkNTe0wY6pgHmVDArwT7YQ1sklKD7S8L2n%2BTOuGkt%2FQLDKBL2opkV0lef9u4LCaBWmIqkIL2jMLK4tfDOLN5Cj2bPFgFVDpiQp%2FM%2BkUMcm%2BpmmuJtUNGx%2Btdo3ccD8vhFN4%2Fh7flH9dWf5IyZ3gqMvZUs4m9BwShJ7LhgPdUbmnINoX1lU%2BSyOkY3%2BVCrCVO5xPcufxk%2BcW2WurpscTw8DrM1uibmo2SwbbtpFI4L&X-Amz-Signature=1ab0b0576200277144c8cd1f148fa39b036202661931ec21a10d2f99e945d3c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636TFIROO%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T032405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFe6wLalnLMg3F7wdHVoPkNELEz%2B6g5tU7SUqMmp60WTAiBXc6YLXBPk9Q59vfqMHC8dp0yJe5dwR4rMpUsRItpFlCr%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMJPZnbzKIHGqIlk7QKtwDgGtkVXjQ45loZLRM4uZ%2FD1oDbX%2B%2FCjWZIY9hlVgVzX%2FhM51CqT3rpKg4SUFBwKivaHpgfpp2%2BH5CmkJfFHCC5y286Ykk%2FGDCAj5yRsO0m0c4RZg0pwP6xgIMS%2FgttLxd05t26U6aphbV3l4f8D3sRWmklpkz0Sy5UqHJhdvUncOcAqm0fbeay%2FvuZxZQSzE%2BdfG6g05DwtETOm3QHJYTjXVzoiw6if8GSyY6FqzpoviaGEvcjoKEkMJtbKjtNX6xTBIoth7iafdHj91nUbiOeNPgKE3bIWDXi4p3MZC3iqKUKzEBkIVEAAzwWxnJ2bmf42ejhzJ0Px%2FRUccNcXqNIP0YkcGDZ9Q0XvveOKo0M4ALwhI1ukuWC72s2fhoevodnBUdpZKtt3JNrauDapFy2%2FejqkyQAz0yJseNfl28AngHj8MZVyzyqCxkd%2FHfuLF1yFPCYeCHQLSTLtq5HLgu%2FZ%2BAsjzdAvkz78aGqWt1uaWNxgzUleuKYwfx3Is8%2BzaNdIAQhSWgO8DPnPG0JfagWTYhoJOJqdRri1yiIJv7qHFnhIrVZ9p%2BQILgj8tpU1F6eTAl4uwTnY4QcACVgjtYwMj5pYiDya9mT7Gm8eHyRD8h340JAHkYdp38b8YwkNTe0wY6pgHmVDArwT7YQ1sklKD7S8L2n%2BTOuGkt%2FQLDKBL2opkV0lef9u4LCaBWmIqkIL2jMLK4tfDOLN5Cj2bPFgFVDpiQp%2FM%2BkUMcm%2BpmmuJtUNGx%2Btdo3ccD8vhFN4%2Fh7flH9dWf5IyZ3gqMvZUs4m9BwShJ7LhgPdUbmnINoX1lU%2BSyOkY3%2BVCrCVO5xPcufxk%2BcW2WurpscTw8DrM1uibmo2SwbbtpFI4L&X-Amz-Signature=24bf2d6a97b8157ce7fc227166b2511e0ee73bb241381e9509ec20233faa5576&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
