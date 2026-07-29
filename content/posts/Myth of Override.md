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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F4QEMMR%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T154411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1jdGVZ97xy9UrvKWB%2B7%2BQq4W14Dfehv3PWl3QSEmaqQIhAPS2AWZ38vJowXDTXNvF%2BuO4oFkiFxArrv155EcLbPywKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXb42trqa4VzKiNkIq3AOZaic7ZXW2ISbRRJUPLpmmDUCwifGIk6Mzbk5OUrApTlAW7xXsB6A356vY21oMmO8PbMz468b4k7gwVD5eSTB82qMVEunnSVFDeLNnGKXTbbTbQhO4MAl%2BxqRe01OfK%2FWSXaXW0nOxoU3VnuLExNyM6%2FKg72XbvGExQzTgg62NCm4cvEdfUd2FHum9JP4tyz%2Bg1V3g6CGqDXLfMAy5sefQqg%2FkGZmMD9iP2h6PToQkHqt6mmJYOT13uXZmokWVPDZmZ%2Fjmrb9BGobwI4ic0pELmwa9vNpKmCZqj7i7BKUzxVuUCPmiK6jw2Y9EDOHdlSI0puD0jKLWFX5uEFPDVGDOna6%2FGDkR4NfXIEABS2MtH3j%2Bon%2BtTQUUh%2FYdt25Q8p1Wfs3Vu2BinjeclkcHE3EjUTuHRZ0Gx9wLbvI4iCbmhXt1X03y7gVMIEaskZC%2F4NzmvtCpT1G7v1rVJP4QcQwJjsfr2AqUx29eqc1XWDV7%2Fc%2BN%2FDx84%2B%2B1jmNdQUUT7TOlLYrAgTELW44oCYFDWeAfvkuuqXU9iLZF200L5H7lkKAQ51GibMJsVMeY6V%2F5CKlN68jvPbSXdmO7PgOs4gHxJbTZo9AE%2FcLGHdsmfkF%2FsvT4P6mv0Kas6sUjWDD0oqjTBjqkAV39acTzAnsQF3drI6JSdGH%2FbmqG2Wfpk1vFhe4wrKjNqp%2FznDEQ%2BolXyQp17RspNZg9I0nuEZj1fhIveZ7ZR6cSZAzdT6dwWLPTSZGvvMmhTGzOaQhDIJ2ajUKpDTuqpSViPdzboaE63VECZPEqjt9cVlG8crp1SwTtZZor8dETbgTFKpIzzlAsei2S%2Bc4f%2BPDxYdLtY2vuVr5FchbI%2FRoleOu8&X-Amz-Signature=10bb5c3ed3f92bc540f387cfb6e8d36a16eb974d23869caccb0d362a229c82b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F4QEMMR%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T154411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1jdGVZ97xy9UrvKWB%2B7%2BQq4W14Dfehv3PWl3QSEmaqQIhAPS2AWZ38vJowXDTXNvF%2BuO4oFkiFxArrv155EcLbPywKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXb42trqa4VzKiNkIq3AOZaic7ZXW2ISbRRJUPLpmmDUCwifGIk6Mzbk5OUrApTlAW7xXsB6A356vY21oMmO8PbMz468b4k7gwVD5eSTB82qMVEunnSVFDeLNnGKXTbbTbQhO4MAl%2BxqRe01OfK%2FWSXaXW0nOxoU3VnuLExNyM6%2FKg72XbvGExQzTgg62NCm4cvEdfUd2FHum9JP4tyz%2Bg1V3g6CGqDXLfMAy5sefQqg%2FkGZmMD9iP2h6PToQkHqt6mmJYOT13uXZmokWVPDZmZ%2Fjmrb9BGobwI4ic0pELmwa9vNpKmCZqj7i7BKUzxVuUCPmiK6jw2Y9EDOHdlSI0puD0jKLWFX5uEFPDVGDOna6%2FGDkR4NfXIEABS2MtH3j%2Bon%2BtTQUUh%2FYdt25Q8p1Wfs3Vu2BinjeclkcHE3EjUTuHRZ0Gx9wLbvI4iCbmhXt1X03y7gVMIEaskZC%2F4NzmvtCpT1G7v1rVJP4QcQwJjsfr2AqUx29eqc1XWDV7%2Fc%2BN%2FDx84%2B%2B1jmNdQUUT7TOlLYrAgTELW44oCYFDWeAfvkuuqXU9iLZF200L5H7lkKAQ51GibMJsVMeY6V%2F5CKlN68jvPbSXdmO7PgOs4gHxJbTZo9AE%2FcLGHdsmfkF%2FsvT4P6mv0Kas6sUjWDD0oqjTBjqkAV39acTzAnsQF3drI6JSdGH%2FbmqG2Wfpk1vFhe4wrKjNqp%2FznDEQ%2BolXyQp17RspNZg9I0nuEZj1fhIveZ7ZR6cSZAzdT6dwWLPTSZGvvMmhTGzOaQhDIJ2ajUKpDTuqpSViPdzboaE63VECZPEqjt9cVlG8crp1SwTtZZor8dETbgTFKpIzzlAsei2S%2Bc4f%2BPDxYdLtY2vuVr5FchbI%2FRoleOu8&X-Amz-Signature=03756576c291a59fcbc8754742c481ac97eb0b7ff0faee1d192ada3ebb8014ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
