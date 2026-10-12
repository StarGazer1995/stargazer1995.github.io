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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636C46YSV%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T192914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDnal1r5tKQNVwgW%2BEEjNu1x1pC6epOZUjhjHVuJrMKgIgGKlQ5ZK6L%2F4r2rwCKBKoCDcS9hPI0NTEI9%2BYEq6ZfPIqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzVoE6ShKkhNovJCSrcA0bUpfNJjOxFBo%2BVvw03Xw5LloS%2BAVPDBbAam17FBL7hpm8JBqeXePKtCKH3yw1TwJYIGCpAJt3xdEZ4uFX5Qa7Mdi%2BVgx4D0d%2FMPy1WKbHfxPomOgAv4bnDJ3riRY7uBF174MsuUm1AK7Xedym2URbRwb4xadvr%2B9FqmshdcDOA9Oi05sN03vxJHLUXGa3K1JkhC7qMbFGanjcFZ3OIcpTs6iiCx3QFeQy1sgHY0OxUsaHYrUCZZi59vs26DSXjDhFKHp6XTCC%2BeZD%2FKfcHKKIspOs9aviat1RD0bkIHi4jZrWhedAsVpRUIp%2F0QxMyfidbFmxCzg4uBFc1q2zjrU4KWQ0Az3czFDrYVQcB9Q6rw2iDvwmpVDDMNcHnXlQ54b%2FcuX655U4oZQD1F56dDK5RPCZv7%2B3D4eLCUVQxElhRxgPiMzfdrhV7b%2FD%2FP723gcYq%2FnaBJPobHjiQ94dMwTtpZ3gQhLTqi5VPzsuRX4t7trbL1pUcAYZQCAiF8qAZ1B%2BHZRzkdJ4wgldwsQ00rKSiebaIau5GSF3aUknjAD1acR6X12exkfCQhn%2BTkOfqnChoKstw7tmnlnu4nZ4UnXf5fU6Y5szYEVzKf1ipZ3SVqdRh4smzs%2FUH%2FkEnMIrTtNYGOqUB3viGM%2BOuIXKmAKRiklYKgPjOMJGZ47Ov2s1mu7O5ngVt3sv1o8hCYGgU84HlSojelx8FWvwZFeAxAhcyDrgItGQQ3Lc%2Fn5KRPaJ3YbD48NvwVoW4tMvKjNB1TptbTrEQPehn1DOLnjxErKKP%2F7Q3TROgHOI4Bo7tudddB8S%2F6qdGQ%2Bklpe%2BFO5qHoEtZrbF6JYz5c9Xko5QlQ6LHioYGqaX%2FannX&X-Amz-Signature=35f616127bd66adcc56e2c2a751ab5863ed666a5da3cb72a066456440bd6ab4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636C46YSV%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T192914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDnal1r5tKQNVwgW%2BEEjNu1x1pC6epOZUjhjHVuJrMKgIgGKlQ5ZK6L%2F4r2rwCKBKoCDcS9hPI0NTEI9%2BYEq6ZfPIqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzVoE6ShKkhNovJCSrcA0bUpfNJjOxFBo%2BVvw03Xw5LloS%2BAVPDBbAam17FBL7hpm8JBqeXePKtCKH3yw1TwJYIGCpAJt3xdEZ4uFX5Qa7Mdi%2BVgx4D0d%2FMPy1WKbHfxPomOgAv4bnDJ3riRY7uBF174MsuUm1AK7Xedym2URbRwb4xadvr%2B9FqmshdcDOA9Oi05sN03vxJHLUXGa3K1JkhC7qMbFGanjcFZ3OIcpTs6iiCx3QFeQy1sgHY0OxUsaHYrUCZZi59vs26DSXjDhFKHp6XTCC%2BeZD%2FKfcHKKIspOs9aviat1RD0bkIHi4jZrWhedAsVpRUIp%2F0QxMyfidbFmxCzg4uBFc1q2zjrU4KWQ0Az3czFDrYVQcB9Q6rw2iDvwmpVDDMNcHnXlQ54b%2FcuX655U4oZQD1F56dDK5RPCZv7%2B3D4eLCUVQxElhRxgPiMzfdrhV7b%2FD%2FP723gcYq%2FnaBJPobHjiQ94dMwTtpZ3gQhLTqi5VPzsuRX4t7trbL1pUcAYZQCAiF8qAZ1B%2BHZRzkdJ4wgldwsQ00rKSiebaIau5GSF3aUknjAD1acR6X12exkfCQhn%2BTkOfqnChoKstw7tmnlnu4nZ4UnXf5fU6Y5szYEVzKf1ipZ3SVqdRh4smzs%2FUH%2FkEnMIrTtNYGOqUB3viGM%2BOuIXKmAKRiklYKgPjOMJGZ47Ov2s1mu7O5ngVt3sv1o8hCYGgU84HlSojelx8FWvwZFeAxAhcyDrgItGQQ3Lc%2Fn5KRPaJ3YbD48NvwVoW4tMvKjNB1TptbTrEQPehn1DOLnjxErKKP%2F7Q3TROgHOI4Bo7tudddB8S%2F6qdGQ%2Bklpe%2BFO5qHoEtZrbF6JYz5c9Xko5QlQ6LHioYGqaX%2FannX&X-Amz-Signature=6bb77de7df015696eea32a03d0df402e398eba0e5c7d987e4faa3b1dc315c435&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
