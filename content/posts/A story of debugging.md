---
created: 2024-07-04T01:57:00+00:00
categories:
  - Blog
tags:
  - Problems
  - Blog
  - Note
updated: 2024-07-04T02:13:00+00:00
date: 2024-07-04T01:57:00+00:00
title: A story of debugging
cover: https://www.notion.so/images/page-cover/nasa_tim_peake_spacewalk.jpg
id: 0ae76d47-ede5-47b7-ab9f-04c1d5b0cda5
---

# Introduction

We've been experiencing an application crash on the QNX platform, which initially seemed like a common occurrence since core dumps happens. However, this issue is different. After the crash, we're unable to enter engineering mode, making it impossible to use SSH to retrieve the core file. Furthermore, the crash occurs near the application start, leaving no time to enter engineering mode when the system boots up. This page serves to document how I've dealt with this issue, which is perhaps my proudest achievement so far at the new company.

# Addressing the code

Given the limitations we face, such as the inability to retrieve the core file, use gdb for debugging, engage the engineering mode for logs, or get console prints from the application, it feels like we've been transported back to the 1960s. However, despite these challenges, I've found that a simple yet effective approach, like binary search, can still be incredibly useful in resolving the issue.

The following code demonstrates a simple pipeline.

```shell
v2x_receiver -> v2x_adapter -> other_functions[we do not modify]
```

After removing the **`v2x_adapter`** from the pipeline, the crash persists, suggesting that it occurs within the **`v2x_receiver`**. Given the rapid occurrence of the crash, I suspect it happens during the receiver's construction phase.

The structure of the `v2x_receiver` is quite simple. I will show a simple example in the following snippet.

```c++
class V2xReceiver{
public:
	V2xReceiver(){
		build_connection();
	}

	void excute(){
	// processing the data
	}
private:
	void build_connection(){
		// build a communication with antenna
		v2x_client();
	}
	V2xClient v2x_client;

};
```

I removed everything about the `v2x_client` in the receiver, and the crash disappeared. I did more tests and confirmed that the program crashed when we call v2x_client’s construction function.

Another problem rises after I have addressed the code crashes the system is that how we delay this construction function call. I moved the declaration and construction of v2x_client in the runtime function. Here I show the modified version of the code.

```c++
class V2xReceiver{
public:
	V2xReceiver(){
		build_connection();
	}

	void excute(){
	// call the construction which crash the application
		// call the construction which crash the application
		while (counter < 2000){
		V2xClient v2x_client();
		}
		counter++;
	// processing the data

	}
private:
	void build_connection(){
		// build a communication with antenna
	}
	int counter = 0;
};
```

By doing so, we have enough time to engage the engineering mode, and enable ssh function for retrieving the core dump file on our local machine.

# Core file analysis

QNX provides a toolchain that we can analyze the core dump file. I would not write details on how we use the toolchain. The important part is the core stack. The backtrace information gives a fact the program received a kill signal from the system because it attempts to construct a socket for communication with the outside.

# System log dump

Upon identifying the issue, we sought to dump the system's kernel log for further investigation. QNX offers a tool called **`slog2info`** for this purpose. Reviewing the system log, we discovered that the socket construction was being denied by the system due to the application's security policy.

# QNX privilege management

QNX employs a strict privilege management system that uses scripts to define an application's permissions. If an application violates these rules, the operating system sends a kill signal to terminate the application. These rules are stored in files with a **`.secpol`** extension.

The QNX system also provides a utility named **`secpol`** for managing privileges. I used the following script to dump the privilege specifications.

```c++
secpol -c > ${some_where_you_want}
```

I could give the application with the required privilege. And thus, the problem is solved.

# End of the story

Yes, the story is short after I have omitted some details I cannot say outside the office. But I believe this could be a good story that tells what we could do when we encountered the same issue. For myself, I am very proud for what I have done during this journey.
