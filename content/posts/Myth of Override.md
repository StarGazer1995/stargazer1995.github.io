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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBBCSK2%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T124829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCx8nRf%2BrtehJhLS%2FY%2B0gI847JjWRSUTO321uiIiq4qNQIhAOEUKwRWXVUQWS8XXbRwkVKxCKUdw8pIF5iyfYPo1fOiKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxIn0d6HGpor%2BpPcGgq3AM98X8NqyEEsGeqBPzo1liH%2B8ASyZzYOyxdsR6EQ9Zdlnvy7lKnCGWUOT22SxK3AC7cuvfbsgTCLTEhrNhbVKFIabRg1lyTfDA0Mn1E6sdjKRaAv5l%2Bho3n%2BSPPk38aYM1niwQM9dEvB%2Fs8IBO0pFR%2BVeNbdMDgYgCGLN%2Ffa0svfzpTgPQVYo1LK%2FAeTmp9OH%2Ft5vtGa5hhG53osyylfHowZ6IA2mXXpJJtNahTiMgy1UOzs3xKVojOMkJoVM1OCd9VjnhE29lLgE%2FzfmXybLRDDnbrA4OfUi%2FHfFS%2FU%2BmcZh8HpZh7SDezjbtgjmYxgOF27lgnYwLX2jiUtz8PaebJDkf5KgH2pZe3t7%2BTz6jN4pu5XQAArbPJJLzehIB2excVJtBRQuK6%2Bpgfwdw2fTHIi3cKFy2Pfaq6qYgGSEsgYM9bX9YBiAELLbT8EIJ6buwyaxMRCoG6afcn7k8pdA%2FSpITyeoKL%2BiAFy6QgkTUhzsu3XzQx6MtSCBogLSuJj3GcPD%2BBfQumo2%2Bz%2Fvllx1ICw%2F440p%2BS9hTJlmodcmYwbStwqzP6we43zXsRifsV9%2BaS1JMoqOwuvqD9Rt4EAXtNCX%2BRbIlCFw08fc9asbRKc8RxL4pysQnc%2BxCW2jDXosjWBjqkAfEGjAp7NQjY7FW490xiSXW8o3TqoAzrt6l8bIcs%2FrBZXTC4e%2BfeQRc3vHPt9jtUXbvRNKYsX7KeXoKjf6IwUBe%2Bakk5c2NwgmuHL84S%2Be%2B12vLkLqDy6PYe8qR2DtlLVUikTM4YODgdipENi5xuL2Ipof8P4vApwfGoadIBNf4yScgqMBP%2FnKj81AkmvO95yVdVsSJgY0gf%2Fv4Ot8jfswi8coX1&X-Amz-Signature=56926da1e6d9b70802fb97dbb1cf5ae05c2444fdbc8a339d28dfdfb7e508f20f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBBCSK2%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T124829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCx8nRf%2BrtehJhLS%2FY%2B0gI847JjWRSUTO321uiIiq4qNQIhAOEUKwRWXVUQWS8XXbRwkVKxCKUdw8pIF5iyfYPo1fOiKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxIn0d6HGpor%2BpPcGgq3AM98X8NqyEEsGeqBPzo1liH%2B8ASyZzYOyxdsR6EQ9Zdlnvy7lKnCGWUOT22SxK3AC7cuvfbsgTCLTEhrNhbVKFIabRg1lyTfDA0Mn1E6sdjKRaAv5l%2Bho3n%2BSPPk38aYM1niwQM9dEvB%2Fs8IBO0pFR%2BVeNbdMDgYgCGLN%2Ffa0svfzpTgPQVYo1LK%2FAeTmp9OH%2Ft5vtGa5hhG53osyylfHowZ6IA2mXXpJJtNahTiMgy1UOzs3xKVojOMkJoVM1OCd9VjnhE29lLgE%2FzfmXybLRDDnbrA4OfUi%2FHfFS%2FU%2BmcZh8HpZh7SDezjbtgjmYxgOF27lgnYwLX2jiUtz8PaebJDkf5KgH2pZe3t7%2BTz6jN4pu5XQAArbPJJLzehIB2excVJtBRQuK6%2Bpgfwdw2fTHIi3cKFy2Pfaq6qYgGSEsgYM9bX9YBiAELLbT8EIJ6buwyaxMRCoG6afcn7k8pdA%2FSpITyeoKL%2BiAFy6QgkTUhzsu3XzQx6MtSCBogLSuJj3GcPD%2BBfQumo2%2Bz%2Fvllx1ICw%2F440p%2BS9hTJlmodcmYwbStwqzP6we43zXsRifsV9%2BaS1JMoqOwuvqD9Rt4EAXtNCX%2BRbIlCFw08fc9asbRKc8RxL4pysQnc%2BxCW2jDXosjWBjqkAfEGjAp7NQjY7FW490xiSXW8o3TqoAzrt6l8bIcs%2FrBZXTC4e%2BfeQRc3vHPt9jtUXbvRNKYsX7KeXoKjf6IwUBe%2Bakk5c2NwgmuHL84S%2Be%2B12vLkLqDy6PYe8qR2DtlLVUikTM4YODgdipENi5xuL2Ipof8P4vApwfGoadIBNf4yScgqMBP%2FnKj81AkmvO95yVdVsSJgY0gf%2Fv4Ot8jfswi8coX1&X-Amz-Signature=79ed84a90fed3078d5826b6502380fca8b3c27676455743013371401ffb0b200&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
