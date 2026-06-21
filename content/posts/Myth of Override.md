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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTCWFXK4%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T023017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDfl3aMZrX1deWv5X4eWle9TWSZ5%2FheLVDIrH5bKbrJkQIgBofjjIRUJ6eNiCo5bUIiqf0i7rpFcShQaFs%2FF3fuL50qiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMAu2e1eOkdH3WbgDSrcA2yThMtp037giH5MGH0GTvyP83trLJR3xuNPr28%2B2ZZtSFErM4DGzMK95Fmp2t41k4u1upy0LULRxUix4wJml77iI3s4pDfTKBv%2FWGfAIIGj3NpP08%2Flkmt9iNVqggt2xjhGUNJ6kxaDYgLhomQptf31CZqxYzqWMReJI8oTN4htCIUw7htqvfddSpcepi8YbA7u94wzamRYse16IbXk66MQM3aXzzpGi7HIg270bvjzl8uyPfpExSMGJCdJ6mUe4jhCOxJPi4xAt%2BvgLW4PrL6b8uY8fkDMn8GoRzgecdlju8Vjwa%2Bg%2B80MeA1ZGynPFU5HUuVdy0bCHUQzYtQm%2FgbmDRRAa0Vyc0o3KWC6o8T6NP6rSHcLHNAhr4r3NSFFPaOH1iXw8FP2NpZXlC0tqPXwfD7DDvgH1lVEGblaBDiEuXF%2F7KDF%2BN0c7rjfMn6rq1APNnkEcZWXfpsrYnBHIxFazCXq5fPGDGIihICQxxbojpgAE0ImdBEx5kXOyr%2FCp6iuo1uLlPF7UcOIRXlfVPC0zd5kSx8n9x%2FwS8mRqEO9%2BI8BGQd%2B%2BZbcnbUK6cRUH2tQuKf6gNCwXlMT6aOtqEI9Mccx04t3TJjIphY%2BS4MjM7md7LMbW%2FehI4aWMLuv3NEGOqUBgGAg5%2FDF8f9Gf0FAK1kg%2BDP3Uf8uZEL5KpP%2FP2HrlK%2F3jqw3pDLxH8q6YalAWxIGrNOdQMQCcoOZEWnkMCrPDXkakpdSQbXs3435%2B%2FMNXpLLwuDb6cN0ZxicOMj%2FWj98HYxviRY57qI1a5B255nlv5yKxzekw0rdQs2Uks051v3NorlS%2BPcl4TpdiZbnAPdTCgdLFJ5%2BLR2e0kfDc6hVCefc71ef&X-Amz-Signature=af64deb4f8180a4d35857602fd68d915737254d76c8d9259b5109d9645d2484a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTCWFXK4%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T023017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDfl3aMZrX1deWv5X4eWle9TWSZ5%2FheLVDIrH5bKbrJkQIgBofjjIRUJ6eNiCo5bUIiqf0i7rpFcShQaFs%2FF3fuL50qiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMAu2e1eOkdH3WbgDSrcA2yThMtp037giH5MGH0GTvyP83trLJR3xuNPr28%2B2ZZtSFErM4DGzMK95Fmp2t41k4u1upy0LULRxUix4wJml77iI3s4pDfTKBv%2FWGfAIIGj3NpP08%2Flkmt9iNVqggt2xjhGUNJ6kxaDYgLhomQptf31CZqxYzqWMReJI8oTN4htCIUw7htqvfddSpcepi8YbA7u94wzamRYse16IbXk66MQM3aXzzpGi7HIg270bvjzl8uyPfpExSMGJCdJ6mUe4jhCOxJPi4xAt%2BvgLW4PrL6b8uY8fkDMn8GoRzgecdlju8Vjwa%2Bg%2B80MeA1ZGynPFU5HUuVdy0bCHUQzYtQm%2FgbmDRRAa0Vyc0o3KWC6o8T6NP6rSHcLHNAhr4r3NSFFPaOH1iXw8FP2NpZXlC0tqPXwfD7DDvgH1lVEGblaBDiEuXF%2F7KDF%2BN0c7rjfMn6rq1APNnkEcZWXfpsrYnBHIxFazCXq5fPGDGIihICQxxbojpgAE0ImdBEx5kXOyr%2FCp6iuo1uLlPF7UcOIRXlfVPC0zd5kSx8n9x%2FwS8mRqEO9%2BI8BGQd%2B%2BZbcnbUK6cRUH2tQuKf6gNCwXlMT6aOtqEI9Mccx04t3TJjIphY%2BS4MjM7md7LMbW%2FehI4aWMLuv3NEGOqUBgGAg5%2FDF8f9Gf0FAK1kg%2BDP3Uf8uZEL5KpP%2FP2HrlK%2F3jqw3pDLxH8q6YalAWxIGrNOdQMQCcoOZEWnkMCrPDXkakpdSQbXs3435%2B%2FMNXpLLwuDb6cN0ZxicOMj%2FWj98HYxviRY57qI1a5B255nlv5yKxzekw0rdQs2Uks051v3NorlS%2BPcl4TpdiZbnAPdTCgdLFJ5%2BLR2e0kfDc6hVCefc71ef&X-Amz-Signature=c59b9fd9b3c3869e58a79185fd24c29035f368675a8bf9091b5d31fdc53b54fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
