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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYLSOG3O%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T184513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCkdh%2FMQLrxaum8%2B0ANG4sfG2S5%2Fp3qh%2BoCNWEqodJlJQIgKyZmAws%2BQIMShgomM%2FHRpo11kNPMx9fLb%2F7KKA1OEZ0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMkmOomhN7GmVV7QSrcAyDpIutvsPdPMIBxtb2RBVsCMDgTNLjytsvrYbJ6KwrD2%2BsZhKJo%2FHBCI6C%2F%2Fbf9r9IkChJtZqgWVZthDs%2FZimhGlcweT7z3euxKPIsOjlyTrAcj6o43%2F2US8zLUjE7Cr7Lxt3iIOB2d%2FNabUswmBWgsYeoCCbju1uEZa3Nv1MeUOAS6eWm4iJ7VMNpNA1NgyfiZpJd9S5ZQqJNcQRREjDE42hV8cwyhqvA7HwxVH%2FB%2B9oYW2ewwxIxCZWOdNFVdl6OcXRKrFwnDSLyyH3affIIOMnUz0UWEBbYX3xL7px4TlqAL32sG%2B%2FNzaQm3K9Z0PrR1JOWNy5W7pLSdbqw10fzdcCASL7H3stYDs4INwmyWmepPgA5sHorpG8th7DDKmaOPGFIBABrdwx4XH%2B4YqIw9Y10pnB%2F4WzJ5euhDykeuhixQ0WWA9Qq4uKqOQDaLKJr7IcO25bZf1OWzHNYWQcQlt2bRv0ZQzX3kyoWW9qcdgPRLikXp%2BHjhZzwM9ldDDJNBOdfPJYbVdRHRz1qdQCJFNWqoHU%2FB2S5wdhRjEw0zFwRAdErhnLqoCqnTMV5IVlF%2B4tT9%2FblenhlHfKkh1VPUZjTa72ADA3NyDvz%2Fpo6ww%2Btib1vwakCYf%2BnoMMyy8tMGOqUBea1jI5TU8cfitYcLWOvCaVpkNKl1E4RsBy5N6eIk3abdZpgIqD3VdqHzCxX42hUGU8lQ4V2skisUIGqzJl1j2XCjBpnF%2Bk753SDw1cVsfP9aPoGbpKfzI3e4y%2FSCegKq%2B1cyK8BbH731ndAzVD2iJ47M%2BHK%2BwZxfcoE7%2BtbYxeB7iDZT0AxzEWlcp2ZZzNrlJR5G2hpl84B3k1LGmnZSGtq6cZLe&X-Amz-Signature=1026ab1487e1cb11bd0e5fba03103a078bafe822256e00246db3074c70baa66e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYLSOG3O%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T184513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCkdh%2FMQLrxaum8%2B0ANG4sfG2S5%2Fp3qh%2BoCNWEqodJlJQIgKyZmAws%2BQIMShgomM%2FHRpo11kNPMx9fLb%2F7KKA1OEZ0qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMkmOomhN7GmVV7QSrcAyDpIutvsPdPMIBxtb2RBVsCMDgTNLjytsvrYbJ6KwrD2%2BsZhKJo%2FHBCI6C%2F%2Fbf9r9IkChJtZqgWVZthDs%2FZimhGlcweT7z3euxKPIsOjlyTrAcj6o43%2F2US8zLUjE7Cr7Lxt3iIOB2d%2FNabUswmBWgsYeoCCbju1uEZa3Nv1MeUOAS6eWm4iJ7VMNpNA1NgyfiZpJd9S5ZQqJNcQRREjDE42hV8cwyhqvA7HwxVH%2FB%2B9oYW2ewwxIxCZWOdNFVdl6OcXRKrFwnDSLyyH3affIIOMnUz0UWEBbYX3xL7px4TlqAL32sG%2B%2FNzaQm3K9Z0PrR1JOWNy5W7pLSdbqw10fzdcCASL7H3stYDs4INwmyWmepPgA5sHorpG8th7DDKmaOPGFIBABrdwx4XH%2B4YqIw9Y10pnB%2F4WzJ5euhDykeuhixQ0WWA9Qq4uKqOQDaLKJr7IcO25bZf1OWzHNYWQcQlt2bRv0ZQzX3kyoWW9qcdgPRLikXp%2BHjhZzwM9ldDDJNBOdfPJYbVdRHRz1qdQCJFNWqoHU%2FB2S5wdhRjEw0zFwRAdErhnLqoCqnTMV5IVlF%2B4tT9%2FblenhlHfKkh1VPUZjTa72ADA3NyDvz%2Fpo6ww%2Btib1vwakCYf%2BnoMMyy8tMGOqUBea1jI5TU8cfitYcLWOvCaVpkNKl1E4RsBy5N6eIk3abdZpgIqD3VdqHzCxX42hUGU8lQ4V2skisUIGqzJl1j2XCjBpnF%2Bk753SDw1cVsfP9aPoGbpKfzI3e4y%2FSCegKq%2B1cyK8BbH731ndAzVD2iJ47M%2BHK%2BwZxfcoE7%2BtbYxeB7iDZT0AxzEWlcp2ZZzNrlJR5G2hpl84B3k1LGmnZSGtq6cZLe&X-Amz-Signature=beb0579f15786d078e8116b4646f4298db4024301f70ef4e0b990cc7fd599f77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
