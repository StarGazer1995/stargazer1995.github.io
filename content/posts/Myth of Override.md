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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWTT3JLZ%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T085415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIAG%2BTEXbYC4wBkNr1rr3VICSFlfsYZXCUHPHvmIW1VO1AiBVImJzCK78rCjHN%2FMjbBaDjWfPHkwRwh%2FSmwU6ymH74yr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMbwPsZDdg3U%2FZpdCgKtwDe8C7VU2f0wAs5SawdTtkc7YHEk15jlk2bFs9LnF9QRSgWKASqcO%2F26CVsmy69dHE8d3hNwXcLVm%2FZGpJWwGffMN5GYcohMy3UqqhQPJZ8VewJEQkB40u%2Fvz9S90F9ZgCJDOriLi5oAD7jBPiBqO4305HOqHanfJcb6O73BlxDvEf3hlBATDYUCPtB%2FK06oHHo%2BEg699MRM%2BVRnVGi8yiXhsqqaMgH8sQk6czdkiRX83CatAEexraN2yIFORuGUPlEtpfIvbEgy1eegnpP0P72acn54KTSxZ8rSvjxAC0d4bApLkTI04A%2B05MnrRvnJCwR%2BghX2xIqxZSq2qJEWnnzqjcDS%2BOcz%2F6ylSUnVN2veVGrzZPcyPxe6Wc8TS0a0bb1Bnd9AXgPFRDrGUPc3ShxmpckcsMNHBVn6%2FIlPgmWQmaPdjvuxKqzR0gKzDHd8py91zkKvxl61KZEoovuEczzsSMkr02xhVqdhINZ5Pjj01pSROLI26eNUcQvSnLmbkJiX70FwN6UDMw9xZMovVKLnseqa30eF2KBVCJwYhscF41VG4pN%2B9QGc%2FG8YxBcJv6jGVB%2FxSdSf8mQryoIkxeZAAj3tqeDw6iKLSIeY4IB3NBjXX8v74ThOXG3hMw3ILe1QY6pgEm43PuqLCu3oDzZwGHThA824VBzQL%2FqIiv0yImiQyiiP%2BVD3noELBBb8UpJh1BQnryTiVLvGgxSRq2og3R739aUDzryvlI68WBdZUbW7YqYDyPfZU8t5VSAZnyCj9mdU4kzStnRUofpALH2Ywce6jKwlS%2FYXsNt51hmVNQ%2Fd3O01RIgibGrHyWrdk8b6glvG4NBYJ8uhFk0IWe0ngVcKGM6be1Ko1V&X-Amz-Signature=6ef38cdf4c82636c342e2b3df30f67fcacb76f7ffdf8dd8646a814b9d919638a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWTT3JLZ%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T085415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIAG%2BTEXbYC4wBkNr1rr3VICSFlfsYZXCUHPHvmIW1VO1AiBVImJzCK78rCjHN%2FMjbBaDjWfPHkwRwh%2FSmwU6ymH74yr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMbwPsZDdg3U%2FZpdCgKtwDe8C7VU2f0wAs5SawdTtkc7YHEk15jlk2bFs9LnF9QRSgWKASqcO%2F26CVsmy69dHE8d3hNwXcLVm%2FZGpJWwGffMN5GYcohMy3UqqhQPJZ8VewJEQkB40u%2Fvz9S90F9ZgCJDOriLi5oAD7jBPiBqO4305HOqHanfJcb6O73BlxDvEf3hlBATDYUCPtB%2FK06oHHo%2BEg699MRM%2BVRnVGi8yiXhsqqaMgH8sQk6czdkiRX83CatAEexraN2yIFORuGUPlEtpfIvbEgy1eegnpP0P72acn54KTSxZ8rSvjxAC0d4bApLkTI04A%2B05MnrRvnJCwR%2BghX2xIqxZSq2qJEWnnzqjcDS%2BOcz%2F6ylSUnVN2veVGrzZPcyPxe6Wc8TS0a0bb1Bnd9AXgPFRDrGUPc3ShxmpckcsMNHBVn6%2FIlPgmWQmaPdjvuxKqzR0gKzDHd8py91zkKvxl61KZEoovuEczzsSMkr02xhVqdhINZ5Pjj01pSROLI26eNUcQvSnLmbkJiX70FwN6UDMw9xZMovVKLnseqa30eF2KBVCJwYhscF41VG4pN%2B9QGc%2FG8YxBcJv6jGVB%2FxSdSf8mQryoIkxeZAAj3tqeDw6iKLSIeY4IB3NBjXX8v74ThOXG3hMw3ILe1QY6pgEm43PuqLCu3oDzZwGHThA824VBzQL%2FqIiv0yImiQyiiP%2BVD3noELBBb8UpJh1BQnryTiVLvGgxSRq2og3R739aUDzryvlI68WBdZUbW7YqYDyPfZU8t5VSAZnyCj9mdU4kzStnRUofpALH2Ywce6jKwlS%2FYXsNt51hmVNQ%2Fd3O01RIgibGrHyWrdk8b6glvG4NBYJ8uhFk0IWe0ngVcKGM6be1Ko1V&X-Amz-Signature=b7ead085063e594acf5b78944b4b69dea653b16ea0224542eca288ba08e1888a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
