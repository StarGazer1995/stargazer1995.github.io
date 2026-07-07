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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LJ5QCPT%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T015316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCB2uBp7JFrB%2FY%2BdBWOe0mMls%2Fu9oWka9Q9XQYO6OnYyQIhAMb4MqqU%2BcE%2FK37NWhn4T%2FG18A4wh4dWxoUPd2%2Fkvk1VKv8DCF4QABoMNjM3NDIzMTgzODA1Igx0UJQqX6r9iDYsrDIq3AOvKrHz0diZjXlMs4Xfx4Z7JxnsGzzQKUtwReV4W6epAlvI%2FHtm3JxlmMC05YrSbTI40xxJ9i17XVUlC3yJuvGza0t2qeHIaGJJJBSeQB0q06tKEGHCO1IkxX3DRxoZ8l5tGHglNeCL30ChhtXDkzP2tTbiOIjO6E7I3v7WM2MlAD31Kwj5vaIGv5hV%2B%2F0E2l3hCYEO5GFSDH1q1GSAtfCjaX1C59dx%2F5qy5r18y6qy9Nl%2B%2FunOHm7ug3iHj%2F9XQXtIPcw5fwA46JNY5prHY7Efv0kjUMrXq13ch03gpRf8uRxpJ%2FL4eTWie3KlgcMfhLR0jpUtDO%2BITt9XPM8jy7bTglie0rKa9ocOy7DBlejMs9KPOcv0ZVJHLvgv%2BLZCKeNs%2FCmoto9aIFw71fTnBGKMdDH%2F7Zi3M%2FDotsQJZXYPbpfVMeQva6jxmfDL6YHdG6DrChFF2ELOeErPMcuQj8Z5%2FLQQfVNkYBp0pzBnHFOqC%2BaM80rULuYcNhJ%2BaoC108YThPqaS1YOxuM9cBE98TRtUDpxrZSNMKYFpxGomH%2B46amYI1Klf4xMggJ%2BGCDfQSRu8BBTzmotAUAxWbzLocA7AK3oEeT63DPeb4jYdI405VGpnG9jnqc1T3ODlzCEr7DSBjqkAWQx2c4wq4MhgCPKrs9DGGrntOCvVQK3DyJdGXFzgv7tT5tZFJXdFANo2%2FxvpV6X4ol6VJmV03hIvrk%2FM87JCDLqKK3CN4rjAQRCySIXm2C4l3fRtajubu7iFJJgwxZMs0%2BcAT0z8r6Hrtm8Kz3cWABCr0Atxn3wKgeIdGARNF6dX4gHRCBARsHA2wJsUUUMFiBdEcRwc2PkopPswQprTHHOEekH&X-Amz-Signature=d15af94ab0d492a5b08c3a38db422cc9762e693badb9abfc9c8ec4b2e0d48806&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LJ5QCPT%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T015316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCB2uBp7JFrB%2FY%2BdBWOe0mMls%2Fu9oWka9Q9XQYO6OnYyQIhAMb4MqqU%2BcE%2FK37NWhn4T%2FG18A4wh4dWxoUPd2%2Fkvk1VKv8DCF4QABoMNjM3NDIzMTgzODA1Igx0UJQqX6r9iDYsrDIq3AOvKrHz0diZjXlMs4Xfx4Z7JxnsGzzQKUtwReV4W6epAlvI%2FHtm3JxlmMC05YrSbTI40xxJ9i17XVUlC3yJuvGza0t2qeHIaGJJJBSeQB0q06tKEGHCO1IkxX3DRxoZ8l5tGHglNeCL30ChhtXDkzP2tTbiOIjO6E7I3v7WM2MlAD31Kwj5vaIGv5hV%2B%2F0E2l3hCYEO5GFSDH1q1GSAtfCjaX1C59dx%2F5qy5r18y6qy9Nl%2B%2FunOHm7ug3iHj%2F9XQXtIPcw5fwA46JNY5prHY7Efv0kjUMrXq13ch03gpRf8uRxpJ%2FL4eTWie3KlgcMfhLR0jpUtDO%2BITt9XPM8jy7bTglie0rKa9ocOy7DBlejMs9KPOcv0ZVJHLvgv%2BLZCKeNs%2FCmoto9aIFw71fTnBGKMdDH%2F7Zi3M%2FDotsQJZXYPbpfVMeQva6jxmfDL6YHdG6DrChFF2ELOeErPMcuQj8Z5%2FLQQfVNkYBp0pzBnHFOqC%2BaM80rULuYcNhJ%2BaoC108YThPqaS1YOxuM9cBE98TRtUDpxrZSNMKYFpxGomH%2B46amYI1Klf4xMggJ%2BGCDfQSRu8BBTzmotAUAxWbzLocA7AK3oEeT63DPeb4jYdI405VGpnG9jnqc1T3ODlzCEr7DSBjqkAWQx2c4wq4MhgCPKrs9DGGrntOCvVQK3DyJdGXFzgv7tT5tZFJXdFANo2%2FxvpV6X4ol6VJmV03hIvrk%2FM87JCDLqKK3CN4rjAQRCySIXm2C4l3fRtajubu7iFJJgwxZMs0%2BcAT0z8r6Hrtm8Kz3cWABCr0Atxn3wKgeIdGARNF6dX4gHRCBARsHA2wJsUUUMFiBdEcRwc2PkopPswQprTHHOEekH&X-Amz-Signature=c85bb1083aa63749eec07905e62b48542a429c8482c3682c2e97067137fc0f2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
