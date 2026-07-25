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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKKITAIZ%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T203944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIBOAD4EMukfMu91Q275mO3UCkVLR9eeGgyyoMq7kw3xAAiEA8xuLHGTUmYO1J%2Fb%2FURgqX%2FNJM%2BbFPSxK4nx6k%2B4f5F4q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDCtnLOyXym1SzyUQIyrcA5BUcLJx6a2Et733MBo8fEb%2F45EXji7wwN2k2dUqGoT8JQBwLNhL4%2FFup7q6oZa9nXtQSIXbYUnZVcB4CmLlVHKiviGG15LF%2BYBB9bLaVgVYUN%2FfgtM7hFnRL2T182YQobkrP%2B0i2kQvTyyUl4i1SWmO%2FUOfG9azL34vNKuy584%2Bev91xjVZfihqgc33RirDviEDJt3wqfymtKUwJLqpHuCXPqysJcPj%2F3i61rPSg14teENov0TNmfWRB9ZMF%2FOHkf8eic7M%2FJkL9ps8VSb5l0SDNazefuC9xaDknVya6W2j29V60peOuxHBAY0MzVZMVHfnkt02g9YJt7ElJ5NsvDEzbCss1LB8CM249EEIaRUUj0DelaDfJFirC7o8h%2Fxq2Ib6%2FLHpxpTd6FAlbghvnO7Go9%2F%2FaSU9bGgD5ayQc%2BD8gwWIpLbRr%2FapU6zSxbuZX9LKSs7x5%2FTmNbNUCE2osbKLYzharklnkaHYE4XunZ0P5Gkn6RgjkFtieeKPi8XMDcUt16iqvJLBTJuoADmULz6eF7JSeGR%2BvUt0eQiuKK%2FlwX9%2FsfY4Mr3FId7Vy%2FY9vTkqJ5jZOaza5ZFfaGroYykwxCWk9dlGqsLqKdr5hcIcgRgfewwY%2BiyF8sYaMKiOlNMGOqUBNO9sA9SjbbV2l6RKkRGm2PcD%2F4241RJ4WkRUqCOwS3gn1vYMhyLR5Fzu%2BGsaHS0tBv2M6c0BUKBqDKOqN3V3oflNzqGaDmhpSKMXIXNkHTzun4g2fS714Wi4U%2Fu%2B6IrpmV5JuQqgCUUIA9wzZcW4%2BQrkV%2BhyzPizo8Jp6BsuU20BZBw6Td4cExerIMTQh0QibcRgw96hsmnT1s2zhJd8WNJUD3r%2B&X-Amz-Signature=86b7ee7b71e8db5a56a7e996fc9e0b2c7596f84099a5d3c23b293c2f1462d8a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKKITAIZ%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T203944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIBOAD4EMukfMu91Q275mO3UCkVLR9eeGgyyoMq7kw3xAAiEA8xuLHGTUmYO1J%2Fb%2FURgqX%2FNJM%2BbFPSxK4nx6k%2B4f5F4q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDCtnLOyXym1SzyUQIyrcA5BUcLJx6a2Et733MBo8fEb%2F45EXji7wwN2k2dUqGoT8JQBwLNhL4%2FFup7q6oZa9nXtQSIXbYUnZVcB4CmLlVHKiviGG15LF%2BYBB9bLaVgVYUN%2FfgtM7hFnRL2T182YQobkrP%2B0i2kQvTyyUl4i1SWmO%2FUOfG9azL34vNKuy584%2Bev91xjVZfihqgc33RirDviEDJt3wqfymtKUwJLqpHuCXPqysJcPj%2F3i61rPSg14teENov0TNmfWRB9ZMF%2FOHkf8eic7M%2FJkL9ps8VSb5l0SDNazefuC9xaDknVya6W2j29V60peOuxHBAY0MzVZMVHfnkt02g9YJt7ElJ5NsvDEzbCss1LB8CM249EEIaRUUj0DelaDfJFirC7o8h%2Fxq2Ib6%2FLHpxpTd6FAlbghvnO7Go9%2F%2FaSU9bGgD5ayQc%2BD8gwWIpLbRr%2FapU6zSxbuZX9LKSs7x5%2FTmNbNUCE2osbKLYzharklnkaHYE4XunZ0P5Gkn6RgjkFtieeKPi8XMDcUt16iqvJLBTJuoADmULz6eF7JSeGR%2BvUt0eQiuKK%2FlwX9%2FsfY4Mr3FId7Vy%2FY9vTkqJ5jZOaza5ZFfaGroYykwxCWk9dlGqsLqKdr5hcIcgRgfewwY%2BiyF8sYaMKiOlNMGOqUBNO9sA9SjbbV2l6RKkRGm2PcD%2F4241RJ4WkRUqCOwS3gn1vYMhyLR5Fzu%2BGsaHS0tBv2M6c0BUKBqDKOqN3V3oflNzqGaDmhpSKMXIXNkHTzun4g2fS714Wi4U%2Fu%2B6IrpmV5JuQqgCUUIA9wzZcW4%2BQrkV%2BhyzPizo8Jp6BsuU20BZBw6Td4cExerIMTQh0QibcRgw96hsmnT1s2zhJd8WNJUD3r%2B&X-Amz-Signature=d52538092f5e6c8a6992691e3bcae5bb172cb8f8261fb93b8b09b32b9a9eedf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
