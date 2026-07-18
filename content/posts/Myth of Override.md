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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HHF5NF6%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T105549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn4qK6pVNvwV8htM8%2FKq5emEfX8TqSD23B4fcTYiUS1gIhALAffuU%2FeXGzecLeh7txCdTKg9AkGdSVcsD1YG2nCqmHKv8DCHMQABoMNjM3NDIzMTgzODA1IgyxShpCXctaIQ4%2B3VUq3AOpquh7RfSGDCX%2FjpjbRgWFEDtps5cyOx1Xf7y4Ovg5REl0df6Blqj12hFRwbHwB%2F2RjVYlqFlUURO7KQpgfUE%2FaGWVaQR34C2wmKe5vM2MV4Q6t36fy2HLRemsDwbrKMtQ484QwJsoiBE%2FgrIoNrmx9OEaA99LDuMjORJuALvNH2Zyr%2FE7h7Rg4jkGUBi0QyjAZdlzKY7uXwUJHS7CKqLGVTvqiP3GWPPmOVyKUEUI5fqx9P6cXUiwX%2BDLO8iomPs%2F859OVgNvglN%2FW1%2Foen1XSD%2FxBAXwrn7UoFM1ESGl7F4EWSPaDRXsAjV0q9zKFSOqy10bA6c9sF6gigjc2w8R1oMl2ko947YhoapDg7EIfub9wImEQGXB7BGxynOTtbH7gPGC6jDOnr1u6TrdSaUl9CpdWlOrR9enLcwJ0gbwPygd%2BgiMerTyrcK3i%2Bi33jlB2T9G8qcNlpwQ%2BEWL9rgSpIHSUFs1NsjhPQcUJDyvHvAuCj46bhU0hm1nlawAdZOXzrZDDeD1KorGZp%2FkK2APwIfG6LhabcxiZUbn7W0BWPGvW2REooFBpj3ARg0BkIAuJK3TM0uHCkvmH0KHBWW%2F8iLyoLWYSTPm%2FOqa0l76ebhl8nBi2MJKnOLnWDC0o%2B3SBjqkAaoqp7NOLCVQeLUJqwzoPdSdjQVLw3bJlEOhnqPlvj1vGHYjSl2gwTwfYbezEtbjEySIPMisyYP%2FXXh%2BFqS2djDEI23uZ5loFyAApsKVMwf4d%2BQude8NNOnEOTaXpaHjq9gstrTSmGhTEcHGfHyXqaunBmaYhirSNFBVH3jzbl%2BnycHuxITgKoKjFrosLY%2FejMgy6Tw%2BaZ98TUbFBpUCADOBVG5m&X-Amz-Signature=fa8867707c360534c5d60a68ed29c71e1df03d5e41e93a3589faa001e73b24b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HHF5NF6%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T105549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn4qK6pVNvwV8htM8%2FKq5emEfX8TqSD23B4fcTYiUS1gIhALAffuU%2FeXGzecLeh7txCdTKg9AkGdSVcsD1YG2nCqmHKv8DCHMQABoMNjM3NDIzMTgzODA1IgyxShpCXctaIQ4%2B3VUq3AOpquh7RfSGDCX%2FjpjbRgWFEDtps5cyOx1Xf7y4Ovg5REl0df6Blqj12hFRwbHwB%2F2RjVYlqFlUURO7KQpgfUE%2FaGWVaQR34C2wmKe5vM2MV4Q6t36fy2HLRemsDwbrKMtQ484QwJsoiBE%2FgrIoNrmx9OEaA99LDuMjORJuALvNH2Zyr%2FE7h7Rg4jkGUBi0QyjAZdlzKY7uXwUJHS7CKqLGVTvqiP3GWPPmOVyKUEUI5fqx9P6cXUiwX%2BDLO8iomPs%2F859OVgNvglN%2FW1%2Foen1XSD%2FxBAXwrn7UoFM1ESGl7F4EWSPaDRXsAjV0q9zKFSOqy10bA6c9sF6gigjc2w8R1oMl2ko947YhoapDg7EIfub9wImEQGXB7BGxynOTtbH7gPGC6jDOnr1u6TrdSaUl9CpdWlOrR9enLcwJ0gbwPygd%2BgiMerTyrcK3i%2Bi33jlB2T9G8qcNlpwQ%2BEWL9rgSpIHSUFs1NsjhPQcUJDyvHvAuCj46bhU0hm1nlawAdZOXzrZDDeD1KorGZp%2FkK2APwIfG6LhabcxiZUbn7W0BWPGvW2REooFBpj3ARg0BkIAuJK3TM0uHCkvmH0KHBWW%2F8iLyoLWYSTPm%2FOqa0l76ebhl8nBi2MJKnOLnWDC0o%2B3SBjqkAaoqp7NOLCVQeLUJqwzoPdSdjQVLw3bJlEOhnqPlvj1vGHYjSl2gwTwfYbezEtbjEySIPMisyYP%2FXXh%2BFqS2djDEI23uZ5loFyAApsKVMwf4d%2BQude8NNOnEOTaXpaHjq9gstrTSmGhTEcHGfHyXqaunBmaYhirSNFBVH3jzbl%2BnycHuxITgKoKjFrosLY%2FejMgy6Tw%2BaZ98TUbFBpUCADOBVG5m&X-Amz-Signature=1a9b37c5c2d0568d5ac512d05a7f3f66a28a0cc07def25118c36a775440a1bd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
