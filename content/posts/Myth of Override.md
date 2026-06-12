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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCG2UDOT%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T021318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCVxCjdTT%2FK4Wr2IUDDDZ%2FYrVCFST2X23dE6rxWLFpXuwIgSBEn7uOHSs3Plsyw%2B0sdqb3pe%2F%2BrtKXc6h5aC0FbRBYq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDJH3VQUk%2BQjyV1cpuSrcAz%2BeN7DpBvstqkC%2BFzQX%2Fh5OsqzyDH9KDV2HkJ1yCwMMM%2BSW6bTBElW3HYtS%2BWaGjjlDgGKJO30EhYoCgciN%2FAtLz8pgHeKocIL6mGH%2F7mLcNG6rgX%2BPFLBqs37JPEwTWj06UI1fhEa5wvnVTv3HWTF%2B542jI5jjzyoix6oG1w%2F3oGZoFQfr3xmMgYpM200BmQVPbSD0dgs11pPB%2FvSubwWwsVWoXXBruCFUPkkeQH4ZDZyHDOdrQxm7iA9IjbGWKnV6AC7OH8HoarvwJBfBfXZ%2FZ1riPDcqoAJ%2Bd7e%2B9CF2EuINQFN%2Br8DweEt%2FxXpGVoC6ciwOXrWHmuuxbzPRRz3aV3HMNdtxNAsqwK0rS96roqpTAB1P%2FsGM5jr5aae3ApykH0E8TwAbqJZIMc5BzJOD4jaM7XFJBzWmoGsLT3iQXHGJyuLTDgN4n75iz5LjZSl%2BpSVoZ2ckcVlnLo4cQMlOqVcqz%2FhpvkdHhMbMi5QBm2k3lV8bG21v%2Fzp0ztF9bgLOnYPgxq8nyPKw0pZWqcP0GjvdJ05iE7yflR%2BauGdyy1gVVgSWv9wzucBXcvcZKKDDBMV%2FKTj8c05N58a7sTXkGwXZ5H%2BOxmQ%2BzjDJPR48Ec9WIHQcUcH%2F47tSMLvLrdEGOqUB%2Ba5hKmznKZYVKWDvzu0%2BrvwNJaxgapdwRRSk4FIe%2F9NMg0VmZuT40Gsq%2FxmCku5L5VAuXLEkOqsunajsNPoKalyc6DZQf4W0%2F%2BcfTuM9ebFQDBysJgEBthaEDs%2FhLnwJjsvaGitce%2F%2F3QQ4A6w66zJL%2BYlftQQO7RDCYpLjzfEU24pvKWJnOJWaC3bMAafKemaav1C5GrWl8eCjYvFk9mrHBxPdJ&X-Amz-Signature=d3e38622f7051b36b686e7696a54e94b1c51af1b320ac49211e441b6d1995a00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCG2UDOT%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T021318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCVxCjdTT%2FK4Wr2IUDDDZ%2FYrVCFST2X23dE6rxWLFpXuwIgSBEn7uOHSs3Plsyw%2B0sdqb3pe%2F%2BrtKXc6h5aC0FbRBYq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDJH3VQUk%2BQjyV1cpuSrcAz%2BeN7DpBvstqkC%2BFzQX%2Fh5OsqzyDH9KDV2HkJ1yCwMMM%2BSW6bTBElW3HYtS%2BWaGjjlDgGKJO30EhYoCgciN%2FAtLz8pgHeKocIL6mGH%2F7mLcNG6rgX%2BPFLBqs37JPEwTWj06UI1fhEa5wvnVTv3HWTF%2B542jI5jjzyoix6oG1w%2F3oGZoFQfr3xmMgYpM200BmQVPbSD0dgs11pPB%2FvSubwWwsVWoXXBruCFUPkkeQH4ZDZyHDOdrQxm7iA9IjbGWKnV6AC7OH8HoarvwJBfBfXZ%2FZ1riPDcqoAJ%2Bd7e%2B9CF2EuINQFN%2Br8DweEt%2FxXpGVoC6ciwOXrWHmuuxbzPRRz3aV3HMNdtxNAsqwK0rS96roqpTAB1P%2FsGM5jr5aae3ApykH0E8TwAbqJZIMc5BzJOD4jaM7XFJBzWmoGsLT3iQXHGJyuLTDgN4n75iz5LjZSl%2BpSVoZ2ckcVlnLo4cQMlOqVcqz%2FhpvkdHhMbMi5QBm2k3lV8bG21v%2Fzp0ztF9bgLOnYPgxq8nyPKw0pZWqcP0GjvdJ05iE7yflR%2BauGdyy1gVVgSWv9wzucBXcvcZKKDDBMV%2FKTj8c05N58a7sTXkGwXZ5H%2BOxmQ%2BzjDJPR48Ec9WIHQcUcH%2F47tSMLvLrdEGOqUB%2Ba5hKmznKZYVKWDvzu0%2BrvwNJaxgapdwRRSk4FIe%2F9NMg0VmZuT40Gsq%2FxmCku5L5VAuXLEkOqsunajsNPoKalyc6DZQf4W0%2F%2BcfTuM9ebFQDBysJgEBthaEDs%2FhLnwJjsvaGitce%2F%2F3QQ4A6w66zJL%2BYlftQQO7RDCYpLjzfEU24pvKWJnOJWaC3bMAafKemaav1C5GrWl8eCjYvFk9mrHBxPdJ&X-Amz-Signature=e46b29f4a29a3299569998352b44f4b0b277a1edc6f8be3a2d27a217ca9222d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
