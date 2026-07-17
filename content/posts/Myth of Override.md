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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T66W5XTX%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T111358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcCzbsnBbRlQ0O71mNCnLB4%2FFiJDmVuAKx2%2FBp26RxUAiB9piiqz1a7t33qKjKUaL9RZwzVQUVpEamgBMI%2Bnk1TuCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMS%2BawPUSAbFT7sBXvKtwDl8ay496z%2BZnh8fFNFLMDC54O7Cd8K0i7OXsv1SEijvMBDl8iFCPjCJS73ma3%2FcDVvauVvUXt3E5tn6Ab%2FfmQwFCeIep1ApJ5dGjkJnuHbIsJxloqkRtGbb%2Fo%2F7cY76I8JLndme3fC5W%2F0fESVldYewvO%2FU%2F%2F1oENVHL%2F9vzGk7%2BMcdqTvm9DynAkFr12ycEhatc876R%2Fzf4GH51itBVZTs0nIoztnezDIF3JamLV4nlvFwzBfNXEamBMayYxNMVjM2f5Lr1yWWtnK35id2XtGtN%2FH5vHjsOO7pROV%2BPiFdP%2Fwcda73x7GdZPp01q102Drs7VzTu0mO5ySXbtPEiWM9cd%2FLy%2FoFhfntB9HSh38B9TtXX08b78wazF3gjjDo2W4HKr6FxDD7UT63c%2Be9M%2B%2FS16R%2FCueL8n5WAqrh8fP3Xhh1PNLopveaGocYTW9DHJQetIutiz974YZibmV%2FSKbcCj1MExBM1Nze2VBII0Dy5V1XziiHDzO%2Bu%2BNG3R6fo%2FltC0UhGKDwMLpjjB60ZE4ZLbIA%2BrYvuWUo5Uerl5Uo12mQ9HLnk8t0JRmXgBA%2BeUrm6B2A5J%2BJC6kP2EjRO4A2Q7vCAYV5MvEZc0ildrDlNGCP9UBGaiMMd7nDow3Ino0gY6pgFSh%2FH4qWzts5ci2CaC3hmZE8ffiJecclse0U3VJo2kM2XoFld6TmvYd8LaVqcnIqL4sCG1Ii1zubYzJ2Z2R9ic2NDQq2rsvcZpFVkEu2%2Fe%2BaSGlF6%2BT%2Fmoz8cMAX5W4g9pjp%2FqcFmlbo%2FKvHTQuEln%2FLwXXU9ujDW5rOajwrol2mXr6%2F49FWLUaHmNVE0AH2t%2Bjiz3e2vGTkulvJv%2FcG%2BErS6MBTOS&X-Amz-Signature=cef8b512738f8d9dfb87286b712418c20d4d0f61f818d98abc721b3b739a6046&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T66W5XTX%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T111358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcCzbsnBbRlQ0O71mNCnLB4%2FFiJDmVuAKx2%2FBp26RxUAiB9piiqz1a7t33qKjKUaL9RZwzVQUVpEamgBMI%2Bnk1TuCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMS%2BawPUSAbFT7sBXvKtwDl8ay496z%2BZnh8fFNFLMDC54O7Cd8K0i7OXsv1SEijvMBDl8iFCPjCJS73ma3%2FcDVvauVvUXt3E5tn6Ab%2FfmQwFCeIep1ApJ5dGjkJnuHbIsJxloqkRtGbb%2Fo%2F7cY76I8JLndme3fC5W%2F0fESVldYewvO%2FU%2F%2F1oENVHL%2F9vzGk7%2BMcdqTvm9DynAkFr12ycEhatc876R%2Fzf4GH51itBVZTs0nIoztnezDIF3JamLV4nlvFwzBfNXEamBMayYxNMVjM2f5Lr1yWWtnK35id2XtGtN%2FH5vHjsOO7pROV%2BPiFdP%2Fwcda73x7GdZPp01q102Drs7VzTu0mO5ySXbtPEiWM9cd%2FLy%2FoFhfntB9HSh38B9TtXX08b78wazF3gjjDo2W4HKr6FxDD7UT63c%2Be9M%2B%2FS16R%2FCueL8n5WAqrh8fP3Xhh1PNLopveaGocYTW9DHJQetIutiz974YZibmV%2FSKbcCj1MExBM1Nze2VBII0Dy5V1XziiHDzO%2Bu%2BNG3R6fo%2FltC0UhGKDwMLpjjB60ZE4ZLbIA%2BrYvuWUo5Uerl5Uo12mQ9HLnk8t0JRmXgBA%2BeUrm6B2A5J%2BJC6kP2EjRO4A2Q7vCAYV5MvEZc0ildrDlNGCP9UBGaiMMd7nDow3Ino0gY6pgFSh%2FH4qWzts5ci2CaC3hmZE8ffiJecclse0U3VJo2kM2XoFld6TmvYd8LaVqcnIqL4sCG1Ii1zubYzJ2Z2R9ic2NDQq2rsvcZpFVkEu2%2Fe%2BaSGlF6%2BT%2Fmoz8cMAX5W4g9pjp%2FqcFmlbo%2FKvHTQuEln%2FLwXXU9ujDW5rOajwrol2mXr6%2F49FWLUaHmNVE0AH2t%2Bjiz3e2vGTkulvJv%2FcG%2BErS6MBTOS&X-Amz-Signature=0c6ec84db9d76abfe22ec23174745d65b8719242eb0cd97f931d5caa0efec743&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
