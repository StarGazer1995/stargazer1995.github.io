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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJLDEMG7%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T011604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDFWsss6NHAZunhtE1giEP1gu1gvKGNdRR1V9lLY%2FL2AgIhAKZp9XOLoDM%2B%2Bj9RCw0H%2F8gEdGsTeLFgr88oftYtNYxuKv8DCAkQABoMNjM3NDIzMTgzODA1IgyDl9B27%2FRRJST9MEEq3AMNj%2BrTsAw%2BsS1qukFA96Gfo8riIxQfTY41P7rXt5RzhiFiS7fFL77kA0%2FVX38JXjfSVtUyGVPRKtxhKkEA1aqXsyCCv5KgJLuoO2aLXJfk%2FqfkCGtMnvPjo6FSCBNrGoQAWWe3dCHBW68dO0JC1oaU40YMZ4QHCunXrvNoB1t0Jz4Rt058LW8oiPNJ2YamT9V%2BnzT8fPgJb2i%2FPBnrAlRMnUWicUiaAfHKfHYCOR%2FEU3TfTvJzWK7k49CxoTamalhML2VnJ8dxjBTgn1LAmc6Zz3BCK3VUxhDMeY7ta2UmRCz5PpSAB9pHLo9dJo6vtNrgrbgJF2fR%2BMzr5pAK6gJMk0LJX7LdssqK4rn%2FmCY1N1pocPfLsLF8DJTJkTjwx9tnAqS7SKOIS4p9RuAzPJQ59i4SBs%2Fc2WGb%2FbXvtcWF%2FSWI1OOydV2sOBArsygaLZFQx%2F%2FC2Qsc%2BbL4CUVvzPLlHKdoq9D2qQtmisIkeq8E6mea4tOcErAjA6WDo4zvjQBiHQZx2IQbcS8ZTKHDJL61KU2iuhcGZUDsMZxnqqW9HShUPC%2BBvTGAHhf%2BZBF41H3TqYrM2FBRmN29yRW3Dn6nzNjTWvgCpDxNWsIafp5q7OgKEe1TC5QifURlITCR8dXSBjqkASBBJ%2B60CrW%2FQS1%2FgN8GAlH4v9RxWcVNlQVHgC4WVG2TnyCHz0%2FeL9Z821j99wF2HFqxjiPd%2BSlkQy1d7MjH7uEKIdaM1gxmEpoRs9Fq99MsdUcZAUtagDQkCDxzyKDXsT4LeuPMeJxLx2p1wB%2B2I8Ocb6xFMgssAHYB8EHFCbFDaoAV2ucDsC%2F0Z16%2Ftm2LHXBC2ipzVt4TUmwk6u%2FQGayLDCG7&X-Amz-Signature=ee8aee78cced9827bbda231d10331873d68ad487fff81c4c4f6b43b939a9a312&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJLDEMG7%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T011604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDFWsss6NHAZunhtE1giEP1gu1gvKGNdRR1V9lLY%2FL2AgIhAKZp9XOLoDM%2B%2Bj9RCw0H%2F8gEdGsTeLFgr88oftYtNYxuKv8DCAkQABoMNjM3NDIzMTgzODA1IgyDl9B27%2FRRJST9MEEq3AMNj%2BrTsAw%2BsS1qukFA96Gfo8riIxQfTY41P7rXt5RzhiFiS7fFL77kA0%2FVX38JXjfSVtUyGVPRKtxhKkEA1aqXsyCCv5KgJLuoO2aLXJfk%2FqfkCGtMnvPjo6FSCBNrGoQAWWe3dCHBW68dO0JC1oaU40YMZ4QHCunXrvNoB1t0Jz4Rt058LW8oiPNJ2YamT9V%2BnzT8fPgJb2i%2FPBnrAlRMnUWicUiaAfHKfHYCOR%2FEU3TfTvJzWK7k49CxoTamalhML2VnJ8dxjBTgn1LAmc6Zz3BCK3VUxhDMeY7ta2UmRCz5PpSAB9pHLo9dJo6vtNrgrbgJF2fR%2BMzr5pAK6gJMk0LJX7LdssqK4rn%2FmCY1N1pocPfLsLF8DJTJkTjwx9tnAqS7SKOIS4p9RuAzPJQ59i4SBs%2Fc2WGb%2FbXvtcWF%2FSWI1OOydV2sOBArsygaLZFQx%2F%2FC2Qsc%2BbL4CUVvzPLlHKdoq9D2qQtmisIkeq8E6mea4tOcErAjA6WDo4zvjQBiHQZx2IQbcS8ZTKHDJL61KU2iuhcGZUDsMZxnqqW9HShUPC%2BBvTGAHhf%2BZBF41H3TqYrM2FBRmN29yRW3Dn6nzNjTWvgCpDxNWsIafp5q7OgKEe1TC5QifURlITCR8dXSBjqkASBBJ%2B60CrW%2FQS1%2FgN8GAlH4v9RxWcVNlQVHgC4WVG2TnyCHz0%2FeL9Z821j99wF2HFqxjiPd%2BSlkQy1d7MjH7uEKIdaM1gxmEpoRs9Fq99MsdUcZAUtagDQkCDxzyKDXsT4LeuPMeJxLx2p1wB%2B2I8Ocb6xFMgssAHYB8EHFCbFDaoAV2ucDsC%2F0Z16%2Ftm2LHXBC2ipzVt4TUmwk6u%2FQGayLDCG7&X-Amz-Signature=37ae7aa0d0c692a07a3200ccdf063110c026800c658099962f0ca5b89177dbbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
