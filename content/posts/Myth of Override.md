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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEPOF7YG%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T020229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIF%2FiwXZaLm8R%2FBvjYc2CPjfkO67XJPZbw8n7So%2FVsSSaAiEA4C%2FslzdtKj693p5RQ4t5gl%2B0WMx6XvY%2BuseyagMJiiAqiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7n%2FP%2BjGFHB7rfO5ircAyJE%2FUeanne5bjHJoiy8Vj8j5gJefUREg401AGyzUZdJE9a8x2OgqXnsXlEiwAsQirw09EBhe%2Bd6y5YqEyUrRmy4X%2Bvc0m2u%2Fhtl3hHj4A9Cozx9n6eCij7upRWdCCYfX0%2BLCKHPM9MCz23CSBSOh49WqmusBJ%2BsikwEweDzQzTDz0is9%2BLO7OB4VyWitD3OXkz3JraeJ1jztyIvGAGZpQK8v5xjARg7NrWlxCceSJGdyVHlaHJ5%2B5dfdzz0AzY9l0iNPlfQ2dDiQAzkEn%2FK1u4KAycdSjX3htDgfWBXtcTjFM5PXLqVi3FI2Z0cdR844JsD0DZya%2Fyd2M%2FhzI5ltADrJ4vmRsF75IrBMkyWihG4%2Bm%2FklNbGHxs0o3fD7a%2Fr9PbGzCvO7ksGcfK8W8wkT3sufpMW34ypN6Joo31nPig%2FSO5eU15bmF3nksFu8Fmq9i43J9L5wuj9Ux%2FF1WADwAdsKm%2FbMNsiTdmI2nWavgyvA9Mj430gmxosauuG9Sr0iohKBA9jE%2FOLrEq1giyKM5a8kFTwWFK2nSrwQxBYzZAMzPoK%2BC3N4OqRltmvCgJIQ14WQhXCMtEDeQ2mLL8jIRQ690j4gQis34GB1dIlkLEMHc4vz0cPAa8ltt3VMN%2BAltIGOqUBFnEWGXMvio5oWSKcIHGEB4XHzcTZpcWevRnUYGk50ZbFck952l%2FqWRXhlLLDY%2B%2BOvBrpK6nRffYdxOl2FDtOr1epBjjMumpebGV26ZT5qKzNaUt8zmV6fDGSayzHz%2F8GnPjiBGFa8gX1bjN0rDOfsJDD%2BS0l%2Bc%2FdZkvE%2FbB%2BvcBs8KfM3N1ldZNw2H%2BnRWLSONKfgKEQTRRMJY1YJas7m6VCeOMv&X-Amz-Signature=6a35e7d20b2a081c99b69ef698f124986ee494f7ea672f53981db567766cdf9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEPOF7YG%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T020229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIF%2FiwXZaLm8R%2FBvjYc2CPjfkO67XJPZbw8n7So%2FVsSSaAiEA4C%2FslzdtKj693p5RQ4t5gl%2B0WMx6XvY%2BuseyagMJiiAqiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7n%2FP%2BjGFHB7rfO5ircAyJE%2FUeanne5bjHJoiy8Vj8j5gJefUREg401AGyzUZdJE9a8x2OgqXnsXlEiwAsQirw09EBhe%2Bd6y5YqEyUrRmy4X%2Bvc0m2u%2Fhtl3hHj4A9Cozx9n6eCij7upRWdCCYfX0%2BLCKHPM9MCz23CSBSOh49WqmusBJ%2BsikwEweDzQzTDz0is9%2BLO7OB4VyWitD3OXkz3JraeJ1jztyIvGAGZpQK8v5xjARg7NrWlxCceSJGdyVHlaHJ5%2B5dfdzz0AzY9l0iNPlfQ2dDiQAzkEn%2FK1u4KAycdSjX3htDgfWBXtcTjFM5PXLqVi3FI2Z0cdR844JsD0DZya%2Fyd2M%2FhzI5ltADrJ4vmRsF75IrBMkyWihG4%2Bm%2FklNbGHxs0o3fD7a%2Fr9PbGzCvO7ksGcfK8W8wkT3sufpMW34ypN6Joo31nPig%2FSO5eU15bmF3nksFu8Fmq9i43J9L5wuj9Ux%2FF1WADwAdsKm%2FbMNsiTdmI2nWavgyvA9Mj430gmxosauuG9Sr0iohKBA9jE%2FOLrEq1giyKM5a8kFTwWFK2nSrwQxBYzZAMzPoK%2BC3N4OqRltmvCgJIQ14WQhXCMtEDeQ2mLL8jIRQ690j4gQis34GB1dIlkLEMHc4vz0cPAa8ltt3VMN%2BAltIGOqUBFnEWGXMvio5oWSKcIHGEB4XHzcTZpcWevRnUYGk50ZbFck952l%2FqWRXhlLLDY%2B%2BOvBrpK6nRffYdxOl2FDtOr1epBjjMumpebGV26ZT5qKzNaUt8zmV6fDGSayzHz%2F8GnPjiBGFa8gX1bjN0rDOfsJDD%2BS0l%2Bc%2FdZkvE%2FbB%2BvcBs8KfM3N1ldZNw2H%2BnRWLSONKfgKEQTRRMJY1YJas7m6VCeOMv&X-Amz-Signature=8c3003ab2aef987d76000c1fac88bcc700580daacfcd6bc1fda51649263ce876&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
