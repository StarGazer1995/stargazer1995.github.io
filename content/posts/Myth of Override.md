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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIP7OURA%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T194306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGALpi5wBzF%2BiJG5%2B5s6rplFn2qiePiaD7zOwlvfgCqnAiEAwjzjboxr5BIc0WNr4XnRv6bsg5cuh5%2FPQEZ3erYh1OIq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDDQAq7eRE5FpbQ0WZyrcA1yY4ygr0uKrveQ3mA46sqHRw0KseHcNKLthP7TlML7JZh6KVl82TMKdkRnuqXueovbDSRHMMPQ23y%2Bys1RAjhmdt209o0IFtTA1uG%2BNIC6W4AwNWialGYn16lnpS4SHWoULRn4OEsgVUDa49CXTIh4enFzNTJ45wuzE03QUsAJtUzFhtpEjkEDm1yMWWJwf7jy%2F6HK0o8Eqw9696AW%2F6hDeoqGwXOMOpDBFbdD%2F7ybIpZvKB%2FY2oNnyDFtE4eT%2BBcuD4z8Fgo0nWXdrXhMDYYt7qQMgPyZNWYDiMLeYf1wVLA2VCaZiPYiCZ2xvuGUaYAn4VvKVrwNZEepWv28pMWXvYczhelW%2FnlLtuw%2Fc%2F584nqALWHJpvkaEMfCvSGEjQUM9KAFvTYCmcjHIhphXZO6MDqhzLnFF12UVIHcpDHfNba4t6W3w9kVosd7Ey8vMtF92TnAr5pGq5FPhvqosV6kZWTFS0nENVnmXVRWTr3Vl5Ssiv3b%2BFMPYM4S2WuvpLroGfNcrmDlAJel%2BI3TsDvEriWPUpw3quDVlmYAA00upWTpsok4a19p9xyaUy7t1j3xvHVzy8xvhTZ0owM3Pf2dQtLIvH9gYSgZi69hJox13QjXNmOkzNF2JcDI%2BMNavu9UGOqUBTG%2BpFzuAoDjvwBrGV3o8HeL2ACloScffmp5iSfZ9worUqjL39yK8t6CswEX5pG1FSz%2Fjo9%2Fl5g4ze6BEBk0AtJ5oUst3EWa5UFT6EMJUEwvchmNkzvBUvPARymZFAqpWkecxYl4%2FEmFvxTtCslSokm3j4GPu6vE6Eap15SALPZSyJvlGP%2FxQSEDyzQDnfkEovQ84fHnIqdcqzHsmnkdLcYIgskZl&X-Amz-Signature=37c1e7661f697e3e465d44cfbf259f489ab577c36972bfc692e5ea639716e228&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIP7OURA%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T194306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGALpi5wBzF%2BiJG5%2B5s6rplFn2qiePiaD7zOwlvfgCqnAiEAwjzjboxr5BIc0WNr4XnRv6bsg5cuh5%2FPQEZ3erYh1OIq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDDQAq7eRE5FpbQ0WZyrcA1yY4ygr0uKrveQ3mA46sqHRw0KseHcNKLthP7TlML7JZh6KVl82TMKdkRnuqXueovbDSRHMMPQ23y%2Bys1RAjhmdt209o0IFtTA1uG%2BNIC6W4AwNWialGYn16lnpS4SHWoULRn4OEsgVUDa49CXTIh4enFzNTJ45wuzE03QUsAJtUzFhtpEjkEDm1yMWWJwf7jy%2F6HK0o8Eqw9696AW%2F6hDeoqGwXOMOpDBFbdD%2F7ybIpZvKB%2FY2oNnyDFtE4eT%2BBcuD4z8Fgo0nWXdrXhMDYYt7qQMgPyZNWYDiMLeYf1wVLA2VCaZiPYiCZ2xvuGUaYAn4VvKVrwNZEepWv28pMWXvYczhelW%2FnlLtuw%2Fc%2F584nqALWHJpvkaEMfCvSGEjQUM9KAFvTYCmcjHIhphXZO6MDqhzLnFF12UVIHcpDHfNba4t6W3w9kVosd7Ey8vMtF92TnAr5pGq5FPhvqosV6kZWTFS0nENVnmXVRWTr3Vl5Ssiv3b%2BFMPYM4S2WuvpLroGfNcrmDlAJel%2BI3TsDvEriWPUpw3quDVlmYAA00upWTpsok4a19p9xyaUy7t1j3xvHVzy8xvhTZ0owM3Pf2dQtLIvH9gYSgZi69hJox13QjXNmOkzNF2JcDI%2BMNavu9UGOqUBTG%2BpFzuAoDjvwBrGV3o8HeL2ACloScffmp5iSfZ9worUqjL39yK8t6CswEX5pG1FSz%2Fjo9%2Fl5g4ze6BEBk0AtJ5oUst3EWa5UFT6EMJUEwvchmNkzvBUvPARymZFAqpWkecxYl4%2FEmFvxTtCslSokm3j4GPu6vE6Eap15SALPZSyJvlGP%2FxQSEDyzQDnfkEovQ84fHnIqdcqzHsmnkdLcYIgskZl&X-Amz-Signature=b2ed76bf6853f255a3a3756c1c6153ff05f703d1a6cb5fa14cc0830ee4f32ff7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
