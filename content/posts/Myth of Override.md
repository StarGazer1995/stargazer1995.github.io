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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYVCLQV%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T014800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDGCQdRi7dlpYHGbae6%2BGPYqK9FNrdI%2Fgv1p7hwkFhjaAIgEKFhSTc3oErqTi1OdFsYbMG6Msw8%2BFMEQz0bwq%2FKFXYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOoH4rqYszCwA8UhiircA5S4FdFc0as5aOuN8YQ%2Fx438Aa7iwM1yrgYixRBGU7xAv9Mh5lkWqqQ%2BW%2FdIeA7YqZC%2FxMCQEeVek2BAr9XuXDk3mnWjLYbJxETtUgmdtM2vpHE%2BsxljtFw4OYkk4iCu9DycaJUMfy7MkA0jrsZjmlg1ptrccP4FNUNKPb1AClqqlEDVmcDWyH%2BZf5GMTDYtoOT9X6j5kplgYZaC6T5uC5mja250z1g34InTSCy7qj5872wYBRW1J1OjDW9vraRYOrV9xwfZ4b41WW10GgFxSFOBNfdK5nf7Cw5%2F90ozPAXvuBhuC2n7RldXDnm0zDVYSlRjLMMKoVgSURTSebudID%2BDMZCENSyrhQWL5ly4SzvzPpAk8rdcDNcs4cO3qJBwvNqQVZTKHBeo1PmBkU%2FHcd%2FcRxdF8kHs6R6qPjyuvMkjAwfx%2BBS7MMySSEezME1xMfw3ioFpvly2VkQMazq4RRHJPuy1gFfopTajdChKPDLNKMvgxGN30FWhomyWFe2IhTzs56uOK%2Bv%2BjUqBMh%2FYQMG1w%2FmauYa1X9Mwqvu1LvgUxyYJnlEsyIHipeQggk8ZsBD6Z3icoC1%2FqI4%2BQwt1fSKrSW6mBnvo%2FCs20uPOQCZ4mLW2OS3RzGnf6LgrMKLB%2F88GOqUByBo9I7QAxesemsVfj8o1DVg59nBC0InbZ1luptdEzMiIChhZneCdaY1fsGH3VrEZKojzUXG4NMcKuNBHoFL%2FpAGKx4P4w5TbgstHUgWyM%2BRWw1DOvfHzuWDux0xPobV2zQvzPrcr5hwerfaexux7HErq48BXzXJuRsGzWYWg46UCarNhULdSuRcdXmsCT%2Fm4XJVfMWW2Ao8nSBsruUSlN0swoYb1&X-Amz-Signature=0c1fef1a526cbac1bd13aae15e3e25d6524ccff1a3ccbea971c451c60e0ad536&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYVCLQV%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T014800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDGCQdRi7dlpYHGbae6%2BGPYqK9FNrdI%2Fgv1p7hwkFhjaAIgEKFhSTc3oErqTi1OdFsYbMG6Msw8%2BFMEQz0bwq%2FKFXYqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOoH4rqYszCwA8UhiircA5S4FdFc0as5aOuN8YQ%2Fx438Aa7iwM1yrgYixRBGU7xAv9Mh5lkWqqQ%2BW%2FdIeA7YqZC%2FxMCQEeVek2BAr9XuXDk3mnWjLYbJxETtUgmdtM2vpHE%2BsxljtFw4OYkk4iCu9DycaJUMfy7MkA0jrsZjmlg1ptrccP4FNUNKPb1AClqqlEDVmcDWyH%2BZf5GMTDYtoOT9X6j5kplgYZaC6T5uC5mja250z1g34InTSCy7qj5872wYBRW1J1OjDW9vraRYOrV9xwfZ4b41WW10GgFxSFOBNfdK5nf7Cw5%2F90ozPAXvuBhuC2n7RldXDnm0zDVYSlRjLMMKoVgSURTSebudID%2BDMZCENSyrhQWL5ly4SzvzPpAk8rdcDNcs4cO3qJBwvNqQVZTKHBeo1PmBkU%2FHcd%2FcRxdF8kHs6R6qPjyuvMkjAwfx%2BBS7MMySSEezME1xMfw3ioFpvly2VkQMazq4RRHJPuy1gFfopTajdChKPDLNKMvgxGN30FWhomyWFe2IhTzs56uOK%2Bv%2BjUqBMh%2FYQMG1w%2FmauYa1X9Mwqvu1LvgUxyYJnlEsyIHipeQggk8ZsBD6Z3icoC1%2FqI4%2BQwt1fSKrSW6mBnvo%2FCs20uPOQCZ4mLW2OS3RzGnf6LgrMKLB%2F88GOqUByBo9I7QAxesemsVfj8o1DVg59nBC0InbZ1luptdEzMiIChhZneCdaY1fsGH3VrEZKojzUXG4NMcKuNBHoFL%2FpAGKx4P4w5TbgstHUgWyM%2BRWw1DOvfHzuWDux0xPobV2zQvzPrcr5hwerfaexux7HErq48BXzXJuRsGzWYWg46UCarNhULdSuRcdXmsCT%2Fm4XJVfMWW2Ao8nSBsruUSlN0swoYb1&X-Amz-Signature=f76efe47f4cdbdd526e87a314eb62e6e536a973b852efc9fac916dca99fbc7ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
