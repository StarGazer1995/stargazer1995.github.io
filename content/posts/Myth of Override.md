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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPLCAYAB%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T145622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICg4H04XHQ%2FNmigv6DSN3L2957OzYUuTQ42TzaPeedcXAiEAm2O5KH%2BUq5Ogr0BD4Ri4PRUjqMrX6KQStuHU%2BFm0Td8q%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDAc%2BVh%2FRtzTJQwbkaCrcA56%2FjzZLehHCj4VAm%2FyRWvfWcIiOZFtbKjJCTYkvwRTVN%2B2mJJK1cIKWQY5%2Bg7XsMWqjX7IrgYXyuJ2%2B69gzA05AXX71KDkx62Wca2BG1gY8fD7FK3%2FmtKPpmsqOZaGT%2FbU%2BtRzX7kfeQG9kfPDX02nzn4E1SUFWiDmNF%2FDpoj4NkYGbJRL9gPgDsugGP5jYTlprmQ%2BdfvMonTUe7ruK%2Bu32F10zYQZbgDW1oWX6%2FITuu6DcIOd1Uc6EtXVVu3wJVjc1a8YhI6F3dIh9seTBS3GC2oK%2BTHzA3DKZivs1Tdi9L8X%2BZIrl93pfyv%2FGmX68d795fG8sRhV3idNUdigXNSbNMEInuOLKulskeqTYyOF8%2F%2Fjww8F72ndfNEg4Lk3BKXc9n9v0jXPl8dcr9km0oTD2FIgjFmQtbVMKeYcJRFR7RS1fEaZrweOdHKw%2B0IkOYq%2BUGTCV2o9e7onBrBHZvYMsy38n1HhN2WdK8xR7OnVMCK98gNYHsZG%2F6u0Rh0Z42Oe9MgKsMMXHUC1bKr0DdxCaQLf5wvFsKqEIcWFYUPaS7FNUgxaBoHUUN%2FK8pN4UaqZk2ZTUvV9UEtllPiUyubXpYVDhG0vHZ41iDA91k3MyRIoV3zgus9zyzUXLMLD2y9AGOqUBAo2Bi9QSHan1YOLeZz7G4ROc1WSe%2BIz3thyERD0A3CkNCC21SHdMwsoNHjK6VIb7N8CZjIJQYAgMRHwpJf2rqXE1gNPuKOYXvbXoGBU1ukrq2URfMuixbMd5Vgd5Tk0FdEny4VE4DWJwY0XXQs5CaeIbX4IRaHKQiBPjYGZtJm0jdLPnBMeYj8jEL0MAjIx76HG4BsA1%2FFbpyLVmWZFozDswoZYU&X-Amz-Signature=b7f993e0c9f8be2a6cad88a09d3a3c7d4d100cb9db789059856a665147320234&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPLCAYAB%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T145622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICg4H04XHQ%2FNmigv6DSN3L2957OzYUuTQ42TzaPeedcXAiEAm2O5KH%2BUq5Ogr0BD4Ri4PRUjqMrX6KQStuHU%2BFm0Td8q%2FwMIThAAGgw2Mzc0MjMxODM4MDUiDAc%2BVh%2FRtzTJQwbkaCrcA56%2FjzZLehHCj4VAm%2FyRWvfWcIiOZFtbKjJCTYkvwRTVN%2B2mJJK1cIKWQY5%2Bg7XsMWqjX7IrgYXyuJ2%2B69gzA05AXX71KDkx62Wca2BG1gY8fD7FK3%2FmtKPpmsqOZaGT%2FbU%2BtRzX7kfeQG9kfPDX02nzn4E1SUFWiDmNF%2FDpoj4NkYGbJRL9gPgDsugGP5jYTlprmQ%2BdfvMonTUe7ruK%2Bu32F10zYQZbgDW1oWX6%2FITuu6DcIOd1Uc6EtXVVu3wJVjc1a8YhI6F3dIh9seTBS3GC2oK%2BTHzA3DKZivs1Tdi9L8X%2BZIrl93pfyv%2FGmX68d795fG8sRhV3idNUdigXNSbNMEInuOLKulskeqTYyOF8%2F%2Fjww8F72ndfNEg4Lk3BKXc9n9v0jXPl8dcr9km0oTD2FIgjFmQtbVMKeYcJRFR7RS1fEaZrweOdHKw%2B0IkOYq%2BUGTCV2o9e7onBrBHZvYMsy38n1HhN2WdK8xR7OnVMCK98gNYHsZG%2F6u0Rh0Z42Oe9MgKsMMXHUC1bKr0DdxCaQLf5wvFsKqEIcWFYUPaS7FNUgxaBoHUUN%2FK8pN4UaqZk2ZTUvV9UEtllPiUyubXpYVDhG0vHZ41iDA91k3MyRIoV3zgus9zyzUXLMLD2y9AGOqUBAo2Bi9QSHan1YOLeZz7G4ROc1WSe%2BIz3thyERD0A3CkNCC21SHdMwsoNHjK6VIb7N8CZjIJQYAgMRHwpJf2rqXE1gNPuKOYXvbXoGBU1ukrq2URfMuixbMd5Vgd5Tk0FdEny4VE4DWJwY0XXQs5CaeIbX4IRaHKQiBPjYGZtJm0jdLPnBMeYj8jEL0MAjIx76HG4BsA1%2FFbpyLVmWZFozDswoZYU&X-Amz-Signature=1251f647d33365daaa7e70b4c93ac9c7a58e277712ea5297b76e4e82ba8c4f38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
