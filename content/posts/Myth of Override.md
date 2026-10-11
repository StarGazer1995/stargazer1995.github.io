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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ICHNPJP%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T023406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FbrJ8LEbwX9BrT6VC0lV8aCETP1BobHprFtBknZYGrQIhAP7hNEQLSdy%2Fk4CWEX66pKGn4tW8C8Ma7PdUvjlPvpPLKv8DCF4QABoMNjM3NDIzMTgzODA1IgyCKy8k9d%2FcWkri8v0q3AO4l%2BWPfIxRWePvqdXt9y6W5ll3E%2B%2FwKh9aeUGRI0mKKjhTfMfH3CHIcsU2z2G1l8oJwe4XzT1e6WBkUTgED2VQ7lPHx8uhnEiTI9EzxZZGElZwdZIuIAfib0nxavLXUggYPmT3l9O2kkrZ3%2FUSLtOgY%2Fmd1bC8FwouYyNoT1m3DgCy8oVf2d2ZTFoa9nDfe%2Bm3fjAQSye4Frt0ElKy0B9P77wZr5xwb3JNMEj67k7qQHU2b4WKFmtZSYmacHgPHt73hJ%2BZs9wOS3ojJ0OLq1ZwSwmaR8FHeLFpqtdCPcBoQPAVWTwfpDo8Tx36Sc0TbAAa89wyHYG3cYIwAmsp%2B1j83tLyhn%2BtVQ3MWxllijqRDlXWFViGSwMELufdUoZa1l2Mgj3juFK81Zi26BbHenXObN8B6%2FKmK%2FU78tbT%2BmtsZDsNDjhSqxcuIp9uv1O3H331lkfZ2pBpKZ5hMR9RIBmL5VD8zIU1L8hOdhfCVYRm60Z%2FjNiYtrNTuM8rELFjSZO3AKLaC4v1sB%2F2h%2Fgym2fJr1sy8VLByukYYxxxRvLy6DIqUOXRZN7Ld%2Fuhrz21484Q6Pz2JPW7cIziyz16z7JUbWqnor29Hj9uW5isGgCzY9Xj%2F1WMaHKPY2PLvjD92KrWBjqkAZslPvsx%2B4DTCg3QTut6NT1JrZ1f7RXbe2wwIi%2FzqnR6v9PLGGHJCl3ysemFjAhFeH8fRrPXvUjkHBxGZ1me9tI6L9kJxPYtuifs2XG61f%2Br7jgFLdO1ldU1yLKD52QXgJC2NOjvvfwmQ2fyiAQXf1znqriQuj3KIzAQ4uSEED8WiJD6n7%2B6VOpfNGe7GbVgL8hFxi3WkOVjT%2BF7TezXDI6lVV1C&X-Amz-Signature=fc6231d7f9a284e168fb598ac77bd5cad4f86a4676d25eec73fb7dca6dd85ada&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ICHNPJP%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T023406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FbrJ8LEbwX9BrT6VC0lV8aCETP1BobHprFtBknZYGrQIhAP7hNEQLSdy%2Fk4CWEX66pKGn4tW8C8Ma7PdUvjlPvpPLKv8DCF4QABoMNjM3NDIzMTgzODA1IgyCKy8k9d%2FcWkri8v0q3AO4l%2BWPfIxRWePvqdXt9y6W5ll3E%2B%2FwKh9aeUGRI0mKKjhTfMfH3CHIcsU2z2G1l8oJwe4XzT1e6WBkUTgED2VQ7lPHx8uhnEiTI9EzxZZGElZwdZIuIAfib0nxavLXUggYPmT3l9O2kkrZ3%2FUSLtOgY%2Fmd1bC8FwouYyNoT1m3DgCy8oVf2d2ZTFoa9nDfe%2Bm3fjAQSye4Frt0ElKy0B9P77wZr5xwb3JNMEj67k7qQHU2b4WKFmtZSYmacHgPHt73hJ%2BZs9wOS3ojJ0OLq1ZwSwmaR8FHeLFpqtdCPcBoQPAVWTwfpDo8Tx36Sc0TbAAa89wyHYG3cYIwAmsp%2B1j83tLyhn%2BtVQ3MWxllijqRDlXWFViGSwMELufdUoZa1l2Mgj3juFK81Zi26BbHenXObN8B6%2FKmK%2FU78tbT%2BmtsZDsNDjhSqxcuIp9uv1O3H331lkfZ2pBpKZ5hMR9RIBmL5VD8zIU1L8hOdhfCVYRm60Z%2FjNiYtrNTuM8rELFjSZO3AKLaC4v1sB%2F2h%2Fgym2fJr1sy8VLByukYYxxxRvLy6DIqUOXRZN7Ld%2Fuhrz21484Q6Pz2JPW7cIziyz16z7JUbWqnor29Hj9uW5isGgCzY9Xj%2F1WMaHKPY2PLvjD92KrWBjqkAZslPvsx%2B4DTCg3QTut6NT1JrZ1f7RXbe2wwIi%2FzqnR6v9PLGGHJCl3ysemFjAhFeH8fRrPXvUjkHBxGZ1me9tI6L9kJxPYtuifs2XG61f%2Br7jgFLdO1ldU1yLKD52QXgJC2NOjvvfwmQ2fyiAQXf1znqriQuj3KIzAQ4uSEED8WiJD6n7%2B6VOpfNGe7GbVgL8hFxi3WkOVjT%2BF7TezXDI6lVV1C&X-Amz-Signature=7ee12fceb2c090d8e068eabbb455ce14761769b739eae6d2c24128f470329743&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
