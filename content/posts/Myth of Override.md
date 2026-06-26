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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7C5V2LL%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T192731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGKiQk99bEmpdUdT1DmvEwklTNkKouWewBEbqsCTvaa9AiBvg%2F6vPwwntQtrCF1e7fh1HFKplbtIvy6pS%2FFv0E2GSyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM4yyNruxoFu7tSgP6KtwD1YTVHSU67pGQ5XpJ7SFDQc0k5YMqA7PmcFNoZ9GfPsiVZLb6KrBvdB9fjX7SCT4JpszdYYH3LHyCI%2FCKDKiVe6r1b10VQqjk2hafttgcJfRKjrbU9ODrHij9gu5vdX3EnGWd%2FiQsqaj5M2Jb4MyksGdoqVpqcOfZnkcXVtokbNSo8IPVLR8YzWrla6%2BBr33cjdNiiNOCvNBzY7RMr%2F%2FAXRRC6%2Bn3iC1N1W%2Bm6AgtZEzCBdHmCw6qeIiIGe3GaKpYt5LXj24IS6AiNxRGFia2q9UpXAwu9XIAJ2Wmpz0y7jVkTjBr%2B1l9iVzM1Kq7H1jjErQrOL2Lsy3m2j65T%2Bfq9lE5A1PHyHfUr2j5cnrCYrYhhZVlpufHLFPYT%2BXqb6L%2Brf%2BSqPTyjlcXxS%2FkV1yRolPgr%2FA7RF1%2BM3NpTGHO0oRMrS4GWgFNur4pUieoktD%2FiO3E3Nnxq639yMBNGSjtV%2BMO%2FoFhkAkh8zGC5udUrSvpHWcOmcnno8nNcSvfzRh0%2FN83cfUoKXetV%2FF3m79E8E2icZbmJff6vZuDNbBHrYQiU7LF3S5yiKiEMSG%2Ff5y9I5XpdneMMCHqkdYbF%2B1rVpyQuEhlEhaEMIIqd98cL8LaRtPvH%2FVxmXpaCTUwhJ770QY6pgFgU1VkVT87kQ8lfhnO7iTygIp02Z8RqoFAQM50DkThkEgAcDkH9caqUzstGcAV4ShSjv8QU7degipJxvtwi26jLgjkMM4jw9UJvuXk1%2B9PmkO1%2BIxC9m1kby613nvfJvOjjr4c7yfpVybQDgXME7IZuKod0BsPhegAG8j1auYcS0%2FyKKKWUuY3u%2F0eGASblgsGp4FXf7lzG%2FbI7FVUvThlg292cZNi&X-Amz-Signature=7af06bbf85405b28100196666b6cdc14f7369b1679d697f623bedaff310c1f8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7C5V2LL%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T192731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGKiQk99bEmpdUdT1DmvEwklTNkKouWewBEbqsCTvaa9AiBvg%2F6vPwwntQtrCF1e7fh1HFKplbtIvy6pS%2FFv0E2GSyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM4yyNruxoFu7tSgP6KtwD1YTVHSU67pGQ5XpJ7SFDQc0k5YMqA7PmcFNoZ9GfPsiVZLb6KrBvdB9fjX7SCT4JpszdYYH3LHyCI%2FCKDKiVe6r1b10VQqjk2hafttgcJfRKjrbU9ODrHij9gu5vdX3EnGWd%2FiQsqaj5M2Jb4MyksGdoqVpqcOfZnkcXVtokbNSo8IPVLR8YzWrla6%2BBr33cjdNiiNOCvNBzY7RMr%2F%2FAXRRC6%2Bn3iC1N1W%2Bm6AgtZEzCBdHmCw6qeIiIGe3GaKpYt5LXj24IS6AiNxRGFia2q9UpXAwu9XIAJ2Wmpz0y7jVkTjBr%2B1l9iVzM1Kq7H1jjErQrOL2Lsy3m2j65T%2Bfq9lE5A1PHyHfUr2j5cnrCYrYhhZVlpufHLFPYT%2BXqb6L%2Brf%2BSqPTyjlcXxS%2FkV1yRolPgr%2FA7RF1%2BM3NpTGHO0oRMrS4GWgFNur4pUieoktD%2FiO3E3Nnxq639yMBNGSjtV%2BMO%2FoFhkAkh8zGC5udUrSvpHWcOmcnno8nNcSvfzRh0%2FN83cfUoKXetV%2FF3m79E8E2icZbmJff6vZuDNbBHrYQiU7LF3S5yiKiEMSG%2Ff5y9I5XpdneMMCHqkdYbF%2B1rVpyQuEhlEhaEMIIqd98cL8LaRtPvH%2FVxmXpaCTUwhJ770QY6pgFgU1VkVT87kQ8lfhnO7iTygIp02Z8RqoFAQM50DkThkEgAcDkH9caqUzstGcAV4ShSjv8QU7degipJxvtwi26jLgjkMM4jw9UJvuXk1%2B9PmkO1%2BIxC9m1kby613nvfJvOjjr4c7yfpVybQDgXME7IZuKod0BsPhegAG8j1auYcS0%2FyKKKWUuY3u%2F0eGASblgsGp4FXf7lzG%2FbI7FVUvThlg292cZNi&X-Amz-Signature=7c295cf8aef43bab6d4fb6352ac94a84e61c9ad67fc40d139effd2231c41ecf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
