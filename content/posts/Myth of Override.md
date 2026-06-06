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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMB2ZGIG%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T082246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWZmpKNkNXg%2BikRq7zN%2Blbr%2BZo0IWT5zGXX7BYA3LYRAIgXjZn4ZY0LR8KBMkEwSXqfz9WoYF6BjZC02X%2FaUqkXK0qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFDfD6OWevwR58krSrcA9f5eeik2qhK%2FwsbdqX4%2BU4QA8S6IMl4HkSvZYRpQyyi1n0GxGtY%2F%2FQtdPXInUZZEvIIRx%2Bln%2FqW7OXoziKUNJhvDUThtem8MpqPi%2Fj1aUmGDIONe66YLdK9VpBXDtMPDo4ikk9Hby0gWzjcpmB0pWqkzO9JHMod7YRUk2ATN6ZXYjLQU%2FEbAJc2Pe3jVD5pGyYxXI26VUJf6BAtHievnWkFfHf2TpGSxdqh82AH0Ih0OSKZXJCBs8Dwk9j8QjnBh5%2FO6zCKU3r5bogNAqv8qbM4r%2FegMsS0talAhobY3C3WPRpi8QgQiq9rybaMfF91AR7oWYYrawsgCVLs9fUqjgqS9avq8yZ8%2BkGu6Id7jBbTor%2Ffafh2dfTWLNDaK8L%2BlMfFMjpufYn6cFoKM8OnO%2BUnzD7SpmpEbsFxoXyeUj2GkENVA697e5wGQ5EjqAZyIcvxg%2FjXpx3Ph1SsUlFMc7hE7rtRGbxXa7h8VHCYBIdS7RiNTzbJjpoBxBrXmlPWqllyHrkSNfyXqz8xaqOjdjD6f%2Fd4iIs63DHluE8yooauhrdBlA65lahL6rC6ejiO82wOaUMqbJV4vme2GQVlfWSY1W3MngBLSmMD0h31Hi%2FndFbvDxtdHppPmgUEMPOsj9EGOqUBe9O%2BHOdGtJZ6GWwsSeJBc7f8oXh1Di1Oi%2BFIVb1dhNzJCeHVMfaq7ke4w6Pkp6VAOq6uyv5A7KLPdTxusd2173d6lxmVqNtbD%2F%2BCLtKQ%2BN00uBA9%2B2idKzT9WK7J%2BkzkzL8ZDTwGJeKBGPP4bqbXyMJdUJRLNMMjSU%2BneKl92QqCNo3zVA%2FGv1Mb%2F8I0val2%2FZSAcILcR1Mmf%2FMxT1pu3%2FOHPrPx&X-Amz-Signature=05b238e156e1d532c43c5a325429174a8924f783857bc0b17b0885d5048ca406&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMB2ZGIG%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T082246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWZmpKNkNXg%2BikRq7zN%2Blbr%2BZo0IWT5zGXX7BYA3LYRAIgXjZn4ZY0LR8KBMkEwSXqfz9WoYF6BjZC02X%2FaUqkXK0qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFDfD6OWevwR58krSrcA9f5eeik2qhK%2FwsbdqX4%2BU4QA8S6IMl4HkSvZYRpQyyi1n0GxGtY%2F%2FQtdPXInUZZEvIIRx%2Bln%2FqW7OXoziKUNJhvDUThtem8MpqPi%2Fj1aUmGDIONe66YLdK9VpBXDtMPDo4ikk9Hby0gWzjcpmB0pWqkzO9JHMod7YRUk2ATN6ZXYjLQU%2FEbAJc2Pe3jVD5pGyYxXI26VUJf6BAtHievnWkFfHf2TpGSxdqh82AH0Ih0OSKZXJCBs8Dwk9j8QjnBh5%2FO6zCKU3r5bogNAqv8qbM4r%2FegMsS0talAhobY3C3WPRpi8QgQiq9rybaMfF91AR7oWYYrawsgCVLs9fUqjgqS9avq8yZ8%2BkGu6Id7jBbTor%2Ffafh2dfTWLNDaK8L%2BlMfFMjpufYn6cFoKM8OnO%2BUnzD7SpmpEbsFxoXyeUj2GkENVA697e5wGQ5EjqAZyIcvxg%2FjXpx3Ph1SsUlFMc7hE7rtRGbxXa7h8VHCYBIdS7RiNTzbJjpoBxBrXmlPWqllyHrkSNfyXqz8xaqOjdjD6f%2Fd4iIs63DHluE8yooauhrdBlA65lahL6rC6ejiO82wOaUMqbJV4vme2GQVlfWSY1W3MngBLSmMD0h31Hi%2FndFbvDxtdHppPmgUEMPOsj9EGOqUBe9O%2BHOdGtJZ6GWwsSeJBc7f8oXh1Di1Oi%2BFIVb1dhNzJCeHVMfaq7ke4w6Pkp6VAOq6uyv5A7KLPdTxusd2173d6lxmVqNtbD%2F%2BCLtKQ%2BN00uBA9%2B2idKzT9WK7J%2BkzkzL8ZDTwGJeKBGPP4bqbXyMJdUJRLNMMjSU%2BneKl92QqCNo3zVA%2FGv1Mb%2F8I0val2%2FZSAcILcR1Mmf%2FMxT1pu3%2FOHPrPx&X-Amz-Signature=d0c650263b6fcd5db5f75fb0576ae92a4b1c24b595c2c0b0bf94395c9864ccda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
