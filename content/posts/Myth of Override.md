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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAEIUS4M%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T135217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpxZztteIi2HfIcDZfjkPv%2Bt6meMq17CQ1XgAFaNI4twIgZ1Uuse%2B9DNJMMyEaLULG9lhU1yxKoP4dhwHO9dXMKJMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPeXJJE0UAffv2SOiircA7DbJLrjLj01Rfo57bOQ5kNauQaBDsibxQpd5vgMWgYlahE70LA9c6lGTGP4t7LqIhweebwJEC%2BSy14shN4uiSjKGwQfGYdosdQA%2Bdn1Y1gKbEubDL4ZJO6sQq0hSCi0AxJDKBbNAxKuZIktfU40EpeImXrNZvKBmsv32eVpkIX14A0b13T1eroo6NPwUb6hP091JfGtwjwi9nbKI334egbuXtCm48eTG1z0yE2ZcvW08zSzlgle9LZxUXqSl64c1mmCbJcl7ESlWXIMVCTqNkI4Ts1qXB%2FIKEUr0N4cCu1sNQ1ox4YMFo4L3YhL4Hn1FcsIrGc5iLTT2MQVAKARFEvhlALrIjzp9LmAz5toctBUVUjP7n3gf8I8waPXWIlbAybC1pndvVHk%2F4%2BhpyX4b4jd%2F7XXTf%2B0sjE2uOBP1V2xot5aORSdd0iY10XdfCnl%2BL0TRe31r474zva9oYEmoeXV5gqnw2N6IkwNr0fLpH974vF1EX123wl4wTSF2LoncMfFaA0nUf9f6ldkX8pW4YwNGCJseQalL9fw5dSW9Ns40cuKcloZ4uPrsDwFjsUSyM7ORcWzKqbt0z8o138wi0xQbjmfpik%2Fp0ykQU2qJdDzxNZxNxugbUJcMG4%2FML24jtIGOqUBs%2FwO4FsNYCc3oJfiUPVW%2BHTRqk16OYi5EZIFNfNrZ%2BlSyWxsBZWjKEjMrs5mcaBtX2E0ucuNwPkCKiAl5AYCMbBPuXLlg6DFhGnghPGoOI0S3Ga5iBu3D2rTCpmLdaWGMGcJ7pXCIdFz0JgTzRSO2DBpmOvs2U6sVx56W8KP7wP9vKtaMwIA5XdWITRBnbTsNSqDUva024M4Wjv32BTgo3fJhxl%2F&X-Amz-Signature=ef0a4ee8173dd2a795288e206e369659db8ce01c1a761732f23e3db7c5005f6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAEIUS4M%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T135217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpxZztteIi2HfIcDZfjkPv%2Bt6meMq17CQ1XgAFaNI4twIgZ1Uuse%2B9DNJMMyEaLULG9lhU1yxKoP4dhwHO9dXMKJMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPeXJJE0UAffv2SOiircA7DbJLrjLj01Rfo57bOQ5kNauQaBDsibxQpd5vgMWgYlahE70LA9c6lGTGP4t7LqIhweebwJEC%2BSy14shN4uiSjKGwQfGYdosdQA%2Bdn1Y1gKbEubDL4ZJO6sQq0hSCi0AxJDKBbNAxKuZIktfU40EpeImXrNZvKBmsv32eVpkIX14A0b13T1eroo6NPwUb6hP091JfGtwjwi9nbKI334egbuXtCm48eTG1z0yE2ZcvW08zSzlgle9LZxUXqSl64c1mmCbJcl7ESlWXIMVCTqNkI4Ts1qXB%2FIKEUr0N4cCu1sNQ1ox4YMFo4L3YhL4Hn1FcsIrGc5iLTT2MQVAKARFEvhlALrIjzp9LmAz5toctBUVUjP7n3gf8I8waPXWIlbAybC1pndvVHk%2F4%2BhpyX4b4jd%2F7XXTf%2B0sjE2uOBP1V2xot5aORSdd0iY10XdfCnl%2BL0TRe31r474zva9oYEmoeXV5gqnw2N6IkwNr0fLpH974vF1EX123wl4wTSF2LoncMfFaA0nUf9f6ldkX8pW4YwNGCJseQalL9fw5dSW9Ns40cuKcloZ4uPrsDwFjsUSyM7ORcWzKqbt0z8o138wi0xQbjmfpik%2Fp0ykQU2qJdDzxNZxNxugbUJcMG4%2FML24jtIGOqUBs%2FwO4FsNYCc3oJfiUPVW%2BHTRqk16OYi5EZIFNfNrZ%2BlSyWxsBZWjKEjMrs5mcaBtX2E0ucuNwPkCKiAl5AYCMbBPuXLlg6DFhGnghPGoOI0S3Ga5iBu3D2rTCpmLdaWGMGcJ7pXCIdFz0JgTzRSO2DBpmOvs2U6sVx56W8KP7wP9vKtaMwIA5XdWITRBnbTsNSqDUva024M4Wjv32BTgo3fJhxl%2F&X-Amz-Signature=8f1602e4a579db4113a27a53c05c7125e6cd48c866b5db35eea1a17b7aa3472e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
