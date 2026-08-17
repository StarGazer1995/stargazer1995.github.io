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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWTHYEU4%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T043104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIHy%2FsujupSzcd7%2FZ0D7esnVorw7gqFRkimvoAJIxMwfEAiB5EeAeWEbgQ14ZwgN3AnmvryO%2F09eMPaQTou2kg03QSir%2FAwg9EAAaDDYzNzQyMzE4MzgwNSIMPDvwHAjZr9sxhDNuKtwD88eBX3PK8wr767Crk4nypSkyU2BNPOJ%2FybPQCsEbPeeok2Hl5JW6vGcTcuC%2B6AjdB2OfhnKPqPPvnB0uHOI45%2B8qrzJzNSDZ0JJYeWdL2ryQ2TTse9U%2ByQSuzrlpC7MdcZq1QI%2B3EtNflxSbwsg3ZVpX3%2FCU4jhCYroF79f6me1uMmXfU7muR9wJXMuOspw6eIjdZKnboIUKxa5wbxzvFIRy6DP%2B4L7fhuJjBCv3ly0HGxyiz4fNNyqqBLQe7JjguYpae%2FPEAdVHZCAloJKUylQYHEg1AL5tDhnv2Y9Qty322VNUVJyg68fwb3fync4DSRKr8F1tmscaRL0QrctzS%2BP7llMzydH6tKKRmjbMOC3snnNPddkhJgzhOLV%2FC5uFNJdh42q3qc6OOv5ZkTw6BJfnofrOV7q7HhEjSRkzTblaQ1aCeP6G6CZT%2FeOITDs2NdDa%2FNMS%2FIE9KRsi3k0GwJLV61GMwMc0Ba3W5alItsn2KhsMkkg%2F4Irm8hhZl50ELd75PBRXmi4ccioKvh3cr9E4bkkIjAM06GOltBRTbimfGQJVLRnU6tzVgimE0ej1Udve8yxmj5an1BW5MIbyk2SMGFYqUMtZVW5FN5k3Tw27vu%2FgT%2BIncS9UY94wiZiK1AY6pgHoHy2LSBBFUaGUTqTqzh%2Brw0ZPuXyqc%2BaclNiFimpZJsSTLOOuMBOLUy6H5TmgXoOQsTgOIT%2F6sZo2Ndn94T5HuqatrLRPhvRCIKq%2Fnd%2BVBXHM9YIN7UIpYP%2F%2BZ2%2FBJPPycgrlCcvIgxtjQ82PhI52hmOpM2smDgfsOI2n%2Bt0P16NADCfwce7GRqs3Kw1Dy6BuIGO0uCd%2B1CpIXkri5H18PR%2BpdGa0&X-Amz-Signature=eee8fbb9500389277511e647ee511426a832dfd8e4e75fc83f6620b03ce4453f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWTHYEU4%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T043104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIHy%2FsujupSzcd7%2FZ0D7esnVorw7gqFRkimvoAJIxMwfEAiB5EeAeWEbgQ14ZwgN3AnmvryO%2F09eMPaQTou2kg03QSir%2FAwg9EAAaDDYzNzQyMzE4MzgwNSIMPDvwHAjZr9sxhDNuKtwD88eBX3PK8wr767Crk4nypSkyU2BNPOJ%2FybPQCsEbPeeok2Hl5JW6vGcTcuC%2B6AjdB2OfhnKPqPPvnB0uHOI45%2B8qrzJzNSDZ0JJYeWdL2ryQ2TTse9U%2ByQSuzrlpC7MdcZq1QI%2B3EtNflxSbwsg3ZVpX3%2FCU4jhCYroF79f6me1uMmXfU7muR9wJXMuOspw6eIjdZKnboIUKxa5wbxzvFIRy6DP%2B4L7fhuJjBCv3ly0HGxyiz4fNNyqqBLQe7JjguYpae%2FPEAdVHZCAloJKUylQYHEg1AL5tDhnv2Y9Qty322VNUVJyg68fwb3fync4DSRKr8F1tmscaRL0QrctzS%2BP7llMzydH6tKKRmjbMOC3snnNPddkhJgzhOLV%2FC5uFNJdh42q3qc6OOv5ZkTw6BJfnofrOV7q7HhEjSRkzTblaQ1aCeP6G6CZT%2FeOITDs2NdDa%2FNMS%2FIE9KRsi3k0GwJLV61GMwMc0Ba3W5alItsn2KhsMkkg%2F4Irm8hhZl50ELd75PBRXmi4ccioKvh3cr9E4bkkIjAM06GOltBRTbimfGQJVLRnU6tzVgimE0ej1Udve8yxmj5an1BW5MIbyk2SMGFYqUMtZVW5FN5k3Tw27vu%2FgT%2BIncS9UY94wiZiK1AY6pgHoHy2LSBBFUaGUTqTqzh%2Brw0ZPuXyqc%2BaclNiFimpZJsSTLOOuMBOLUy6H5TmgXoOQsTgOIT%2F6sZo2Ndn94T5HuqatrLRPhvRCIKq%2Fnd%2BVBXHM9YIN7UIpYP%2F%2BZ2%2FBJPPycgrlCcvIgxtjQ82PhI52hmOpM2smDgfsOI2n%2Bt0P16NADCfwce7GRqs3Kw1Dy6BuIGO0uCd%2B1CpIXkri5H18PR%2BpdGa0&X-Amz-Signature=c340ca1d4eeefdb0412a4b05d65898e7dbdb10b5ea6d525411f7e44eb915ef98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
