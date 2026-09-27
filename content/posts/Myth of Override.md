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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EPMRLVA%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T223914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDH%2FvF3OUrO0GGADukn0cdl1ir8Ups5Uy3N77AQJrpdfwIgPZXqGGkU%2B0kyusuDpXckvJJcg5v4acKb%2BRlz%2ByAKF4oq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNE0L95Pa9OIu5s1jircAy3i5JJkH%2Bek8jCaOWzl1vppOZqsWUu7bef2uL%2BQi40TO%2FDq5CXgFfDA%2FRkW4Vx%2FK35COH4VmIdrk807e%2Fy0TXMI2aKxOyYs5Y0FSuHxAO8Cy%2FyKLRNsQr%2FwU88q5hd7iK1ivb8OB74hYHQPY6FC68TVSevtkuouTknuRHcnI4KEkuFuRIlgh7aE6dLzq3Ym%2Bm02nj9OxMeZTx3zDaDeWfY%2FT9BnPKj2Aaf4w4FQNeX%2F7e%2BMoP84bkYGHeMGYPwAUTcVDq%2Bggk7wRusLlhhvBcxACNGBWQ%2BSFY9XqrfDDjQ2UUArERoFYfqvMt4mvm2%2FYfm6KVdlUvATNe1VRMGIzASnWjfGvmFkg1zPpEQNjSN28jqoXd0NRS5o2zolqLlAMn6ms4wwDbP%2FBn%2FLI3nlMkyxAEr7u9Vpu5MizYJdcfVshtZhxkNRmXiVGGJe18Xf8zPEI%2BJV%2FgLVrbK3UdMAdOaaxwiLG%2BQgEzi4W5HQPwPiXgDSpNvH%2FP%2FA92%2FGExhEdG1tely4JjRL6H%2FTgWsHn4awGsiAQRToGaf7Eguunb7OJ0%2BV8FWUk5xiABp6mrbb8PMtvQFqK06SdEbCqBkM0IsM%2FnRw%2F6k5FBGvlbeOFcTSB6EnHLivTY%2FzuiXvMIOI5tUGOqUBcclrskI8Znl6IFAobHcmhhoxd3nPhAQcjFClDnqsAGGsdsqX6%2FB%2FuOwnLItgk2HwHYLaPFZVVX1cicFGO0JmorTmv6CCcyrebOZrO%2BCBR062OhpLXFxJ1l2BtYd4f7Kf8gWf94DzdTMsV%2F6dmiXiVa%2FM0MMgo2%2FY5T4H7k9Z6NHSEB3AmUjArqD0ctn%2F0%2FS0rxbdzXQlogtT0tpmYwQ1QHDWx%2FsY&X-Amz-Signature=abf8f9b0c393fbe94bfb4cf78ff7f438fe4e931d7706bc9f0abed9e17de3b7ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EPMRLVA%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T223914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDH%2FvF3OUrO0GGADukn0cdl1ir8Ups5Uy3N77AQJrpdfwIgPZXqGGkU%2B0kyusuDpXckvJJcg5v4acKb%2BRlz%2ByAKF4oq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDNE0L95Pa9OIu5s1jircAy3i5JJkH%2Bek8jCaOWzl1vppOZqsWUu7bef2uL%2BQi40TO%2FDq5CXgFfDA%2FRkW4Vx%2FK35COH4VmIdrk807e%2Fy0TXMI2aKxOyYs5Y0FSuHxAO8Cy%2FyKLRNsQr%2FwU88q5hd7iK1ivb8OB74hYHQPY6FC68TVSevtkuouTknuRHcnI4KEkuFuRIlgh7aE6dLzq3Ym%2Bm02nj9OxMeZTx3zDaDeWfY%2FT9BnPKj2Aaf4w4FQNeX%2F7e%2BMoP84bkYGHeMGYPwAUTcVDq%2Bggk7wRusLlhhvBcxACNGBWQ%2BSFY9XqrfDDjQ2UUArERoFYfqvMt4mvm2%2FYfm6KVdlUvATNe1VRMGIzASnWjfGvmFkg1zPpEQNjSN28jqoXd0NRS5o2zolqLlAMn6ms4wwDbP%2FBn%2FLI3nlMkyxAEr7u9Vpu5MizYJdcfVshtZhxkNRmXiVGGJe18Xf8zPEI%2BJV%2FgLVrbK3UdMAdOaaxwiLG%2BQgEzi4W5HQPwPiXgDSpNvH%2FP%2FA92%2FGExhEdG1tely4JjRL6H%2FTgWsHn4awGsiAQRToGaf7Eguunb7OJ0%2BV8FWUk5xiABp6mrbb8PMtvQFqK06SdEbCqBkM0IsM%2FnRw%2F6k5FBGvlbeOFcTSB6EnHLivTY%2FzuiXvMIOI5tUGOqUBcclrskI8Znl6IFAobHcmhhoxd3nPhAQcjFClDnqsAGGsdsqX6%2FB%2FuOwnLItgk2HwHYLaPFZVVX1cicFGO0JmorTmv6CCcyrebOZrO%2BCBR062OhpLXFxJ1l2BtYd4f7Kf8gWf94DzdTMsV%2F6dmiXiVa%2FM0MMgo2%2FY5T4H7k9Z6NHSEB3AmUjArqD0ctn%2F0%2FS0rxbdzXQlogtT0tpmYwQ1QHDWx%2FsY&X-Amz-Signature=9683762d231869a1ae2593e123c6c7a371e98f949d16d51a3d73f3b325fa8ef8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
