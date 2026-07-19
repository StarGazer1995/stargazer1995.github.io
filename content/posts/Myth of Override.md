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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665R5FVQKQ%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T144610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIACXnuIueVxp52hQ9xI4wMBt8q3R8wKdPyE5p%2FropWaDAiEA1YOuBQyrYeAaBjqqhxJt%2B5cPbEyuisA8PXIm%2BjrctTkqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPuEv3wZr558VyZdCrcAxIjG19QLkIkWNflhCW8Hj5UKZ3qXejNFgm%2FV6bsMDBa61QGX%2FJMWARK18j6dXII7UVjAUST5POk9APqXTbnvyHbNv4ZojHPHUZo9kCHeqvHBzvbRW3adX420gHmENRjQcF8ydYb%2FJRZGDqQcklL491w6vZEbTk%2FtsRP%2BeXaCZxTS3hFa0%2Blt6ExpP87WHSt9tOY%2B%2Fru8segHxyqL0ueU2%2B1x1xHPHY5lqtqNAyZo20uP9CkeM9%2FOh2NqV0lQudOlFFoqYMiWd5S77f8uU7aoI12LAiuqIbmxabV2FyEU0o8Xhfnh0kzSOWoSA5FQ5ct6DSUL0Wkdh2O0J6j89Ok1fWYMxMefEAPmUNJhKt1hvcBWTZoBRuG8I%2Bp5gFcLvLqaHoga1oSpft9mdhxw4Lr3gPAIQg7HfTadI3%2FDVCdwht%2Bltb4XNE%2BKbZ5HIdf4GQE2ei9W4QYl2DhMOuYSFQtbwRkm%2BZ7SvxKZKCldqtz5EPwenKvUkVUc69mVheQLgE74mAjzBN%2BzoW%2FwYDWlBeJ7yJqB24TilLGfH0QWlw9Qzjs0IGlM2OTlBm5y%2FLtr0rGlfe0uwqpJ5yYrGUrS6%2BpxC8wCDI2%2BlSMVZajwdDIj7RJ9avdNYxLOU%2FlpZhjMMyh89IGOqUBqsyytnm0Dzw3I7jfrEx1sKWKVoAV2EBdY182vqJe2HchHIw1c2FYb%2FZwiDni6Na8HimI0iecOhWulKIOHTSCmXzNAaQgj6IhbNdg%2FHoznDXrnDsXs9ft%2F7i4hc2TKsx66pU71Kyh%2Bm9DgFWDsYRms9fj7PL3VFMKOuU%2B8TmTQOnOHvYsGJX3UEvmZxK%2Bh1VSxoclAcpW96wTR1Sgl2ozLmI55CvB&X-Amz-Signature=49d3116d6422a4890b78c6b2e43b00bc39381ffd664a37e7ec60c37d43c6d397&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665R5FVQKQ%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T144610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIACXnuIueVxp52hQ9xI4wMBt8q3R8wKdPyE5p%2FropWaDAiEA1YOuBQyrYeAaBjqqhxJt%2B5cPbEyuisA8PXIm%2BjrctTkqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPuEv3wZr558VyZdCrcAxIjG19QLkIkWNflhCW8Hj5UKZ3qXejNFgm%2FV6bsMDBa61QGX%2FJMWARK18j6dXII7UVjAUST5POk9APqXTbnvyHbNv4ZojHPHUZo9kCHeqvHBzvbRW3adX420gHmENRjQcF8ydYb%2FJRZGDqQcklL491w6vZEbTk%2FtsRP%2BeXaCZxTS3hFa0%2Blt6ExpP87WHSt9tOY%2B%2Fru8segHxyqL0ueU2%2B1x1xHPHY5lqtqNAyZo20uP9CkeM9%2FOh2NqV0lQudOlFFoqYMiWd5S77f8uU7aoI12LAiuqIbmxabV2FyEU0o8Xhfnh0kzSOWoSA5FQ5ct6DSUL0Wkdh2O0J6j89Ok1fWYMxMefEAPmUNJhKt1hvcBWTZoBRuG8I%2Bp5gFcLvLqaHoga1oSpft9mdhxw4Lr3gPAIQg7HfTadI3%2FDVCdwht%2Bltb4XNE%2BKbZ5HIdf4GQE2ei9W4QYl2DhMOuYSFQtbwRkm%2BZ7SvxKZKCldqtz5EPwenKvUkVUc69mVheQLgE74mAjzBN%2BzoW%2FwYDWlBeJ7yJqB24TilLGfH0QWlw9Qzjs0IGlM2OTlBm5y%2FLtr0rGlfe0uwqpJ5yYrGUrS6%2BpxC8wCDI2%2BlSMVZajwdDIj7RJ9avdNYxLOU%2FlpZhjMMyh89IGOqUBqsyytnm0Dzw3I7jfrEx1sKWKVoAV2EBdY182vqJe2HchHIw1c2FYb%2FZwiDni6Na8HimI0iecOhWulKIOHTSCmXzNAaQgj6IhbNdg%2FHoznDXrnDsXs9ft%2F7i4hc2TKsx66pU71Kyh%2Bm9DgFWDsYRms9fj7PL3VFMKOuU%2B8TmTQOnOHvYsGJX3UEvmZxK%2Bh1VSxoclAcpW96wTR1Sgl2ozLmI55CvB&X-Amz-Signature=16879d58fbd5a7841f242fe74e873ff7cea30d2b92d8381964af27e295155096&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
