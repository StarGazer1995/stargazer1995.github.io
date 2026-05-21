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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VPKIFMO%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T175036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIFXSiiiHjYFHzBvBLeJSI76tF58jK6SRXJu3x%2FS%2BvWPPAiEAgxvD%2BM4C%2Be47vn7qW%2Blit4TZCQEGrDgSHIrnXH71y5wq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDAVwmXw1zHHpZx%2BSFSrcA9SrZy%2FxMsw9AsMpjNrtFIVQN44wYKH4LcgwZl2PEUALILjQJxB36O3SU1mIppLs%2BZy2FEkdhjG%2B9wT4fuF6DTVy5X3yO%2FeVAfl%2B3fcBm4w0T%2FWS1m%2BgFdQro8HqAVdd9Tgc9E3XG7iiM250syUivoNc%2BNBAwhSHBZg8az0Zr2EfWowErfYgq4Wl%2BjlsHieccasldmPWf3LW8ENpqJGqx%2FIn%2ByAnr4%2FU%2FsZkq0pqsfE0B%2BOA%2BBFv0xar6JZQgd2LZlZO6%2FRvcUMBBYy6SEnF9c3tmkqdN6aH5Foj9ZJ5SZyMTVxZ7XP9nbdPInrV7ig6%2FCKgkhlEXQVxJpsPDl4p%2FLsFdoOdgAoZS64JOpWkt6CAfleHiH1dllvF3LDk0wsLmAhN4s6Te9TAh7sLEBrz9JPKl9bb3cmncPcZfmWn3Hgr3ZFXxDoJ%2FsKF%2FeZhPK6bWwCuOnsYk8tRAcw29NidhBlCjFVKJhAdtpL%2BfZWPSzY%2BvN56ctr9AWYrdLHpCz%2BQsRd3zTLFQOqa143vKivnzCrb%2F6ye67jTWwcon%2BjDnr9yqT2IkwHaoaXcvN2TkhdECLSTXNRg3sl3vQ2AB1tqiQKk5bQxeTEgNbzdMSMqDlPutyHx3By5EkupHabPMM%2F3vNAGOqUBzNzw6H7qBapBRmqbE8NG%2FFbnfVC%2FCTHYlLTPeSfHS1TyXoioHlwSuUD%2FqzI2ole94onaleitTKmQHZjbiS6CqWDAoJO%2BVtNW5s693yw4FinqRSBzT8tZ%2BsnAH6EhaZPLiBXGCvZos9vDmilbWdYh%2BSCERbewkw8RKr%2BNAp2BV7i6LfhtSlC5RDuRNxJgm0y9D52Ez127lqeD9AzGeAlfYmSIOc7f&X-Amz-Signature=f4477234655ce2f304c4c7aa882d05536b94e3317a4f1144ff2350ab0c271985&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VPKIFMO%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T175036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIFXSiiiHjYFHzBvBLeJSI76tF58jK6SRXJu3x%2FS%2BvWPPAiEAgxvD%2BM4C%2Be47vn7qW%2Blit4TZCQEGrDgSHIrnXH71y5wq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDAVwmXw1zHHpZx%2BSFSrcA9SrZy%2FxMsw9AsMpjNrtFIVQN44wYKH4LcgwZl2PEUALILjQJxB36O3SU1mIppLs%2BZy2FEkdhjG%2B9wT4fuF6DTVy5X3yO%2FeVAfl%2B3fcBm4w0T%2FWS1m%2BgFdQro8HqAVdd9Tgc9E3XG7iiM250syUivoNc%2BNBAwhSHBZg8az0Zr2EfWowErfYgq4Wl%2BjlsHieccasldmPWf3LW8ENpqJGqx%2FIn%2ByAnr4%2FU%2FsZkq0pqsfE0B%2BOA%2BBFv0xar6JZQgd2LZlZO6%2FRvcUMBBYy6SEnF9c3tmkqdN6aH5Foj9ZJ5SZyMTVxZ7XP9nbdPInrV7ig6%2FCKgkhlEXQVxJpsPDl4p%2FLsFdoOdgAoZS64JOpWkt6CAfleHiH1dllvF3LDk0wsLmAhN4s6Te9TAh7sLEBrz9JPKl9bb3cmncPcZfmWn3Hgr3ZFXxDoJ%2FsKF%2FeZhPK6bWwCuOnsYk8tRAcw29NidhBlCjFVKJhAdtpL%2BfZWPSzY%2BvN56ctr9AWYrdLHpCz%2BQsRd3zTLFQOqa143vKivnzCrb%2F6ye67jTWwcon%2BjDnr9yqT2IkwHaoaXcvN2TkhdECLSTXNRg3sl3vQ2AB1tqiQKk5bQxeTEgNbzdMSMqDlPutyHx3By5EkupHabPMM%2F3vNAGOqUBzNzw6H7qBapBRmqbE8NG%2FFbnfVC%2FCTHYlLTPeSfHS1TyXoioHlwSuUD%2FqzI2ole94onaleitTKmQHZjbiS6CqWDAoJO%2BVtNW5s693yw4FinqRSBzT8tZ%2BsnAH6EhaZPLiBXGCvZos9vDmilbWdYh%2BSCERbewkw8RKr%2BNAp2BV7i6LfhtSlC5RDuRNxJgm0y9D52Ez127lqeD9AzGeAlfYmSIOc7f&X-Amz-Signature=1ae272dcc5cf5960220685c6abba4f4c318912dba39cf076542f5da4f56575f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
