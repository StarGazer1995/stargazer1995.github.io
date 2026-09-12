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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJVCJ743%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T015236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrqHkiHSsJfjE7nBWtoT34kU3n2S7CBnJDQiHBdhqmEwIhAOnQdt4Rm9cjsLX%2Bksr%2F5OCcnLo%2B9oyUzt3NzXagrb%2FwKogECKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFYUNOzunXlkvDRHsq3APtphXOFrwhEpqYYkBswjA2GDvbqh1tWI2pwYlk2yYoxvzl4HfE8ujZw9%2B63U1sDsIYVKBC9GEzVHXIveaM6UzeMgqoUO4rPV2yVMK9FNv8421tu%2FLG8WyCMdmFK5SxsYPda%2BCk25DG3tYWGRyJqtJa1nA0gK%2FBFxCeltpJCTIVTqg16xQ3sWZKQmwtxW46jA%2Fdd5nWGp8tUNr%2F0AA6VkRduuMHG3PgShrGYILNb9NzWkEkLCONBYiua6leiVnviqxc7eEOaKLbof5bOL%2B%2FZc4CSQlBu%2Fmwuv4%2ByVBRyw7s55ms9Py1K5nspiT%2B1PCwL7ZHuhQF%2BLHY9Lh2Uetc%2F0Osu82pplwEu8cotcJwwuj6wdvC28PleYUEwe2cfX0LvMoVydkPAfvS3%2BQvFVD%2F1eFvA%2FFV%2BvMxv5SGRQINB9O1iB61fktiC1V9VUNzlY0gd0nAkjxqocQ4Z0PhdfADbWtFFjNUP7K%2F3ORozwSceOWb6wkEBJ1KgtGt%2BgZlXlcfbLYSOv%2FJu7h50oS7EUfr69IUTqIjPrWMydReMSSoeXSKX8HYIr05AvKc%2B3yoo%2F0ZYBv9jcy8%2BfsL5GRuKY0mAbCgzz1TlQ4b4C4IRjrNFRGhM6gKbgJBrYd6Q9AJujDhrZLVBjqkAcoj2%2FyFr4Kq9d18poaJ0J6ZEF%2Fk7gua2iiOrQZ5FzL65BYSkfMSQDHXtr1%2FoE3j1egV5OVlNxYGE8npB7t7CfrHTCBp0EeR096hcr8CVDEy7P1UZT%2BzjP3eqUg1S39dJHBQXY84BMihgGkI2cGcSfriu6XCN4k3KhW%2FgK3l4%2BWSrwykbeOXodpW0O6FXsKKu%2Fop0wSkCLu31nA3tIl1gS8m4VQq&X-Amz-Signature=e0b0dfb2e0f8050e0f8f1a045c40773a9a62b0ecc92c7cecd69bf1fad2255922&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJVCJ743%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T015236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrqHkiHSsJfjE7nBWtoT34kU3n2S7CBnJDQiHBdhqmEwIhAOnQdt4Rm9cjsLX%2Bksr%2F5OCcnLo%2B9oyUzt3NzXagrb%2FwKogECKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFYUNOzunXlkvDRHsq3APtphXOFrwhEpqYYkBswjA2GDvbqh1tWI2pwYlk2yYoxvzl4HfE8ujZw9%2B63U1sDsIYVKBC9GEzVHXIveaM6UzeMgqoUO4rPV2yVMK9FNv8421tu%2FLG8WyCMdmFK5SxsYPda%2BCk25DG3tYWGRyJqtJa1nA0gK%2FBFxCeltpJCTIVTqg16xQ3sWZKQmwtxW46jA%2Fdd5nWGp8tUNr%2F0AA6VkRduuMHG3PgShrGYILNb9NzWkEkLCONBYiua6leiVnviqxc7eEOaKLbof5bOL%2B%2FZc4CSQlBu%2Fmwuv4%2ByVBRyw7s55ms9Py1K5nspiT%2B1PCwL7ZHuhQF%2BLHY9Lh2Uetc%2F0Osu82pplwEu8cotcJwwuj6wdvC28PleYUEwe2cfX0LvMoVydkPAfvS3%2BQvFVD%2F1eFvA%2FFV%2BvMxv5SGRQINB9O1iB61fktiC1V9VUNzlY0gd0nAkjxqocQ4Z0PhdfADbWtFFjNUP7K%2F3ORozwSceOWb6wkEBJ1KgtGt%2BgZlXlcfbLYSOv%2FJu7h50oS7EUfr69IUTqIjPrWMydReMSSoeXSKX8HYIr05AvKc%2B3yoo%2F0ZYBv9jcy8%2BfsL5GRuKY0mAbCgzz1TlQ4b4C4IRjrNFRGhM6gKbgJBrYd6Q9AJujDhrZLVBjqkAcoj2%2FyFr4Kq9d18poaJ0J6ZEF%2Fk7gua2iiOrQZ5FzL65BYSkfMSQDHXtr1%2FoE3j1egV5OVlNxYGE8npB7t7CfrHTCBp0EeR096hcr8CVDEy7P1UZT%2BzjP3eqUg1S39dJHBQXY84BMihgGkI2cGcSfriu6XCN4k3KhW%2FgK3l4%2BWSrwykbeOXodpW0O6FXsKKu%2Fop0wSkCLu31nA3tIl1gS8m4VQq&X-Amz-Signature=9d4eef2a981c4dc4eb05412b1ab54dc6f354bdabe6ad891178bfffe0889410bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
