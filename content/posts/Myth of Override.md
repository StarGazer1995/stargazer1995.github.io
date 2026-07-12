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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZKSPJKX%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T184626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIQDXOZIxYmBugJ22wJxadazwmAqoyZrj%2BGKhmwqthRA83gIgeoIp%2FonHWx2UCzMMPgwCaO5jpkb6Djsxf7PDoN6VcUYqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtaAd8ZILJq4mg6MircA8oJKk8XcRcVIJV7hA2Y1XOV54oi4AXX6Cor%2BCiJoaN6RTCW%2BkhH1dIrygBrW6yX4NjNZFMdZgg3tmi0tgisA0azIoV5QWsND2zz5uEJ8ORLO91qqYMsn0Lz7CQi31t3tjmy5nVSoGBVV6iFqvzciac9waKdB3CGh72DRVv2HaWAekeoXJEjzWKGcThM%2BlvQB8Q4wpxbFJAhFuQeDtqnhhXoa5TyUHO7AwEu5qoRPZze3JxDvgZSKN5opJV0yQieydXFuHosE5wkfT9zF2maTBtLJ0rBMF8ISE5qGfSq%2FyOKi7RzNZGcl6RjLWmjCr7JqJ2STti7EE3HEYBxdWKgrWBu60ll8pRzauDENf7dwlkBbZX1KTeo7kEGPBzZ6MOn8hIT%2Fwp%2BgWfv2PAJJDTmklVJN6dHCK5FBCE%2BS1pPAofuBViN1sLzGliiVwZVt5nWadtydpy%2BH6dkYJROjv1twEPiz4V7za2zy4ql9mVNKuxjVOtlvU0066ePXCEcZs%2BiwQuivIRJ5mhELpvNri1ROyoy9bASuvJ9VWBELWzYxmYQ4dP%2Bn57AuHPi3oGWBNkK60Utl4Oc6XYQtWUPDqvXReplyWty909OLtn8sBtk406FdwKwMuRUgXCPAIuqMLSNz9IGOqUBjThtWKXYJe2M5B%2BFXmySXReArLsc023J%2FV39ys74omNrje1fkO2uqR8pDHuNk0VHYzzOVokJ%2FDFsDDQVd6m5H%2BgwSBe6xkY9MYzN9ErVdJhrSE4afsI16TpqUzYB%2FZhkFaY%2B3Rrn8eecV6mWpyiyrn4jc9TK1uKidpMA3UjFl%2FlKGoo%2BvIzwZNBdGS7GuRhhEZJw9octI639cHBv8iqchJ1UKmyw&X-Amz-Signature=7ffbeed531004d3ec36285f0fb256cac20f0783361c9dfa8db5bc171a4102864&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZKSPJKX%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T184626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIQDXOZIxYmBugJ22wJxadazwmAqoyZrj%2BGKhmwqthRA83gIgeoIp%2FonHWx2UCzMMPgwCaO5jpkb6Djsxf7PDoN6VcUYqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtaAd8ZILJq4mg6MircA8oJKk8XcRcVIJV7hA2Y1XOV54oi4AXX6Cor%2BCiJoaN6RTCW%2BkhH1dIrygBrW6yX4NjNZFMdZgg3tmi0tgisA0azIoV5QWsND2zz5uEJ8ORLO91qqYMsn0Lz7CQi31t3tjmy5nVSoGBVV6iFqvzciac9waKdB3CGh72DRVv2HaWAekeoXJEjzWKGcThM%2BlvQB8Q4wpxbFJAhFuQeDtqnhhXoa5TyUHO7AwEu5qoRPZze3JxDvgZSKN5opJV0yQieydXFuHosE5wkfT9zF2maTBtLJ0rBMF8ISE5qGfSq%2FyOKi7RzNZGcl6RjLWmjCr7JqJ2STti7EE3HEYBxdWKgrWBu60ll8pRzauDENf7dwlkBbZX1KTeo7kEGPBzZ6MOn8hIT%2Fwp%2BgWfv2PAJJDTmklVJN6dHCK5FBCE%2BS1pPAofuBViN1sLzGliiVwZVt5nWadtydpy%2BH6dkYJROjv1twEPiz4V7za2zy4ql9mVNKuxjVOtlvU0066ePXCEcZs%2BiwQuivIRJ5mhELpvNri1ROyoy9bASuvJ9VWBELWzYxmYQ4dP%2Bn57AuHPi3oGWBNkK60Utl4Oc6XYQtWUPDqvXReplyWty909OLtn8sBtk406FdwKwMuRUgXCPAIuqMLSNz9IGOqUBjThtWKXYJe2M5B%2BFXmySXReArLsc023J%2FV39ys74omNrje1fkO2uqR8pDHuNk0VHYzzOVokJ%2FDFsDDQVd6m5H%2BgwSBe6xkY9MYzN9ErVdJhrSE4afsI16TpqUzYB%2FZhkFaY%2B3Rrn8eecV6mWpyiyrn4jc9TK1uKidpMA3UjFl%2FlKGoo%2BvIzwZNBdGS7GuRhhEZJw9octI639cHBv8iqchJ1UKmyw&X-Amz-Signature=3735947cc292d9d9ded42408546c6f7f1d634e6f32f61fa4d811946e2dcb238e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
