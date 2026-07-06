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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SQKIJZY%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T145340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzd2VrTeB0vCqUy9pXf5Ef5MdAiVHAFpTz0P5DyD1HuAIhALfqYTpxEMoAqOx1bs1l1H%2BeOKosqAQthLfx76wJtnhpKv8DCFgQABoMNjM3NDIzMTgzODA1Igzgj69LZyg4QWNP2%2B8q3ANktQkjYmcnSAZ6LdNL31rOlE9amVmi6YUK2ArjuKGotW1rI19CruhYQH3Mj%2FMdyM9Bxi17wyQi8gQdaVJjB7MwbF6M3xfLIzwZNb5N1TRyE%2Bpp4jhMpGaqa%2Be8ms5E3ceJBCMQZ1ARAMl2OkwNN%2FS1AnOYs26Piqy3x6JWhpjmmOnot%2FgB3p%2B6nERY0ytYyNf4%2FtvE%2BHuxEsSmEBgZyJKgWW5J%2FXnId9LVXq4VyWSrMcRzl8uhe8k3%2BzozMHknhuCELK2IbZwhkEq9ZZwvEnttA2SNPkrn8XpS7YqZa5A8pqujQDsDN3n0lhuqnu57h%2Btyzj9jGiqcXeAuzCaG5OEyfqtZjRd4H0W5adG%2BxJGgiA8zgXUckmumkrNJgY4QoJWA0L5OQcd%2FZvUN8bS5IUpn5KeUvOctsOLYxQ7IMu7%2FGPkcVxS1T3lvkD3IryScNk0Bb1rGeZGW3wkND%2Fc7591hlFlMoWTMJmBsdfiS%2FGFSSdwjUdKgnLnXPDh3l2Lu6TmbZwQQdzPwU6ydFrqavRYDEVlZBjslP3Z8CTBJ2JUnsSvpwgGBVtGOnQ%2FRerKphSsx0diUbVuOMTKK2ZZDxTKqIO%2BQjxCVtTqDgN3U072guzqb2lBb%2BcYfJB5wKTD8%2Bq7SBjqkATweyO5xQQp17wc4sNcsn7Z0esBFjJbJX9sDBj1MNP1hWbQnV7HtVnpp3yWp3eeWDny%2B4AKLrZjkNhyQomQzXU0OHwP50xLNz1%2FsfxF6FnXC3E7OrYDXTQa9enz9znhSSxdw%2BoJ4X2Sw094TU47KqkdKSCHL0x%2BmPx6DGVjTh81HC%2Fa2rELe3%2BUsOWjx2L8vFCuDKXpDKl7%2BSw906AobZoA6cM95&X-Amz-Signature=d67b97e0441da8105d1edd3e04a95ec24db65372783011b71a7f809b38958602&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SQKIJZY%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T145340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzd2VrTeB0vCqUy9pXf5Ef5MdAiVHAFpTz0P5DyD1HuAIhALfqYTpxEMoAqOx1bs1l1H%2BeOKosqAQthLfx76wJtnhpKv8DCFgQABoMNjM3NDIzMTgzODA1Igzgj69LZyg4QWNP2%2B8q3ANktQkjYmcnSAZ6LdNL31rOlE9amVmi6YUK2ArjuKGotW1rI19CruhYQH3Mj%2FMdyM9Bxi17wyQi8gQdaVJjB7MwbF6M3xfLIzwZNb5N1TRyE%2Bpp4jhMpGaqa%2Be8ms5E3ceJBCMQZ1ARAMl2OkwNN%2FS1AnOYs26Piqy3x6JWhpjmmOnot%2FgB3p%2B6nERY0ytYyNf4%2FtvE%2BHuxEsSmEBgZyJKgWW5J%2FXnId9LVXq4VyWSrMcRzl8uhe8k3%2BzozMHknhuCELK2IbZwhkEq9ZZwvEnttA2SNPkrn8XpS7YqZa5A8pqujQDsDN3n0lhuqnu57h%2Btyzj9jGiqcXeAuzCaG5OEyfqtZjRd4H0W5adG%2BxJGgiA8zgXUckmumkrNJgY4QoJWA0L5OQcd%2FZvUN8bS5IUpn5KeUvOctsOLYxQ7IMu7%2FGPkcVxS1T3lvkD3IryScNk0Bb1rGeZGW3wkND%2Fc7591hlFlMoWTMJmBsdfiS%2FGFSSdwjUdKgnLnXPDh3l2Lu6TmbZwQQdzPwU6ydFrqavRYDEVlZBjslP3Z8CTBJ2JUnsSvpwgGBVtGOnQ%2FRerKphSsx0diUbVuOMTKK2ZZDxTKqIO%2BQjxCVtTqDgN3U072guzqb2lBb%2BcYfJB5wKTD8%2Bq7SBjqkATweyO5xQQp17wc4sNcsn7Z0esBFjJbJX9sDBj1MNP1hWbQnV7HtVnpp3yWp3eeWDny%2B4AKLrZjkNhyQomQzXU0OHwP50xLNz1%2FsfxF6FnXC3E7OrYDXTQa9enz9znhSSxdw%2BoJ4X2Sw094TU47KqkdKSCHL0x%2BmPx6DGVjTh81HC%2Fa2rELe3%2BUsOWjx2L8vFCuDKXpDKl7%2BSw906AobZoA6cM95&X-Amz-Signature=0fe855c2f2925ae92317947b593de7e58a92fe6fd4625145f72a67f77aff0dc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
