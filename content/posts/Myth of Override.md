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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVURGPLW%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T191917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDTtX55uQRm7YrOR4oN%2BEs3qp2r2pZG4LIw5ptMfYukPQIgasHKlArT1ABcwTYWxf2kKnEn%2BdwMNYtuaejY07rw0aQq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAKvXot68NHIZy7%2BdCrcA%2FvCG%2BSjQ7UYXwVwvSi%2BXAR7oD4Guymt8j2HQ1hEsmPijIOEdcLOZfqzxQ1aMd9pZgB%2B6Pb8n3q3Kkfl%2FABjzauuXWGCuFoI6i6cmKH1tPZBeFbPYUIr4jQ0%2FHhuId2ssBLRYoX3tjWGI7wZTvm5%2FoZzBnPjnNXtCwi93pc%2ByPl2%2BfnxtfCsRlO3A8IrEmjqM%2F%2By1afyoIf8wWTugUBRSu6lOENDYYr8I7U0XChSxggA5x9H1LTXbmQqscIQFwaUqAm1hbwGcpGeIPRp5N%2BGukP37C9tY9WVUAYDsJZQIpPqNpTbK92CjRN6SuAYh6QEUK9WDeNfmU1lykQdtk17US85HB%2BIwbHOOR4imYii7%2B%2BGkwEKLX3eQG%2F9RVXH8cXJN2PeDzmtscxe72%2BpmdT3K43vOB0i1wheNccIkZ01cxNXHftv%2F21d3UVqEeNWcSDy1jzLnEn3GFpjSDvdfm8djVm2CUEOJTfKaBkCXZTWv7%2FDd2QzkwiOApBX3p2QBMOSWwdNdk8HdJSXJPTONIPKmvitZs6ekPTlOrFG8aR1VQX5PIdYR8F9%2FiSnKogm8lEnGw55ge9jpxJ89AC2mRjbEilTVKNQKxzJ7dQ7495OBtnjTiUF%2BoYonFQ500NZMP%2BNyNMGOqUB0oChog9AvwxT4kJO5v8ND8Hvbko3Iami24Y2kSNpl1ORqgQS6qPYARVt%2BaOiMnZFpelYjqCVFzeoa8AtdU5AvR5BLrPfTD3Djx3kPdNaxip85RFgWd0tOlI2GZBsdrVVXO1K4o%2B99GuU%2BddCp4hP5IlG4SsWk70I%2FU0w4eVBAj%2FHmppFXURTnEAIO4jeXT1TSRdEft5C5ny4HYVT5xPG9n%2Bm3iUq&X-Amz-Signature=f4d36aaa4ea16c6bed8e5026d2b06cad2a7bc116075b0c1900122088e9e33e93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVURGPLW%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T191917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDTtX55uQRm7YrOR4oN%2BEs3qp2r2pZG4LIw5ptMfYukPQIgasHKlArT1ABcwTYWxf2kKnEn%2BdwMNYtuaejY07rw0aQq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAKvXot68NHIZy7%2BdCrcA%2FvCG%2BSjQ7UYXwVwvSi%2BXAR7oD4Guymt8j2HQ1hEsmPijIOEdcLOZfqzxQ1aMd9pZgB%2B6Pb8n3q3Kkfl%2FABjzauuXWGCuFoI6i6cmKH1tPZBeFbPYUIr4jQ0%2FHhuId2ssBLRYoX3tjWGI7wZTvm5%2FoZzBnPjnNXtCwi93pc%2ByPl2%2BfnxtfCsRlO3A8IrEmjqM%2F%2By1afyoIf8wWTugUBRSu6lOENDYYr8I7U0XChSxggA5x9H1LTXbmQqscIQFwaUqAm1hbwGcpGeIPRp5N%2BGukP37C9tY9WVUAYDsJZQIpPqNpTbK92CjRN6SuAYh6QEUK9WDeNfmU1lykQdtk17US85HB%2BIwbHOOR4imYii7%2B%2BGkwEKLX3eQG%2F9RVXH8cXJN2PeDzmtscxe72%2BpmdT3K43vOB0i1wheNccIkZ01cxNXHftv%2F21d3UVqEeNWcSDy1jzLnEn3GFpjSDvdfm8djVm2CUEOJTfKaBkCXZTWv7%2FDd2QzkwiOApBX3p2QBMOSWwdNdk8HdJSXJPTONIPKmvitZs6ekPTlOrFG8aR1VQX5PIdYR8F9%2FiSnKogm8lEnGw55ge9jpxJ89AC2mRjbEilTVKNQKxzJ7dQ7495OBtnjTiUF%2BoYonFQ500NZMP%2BNyNMGOqUB0oChog9AvwxT4kJO5v8ND8Hvbko3Iami24Y2kSNpl1ORqgQS6qPYARVt%2BaOiMnZFpelYjqCVFzeoa8AtdU5AvR5BLrPfTD3Djx3kPdNaxip85RFgWd0tOlI2GZBsdrVVXO1K4o%2B99GuU%2BddCp4hP5IlG4SsWk70I%2FU0w4eVBAj%2FHmppFXURTnEAIO4jeXT1TSRdEft5C5ny4HYVT5xPG9n%2Bm3iUq&X-Amz-Signature=31344582b0946d6072b9267ebf56bdf3f34390ec36616c0037304f4cbadc406a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
