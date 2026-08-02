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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG5Z2AEE%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDFnf0g9E6NZIpaKt0sQ00D4HwW8sGQhw6Mj49oCjhubgIgJqmRjw4VAdtCHlogxGy6IEpK1tnsemy95Nr6l3EVupoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjm36bJtSjB1QzvpyrcA1fwDub5WE6%2FoQH03PcVmVuSFJEGBqwvcU8Yjr%2FdZyEtp3NZqtZ6jrU37WSQhvZjFGt%2FCYpcbIwdrl5RHO%2FrBkGbowpwVO7RdFcp%2BprPCja2C0IfkCvmUbe8uEb4iNivOevf5%2FFephxT9tcKC7plHZAKwcw0JuHALprq%2FvPUsRDfE23TlKMgz82XTmfKirpNDCsmtXyKlPEAIQ4KPa3khNRC57Su2jvLERGqcb8alVekXE9iyCSgIhY%2B4yccVBTm%2BKT6RmdbTv98S2HhXFhn10qJxJV%2FPkwsZrH%2FnnSQMB9ejyS9CRU1etphCyqpbg0PZ0ByVxXI20bZulvUXjVoRUxaJmhZSLL%2BWfRxjC%2Bv71kZzCOUx8m1OJyGecWV2z2as5luijVOpyQa1ZXHd5NKqTxvGo%2FDc2oa9APv2n47KmX2Q4C37y5VVHI%2FsCVSJ1Vg85OoWpb3ozbD798KdMnrST5rkdZvrzVHK4eLw0ljSIlYZWneMYgW6fnCGSQOgT7wza0c3aEXmJXw9ipo6eV9indqvLGsC8NpXjTGUoShQrzxIrxgOVzOWlw3Kjfp4tb90hblvOFIswfHJ4eFXVH70CV948tE3xfIxL12HAQaJSLvl3yASxfDYUevIVg4MJ%2FButMGOqUB5aOUwsNAkaiEsRsafK1j%2FDUhmNBBoBeS7y8BhXJbw%2F7a8dPj%2FzphzWO5dFHuLPM53d%2BxaIFfm%2FMhI6Yy%2BHQCg2T89Np7OKf%2F6%2FsiKHwPxK6d84mbC%2FTL3EXkIBBVC2%2FWwHn4ac0ZlvqI1qOtynm9394uKEHsiChVoWeIPF8EkE3EyBfUX9ZQCSg0WnJZHKIlrEy%2FDQiDlDgcptNd1GvsDuAgouEo&X-Amz-Signature=ab31a7b3d819a385e89f52e593b6e8fa86aafaf990dac5568b0c7e98a45437bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG5Z2AEE%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDFnf0g9E6NZIpaKt0sQ00D4HwW8sGQhw6Mj49oCjhubgIgJqmRjw4VAdtCHlogxGy6IEpK1tnsemy95Nr6l3EVupoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjm36bJtSjB1QzvpyrcA1fwDub5WE6%2FoQH03PcVmVuSFJEGBqwvcU8Yjr%2FdZyEtp3NZqtZ6jrU37WSQhvZjFGt%2FCYpcbIwdrl5RHO%2FrBkGbowpwVO7RdFcp%2BprPCja2C0IfkCvmUbe8uEb4iNivOevf5%2FFephxT9tcKC7plHZAKwcw0JuHALprq%2FvPUsRDfE23TlKMgz82XTmfKirpNDCsmtXyKlPEAIQ4KPa3khNRC57Su2jvLERGqcb8alVekXE9iyCSgIhY%2B4yccVBTm%2BKT6RmdbTv98S2HhXFhn10qJxJV%2FPkwsZrH%2FnnSQMB9ejyS9CRU1etphCyqpbg0PZ0ByVxXI20bZulvUXjVoRUxaJmhZSLL%2BWfRxjC%2Bv71kZzCOUx8m1OJyGecWV2z2as5luijVOpyQa1ZXHd5NKqTxvGo%2FDc2oa9APv2n47KmX2Q4C37y5VVHI%2FsCVSJ1Vg85OoWpb3ozbD798KdMnrST5rkdZvrzVHK4eLw0ljSIlYZWneMYgW6fnCGSQOgT7wza0c3aEXmJXw9ipo6eV9indqvLGsC8NpXjTGUoShQrzxIrxgOVzOWlw3Kjfp4tb90hblvOFIswfHJ4eFXVH70CV948tE3xfIxL12HAQaJSLvl3yASxfDYUevIVg4MJ%2FButMGOqUB5aOUwsNAkaiEsRsafK1j%2FDUhmNBBoBeS7y8BhXJbw%2F7a8dPj%2FzphzWO5dFHuLPM53d%2BxaIFfm%2FMhI6Yy%2BHQCg2T89Np7OKf%2F6%2FsiKHwPxK6d84mbC%2FTL3EXkIBBVC2%2FWwHn4ac0ZlvqI1qOtynm9394uKEHsiChVoWeIPF8EkE3EyBfUX9ZQCSg0WnJZHKIlrEy%2FDQiDlDgcptNd1GvsDuAgouEo&X-Amz-Signature=acf6193fada2b456f14c131c336d469c27b7f38c150dd1cb2ece2e7730cdf541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
