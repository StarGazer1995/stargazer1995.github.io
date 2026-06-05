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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2GZRJPK%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T192944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBD4FHREhn2PzwOtzHXm0TVxqTFswnOwaHWGERtZ1WHwIhAOrGORiwdz8fNccacwJBppeaNeTPoukQu0YvioisUgfRKv8DCHMQABoMNjM3NDIzMTgzODA1IgyZ3vhp2jzoWl2YEqIq3AO9LeeBUg2sxGVM6LxklPrnnqj3wGeDxzKlZ%2B1KWevGKFnCyx2qlhBN7D%2FT5JHWJ4JHK7d2vtPjwbEMmQ4tX8V2WRYZDl5VGM52QJbRQXdLHT8b5v20CBTWBm1uDwp1ZA1hv6U1kWvjQZ98cq9J9lWZ9qA0YVIuLprYpX2Hvi4moPbUa%2BUifv9tJsfHzSHJm6rHl0VbMoaDJTj2LjkchhL9BzWUfZWxd5vnuh586%2FtT3olLFgDyyllxYkHMI4lvbvS1PR6nR1zaN5bkXZo0OcIH4S0hNFNAB0YLAv8WyaZtdQLn4mgym9wv7a%2BS9H0b%2F6JrNsrt9IllS5zZPXh04oUJh3cXe8pXZdh56UOWurQbkGTW0fJSfoF8FCbliffj5OyaAfMUgcX1KD%2B%2BEFJ9GE2BPyrz8wBVc1iJrf0BuQvPWyWrk2UJ%2F523ud%2Fs%2B5D%2FRC%2BoLp%2FiGBluBeYGfNbhnZ7QZGoIzuP2XJxvq0DPGguyc%2BwhqNKTOJ3qexEn2c1DIhkqrBrbYUsNNnxJpZKCJiFc7DlNddQdncL578IWWBE30ySSziKPr41MH9WlCuTrztVf9c%2FUn%2B0X3zZ6GJvAYt%2BY9d3n%2FARC%2FZc3dg6HT8opchFqZ%2B4XGO9puR3FRTDPoIzRBjqkAaipptlZanYDRJjl7WIKDLm6gzw%2F1EAXkGx2ygD7z781wCN8aHmX7O4I1sG%2BC5q9G1LqgjQhxWfiej7tIM0GjpqT0em7le9E3xxPhN%2FHUIZb%2F6dECSz0JYg4RXkIdjT5lNGBxrkxqLALfbgtlznZtS2UakX%2F4YlmEl2tFYsWpohQ%2FRDg%2F6JYonyguIylcF7FeiWS%2B4ybsZI3C6zN9rCFOdcqXKYk&X-Amz-Signature=169b78ebd9ab0a15ecbde53ede14b46daeb07f35a4cb7499edf0343e0823199b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2GZRJPK%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T192944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBD4FHREhn2PzwOtzHXm0TVxqTFswnOwaHWGERtZ1WHwIhAOrGORiwdz8fNccacwJBppeaNeTPoukQu0YvioisUgfRKv8DCHMQABoMNjM3NDIzMTgzODA1IgyZ3vhp2jzoWl2YEqIq3AO9LeeBUg2sxGVM6LxklPrnnqj3wGeDxzKlZ%2B1KWevGKFnCyx2qlhBN7D%2FT5JHWJ4JHK7d2vtPjwbEMmQ4tX8V2WRYZDl5VGM52QJbRQXdLHT8b5v20CBTWBm1uDwp1ZA1hv6U1kWvjQZ98cq9J9lWZ9qA0YVIuLprYpX2Hvi4moPbUa%2BUifv9tJsfHzSHJm6rHl0VbMoaDJTj2LjkchhL9BzWUfZWxd5vnuh586%2FtT3olLFgDyyllxYkHMI4lvbvS1PR6nR1zaN5bkXZo0OcIH4S0hNFNAB0YLAv8WyaZtdQLn4mgym9wv7a%2BS9H0b%2F6JrNsrt9IllS5zZPXh04oUJh3cXe8pXZdh56UOWurQbkGTW0fJSfoF8FCbliffj5OyaAfMUgcX1KD%2B%2BEFJ9GE2BPyrz8wBVc1iJrf0BuQvPWyWrk2UJ%2F523ud%2Fs%2B5D%2FRC%2BoLp%2FiGBluBeYGfNbhnZ7QZGoIzuP2XJxvq0DPGguyc%2BwhqNKTOJ3qexEn2c1DIhkqrBrbYUsNNnxJpZKCJiFc7DlNddQdncL578IWWBE30ySSziKPr41MH9WlCuTrztVf9c%2FUn%2B0X3zZ6GJvAYt%2BY9d3n%2FARC%2FZc3dg6HT8opchFqZ%2B4XGO9puR3FRTDPoIzRBjqkAaipptlZanYDRJjl7WIKDLm6gzw%2F1EAXkGx2ygD7z781wCN8aHmX7O4I1sG%2BC5q9G1LqgjQhxWfiej7tIM0GjpqT0em7le9E3xxPhN%2FHUIZb%2F6dECSz0JYg4RXkIdjT5lNGBxrkxqLALfbgtlznZtS2UakX%2F4YlmEl2tFYsWpohQ%2FRDg%2F6JYonyguIylcF7FeiWS%2B4ybsZI3C6zN9rCFOdcqXKYk&X-Amz-Signature=92fcb8dca6c4ea6da48b32880d7fda310b12fc928a0efeb4597a6d3ef09b1af9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
