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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZZEGCME%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T184422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUkNW18kHScGKE3czwQhiJcx6HpZ7EGPRQ3uGvh8nbRwIgTMPoqvUUczajIZ0kzRSgf7hChiMS0BfXkhWA22%2FV%2F%2FAq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIZ3Rtbgzg2UOY59SSrcA93Dhw4fDwUYlMLw3Hf5LvT3OblAZF%2FYL35B%2F%2FtiSO8YIKdNtqc1J2ApDSPfD7iZg5aXMCNRcfxg%2Fd1%2F2dxEiIFlNLm2J4oOxLsOnX8IeiEZo5Zfpx3557MWkOu3z3WoUdz9DPYsTxOtFEHTzMgJF8yPCZRxmnL6yeM2z%2B0Xa5I89e0lTrGUTQ5F1aBIYIZYzYItFSumv1bVVTMAeol7mE6cmRtzlhJvNiKwYTiXeiuOO%2F6QoGNcF0GwRS1S58vrnEhbZ0eKbcSobDrU0irNYEiky3pWPAtap6QWjzlJxqZNZwJE5LzpbsJ0BP227R58WAWMkxX39PBfXtk8g%2BwEwXG56GZYfDqIEG2XSUFJjrZvC2VLWFeJuC7uEv1KDVJvPFl0lNFWLv7oVK2pOGWRuC%2BpUKuGkow6gsu7F32YeEM0ky45SpKoqWX2WVkIBGnHBnk85%2FjWfow3smHa8STa5KwX2k7T7J4ZJfQmT%2FWGRLFpLKQ0%2FtqIy%2BnuXJP%2Fuq8DhhYaIJLIaN9F%2BC3SVQ%2BYI%2BQ2ABqjpbeRH4ugx0q3zBBxYVFE4wt4BB4h3tiqn3NsVVVEyvNEFPp00zosQhkBPW2rhQE7ylet8D1w3JT8mecmNCq5lH99%2FQk3x3S1MPDj7tIGOqUBsDQFLQ74lrkB6qIuQAtwKh%2BQAx8PS9bvio5wJnnqrQiD%2FI7BbpKhg5C5Ef9%2BT6osF3r5jAxHPXHCrmClt80Tf7PDA2U%2BQvVtsxIb2iAt9aTsAAHpG%2FujhH6S%2By7%2F8d7ozUH5NcYXh5J7arzvxeRtcbHheGaaanPFzjd1ioWL0rsNIcK0Bshhhrl9imO%2FBVCl1jIBXowwICNy%2BNi0V8gdyYHUcQ%2BJ&X-Amz-Signature=4db6bd59bda2ddc1c07ff450a42b4e545865ac4930af4875a338e2b742a7176d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZZEGCME%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T184422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUkNW18kHScGKE3czwQhiJcx6HpZ7EGPRQ3uGvh8nbRwIgTMPoqvUUczajIZ0kzRSgf7hChiMS0BfXkhWA22%2FV%2F%2FAq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIZ3Rtbgzg2UOY59SSrcA93Dhw4fDwUYlMLw3Hf5LvT3OblAZF%2FYL35B%2F%2FtiSO8YIKdNtqc1J2ApDSPfD7iZg5aXMCNRcfxg%2Fd1%2F2dxEiIFlNLm2J4oOxLsOnX8IeiEZo5Zfpx3557MWkOu3z3WoUdz9DPYsTxOtFEHTzMgJF8yPCZRxmnL6yeM2z%2B0Xa5I89e0lTrGUTQ5F1aBIYIZYzYItFSumv1bVVTMAeol7mE6cmRtzlhJvNiKwYTiXeiuOO%2F6QoGNcF0GwRS1S58vrnEhbZ0eKbcSobDrU0irNYEiky3pWPAtap6QWjzlJxqZNZwJE5LzpbsJ0BP227R58WAWMkxX39PBfXtk8g%2BwEwXG56GZYfDqIEG2XSUFJjrZvC2VLWFeJuC7uEv1KDVJvPFl0lNFWLv7oVK2pOGWRuC%2BpUKuGkow6gsu7F32YeEM0ky45SpKoqWX2WVkIBGnHBnk85%2FjWfow3smHa8STa5KwX2k7T7J4ZJfQmT%2FWGRLFpLKQ0%2FtqIy%2BnuXJP%2Fuq8DhhYaIJLIaN9F%2BC3SVQ%2BYI%2BQ2ABqjpbeRH4ugx0q3zBBxYVFE4wt4BB4h3tiqn3NsVVVEyvNEFPp00zosQhkBPW2rhQE7ylet8D1w3JT8mecmNCq5lH99%2FQk3x3S1MPDj7tIGOqUBsDQFLQ74lrkB6qIuQAtwKh%2BQAx8PS9bvio5wJnnqrQiD%2FI7BbpKhg5C5Ef9%2BT6osF3r5jAxHPXHCrmClt80Tf7PDA2U%2BQvVtsxIb2iAt9aTsAAHpG%2FujhH6S%2By7%2F8d7ozUH5NcYXh5J7arzvxeRtcbHheGaaanPFzjd1ioWL0rsNIcK0Bshhhrl9imO%2FBVCl1jIBXowwICNy%2BNi0V8gdyYHUcQ%2BJ&X-Amz-Signature=8ed45a3aac5b8f0e57f2f0f217f806a17d9164cc342821b350d3d55b617f8f95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
