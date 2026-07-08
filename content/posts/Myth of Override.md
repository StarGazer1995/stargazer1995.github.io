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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGG4U2WY%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T225500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8Dt5L3ZhhSMmk7cDpYY2gmEfRyZh2crADqTCcThyYzAIhAJ8LLiRK%2FqFRLbt%2FhkM63F2V%2Fx3Bw41kFKyFdkxHGrDQKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwz0K7TYhjbAml%2FVQwq3AOCbnPJr8g0Yi%2FuHgYSSi2gZNQR%2FZqOX67A9Q72XElhO9%2Fumjtq0dSA8Z9VdwivJ4Ou2Pyd7D21Uj2RyhVW284OdrpgYrUImNHtvU7dFfJFrUlEN68FZGmZ2JfC5L90D8AfEkY6Z2uN6Zx7DfxDnN4O5VrEIQU8J3jsiUnTN2qzAkbpWkC9Vyrnl0P27uu2j6LMMZi2yq7YgQtvbjMeUOFUy671GCjJhsp8d4r57a0d6BihmA%2FwJXAC4Kt5A6tH0pZgbWZaev1r2mI0x%2F2dqfI%2FQRSNwIRU2I1Pfy3P9q6YM12V9bF%2B5VFMF6MveIR%2ByvjA42300KyWCwmInyYzW8m5AmU0WZPfeflpiUitnyXfGKukNQqTh2KpM6G7qGfnM1AfvnEh2%2BY5u7I%2FfBJfM9BDuVf0yu0bYtdABfAv%2BmpmdE%2Bg%2Fb128%2FaV5C%2FcNyCdtrAKmJSodmwSor8EbEQshqrP%2BYFYCn92%2BHjozY6c%2BF7WUY4XPblYOGjaUeKGebetmTmipH6CqO6%2BeZgAHlPtQ5luVyc0od06bGCYDlInBDR%2FbavpdCr24BLQgwaWQFYmH%2BykTuD2fxmtPMH%2BaHw33fUAmuxoYMATIbijEGWiQX%2Fjsi06BOtyPJha3YLRvDCkibvSBjqkAYI%2Fz3LFItL1goifUFpj%2Bq5QBcg3mAXOHj0joY49gCs%2FH1W%2BCIv87GeYgzKUq4zf7R6%2Fx82LzYQCTb3YXxoxVF2g7ezj438zJ1dC%2Fos%2B8WY7QhZCmrPMlNKEMXM7MTZf5qTXt%2B9isNm5G4JK0MsRfYyEwjjmp3MHdCVPKLbfiS%2B5zC9QvzsATUGi6IQArxkVATcIk%2FzMKr4ASbdznrdcl0UBkNJq&X-Amz-Signature=9e9b4ede84273cf47612914f1c7e1d1bb6e616376f6da12118f5e86e5719da1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGG4U2WY%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T225500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8Dt5L3ZhhSMmk7cDpYY2gmEfRyZh2crADqTCcThyYzAIhAJ8LLiRK%2FqFRLbt%2FhkM63F2V%2Fx3Bw41kFKyFdkxHGrDQKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwz0K7TYhjbAml%2FVQwq3AOCbnPJr8g0Yi%2FuHgYSSi2gZNQR%2FZqOX67A9Q72XElhO9%2Fumjtq0dSA8Z9VdwivJ4Ou2Pyd7D21Uj2RyhVW284OdrpgYrUImNHtvU7dFfJFrUlEN68FZGmZ2JfC5L90D8AfEkY6Z2uN6Zx7DfxDnN4O5VrEIQU8J3jsiUnTN2qzAkbpWkC9Vyrnl0P27uu2j6LMMZi2yq7YgQtvbjMeUOFUy671GCjJhsp8d4r57a0d6BihmA%2FwJXAC4Kt5A6tH0pZgbWZaev1r2mI0x%2F2dqfI%2FQRSNwIRU2I1Pfy3P9q6YM12V9bF%2B5VFMF6MveIR%2ByvjA42300KyWCwmInyYzW8m5AmU0WZPfeflpiUitnyXfGKukNQqTh2KpM6G7qGfnM1AfvnEh2%2BY5u7I%2FfBJfM9BDuVf0yu0bYtdABfAv%2BmpmdE%2Bg%2Fb128%2FaV5C%2FcNyCdtrAKmJSodmwSor8EbEQshqrP%2BYFYCn92%2BHjozY6c%2BF7WUY4XPblYOGjaUeKGebetmTmipH6CqO6%2BeZgAHlPtQ5luVyc0od06bGCYDlInBDR%2FbavpdCr24BLQgwaWQFYmH%2BykTuD2fxmtPMH%2BaHw33fUAmuxoYMATIbijEGWiQX%2Fjsi06BOtyPJha3YLRvDCkibvSBjqkAYI%2Fz3LFItL1goifUFpj%2Bq5QBcg3mAXOHj0joY49gCs%2FH1W%2BCIv87GeYgzKUq4zf7R6%2Fx82LzYQCTb3YXxoxVF2g7ezj438zJ1dC%2Fos%2B8WY7QhZCmrPMlNKEMXM7MTZf5qTXt%2B9isNm5G4JK0MsRfYyEwjjmp3MHdCVPKLbfiS%2B5zC9QvzsATUGi6IQArxkVATcIk%2FzMKr4ASbdznrdcl0UBkNJq&X-Amz-Signature=502b431d6b981271f1f2394851c65ccec2b35d3102856a27f767a0abcfa4d09c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
