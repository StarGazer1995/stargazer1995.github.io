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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDVFI6AD%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T173925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDc0D1rTjRVlb3cvE1KhgpEFWtjD6cl4GPdT46kH0ByiwIhAKWwsA0Ev4iNgNjn59xNIojhzORemocDtgQB02ai6Q43Kv8DCFoQABoMNjM3NDIzMTgzODA1IgwyWf1NkxqBMg5peMcq3APDaSUeO6WMpw74iuv3JI1%2FzTtrlLoqs0RoyQpr2uLVhtqJlL29oBTCFTxSUYmjvwxQOOEaXb1wbEH%2FGcqF2%2Brp6bdEDap18NW%2BbJR18wp8qYnRlaAOk%2FmNBFxFwEMYv0oNAEX8kf2bR8276Oq24AuraVvu3LynRQ%2F40lfCx74b9JovoPbBwPi5BlSHO3KywT0Z7czjZOwwt%2FjfJtLE56gyACpzd2PyJUXVCE8vmlFuWQ2bWkD6kwU09fsBhLExZMZtWOc6HmIug4K%2B4FY%2BdLLZut6H7Q3QHa39XFRXOeeVEXBkXDJHw3txrAxc1S6Val5oj4pe4%2FPMltVbK1IqMWXyMzCANtxfzB6cRpr2LMTDM9XwOCOtGtLwdmlnP3bFJcwTFAAgqyHKpZwIhtktMX9IsinXuLdOeErs2tM8AmszMH4mYdMFG1asP9pRpcF0fIOz%2BIYWn92xDV2y0wyj18GMSJ1YWUBcHlWdE3lL4mSA61s270V4NBXZKyvpv1hrLWNsRp%2BnjAJMdzst9vPHNVZcxBwqLu4CBxruihCHMvIiUChOl0qyf43t4qIb1rvbJmnHPN87MmnyUcxudxzOH%2FdsX4tg9u4gKHLp9sIv8WMGusGoCj9KaHjm19rucjCzgYHVBjqkAbqBYt5FlUinKThiICWRT3dluYxpb7%2Fth4dSgnViKQwRqwW5mwKmKv4tl9AFYLFCKMmRMJ%2Blb1RWQi4%2FWjXA8h5aW5D8VzRG1MIciM88RAP%2B%2FILKkUmOjWb7C3Zf2wQsI0iinQqll1dtCQW5e2sz%2BJFsdhtaxvGN%2Bb3kuWEQtNmvLr7mN3fBZH3LeacJ1eEAVS97TeW%2FTmahAq7WHeAA2ikiM1fg&X-Amz-Signature=7590091fdc1173c76acd9da7ff16981beb76d438eedafe7c48579125620b10e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDVFI6AD%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T173925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDc0D1rTjRVlb3cvE1KhgpEFWtjD6cl4GPdT46kH0ByiwIhAKWwsA0Ev4iNgNjn59xNIojhzORemocDtgQB02ai6Q43Kv8DCFoQABoMNjM3NDIzMTgzODA1IgwyWf1NkxqBMg5peMcq3APDaSUeO6WMpw74iuv3JI1%2FzTtrlLoqs0RoyQpr2uLVhtqJlL29oBTCFTxSUYmjvwxQOOEaXb1wbEH%2FGcqF2%2Brp6bdEDap18NW%2BbJR18wp8qYnRlaAOk%2FmNBFxFwEMYv0oNAEX8kf2bR8276Oq24AuraVvu3LynRQ%2F40lfCx74b9JovoPbBwPi5BlSHO3KywT0Z7czjZOwwt%2FjfJtLE56gyACpzd2PyJUXVCE8vmlFuWQ2bWkD6kwU09fsBhLExZMZtWOc6HmIug4K%2B4FY%2BdLLZut6H7Q3QHa39XFRXOeeVEXBkXDJHw3txrAxc1S6Val5oj4pe4%2FPMltVbK1IqMWXyMzCANtxfzB6cRpr2LMTDM9XwOCOtGtLwdmlnP3bFJcwTFAAgqyHKpZwIhtktMX9IsinXuLdOeErs2tM8AmszMH4mYdMFG1asP9pRpcF0fIOz%2BIYWn92xDV2y0wyj18GMSJ1YWUBcHlWdE3lL4mSA61s270V4NBXZKyvpv1hrLWNsRp%2BnjAJMdzst9vPHNVZcxBwqLu4CBxruihCHMvIiUChOl0qyf43t4qIb1rvbJmnHPN87MmnyUcxudxzOH%2FdsX4tg9u4gKHLp9sIv8WMGusGoCj9KaHjm19rucjCzgYHVBjqkAbqBYt5FlUinKThiICWRT3dluYxpb7%2Fth4dSgnViKQwRqwW5mwKmKv4tl9AFYLFCKMmRMJ%2Blb1RWQi4%2FWjXA8h5aW5D8VzRG1MIciM88RAP%2B%2FILKkUmOjWb7C3Zf2wQsI0iinQqll1dtCQW5e2sz%2BJFsdhtaxvGN%2Bb3kuWEQtNmvLr7mN3fBZH3LeacJ1eEAVS97TeW%2FTmahAq7WHeAA2ikiM1fg&X-Amz-Signature=eafdda1eaf1fb55a031ddee23d4c708d39589496f27d4cebe2f7ec1ae0af02eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
