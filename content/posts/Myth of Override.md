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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JCD76A5%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T122123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNhD50hKckFJUr9OPYqLs8F8UxZSyvA9NnZT24bTsqAIgGwOFyWFWXYiq0cftKReXmKUy7c7NLGd%2FNevh0U2yihIq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDFsNGLWX%2FpIq8TO43CrcA2S4xKO%2BAOPOhlVZd%2FtDfWZHdUV40VSu4DdiAcz9ckaJ0Cq5U1OLKo%2Bvs8HHcm7TTY4vRCcv8%2F6PFkZUJIW3d9iAv%2B8pN0czfiD%2Fp3USRr8lOSwbOPqK4NY8bglcxfC6Uu6JOy5h6uYeoLHVQgWJ54RHrDfwvclPKXI4oJmjncP1ogM2Wp2TDbmOrWs1sMk4huaY%2FUqSMAj2BoVYyU52R%2Fq6%2FzHL%2FX6TdRexmgOw%2BfWYUD%2BmpUURR1gpvS3y%2BcIqh%2F%2FIJnZehwgREnlAdsZajYux7LahAl5AcBkZpOooJwX9AwTT2CiKcUz03XYtAaSAPjFM9yt81PUAWDtpaphM0A%2BXoKZ1UVIZzLBKrA6sGJogcgTY124kvRL2RQ7Es6OdbEoUIxhS4PEvyt4EhrRyb1DaYmMN27Vh1Mgr8bI4z5zkxqsGeVIFcSBXz09uuxlxGemIXueW8dmQ71a3Gl3d8%2F3Lmq0O41qw%2FbEStKRvg1CvBHaTGi5x%2FNPza5061vnRcVOxjkUS1sOT94kEk2aJiS3SXCrs1BqpqgFShIBcfmHS3LMb%2FALhw3B2%2BGKI1q%2BrwgS1n8%2FWw528C8wtbF%2FQ4VFMa9sr8tTMwG0d176cCHmB%2Fzmy8L9YBoInai2WMPi6s9IGOqUBGF8zPz9uSJkgp%2B1wkaCLTWntQvoNrFDyQ8DiTDzwGjaTBM8P6AXwSVokoeQ%2BFNYGIIBVXuJtejKcnw5b%2F6M60FSXfvvjSFTmF7iheumI3q6gl71FiDwEoFAj%2BYWFMhizhGQPQiL%2BsdU4PSSwaaPWFHt79QJt4viTqLF1YeWu%2FZHbsVhp80THpHcD2fvRD1jjux%2B8WqjNGE%2BFlHffq1KuN6fZpwkJ&X-Amz-Signature=185c926efb8e4b156eec44fcd349e952dc38dd2fb8ef660ccfa67553914c2b67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JCD76A5%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T122123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNhD50hKckFJUr9OPYqLs8F8UxZSyvA9NnZT24bTsqAIgGwOFyWFWXYiq0cftKReXmKUy7c7NLGd%2FNevh0U2yihIq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDFsNGLWX%2FpIq8TO43CrcA2S4xKO%2BAOPOhlVZd%2FtDfWZHdUV40VSu4DdiAcz9ckaJ0Cq5U1OLKo%2Bvs8HHcm7TTY4vRCcv8%2F6PFkZUJIW3d9iAv%2B8pN0czfiD%2Fp3USRr8lOSwbOPqK4NY8bglcxfC6Uu6JOy5h6uYeoLHVQgWJ54RHrDfwvclPKXI4oJmjncP1ogM2Wp2TDbmOrWs1sMk4huaY%2FUqSMAj2BoVYyU52R%2Fq6%2FzHL%2FX6TdRexmgOw%2BfWYUD%2BmpUURR1gpvS3y%2BcIqh%2F%2FIJnZehwgREnlAdsZajYux7LahAl5AcBkZpOooJwX9AwTT2CiKcUz03XYtAaSAPjFM9yt81PUAWDtpaphM0A%2BXoKZ1UVIZzLBKrA6sGJogcgTY124kvRL2RQ7Es6OdbEoUIxhS4PEvyt4EhrRyb1DaYmMN27Vh1Mgr8bI4z5zkxqsGeVIFcSBXz09uuxlxGemIXueW8dmQ71a3Gl3d8%2F3Lmq0O41qw%2FbEStKRvg1CvBHaTGi5x%2FNPza5061vnRcVOxjkUS1sOT94kEk2aJiS3SXCrs1BqpqgFShIBcfmHS3LMb%2FALhw3B2%2BGKI1q%2BrwgS1n8%2FWw528C8wtbF%2FQ4VFMa9sr8tTMwG0d176cCHmB%2Fzmy8L9YBoInai2WMPi6s9IGOqUBGF8zPz9uSJkgp%2B1wkaCLTWntQvoNrFDyQ8DiTDzwGjaTBM8P6AXwSVokoeQ%2BFNYGIIBVXuJtejKcnw5b%2F6M60FSXfvvjSFTmF7iheumI3q6gl71FiDwEoFAj%2BYWFMhizhGQPQiL%2BsdU4PSSwaaPWFHt79QJt4viTqLF1YeWu%2FZHbsVhp80THpHcD2fvRD1jjux%2B8WqjNGE%2BFlHffq1KuN6fZpwkJ&X-Amz-Signature=5a6bc63bf639057fda20955d089111b3a10634b8a6bdcc65fe6779b0e7db9e5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
