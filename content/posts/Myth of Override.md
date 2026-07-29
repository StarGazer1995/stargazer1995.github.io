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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MLITYT3%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T012232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoW3eqOA%2BaT%2BPfsawk5u6Rd3sdab%2FyBVBzQSAqlek5yAIgLWryucVUgRN%2BtEVeJfoxAJtTaKf5T5d9vbLLKOvQJuAq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDGrCKrqzCnqsvfeqzyrcAwS3g1roxGTlmZ3kcr%2FLVDwuw1dpKGfp%2FRDtaLGdSxIyfyVRKsDrnXaxJ1pThYLQUHgdFbDayh0s0EZQIukQCTImRsxg1VO9LaxnaK1Ow2dgvEaVrnp6VkMb3egkavUUFXtrEgFZKkmBHGGOz8gJ7Upvt3LBtDEharHB0FxqWzpKRw4kuaDPJEP89PzPzIX%2F3efn0NmOSA%2BExk3HvaqCBETTXenM3zyJJ6ZP7DKvQ0jlsOtsI2rYCnRXiGnw%2Bt92Km6Bi6XUA4oq2HmJbJbKF3O7i1zhRe0eIRtVzjePNJbNG4XRCH7zCiMTeaSaqkWM2QN728Hstu5avoGKXezZV1PtY10G2191bfIPhEHB%2FgBwi%2FrjNwjUPAT62Qvs6sCe3sy79ZlFYn2VP0NA5iUYALP55YyHGL1IUQlwZqtyjGMWjgzXzEQnTlgJ6RhleZ%2FNjOdo8uXhltlUmS2kOz3Wmm%2BPyuQJKr06ESKUqi%2FbsMq61HxhHfv3ZEdGVi2uqIr5WO436%2BKF23Gdb%2FTEBnrz41zqLVhUAAHLndCDWfPDHWrdTSAowcKH%2FIWscDLPYF%2BnSAZH6J3i4kG4ZtRT1EV7%2BFqiFjl6RvY0HkKh2MascIa73X1LL%2Bzi0GeNJZ0UMNampdMGOqUB%2Fmhr536AMGD8eDgcRhdizLO2ATX1WhcpgDERY8y9drBlQMfYibWLer%2Fgo7n5%2B4Jb07hWoX8GL8QP9WJOb9izXHGK5FyVgswy4YTrFCw9UFYwuBeC0ROK8GR9ufQTbOxHBO3oFCNLOxfwjQhcc0P0gZ4spNx9CGtq5GhKdJu1iHFmMWXuHrA%2F25cKwpCkDJDcwAcEIX6rUX83jvP%2FcPXwkGuii%2FbL&X-Amz-Signature=567f85de5b4facf7d63fd5a98803444a3867dfa5aeaa83b4a6b246a6b5750a91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MLITYT3%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T012232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoW3eqOA%2BaT%2BPfsawk5u6Rd3sdab%2FyBVBzQSAqlek5yAIgLWryucVUgRN%2BtEVeJfoxAJtTaKf5T5d9vbLLKOvQJuAq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDGrCKrqzCnqsvfeqzyrcAwS3g1roxGTlmZ3kcr%2FLVDwuw1dpKGfp%2FRDtaLGdSxIyfyVRKsDrnXaxJ1pThYLQUHgdFbDayh0s0EZQIukQCTImRsxg1VO9LaxnaK1Ow2dgvEaVrnp6VkMb3egkavUUFXtrEgFZKkmBHGGOz8gJ7Upvt3LBtDEharHB0FxqWzpKRw4kuaDPJEP89PzPzIX%2F3efn0NmOSA%2BExk3HvaqCBETTXenM3zyJJ6ZP7DKvQ0jlsOtsI2rYCnRXiGnw%2Bt92Km6Bi6XUA4oq2HmJbJbKF3O7i1zhRe0eIRtVzjePNJbNG4XRCH7zCiMTeaSaqkWM2QN728Hstu5avoGKXezZV1PtY10G2191bfIPhEHB%2FgBwi%2FrjNwjUPAT62Qvs6sCe3sy79ZlFYn2VP0NA5iUYALP55YyHGL1IUQlwZqtyjGMWjgzXzEQnTlgJ6RhleZ%2FNjOdo8uXhltlUmS2kOz3Wmm%2BPyuQJKr06ESKUqi%2FbsMq61HxhHfv3ZEdGVi2uqIr5WO436%2BKF23Gdb%2FTEBnrz41zqLVhUAAHLndCDWfPDHWrdTSAowcKH%2FIWscDLPYF%2BnSAZH6J3i4kG4ZtRT1EV7%2BFqiFjl6RvY0HkKh2MascIa73X1LL%2Bzi0GeNJZ0UMNampdMGOqUB%2Fmhr536AMGD8eDgcRhdizLO2ATX1WhcpgDERY8y9drBlQMfYibWLer%2Fgo7n5%2B4Jb07hWoX8GL8QP9WJOb9izXHGK5FyVgswy4YTrFCw9UFYwuBeC0ROK8GR9ufQTbOxHBO3oFCNLOxfwjQhcc0P0gZ4spNx9CGtq5GhKdJu1iHFmMWXuHrA%2F25cKwpCkDJDcwAcEIX6rUX83jvP%2FcPXwkGuii%2FbL&X-Amz-Signature=d523ff1418ddc2f89a25302a0f796479c54cac706de1d11e649402404497447e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
