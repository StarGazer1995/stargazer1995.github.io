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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGEJZRSA%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T114141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC78UjZEUAOZiDo%2FOcEK2TFQiDolXq68w4ub%2BaUUJi51AIhAMZ0ac7A6fSmlmz5eYP1ptmtqPbdssRhbjcfXw9zNevzKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWee3kIk5PBf%2Fz2sMq3ANCWAwht7ONNuU0bAB4n%2BlsgagxLXPXACo6oM4N3ekn3GhvSg86erBO5MleXAXz6El0bgo5UEzGxxMubwi2di%2Bue3lQc%2FjIN4C1GeCK8M%2FU9K5incNajszBcVBlj5%2BOLq0gl2UbydA4Z8Zp4dJw8jqKiQKTzLynczbv1eE%2Fzt4wU%2F7bz8ZeYxiDp2Emt3aBX3vqx1L60wS5a6YWAFOulrBIXop%2FU2hKsosMYWP2qKGMl2pv%2FJ6ylLijNFOkrWG5%2BLZTHitoccVaRY%2FUF7jUo3aDtR1JfmhU34x2GgK5%2FlZWHo4Vc7r5fdKb2GClWt1WhgQi7ZnYSNH%2FeZ37XzlkSxBS6pWP98zZS5mFhZXDoWMI4OgJiko%2F6Cs7ScOKfn6s%2Bmevh1q%2F7OIM%2Bb5wypBzmZJGZLrfXAs3hUiV8V%2FADaJy0L38rJbJUR60J7T6PnkruIL4dSvx7jghfjfrc4FUqCfbjEt%2FVOcQoU%2FLLC7A3Wn8C1spGzfAZZAEvkBh1pGB6cOPVYr1wvREpzH27ZD63WrlO2zxR11Iy745moil9rEYrHE23RVt%2FvaTBpsv%2BS26iSw5qBmR3Jh2SleYXm%2B7zeMXJxCVwm6rPlI145sOFxyD5%2FDnRDHbjwUQ76eKQjClvrjSBjqkAVKott9LLMlNDj9pz6SEKnb%2FE2D%2BzexrmI20KlPiugY5UQRiBBsbcCcFpD%2FdV1thj%2BrV6CAhyQ4U3yHRwaQsYIPaiRacSfer3ZWS0xza7uasLRz%2BL1ExHFjevq%2BngJuTdl3Bwslla%2BzF8rfw3Lmi4kzh91hB8rNmytniW3px4qqwGopQHQSY7ub9YvRzMbuteEMRVvI%2FKS6CvhiJkwsygBg7LIVZ&X-Amz-Signature=fc61c61cebc083c03e35a2a849be0d85d1908c66148efc9fb00c44e44ebaa77f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGEJZRSA%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T114141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC78UjZEUAOZiDo%2FOcEK2TFQiDolXq68w4ub%2BaUUJi51AIhAMZ0ac7A6fSmlmz5eYP1ptmtqPbdssRhbjcfXw9zNevzKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWee3kIk5PBf%2Fz2sMq3ANCWAwht7ONNuU0bAB4n%2BlsgagxLXPXACo6oM4N3ekn3GhvSg86erBO5MleXAXz6El0bgo5UEzGxxMubwi2di%2Bue3lQc%2FjIN4C1GeCK8M%2FU9K5incNajszBcVBlj5%2BOLq0gl2UbydA4Z8Zp4dJw8jqKiQKTzLynczbv1eE%2Fzt4wU%2F7bz8ZeYxiDp2Emt3aBX3vqx1L60wS5a6YWAFOulrBIXop%2FU2hKsosMYWP2qKGMl2pv%2FJ6ylLijNFOkrWG5%2BLZTHitoccVaRY%2FUF7jUo3aDtR1JfmhU34x2GgK5%2FlZWHo4Vc7r5fdKb2GClWt1WhgQi7ZnYSNH%2FeZ37XzlkSxBS6pWP98zZS5mFhZXDoWMI4OgJiko%2F6Cs7ScOKfn6s%2Bmevh1q%2F7OIM%2Bb5wypBzmZJGZLrfXAs3hUiV8V%2FADaJy0L38rJbJUR60J7T6PnkruIL4dSvx7jghfjfrc4FUqCfbjEt%2FVOcQoU%2FLLC7A3Wn8C1spGzfAZZAEvkBh1pGB6cOPVYr1wvREpzH27ZD63WrlO2zxR11Iy745moil9rEYrHE23RVt%2FvaTBpsv%2BS26iSw5qBmR3Jh2SleYXm%2B7zeMXJxCVwm6rPlI145sOFxyD5%2FDnRDHbjwUQ76eKQjClvrjSBjqkAVKott9LLMlNDj9pz6SEKnb%2FE2D%2BzexrmI20KlPiugY5UQRiBBsbcCcFpD%2FdV1thj%2BrV6CAhyQ4U3yHRwaQsYIPaiRacSfer3ZWS0xza7uasLRz%2BL1ExHFjevq%2BngJuTdl3Bwslla%2BzF8rfw3Lmi4kzh91hB8rNmytniW3px4qqwGopQHQSY7ub9YvRzMbuteEMRVvI%2FKS6CvhiJkwsygBg7LIVZ&X-Amz-Signature=3f1e04da01bce428d3c6157d9a4f538910482fa567e1d3b3e9f7d6adc7fb4ab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
