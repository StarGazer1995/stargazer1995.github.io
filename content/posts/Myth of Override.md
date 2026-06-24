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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JK6M2Z4%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T060829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIEaPhK6h9Jlw0IRA4YcOnp3TSzwlA0HdrGP7LxErbd4dAiATnPeijaichebb0noiDL3m7WRImXQ3GjSzfDJ%2FfE06pCr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM9Vmr82sNUfUoeyCMKtwDDo1xRa5lYmOSiGqGC3y9v72%2FwRUmfaXnAbUNNGfpfw7DEDgv9bZif4BVdYdhxOeZ%2F3uMeBWEWG5hoem7oHZzZgcJqs4JjgQOJb7%2FmEdk2qRYg%2FYbBsDhh35FshUXKq2asmc7T9vxDFEnvMY5xEKxO9NbnS0I%2BFZmGO1lhscZlOq3hbhaQTxjJ6VOvhn05NIFjzSQRjZSfiz0D42ZlL%2BLz%2BwPwiHbSTlBV556ZUTOpwBXQfKgI%2B67lBpgVQcPwC64%2Foq1mHoFw4mdHozArOkqtC6dKmbb07zgtB4nEpLggnJX7FOXJ4jF59dvIx23RRiJyse%2FwFeZh8iQmUiDPXZWdzyPA%2Ft6bkE77aFupMNZ4jLycRlzXT3lnTCC1g1uxid5TPeuLqoTvWLa83rBOIgXtvfKuP46tkQIIcN1EQZvIQIHy20tWeIHQ9Q3gY42C5oD8r5T17Ya3tz2UIfqAIq4xcKbrpdggzk%2BjAJvutk7FPU34LwBi5Rz2m%2FjuXPr0V%2F%2BF1q1UDq1IFLG3A55hkYtKMVwQGCm%2B3xTwvEm7vT1n0MA3p0HUsXH7b29tZfqVf%2Bg7KM2mana2yIaCrIDnakwQ9eW5XFN%2F1aE%2FkhY2Ujlr%2F%2BTfpd2gIf%2BN1bxYj8wmqPt0QY6pgEfjS57zD5TVQwx3XVWbpp%2BfaoOvW%2FHhQJ1TcOiUMem8L4GO65pknq71THmRQSlJ%2BGqXcpzUgGFc5GeJSOfBOIlxmBtzHn3z2fyYEoIeUmSi5OjSom80Vzh6lRHX%2BdfRxNW59FpTIitqgWqXSeR3d2aHvctoInJnrGiUBbmq7xzDNEEsAYExq07Idf1li4ka9m9nWPSM8%2FD6oRDOHPJjKFdiPf3R2Y7&X-Amz-Signature=7d02f980b37b8c9596990ae629b863fd6c6b8cc5285b1cc109268c5eeb48db86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JK6M2Z4%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T060829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIEaPhK6h9Jlw0IRA4YcOnp3TSzwlA0HdrGP7LxErbd4dAiATnPeijaichebb0noiDL3m7WRImXQ3GjSzfDJ%2FfE06pCr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM9Vmr82sNUfUoeyCMKtwDDo1xRa5lYmOSiGqGC3y9v72%2FwRUmfaXnAbUNNGfpfw7DEDgv9bZif4BVdYdhxOeZ%2F3uMeBWEWG5hoem7oHZzZgcJqs4JjgQOJb7%2FmEdk2qRYg%2FYbBsDhh35FshUXKq2asmc7T9vxDFEnvMY5xEKxO9NbnS0I%2BFZmGO1lhscZlOq3hbhaQTxjJ6VOvhn05NIFjzSQRjZSfiz0D42ZlL%2BLz%2BwPwiHbSTlBV556ZUTOpwBXQfKgI%2B67lBpgVQcPwC64%2Foq1mHoFw4mdHozArOkqtC6dKmbb07zgtB4nEpLggnJX7FOXJ4jF59dvIx23RRiJyse%2FwFeZh8iQmUiDPXZWdzyPA%2Ft6bkE77aFupMNZ4jLycRlzXT3lnTCC1g1uxid5TPeuLqoTvWLa83rBOIgXtvfKuP46tkQIIcN1EQZvIQIHy20tWeIHQ9Q3gY42C5oD8r5T17Ya3tz2UIfqAIq4xcKbrpdggzk%2BjAJvutk7FPU34LwBi5Rz2m%2FjuXPr0V%2F%2BF1q1UDq1IFLG3A55hkYtKMVwQGCm%2B3xTwvEm7vT1n0MA3p0HUsXH7b29tZfqVf%2Bg7KM2mana2yIaCrIDnakwQ9eW5XFN%2F1aE%2FkhY2Ujlr%2F%2BTfpd2gIf%2BN1bxYj8wmqPt0QY6pgEfjS57zD5TVQwx3XVWbpp%2BfaoOvW%2FHhQJ1TcOiUMem8L4GO65pknq71THmRQSlJ%2BGqXcpzUgGFc5GeJSOfBOIlxmBtzHn3z2fyYEoIeUmSi5OjSom80Vzh6lRHX%2BdfRxNW59FpTIitqgWqXSeR3d2aHvctoInJnrGiUBbmq7xzDNEEsAYExq07Idf1li4ka9m9nWPSM8%2FD6oRDOHPJjKFdiPf3R2Y7&X-Amz-Signature=eab5f108263a861b5a64a7afc4013e3cf243aa563a473df006a209734243fa84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
