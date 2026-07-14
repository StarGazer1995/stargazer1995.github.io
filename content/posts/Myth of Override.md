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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIIXKKR%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T204913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQDAOB76D7MFs5siZO%2BJcxSZh4PB29e%2BWrXMgoOLNPbb%2BQIhAOyPr2aSn8T4MqlqbsELEyYYpaG1qlPsEWRi%2BI07fV%2BaKv8DCBwQABoMNjM3NDIzMTgzODA1IgzD4Ur5m5icAXx3XY4q3AMkoCwoBB0DNTJEzJ4%2BuO9%2FKby7EjmNPy93%2FCAG7Rq9HfN0prblzdLEAXlQosYt%2BoQzCedLKsiQOHbMncA%2FE3nABNHJ8RpU9%2FLdarkE27mhsgnib7sZ7ErMglVeaMciSueqtekwrRj%2FbqZIoiWQi6%2FqJL7TkhSYu7fqvPCsIiBEGeYACjlp2eSwHi2M4%2Fgwe69%2BJ4nBMASGDEs%2FH8lnn3am1QMcQB347i%2ByEGer3LLW%2FmEjCL%2BQDPBP%2Bgb%2FmiAnXdnGVb2LsLz5ZgtkBnPEy7XCj8i7Bgpaz%2F2NCxTpulCzaW2z1vqJfKZwT4VMgWXPNNcbL6b1OL0u04Zh9hS6PPzvZERY%2BAIWsh%2FGJFkgjY050XoRIT%2FP2SCrCHIq76eCRBIgFhqWkPaKT7zWsPOUXo8ZmHDel5GnIAM3vJOV7%2Fi7v%2FHNbjQMxBngLiUjg5CcDSLR8lNVs4roOkQ5%2BREZ6bN2%2FA2eW%2FInIThRIXjSyMBZhcOVx%2FNzUZauJ0GsFpUONdt2vxwtsT8pzjZckWSCa2b%2FV2j9JNpOR7dGJhenSGSDNS5iQcxjzXgLLMhDlkBEg44%2Fn93QcHVIjarVO24FaD9VA4%2FeM7rZ3K9TIuDuoy9o7LHgr2bkGxw%2FSMzD%2FzCJnNrSBjqkAZlsfpj4AzKJtm5eU3RCQ3nkOE8QpqJechGY%2FaJOJr2Fdz4Bnmog20NZyQudk75VhZQOt292oXZ7BSQOrLvxWXREUrCTVILpRDa8pcEBW4lbHmZpzzGDRhe9uJ%2BVfyfI2evg3mnUNWoWKZIm9%2BzcUxUtrZNwV2R3wYX0XGXmzGm0OWVE4mu9dGhhAeRmGL%2FidMTejn9RQt0b1kaPJyUbQh9dzDI9&X-Amz-Signature=d40cedcdc6cb395f5a2e4d21011c64f7782f07faf2360f7ea33cbb67a061ad30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PIIXKKR%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T204913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJIMEYCIQDAOB76D7MFs5siZO%2BJcxSZh4PB29e%2BWrXMgoOLNPbb%2BQIhAOyPr2aSn8T4MqlqbsELEyYYpaG1qlPsEWRi%2BI07fV%2BaKv8DCBwQABoMNjM3NDIzMTgzODA1IgzD4Ur5m5icAXx3XY4q3AMkoCwoBB0DNTJEzJ4%2BuO9%2FKby7EjmNPy93%2FCAG7Rq9HfN0prblzdLEAXlQosYt%2BoQzCedLKsiQOHbMncA%2FE3nABNHJ8RpU9%2FLdarkE27mhsgnib7sZ7ErMglVeaMciSueqtekwrRj%2FbqZIoiWQi6%2FqJL7TkhSYu7fqvPCsIiBEGeYACjlp2eSwHi2M4%2Fgwe69%2BJ4nBMASGDEs%2FH8lnn3am1QMcQB347i%2ByEGer3LLW%2FmEjCL%2BQDPBP%2Bgb%2FmiAnXdnGVb2LsLz5ZgtkBnPEy7XCj8i7Bgpaz%2F2NCxTpulCzaW2z1vqJfKZwT4VMgWXPNNcbL6b1OL0u04Zh9hS6PPzvZERY%2BAIWsh%2FGJFkgjY050XoRIT%2FP2SCrCHIq76eCRBIgFhqWkPaKT7zWsPOUXo8ZmHDel5GnIAM3vJOV7%2Fi7v%2FHNbjQMxBngLiUjg5CcDSLR8lNVs4roOkQ5%2BREZ6bN2%2FA2eW%2FInIThRIXjSyMBZhcOVx%2FNzUZauJ0GsFpUONdt2vxwtsT8pzjZckWSCa2b%2FV2j9JNpOR7dGJhenSGSDNS5iQcxjzXgLLMhDlkBEg44%2Fn93QcHVIjarVO24FaD9VA4%2FeM7rZ3K9TIuDuoy9o7LHgr2bkGxw%2FSMzD%2FzCJnNrSBjqkAZlsfpj4AzKJtm5eU3RCQ3nkOE8QpqJechGY%2FaJOJr2Fdz4Bnmog20NZyQudk75VhZQOt292oXZ7BSQOrLvxWXREUrCTVILpRDa8pcEBW4lbHmZpzzGDRhe9uJ%2BVfyfI2evg3mnUNWoWKZIm9%2BzcUxUtrZNwV2R3wYX0XGXmzGm0OWVE4mu9dGhhAeRmGL%2FidMTejn9RQt0b1kaPJyUbQh9dzDI9&X-Amz-Signature=840f184ed20ad3c2681b1d5550c2b515550c072fd89c9cb17d81c23f49312026&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
