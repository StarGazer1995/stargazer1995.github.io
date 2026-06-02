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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YLEULTL%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T021728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIF%2BUeu4dqV9Gf2Nsa1DUzCssyEdE4tlFOGtCGTz4Ial8AiEAsxJtcV1C06rC5T0Sb146J1ELHsOYU4CDoPKCBRwDKDgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDA4pnJTs9aHWC%2BQIiyrcA1q1M7Nszas1diuZTkl4wi%2BJylgawrUY55PI489ElgPCLeYqZiCTaahPwVIo8iSZRD5AOx2FJlkzmoWQd1zd8EiPGSrr41uNSK69EuM82O2bfa8T4EveR3wZIlIVUaqp6LV2yk96oDeU74eHQF9B5zImCaQGY5SOZdFAvgQPRBrBwELB9K6ntSdxdggHZiqiob7C%2BHFF4xmv%2BVbGL2ReZ7Q%2FtrrC1nmbwXFk1Bd0B1EcBP2odhyefXoGFoUlgZDoHURMa2JIa470AE8U1VgbaELQ72M5AEroZbaSucetCO8pk%2F4aCsP%2F04Sz%2F%2BhywUR4YhA5c%2B%2FKsrE1UGsOVyf%2Fb%2FGqzWuv61AwCpGjpTzF8dfWHQwUuLf4WptIR28K0KeTCv2e2E%2Fh0Rs1ms%2BngwHx1I5VI6p9B3Sx8EeUG2mcxTIEQc24X9pDCuw82Qj7qvZa7uMg%2BgiS%2FqxcEYAqPhS9m4rkBTof5UBpUqCLgtSl%2Fc9OJgbzDMOaBPfwN%2BFo9k7FE8lrPULB16wgBqXmO0aVf40UVOcXTFl2H6lgODLpb7VIFFvlb2I0%2Fkr7Ns6TFRWLX3K0spI2wAeiBLOz%2BH5GbtM69VRmiXBQ2MjzLCpdG17oB1xcH8CPreeoXrdwMPCG%2BNAGOqUBPzgyo0lGnlNn9GXjpLKXKiX0GXyBY5rQwvD3Jw0dRSgQTEC8%2FV7zeR3cVy%2Bf%2F37dWbq2CTaOdVFJhTTlf%2BSNLk%2B53ZR9EjDxJdphzPKOILtI4AeNglyvIiChgmo7q%2F7%2Fa7S%2BajXSV13NTzdAUHOF%2BLm236gaTxtKyDHesrjlzqYWM7rHdtDZ9IiUf2wcEqNNhQmKk3bzq5gWWPVoXZEtteidyIrw&X-Amz-Signature=a5087a1c12e0cd0ebeba639f68310ac9bfda28d429391a737329fe07c773c9c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YLEULTL%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T021728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJHMEUCIF%2BUeu4dqV9Gf2Nsa1DUzCssyEdE4tlFOGtCGTz4Ial8AiEAsxJtcV1C06rC5T0Sb146J1ELHsOYU4CDoPKCBRwDKDgq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDA4pnJTs9aHWC%2BQIiyrcA1q1M7Nszas1diuZTkl4wi%2BJylgawrUY55PI489ElgPCLeYqZiCTaahPwVIo8iSZRD5AOx2FJlkzmoWQd1zd8EiPGSrr41uNSK69EuM82O2bfa8T4EveR3wZIlIVUaqp6LV2yk96oDeU74eHQF9B5zImCaQGY5SOZdFAvgQPRBrBwELB9K6ntSdxdggHZiqiob7C%2BHFF4xmv%2BVbGL2ReZ7Q%2FtrrC1nmbwXFk1Bd0B1EcBP2odhyefXoGFoUlgZDoHURMa2JIa470AE8U1VgbaELQ72M5AEroZbaSucetCO8pk%2F4aCsP%2F04Sz%2F%2BhywUR4YhA5c%2B%2FKsrE1UGsOVyf%2Fb%2FGqzWuv61AwCpGjpTzF8dfWHQwUuLf4WptIR28K0KeTCv2e2E%2Fh0Rs1ms%2BngwHx1I5VI6p9B3Sx8EeUG2mcxTIEQc24X9pDCuw82Qj7qvZa7uMg%2BgiS%2FqxcEYAqPhS9m4rkBTof5UBpUqCLgtSl%2Fc9OJgbzDMOaBPfwN%2BFo9k7FE8lrPULB16wgBqXmO0aVf40UVOcXTFl2H6lgODLpb7VIFFvlb2I0%2Fkr7Ns6TFRWLX3K0spI2wAeiBLOz%2BH5GbtM69VRmiXBQ2MjzLCpdG17oB1xcH8CPreeoXrdwMPCG%2BNAGOqUBPzgyo0lGnlNn9GXjpLKXKiX0GXyBY5rQwvD3Jw0dRSgQTEC8%2FV7zeR3cVy%2Bf%2F37dWbq2CTaOdVFJhTTlf%2BSNLk%2B53ZR9EjDxJdphzPKOILtI4AeNglyvIiChgmo7q%2F7%2Fa7S%2BajXSV13NTzdAUHOF%2BLm236gaTxtKyDHesrjlzqYWM7rHdtDZ9IiUf2wcEqNNhQmKk3bzq5gWWPVoXZEtteidyIrw&X-Amz-Signature=991fd323390fa1353abb03a38e8baa0f9895f808b20574cb4dc7b654ef0f150d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
