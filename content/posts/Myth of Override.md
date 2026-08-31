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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRRMOCR%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T075951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtA%2B%2FOuXTEStUw5u74xtCF2Ps%2FL1INgEygKc66rtCOhAIhAMr5BkQ0JbAGDGUZ9UqbKdWLZczrw%2FeTDBH2x62O0AVlKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGe0GEdx%2B2UeRvcUoq3AOkL9MqkcWInXTfhFytC76y2NX0Rt3fPrVjnPHZ1TjzFPys%2F7eXRdJLmTwq2dkb4RJW8BDnMgKZsClk0FIjcBgz92mNBnvgTzyOnp59Cx8Y1EDggBNiNcTzCBrcGk83kE0w4f0CrQ5t9vzLdWxDu99%2BdKJnzKEnYnNwwYrcPMynzxYFksRZoiexsgVVmeVAze09IDA%2Fmo94F7WhUKiPYbs8WiZR9n33%2BNwOOCV178FOvwvpyi69BWx9io3K6JfhbUrd9fByWp3kwV3tfNRhNunVk8M%2BasaliWMob1DCAgdTE36YzZPtuAK8t%2Bk8%2BJGY8aOMno%2BSmw40O7QgGKjw0OxlmGI0s1hpGX9Kam%2BjG%2FbtpWpatSjc5V%2ByhR%2BpBDL4%2FuxeDjYx9TviL6mBf%2BuFzLFNRvwzMwAkCvW%2FP38LF0QujeJgmYNTpshIiYjIhl%2BCz4RgUgX%2FpsJD1o9C%2FcXC5GR%2BeUe9eWho2ZcL4T2U9mT0Sf3MCaIw40IDImfwC5CYLfAWOKhPFIZc3vUtZgclWig5oaMvyI18PZNWejnrmps8WLHpD%2FgBA2f8JCS2JRpfcCw2RfbOXOsP2XIs0aG%2B685Hieat%2FfsKpEN3ihiyfJoKbUlASO1ttMMFv0nu0jDB0NTUBjqkAeMYJXAuAI85Kz%2Fd4TS2xXcmHN2WGGWYiRvNQzwxh465zMSjhtdrtTZcooNc7AWutVC1Z9v2paFCqU%2FH%2F%2BXzNaix%2Fjr9Dv0Qjx8Kzb008u8J6XurRdx2c73oasahn20ntnrKpsUnDcEzu%2BUTDssL8Y1lPnkYwnF%2FSAHUVWxvgpHFDkMim73AXq5LcReblqCu%2FyuLnifkxdk2MdEn2bkMggQ6gLmY&X-Amz-Signature=6974cf7130a35ec8bae1c33923f90dbbe212f40de86a434582afe13197d8dbe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BRRMOCR%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T075951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtA%2B%2FOuXTEStUw5u74xtCF2Ps%2FL1INgEygKc66rtCOhAIhAMr5BkQ0JbAGDGUZ9UqbKdWLZczrw%2FeTDBH2x62O0AVlKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGe0GEdx%2B2UeRvcUoq3AOkL9MqkcWInXTfhFytC76y2NX0Rt3fPrVjnPHZ1TjzFPys%2F7eXRdJLmTwq2dkb4RJW8BDnMgKZsClk0FIjcBgz92mNBnvgTzyOnp59Cx8Y1EDggBNiNcTzCBrcGk83kE0w4f0CrQ5t9vzLdWxDu99%2BdKJnzKEnYnNwwYrcPMynzxYFksRZoiexsgVVmeVAze09IDA%2Fmo94F7WhUKiPYbs8WiZR9n33%2BNwOOCV178FOvwvpyi69BWx9io3K6JfhbUrd9fByWp3kwV3tfNRhNunVk8M%2BasaliWMob1DCAgdTE36YzZPtuAK8t%2Bk8%2BJGY8aOMno%2BSmw40O7QgGKjw0OxlmGI0s1hpGX9Kam%2BjG%2FbtpWpatSjc5V%2ByhR%2BpBDL4%2FuxeDjYx9TviL6mBf%2BuFzLFNRvwzMwAkCvW%2FP38LF0QujeJgmYNTpshIiYjIhl%2BCz4RgUgX%2FpsJD1o9C%2FcXC5GR%2BeUe9eWho2ZcL4T2U9mT0Sf3MCaIw40IDImfwC5CYLfAWOKhPFIZc3vUtZgclWig5oaMvyI18PZNWejnrmps8WLHpD%2FgBA2f8JCS2JRpfcCw2RfbOXOsP2XIs0aG%2B685Hieat%2FfsKpEN3ihiyfJoKbUlASO1ttMMFv0nu0jDB0NTUBjqkAeMYJXAuAI85Kz%2Fd4TS2xXcmHN2WGGWYiRvNQzwxh465zMSjhtdrtTZcooNc7AWutVC1Z9v2paFCqU%2FH%2F%2BXzNaix%2Fjr9Dv0Qjx8Kzb008u8J6XurRdx2c73oasahn20ntnrKpsUnDcEzu%2BUTDssL8Y1lPnkYwnF%2FSAHUVWxvgpHFDkMim73AXq5LcReblqCu%2FyuLnifkxdk2MdEn2bkMggQ6gLmY&X-Amz-Signature=0584f6769f471bc2154da6c9f983fed2dc50131b7f2800aded4b98b8349036bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
