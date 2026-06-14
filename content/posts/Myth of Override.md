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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z34B2WVH%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T132514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIDyIlFnOr%2FolwE3qtuxF5O%2FktkgHSDY9asRQVPJMmGMUAiEAwbUK5n0fSEv1cO0uhEDUVHIpfzUnHwJuvfkiRgu59KIq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDAWpnzzptqn9huGEoSrcA0ONJcGYqjLSNxaFs0Te9cGkkZfkPjLpjZiOJeXoSXyK0kSxuWlZ7uxfeEwdxFjRd49xtzoPoKa36BT7ho6pGY%2FPRU2LZkFwSf6KXq3h8As7nbkAE%2BEiMGnloBWwxnYJckDKBnKnrSmOZynbt58YsPvqT6QHO5GJ2lG%2BZKk1MVj54O0wlvpou62nE4uonKcof9yE7yjK7O2dB%2Bw1n5vO0O%2FXB0yBqQ%2FJgH5NfYF%2FmCOifLZ%2FUhY0WdAUhDc6BfiiZ7YVq8vOF6llrSlg%2B0xbgKmC77kRvb6ie%2BNsIfsgLx3A62GVNCFTvhsx%2FJqoC2MRqtOFaLn2GxzJSKbm%2Fy5pnTk0kUQ6Ztm%2B0Yey1ogjzQWBq8vcsyNd0kGjYGA1nvZLv790is2y5e1fmtcXk48oaj97Qixo8yxRCHrugdaqErFTkFNeRdPOkwBXLY012jWwB0bj5HZv14k8UG%2FNQA%2FnRS4PUS6a%2BQ%2Bkk%2BtXEWUI4VBZrIqTvgMO7GOFmIHI2CkYiZcq%2Boz0JTHSg9%2BrglQLNq3d%2BvVufQaYlOyVAUW09EGASZ%2FLxjB%2BFekqdvobEPb9lKNGXNf7EiJ7zFSgmoVTxqS%2FV88OqL8syAG5eSIew9DiPU9DtanGQc%2BhFzRBML%2FFudEGOqUBfP9rvMS1AENyUMjrsI6yg6m8vLHcqWGSojhI%2Bt8Hd%2FU0G%2FTAgCY4%2FBUZUq5BGGDyJMvWLq6qpnCNrftqM3Ber%2B33vqFhHAjDPiUDjMcAYuFkbIr3H5%2Bn1ymZxRpnXmeEmC1Ww2Dt9DoXCn4YXnpPWLaRBAWxnKlPe08eCnPtVtviT2YaqD2s2zjkKJyfiMb0RLtaU7jbCSGaL47MKjtuTF4aZzvG&X-Amz-Signature=e3be8222d992139ef9e9f04f86af7d190e7840f14bbc0446572623a2cb69b275&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z34B2WVH%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T132514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIDyIlFnOr%2FolwE3qtuxF5O%2FktkgHSDY9asRQVPJMmGMUAiEAwbUK5n0fSEv1cO0uhEDUVHIpfzUnHwJuvfkiRgu59KIq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDAWpnzzptqn9huGEoSrcA0ONJcGYqjLSNxaFs0Te9cGkkZfkPjLpjZiOJeXoSXyK0kSxuWlZ7uxfeEwdxFjRd49xtzoPoKa36BT7ho6pGY%2FPRU2LZkFwSf6KXq3h8As7nbkAE%2BEiMGnloBWwxnYJckDKBnKnrSmOZynbt58YsPvqT6QHO5GJ2lG%2BZKk1MVj54O0wlvpou62nE4uonKcof9yE7yjK7O2dB%2Bw1n5vO0O%2FXB0yBqQ%2FJgH5NfYF%2FmCOifLZ%2FUhY0WdAUhDc6BfiiZ7YVq8vOF6llrSlg%2B0xbgKmC77kRvb6ie%2BNsIfsgLx3A62GVNCFTvhsx%2FJqoC2MRqtOFaLn2GxzJSKbm%2Fy5pnTk0kUQ6Ztm%2B0Yey1ogjzQWBq8vcsyNd0kGjYGA1nvZLv790is2y5e1fmtcXk48oaj97Qixo8yxRCHrugdaqErFTkFNeRdPOkwBXLY012jWwB0bj5HZv14k8UG%2FNQA%2FnRS4PUS6a%2BQ%2Bkk%2BtXEWUI4VBZrIqTvgMO7GOFmIHI2CkYiZcq%2Boz0JTHSg9%2BrglQLNq3d%2BvVufQaYlOyVAUW09EGASZ%2FLxjB%2BFekqdvobEPb9lKNGXNf7EiJ7zFSgmoVTxqS%2FV88OqL8syAG5eSIew9DiPU9DtanGQc%2BhFzRBML%2FFudEGOqUBfP9rvMS1AENyUMjrsI6yg6m8vLHcqWGSojhI%2Bt8Hd%2FU0G%2FTAgCY4%2FBUZUq5BGGDyJMvWLq6qpnCNrftqM3Ber%2B33vqFhHAjDPiUDjMcAYuFkbIr3H5%2Bn1ymZxRpnXmeEmC1Ww2Dt9DoXCn4YXnpPWLaRBAWxnKlPe08eCnPtVtviT2YaqD2s2zjkKJyfiMb0RLtaU7jbCSGaL47MKjtuTF4aZzvG&X-Amz-Signature=df1e595876ba9a8e025c456ae44f6d9a84b10d96d6f428d4d858208267378d2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
