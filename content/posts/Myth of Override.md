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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNMKJ2GA%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T131456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIDUEcQyv0rbKEiNwYA%2B4N77zRWpVybdBIUixZqhnCzZKAiEAg2Wb1k7bbayKaCykIXcnwwPbBXXiQDHFe5LroB%2FqKywq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDEPeSScdYsHO8oOwGyrcA5BVAe8kAEAr4oChSKG8BniUa3z30gsX995jxd5LsTocD4yWh8EpQxTHR1RrFvqAS%2BL3R%2BVhFNPcX3ncWM5m%2B7oHjsjd9H8ZFR%2FEM1cV7rQnr1kg%2FgmoOC4GWdMuSG0N5Prv9lGrmpEdgmpvm16Qpg9H4gVU7PjiilVngWtvzBieW4zb%2BuPOojeU7pw5WYej25QEfqGb1qYSAKH2LQic1u4uuLjzun4aVPAPsm7a6Dj%2BvxwwIGcIglKIe%2Bfi17JEQZdMHyG8NCyxm3c5gkmAbz8jlL4kDVe2EfWzrIXF3cmwHanz14KdEMMfvz7Z7O%2FskJkind49DZS5olreWVfrelGM6KhPukNKx0md8X4iXNGU95W%2F8eg7H7IBRwwX9dcO%2FHyOdtJQdef8iDfK2Qniov5S3MIHpZQuGS60Y5tV6sNW5UYU%2Bf6IUbXCeqUZ63JWq7GJIqLZA1ozMGJfwbJxGWjbYHrDOm6mqBH0ropcxBig7wLCG%2Bq%2BQbeDl2E7sMTI1CUuMNxGERRDdNq2dR9votpJDIVS01LbdJ0JQuWADbBKev5pXQ8YOIPParUP9Wm1VQJn3fy6nBetTF5tknN7K0MXWhHvOAWZcmsVwPkMhr5hI4W3cU9zOXcxvLr6MP6M49IGOqUBuue4h0XcoJy%2FP0ABoSsMVfFaTBHDTKzUypogPEfTapgDkqycTZ97g%2Ba3PvIJp03VbIffTKjHqe14D48gXaf8lq%2FJ2i581zBHyQ%2BZCHl%2BsCz9aF05f5CvOjsx9zsyIdr35h5WCp4N8J34FV6UDHLbkykuJ5gdDYppGcFAjpfl1SHE2HpJLkouPW73RbEPOmZHJJFIPXMSsg1sFaQs%2FMFDbYk6a3Cs&X-Amz-Signature=ab94ed4a740a9a67d3f230f8c0d5acc8e6c6d551bacdac76e9a51bc3fa00620a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNMKJ2GA%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T131456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIDUEcQyv0rbKEiNwYA%2B4N77zRWpVybdBIUixZqhnCzZKAiEAg2Wb1k7bbayKaCykIXcnwwPbBXXiQDHFe5LroB%2FqKywq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDEPeSScdYsHO8oOwGyrcA5BVAe8kAEAr4oChSKG8BniUa3z30gsX995jxd5LsTocD4yWh8EpQxTHR1RrFvqAS%2BL3R%2BVhFNPcX3ncWM5m%2B7oHjsjd9H8ZFR%2FEM1cV7rQnr1kg%2FgmoOC4GWdMuSG0N5Prv9lGrmpEdgmpvm16Qpg9H4gVU7PjiilVngWtvzBieW4zb%2BuPOojeU7pw5WYej25QEfqGb1qYSAKH2LQic1u4uuLjzun4aVPAPsm7a6Dj%2BvxwwIGcIglKIe%2Bfi17JEQZdMHyG8NCyxm3c5gkmAbz8jlL4kDVe2EfWzrIXF3cmwHanz14KdEMMfvz7Z7O%2FskJkind49DZS5olreWVfrelGM6KhPukNKx0md8X4iXNGU95W%2F8eg7H7IBRwwX9dcO%2FHyOdtJQdef8iDfK2Qniov5S3MIHpZQuGS60Y5tV6sNW5UYU%2Bf6IUbXCeqUZ63JWq7GJIqLZA1ozMGJfwbJxGWjbYHrDOm6mqBH0ropcxBig7wLCG%2Bq%2BQbeDl2E7sMTI1CUuMNxGERRDdNq2dR9votpJDIVS01LbdJ0JQuWADbBKev5pXQ8YOIPParUP9Wm1VQJn3fy6nBetTF5tknN7K0MXWhHvOAWZcmsVwPkMhr5hI4W3cU9zOXcxvLr6MP6M49IGOqUBuue4h0XcoJy%2FP0ABoSsMVfFaTBHDTKzUypogPEfTapgDkqycTZ97g%2Ba3PvIJp03VbIffTKjHqe14D48gXaf8lq%2FJ2i581zBHyQ%2BZCHl%2BsCz9aF05f5CvOjsx9zsyIdr35h5WCp4N8J34FV6UDHLbkykuJ5gdDYppGcFAjpfl1SHE2HpJLkouPW73RbEPOmZHJJFIPXMSsg1sFaQs%2FMFDbYk6a3Cs&X-Amz-Signature=a107438b4660bae68afdc8b4c208351813b46a9ebe985731f263ca898f0a38b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
