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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FIS52RM%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T104124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQDgMfJG%2Bslgq6GbXpLToi%2FYoVHUkYgn3hNYQ9MNlLx8qwIhAOy5ohuTQ%2F%2FnxWjwmRhCDK%2Fms7MKBQrU7IkItybcAO3kKv8DCBsQABoMNjM3NDIzMTgzODA1IgxBCpBevz5pDVpgCk8q3AMighPb8Uq%2B073nRVAcaAwknoazbbQaG9htebxHdXy0NWVTULgZ0jp6jW6qCpM2dmpLJ%2BhP5FK%2BmJmKE2SnrhP1wjkqSFJDG6Ng4g8rQVrGT8uOz6TdLGq9xaa1KwuwrJW6W1kP8AIxbsQsrJKLf70Qbwz1kaJnn3xTsNeJxEYiDRPmVPORWEG8MiSo4anUeQ%2ByCQEpZLTd%2B%2Bv50g18TBaJ1UQbLtsggwDctsP%2BAg9rLDkGwuiQbcJJYgSASFESfImA0%2Bz%2FB0P%2B3vcq6Z%2Fd00W%2FYoe1bzs%2FHK4FC6iOh6AtSWuziZ1Xw2q6YPZwvAgS60iD%2FPhK4R8jeBWjmvT8vNdCMGvRHB9FUoVpe5Uv%2F6xf89T5P4olM0wmR13fYD1reB6XinzUeBlWWok3SKgZFf3PM2ceNCUYezJgeU24BMkQmo9roNngsDMgPFKktzXPfFpK25bQiWMMeeFJw3KTg8SKpE%2Bf8RwFW8JOjcHYc0CSsb2qJ7plkuLLHYrbW9i0GVUzJ982qQFaliZmpMZaJft%2Fg%2Fwt5%2BU4a02cn6U%2BFtLBGBinE2kyk14D8Bge1Yf2yCJYB5osM0uzAGd8vT5UJxLSRNZQ7HhZucUUR2aeATcwTaNDFeQCHPu%2BjF10VDDn1MDQBjqkATZeo3wtKyO9ociqeqnMrPPXcAjqo5s0lhYm%2FQoHWrywIB4XwLscjnPLdwUQIgkFkc7viAf8Y3r1HSwbAVhFj3vBNe1dk8o4W%2BKvaYTYY58pappgDS5ncs9Ozd8e%2BdQVZmjtKve1hI1vtqWh2WX0lkVi07yBk2BOdu%2FawBw0Hg0i90Ng1yCRSZthtm6okpG1eIR%2FuxB8R8JOLZyEW%2Ff%2BKx2lcTdh&X-Amz-Signature=80a9ae695ed8412a31384c681aa9fdf0957fbddbe2e949b62f6902aa57dbf17e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FIS52RM%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T104124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQDgMfJG%2Bslgq6GbXpLToi%2FYoVHUkYgn3hNYQ9MNlLx8qwIhAOy5ohuTQ%2F%2FnxWjwmRhCDK%2Fms7MKBQrU7IkItybcAO3kKv8DCBsQABoMNjM3NDIzMTgzODA1IgxBCpBevz5pDVpgCk8q3AMighPb8Uq%2B073nRVAcaAwknoazbbQaG9htebxHdXy0NWVTULgZ0jp6jW6qCpM2dmpLJ%2BhP5FK%2BmJmKE2SnrhP1wjkqSFJDG6Ng4g8rQVrGT8uOz6TdLGq9xaa1KwuwrJW6W1kP8AIxbsQsrJKLf70Qbwz1kaJnn3xTsNeJxEYiDRPmVPORWEG8MiSo4anUeQ%2ByCQEpZLTd%2B%2Bv50g18TBaJ1UQbLtsggwDctsP%2BAg9rLDkGwuiQbcJJYgSASFESfImA0%2Bz%2FB0P%2B3vcq6Z%2Fd00W%2FYoe1bzs%2FHK4FC6iOh6AtSWuziZ1Xw2q6YPZwvAgS60iD%2FPhK4R8jeBWjmvT8vNdCMGvRHB9FUoVpe5Uv%2F6xf89T5P4olM0wmR13fYD1reB6XinzUeBlWWok3SKgZFf3PM2ceNCUYezJgeU24BMkQmo9roNngsDMgPFKktzXPfFpK25bQiWMMeeFJw3KTg8SKpE%2Bf8RwFW8JOjcHYc0CSsb2qJ7plkuLLHYrbW9i0GVUzJ982qQFaliZmpMZaJft%2Fg%2Fwt5%2BU4a02cn6U%2BFtLBGBinE2kyk14D8Bge1Yf2yCJYB5osM0uzAGd8vT5UJxLSRNZQ7HhZucUUR2aeATcwTaNDFeQCHPu%2BjF10VDDn1MDQBjqkATZeo3wtKyO9ociqeqnMrPPXcAjqo5s0lhYm%2FQoHWrywIB4XwLscjnPLdwUQIgkFkc7viAf8Y3r1HSwbAVhFj3vBNe1dk8o4W%2BKvaYTYY58pappgDS5ncs9Ozd8e%2BdQVZmjtKve1hI1vtqWh2WX0lkVi07yBk2BOdu%2FawBw0Hg0i90Ng1yCRSZthtm6okpG1eIR%2FuxB8R8JOLZyEW%2Ff%2BKx2lcTdh&X-Amz-Signature=ae1a9d833b56c8279bc15c847548b1532c8e6a1aed29d2db784f478daa2363a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
