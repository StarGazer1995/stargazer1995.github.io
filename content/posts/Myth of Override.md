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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626ZES7IH%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T162054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJJPaquAW%2BA5OxqEmsx3hE3rbZuOkFCvS6wvdSwseamwIgPhW04%2Fl%2B5FZFYQSYBhoq9QuQJcjs82wgjIOYAwbw2GEqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL2Vk7d3mwOGN4RH9yrcA9L5Gh%2B6xU44rz5JONHOjXzh5b8Nc1nwLy8G9ll%2BbB%2BC4%2F0zM4BkclHDXPZ5Fj3adUfELVTU7zHT%2FiE29tLOdvvhBcr%2FZV324I4AkA2ob3W3SlTsCkSbRGnFRZyXtULI121JBR2XvQ5P81SgnLt193K5%2BTZH%2BAK5xbMIZ1h7M4Y0IQ0AOsF63F6zTdYRWNPYfDmD6OajkfiOWvPXrm0jMvxETRQo3USnqvhtYETVQH2g1aOV%2BBoZFGmlhQiyWprTovL6XbVv0AhUjMHC6BRXqRJmvgolxmjrltfiYBM1Vb9H8cN%2FWTsFD20LwUjw1KidVsGlrTwDo6IBleyCZ2oJJo3N5tjAvEmL9qFWPD6nQi90LLOGa4ZUUqrOzy5SxFO3RSly8rvEV%2FSVWhBaJ%2F2uYFXTZVnrxUQWPGzN7vHDCGWYZM0Q2p8lJ9Mx8NgbjJtEqLrZD261gqN2Qhlq8EN35m1c72K5LYZGsgjOO%2Ff%2BMdpmBTu3zEJFfQfCdNDyJhWnBlv3uPZVQvbum7mrIzNGtt2UzzYiRT78Fw0n0HhJxWLwMsDjeWhMAKWe2MjoaAmxFuANpWMWcIL57cyPKVdw1minUZayd5qSJrhzRhuHLbvoRgrnW5M7Z597gXejMLvD4tMGOqUBzWrdYxDS%2BF6wkdjwn6knbKeqbt935BrabVBuvzC0wlz1l8zeRcJ1wJcYiWy5swlWTwEHIddoO%2FFcg65LjVv561T9UlyDebQMSj%2F%2F6GQr5xJynU49Kd8BK7u3sm%2BpS63i7ulEr4yjASIVSD5z4itHn1odH9fo2WiKBIObSHC81CZxebR1gRMRkYIHV68cLS2pKCRMxRvitUpT90fhf%2BvPJ652%2BY8e&X-Amz-Signature=5093a352d55e5fa716371b7dd9f64cbb22263b57befcf5e0f5e333df1441fc4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626ZES7IH%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T162054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJJPaquAW%2BA5OxqEmsx3hE3rbZuOkFCvS6wvdSwseamwIgPhW04%2Fl%2B5FZFYQSYBhoq9QuQJcjs82wgjIOYAwbw2GEqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL2Vk7d3mwOGN4RH9yrcA9L5Gh%2B6xU44rz5JONHOjXzh5b8Nc1nwLy8G9ll%2BbB%2BC4%2F0zM4BkclHDXPZ5Fj3adUfELVTU7zHT%2FiE29tLOdvvhBcr%2FZV324I4AkA2ob3W3SlTsCkSbRGnFRZyXtULI121JBR2XvQ5P81SgnLt193K5%2BTZH%2BAK5xbMIZ1h7M4Y0IQ0AOsF63F6zTdYRWNPYfDmD6OajkfiOWvPXrm0jMvxETRQo3USnqvhtYETVQH2g1aOV%2BBoZFGmlhQiyWprTovL6XbVv0AhUjMHC6BRXqRJmvgolxmjrltfiYBM1Vb9H8cN%2FWTsFD20LwUjw1KidVsGlrTwDo6IBleyCZ2oJJo3N5tjAvEmL9qFWPD6nQi90LLOGa4ZUUqrOzy5SxFO3RSly8rvEV%2FSVWhBaJ%2F2uYFXTZVnrxUQWPGzN7vHDCGWYZM0Q2p8lJ9Mx8NgbjJtEqLrZD261gqN2Qhlq8EN35m1c72K5LYZGsgjOO%2Ff%2BMdpmBTu3zEJFfQfCdNDyJhWnBlv3uPZVQvbum7mrIzNGtt2UzzYiRT78Fw0n0HhJxWLwMsDjeWhMAKWe2MjoaAmxFuANpWMWcIL57cyPKVdw1minUZayd5qSJrhzRhuHLbvoRgrnW5M7Z597gXejMLvD4tMGOqUBzWrdYxDS%2BF6wkdjwn6knbKeqbt935BrabVBuvzC0wlz1l8zeRcJ1wJcYiWy5swlWTwEHIddoO%2FFcg65LjVv561T9UlyDebQMSj%2F%2F6GQr5xJynU49Kd8BK7u3sm%2BpS63i7ulEr4yjASIVSD5z4itHn1odH9fo2WiKBIObSHC81CZxebR1gRMRkYIHV68cLS2pKCRMxRvitUpT90fhf%2BvPJ652%2BY8e&X-Amz-Signature=b0424414eecfbf447ed93cd57349c617283dc2fde7325f22e57cec8a788d0da8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
