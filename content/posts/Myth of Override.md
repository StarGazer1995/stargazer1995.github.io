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

![What a joke.](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/7076b5a7-f77b-4088-89a5-4af49191dc75/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF75JXGS%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T074325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCXxMh0g3tdu8BgXvyIlUzTeNsAXQFE1VJjx6w9U9BtwIgV8NJ0OENiLrwSGYVO%2F1%2F9HU7H9J5zmGcs8%2Fq7g7qH%2FkqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPj4hIIN2qblLXgC%2BCrcA8XHjSZlQiUgX4oIe3ks80qQINE7VMl1DhFSDbJyBfWM2O69euG85lz0MTUiBQW4i6njlU2el7YbSvoUf5nbtD5%2Fecqoc3HJTroKuTCBs72a7LkCMtukeadZuEjbDhsvEBKYHMb%2Fzrp6qPwNy44X5tZyJKnRg4s3Ycz3HxyY3CfCCWshCI7xaWz%2BsNfR0SFFlWvpJbF%2FCzwQ8nPIu8tySl1U22rsIAHaQ6Kyqabt%2FdrNjyCZv8djrk1hMkBinNclbV1tYiJw48cblR5Qz4ftdDFd5bxU5AAONqV%2FuRitpdFZpqov%2FWeio2kwIlMBWJjgy68kjWTRtpRWgy%2FJpRYbfKYwyA9ANM6QRiIYIKRVRxv9qX7thni5k8yZilONyr1D8xL1Lbf5P9rAr%2FPYnk%2FoQa8kR9H8p3Q5%2FEqI1IqoeJ%2Bl8Sncwhz9son%2BYF4YpWXanUlqnTb2%2BR%2BUmYbAIn5KyP7Lup9Y0Ti1TDXuk8T7fefTMngwGrVwMpL7WEAKPqxfEyfrSMF2%2B9Sx4yCPBBnVc7cVvI%2BY9P%2BZNpX4y%2BNVd%2Fm9ds5FQvi3yntlf8vAWNWBL2yyAgPWHbeYKu2kfyDfZ6Ew6Gdjqy9JO5uVFI54uPMbX2jKGR%2FbQ01ULJ9KMITsgtIGOqUBKE8N%2BKeMCzjnuDYb7v3SHF8EJuCSkT8BvQ3CkRVaulyPqzAXMeKIgowqlIz%2BZUSHgZ0k6RQ36ZzOw5GDGvlvXmk2OrtV2eOKGlhJkGmAlGEClxWyWVUuq54%2BRnO5kOhuf8h8hWzBRopiWTtVUE1gWAF4XbAlSqbQxkT%2FzXnk8TOpj4r2vPEM%2FHpjeILqRGktOhyiQV1lQ0m%2FJnqG%2Fvbgv3g15MT0&X-Amz-Signature=e9fdb827eeefc0a82abd4b48c9834c8157805e3a39d418f9f0cd36e3f86580b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![The joke, again!](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/2529529b-7ad6-4518-8580-80a12b76db36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF75JXGS%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T074325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCXxMh0g3tdu8BgXvyIlUzTeNsAXQFE1VJjx6w9U9BtwIgV8NJ0OENiLrwSGYVO%2F1%2F9HU7H9J5zmGcs8%2Fq7g7qH%2FkqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPj4hIIN2qblLXgC%2BCrcA8XHjSZlQiUgX4oIe3ks80qQINE7VMl1DhFSDbJyBfWM2O69euG85lz0MTUiBQW4i6njlU2el7YbSvoUf5nbtD5%2Fecqoc3HJTroKuTCBs72a7LkCMtukeadZuEjbDhsvEBKYHMb%2Fzrp6qPwNy44X5tZyJKnRg4s3Ycz3HxyY3CfCCWshCI7xaWz%2BsNfR0SFFlWvpJbF%2FCzwQ8nPIu8tySl1U22rsIAHaQ6Kyqabt%2FdrNjyCZv8djrk1hMkBinNclbV1tYiJw48cblR5Qz4ftdDFd5bxU5AAONqV%2FuRitpdFZpqov%2FWeio2kwIlMBWJjgy68kjWTRtpRWgy%2FJpRYbfKYwyA9ANM6QRiIYIKRVRxv9qX7thni5k8yZilONyr1D8xL1Lbf5P9rAr%2FPYnk%2FoQa8kR9H8p3Q5%2FEqI1IqoeJ%2Bl8Sncwhz9son%2BYF4YpWXanUlqnTb2%2BR%2BUmYbAIn5KyP7Lup9Y0Ti1TDXuk8T7fefTMngwGrVwMpL7WEAKPqxfEyfrSMF2%2B9Sx4yCPBBnVc7cVvI%2BY9P%2BZNpX4y%2BNVd%2Fm9ds5FQvi3yntlf8vAWNWBL2yyAgPWHbeYKu2kfyDfZ6Ew6Gdjqy9JO5uVFI54uPMbX2jKGR%2FbQ01ULJ9KMITsgtIGOqUBKE8N%2BKeMCzjnuDYb7v3SHF8EJuCSkT8BvQ3CkRVaulyPqzAXMeKIgowqlIz%2BZUSHgZ0k6RQ36ZzOw5GDGvlvXmk2OrtV2eOKGlhJkGmAlGEClxWyWVUuq54%2BRnO5kOhuf8h8hWzBRopiWTtVUE1gWAF4XbAlSqbQxkT%2FzXnk8TOpj4r2vPEM%2FHpjeILqRGktOhyiQV1lQ0m%2FJnqG%2Fvbgv3g15MT0&X-Amz-Signature=889f13bffb55557a9b897cc1f1e96a6fca43185c96759e1639e8fa579b3bebfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Not only does it override the private virtual function, but it also changes the access level of the function in the derived class.

This seems to violate coding rules. The virtual function shouldn't be accessible by derived classes. However, it appears that the override has a higher priority than the public and private declarations. I sought clarification from ChatGPT but didn't receive a satisfactory answer. After consulting the C++ reference, I found a solution on our favorite platform, Stack Overflow.

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://en.cppreference.com/w/cpp/language/virtual#In_detail"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">en.cppreference.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://en.cppreference.com/w/cpp/language/virtual#In_detail</div></div></div></a></div></div>

It's surprising that the C++ committees have left this issue to developers, essentially telling us to 'handle it ourselves.' This approach grants too much freedom to manipulate virtual functions, potentially leading to violations of coding rules. The committees should address this to prevent such issues during development. One possible solution could be to restrict the `override` syntax to the protected level, thus providing more control and reducing the risk of unintended violations.
