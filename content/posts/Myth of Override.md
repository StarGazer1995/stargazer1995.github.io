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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STW2RVDX%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T132649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQCoiygflSCkq%2BTNEeBNX9Mo2wNwPp7dq3N5QJMa76kYcAIhAKyXNAmC%2F8zJyG79%2F9OEEKmDElrIya1im08FGEUgezQbKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKT9Z8B3SNW12NWn0q3ANdEGpg4NJJRXrNec4m2rzyNi1k8OMJbPU40o6zlDiVRt%2BIUVhRIli00YvbI2RPH%2BUMn4PakXol2INWPcVkl2zzXid%2BEi%2BDmFFOCXVkh26WB4IuXj1Ysb7I0ZNhI%2F%2FMZQEhB0q7kyXCwSL9raLptluxJVUBE7F%2Fu7am8sSis1jCZ6q2M0DaRq56vxJ392UUK6Cv5j9jLTw8uuI8g3Z3iQeSQRuNf0irqL5dxYaSJymdGwwrj3GSmPyLBYVRJorcCuHvhraZZNde2gHJNQ%2BFoZiSfgF%2BKMe%2Bn6st60HDlKwRIAkBsIATwOAVMs6K9p0ZIB04mNtua%2FtF%2FtxX4DZmR0fpI%2FnzXI6iymxGQp3hcACV8JBvJiLTBnM%2Fu2kHW5KUt2XBZfQhghR97fw41mu7I3n%2BCyQIbZl%2B6TvVyjBZJsvz9FEbxnsPR54yHTTVu3IRKa5BRnCcyOqbjcXusgXot4TP%2Fhh8U2ofW4BzUGbgo8XfEzGrqC5z8wBW8uW42ny%2BFoCnCiNjk7DfECFhDmWeM7L%2FGvSmj%2Fx88fgprTQJTVXEXBHcNOTw3hPLZbqMtD5vjNi16MpaHbHZukAHQcy3M%2FI6UHHBGuEwsLF1kpDNSpEbZkFyMlv0dojW6PrmtTDwxZnSBjqkAV%2B8KwWQX%2BbpJo6RbHb%2BeMEqPbsCy8fAqUDmGTVkLyRDpwJ%2FzuPXHHgE1hVOstiVF1iizZ1gvT%2FGd88O0VbL4bZq31%2F758P%2FcnnVb%2BSZzfEQ2pt5ZjrAZMHZfW3eP0h1IFv4yLQJJIcQQWXSe4ap4M2ISJvG0tqLvaA5fzd1AcO5r6iHlZVt1FuECVSIV5o%2FQdmfcu8Kpv5AUjTeAiQMOF60Qo3C&X-Amz-Signature=3add03ef864fcc94b1d3bb66f6fc4f4fdb30862a472ac4a31147bbedef9381cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STW2RVDX%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T132649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJIMEYCIQCoiygflSCkq%2BTNEeBNX9Mo2wNwPp7dq3N5QJMa76kYcAIhAKyXNAmC%2F8zJyG79%2F9OEEKmDElrIya1im08FGEUgezQbKogECPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKT9Z8B3SNW12NWn0q3ANdEGpg4NJJRXrNec4m2rzyNi1k8OMJbPU40o6zlDiVRt%2BIUVhRIli00YvbI2RPH%2BUMn4PakXol2INWPcVkl2zzXid%2BEi%2BDmFFOCXVkh26WB4IuXj1Ysb7I0ZNhI%2F%2FMZQEhB0q7kyXCwSL9raLptluxJVUBE7F%2Fu7am8sSis1jCZ6q2M0DaRq56vxJ392UUK6Cv5j9jLTw8uuI8g3Z3iQeSQRuNf0irqL5dxYaSJymdGwwrj3GSmPyLBYVRJorcCuHvhraZZNde2gHJNQ%2BFoZiSfgF%2BKMe%2Bn6st60HDlKwRIAkBsIATwOAVMs6K9p0ZIB04mNtua%2FtF%2FtxX4DZmR0fpI%2FnzXI6iymxGQp3hcACV8JBvJiLTBnM%2Fu2kHW5KUt2XBZfQhghR97fw41mu7I3n%2BCyQIbZl%2B6TvVyjBZJsvz9FEbxnsPR54yHTTVu3IRKa5BRnCcyOqbjcXusgXot4TP%2Fhh8U2ofW4BzUGbgo8XfEzGrqC5z8wBW8uW42ny%2BFoCnCiNjk7DfECFhDmWeM7L%2FGvSmj%2Fx88fgprTQJTVXEXBHcNOTw3hPLZbqMtD5vjNi16MpaHbHZukAHQcy3M%2FI6UHHBGuEwsLF1kpDNSpEbZkFyMlv0dojW6PrmtTDwxZnSBjqkAV%2B8KwWQX%2BbpJo6RbHb%2BeMEqPbsCy8fAqUDmGTVkLyRDpwJ%2FzuPXHHgE1hVOstiVF1iizZ1gvT%2FGd88O0VbL4bZq31%2F758P%2FcnnVb%2BSZzfEQ2pt5ZjrAZMHZfW3eP0h1IFv4yLQJJIcQQWXSe4ap4M2ISJvG0tqLvaA5fzd1AcO5r6iHlZVt1FuECVSIV5o%2FQdmfcu8Kpv5AUjTeAiQMOF60Qo3C&X-Amz-Signature=a71a3134e47c7112ec039df9ac04d1d249fb92ef2bc0f04f6537df68d8335ab3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
