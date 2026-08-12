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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE3HAMKX%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T203122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDYZQJ7pWFzquruYmolheZdYQUPkkSSxWkNQGuT22oN2AIgSjLp%2Bf5es1lmD%2FjdnHTCSYlhDsPMkOQV25UQ3B4QC0oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY%2FKX5Ry24xj%2B0xIyrcAxU3AxPqMSRgazeC1DhI%2BCCZW7fNPPKc3k23UK2dZYpEVMYicO3Pt3W3favLl8CK48TjjvD5mPvzQBEaEM%2BJpjkndtBEskWWlJsZiyuomz6E4cymlSe9oLUZjXg8SNm3qYKNkAt5fOQ3bKC2Qd9kAe5s3%2BfA5PEen8Lgtk6Wbayuop1OydrcKYnrsDBFApWKS6f%2Bo7nlJjIadIup8NagwKX3gUZoY95I5Sn1B2ZjddoliEWtewRjc2YYrbRniHDK1l2f%2FRmVDS4XxyKbAa6sYQ3%2BL%2FukvebNLsz1B9I3b3FnYJTrYImGLwDuS69QL0EdoMZpkYumlQDuwtmPI545yU1Gv0I5ukX5bpOC2iKTOv6v2XqeLNimqn4DT%2BsnzaZiAxijiXAeyDLiGys868DjyjcJsU%2FjAfzYk1D5sNq2Z%2FkLm4oNe6ijSshn2SinPk3dDwOBQW9J1I2NrPdlLY2z7rsFgLgB57demC6yycdGDaehLDhdNYI%2BddB3DN0vjUIKTo%2Bld%2FoOGwUEThXZdTvWoKmIKAw9G8jcB2NioLGBqcFdBvNWwqRY6eMKMFmvFVEm99cthYQLhogyzLjxGuw0XUmWLBlZeiWhg0CiwaO3NrZh0%2BvvnG7OOqjHDNVNMK6H89MGOqUBue0UcIHgcp0tnFbtS1arFefydGiYYqW2P6ynAFHOWrCpKKcMeS3VeAu8dOH86ufjlZO%2B5RzRMnKWnRy76X4skgL8zr5o1ZmgOAtm99V7diw2zAzaVgwwpjTZwQpOd6Zhm1QfBVWvixHPG8wXLv0lQzopXQRbWyADUrS4ZxdWOFYzjz01zagtgZrlGFeJH4JE8M%2FM3SbUEjqvORu8UYQC6RK3UOgd&X-Amz-Signature=dedee08d4682a1f7d91d8ebfade4885bd1fba5b7ba8d25a6040fe63407b994aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE3HAMKX%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T203122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDYZQJ7pWFzquruYmolheZdYQUPkkSSxWkNQGuT22oN2AIgSjLp%2Bf5es1lmD%2FjdnHTCSYlhDsPMkOQV25UQ3B4QC0oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLY%2FKX5Ry24xj%2B0xIyrcAxU3AxPqMSRgazeC1DhI%2BCCZW7fNPPKc3k23UK2dZYpEVMYicO3Pt3W3favLl8CK48TjjvD5mPvzQBEaEM%2BJpjkndtBEskWWlJsZiyuomz6E4cymlSe9oLUZjXg8SNm3qYKNkAt5fOQ3bKC2Qd9kAe5s3%2BfA5PEen8Lgtk6Wbayuop1OydrcKYnrsDBFApWKS6f%2Bo7nlJjIadIup8NagwKX3gUZoY95I5Sn1B2ZjddoliEWtewRjc2YYrbRniHDK1l2f%2FRmVDS4XxyKbAa6sYQ3%2BL%2FukvebNLsz1B9I3b3FnYJTrYImGLwDuS69QL0EdoMZpkYumlQDuwtmPI545yU1Gv0I5ukX5bpOC2iKTOv6v2XqeLNimqn4DT%2BsnzaZiAxijiXAeyDLiGys868DjyjcJsU%2FjAfzYk1D5sNq2Z%2FkLm4oNe6ijSshn2SinPk3dDwOBQW9J1I2NrPdlLY2z7rsFgLgB57demC6yycdGDaehLDhdNYI%2BddB3DN0vjUIKTo%2Bld%2FoOGwUEThXZdTvWoKmIKAw9G8jcB2NioLGBqcFdBvNWwqRY6eMKMFmvFVEm99cthYQLhogyzLjxGuw0XUmWLBlZeiWhg0CiwaO3NrZh0%2BvvnG7OOqjHDNVNMK6H89MGOqUBue0UcIHgcp0tnFbtS1arFefydGiYYqW2P6ynAFHOWrCpKKcMeS3VeAu8dOH86ufjlZO%2B5RzRMnKWnRy76X4skgL8zr5o1ZmgOAtm99V7diw2zAzaVgwwpjTZwQpOd6Zhm1QfBVWvixHPG8wXLv0lQzopXQRbWyADUrS4ZxdWOFYzjz01zagtgZrlGFeJH4JE8M%2FM3SbUEjqvORu8UYQC6RK3UOgd&X-Amz-Signature=3c407ee6881d25586a317ce8165845566d19039cd003cad1ab2f060ca191d3ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
