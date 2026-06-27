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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7YZN3KS%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T111916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXQfQTpkwXSkBLHsp0avhBwDKZZa1MEX70At94mYQOsAIgR2aK8UoBTtJXd%2B9Hl28Jm3UkKfBhvQCtuhAMXtB7QGoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJRF25PkaHIzPhTcgCrcA6pwaOUi%2Ftns6cHqhEWrah8M8eO%2F%2F7Yzc8D9otf0Re6POlxgztJgSKRB1zJCCe7IPno0NwxM7lU12Jtaklaq89lvYgF5i3A8sZPBl9XdKZXGRt0xQ53r%2FOQ7FGZnLpDqXo0tbRp%2B57w5p6KYKsppxKCjUQGibtsn19eDqZXbT8GHJveTI4cTIDBMdYZdRxIxawBemoFsfANZkM61tMO%2FkmG%2BXWTlLXjZQL9JxavfEXe%2F1NsAQsRXEMygIGkz0KTR5tsZVBtHlTgqYK81DkKpgOs8%2BkFVcCGSuxEv8r8Sw4Qv3ZkFnVzxCxvacCTuAolCOYmKpPwZjyc85v3RAv%2F0b2MRnTki%2FdbU5lY4I7KYswkFPnUhztJRDBSnUmAI4difBH8%2FZKiPPaucrYE9slAtsZxQBaDaw0LlF2jTltIJ8QzdCQGeMOfnLWdJTy9v6xdnfRh2uWVgedW%2FuGkYGbptZiDVB%2BEcAOQnnXZrTx5slhsCpX6x4jWBtM%2FMCgBYf7J8xDLesD9YO7H7mmgW%2BLGDyY6jCdl%2FhftKapMceWWoTEk7%2BEO9ilY4pM7ItT8EDh9PmTP%2BRNPzCESzrAW8Y%2Bcs%2FMlppabjU4B%2FA%2B0cLHW3bduHE2ViX8VOxrWwUEDzMLDG%2FtEGOqUBROQ7%2F89nOaaG1CHki4fVL0zxgLYaKjCOe5UzEWbFCGJo1C8L%2FKPelyvVQ1G26IEUrq%2Bmz1SD1khAP0O6gyBmBBsph5Xw6pMMu3wWCpIardNyFIpSobd7yKWQf0SFStHq4LanpEM4OMCmzozHG0Xc4cFVkvlwGNr93PDCKvJ9EcFKr5XrGPq2PLycxDk%2BAB0bnPH61SJtj3kVac7%2FwRmog2cQFVr7&X-Amz-Signature=2cd1009f74da2de21ef990fe3d535bbb24401106d31a6d13344bb0c48d046f74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7YZN3KS%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T111916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXQfQTpkwXSkBLHsp0avhBwDKZZa1MEX70At94mYQOsAIgR2aK8UoBTtJXd%2B9Hl28Jm3UkKfBhvQCtuhAMXtB7QGoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJRF25PkaHIzPhTcgCrcA6pwaOUi%2Ftns6cHqhEWrah8M8eO%2F%2F7Yzc8D9otf0Re6POlxgztJgSKRB1zJCCe7IPno0NwxM7lU12Jtaklaq89lvYgF5i3A8sZPBl9XdKZXGRt0xQ53r%2FOQ7FGZnLpDqXo0tbRp%2B57w5p6KYKsppxKCjUQGibtsn19eDqZXbT8GHJveTI4cTIDBMdYZdRxIxawBemoFsfANZkM61tMO%2FkmG%2BXWTlLXjZQL9JxavfEXe%2F1NsAQsRXEMygIGkz0KTR5tsZVBtHlTgqYK81DkKpgOs8%2BkFVcCGSuxEv8r8Sw4Qv3ZkFnVzxCxvacCTuAolCOYmKpPwZjyc85v3RAv%2F0b2MRnTki%2FdbU5lY4I7KYswkFPnUhztJRDBSnUmAI4difBH8%2FZKiPPaucrYE9slAtsZxQBaDaw0LlF2jTltIJ8QzdCQGeMOfnLWdJTy9v6xdnfRh2uWVgedW%2FuGkYGbptZiDVB%2BEcAOQnnXZrTx5slhsCpX6x4jWBtM%2FMCgBYf7J8xDLesD9YO7H7mmgW%2BLGDyY6jCdl%2FhftKapMceWWoTEk7%2BEO9ilY4pM7ItT8EDh9PmTP%2BRNPzCESzrAW8Y%2Bcs%2FMlppabjU4B%2FA%2B0cLHW3bduHE2ViX8VOxrWwUEDzMLDG%2FtEGOqUBROQ7%2F89nOaaG1CHki4fVL0zxgLYaKjCOe5UzEWbFCGJo1C8L%2FKPelyvVQ1G26IEUrq%2Bmz1SD1khAP0O6gyBmBBsph5Xw6pMMu3wWCpIardNyFIpSobd7yKWQf0SFStHq4LanpEM4OMCmzozHG0Xc4cFVkvlwGNr93PDCKvJ9EcFKr5XrGPq2PLycxDk%2BAB0bnPH61SJtj3kVac7%2FwRmog2cQFVr7&X-Amz-Signature=0f3b80b40bc42eb45ba6288812ee92a8cb53778e7f23f061e3137903be95a030&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
