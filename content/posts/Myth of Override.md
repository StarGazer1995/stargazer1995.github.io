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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFG6AVWC%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T201513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCG49Qs93FXxcMMg83beykmKsY%2Bu80hsEekaiW5UC6nugIgdNHZLcliYSHxLDqXY7xwiILScxn243XqlzUw6pg29%2FYqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLdukN%2FXB%2Fpy5iSqUyrcA0v5xwFMX%2BFYOug8Yj9Lv9T6eSDpRUF26JO0Y4MLbyThuPseL%2FFe8nN9C1tww%2F8FNdJaqWeb8ugoKRhOEAr3nW39aGuYu1FQNyFoHlxkDitjoXG23LLiTyjksNYH46a8OFoyaxmEh8plzMNQdg7XOKxznWvK%2BI8N9gFtNi0wKV2N8njpwNDAEX9zF%2BhxW5fx%2BZ5WaeMzzj4Er9vuvVoVF6rf6NxH7eplqw6OxA6YckmoLKJ3ksntSwU9X9DJTw6%2BKYFBfvnFSjCcRjL8wny6vamBEo%2BxIDAVT2WxH8c7yOS1%2FqdwLVjK82X4yLUl8JU45Am31RWXoAlGsn1YvNdnr76DKpytwb12a01hXYOo8BUozzJwFGUoGjrvJnhmaAQf3Y7Ea9uXndKkw%2B9wFGRrFiFJsa%2FfVKWMJKXlBTKmIKGBHOUcIj4eUAxAxBJY8%2BRpphm87PNRrsU925wWqf5TnNvdM5nsGli0OmajopFyewRFdeFNcbVQNYYyPSSgdBUXkvMrs1IK4hrbfmtYum3dU%2Bq3zCR0rM%2B6nlq0u8iZRVr8nzY%2B80QcjgR0esI0X2BgG%2BLYwh4nAgnILkLcRO9qLwutfXtdgAX0etDjsXRQD2dcuw7pqVfU2JYqfCkZMLHZ3NQGOqUBM2%2F3tJrMHeKDd1Ho90sQ6c5woVf4yHEA79UJmrIdZnDsmFqQfyw0KFbCenjBGQ3ZRrtFXAYG0zk8znVtEFDGYhFLE6w3GwLLbxgMjIR5l32aw8%2BL5QUzGGWugV1Rm62MrsyeQpoyO3tLiFaqvqoHEykzgwsA1cO5usi4fdSJ2%2Fsp%2FVNfJZ1ODp5Td2quo8xob1ry%2FssXPQRStJlRXWa8H06rtY%2FK&X-Amz-Signature=9638ea156763295b3e6ac893780390c1ea4cfe3954b90cec632875dd82cc9581&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFG6AVWC%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T201513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCG49Qs93FXxcMMg83beykmKsY%2Bu80hsEekaiW5UC6nugIgdNHZLcliYSHxLDqXY7xwiILScxn243XqlzUw6pg29%2FYqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLdukN%2FXB%2Fpy5iSqUyrcA0v5xwFMX%2BFYOug8Yj9Lv9T6eSDpRUF26JO0Y4MLbyThuPseL%2FFe8nN9C1tww%2F8FNdJaqWeb8ugoKRhOEAr3nW39aGuYu1FQNyFoHlxkDitjoXG23LLiTyjksNYH46a8OFoyaxmEh8plzMNQdg7XOKxznWvK%2BI8N9gFtNi0wKV2N8njpwNDAEX9zF%2BhxW5fx%2BZ5WaeMzzj4Er9vuvVoVF6rf6NxH7eplqw6OxA6YckmoLKJ3ksntSwU9X9DJTw6%2BKYFBfvnFSjCcRjL8wny6vamBEo%2BxIDAVT2WxH8c7yOS1%2FqdwLVjK82X4yLUl8JU45Am31RWXoAlGsn1YvNdnr76DKpytwb12a01hXYOo8BUozzJwFGUoGjrvJnhmaAQf3Y7Ea9uXndKkw%2B9wFGRrFiFJsa%2FfVKWMJKXlBTKmIKGBHOUcIj4eUAxAxBJY8%2BRpphm87PNRrsU925wWqf5TnNvdM5nsGli0OmajopFyewRFdeFNcbVQNYYyPSSgdBUXkvMrs1IK4hrbfmtYum3dU%2Bq3zCR0rM%2B6nlq0u8iZRVr8nzY%2B80QcjgR0esI0X2BgG%2BLYwh4nAgnILkLcRO9qLwutfXtdgAX0etDjsXRQD2dcuw7pqVfU2JYqfCkZMLHZ3NQGOqUBM2%2F3tJrMHeKDd1Ho90sQ6c5woVf4yHEA79UJmrIdZnDsmFqQfyw0KFbCenjBGQ3ZRrtFXAYG0zk8znVtEFDGYhFLE6w3GwLLbxgMjIR5l32aw8%2BL5QUzGGWugV1Rm62MrsyeQpoyO3tLiFaqvqoHEykzgwsA1cO5usi4fdSJ2%2Fsp%2FVNfJZ1ODp5Td2quo8xob1ry%2FssXPQRStJlRXWa8H06rtY%2FK&X-Amz-Signature=2be990c1a0dcc692eb1cb3155d565518b67df1c9e29e6e1a2e66854dee9e6583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
