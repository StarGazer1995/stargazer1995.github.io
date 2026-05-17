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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ISRAE36%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T015350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg7diJqD0gpNxGsPHlJiofnBwHRZZVjyZS3YfCk%2Fp0SAIhAIvD7uMtUGY5W54I%2FtE%2BTnYNcDSEi%2FQ%2Bh%2FevXcZQHhDfKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycPj7JrkObCLwe%2BXAq3ANxYyjXS3azb0EIX5LrrQ0WQQirL2olRX3gBJg1gZ5PlIHUdDfksrA1Wgba3dCx9dTemDfHa%2FLga9ccBszlzyfXk3PwA9pzVyAducNnEgr96e%2B88lU7oEviCVGEFEL6MUbcg3RY3GsBzimC1dEMGch%2FkbEh%2FLNpcYbJodIw5wcf28FhG8oYIVkJnxFJ8ngrymd1H9yy%2BXiu9ZdeQ93PYKOXGZdfVzZ66pFu%2BrHIiTzffR0odcSK6900mn2B1tQRunl14V%2BDftCEHMHOdXDGm9qD2pbC6ky4eQ%2FendZH8%2FExPfI26M4tb4Xc4UHOht58MG5k20tQoRoz735PKYhOjTK2H%2BoM8KQ%2BsU1yxhaadc5TRjJgsXpRIgOsFhi1OCEfMsNYplAHinbRQQII8g3pfpYpYj5XkRvMnwv03MpOxRfGEwDQLpO9ri2%2Fk%2BkxgGNzvn5Eijnz43SuJhKUD7s3PxEwy9ZLYHcmmQlMgvOuYFeV2f9if2W6P7TdnW6LCgtVykrID3KMm1%2F0d9XdYPwrrdGxviLEgfUH6i%2FHPa74tK43iFJdW%2FYyrRgvgQx4%2FaRhR1ZAG%2BqKz8ZgOkcQ%2F1lO95TUs6%2FXI3Ykl1JvSS2yvRT103wL9nZudB%2BlDZa1ejDetKPQBjqkAZtpJZLJObWs0P4G9uatvKnM8sbODVhy9v2FXR8QkyeFT1km%2BxiURXCVl10s%2Fq1rxpkRIchZcjELEOQTpxFHJR18dd3slD6XAv16u3Qldqqt9%2Btm4k9FS0LPDJIoj5al%2B0SfdprPq%2BvkLkOlEb4aHfFouh0Ox8shB5nVWHTZg8jxIjJD1f1CvhYegyQcuKq8YAIA4dSfz8JpAR6zLuyoCAarSNYz&X-Amz-Signature=935c4e428042b643896e4e4a91fef4b781c7d266815a73e9e219414530a2f783&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ISRAE36%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T015350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg7diJqD0gpNxGsPHlJiofnBwHRZZVjyZS3YfCk%2Fp0SAIhAIvD7uMtUGY5W54I%2FtE%2BTnYNcDSEi%2FQ%2Bh%2FevXcZQHhDfKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgycPj7JrkObCLwe%2BXAq3ANxYyjXS3azb0EIX5LrrQ0WQQirL2olRX3gBJg1gZ5PlIHUdDfksrA1Wgba3dCx9dTemDfHa%2FLga9ccBszlzyfXk3PwA9pzVyAducNnEgr96e%2B88lU7oEviCVGEFEL6MUbcg3RY3GsBzimC1dEMGch%2FkbEh%2FLNpcYbJodIw5wcf28FhG8oYIVkJnxFJ8ngrymd1H9yy%2BXiu9ZdeQ93PYKOXGZdfVzZ66pFu%2BrHIiTzffR0odcSK6900mn2B1tQRunl14V%2BDftCEHMHOdXDGm9qD2pbC6ky4eQ%2FendZH8%2FExPfI26M4tb4Xc4UHOht58MG5k20tQoRoz735PKYhOjTK2H%2BoM8KQ%2BsU1yxhaadc5TRjJgsXpRIgOsFhi1OCEfMsNYplAHinbRQQII8g3pfpYpYj5XkRvMnwv03MpOxRfGEwDQLpO9ri2%2Fk%2BkxgGNzvn5Eijnz43SuJhKUD7s3PxEwy9ZLYHcmmQlMgvOuYFeV2f9if2W6P7TdnW6LCgtVykrID3KMm1%2F0d9XdYPwrrdGxviLEgfUH6i%2FHPa74tK43iFJdW%2FYyrRgvgQx4%2FaRhR1ZAG%2BqKz8ZgOkcQ%2F1lO95TUs6%2FXI3Ykl1JvSS2yvRT103wL9nZudB%2BlDZa1ejDetKPQBjqkAZtpJZLJObWs0P4G9uatvKnM8sbODVhy9v2FXR8QkyeFT1km%2BxiURXCVl10s%2Fq1rxpkRIchZcjELEOQTpxFHJR18dd3slD6XAv16u3Qldqqt9%2Btm4k9FS0LPDJIoj5al%2B0SfdprPq%2BvkLkOlEb4aHfFouh0Ox8shB5nVWHTZg8jxIjJD1f1CvhYegyQcuKq8YAIA4dSfz8JpAR6zLuyoCAarSNYz&X-Amz-Signature=b38ab3bdcaa507859f792ffb4a4c0649e5077f9ccd36926cdc445f82c2e1ed80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
