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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC435RCT%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T121527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIHWJTebtz9hZpbRznoAEonyNbw4LO8JJRWdGp4CJTZeqAiEAgK2osUo%2FkqHwXIHJB1rQap%2FgXjROjgiMq3hBVLG%2BAhAq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDGOIOqtCLswr0ZgEBSrcA3OUyo8GsWQHt9jJGynYZxGHJoZg9GdqFXisI791ozKsmBfpKpVRT56K0xEhAVWG2rgJPM5yHxndo3lmMaVlQpUJIe0GQTx957APKIl%2BK0f%2Fog%2FQzdu%2B6Duo9Zo%2BEm%2BAdvtjRXdKH9ovXKsjc1aARChAdELuGf4xxNdK5hb20rD%2FWJnxmtswseMI7Eg%2Ba5yw%2BP3bCrsPZEsvJueIbfCoACNfc%2BE4X%2FZzythBNyEDOb2rZPd5r%2BXxRNHZ2oBqnjMhUfPWpHah8%2FEPMH5rcVQoDjva4Yjq6rsR%2FPEaJmT0%2Bq%2FHhcZQMp88BUtodVJxEFaZe7RUdeDGOjZhK51%2BFIWfLGo%2Be%2FQFvW5TWh%2FjCF5HjyRk%2FEjDSc0Hcbl7QFk%2BhFwtGu9Tx65f9q3Un5oAyxAU3jNCTK94L6ZCcxnC4lVH7A%2FK2xB8e%2F6XCNAm2DZaOtv%2BMR8o3GvGR4YqkLzC%2FUklVfINx1%2FJAo6NLHII0Syyw2xGNiUbd4VaBKXSxrT4cC4wBn3ytWOycUV%2FrRtGBG3pisGjDgsRpl%2FEkGd8iZbrZKSDMV6SjkjOGrYYtDxw4Hv9vCZLcKB%2FJyL5PgSw7M8LPeeict%2BZMA7c5tTKr0uvTvUjAcWIp1AZ2%2Be1fPQZMNOfhtQGOqUBzHlsjhCu4AkJWbwbs%2BRW%2FDiUbxU5hdsP8EGXIawNddRJNWq0rMKrS0aQ3j0jKgofIYeVyfBF2xzEckAKixfq6IhqJKMlRdYpVjHU0943VfxSugswclIhVkKVTew9QPIBiDDX1UApfOhU1aDA17QzzsXsL%2BZZb38reOAHnwdTNYQMUd2rfsJ1L6uzVfoWFnQffTbXMvPOxg4ovAANrROhPV4WdkUe&X-Amz-Signature=4feb558eeeae9b0afd5b8671b4e777e91da8289443400629d75bda61e6fe00d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC435RCT%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T121527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIHWJTebtz9hZpbRznoAEonyNbw4LO8JJRWdGp4CJTZeqAiEAgK2osUo%2FkqHwXIHJB1rQap%2FgXjROjgiMq3hBVLG%2BAhAq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDGOIOqtCLswr0ZgEBSrcA3OUyo8GsWQHt9jJGynYZxGHJoZg9GdqFXisI791ozKsmBfpKpVRT56K0xEhAVWG2rgJPM5yHxndo3lmMaVlQpUJIe0GQTx957APKIl%2BK0f%2Fog%2FQzdu%2B6Duo9Zo%2BEm%2BAdvtjRXdKH9ovXKsjc1aARChAdELuGf4xxNdK5hb20rD%2FWJnxmtswseMI7Eg%2Ba5yw%2BP3bCrsPZEsvJueIbfCoACNfc%2BE4X%2FZzythBNyEDOb2rZPd5r%2BXxRNHZ2oBqnjMhUfPWpHah8%2FEPMH5rcVQoDjva4Yjq6rsR%2FPEaJmT0%2Bq%2FHhcZQMp88BUtodVJxEFaZe7RUdeDGOjZhK51%2BFIWfLGo%2Be%2FQFvW5TWh%2FjCF5HjyRk%2FEjDSc0Hcbl7QFk%2BhFwtGu9Tx65f9q3Un5oAyxAU3jNCTK94L6ZCcxnC4lVH7A%2FK2xB8e%2F6XCNAm2DZaOtv%2BMR8o3GvGR4YqkLzC%2FUklVfINx1%2FJAo6NLHII0Syyw2xGNiUbd4VaBKXSxrT4cC4wBn3ytWOycUV%2FrRtGBG3pisGjDgsRpl%2FEkGd8iZbrZKSDMV6SjkjOGrYYtDxw4Hv9vCZLcKB%2FJyL5PgSw7M8LPeeict%2BZMA7c5tTKr0uvTvUjAcWIp1AZ2%2Be1fPQZMNOfhtQGOqUBzHlsjhCu4AkJWbwbs%2BRW%2FDiUbxU5hdsP8EGXIawNddRJNWq0rMKrS0aQ3j0jKgofIYeVyfBF2xzEckAKixfq6IhqJKMlRdYpVjHU0943VfxSugswclIhVkKVTew9QPIBiDDX1UApfOhU1aDA17QzzsXsL%2BZZb38reOAHnwdTNYQMUd2rfsJ1L6uzVfoWFnQffTbXMvPOxg4ovAANrROhPV4WdkUe&X-Amz-Signature=0cc25e1aabc22ad84e52d67fa321172f271531e8a9fa5a2deefb3fc9f1b15564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
