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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CRPJ3HQ%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T045345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQDKFTt6wWx7Pkiik05zbbaG9AGzi8tCMwXq2peeMFmirwIgTqKDh3GRQwE4Q3I7YZPS4gCoJktXz6vgKNUErHA0EC0q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDEQAfmR2ZqR1GYYAeyrcA0lPuGmEvatwt1exS1kQ%2FmqRQhhxv0FzEKe72GaPFMSxmYFx5V63sQnYTyhGEo2Vq9%2Fc671lbuW%2FIPgBp%2BJvZj4U%2FpPhewVfwherJ0sDwr%2BuW%2BeNTERQtmAGcwT7o6jDbDDVpdon2X5LlEG0EqrBlbLfGClV4woHM50h3LknWHDGicon70hF162ppz5IVRQkpEp9YZ84yku9hw51BkFS3w61%2BAgv2ET85lY1xuy1KPpJ5JCRijzxoGpCXtLnLZSO%2F%2BcRuA14NZCo9w%2BetAWPSZkzXdudRTcXYzn7RTrRIKuR6wWdBjWTiUOyI3RrLMpcsdV0IcSL%2BVmw3Sn6er%2BmSems8XRzxZzFBN7943oYDYhok%2FyiW%2Ff7rcsAyHswlMa7u4NcUYy8wxAeYMZ4PgcxijZ4RNFeIGKrwvxMsYVdAdvRFSGZ50j4Ho%2F39q%2FngWG0cb84gyqAHR0tP5IGv5Ybq%2B5%2BUk2MBFpc1HEH9laHO0iDt%2FXXstdh6yRNLgKry5L4ejflGb8NhQawktRqGScyETSzHOD1uPHC7CDtcivumwjRs9u%2FnvTpNO749G6kx5R2rrUU46BcQMVALwxVaxJZvWuo7HYXj8yD9EQhrs0%2F3Q0bPAGFfmIJhQOK6vYWMPbqytMGOqUBLj5s2RHyE5%2Fsx5rQ6ANBZPQzwqV%2FQTsfEuvwQn5nFyWtvSF4okVECo%2FZQjw%2BwcFE9hc9P9AlZu9i%2F3EJv66%2FftZdQOEA%2FrgoHf1HIXEByUjDiCRz%2FtX2oDO5pS308aBCdn%2B60rtpamC6GykN5ZporUWzR9jM%2BVLTD7eLk39lZxgTYl4wzZ61KLMF7smc7FWy7QtE3fva5WmQVZx9JsuMmfeeJu8d&X-Amz-Signature=d0395dccdb64291867f364f086f24b9e334d27ab36f8e35b3363f9acd05ae4e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CRPJ3HQ%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T045345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQDKFTt6wWx7Pkiik05zbbaG9AGzi8tCMwXq2peeMFmirwIgTqKDh3GRQwE4Q3I7YZPS4gCoJktXz6vgKNUErHA0EC0q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDEQAfmR2ZqR1GYYAeyrcA0lPuGmEvatwt1exS1kQ%2FmqRQhhxv0FzEKe72GaPFMSxmYFx5V63sQnYTyhGEo2Vq9%2Fc671lbuW%2FIPgBp%2BJvZj4U%2FpPhewVfwherJ0sDwr%2BuW%2BeNTERQtmAGcwT7o6jDbDDVpdon2X5LlEG0EqrBlbLfGClV4woHM50h3LknWHDGicon70hF162ppz5IVRQkpEp9YZ84yku9hw51BkFS3w61%2BAgv2ET85lY1xuy1KPpJ5JCRijzxoGpCXtLnLZSO%2F%2BcRuA14NZCo9w%2BetAWPSZkzXdudRTcXYzn7RTrRIKuR6wWdBjWTiUOyI3RrLMpcsdV0IcSL%2BVmw3Sn6er%2BmSems8XRzxZzFBN7943oYDYhok%2FyiW%2Ff7rcsAyHswlMa7u4NcUYy8wxAeYMZ4PgcxijZ4RNFeIGKrwvxMsYVdAdvRFSGZ50j4Ho%2F39q%2FngWG0cb84gyqAHR0tP5IGv5Ybq%2B5%2BUk2MBFpc1HEH9laHO0iDt%2FXXstdh6yRNLgKry5L4ejflGb8NhQawktRqGScyETSzHOD1uPHC7CDtcivumwjRs9u%2FnvTpNO749G6kx5R2rrUU46BcQMVALwxVaxJZvWuo7HYXj8yD9EQhrs0%2F3Q0bPAGFfmIJhQOK6vYWMPbqytMGOqUBLj5s2RHyE5%2Fsx5rQ6ANBZPQzwqV%2FQTsfEuvwQn5nFyWtvSF4okVECo%2FZQjw%2BwcFE9hc9P9AlZu9i%2F3EJv66%2FftZdQOEA%2FrgoHf1HIXEByUjDiCRz%2FtX2oDO5pS308aBCdn%2B60rtpamC6GykN5ZporUWzR9jM%2BVLTD7eLk39lZxgTYl4wzZ61KLMF7smc7FWy7QtE3fva5WmQVZx9JsuMmfeeJu8d&X-Amz-Signature=57e9cf253222aaf96a9a21b429af0dc8c1907820e224df0bc9fac8c43e5bd982&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
