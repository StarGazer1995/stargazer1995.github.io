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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZROHE2WL%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T132335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDLTyT3TuHDBdH5pi85lnqe%2BsFjQ0YLKkdb7yUpbKHF%2FQIgORlTt7AoWN1fs2UhdtHQPT7kbXQC3QMmyOXTTgXaBLIqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDONn%2BIkgfTnKi%2FyrWircA8HtT7e%2F6wphRwR9Ms6obUVwQtG42hROaUw3tbmsZP4kiJZqox%2BbLfEq992%2FhkdqsgM5Lz2W%2FW0%2BB1QZbWER4wXthNt8xSi9mqi4hLjGz0LIWZVdSwl8GlsHXqiIjnyQGZOUUkaBvZPBdbASTR53UFwi9ex1uZnE1isvmVyTD7HUMBgrSNxc7hpgItBx3fk1OWzIQe%2Fz7GvoyDpyeXfnbWAp33Gyn9drjkx0xUaNbM1g3nkm6ozQMxF9uUNS5%2FsaSGrrfap%2FX1JfphHYY9926oDyhdWF%2FVVgfSci50x2uNA1HYFNkf31d9LlKZojC1%2BwvsGIVXHmwEe68WXSmnMVGEd8WNMu5NXJZlgEdFqGbrh2aeXbbm8PEHCB4ArxZ89sUFSq02mdmAutmFqUNsH%2BE2SeULUz22LnalB%2FY8aqaQHhGHHM%2BETqe4hXeq6DoisQ8LeEspAPjpJNt3u8oY3ubiyYuWj%2BfKfNjofFmJUMOkqH5upYrFf%2F6JTy2PuusS9H98bHlBOkFDlES04sMOCiy%2Ff%2B0L2ffv10ZesHXFNBbUEUuZc5QNwdidQGXIg4tssoE706SZODbEM9EEcTFVRxklvHExGzkjRdGhSnlMqfRIGifpAfuczk51noU%2BVYMJvp2dEGOqUB%2BRADimLXYX2VbkZpQJBruHwDFvpibpkmG26%2BvamdXtOEp0cxFuECICLwu1SGtLuSqvXUB%2BeRaDwcviuw6AJuNQvoaVNUw82%2B24JCnhw1D0avylhWk4tjhFaMOjBBN6tabmsIeBiyZ7LW4ZW8DVCu0R%2FHZhCwH%2FcR8HCp3Eqpaj7S2fi1%2BFviNVLte2TyCaR746xjlEBpRo5GBiZnuE9AyXwOgFXk&X-Amz-Signature=430afd73771f8e33d3dbed35947ef4ba7db40247762f6b16e680f2aec6b661f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZROHE2WL%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T132335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDLTyT3TuHDBdH5pi85lnqe%2BsFjQ0YLKkdb7yUpbKHF%2FQIgORlTt7AoWN1fs2UhdtHQPT7kbXQC3QMmyOXTTgXaBLIqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDONn%2BIkgfTnKi%2FyrWircA8HtT7e%2F6wphRwR9Ms6obUVwQtG42hROaUw3tbmsZP4kiJZqox%2BbLfEq992%2FhkdqsgM5Lz2W%2FW0%2BB1QZbWER4wXthNt8xSi9mqi4hLjGz0LIWZVdSwl8GlsHXqiIjnyQGZOUUkaBvZPBdbASTR53UFwi9ex1uZnE1isvmVyTD7HUMBgrSNxc7hpgItBx3fk1OWzIQe%2Fz7GvoyDpyeXfnbWAp33Gyn9drjkx0xUaNbM1g3nkm6ozQMxF9uUNS5%2FsaSGrrfap%2FX1JfphHYY9926oDyhdWF%2FVVgfSci50x2uNA1HYFNkf31d9LlKZojC1%2BwvsGIVXHmwEe68WXSmnMVGEd8WNMu5NXJZlgEdFqGbrh2aeXbbm8PEHCB4ArxZ89sUFSq02mdmAutmFqUNsH%2BE2SeULUz22LnalB%2FY8aqaQHhGHHM%2BETqe4hXeq6DoisQ8LeEspAPjpJNt3u8oY3ubiyYuWj%2BfKfNjofFmJUMOkqH5upYrFf%2F6JTy2PuusS9H98bHlBOkFDlES04sMOCiy%2Ff%2B0L2ffv10ZesHXFNBbUEUuZc5QNwdidQGXIg4tssoE706SZODbEM9EEcTFVRxklvHExGzkjRdGhSnlMqfRIGifpAfuczk51noU%2BVYMJvp2dEGOqUB%2BRADimLXYX2VbkZpQJBruHwDFvpibpkmG26%2BvamdXtOEp0cxFuECICLwu1SGtLuSqvXUB%2BeRaDwcviuw6AJuNQvoaVNUw82%2B24JCnhw1D0avylhWk4tjhFaMOjBBN6tabmsIeBiyZ7LW4ZW8DVCu0R%2FHZhCwH%2FcR8HCp3Eqpaj7S2fi1%2BFviNVLte2TyCaR746xjlEBpRo5GBiZnuE9AyXwOgFXk&X-Amz-Signature=6cde8438051e731b9f35e72f0e1c3b1cd4ff83601b537ced93aed06ba5db2c44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
