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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVISCKMY%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T203721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBg26s8RYxJdmPfJc94p21z8Vp5FJtUT%2BLqg2EHi1mgzAiEAxiWICqvOa2Ws6b4IGQ2OypVjhGXR18u%2FC0x1MCa1JrsqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2BVqsLgxvhFe6iZpCrcA%2F6yEyLkZyr1mXRCeaVyW2C7gU35kUxcAl%2BETWOvN389LrmVVgeul1zP9luLtk0IFfuu2vLHmaamU0QBxa%2Bza%2FG0sWj5aZTpnw14K5L%2F2oHGEdpPIseL13ktW5AfXbWB9ryOS%2BbzYziVX988o0jrYIgz%2FbCueQ36ulb1XCvZZJVuNseMhHRtpMCwQo2cQP3aomv7WvlCj61bHV4wxqpkyxFFeNncaZL6vH6a6P0Cvchwf%2BrR0fTp5vCADB0203BOlzUKvGUL0StneLrkmFl%2FSR08R4ial75rk2d0oSZhZrVcpjzmkT7jlNQjKuyMBHubTEpMpymfAMhlQGVfQ7XdaK1fCDsubl%2B2LRssfPgCx35Wh01l6p42X7%2FutUtVG4tkfyWyZMpucGrYYHiCy6id6rZV6m0%2Fe77CrrHPNtCnZ0Zjh5lbpWjbqMN8vfb%2FiX3xAsVCpDal6YtXB8toeNCz4rzwHYqf9TnQ0UBq%2BlzY6pFVaD3QIStztnJFEQ%2Fvcewk9aDtZZp%2F0IeVs3Ye5jAaoMK3h6HgO6zeVcv17u4aPAHqvEgrQRApK3ZLWJTlHhpBUVLTWAGp1tYn5WNTvYKFj6EgIm0lBPqqGVOmCv2dRKu7mylEqFpW2d3d1HSxMLfE9NIGOqUBtOi4FEYlBA1gP%2BoGjWs7O82Egk2NDrjts%2B0snC3EOjDltEbzOMHGi75W92CF%2By%2FrP9xrQ11GqK7g3VKSD%2FS7LMdcqSWpDv9NowA5kKYCdEa%2FyzTmDpQo31fQ6tT9Tg8rwUoIehg3Prr0GtHEzDcBERq9StWRFz46vXAQlDbWIznbKNQbr5zEPYzKuvvI1BF4Kl5%2FjUatwLIacRM9Dmp%2FfpPsb0cF&X-Amz-Signature=d969f17ad53eaa191cce0cd95aa0d6d18862b343a14bd33f471292a9a5e7804b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVISCKMY%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T203721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBg26s8RYxJdmPfJc94p21z8Vp5FJtUT%2BLqg2EHi1mgzAiEAxiWICqvOa2Ws6b4IGQ2OypVjhGXR18u%2FC0x1MCa1JrsqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2BVqsLgxvhFe6iZpCrcA%2F6yEyLkZyr1mXRCeaVyW2C7gU35kUxcAl%2BETWOvN389LrmVVgeul1zP9luLtk0IFfuu2vLHmaamU0QBxa%2Bza%2FG0sWj5aZTpnw14K5L%2F2oHGEdpPIseL13ktW5AfXbWB9ryOS%2BbzYziVX988o0jrYIgz%2FbCueQ36ulb1XCvZZJVuNseMhHRtpMCwQo2cQP3aomv7WvlCj61bHV4wxqpkyxFFeNncaZL6vH6a6P0Cvchwf%2BrR0fTp5vCADB0203BOlzUKvGUL0StneLrkmFl%2FSR08R4ial75rk2d0oSZhZrVcpjzmkT7jlNQjKuyMBHubTEpMpymfAMhlQGVfQ7XdaK1fCDsubl%2B2LRssfPgCx35Wh01l6p42X7%2FutUtVG4tkfyWyZMpucGrYYHiCy6id6rZV6m0%2Fe77CrrHPNtCnZ0Zjh5lbpWjbqMN8vfb%2FiX3xAsVCpDal6YtXB8toeNCz4rzwHYqf9TnQ0UBq%2BlzY6pFVaD3QIStztnJFEQ%2Fvcewk9aDtZZp%2F0IeVs3Ye5jAaoMK3h6HgO6zeVcv17u4aPAHqvEgrQRApK3ZLWJTlHhpBUVLTWAGp1tYn5WNTvYKFj6EgIm0lBPqqGVOmCv2dRKu7mylEqFpW2d3d1HSxMLfE9NIGOqUBtOi4FEYlBA1gP%2BoGjWs7O82Egk2NDrjts%2B0snC3EOjDltEbzOMHGi75W92CF%2By%2FrP9xrQ11GqK7g3VKSD%2FS7LMdcqSWpDv9NowA5kKYCdEa%2FyzTmDpQo31fQ6tT9Tg8rwUoIehg3Prr0GtHEzDcBERq9StWRFz46vXAQlDbWIznbKNQbr5zEPYzKuvvI1BF4Kl5%2FjUatwLIacRM9Dmp%2FfpPsb0cF&X-Amz-Signature=0498b0c6eeaf8b2aa16728121dc4c9c8b43df0141170a48bd2266d5f945ae5c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
