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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXKGFFW%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T231911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCH3LG2elMDFyGRrA7FWzfZrd1UhyeMENnyhKfw2qRBNoCIQDFY7XdxcJ052KUoNxp4Ox6Kpw6LXzKDdVIaR2RhsqNTyqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb%2F50xqobeeOD%2B8SLKtwDHkQSpVPbdYfOBCgNMujNpfzrrv9fZlm7nThLAUTKFBfuyP7tK7EhG0Ya2mm%2B8mV7b3IVgLGJ%2BflIHXgUzJq%2FA4zVuCFW18HMPm0kscCtuQL0oUcZsph2CsbEhW0zfVHA4d2eduuwgnNYdW7yG%2FWPIVYy5qT9DtRRrYQsyQTP6bAIdxNxs5Hi2M%2BVTeScMNgQqoTwJGS6TKgCDmvHBA%2BmERN3n5UIGDSfallFQrRh0O3CUVIvrSvB%2B2n1ue%2F4YsSgNRNLAxxk3bPuprlHcl%2FAJOEQso%2BLzy8dSQ68YSYe1tmyBeLINJHGk8VBu5eA0DStX5qxUPUY5m5Cr9I0S8iCzZbK%2F3DKdLTWsVqmfWXm6cemNXobvIC5QbfekDncPQcVkcuAOkXq2kifBev0KBWJvESpUZHtMMighxqYIhiWkIO06q2t6iqHdxMg2U9dpFr2jfyF%2B%2BqNYGrM%2BbxeN6yONe%2BBtJZMCyjRVzGIPulLRAErTUPGU%2F%2FowWR8t6juyt6PdN409gFEbEeriZGb9b3SeoPYoc1Whwd7AMbCVfOId90kC3i5PH7rLh5BA1ghhe9bKFN6m6yHQRHDCtSNxw%2BM%2FylLdr0hg%2BgjHRUOcPjawivQDof8ZyR568EuE5kw07en0QY6pgEf14j2fDQujHVXxgiXnhGei3UsltfXKekhJK4ntqNnlv0hSac%2BMrX42Op7lYCrSSeNO1htFT7XXBkUvIzIZRN0soeLzqNaXUPqRuwHOY4x%2B5w0fXBL6zpEuf9OWnT66Vw9IKnlK09bvliPPbylKfZxzJZY8isFxTY8ItuRGeQZvU517C5DQQuGk0ifggb9eEYpMllEJTJ%2Ff17OtW2tuvf9s%2Bon9J7d&X-Amz-Signature=0513e60845b1ecf7373ff8af42ac8bc7c7714e10ad4cef902ff97ebd3a827ca1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTXKGFFW%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T231911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCH3LG2elMDFyGRrA7FWzfZrd1UhyeMENnyhKfw2qRBNoCIQDFY7XdxcJ052KUoNxp4Ox6Kpw6LXzKDdVIaR2RhsqNTyqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb%2F50xqobeeOD%2B8SLKtwDHkQSpVPbdYfOBCgNMujNpfzrrv9fZlm7nThLAUTKFBfuyP7tK7EhG0Ya2mm%2B8mV7b3IVgLGJ%2BflIHXgUzJq%2FA4zVuCFW18HMPm0kscCtuQL0oUcZsph2CsbEhW0zfVHA4d2eduuwgnNYdW7yG%2FWPIVYy5qT9DtRRrYQsyQTP6bAIdxNxs5Hi2M%2BVTeScMNgQqoTwJGS6TKgCDmvHBA%2BmERN3n5UIGDSfallFQrRh0O3CUVIvrSvB%2B2n1ue%2F4YsSgNRNLAxxk3bPuprlHcl%2FAJOEQso%2BLzy8dSQ68YSYe1tmyBeLINJHGk8VBu5eA0DStX5qxUPUY5m5Cr9I0S8iCzZbK%2F3DKdLTWsVqmfWXm6cemNXobvIC5QbfekDncPQcVkcuAOkXq2kifBev0KBWJvESpUZHtMMighxqYIhiWkIO06q2t6iqHdxMg2U9dpFr2jfyF%2B%2BqNYGrM%2BbxeN6yONe%2BBtJZMCyjRVzGIPulLRAErTUPGU%2F%2FowWR8t6juyt6PdN409gFEbEeriZGb9b3SeoPYoc1Whwd7AMbCVfOId90kC3i5PH7rLh5BA1ghhe9bKFN6m6yHQRHDCtSNxw%2BM%2FylLdr0hg%2BgjHRUOcPjawivQDof8ZyR568EuE5kw07en0QY6pgEf14j2fDQujHVXxgiXnhGei3UsltfXKekhJK4ntqNnlv0hSac%2BMrX42Op7lYCrSSeNO1htFT7XXBkUvIzIZRN0soeLzqNaXUPqRuwHOY4x%2B5w0fXBL6zpEuf9OWnT66Vw9IKnlK09bvliPPbylKfZxzJZY8isFxTY8ItuRGeQZvU517C5DQQuGk0ifggb9eEYpMllEJTJ%2Ff17OtW2tuvf9s%2Bon9J7d&X-Amz-Signature=75683622adc25026cd9047ae4f9669a1bc5557887d5b29228c8aba82cd32cf6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
