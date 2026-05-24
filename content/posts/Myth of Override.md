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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z57YYKXE%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T083211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2FCD9Dizbg3qhOy16WxRkXMGs7hakRzutZkkFcNmC67AiBumZFmc%2BCQlBEpI%2Faz0thRWhO9l%2FZbf3eAoMW06KBdUir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTVP2BOn%2FmZhriiEXKtwDTxlCOnm9lDw4Sf3MmENZh%2Bm5BKPOvxqG5Vy20LtI0AYL5dTZ01WheMNadl8EIh%2FkuO5Baht8GuFrElTaIjWddOxB5GLzARvG16l6kL67rSYOt9ev3eTt0ZaMEkynK6FxxG%2B0hNJ%2FZs4FAzpmN64V4p2b1IYgMpYnfWsfgphjoDAcpK3PukFexA1GnZksu3APnZ8woYHhinGZlnIqXOJCAq6VqSQ2bQk53HPXoWFKPwEaYtZcR4DwDA9vvcoRhYmekg1XIDKJeQCDe75xD%2FR4lBUXPu9%2BplgaQBdpLQyZ1o1PPm2mp73FQFjjVV%2FAZYwkYTre%2B%2F8dFAHY%2BEfylKD3M940VtMYVHuiUxdRSN3rAHsKpz6MK0GaOrtkJBSSFwIBjIxCPIbZQDFgQZBqVuU6jfiEripRr%2FXiJVwIor0EUmSBVuYdSfGGDVg2M8W7s9eu%2BLFLxHOJkkCAYyCGc5nQrY6hOW1DvTJQ8%2BSD9Ki8ScGIg8B7HfsQvejYgygbEd7owUTLL0zKsZqGYpek5TTlGJ3WLZ3%2BXSbfxzmCvSeXgMPisS7axFyJc5PNF1TP14Wv9Y%2FePGAPyGkmhuSduH6%2FJXyBlWGA%2FPcnBkRWTxo4Usuv0CwH%2FLyPKwM2l14wieTK0AY6pgHxFWaS82CzSCjjaxrj%2BuHzzEn0YOCsKjj%2F6ZEZjPy7cp%2B72dcfmiOBYfP%2BZ4O8bAF9rXt69phgVawc8iUav8CjN8sZ%2BlKTGPQgoBeB06Dn%2BYzTljGOm6PiRcpE7zLADdI5KA4qjceMfpGt7HNSj7NhEFx8zvdHoJU7cQ6y56EuDMgk3zxqqkWk6RZq5dVZtWkgjccqhjGX8b4dpgdUz7SNEVHEGInX&X-Amz-Signature=03db58d6597db3a86347dac7ed1203e87c9beb1cd2b6d0ebbeb5c8496fcdfdd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z57YYKXE%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T083211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2FCD9Dizbg3qhOy16WxRkXMGs7hakRzutZkkFcNmC67AiBumZFmc%2BCQlBEpI%2Faz0thRWhO9l%2FZbf3eAoMW06KBdUir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMTVP2BOn%2FmZhriiEXKtwDTxlCOnm9lDw4Sf3MmENZh%2Bm5BKPOvxqG5Vy20LtI0AYL5dTZ01WheMNadl8EIh%2FkuO5Baht8GuFrElTaIjWddOxB5GLzARvG16l6kL67rSYOt9ev3eTt0ZaMEkynK6FxxG%2B0hNJ%2FZs4FAzpmN64V4p2b1IYgMpYnfWsfgphjoDAcpK3PukFexA1GnZksu3APnZ8woYHhinGZlnIqXOJCAq6VqSQ2bQk53HPXoWFKPwEaYtZcR4DwDA9vvcoRhYmekg1XIDKJeQCDe75xD%2FR4lBUXPu9%2BplgaQBdpLQyZ1o1PPm2mp73FQFjjVV%2FAZYwkYTre%2B%2F8dFAHY%2BEfylKD3M940VtMYVHuiUxdRSN3rAHsKpz6MK0GaOrtkJBSSFwIBjIxCPIbZQDFgQZBqVuU6jfiEripRr%2FXiJVwIor0EUmSBVuYdSfGGDVg2M8W7s9eu%2BLFLxHOJkkCAYyCGc5nQrY6hOW1DvTJQ8%2BSD9Ki8ScGIg8B7HfsQvejYgygbEd7owUTLL0zKsZqGYpek5TTlGJ3WLZ3%2BXSbfxzmCvSeXgMPisS7axFyJc5PNF1TP14Wv9Y%2FePGAPyGkmhuSduH6%2FJXyBlWGA%2FPcnBkRWTxo4Usuv0CwH%2FLyPKwM2l14wieTK0AY6pgHxFWaS82CzSCjjaxrj%2BuHzzEn0YOCsKjj%2F6ZEZjPy7cp%2B72dcfmiOBYfP%2BZ4O8bAF9rXt69phgVawc8iUav8CjN8sZ%2BlKTGPQgoBeB06Dn%2BYzTljGOm6PiRcpE7zLADdI5KA4qjceMfpGt7HNSj7NhEFx8zvdHoJU7cQ6y56EuDMgk3zxqqkWk6RZq5dVZtWkgjccqhjGX8b4dpgdUz7SNEVHEGInX&X-Amz-Signature=24a342b57b09f090b49c59713efe547294ed8aa472f7d4f1cfdaa26015337a6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
