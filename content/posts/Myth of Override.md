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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA5F5EC%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T180359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEH0f9934WNy%2BzwcUPR9MJuu%2B58uc0WuNSKiu9vF%2FTAIhAOZO1ENEvxMNfuMWm8nuPFWPMH1oIPLHBv92E9ZzmaG9Kv8DCFoQABoMNjM3NDIzMTgzODA1Igys9PCLT3t1vWfg5Ycq3ANbPOmyrRxSLGjAbU637WiFnAR0RVdwLy4HJD9jGqcWA9FDNVtbIWgva8A%2FWV2lOyPIORBO47JyBH3zkqcvH7ZE0lb3oXfzYgoh3bJJZw4d1OyyHtKbtPMZDdGxmGd5GqWJ6keQqx3yTAaO9xRm%2BvV05EfCaKSwio7vt%2BQuW8wwm%2Bgt3ia7naAx3J4AF8ZgTrUBFPqehvN9gecMLG7ipvrtMFF8BdBSYMOQNsA973wKPfSMMMh59D38Fm2muVSY9irEA4EEDvHGOoXtFVm26pFGn7DkAa5YitF1%2BwF9zuqkitMOEWR7Y7T4smLwYXYjDS6pJNC1l91w2SBP5qtHkLGURkWjG%2BJPxOcZeVgJB4vX50dmyeo%2FZsezArL6hPbaj5VRUiHh2UAuQv6P6TOzBrs3%2BzKWweLTtrIdfSpQwiPAtR%2F8GF4uD81uKV2rJ9w%2Bl4H3pwIT1tPa6ZlCthJurA1HjY98rD%2FOkpWAEcILQkR3%2BiH5Udyt28hzgdHjGxQ1QxMxGIZiehiFMztb%2F%2Bb8UGYXN7EOptp1loHc8JsLqo5MCMve9UJOxkbUPVZDXt7pwDcLhaaRStWJnjR%2Bo5As5ZKuX93I7QPqKqFwPShkAArkxsNot3DEABHzZZejyjC9s6%2FSBjqkAf1tkofiHUcWf%2BVAbA2Iq2%2Bgo%2FxATH86LHu08RdxRLtM3JOqY8hJnSLoCs9eMve8pqk2gCjzRIxzzk%2FHXpgJmRNKnnsSaN8T1va5uYiNeTMlQsnAZIt9sPOmbbsaXKu%2BPtqRgV05Gb3VAh%2F00SC1txz2ZfAaVHRRCpCF5O3h%2BuX8ilwYVScMYWl0QbbrYhI3hlnCuRbSfKWYpYaaA4jbocNZCrVX&X-Amz-Signature=4a85977d6358dd81512bdbb712d3dc815121044506910841af863b964dea7eea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTA5F5EC%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T180359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEH0f9934WNy%2BzwcUPR9MJuu%2B58uc0WuNSKiu9vF%2FTAIhAOZO1ENEvxMNfuMWm8nuPFWPMH1oIPLHBv92E9ZzmaG9Kv8DCFoQABoMNjM3NDIzMTgzODA1Igys9PCLT3t1vWfg5Ycq3ANbPOmyrRxSLGjAbU637WiFnAR0RVdwLy4HJD9jGqcWA9FDNVtbIWgva8A%2FWV2lOyPIORBO47JyBH3zkqcvH7ZE0lb3oXfzYgoh3bJJZw4d1OyyHtKbtPMZDdGxmGd5GqWJ6keQqx3yTAaO9xRm%2BvV05EfCaKSwio7vt%2BQuW8wwm%2Bgt3ia7naAx3J4AF8ZgTrUBFPqehvN9gecMLG7ipvrtMFF8BdBSYMOQNsA973wKPfSMMMh59D38Fm2muVSY9irEA4EEDvHGOoXtFVm26pFGn7DkAa5YitF1%2BwF9zuqkitMOEWR7Y7T4smLwYXYjDS6pJNC1l91w2SBP5qtHkLGURkWjG%2BJPxOcZeVgJB4vX50dmyeo%2FZsezArL6hPbaj5VRUiHh2UAuQv6P6TOzBrs3%2BzKWweLTtrIdfSpQwiPAtR%2F8GF4uD81uKV2rJ9w%2Bl4H3pwIT1tPa6ZlCthJurA1HjY98rD%2FOkpWAEcILQkR3%2BiH5Udyt28hzgdHjGxQ1QxMxGIZiehiFMztb%2F%2Bb8UGYXN7EOptp1loHc8JsLqo5MCMve9UJOxkbUPVZDXt7pwDcLhaaRStWJnjR%2Bo5As5ZKuX93I7QPqKqFwPShkAArkxsNot3DEABHzZZejyjC9s6%2FSBjqkAf1tkofiHUcWf%2BVAbA2Iq2%2Bgo%2FxATH86LHu08RdxRLtM3JOqY8hJnSLoCs9eMve8pqk2gCjzRIxzzk%2FHXpgJmRNKnnsSaN8T1va5uYiNeTMlQsnAZIt9sPOmbbsaXKu%2BPtqRgV05Gb3VAh%2F00SC1txz2ZfAaVHRRCpCF5O3h%2BuX8ilwYVScMYWl0QbbrYhI3hlnCuRbSfKWYpYaaA4jbocNZCrVX&X-Amz-Signature=2e7ecf7ba194d62e7f25194814be066a3606f5cf6d05dbe6fd40c5c51715331f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
