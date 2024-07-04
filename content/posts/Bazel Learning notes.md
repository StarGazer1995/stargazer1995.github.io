---
created: 2024-07-04T01:57:00+00:00
categories:
  - Blog
tags:
  - Note
  - Notion
updated: 2024-07-04T02:13:00+00:00
date: 2024-07-04T01:57:00+00:00
title: Bazel Learning notes
id: 77875caf-8230-4c53-8c5c-9555264826d7
---

For installation and code sample, plz refer to [official documents](https://bazel.build/about/intro)。

# Project Structure

Typically, a simple bazel-based project looks like the following file structure.

```javascript
my_cpp_project/
├── WORKSPACE
├── BUILD
└── src
    ├── main.cc
    └── BUILD
```

In this project, there are files we need to know：

- a WORKSPACE file: In this project, if self-contained, we can leave it as blank. We could discuss it in the later future.
- A BUILD file: could be blank
- A folder：
  - source file
  - A BUILD file: must contain compiling instructions.

# BUILD file

In Bazel, the BUILD file contains instructions for compilation. So we need to write down instruction how we want to compile the project. Here is an example for our simple project.

```python
# src/BUILD
cc_binary(
    name = "my_cpp_app",
    srcs = ["main.cc"],
)
```

In this file, we set a compilation task named `my_cpp_app` using the `cc_binary` instruction. In this task, we specify [main.cc](http://main.cc/) as the source code of the project for compiling a binary executable file.

Alternatively, we could use an instruction, `cc_library` , for compiling a library from source. When the project becomes complex, we re-write the BUILD file like the following code.

```python
cc_binary(
    name = "my_cpp_app",
    srcs = ["main.cc"],
    deps = [":my_library"],
)
```

This deps attribute tells compiler that it should link the output of [main.cc](http://main.cc/)’s compilation to `my_library` . The colon in the deps stands means: the my_library uses the same BUILD file. More, when we want to link a library at a specific location with in the project, we can then rewrite the BUILD file.

```python
cc_binary(
    name = "my_cpp_app",
    srcs = ["main.cc"],
    deps = ["//${path_to}/my_library"],
)
```

“//” stands for the root path of workspace. Although there are many details we can discuss, we leave it to the future. Right now, we learn how to use it, and we will master it as we practice more.

# How to compile the project

Like other compilers, compiling a project is fairly simple. The instruction for compiling could be:

```shell
bazel build //src:my_cpp_app
```

---

# What if I have an external project?
