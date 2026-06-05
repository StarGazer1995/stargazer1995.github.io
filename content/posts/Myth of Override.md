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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI6GFVCT%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T174626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgvl7xkRwlR0RkgOhVE9iLK60WhUJ8wn7vl2pUmwcqfAiBrWzB1j5itIg59O2wIqm%2FUt%2FchZtgDQlcWX1u%2Bc5NZOyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMG8qQnxE35r4vrLhAKtwDLjWNwvdHgwxxR2Gxtr1bIZMhmxkf6oMj0q62yGSPp%2BR5HnbtUBAIdh3itSVmLRORv3wFwGQyPMWPefKKD6e5EMn7gfG6KIunYDJF%2BqcpUr042b07LGckn8Nf9nH8iNr9zh5iQfbPFBx1YnQa1Whtgp42QPXMLwi6WUofT1ARZW%2BVT4AFnepheeCOGOIRyQMqagCmyuSLVyBIqD01EafuWPwsN1Mmm7xgRCW2KsBTxEU%2F8AwOtOvaiE%2BNg4A22cvn11f%2Bbo%2FpvRBJrZ0za6fHpXwZkyT%2F0RR%2BZXc%2Beket4VfkT1a6vnJZH7AuvOpTwr3bEBdwcM9SsDUvN6W8%2BZGYj65WJSkhVZ5Cjl%2FLjCuWiRjaJOayzz7AG9vBf30LajzJn59B28%2BaGgh%2Bk20McpoAmybbmbNmCFumSLukbDtdhQqgFpFl0XJMlsCZYjJ5UG9jndOgoukK0uAF%2FnEQYpVeTutkgR4OM5fX%2B0%2BRawISGbZ9aH8sNgXNi%2Brb2mA8zTZNJ9mvuIf9PrElfJ25PjPSLFTC4I4dj9tcjTwvFssZi7vihTARff7la%2BFesQO5NdIYwEDkqcTu2oGlOPDC7iJweVqPkcV%2FsccMpSx72%2BA%2BXgdnHN%2BiTFiZ0XHGsHcwxe2L0QY6pgE7FfgBCNGhdRD0FaZ0KBfYoAG7J2B2838rDT9d7PGGa4QTYhCRFGCGT80sKJCXiDPobOvP16UdgJniyejOMTJ3HUPK4En5Oo5yvtGMrq9mIkxo8rtlz7f%2FqYXGYs7UoVteX4RobX3L%2B6xRVTez9Esd63ikbPEoWkLN1814XzrhcUk7D5KMB%2FaA%2B%2BScWR6Q3OhssdHth9sR8ULoRbxH5bOJW9TyfbFy&X-Amz-Signature=d665495adc29a1121fba9eb0230b0f597a86e7cd3f64c04ec7972029f0be7f63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI6GFVCT%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T174626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgvl7xkRwlR0RkgOhVE9iLK60WhUJ8wn7vl2pUmwcqfAiBrWzB1j5itIg59O2wIqm%2FUt%2FchZtgDQlcWX1u%2Bc5NZOyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMG8qQnxE35r4vrLhAKtwDLjWNwvdHgwxxR2Gxtr1bIZMhmxkf6oMj0q62yGSPp%2BR5HnbtUBAIdh3itSVmLRORv3wFwGQyPMWPefKKD6e5EMn7gfG6KIunYDJF%2BqcpUr042b07LGckn8Nf9nH8iNr9zh5iQfbPFBx1YnQa1Whtgp42QPXMLwi6WUofT1ARZW%2BVT4AFnepheeCOGOIRyQMqagCmyuSLVyBIqD01EafuWPwsN1Mmm7xgRCW2KsBTxEU%2F8AwOtOvaiE%2BNg4A22cvn11f%2Bbo%2FpvRBJrZ0za6fHpXwZkyT%2F0RR%2BZXc%2Beket4VfkT1a6vnJZH7AuvOpTwr3bEBdwcM9SsDUvN6W8%2BZGYj65WJSkhVZ5Cjl%2FLjCuWiRjaJOayzz7AG9vBf30LajzJn59B28%2BaGgh%2Bk20McpoAmybbmbNmCFumSLukbDtdhQqgFpFl0XJMlsCZYjJ5UG9jndOgoukK0uAF%2FnEQYpVeTutkgR4OM5fX%2B0%2BRawISGbZ9aH8sNgXNi%2Brb2mA8zTZNJ9mvuIf9PrElfJ25PjPSLFTC4I4dj9tcjTwvFssZi7vihTARff7la%2BFesQO5NdIYwEDkqcTu2oGlOPDC7iJweVqPkcV%2FsccMpSx72%2BA%2BXgdnHN%2BiTFiZ0XHGsHcwxe2L0QY6pgE7FfgBCNGhdRD0FaZ0KBfYoAG7J2B2838rDT9d7PGGa4QTYhCRFGCGT80sKJCXiDPobOvP16UdgJniyejOMTJ3HUPK4En5Oo5yvtGMrq9mIkxo8rtlz7f%2FqYXGYs7UoVteX4RobX3L%2B6xRVTez9Esd63ikbPEoWkLN1814XzrhcUk7D5KMB%2FaA%2B%2BScWR6Q3OhssdHth9sR8ULoRbxH5bOJW9TyfbFy&X-Amz-Signature=5dc26ac96916d47a09184a06e805c181c58f2755120fb7d5ec09d4350cc91194&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
