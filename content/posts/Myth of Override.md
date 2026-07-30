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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EYT5PNU%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T155334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHD7rAUtULtaqs3U4H4oHMkj8%2BNfiNoatNAErjwpzbNgAiEA6gaTFhs%2BYqavP6aOwdYE9V5%2BHuaRYoe2XISsvix2xz4qiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIt8URRA9V6o3sPR5SrcA%2FSJG5t6gHcdFSCdcNxHul%2Bizat2NTLKTdxO%2B3L0QxipN7lYsDYzlOzHNqRm67qZ2FS9rd%2Bd%2FT1Dw7uCAGYCULvsXEq9t4M0tyVsdKUR7BmuH9xR4paUCaF8dvjKvArG5vUR7zrJg3YV%2Bj6kC0Y80UFajFfSj98hube8WfKeDjo3QC7QuYPFULbuu21O84BrRPqgY6Kx%2Fh4bonpHILhG1hXF0oBw36%2BK%2BS1CXUcSJ4kdKi2TCokMVY%2F3EQScwiB0p%2FZpblLf0T2gyeg48rPZgZ7HYu2naNQq%2FGs%2FUQcv29ZE4LG9F4h4AFudCFDwPNo%2BOzLR%2FhwxeBHI2VQybC1AXIqKVttdSO5JtxLOREcD%2FO6rwsFZGQqgywmH0IKR9yA8trQzsYiJddQdRck6KEMbQqSfhINvfvNs8Q9Darsd8njcKDz96mjzc1ZmcDDDqi8EiAYlpArFRF1%2BIULIinni9qkcNPLVY3xLn3kXJ0ac0LHaZkZitEgqkn4TL5vCGywcmqea9vNswCKnsp8y38%2FSFviKvM5eyn3oe%2F8UlkyUBiKqcHqI%2BU6HzVSG55%2B4gy4CfNh5xJx10%2Bf6fpTYD4RjqYX8rtybvTZYVnBB3c2F774lVBMcJGsMIrQlWIdUMPPArdMGOqUBZFD0WyIYDwC%2FMjcP%2Fw%2BWgQUxdQPsoQb8F7EOyofZvqexFGC7C4x%2B%2BjIsXZpDAU0ehR1v%2FieQdR1d4yjgS2fysf%2Fmcquf8%2Flmab8fTAWft%2BVwNbPi%2FQZYL0majDHfDiSFW1h1K6JYK1kkxj5VDlTRMrAIeARt52CnbnenZUQ8VfXe5EHdEgSziwaCoBqe6N18gUyF7sDhMa1v%2FSQIEuuSDWdQ6vcj&X-Amz-Signature=fadffedc6365856ad54b96e99b35bf81c4f39960ba4cdc98620325527e4b78eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EYT5PNU%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T155334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHD7rAUtULtaqs3U4H4oHMkj8%2BNfiNoatNAErjwpzbNgAiEA6gaTFhs%2BYqavP6aOwdYE9V5%2BHuaRYoe2XISsvix2xz4qiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIt8URRA9V6o3sPR5SrcA%2FSJG5t6gHcdFSCdcNxHul%2Bizat2NTLKTdxO%2B3L0QxipN7lYsDYzlOzHNqRm67qZ2FS9rd%2Bd%2FT1Dw7uCAGYCULvsXEq9t4M0tyVsdKUR7BmuH9xR4paUCaF8dvjKvArG5vUR7zrJg3YV%2Bj6kC0Y80UFajFfSj98hube8WfKeDjo3QC7QuYPFULbuu21O84BrRPqgY6Kx%2Fh4bonpHILhG1hXF0oBw36%2BK%2BS1CXUcSJ4kdKi2TCokMVY%2F3EQScwiB0p%2FZpblLf0T2gyeg48rPZgZ7HYu2naNQq%2FGs%2FUQcv29ZE4LG9F4h4AFudCFDwPNo%2BOzLR%2FhwxeBHI2VQybC1AXIqKVttdSO5JtxLOREcD%2FO6rwsFZGQqgywmH0IKR9yA8trQzsYiJddQdRck6KEMbQqSfhINvfvNs8Q9Darsd8njcKDz96mjzc1ZmcDDDqi8EiAYlpArFRF1%2BIULIinni9qkcNPLVY3xLn3kXJ0ac0LHaZkZitEgqkn4TL5vCGywcmqea9vNswCKnsp8y38%2FSFviKvM5eyn3oe%2F8UlkyUBiKqcHqI%2BU6HzVSG55%2B4gy4CfNh5xJx10%2Bf6fpTYD4RjqYX8rtybvTZYVnBB3c2F774lVBMcJGsMIrQlWIdUMPPArdMGOqUBZFD0WyIYDwC%2FMjcP%2Fw%2BWgQUxdQPsoQb8F7EOyofZvqexFGC7C4x%2B%2BjIsXZpDAU0ehR1v%2FieQdR1d4yjgS2fysf%2Fmcquf8%2Flmab8fTAWft%2BVwNbPi%2FQZYL0majDHfDiSFW1h1K6JYK1kkxj5VDlTRMrAIeARt52CnbnenZUQ8VfXe5EHdEgSziwaCoBqe6N18gUyF7sDhMa1v%2FSQIEuuSDWdQ6vcj&X-Amz-Signature=5b6e0cd32f143f5f6f61ba24de630e1987fec949d4fbc1be3c94efeb92bd7dd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
